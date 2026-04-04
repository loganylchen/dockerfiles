# whippet

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Whippet 快速剪接分析

**类别**: 可变剪接

#### 简介

基于Julia语言的快速RNA-seq剪接事件分析工具，计算PSI值。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/whippet:1.6.1
```

#### 可用版本

`1.6.1`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/whippet Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/whippet whippet --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/whippet bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/whippet whippet [options]
```

#### 参考资料

- [https://github.com/timbitz/Whippet.jl](https://github.com/timbitz/Whippet.jl)
- Sterne-Weiler, T. et al. (2018). Mol Cell, 72(1), 187-200.


---

## English Documentation

### Whippet Fast Splicing Analysis

**Category**: Alternative Splicing

#### Introduction

Fast Julia-based RNA-seq splicing analysis tool for quantifying percent-spliced-in (PSI) values.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/whippet:1.6.1
```

#### Available Versions

`1.6.1`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/whippet Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/whippet whippet --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/whippet bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/whippet whippet [options]
```

#### References

- [https://github.com/timbitz/Whippet.jl](https://github.com/timbitz/Whippet.jl)
- Sterne-Weiler, T. et al. (2018). Mol Cell, 72(1), 187-200.
