# bonito

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Bonito Nanopore碱基调用

**类别**: Nanopore分析

#### 简介

Oxford Nanopore官方的GPU加速碱基调用工具，使用神经网络进行高精度碱基调用。

#### 安装

```bash
# Pull the Docker image
docker pull username/bonito:0.8.1
```

#### 可用版本

`0.8.1`, `0.7.3`, `0.6.2`

#### 使用方法

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data username/bonito bonito reads.fq
```

#### 参数说明

运行 `docker run --rm username/bonito bonito --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bonito bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bonito bonito [options]
```

#### 参考资料

- [https://github.com/nanoporetech/bonito](https://github.com/nanoporetech/bonito)


---

## English Documentation

### Bonito Nanopore Basecaller

**Category**: Nanopore Analysis

#### Introduction

GPU-accelerated basecaller for Oxford Nanopore sequencing data using neural networks.

#### Installation

```bash
# Pull the Docker image
docker pull username/bonito:0.8.1
```

#### Available Versions

`0.8.1`, `0.7.3`, `0.6.2`

#### Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data username/bonito bonito reads.fq
```

#### Parameters

Run `docker run --rm username/bonito bonito --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/bonito bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/bonito bonito [options]
```

#### References

- [https://github.com/nanoporetech/bonito](https://github.com/nanoporetech/bonito)
