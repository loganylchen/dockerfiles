# star

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### STAR RNA-seq比对工具

**类别**: 序列比对

#### 简介

超快速通用的RNA-seq比对工具，支持拼接感知比对。

#### 安装

```bash
# Pull the Docker image
docker pull username/star:2.7.11b
```

#### 可用版本

`2.7.11b`, `2.7.10a`, `2.7.9a`

#### 使用方法

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/star star -t 4 reference.fa reads.fq > alignment.sam
```

#### 参数说明

运行 `docker run --rm username/star star --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/star bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/star star [options]
```

#### 参考资料

- [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
- Dobin, A. et al. (2013). Bioinformatics, 29(1), 15-21.


---

## English Documentation

### STAR RNA-seq Aligner

**Category**: Sequence Alignment

#### Introduction

Ultrafast universal RNA-seq aligner with splice-aware alignment support.

#### Installation

```bash
# Pull the Docker image
docker pull username/star:2.7.11b
```

#### Available Versions

`2.7.11b`, `2.7.10a`, `2.7.9a`

#### Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/star star -t 4 reference.fa reads.fq > alignment.sam
```

#### Parameters

Run `docker run --rm username/star star --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/star bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/star star [options]
```

#### References

- [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
- Dobin, A. et al. (2013). Bioinformatics, 29(1), 15-21.
