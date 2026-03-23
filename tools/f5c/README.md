# f5c

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### f5c Nanopore信号处理

**类别**: Nanopore分析

#### 简介

高效的Nanopore信号处理工具，支持事件对齐和甲基化检测。

#### 安装

```bash
# Pull the Docker image
docker pull username/f5c:1.6
```

#### 可用版本

`1.6`, `1.5`, `1.4`, `1.3`, `1.2`, `1.1`

#### 使用方法

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data username/f5c f5c reads.fq
```

#### 参数说明

运行 `docker run --rm username/f5c f5c --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/f5c bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/f5c f5c [options]
```

#### 参考资料

- [https://github.com/hasindu2008/f5c](https://github.com/hasindu2008/f5c)


---

## English Documentation

### f5c Nanopore Signal Processing

**Category**: Nanopore Analysis

#### Introduction

Efficient Oxford Nanopore signal processing for event alignment and methylation detection.

#### Installation

```bash
# Pull the Docker image
docker pull username/f5c:1.6
```

#### Available Versions

`1.6`, `1.5`, `1.4`, `1.3`, `1.2`, `1.1`

#### Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data username/f5c f5c reads.fq
```

#### Parameters

Run `docker run --rm username/f5c f5c --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/f5c bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/f5c f5c [options]
```

#### References

- [https://github.com/hasindu2008/f5c](https://github.com/hasindu2008/f5c)
