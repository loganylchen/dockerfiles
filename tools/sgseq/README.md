# sgseq

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### SGSeq 剪接图分析

**类别**: 可变剪接

#### 简介

用于从RNA-seq数据分析外显子使用和剪接位点模式的R/Bioconductor包。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/sgseq:1.38.0
```

#### 可用版本

`1.38.0`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/sgseq Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/sgseq sgseq --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/sgseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/sgseq sgseq [options]
```

#### 参考资料

- [https://bioconductor.org/packages/SGSeq/](https://bioconductor.org/packages/SGSeq/)
- Goldstein, L.D. et al. (2016). BMC Bioinformatics, 17, 464.


---

## English Documentation

### SGSeq Splice Graph Analysis

**Category**: Alternative Splicing

#### Introduction

R/Bioconductor package for splice graph analysis of exon usage and splice site patterns from RNA-seq data.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/sgseq:1.38.0
```

#### Available Versions

`1.38.0`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/sgseq Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/sgseq sgseq --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/sgseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/sgseq sgseq [options]
```

#### References

- [https://bioconductor.org/packages/SGSeq/](https://bioconductor.org/packages/SGSeq/)
- Goldstein, L.D. et al. (2016). BMC Bioinformatics, 17, 464.
