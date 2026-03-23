# differr

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### differr

**类别**: 通用

#### 简介

differr 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/differr:0.2
```

#### 可用版本

`0.2`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/differr differr --help
```

#### 参数说明

运行 `docker run --rm username/differr differr --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/differr bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/differr differr [options]
```

#### 参考资料



---

## English Documentation

### differr

**Category**: General

#### Introduction

differr bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/differr:0.2
```

#### Available Versions

`0.2`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/differr differr --help
```

#### Parameters

Run `docker run --rm username/differr differr --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/differr bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/differr differr [options]
```

#### References

