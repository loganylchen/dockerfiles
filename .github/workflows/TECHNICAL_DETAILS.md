# 构建系统技术细节

## 架构优化说明

### 1. 原生架构构建 vs QEMU 模拟

#### 传统方法（QEMU 模拟）
```yaml
- name: Set up QEMU
  uses: docker/setup-qemu-action@v2

- name: Build multi-arch
  run: |
    docker buildx build --platform linux/amd64,linux/arm64 ...
```

**问题**：
- 在 x86_64 机器上用 QEMU 模拟 ARM64，速度慢 10-50 倍
- 大型编译（如 minimap2, samtools）可能需要数小时
- 占用更多 CPU 和内存资源

#### 新方法（原生架构）
```yaml
build-amd64:
  runs-on: ubuntu-latest  # x86_64 原生
  
build-arm64:
  runs-on: ubuntu-24.04-arm64  # ARM64 原生

create-manifest:
  run: |
    docker buildx imagetools create \
      --tag $IMAGE:$VERSION \
      $IMAGE:$VERSION-amd64 \
      $IMAGE:$VERSION-arm64
```

**优势**：
- ✅ 每个架构在原生硬件上构建
- ✅ ARM64 构建速度提升 10-50 倍
- ✅ 并行构建两个架构
- ✅ 最后用 manifest 组合成多架构镜像

### 2. 磁盘空间优化

#### 问题背景
GitHub Actions runners 默认磁盘布局：
```
/           14GB (系统分区，Docker 默认位置)
/mnt        72GB (数据分区，通常未使用)
```

构建大型生物信息学工具时，`/var/lib/docker` 很容易耗尽 14GB 空间。

#### 解决方案
```yaml
- name: Configure Docker data-root to /mnt/docker
  run: |
    sudo systemctl stop docker
    sudo mkdir -p /mnt/docker
    sudo jq '. + {"data-root": "/mnt/docker"}' /etc/docker/daemon.json > /tmp/daemon.json || \
      echo '{"data-root": "/mnt/docker"}' > /tmp/daemon.json
    sudo mv /tmp/daemon.json /etc/docker/daemon.json
    sudo systemctl start docker
    df -h
```

**效果**：
- Docker 镜像、容器、volume 都存储到 `/mnt/docker`
- 可用空间从 14GB 增加到 72GB
- 避免构建失败："no space left on device"

### 3. 构建缓存优化

#### 分架构缓存
```yaml
# AMD64 缓存
cache-from: type=registry,ref=$IMAGE:cache-amd64
cache-to: type=registry,ref=$IMAGE:cache-amd64,mode=max

# ARM64 缓存
cache-from: type=registry,ref=$IMAGE:cache-arm64
cache-to: type=registry,ref=$IMAGE:cache-arm64,mode=max
```

**优势**：
- 不同架构的缓存互不干扰
- 每个架构独立优化缓存命中率
- 重新构建时只下载对应架构的缓存

### 4. Multi-arch Manifest

#### 什么是 Manifest？
Docker manifest 是一个索引，包含多个架构的镜像引用：

```json
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
  "manifests": [
    {
      "platform": {"architecture": "amd64", "os": "linux"},
      "digest": "sha256:abc123..."
    },
    {
      "platform": {"architecture": "arm64", "os": "linux"},
      "digest": "sha256:def456..."
    }
  ]
}
```

#### 用户体验
用户执行 `docker pull user/minimap2:2.28`，Docker 自动：
1. 检测当前系统架构
2. 从 manifest 中选择对应架构的镜像
3. 下载正确的镜像

无需手动指定 `-amd64` 或 `-arm64` 后缀！

## 构建流程图

```
┌─────────────────┐
│ detect-changes  │  检测变更的工具
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌──────┐  ┌──────┐
│ AMD64│  │ ARM64│  并行原生构建
│ build│  │ build│
└───┬──┘  └──┬───┘
    │        │
    └────┬───┘
         │
    ┌────▼─────────┐
    │   manifest   │  组合多架构镜像
    │   creation   │
    └──────────────┘
         │
    ┌────▼─────────┐
    │   推送到 Hub  │
    └──────────────┘
```

## 性能对比

