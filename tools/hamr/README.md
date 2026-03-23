# hamr

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### hamr

**类别**: 通用

#### 简介

hamr 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/hamr:latest
```

#### 可用版本

`latest`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/hamr hamr --help
```

#### 参数说明

运行 `docker run --rm username/hamr hamr --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/hamr bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/hamr hamr [options]
```

#### 参考资料



---

## English Documentation

### hamr

**Category**: General

#### Introduction

hamr bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/hamr:latest
```

#### Available Versions

`latest`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/hamr hamr --help
```

#### Parameters

Run `docker run --rm username/hamr hamr --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/hamr bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/hamr hamr [options]
```

#### References

