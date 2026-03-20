# hisat2

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### HISAT2 分层索引比对工具

**类别**: 序列比对

#### 简介

快速敏感的拼接感知比对工具，使用分层索引进行基因组比对。

#### 安装

```bash
# Pull the Docker image
docker pull username/hisat2:2.2.1
```

#### 可用版本

`2.2.1`

#### 使用方法

```bash
# 1. 构建基因组索引
docker run --rm -v /path/to/data:/data username/hisat2 \
    hisat2-build genome.fa genome_index

# 2. 双端数据比对
docker run --rm -v /path/to/data:/data username/hisat2 \
    hisat2 -x genome_index -1 R1.fq -2 R2.fq -S output.sam -p 8

# 3. 链特异性 RNA-seq
docker run --rm -v /path/to/data:/data username/hisat2 \
    hisat2 -x genome_index -1 R1.fq -2 R2.fq --rna-strandness FR -S output.sam
```

#### 主要参数

| 参数 | 说明 |
|------|------|
| `-x` | 基因组索引前缀 |
| `-1/-2` | 双端输入文件 |
| `-S` | 输出 SAM 文件 |
| `-p` | 线程数 |
| `--rna-strandness` | 链特异性 (FR/RF) |
| `--dta` | 为 StringTie 优化输出 |

#### 常见问题

**Q: FR 和 RF 链特异性有什么区别？**
A: FR 表示 read1 对应正义链，RF 表示 read1 对应反义链。

**Q: 与 STAR 相比如何选择？**
A: HISAT2 使用更少内存，适合小内存环境；STAR 速度更快。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/hisat2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/hisat2 hisat2 [options]
```

#### 参考资料

- [https://daehwankimlab.github.io/hisat2/](https://daehwankimlab.github.io/hisat2/)
- Kim, D. et al. (2019). Nat Methods, 12, 357-360.


---

## English Documentation

### HISAT2 Hierarchical Indexing Aligner

**Category**: Sequence Alignment

#### Introduction

Fast and sensitive alignment for mapping next-generation sequencing reads.

#### Installation

```bash
# Pull the Docker image
docker pull username/hisat2:2.2.1
```

#### Available Versions

`2.2.1`

#### Usage

```bash
# 1. Build genome index
docker run --rm -v /path/to/data:/data username/hisat2 \
    hisat2-build genome.fa genome_index

# 2. Paired-end alignment
docker run --rm -v /path/to/data:/data username/hisat2 \
    hisat2 -x genome_index -1 R1.fq -2 R2.fq -S output.sam -p 8

# 3. Strand-specific RNA-seq
docker run --rm -v /path/to/data:/data username/hisat2 \
    hisat2 -x genome_index -1 R1.fq -2 R2.fq --rna-strandness FR -S output.sam
```

#### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `-x` | Genome index prefix |
| `-1/-2` | Paired input files |
| `-S` | Output SAM file |
| `-p` | Number of threads |
| `--rna-strandness` | Strand specificity (FR/RF) |
| `--dta` | Output optimized for StringTie |

#### FAQ

**Q: What's the difference between FR and RF strand specificity?**
A: FR means read1 corresponds to sense strand, RF means read1 corresponds to antisense strand.

**Q: How to choose between HISAT2 and STAR?**
A: HISAT2 uses less memory (good for small RAM), STAR is faster.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/hisat2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/hisat2 hisat2 [options]
```

#### References

- [https://daehwankimlab.github.io/hisat2/](https://daehwankimlab.github.io/hisat2/)
- Kim, D. et al. (2019). Nat Methods, 12, 357-360.
