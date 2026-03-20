# gffcompare

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### GffCompare 注释比较工具

**类别**: RNA-seq分析

#### 简介

用于比较和评估转录本组装结果与参考注释的工具。

#### 安装

```bash
# Pull the Docker image
docker pull username/gffcompare:0.12.10
```

#### 可用版本

`0.12.10`, `0.12.9`, `0.12.6`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/gffcompare gffcompare --help
```

#### 参数说明

运行 `docker run --rm username/gffcompare gffcompare --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gffcompare bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gffcompare gffcompare [options]
```

#### 参考资料

- [https://ccb.jhu.edu/software/stringtie/gffcompare.shtml](https://ccb.jhu.edu/software/stringtie/gffcompare.shtml)


---

## English Documentation

### GffCompare Annotation Comparison Tool

**Category**: RNA-seq Analysis

#### Introduction

Compare and evaluate transcript assemblies against reference annotations.

#### Installation

```bash
# Pull the Docker image
docker pull username/gffcompare:0.12.10
```

#### Available Versions

`0.12.10`, `0.12.9`, `0.12.6`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/gffcompare gffcompare --help
```

#### Parameters

Run `docker run --rm username/gffcompare gffcompare --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gffcompare bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gffcompare gffcompare [options]
```

#### References

- [https://ccb.jhu.edu/software/stringtie/gffcompare.shtml](https://ccb.jhu.edu/software/stringtie/gffcompare.shtml)
