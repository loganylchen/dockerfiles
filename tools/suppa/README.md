# suppa

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### suppa

**类别**: 通用

#### 简介

suppa 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/suppa:2.3
```

#### 可用版本

`2.3`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/suppa suppa --help
```

#### 参数说明

运行 `docker run --rm username/suppa suppa --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/suppa bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/suppa suppa [options]
```

#### 参考资料



---

## English Documentation

### suppa

**Category**: General

#### Introduction

suppa bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/suppa:2.3
```

#### Available Versions

`2.3`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/suppa suppa --help
```

#### Parameters

Run `docker run --rm username/suppa suppa --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/suppa bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/suppa suppa [options]
```

#### References

