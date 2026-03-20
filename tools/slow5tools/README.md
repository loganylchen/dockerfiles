# slow5tools

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### slow5tools

**类别**: 通用

#### 简介

slow5tools 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/slow5tools:1.4.0
```

#### 可用版本

`1.4.0`, `1.3.0`, `1.2.0`, `1.1.0`, `1.0.0`, `0.9.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/slow5tools slow5tools --help
```

#### 参数说明

运行 `docker run --rm username/slow5tools slow5tools --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/slow5tools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/slow5tools slow5tools [options]
```

#### 参考资料



---

## English Documentation

### slow5tools

**Category**: General

#### Introduction

slow5tools bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/slow5tools:1.4.0
```

#### Available Versions

`1.4.0`, `1.3.0`, `1.2.0`, `1.1.0`, `1.0.0`, `0.9.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/slow5tools slow5tools --help
```

#### Parameters

Run `docker run --rm username/slow5tools slow5tools --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/slow5tools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/slow5tools slow5tools [options]
```

#### References

