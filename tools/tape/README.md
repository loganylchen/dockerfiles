# tape

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### tape

**类别**: 通用

#### 简介

tape 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/tape:0.4.0
```

#### 可用版本

`0.4.0`, `0.3.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/tape tape --help
```

#### 参数说明

运行 `docker run --rm username/tape tape --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/tape bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/tape tape [options]
```

#### 参考资料



---

## English Documentation

### tape

**Category**: General

#### Introduction

tape bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/tape:0.4.0
```

#### Available Versions

`0.4.0`, `0.3.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/tape tape --help
```

#### Parameters

Run `docker run --rm username/tape tape --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/tape bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/tape tape [options]
```

#### References

