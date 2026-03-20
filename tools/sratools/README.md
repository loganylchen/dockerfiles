# sratools

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### SRA Toolkit 序列数据下载工具

**类别**: 数据下载

#### 简介

用于从NCBI序列读取存档(SRA)下载和处理高通量测序数据的工具集。

#### 安装

```bash
# Pull the Docker image
docker pull username/sratools:3.1.1
```

#### 可用版本

`3.1.1`, `3.0.10`, `3.0.7`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/sratools sratools --help
```

#### 参数说明

运行 `docker run --rm username/sratools sratools --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/sratools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/sratools sratools [options]
```

#### 参考资料

- [https://github.com/ncbi/sra-tools](https://github.com/ncbi/sra-tools)


---

## English Documentation

### SRA Toolkit Sequence Data Download Tools

**Category**: Data Download

#### Introduction

Tools for downloading and processing high-throughput sequencing data from NCBI Sequence Read Archive.

#### Installation

```bash
# Pull the Docker image
docker pull username/sratools:3.1.1
```

#### Available Versions

`3.1.1`, `3.0.10`, `3.0.7`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/sratools sratools --help
```

#### Parameters

Run `docker run --rm username/sratools sratools --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/sratools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/sratools sratools [options]
```

#### References

- [https://github.com/ncbi/sra-tools](https://github.com/ncbi/sra-tools)
