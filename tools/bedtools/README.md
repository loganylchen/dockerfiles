# bedtools

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### BEDTools 基因组算术工具集

**类别**: 基因组工具

#### 简介

用于基因组算术运算的强大工具集，支持BED、BAM、VCF等格式的操作。

#### 安装

```bash
# Pull the Docker image
docker pull username/bedtools:2.31.1
```

#### 可用版本

`2.31.1`, `2.31.0`, `2.30.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/bedtools bedtools --help
```

#### 参数说明

运行 `docker run --rm username/bedtools bedtools --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bedtools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bedtools bedtools [options]
```

#### 参考资料

- [https://bedtools.readthedocs.io/](https://bedtools.readthedocs.io/)
- Quinlan, A.R. & Hall, I.M. (2010). Bioinformatics, 26(6), 841-842.


---

## English Documentation

### BEDTools Genomic Arithmetic Suite

**Category**: Genomic Utilities

#### Introduction

A powerful toolset for genomic arithmetic operations on BED, BAM, VCF and other genomic file formats.

#### Installation

```bash
# Pull the Docker image
docker pull username/bedtools:2.31.1
```

#### Available Versions

`2.31.1`, `2.31.0`, `2.30.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/bedtools bedtools --help
```

#### Parameters

Run `docker run --rm username/bedtools bedtools --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bedtools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bedtools bedtools [options]
```

#### References

- [https://bedtools.readthedocs.io/](https://bedtools.readthedocs.io/)
- Quinlan, A.R. & Hall, I.M. (2010). Bioinformatics, 26(6), 841-842.
