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
# Oxford Nanopore 比对
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -ax map-ont reference.fa reads.fq > alignment.sam

# PacBio HiFi 比对
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -ax map-hifi reference.fa reads.fq > alignment.sam

# RNA-seq 剪接比对
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -ax splice reference.fa reads.fq > alignment.sam

# 输出 BAM 格式
docker run --rm -v /path/to/data:/data username/minimap2 sh -c "minimap2 -ax map-ont -t 8 reference.fa reads.fq | samtools sort -o aligned.bam -"
```

#### 预设模式

| 预设 | 适用平台 |
|------|----------|
| `map-ont` | Oxford Nanopore |
| `map-pb` | PacBio CLR |
| `map-hifi` | PacBio HiFi |
| `splice` | RNA-seq |
| `sr` | Illumina 短读段 |

#### 常见问题

**Q: Nanopore 和 PacBio 数据应该用哪个预设？**
A: Nanopore 使用 `-ax map-ont`，PacBio HiFi 使用 `-ax map-hifi`，PacBio CLR 使用 `-ax map-pb`。

**Q: 如何输出 BAM 格式？**
A: 使用管道：`minimap2 ... | samtools sort -o output.bam -`

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/minimap2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 [options]
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
# Oxford Nanopore alignment
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -ax map-ont reference.fa reads.fq > alignment.sam

# PacBio HiFi alignment
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -ax map-hifi reference.fa reads.fq > alignment.sam

# RNA-seq spliced alignment
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 -ax splice reference.fa reads.fq > alignment.sam

# Output BAM format
docker run --rm -v /path/to/data:/data username/minimap2 sh -c "minimap2 -ax map-ont -t 8 reference.fa reads.fq | samtools sort -o aligned.bam -"
```

#### Preset Modes

| Preset | Platform |
|--------|----------|
| `map-ont` | Oxford Nanopore |
| `map-pb` | PacBio CLR |
| `map-hifi` | PacBio HiFi |
| `splice` | RNA-seq |
| `sr` | Illumina short reads |

#### FAQ

**Q: Which preset for Nanopore vs PacBio?**
A: Use `-ax map-ont` for Nanopore, `-ax map-hifi` for PacBio HiFi, `-ax map-pb` for PacBio CLR.

**Q: How to output BAM format?**
A: Use pipe: `minimap2 ... | samtools sort -o output.bam -`

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/minimap2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/minimap2 minimap2 [options]
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
