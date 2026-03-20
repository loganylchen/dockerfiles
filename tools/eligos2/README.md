# ELIGOS2 Docker Image

[中文](#中文文档) | [English](#english-documentation)

ELIGOS2: Epitranscriptional Landscape Inference by Genetically Ontology-aSsigned sequencing.

---

## 中文文档

### ELIGOS2

**类别**: RNA修饰检测

#### 简介

ELIGOS2 是用于从 Nanopore 直接 RNA 测序数据中检测 RNA 修饰的工具。它基于错误特征分析方法识别修饰位点。

#### 版本信息

- **ELIGOS2**: v2.1.0 (default) - 使用 `--build-arg VERSION=<tag>` 指定版本
- **bedtools**: 2.25 (固定版本，确保 BED 文件格式兼容)
- **Python**: 3.10

#### 环境说明

此镜像使用 Conda 管理依赖，确保版本一致性：

| 工具 | 版本 | 说明 |
|------|------|------|
| ELIGOS2 | 2.1.0 | RNA 修饰检测 |
| bedtools | 2.25 | BED 文件操作 (固定版本) |
| pybedtools | latest | Python bedtools 接口 |
| pysam | latest | SAM/BAM 文件处理 |
| r-base | latest | R 统计环境 |
| rpy2 | latest | Python-R 接口 |

**重要**: bedtools 版本固定为 2.25，因为新版本可能产生不同的 BED 输出格式，导致 pybedtools 解析错误。

#### 构建

```bash
# 默认版本构建
docker build -t eligos2:2.1.0 tools/eligos2/

# 指定版本构建
docker build --build-arg VERSION=2.1.0 -t eligos2:2.1.0 tools/eligos2/
```

#### 使用方法

```bash
# 基本用法
docker run --rm -v /path/to/data:/data eligos2:2.1.0 eligos2 --help

# 运行 ELIGOS2
docker run --rm -v /path/to/data:/data eligos2:2.1.0 \
    eligos2 -i /data/input.bam -r /data/reference.fa -o /data/output
```

#### 示例

```bash
# 交互式 shell
docker run --rm -it -v $(pwd):/data eligos2:2.1.0 bash

# 在 conda 环境中运行 Python
docker run --rm -v $(pwd):/data eligos2:2.1.0 \
    bash -c "source /opt/conda/etc/profile.d/conda.sh && conda activate eligos2 && python your_script.py"
```

#### 参考资料

- [ELIGOS2 GitLab](https://gitlab.com/piroonj/eligos2)

---

## English Documentation

### ELIGOS2

**Category**: RNA Modification Detection

#### Introduction

ELIGOS2 is a tool for detecting RNA modifications from Nanopore direct RNA sequencing data. It identifies modification sites based on error signature analysis.

#### Version Information

- **ELIGOS2**: v2.1.0 (default) - use `--build-arg VERSION=<tag>` to specify
- **bedtools**: 2.25 (pinned version for BED file format compatibility)
- **Python**: 3.10

#### Environment

This image uses Conda for dependency management to ensure version consistency:

| Tool | Version | Description |
|------|---------|-------------|
| ELIGOS2 | 2.1.0 | RNA modification detection |
| bedtools | 2.25 | BED file operations (pinned version) |
| pybedtools | latest | Python bedtools interface |
| pysam | latest | SAM/BAM file processing |
| r-base | latest | R statistical environment |
| rpy2 | latest | Python-R interface |

**Important**: bedtools is pinned to version 2.25 because newer versions may produce different BED output formats, causing pybedtools parsing errors.

#### Build

```bash
# Build with default version
docker build -t eligos2:2.1.0 tools/eligos2/

# Build with specific version
docker build --build-arg VERSION=2.1.0 -t eligos2:2.1.0 tools/eligos2/
```

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data eligos2:2.1.0 eligos2 --help

# Run ELIGOS2
docker run --rm -v /path/to/data:/data eligos2:2.1.0 \
    eligos2 -i /data/input.bam -r /data/reference.fa -o /data/output
```

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data eligos2:2.1.0 bash

# Run Python in conda environment
docker run --rm -v $(pwd):/data eligos2:2.1.0 \
    bash -c "source /opt/conda/etc/profile.d/conda.sh && conda activate eligos2 && python your_script.py"
```

#### References

- [ELIGOS2 GitLab](https://gitlab.com/piroonj/eligos2)

