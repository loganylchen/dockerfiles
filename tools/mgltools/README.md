# mgltools

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### mgltools

**类别**: 通用

#### 简介

mgltools 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/mgltools:1.5.7
```

#### 可用版本

`1.5.7`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/mgltools mgltools --help
```

#### 参数说明

运行 `docker run --rm username/mgltools mgltools --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/mgltools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/mgltools mgltools [options]
```

#### 参考资料



---

## English Documentation

### mgltools

**Category**: General

#### Introduction

mgltools bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/mgltools:1.5.7
```

#### Available Versions

`1.5.7`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/mgltools mgltools --help
```

#### Parameters

Run `docker run --rm username/mgltools mgltools --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/mgltools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/mgltools mgltools [options]
```

#### References

