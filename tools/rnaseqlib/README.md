# rnaseqlib

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### RNAseqLib RNA-seq分析库

**类别**: 可变剪接

#### 简介

用于分析剪接模式和从GTF文件创建基因注释的RNA-seq工具库。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/rnaseqlib:1.1.2
```

#### 可用版本

`1.1.2`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/rnaseqlib Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/rnaseqlib rnaseqlib --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rnaseqlib bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rnaseqlib rnaseqlib [options]
```

#### 参考资料

- [https://github.com/yarden/rnaseqlib](https://github.com/yarden/rnaseqlib)


---

## English Documentation

### RNAseqLib RNA-seq Analysis Library

**Category**: Alternative Splicing

#### Introduction

RNA-seq library for analyzing splicing patterns and creating gene annotations from GTF files.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/rnaseqlib:1.1.2
```

#### Available Versions

`1.1.2`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/rnaseqlib Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/rnaseqlib rnaseqlib --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rnaseqlib bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rnaseqlib rnaseqlib [options]
```

#### References

- [https://github.com/yarden/rnaseqlib](https://github.com/yarden/rnaseqlib)
