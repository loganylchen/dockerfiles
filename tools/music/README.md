# music

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### music

**类别**: 通用

#### 简介

music 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/music:latest
```

#### 可用版本

`latest`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/music music --help
```

#### 参数说明

运行 `docker run --rm username/music music --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/music bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/music music [options]
```

#### 参考资料



---

## English Documentation

### music

**Category**: General

#### Introduction

music bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/music:latest
```

#### Available Versions

`latest`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/music music --help
```

#### Parameters

Run `docker run --rm username/music music --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/music bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/music music [options]
```

#### References

