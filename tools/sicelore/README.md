# sicelore

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### sicelore

**类别**: 通用

#### 简介

sicelore 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/sicelore:latest
```

#### 可用版本

`latest`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/sicelore sicelore --help
```

#### 参数说明

运行 `docker run --rm username/sicelore sicelore --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/sicelore bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/sicelore sicelore [options]
```

#### 参考资料



---

## English Documentation

### sicelore

**Category**: General

#### Introduction

sicelore bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/sicelore:latest
```

#### Available Versions

`latest`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/sicelore sicelore --help
```

#### Parameters

Run `docker run --rm username/sicelore sicelore --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/sicelore bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/sicelore sicelore [options]
```

#### References

