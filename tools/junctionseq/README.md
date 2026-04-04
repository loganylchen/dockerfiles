# junctionseq

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### JunctionSeq 差异剪接分析

**类别**: 可变剪接

#### 简介

分析RNA-seq外显子连接和差异剪接使用情况的R/Bioconductor包。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/junctionseq:1.26.0
```

#### 可用版本

`1.26.0`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/junctionseq Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/junctionseq junctionseq --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/junctionseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/junctionseq junctionseq [options]
```

#### 参考资料

- [https://bioconductor.org/packages/JunctionSeq/](https://bioconductor.org/packages/JunctionSeq/)
- Hartley, S.W. & Mullikin, J.C. (2016). Nucleic Acids Res, 44(16), e127.


---

## English Documentation

### JunctionSeq Differential Junction Analysis

**Category**: Alternative Splicing

#### Introduction

R/Bioconductor package for analyzing differential junction and exon usage from RNA-seq data.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/junctionseq:1.26.0
```

#### Available Versions

`1.26.0`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/junctionseq Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/junctionseq junctionseq --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/junctionseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/junctionseq junctionseq [options]
```

#### References

- [https://bioconductor.org/packages/JunctionSeq/](https://bioconductor.org/packages/JunctionSeq/)
- Hartley, S.W. & Mullikin, J.C. (2016). Nucleic Acids Res, 44(16), e127.
