# genion

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### genion

**类别**: 通用

#### 简介

genion 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/genion:1.1.1
```

#### 可用版本

`1.1.1`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/genion genion --help
```

#### 参数说明

运行 `docker run --rm username/genion genion --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/genion bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/genion genion [options]
```

#### 参考资料



---

## English Documentation

### genion

**Category**: General

#### Introduction

genion bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/genion:1.1.1
```

#### Available Versions

`1.1.1`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/genion genion --help
```

#### Parameters

Run `docker run --rm username/genion genion --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/genion bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/genion genion [options]
```

#### References

