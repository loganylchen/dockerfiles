# dexseq

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### DEXSeq 差异外显子使用分析

**类别**: 可变剪接

#### 简介

检测RNA-seq数据中差异外显子使用情况的R/Bioconductor包。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/dexseq:1.50.0
```

#### 可用版本

`1.50.0`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/dexseq Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/dexseq dexseq --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/dexseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/dexseq dexseq [options]
```

#### 参考资料

- [https://bioconductor.org/packages/DEXSeq/](https://bioconductor.org/packages/DEXSeq/)
- Anders, S. et al. (2012). Genome Res, 22(10), 2008-2017.


---

## English Documentation

### DEXSeq Differential Exon Usage Analysis

**Category**: Alternative Splicing

#### Introduction

R/Bioconductor package for testing differential exon usage in RNA-seq data.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/dexseq:1.50.0
```

#### Available Versions

`1.50.0`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/dexseq Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/dexseq dexseq --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/dexseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/dexseq dexseq [options]
```

#### References

- [https://bioconductor.org/packages/DEXSeq/](https://bioconductor.org/packages/DEXSeq/)
- Anders, S. et al. (2012). Genome Res, 22(10), 2008-2017.
