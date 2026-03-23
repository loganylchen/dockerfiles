# epinano

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### epinano

**类别**: 通用

#### 简介

epinano 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/epinano:1.2.5
```

#### 可用版本

`1.2.5`, `1.2.3`, `1.2.2`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/epinano epinano --help
```

#### 参数说明

运行 `docker run --rm username/epinano epinano --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/epinano bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/epinano epinano [options]
```

#### 参考资料



---

## English Documentation

### epinano

**Category**: General

#### Introduction

epinano bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/epinano:1.2.5
```

#### Available Versions

`1.2.5`, `1.2.3`, `1.2.2`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/epinano epinano --help
```

#### Parameters

Run `docker run --rm username/epinano epinano --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/epinano bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/epinano epinano [options]
```

#### References