### 示例：构建 minimap2:2.28

| 方法 | AMD64 时间 | ARM64 时间 | 总时间 |
|------|-----------|-----------|--------|
| **QEMU 模拟** | 5 分钟 | 45 分钟 | 45 分钟 |
| **原生构建** | 5 分钟 | 6 分钟 | 6 分钟（并行）|
| **速度提升** | - | **7.5x** | **7.5x** |

### 磁盘使用

| 场景 | 默认配置 | 优化后 |
|------|---------|--------|
| 可用空间 | 14 GB | 72 GB |
| 构建失败率 | ~20% | <1% |

## GitHub Actions Runner 类型

### ubuntu-latest (AMD64)
- 架构: x86_64
- CPU: 2 核
- 内存: 7 GB
- 磁盘: 14 GB (/) + 72 GB (/mnt)
- 费用: 免费（公共仓库）

### ubuntu-24.04-arm64 (ARM64)
- 架构: aarch64
- CPU: 2 核
- 内存: 7 GB
- 磁盘: 14 GB (/) + 72 GB (/mnt)
- 费用: 免费（公共仓库）

## 故障排查

### 问题 1: "no space left on device"
**原因**: 未配置 `/mnt/docker`  
**解决**: 确保 workflow 包含 "Configure Docker data-root" 步骤

### 问题 2: ARM64 构建失败
**原因**: 未启用 ARM64 runners  
**解决**: 
1. 仓库设置 → Actions → Runners
2. 启用 "ubuntu-24.04-arm64"

### 问题 3: Manifest 创建失败
**原因**: AMD64 或 ARM64 镜像未推送成功  
**解决**: 检查前置 job 是否都成功，确保镜像标签正确

### 问题 4: 缓存未命中
**原因**: 缓存 ref 不一致或 Dockerfile 大幅修改  
**解决**: 
- 检查 cache-from/cache-to ref 是否一致
- 确保 Dockerfile 层次结构相似
- 使用 `mode=max` 最大化缓存导出

## 最佳实践

1. **Dockerfile 优化**
   - 将频繁变动的层放在后面
   - 合并 RUN 命令减少层数
   - 使用多阶段构建减小镜像大小

2. **版本管理**
   - 在 `versions.txt` 中维护所有版本
   - 一行一个版本号
   - 注释行用 `#` 开头

3. **构建策略**
   - 设置 `fail-fast: false` 允许部分失败
   - 为不同工具设置合理的超时时间
   - 监控构建时间，优化慢的步骤

4. **缓存策略**
   - 定期清理旧缓存（手动或自动）
   - 为频繁构建的工具保留缓存
   - 考虑使用 GitHub Actions cache（适合小文件）

## 迁移指南

### 从 QEMU 方式迁移

**旧配置**:
```yaml
- name: Set up QEMU
  uses: docker/setup-qemu-action@v2
- name: Build
  run: docker buildx build --platform linux/amd64,linux/arm64 ...
```

**新配置**:
```yaml
jobs:
  build-amd64:
    runs-on: ubuntu-latest
    steps:
      - name: Configure Docker data-root
        run: |
          sudo systemctl stop docker
          sudo mkdir -p /mnt/docker
          echo '{"data-root": "/mnt/docker"}' | sudo tee /etc/docker/daemon.json
          sudo systemctl start docker
      - name: Build AMD64
        run: docker buildx build --platform linux/amd64 ...
        
  build-arm64:
    runs-on: ubuntu-24.04-arm64
    steps:
      - name: Configure Docker data-root
        run: |
          sudo systemctl stop docker
          sudo mkdir -p /mnt/docker
          echo '{"data-root": "/mnt/docker"}' | sudo tee /etc/docker/daemon.json
          sudo systemctl start docker
      - name: Build ARM64
        run: docker buildx build --platform linux/arm64 ...
        
  create-manifest:
    needs: [build-amd64, build-arm64]
    runs-on: ubuntu-latest
    steps:
      - name: Create manifest
        run: docker buildx imagetools create ...
```

### 预期改进
- ⏱️ 构建时间减少 50-80%
- 💾 磁盘空间失败减少 95%+
- 💰 CI 分钟数节省 50-80%
