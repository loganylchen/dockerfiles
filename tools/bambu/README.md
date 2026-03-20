# bambu

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### bambu

**类别**: 通用

#### 简介

bambu 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/bambu:3.4.0
```

#### 可用版本

`3.4.0`, `3.2.6`, `3.0.8`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/bambu bambu --help
```

#### 参数说明

运行 `docker run --rm username/bambu bambu --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bambu bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bambu bambu [options]
```

#### 参考资料



---

## English Documentation

### bambu

**Category**: General

#### Introduction

bambu bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/bambu:3.4.0
```

#### Available Versions

`3.4.0`, `3.2.6`, `3.0.8`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/bambu bambu --help
```

#### Parameters

Run `docker run --rm username/bambu bambu --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bambu bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bambu bambu [options]
```

#### References

