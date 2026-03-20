# rmats

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### rmats

**类别**: 通用

#### 简介

rmats 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/rmats:4.3.0
```

#### 可用版本

`4.3.0`, `4.2.0`, `4.1.2`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/rmats rmats --help
```

#### 参数说明

运行 `docker run --rm username/rmats rmats --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/rmats bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/rmats rmats [options]
```

#### 参考资料



---

## English Documentation

### rmats

**Category**: General

#### Introduction

rmats bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/rmats:4.3.0
```

#### Available Versions

`4.3.0`, `4.2.0`, `4.1.2`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/rmats rmats --help
```

#### Parameters

Run `docker run --rm username/rmats rmats --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/rmats bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/rmats rmats [options]
```

#### References

