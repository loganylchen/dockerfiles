# 并行构建说明

## 🚀 并行构建优化

### 改进前（顺序构建）
```yaml
# 每个工具的版本按顺序构建
for version in 2.28 2.27 2.26; do
  docker build ... $version
done
```

**问题**：
- minimap2:2.28 → 6 分钟
- minimap2:2.27 → 6 分钟  
- minimap2:2.26 → 6 分钟
- **总时间：18 分钟**

### 改进后（并行构建）
```yaml
# 使用 GitHub Actions matrix 并行构建
strategy:
  matrix:
    include:
      - {tool: minimap2, version: 2.28}
      - {tool: minimap2, version: 2.27}
      - {tool: minimap2, version: 2.26}
  max-parallel: 10  # 最多同时 10 个任务
```

**效果**：
- minimap2:2.28 ┐
- minimap2:2.27 ├─ 同时进行
- minimap2:2.26 ┘
- **总时间：6 分钟**

**速度提升：3x！**

---

## 📊 性能对比

### 单工具多版本

| 版本数 | 顺序构建 | 并行构建 | 加速比 |
|--------|---------|---------|--------|
| 3 个版本 | 18 分钟 | 6 分钟 | **3x** |
| 5 个版本 | 30 分钟 | 6 分钟 | **5x** |
| 10 个版本 | 60 分钟 | 6 分钟 | **10x** |

### 多工具同时更新

假设更新 3 个工具，每个 3 个版本：

| 方案 | 时间 | 说明 |
|------|------|------|
| 顺序构建 | 54 分钟 | 3 工具 × 3 版本 × 6 分钟 |
| 工具级并行 | 18 分钟 | 3 工具并行，版本顺序 |
| **版本级并行** | **6 分钟** | 9 个任务完全并行 |

**速度提升：9x！**

---

## 🔧 技术实现

### 动态矩阵生成

```bash
# 步骤 1: 检测变更的工具
tools = ["minimap2", "salmon"]

# 步骤 2: 读取每个工具的 versions.txt
minimap2/versions.txt: 2.28, 2.27, 2.26
salmon/versions.txt: 1.10.3, 1.10.2

# 步骤 3: 生成组合矩阵
matrix = [
  {tool: minimap2, version: 2.28},
  {tool: minimap2, version: 2.27},
  {tool: minimap2, version: 2.26},
  {tool: salmon, version: 1.10.3},
  {tool: salmon, version: 1.10.2}
]

# 步骤 4: GitHub Actions 并行执行 5 个任务
```

### Workflow 结构

```yaml
jobs:
  detect-changes:
    # 1. 检测变更的工具
    # 2. 读取 versions.txt
    # 3. 生成动态矩阵
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}

  build:
    needs: detect-changes
    strategy:
      matrix: ${{ fromJSON(needs.detect-changes.outputs.matrix) }}
      fail-fast: false
      # 不限制并行数，让 GitHub Actions 自动管理
    
    steps:
      - name: Build ${{ matrix.tool }}:${{ matrix.version }}
        # 每个版本独立构建
```

---

## 💡 并行构建优势

### 1. 时间效率
- **理论加速比 = 版本数**
- 3 个版本 → 3x 加速
- 10 个版本 → 10x 加速

### 2. 独立失败处理
```yaml
fail-fast: false  # 一个失败不影响其他
```

**好处**：
- minimap2:2.28 失败 ❌
- minimap2:2.27 成功 ✅
- minimap2:2.26 成功 ✅

部分成功总比全部失败好！

### 3. 缓存共享
```yaml
cache-from: type=registry,ref=$USER/minimap2:cache
cache-to: type=registry,ref=$USER/minimap2:cache
```

**效果**：
- 第一个版本构建较慢（6 分钟）
- 后续版本利用缓存（2-3 分钟）
- 并行时自动共享缓存

---

## 🎯 实际使用场景

### 场景 1: 发布新版本
```bash
# 添加新版本
echo "2.29" >> tools/minimap2/versions.txt
git push

# 只构建新版本（如果其他版本已存在）
# GitHub Actions 自动检测并只构建 2.29
```

### 场景 2: 批量重建
```bash
# 修改 Dockerfile
vim tools/minimap2/Dockerfile
git push

# 并行重建所有版本
# 3 个版本同时构建，总时间 = 单个版本的时间
```

### 场景 3: 多工具更新
```bash
# 同时更新多个工具
echo "2.29" >> tools/minimap2/versions.txt
echo "1.10.4" >> tools/salmon/versions.txt
git push

# 所有版本完全并行
# minimap2:2.29, salmon:1.10.4 同时构建
```

---

## 📈 GitHub Actions 并发限制

### 免费账户
- **公共仓库**: 20 个并发任务
- **私有仓库**: 5 个并发任务

### 付费账户
- 可配置更高的并发数
- 企业账户可达 180 个并发

### 我们的策略
```yaml
# 不设置 max-parallel，让 GitHub 自动管理
strategy:
  matrix: ${{ fromJSON(...) }}
  fail-fast: false
  # 自动使用账户的最大并发数
```

---

## 🔍 监控并行构建

### GitHub Actions 界面

```
✓ detect-changes  (10s)
├─ ✓ build (minimap2:2.28)  [6m 20s]
├─ ✓ build (minimap2:2.27)  [6m 15s]
├─ ✓ build (minimap2:2.26)  [6m 18s]
├─ ✓ build (salmon:1.10.3)  [4m 50s]
└─ ✓ build (salmon:1.10.2)  [4m 48s]

Total: 6m 30s (vs 32m 顺序构建)
```

### 日志检查
每个任务有独立的日志：
```
Actions → Workflow run → 展开 "build (minimap2:2.28)"
```

---

## ⚙️ 可选配置

### 限制并行数
如果担心资源争抢，可以限制：

```yaml
strategy:
  matrix: ${{ fromJSON(...) }}
  max-parallel: 5  # 最多同时 5 个
```

### 为不同工具设置优先级
```yaml
# 先构建重要工具
jobs:
  build-critical:
    # minimap2, salmon
  
  build-others:
    needs: build-critical
    # 其他工具
```

---

## 🎁 额外好处

### 1. 更快的反馈
- 6 分钟知道所有结果
- vs 18 分钟等待顺序完成

### 2. 更好的资源利用
- 充分利用 GitHub Actions 并发能力
- 不浪费空闲的 runners

### 3. 更灵活的失败处理
- 部分失败不阻塞其他构建
- 可以选择性重新触发失败的版本

---

## 🚀 最终效果

### 时间节省
```
单工具 3 版本:  18分钟 → 6分钟   (节省 67%)
单工具 5 版本:  30分钟 → 6分钟   (节省 80%)
双工具 6 版本:  36分钟 → 6分钟   (节省 83%)
三工具 9 版本:  54分钟 → 6分钟   (节省 89%)
```

### 用户体验
- ✅ 更快的构建完成
- ✅ 更及时的反馈
- ✅ 更高的构建成功率（部分失败可接受）
- ✅ 更好的 CI 资源利用

---

**总结：并行构建让多版本构建时间从线性增长变为常数时间！** 🚀
