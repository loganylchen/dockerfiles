# hisat2

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### HISAT2 分层索引比对工具

**类别**: 序列比对

#### 简介

快速敏感的拼接感知比对工具，使用分层索引进行基因组比对。

#### 安装

```bash
# Pull the Docker image
docker pull username/hisat2:2.2.1
```

#### 可用版本

`2.2.1`

#### 使用方法

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/hisat2 hisat2 -t 4 reference.fa reads.fq > alignment.sam
```

#### 参数说明

运行 `docker run --rm username/hisat2 hisat2 --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/hisat2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/hisat2 hisat2 [options]
```

#### 参考资料

- [https://daehwankimlab.github.io/hisat2/](https://daehwankimlab.github.io/hisat2/)
- Kim, D. et al. (2019). Nat Methods, 12, 357-360.


---

## English Documentation

### HISAT2 Hierarchical Indexing Aligner

**Category**: Sequence Alignment

#### Introduction

Fast and sensitive alignment for mapping next-generation sequencing reads.

#### Installation

```bash
# Pull the Docker image
docker pull username/hisat2:2.2.1
```

#### Available Versions

`2.2.1`

#### Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/hisat2 hisat2 -t 4 reference.fa reads.fq > alignment.sam
```

#### Parameters

Run `docker run --rm username/hisat2 hisat2 --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/hisat2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/hisat2 hisat2 [options]
```

#### References

- [https://daehwankimlab.github.io/hisat2/](https://daehwankimlab.github.io/hisat2/)
- Kim, D. et al. (2019). Nat Methods, 12, 357-360.
