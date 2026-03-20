# minimap2

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Minimap2 长读段比对工具

**类别**: 序列比对

#### 简介

用于长读段（PacBio/Oxford Nanopore）序列比对的高效工具，支持DNA和RNA序列比对。

#### 安装

```bash
# Pull the Docker image
docker pull username/minimap2:2.30
```

#### 可用版本

`2.30`, `2.29`, `2.28`, `2.27`, `2.26`, `2.25`

#### 使用方法

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -t 4 reference.fa reads.fq > alignment.sam
```

#### 参数说明

运行 `docker run --rm username/minimap2 minimap2 --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/minimap2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 [options]
```

#### 参考资料

- [https://github.com/lh3/minimap2](https://github.com/lh3/minimap2)
- Li, H. (2018). Bioinformatics, 34(18), 3094-3100.


---

## English Documentation

### Minimap2 Long Read Aligner

**Category**: Sequence Alignment

#### Introduction

A versatile pairwise aligner for genomic and spliced nucleotide sequences, optimized for long reads (PacBio/Oxford Nanopore).

#### Installation

```bash
# Pull the Docker image
docker pull username/minimap2:2.30
```

#### Available Versions

`2.30`, `2.29`, `2.28`, `2.27`, `2.26`, `2.25`

#### Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -t 4 reference.fa reads.fq > alignment.sam
```

#### Parameters

Run `docker run --rm username/minimap2 minimap2 --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/minimap2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 [options]
```

#### References

- [https://github.com/lh3/minimap2](https://github.com/lh3/minimap2)
- Li, H. (2018). Bioinformatics, 34(18), 3094-3100.
