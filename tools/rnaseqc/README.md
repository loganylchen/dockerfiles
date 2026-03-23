# rnaseqc

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### rnaseqc

**类别**: 通用

#### 简介

rnaseqc 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/rnaseqc:2.4.2
```

#### 可用版本

`2.4.2`, `2.4.1`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/rnaseqc rnaseqc --help
```

#### 参数说明

运行 `docker run --rm username/rnaseqc rnaseqc --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/rnaseqc bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/rnaseqc rnaseqc [options]
```

#### 参考资料



---

## English Documentation

### rnaseqc

**Category**: General

#### Introduction

rnaseqc bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/rnaseqc:2.4.2
```

#### Available Versions

`2.4.2`, `2.4.1`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/rnaseqc rnaseqc --help
```

#### Parameters

Run `docker run --rm username/rnaseqc rnaseqc --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/rnaseqc bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/rnaseqc rnaseqc [options]
```

#### References

