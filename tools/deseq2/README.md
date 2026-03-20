# deseq2

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### DESeq2 差异表达分析

**类别**: 差异表达

#### 简介

基于负二项分布的RNA-seq数据差异基因表达分析R包。

#### 安装

```bash
# Pull the Docker image
docker pull username/deseq2:1.44.0
```

#### 可用版本

`1.44.0`, `1.42.1`, `1.40.2`

#### 使用方法

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/deseq2 Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm username/deseq2 deseq2 --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/deseq2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/deseq2 deseq2 [options]
```

#### 参考资料

- [https://bioconductor.org/packages/DESeq2/](https://bioconductor.org/packages/DESeq2/)
- Love, M.I. et al. (2014). Genome Biol, 15, 550.


---

## English Documentation

### DESeq2 Differential Expression Analysis

**Category**: Differential Expression

#### Introduction

R package for differential gene expression analysis based on the negative binomial distribution.

#### Installation

```bash
# Pull the Docker image
docker pull username/deseq2:1.44.0
```

#### Available Versions

`1.44.0`, `1.42.1`, `1.40.2`

#### Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/deseq2 Rscript analysis.R
```

#### Parameters

Run `docker run --rm username/deseq2 deseq2 --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/deseq2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/deseq2 deseq2 [options]
```

#### References

- [https://bioconductor.org/packages/DESeq2/](https://bioconductor.org/packages/DESeq2/)
- Love, M.I. et al. (2014). Genome Biol, 15, 550.
