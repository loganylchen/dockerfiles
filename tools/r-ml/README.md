# r-ml

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### r-ml

**类别**: 通用

#### 简介

r-ml 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/r-ml:latest
```

#### 可用版本

`latest`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/r-ml r-ml --help
```

#### 参数说明

运行 `docker run --rm username/r-ml r-ml --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/r-ml bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/r-ml r-ml [options]
```

#### 参考资料



---

## English Documentation

### r-ml

**Category**: General

#### Introduction

r-ml bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/r-ml:latest
```

#### Available Versions

`latest`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/r-ml r-ml --help
```

#### Parameters

Run `docker run --rm username/r-ml r-ml --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/r-ml bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/r-ml r-ml [options]
```

#### References

