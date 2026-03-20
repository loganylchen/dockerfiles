# drummer

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### drummer

**类别**: 通用

#### 简介

drummer 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/drummer:dd0ccc81
```

#### 可用版本

`dd0ccc81`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/drummer drummer --help
```

#### 参数说明

运行 `docker run --rm username/drummer drummer --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/drummer bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/drummer drummer [options]
```

#### 参考资料



---

## English Documentation

### drummer

**Category**: General

#### Introduction

drummer bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/drummer:dd0ccc81
```

#### Available Versions

`dd0ccc81`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/drummer drummer --help
```

#### Parameters

Run `docker run --rm username/drummer drummer --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/drummer bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/drummer drummer [options]
```

#### References

