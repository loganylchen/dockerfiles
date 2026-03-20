# estimate

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### estimate

**类别**: 通用

#### 简介

estimate 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/estimate:1.0.13
```

#### 可用版本

`1.0.13`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/estimate estimate --help
```

#### 参数说明

运行 `docker run --rm username/estimate estimate --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/estimate bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/estimate estimate [options]
```

#### 参考资料



---

## English Documentation

### estimate

**Category**: General

#### Introduction

estimate bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/estimate:1.0.13
```

#### Available Versions

`1.0.13`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/estimate estimate --help
```

#### Parameters

Run `docker run --rm username/estimate estimate --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/estimate bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/estimate estimate [options]
```

#### References

