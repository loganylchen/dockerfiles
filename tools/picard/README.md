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
# 排序 BAM 文件
docker run --rm -v /path/to/data:/data username/picard \
    picard SortSam I=input.bam O=sorted.bam SORT_ORDER=coordinate

# 标记重复
docker run --rm -v /path/to/data:/data username/picard \
    picard MarkDuplicates I=input.bam O=marked.bam M=dup_metrics.txt

# 添加 Read Groups
docker run --rm -v /path/to/data:/data username/picard \
    picard AddOrReplaceReadGroups I=input.bam O=output.bam RGID=id1 RGLB=lib1 RGPL=ILLUMINA RGSM=sample1

# 收集比对统计
docker run --rm -v /path/to/data:/data username/picard \
    picard CollectAlignmentSummaryMetrics I=input.bam R=reference.fa O=alignment_metrics.txt
```

#### 主要命令

| 命令 | 说明 |
|------|------|
| `SortSam` | 排序 BAM 文件 |
| `MarkDuplicates` | 标记重复 reads |
| `AddOrReplaceReadGroups` | 添加 Read Groups |
| `CollectAlignmentSummaryMetrics` | 比对质量统计 |
| `CollectInsertSizeMetrics` | 插入片段大小统计 |

#### 常见问题

**Q: SortSam 的坐标排序和查询排序有什么区别？**
A: 坐标排序 (coordinate) 按基因组位置排序，用于下游分析；查询排序 (queryname) 按 read 名称排序。

**Q: 为什么要标记重复？**
A: PCR 扩增会产生重复 reads，标记后可在变异检测时过滤，提高准确性。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/picard bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/picard picard [command] [options]
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
# Sort BAM file
docker run --rm -v /path/to/data:/data username/picard \
    picard SortSam I=input.bam O=sorted.bam SORT_ORDER=coordinate

# Mark duplicates
docker run --rm -v /path/to/data:/data username/picard \
    picard MarkDuplicates I=input.bam O=marked.bam M=dup_metrics.txt

# Add Read Groups
docker run --rm -v /path/to/data:/data username/picard \
    picard AddOrReplaceReadGroups I=input.bam O=output.bam RGID=id1 RGLB=lib1 RGPL=ILLUMINA RGSM=sample1

# Collect alignment statistics
docker run --rm -v /path/to/data:/data username/picard \
    picard CollectAlignmentSummaryMetrics I=input.bam R=reference.fa O=alignment_metrics.txt
```

#### Main Commands

| Command | Description |
|---------|-------------|
| `SortSam` | Sort BAM file |
| `MarkDuplicates` | Mark duplicate reads |
| `AddOrReplaceReadGroups` | Add Read Groups |
| `CollectAlignmentSummaryMetrics` | Alignment quality statistics |
| `CollectInsertSizeMetrics` | Insert size metrics |

#### FAQ

**Q: Difference between coordinate and query sorting?**
A: Coordinate sorting sorts by genomic position (for downstream analysis), query sorting sorts by read name.

**Q: Why mark duplicates?**
A: PCR amplification creates duplicate reads; marking allows filtering in variant calling for better accuracy.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/picard bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/picard picard [command] [options]
```

#### References

- [https://broadinstitute.github.io/picard/](https://broadinstitute.github.io/picard/)
