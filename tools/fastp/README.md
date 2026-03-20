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
# Quality control
docker run --rm -v /path/to/data:/data username/fastp fastp -i input.fq -o output.html
```

#### 参数说明

运行 `docker run --rm username/fastp fastp --help` 查看完整参数列表。

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
# Quality control
docker run --rm -v /path/to/data:/data username/fastp fastp -i input.fq -o output.html
```

#### Parameters

Run `docker run --rm username/fastp fastp --help` to see the full parameter list.

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
