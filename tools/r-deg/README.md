# r-deg

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### r-deg

**类别**: 通用

#### 简介

r-deg 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/r-deg:latest
```

#### 可用版本

`latest`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/r-deg r-deg --help
```

#### 参数说明

运行 `docker run --rm username/r-deg r-deg --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/r-deg bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/r-deg r-deg [options]
```

#### 参考资料



---

## English Documentation

### r-deg

**Category**: General

#### Introduction

r-deg bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/r-deg:latest
```

#### Available Versions

`latest`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/r-deg r-deg --help
```

#### Parameters

Run `docker run --rm username/r-deg r-deg --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/r-deg bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/r-deg r-deg [options]
```

#### References

