# eligos2

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### eligos2

**类别**: 通用

#### 简介

eligos2 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/eligos2:2.1.0
```

#### 可用版本

`2.1.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/eligos2 eligos2 --help
```

#### 参数说明

运行 `docker run --rm username/eligos2 eligos2 --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/eligos2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/eligos2 eligos2 [options]
```

#### 参考资料



---

## English Documentation

### eligos2

**Category**: General

#### Introduction

eligos2 bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/eligos2:2.1.0
```

#### Available Versions

`2.1.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/eligos2 eligos2 --help
```

#### Parameters

Run `docker run --rm username/eligos2 eligos2 --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/eligos2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/eligos2 eligos2 [options]
```

#### References

