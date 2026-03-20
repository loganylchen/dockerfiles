# wgcna

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### wgcna

**类别**: 通用

#### 简介

wgcna 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/wgcna:1.73
```

#### 可用版本

`1.73`, `1.72_5`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/wgcna wgcna --help
```

#### 参数说明

运行 `docker run --rm username/wgcna wgcna --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/wgcna bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/wgcna wgcna [options]
```

#### 参考资料



---

## English Documentation

### wgcna

**Category**: General

#### Introduction

wgcna bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/wgcna:1.73
```

#### Available Versions

`1.73`, `1.72_5`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/wgcna wgcna --help
```

#### Parameters

Run `docker run --rm username/wgcna wgcna --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/wgcna bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/wgcna wgcna [options]
```

#### References

