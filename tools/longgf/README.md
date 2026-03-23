# longgf

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### longgf

**类别**: 通用

#### 简介

longgf 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/longgf:0.1.2
```

#### 可用版本

`0.1.2`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/longgf longgf --help
```

#### 参数说明

运行 `docker run --rm username/longgf longgf --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/longgf bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/longgf longgf [options]
```

#### 参考资料



---

## English Documentation

### longgf

**Category**: General

#### Introduction

longgf bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/longgf:0.1.2
```

#### Available Versions

`0.1.2`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/longgf longgf --help
```

#### Parameters

Run `docker run --rm username/longgf longgf --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/longgf bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/longgf longgf [options]
```

#### References

