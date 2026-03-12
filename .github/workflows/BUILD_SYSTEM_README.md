# Universal Tools Build System

这个仓库提供了**三种**方式来构建 Docker 工具镜像（仅 AMD64 架构）。

## ⚡ 性能优化

### 1. 磁盘空间优化
- 自动将 Docker data-root 从 `/var/lib/docker` 迁移到 `/mnt/docker`
- `/mnt` 挂载点通常有更大的磁盘空间
- 避免构建大型镜像时的磁盘空间不足问题
- 可用空间：14GB → 72GB

### 2. 架构选择
- **仅构建 AMD64**: 简化配置，加快构建速度
- ARM64 使用场景较少，按需可以单独添加

---

## 方案 1: 自动构建（推荐）⭐

使用 `tools_auto_build.yaml` - **一个 workflow 自动处理所有 tools**

### 工作原理：
- 当 `tools/` 目录下任何文件变更时自动触发
- 自动检测哪些工具被修改
- 读取每个工具目录下的 `versions.txt` 来确定要构建的版本
- 并行构建所有变更的工具

### 使用方法：
1. 在工具目录下创建 `versions.txt`：
```bash
tools/minimap2/versions.txt
```

内容：
```
2.28
2.27
2.26
```

2. 修改 Dockerfile 或工具文件，提交即可自动构建
3. 也可以手动触发并指定特定工具：
   - 在 GitHub Actions 界面点击 "Run workflow"
   - 输入工具名（如 `minimap2`）

### 优点：
✅ 零配置 - 新工具只需添加 `versions.txt`  
✅ 自动检测变更  
✅ 并行构建多个工具  
✅ 支持手动触发特定工具  
✅ **自动配置大磁盘空间（/mnt/docker）**  
✅ **AMD64 原生构建，速度快**  

### 构建流程：
1. **detect-changes**: 检测哪些工具被修改
2. **build**: 在 ubuntu-latest 上构建 AMD64 镜像并推送

---

## 方案 2: 可重用 Workflow

使用 `tools_build_reusable.yaml` - 创建简化的单工具 workflow

### 使用方法：
创建简化的工具 workflow（如 `tools_minimap2_build.yaml`）：

```yaml
name: minimap2

on:
  push:
    paths:
      - 'tools/minimap2/**'
  workflow_dispatch:

jobs:
  build:
    uses: ./.github/workflows/tools_build_reusable.yaml
    with:
      tool_name: minimap2
      versions: '["2.28", "2.27", "2.26"]'
    secrets:
      DH_USER: ${{ secrets.DH_USER }}
      DH_TOKEN: ${{ secrets.DH_TOKEN }}
```

### 优点：
✅ 每个工具独立触发  
✅ 配置集中管理  
✅ 易于理解和调试  
✅ **自动配置大磁盘空间**  

---

## 方案 3: 传统独立 Workflow（现有方式）

每个工具有完整独立的 workflow 文件

### 优点：
✅ 完全独立，互不干扰  
✅ 最大灵活性  

### 缺点：
❌ 代码重复  
❌ 维护成本高  
❌ 需要为每个新工具创建完整 workflow  

---

## 推荐迁移路径

### 立即使用方案 1（自动构建）：
```bash
# 1. 为所有工具添加 versions.txt
for tool in tools/*/; do
  tool_name=$(basename "$tool")
  # 从现有 workflow 中提取版本号
  grep -A 20 "matrix:" .github/workflows/tools_${tool_name}_build.yaml | \
    grep "^ *- " | sed 's/^ *- //' > "$tool/versions.txt"
done

# 2. 提交变更
git add tools/*/versions.txt
git commit -m "Add versions.txt for auto build"
git push

# 3. 启用 tools_auto_build.yaml（已创建）
# 现在所有工具都会自动构建！
```

### 可选：保留现有 workflow 作为备份
旧的独立 workflow 和新的自动构建可以共存，逐步迁移。

---

## 示例目录结构

```
dockerfiles/
├── .github/workflows/
│   ├── tools_auto_build.yaml         # 方案1：自动构建所有工具
│   ├── tools_build_reusable.yaml     # 方案2：可重用模板
│   ├── tools_minimap2_build.yaml     # 方案3：传统方式（可选保留）
│   └── tools_salmon_build.yaml       # 方案3：传统方式（可选保留）
└── tools/
    ├── minimap2/
    │   ├── Dockerfile
    │   └── versions.txt               # 2.28, 2.27, 2.26
    ├── salmon/
    │   ├── Dockerfile
    │   └── versions.txt               # 1.10.3, 1.10.2, ...
    └── fastp/
        ├── Dockerfile
        └── versions.txt               # 0.24.0, 0.23.4
```

---

## 对比总结

| 特性 | 方案1：自动构建 | 方案2：可重用 | 方案3：传统 |
|------|----------------|--------------|------------|
| Workflow 数量 | 1 个 | 1 通用 + N 简化 | N 个完整 |
| 配置位置 | versions.txt | workflow yaml | workflow yaml |
| 新增工具成本 | 只需 versions.txt | 需要简化 yaml | 需要完整 yaml |
| 自动检测变更 | ✅ | ❌ | ❌ |
| 独立触发 | ✅ (手动) | ✅ | ✅ |
| 架构支持 | AMD64 | AMD64 | AMD64 |
| 维护成本 | 极低 | 低 | 高 |
| 推荐度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
