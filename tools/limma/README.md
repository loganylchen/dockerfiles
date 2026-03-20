# limma

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### limma 线性模型分析

**类别**: 差异表达

#### 简介

用于基因表达数据分析的R包，支持微阵列和RNA-seq数据。

#### 安装

```bash
# Pull the Docker image
docker pull username/limma:3.60.4
```

#### 可用版本

`3.60.4`, `3.58.1`, `3.56.2`

#### 使用方法

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/limma Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm username/limma limma --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/limma bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/limma limma [options]
```

#### 参考资料

- [https://bioconductor.org/packages/limma/](https://bioconductor.org/packages/limma/)
- Ritchie, M.E. et al. (2015). Nucleic Acids Res, 43(7), e47.


---

## English Documentation

### limma Linear Models for Microarray

**Category**: Differential Expression

#### Introduction

R package for analyzing gene expression data from microarrays and RNA-seq using linear models.

#### Installation

```bash
# Pull the Docker image
docker pull username/limma:3.60.4
```

#### Available Versions

`3.60.4`, `3.58.1`, `3.56.2`

#### Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/limma Rscript analysis.R
```

#### Parameters

Run `docker run --rm username/limma limma --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/limma bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/limma limma [options]
```

#### References

- [https://bioconductor.org/packages/limma/](https://bioconductor.org/packages/limma/)
- Ritchie, M.E. et al. (2015). Nucleic Acids Res, 43(7), e47.
