# star

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### STAR RNA-seq比对工具

**类别**: 序列比对

#### 简介

超快速通用的RNA-seq比对工具，支持拼接感知比对。

#### 安装

```bash
# Pull the Docker image
docker pull username/star:2.7.11b
```

#### 可用版本

`2.7.11b`, `2.7.10a`, `2.7.9a`

#### 使用方法

```bash
# 1. 生成基因组索引
docker run --rm -v /path/to/data:/data username/star \
    STAR --runMode genomeGenerate \
    --genomeDir /data/genome_index \
    --genomeFastaFiles genome.fa \
    --sjdbGTFfile annotation.gtf \
    --sjdbOverhang 100 \
    --runThreadN 8

# 2. 双端数据比对
docker run --rm -v /path/to/data:/data username/star \
    STAR --genomeDir /data/genome_index \
    --readFilesIn R1.fastq.gz R2.fastq.gz \
    --readFilesCommand zcat \
    --outFileNamePrefix sample_ \
    --outSAMtype BAM SortedByCoordinate \
    --runThreadN 8

# 3. 两步比对模式（推荐）
docker run --rm -v /path/to/data:/data username/star \
    STAR --genomeDir /data/genome_index \
    --readFilesIn R1.fastq.gz R2.fastq.gz \
    --readFilesCommand zcat \
    --twopassMode Basic \
    --outSAMtype BAM SortedByCoordinate \
    --runThreadN 8
```

#### 主要参数

| 参数 | 说明 |
|------|------|
| `--genomeDir` | 基因组索引目录 |
| `--genomeFastaFiles` | 参考基因组 FASTA |
| `--sjdbGTFfile` | 基因注释 GTF |
| `--sjdbOverhang` | read长度减1 |
| `--readFilesIn` | 输入 FASTQ |
| `--outSAMtype` | 输出格式 |
| `--runThreadN` | 线程数 |
| `--twopassMode` | 两步比对模式 |

#### 常见问题

**Q: --sjdbOverhang 应该设置多少？**
A: 一般为 read 长度减 1。例如 101bp reads 使用 100。

**Q: 什么是两步比对模式？**
A: 第一次运行发现新剪接位点，第二次使用这些位点重新比对，提高准确率。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/star bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/star star [options]
```

#### 参考资料

- [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
- Dobin, A. et al. (2013). Bioinformatics, 29(1), 15-21.


---

## English Documentation

### STAR RNA-seq Aligner

**Category**: Sequence Alignment

#### Introduction

Ultrafast universal RNA-seq aligner with splice-aware alignment support.

#### Installation

```bash
# Pull the Docker image
docker pull username/star:2.7.11b
```

#### Available Versions

`2.7.11b`, `2.7.10a`, `2.7.9a`

#### Usage

```bash
# 1. Generate genome index
docker run --rm -v /path/to/data:/data username/star \
    STAR --runMode genomeGenerate \
    --genomeDir /data/genome_index \
    --genomeFastaFiles genome.fa \
    --sjdbGTFfile annotation.gtf \
    --sjdbOverhang 100 \
    --runThreadN 8

# 2. Paired-end alignment
docker run --rm -v /path/to/data:/data username/star \
    STAR --genomeDir /data/genome_index \
    --readFilesIn R1.fastq.gz R2.fastq.gz \
    --readFilesCommand zcat \
    --outFileNamePrefix sample_ \
    --outSAMtype BAM SortedByCoordinate \
    --runThreadN 8

# 3. Two-pass mode (recommended)
docker run --rm -v /path/to/data:/data username/star \
    STAR --genomeDir /data/genome_index \
    --readFilesIn R1.fastq.gz R2.fastq.gz \
    --readFilesCommand zcat \
    --twopassMode Basic \
    --outSAMtype BAM SortedByCoordinate \
    --runThreadN 8
```

#### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `--genomeDir` | Genome index directory |
| `--genomeFastaFiles` | Reference genome FASTA |
| `--sjdbGTFfile` | Gene annotation GTF |
| `--sjdbOverhang` | Read length minus 1 |
| `--readFilesIn` | Input FASTQ files |
| `--outSAMtype` | Output format |
| `--runThreadN` | Number of threads |
| `--twopassMode` | Two-pass alignment mode |

#### FAQ

**Q: What should --sjdbOverhang be set to?**
A: Typically read length minus 1. For 101bp reads, use 100.

**Q: What is two-pass mode?**
A: First pass discovers novel splice junctions, second pass uses them for realignment, improving accuracy.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/star bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/star star [options]
```

#### References

- [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
- Dobin, A. et al. (2013). Bioinformatics, 29(1), 15-21.
