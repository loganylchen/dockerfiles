# picard

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Picard 序列数据处理工具

**类别**: 变异检测

#### 简介

用于处理高通量测序数据的Java工具集，包括排序、去重等功能。

#### 安装

```bash
# Pull the Docker image
docker pull username/picard:3.2.0
```

#### 可用版本

`3.2.0`, `3.1.1`, `3.0.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/picard picard --help
```

#### 参数说明

运行 `docker run --rm username/picard picard --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/picard bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/picard picard [options]
```

#### 参考资料

- [https://broadinstitute.github.io/picard/](https://broadinstitute.github.io/picard/)


---

## English Documentation

### Picard Sequence Data Processing Tools

**Category**: Variant Calling

#### Introduction

Java tools for processing high-throughput sequencing data including sorting and duplicate marking.

#### Installation

```bash
# Pull the Docker image
docker pull username/picard:3.2.0
```

#### Available Versions

`3.2.0`, `3.1.1`, `3.0.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/picard picard --help
```

#### Parameters

Run `docker run --rm username/picard picard --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/picard bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/picard picard [options]
```

#### References

- [https://broadinstitute.github.io/picard/](https://broadinstitute.github.io/picard/)
