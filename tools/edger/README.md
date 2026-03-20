# edger

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### edgeR 差异表达分析

**类别**: 差异表达

#### 简介

用于差异表达分析的R包，特别适用于小样本量的RNA-seq数据。

#### 安装

```bash
# Pull the Docker image
docker pull username/edger:4.2.1
```

#### 可用版本

`4.2.1`, `4.0.16`, `3.42.4`

#### 使用方法

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/edger Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm username/edger edger --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/edger bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/edger edger [options]
```

#### 参考资料

- [https://bioconductor.org/packages/edgeR/](https://bioconductor.org/packages/edgeR/)
- Robinson, M.D. et al. (2010). Bioinformatics, 26(1), 139-140.


---

## English Documentation

### edgeR Differential Expression Analysis

**Category**: Differential Expression

#### Introduction

R package for differential expression analysis of RNA-seq data, especially suited for small sample sizes.

#### Installation

```bash
# Pull the Docker image
docker pull username/edger:4.2.1
```

#### Available Versions

`4.2.1`, `4.0.16`, `3.42.4`

#### Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/edger Rscript analysis.R
```

#### Parameters

Run `docker run --rm username/edger edger --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/edger bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/edger edger [options]
```

#### References

- [https://bioconductor.org/packages/edgeR/](https://bioconductor.org/packages/edgeR/)
- Robinson, M.D. et al. (2010). Bioinformatics, 26(1), 139-140.
