# flair

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### flair

**类别**: 通用

#### 简介

flair 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/flair:2.0.0
```

#### 可用版本

`2.0.0`, `1.7.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/flair flair --help
```

#### 参数说明

运行 `docker run --rm username/flair flair --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/flair bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/flair flair [options]
```

#### 参考资料



---

## English Documentation

### flair

**Category**: General

#### Introduction

flair bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/flair:2.0.0
```

#### Available Versions

`2.0.0`, `1.7.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/flair flair --help
```

#### Parameters

Run `docker run --rm username/flair flair --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/flair bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/flair flair [options]
```

#### References

