# bedops

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### BEDOPS 高性能基因组操作工具

**类别**: 基因组工具

#### 简介

高性能基因组数据操作工具集，针对大规模基因组数据分析优化。

#### 安装

```bash
# Pull the Docker image
docker pull username/bedops:2.4.41
```

#### 可用版本

`2.4.41`, `2.4.40`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/bedops bedops --help
```

#### 参数说明

运行 `docker run --rm username/bedops bedops --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bedops bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bedops bedops [options]
```

#### 参考资料

- [https://bedops.readthedocs.io/](https://bedops.readthedocs.io/)


---

## English Documentation

### BEDOPS High-Performance Genomic Operations

**Category**: Genomic Utilities

#### Introduction

High-performance genomic data operations suite optimized for large-scale genomic data analysis.

#### Installation

```bash
# Pull the Docker image
docker pull username/bedops:2.4.41
```

#### Available Versions

`2.4.41`, `2.4.40`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/bedops bedops --help
```

#### Parameters

Run `docker run --rm username/bedops bedops --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bedops bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bedops bedops [options]
```

#### References

- [https://bedops.readthedocs.io/](https://bedops.readthedocs.io/)
