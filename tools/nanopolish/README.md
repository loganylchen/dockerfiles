# nanopolish

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Nanopolish Nanopore数据分析

**类别**: Nanopore分析

#### 简介

用于Oxford Nanopore测序数据的信号级分析和变异检测工具。

#### 安装

```bash
# Pull the Docker image
docker pull username/nanopolish:0.14.0
```

#### 可用版本

`0.14.0`, `0.13.3`, `0.13.2`

#### 使用方法

```bash
# 1. 索引 fast5 文件到 BAM
docker run --rm -v /path/to/data:/data username/nanopolish \
    nanopolish index -d fast5_dir/ alignments.bam

# 2. 甲基化检测
docker run --rm -v /path/to/data:/data username/nanopolish \
    nanopolish call-methylation -t 8 -r reads.fa -b alignments.bam \
    -g reference.fa > methylation.tsv

# 3. Consensus polishing
docker run --rm -v /path/to/data:/data username/nanopolish \
    nanopolish variants --consensus -o polished.vcf -r reads.fa \
    -b alignments.bam -g reference.fa -t 8
```

#### 主要命令

| 命令 | 说明 |
|------|------|
| `index` | 将 fast5 索引到 BAM |
| `call-methylation` | 甲基化检测 |
| `variants` | 变异检测/polishing |
| `polya` | Poly(A) 尾分析 |

#### 常见问题

**Q: fast5 文件和 BAM 如何关联？**
A: 使用 `nanopolish index` 命令将 fast5 路径信息添加到 BAM 文件中。

**Q: 为什么需要原始信号数据？**
A: nanopolish 使用电信号级别的数据进行更精确的碱基校正和甲基化检测。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/nanopolish bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/nanopolish nanopolish [command] [options]
```

#### 参考资料

- [https://github.com/jts/nanopolish](https://github.com/jts/nanopolish)
- Loman, N.J. et al. (2015). Nat Methods, 12, 733-735.


---

## English Documentation

### Nanopolish Nanopore Data Analysis

**Category**: Nanopore Analysis

#### Introduction

Signal-level analysis and variant calling for Oxford Nanopore sequencing data.

#### Installation

```bash
# Pull the Docker image
docker pull username/nanopolish:0.14.0
```

#### Available Versions

`0.14.0`, `0.13.3`, `0.13.2`

#### Usage

```bash
# 1. Index fast5 files into BAM
docker run --rm -v /path/to/data:/data username/nanopolish \
    nanopolish index -d fast5_dir/ alignments.bam

# 2. Methylation calling
docker run --rm -v /path/to/data:/data username/nanopolish \
    nanopolish call-methylation -t 8 -r reads.fa -b alignments.bam \
    -g reference.fa > methylation.tsv

# 3. Consensus polishing
docker run --rm -v /path/to/data:/data username/nanopolish \
    nanopolish variants --consensus -o polished.vcf -r reads.fa \
    -b alignments.bam -g reference.fa -t 8
```

#### Main Commands

| Command | Description |
|---------|-------------|
| `index` | Index fast5 files into BAM |
| `call-methylation` | Methylation detection |
| `variants` | Variant calling/polishing |
| `polya` | Poly(A) tail analysis |

#### FAQ

**Q: How to associate fast5 files with BAM?**
A: Use `nanopolish index` command to add fast5 path information to BAM.

**Q: Why is raw signal data needed?**
A: nanopolish uses electrical signal-level data for more accurate base correction and methylation detection.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/nanopolish bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/nanopolish nanopolish [command] [options]
```

#### References

- [https://github.com/jts/nanopolish](https://github.com/jts/nanopolish)
- Loman, N.J. et al. (2015). Nat Methods, 12, 733-735.
