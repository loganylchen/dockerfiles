# fastp

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### fastp 快速质控工具

**类别**: 质量控制

#### 简介

超快速的FASTQ文件质控和预处理工具，支持过滤、修剪、质量检测等功能。

#### 安装

```bash
# Pull the Docker image
docker pull username/fastp:0.24.0
```

#### 可用版本

`0.24.0`, `0.23.2`

#### 使用方法

```bash
# 单端数据质控
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i input.fq -o output.fq -h report.html

# 双端数据质控
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i R1.fq -I R2.fq -o R1.clean.fq -O R2.clean.fq -h report.html

# 质量过滤
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i input.fq -o output.fq -q 20 -u 30 -n 5 -h report.html

# 修剪低质量碱基
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i input.fq -o output.fq --cut_front --cut_tail -h report.html
```

#### 主要参数

| 参数 | 说明 |
|------|------|
| `-i, -I` | 输入文件（单端/双端） |
| `-o, -O` | 输出文件（单端/双端） |
| `-h` | HTML 报告 |
| `-j` | JSON 报告 |
| `-q` | 质量值阈值 |
| `-u` | 不合格碱基比例限制 |
| `-n` | N 碱基数限制 |
| `-w` | 线程数 |
| `--detect_adapter_for_pe` | 自动检测 adapter |

#### 常见问题

**Q: 如何设置质量过滤参数？**
A: `-q 20` 表示保留质量值≥20 的碱基，`-u 30` 表示如果超过30%碱基不合格则丢弃整个 read。

**Q: 输出的 HTML 报告包含什么？**
A: 包含质量分布、GC 含量、序列长度分布、adapter 检测等全面的 QC 信息。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/fastp bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/fastp fastp [options]
```

#### 参考资料

- [https://github.com/OpenGene/fastp](https://github.com/OpenGene/fastp)
- Chen, S. et al. (2018). iMeta, e20.


---

## English Documentation

### fastp Fast Quality Control Tool

**Category**: Quality Control

#### Introduction

Ultra-fast all-in-one FASTQ preprocessor with quality control, filtering, and trimming.

#### Installation

```bash
# Pull the Docker image
docker pull username/fastp:0.24.0
```

#### Available Versions

`0.24.0`, `0.23.2`

#### Usage

```bash
# Single-end QC
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i input.fq -o output.fq -h report.html

# Paired-end QC
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i R1.fq -I R2.fq -o R1.clean.fq -O R2.clean.fq -h report.html

# Quality filtering
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i input.fq -o output.fq -q 20 -u 30 -n 5 -h report.html

# Trim low quality bases
docker run --rm -v /path/to/data:/data username/fastp \
    fastp -i input.fq -o output.fq --cut_front --cut_tail -h report.html
```

#### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `-i, -I` | Input files (single/paired) |
| `-o, -O` | Output files (single/paired) |
| `-h` | HTML report |
| `-j` | JSON report |
| `-q` | Quality threshold |
| `-u` | Unqualified base percent limit |
| `-n` | N base limit |
| `-w` | Number of threads |
| `--detect_adapter_for_pe` | Auto detect adapter |

#### FAQ

**Q: How to set quality filtering parameters?**
A: `-q 20` keeps bases with quality≥20, `-u 30` discards reads if >30% bases fail.

**Q: What does the HTML report contain?**
A: Quality distribution, GC content, sequence length, adapter detection, and comprehensive QC metrics.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/fastp bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/fastp fastp [options]
```

#### References

- [https://github.com/OpenGene/fastp](https://github.com/OpenGene/fastp)
- Chen, S. et al. (2018). iMeta, e20.
