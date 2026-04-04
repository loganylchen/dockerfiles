# aspli

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### ASpli 可变剪接分析

**类别**: 可变剪接

#### 简介

用于RNA-seq数据中可变剪接事件检测和定量的R/Bioconductor包。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/aspli:2.14.0
```

#### 可用版本

`2.14.0`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/aspli Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/aspli aspli --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/aspli bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/aspli aspli [options]
```

#### 参考资料

- [https://bioconductor.org/packages/ASpli/](https://bioconductor.org/packages/ASpli/)
- Mancini, E. et al. (2021). Bioinformatics, 37(18), 2884-2891.


---

## English Documentation

### ASpli Alternative Splicing Analysis

**Category**: Alternative Splicing

#### Introduction

R/Bioconductor package for analysis, detection, and quantification of alternative splicing events from RNA-seq data.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/aspli:2.14.0
```

#### Available Versions

`2.14.0`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/aspli Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/aspli aspli --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/aspli bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/aspli aspli [options]
```

#### References

- [https://bioconductor.org/packages/ASpli/](https://bioconductor.org/packages/ASpli/)
- Mancini, E. et al. (2021). Bioinformatics, 37(18), 2884-2891.
