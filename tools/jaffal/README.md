# jaffal

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### jaffal

**类别**: 通用

#### 简介

jaffal 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/jaffal:2.3
```

#### 可用版本

`2.3`, `2.2`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/jaffal jaffal --help
```

#### 参数说明

运行 `docker run --rm username/jaffal jaffal --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/jaffal bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/jaffal jaffal [options]
```

#### 参考资料



---

## English Documentation

### jaffal

**Category**: General

#### Introduction

jaffal bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/jaffal:2.3
```

#### Available Versions

`2.3`, `2.2`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/jaffal jaffal --help
```

#### Parameters

Run `docker run --rm username/jaffal jaffal --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/jaffal bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/jaffal jaffal [options]
```

#### References

