# gffread

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### GffRead GFF/GTF处理工具

**类别**: 基因组工具

#### 简介

用于验证、过滤和转换GFF/GTF注释文件的工具。

#### 安装

```bash
# Pull the Docker image
docker pull username/gffread:0.12.7
```

#### 可用版本

`0.12.7`, `0.12.6`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/gffread gffread --help
```

#### 参数说明

运行 `docker run --rm username/gffread gffread --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gffread bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gffread gffread [options]
```

#### 参考资料

- [http://ccb.jhu.edu/software/stringtie/gffread.shtml](http://ccb.jhu.edu/software/stringtie/gffread.shtml)


---

## English Documentation

### GffRead GFF/GTF Processing Tool

**Category**: Genomic Utilities

#### Introduction

A tool for validating, filtering, and converting GFF/GTF annotation files.

#### Installation

```bash
# Pull the Docker image
docker pull username/gffread:0.12.7
```

#### Available Versions

`0.12.7`, `0.12.6`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/gffread gffread --help
```

#### Parameters

Run `docker run --rm username/gffread gffread --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gffread bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gffread gffread [options]
```

#### References

- [http://ccb.jhu.edu/software/stringtie/gffread.shtml](http://ccb.jhu.edu/software/stringtie/gffread.shtml)
