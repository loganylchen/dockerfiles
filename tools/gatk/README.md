# gatk

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### GATK 基因组分析工具包

**类别**: 变异检测

#### 简介

用于变异检测和基因组分析的综合性工具包，广泛应用于人类基因组学研究。

#### 安装

```bash
# Pull the Docker image
docker pull username/gatk:4.6.1.0
```

#### 可用版本

`4.6.1.0`, `4.5.0.0`, `4.4.0.0`

#### 使用方法

```bash
# HaplotypeCaller (变异检测)
docker run --rm -v /path/to/data:/data username/gatk \
    gatk HaplotypeCaller -R reference.fa -I input.bam -O output.vcf

# BaseRecalibrator (碱基质量重校正)
docker run --rm -v /path/to/data:/data username/gatk \
    gatk BaseRecalibrator -I input.bam -R reference.fa --known-sites dbsnp.vcf -O recal.table

# ApplyBQSR (应用校正)
docker run --rm -v /path/to/data:/data username/gatk \
    gatk ApplyBQSR -R reference.fa -I input.bam --bqsr-recal-table recal.table -O recalibrated.bam
```

#### 主要工具

| 工具 | 说明 |
|------|------|
| `HaplotypeCaller` | 单样本/群体变异检测 |
| `BaseRecalibrator` | 碱基质量重校正 |
| `ApplyBQSR` | 应用质量校正 |
| `MarkDuplicates` | 标记重复 (使用 Picard) |
| `CalculateContamination` | 计算污染程度 |

#### 常见问题

**Q: GATK 4 与 GATK 3 有什么区别？**
A: GATK 4 是纯 Java 实现，无需 Python，且支持 Spark 大数据处理。

**Q: 变异检测前需要什么预处理？**
A: 通常包括：标记重复 (MarkDuplicates)、碱基质量重校正 (BQSR)、索引排序。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gatk bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gatk gatk [tool] [options]
```

#### 参考资料

- [https://gatk.broadinstitute.org/](https://gatk.broadinstitute.org/)
- Van der Auwera, G.A. et al. (2013). Curr Protoc Bioinformatics, 43, 11.10.1-11.10.33.


---

## English Documentation

### GATK Genome Analysis Toolkit

**Category**: Variant Calling

#### Introduction

Comprehensive toolkit for variant discovery and genotyping, widely used in human genomics research.

#### Installation

```bash
# Pull the Docker image
docker pull username/gatk:4.6.1.0
```

#### Available Versions

`4.6.1.0`, `4.5.0.0`, `4.4.0.0`

#### Usage

```bash
# HaplotypeCaller (variant calling)
docker run --rm -v /path/to/data:/data username/gatk \
    gatk HaplotypeCaller -R reference.fa -I input.bam -O output.vcf

# BaseRecalibrator (base quality recalibration)
docker run --rm -v /path/to/data:/data username/gatk \
    gatk BaseRecalibrator -I input.bam -R reference.fa --known-sites dbsnp.vcf -O recal.table

# ApplyBQSR (apply recalibration)
docker run --rm -v /path/to/data:/data username/gatk \
    gatk ApplyBQSR -R reference.fa -I input.bam --bqsr-recal-table recal.table -O recalibrated.bam
```

#### Key Tools

| Tool | Description |
|------|-------------|
| `HaplotypeCaller` | Single-sample/joint variant calling |
| `BaseRecalibrator` | Base quality score recalibration |
| `ApplyBQSR` | Apply recalibration |
| `MarkDuplicates` | Mark duplicates (via Picard) |
| `CalculateContamination` | Calculate contamination |

#### FAQ

**Q: Difference between GATK 4 and GATK 3?**
A: GATK 4 is pure Java with no Python dependency, and supports Spark for big data.

**Q: What preprocessing is needed before variant calling?**
A: Typically: MarkDuplicates, Base Quality Score Recalibration (BQSR), and sort indexing.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gatk bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gatk gatk [tool] [options]
```

#### References

- [https://gatk.broadinstitute.org/](https://gatk.broadinstitute.org/)
- Van der Auwera, G.A. et al. (2013). Curr Protoc Bioinformatics, 43, 11.10.1-11.10.33.
