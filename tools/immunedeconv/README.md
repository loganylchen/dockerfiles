# immunedeconv

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### immunedeconv

**类别**: 通用

#### 简介

immunedeconv 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/immunedeconv:2.1.0
```

#### 可用版本

`2.1.0`, `2.0.3`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/immunedeconv immunedeconv --help
```

#### 参数说明

运行 `docker run --rm username/immunedeconv immunedeconv --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/immunedeconv bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/immunedeconv immunedeconv [options]
```

#### 参考资料



---

## English Documentation

### immunedeconv

**Category**: General

#### Introduction

immunedeconv bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/immunedeconv:2.1.0
```

#### Available Versions

`2.1.0`, `2.0.3`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/immunedeconv immunedeconv --help
```

#### Parameters

Run `docker run --rm username/immunedeconv immunedeconv --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/immunedeconv bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/immunedeconv immunedeconv [options]
```

#### References

