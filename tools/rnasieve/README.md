# rnasieve

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### rnasieve

**类别**: 通用

#### 简介

rnasieve 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/rnasieve:latest
```

#### 可用版本

`latest`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/rnasieve rnasieve --help
```

#### 参数说明

运行 `docker run --rm username/rnasieve rnasieve --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/rnasieve bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/rnasieve rnasieve [options]
```

#### 参考资料



---

## English Documentation

### rnasieve

**Category**: General

#### Introduction

rnasieve bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/rnasieve:latest
```

#### Available Versions

`latest`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/rnasieve rnasieve --help
```

#### Parameters

Run `docker run --rm username/rnasieve rnasieve --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/rnasieve bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/rnasieve rnasieve [options]
```

#### References

