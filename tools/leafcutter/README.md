# leafcutter

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Leafcutter 内含子剪接分析

**类别**: 可变剪接

#### 简介

基于内含子使用的轻量级可变剪接定量和差异分析工具。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/leafcutter:0.2.9
```

#### 可用版本

`0.2.9`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/leafcutter Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/leafcutter leafcutter --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/leafcutter bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/leafcutter leafcutter [options]
```

#### 参考资料

- [https://github.com/davidaknowles/leafcutter](https://github.com/davidaknowles/leafcutter)
- Li, Y.I. et al. (2018). Nat Genet, 50, 151-158.


---

## English Documentation

### Leafcutter Intron Splicing Analysis

**Category**: Alternative Splicing

#### Introduction

Lightweight tool for quantifying and testing differential intron usage as a proxy for splicing.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/leafcutter:0.2.9
```

#### Available Versions

`0.2.9`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/leafcutter Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/leafcutter leafcutter --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/leafcutter bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/leafcutter leafcutter [options]
```

#### References

- [https://github.com/davidaknowles/leafcutter](https://github.com/davidaknowles/leafcutter)
- Li, Y.I. et al. (2018). Nat Genet, 50, 151-158.
