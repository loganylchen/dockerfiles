# xpore

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### xpore

**类别**: 通用

#### 简介

xpore 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/xpore:2.1
```

#### 可用版本

`2.1`, `2.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/xpore xpore --help
```

#### 参数说明

运行 `docker run --rm username/xpore xpore --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/xpore bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/xpore xpore [options]
```

#### 参考资料



---

## English Documentation

### xpore

**Category**: General

#### Introduction

xpore bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/xpore:2.1
```

#### Available Versions

`2.1`, `2.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/xpore xpore --help
```

#### Parameters

Run `docker run --rm username/xpore xpore --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/xpore bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/xpore xpore [options]
```

#### References

