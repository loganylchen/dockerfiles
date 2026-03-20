# stringtie

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### StringTie 转录本组装工具

**类别**: RNA-seq分析

#### 简介

高效的RNA-seq比对数据转录本组装和定量工具。

#### 安装

```bash
# Pull the Docker image
docker pull username/stringtie:2.2.3
```

#### 可用版本

`2.2.3`, `2.2.1`, `2.1.7`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/stringtie stringtie --help
```

#### 参数说明

运行 `docker run --rm username/stringtie stringtie --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/stringtie bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/stringtie stringtie [options]
```

#### 参考资料

- [https://ccb.jhu.edu/software/stringtie/](https://ccb.jhu.edu/software/stringtie/)
- Pertea, M. et al. (2015). Nat Biotechnol, 33, 290-295.


---

## English Documentation

### StringTie Transcript Assembler

**Category**: RNA-seq Analysis

#### Introduction

A fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.

#### Installation

```bash
# Pull the Docker image
docker pull username/stringtie:2.2.3
```

#### Available Versions

`2.2.3`, `2.2.1`, `2.1.7`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/stringtie stringtie --help
```

#### Parameters

Run `docker run --rm username/stringtie stringtie --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/stringtie bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/stringtie stringtie [options]
```

#### References

- [https://ccb.jhu.edu/software/stringtie/](https://ccb.jhu.edu/software/stringtie/)
- Pertea, M. et al. (2015). Nat Biotechnol, 33, 290-295.
