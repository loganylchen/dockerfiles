# subread

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Subread 序列比对工具

**类别**: 序列比对

#### 简介

高效的读段比对和特征计数工具，包含featureCounts程序。

#### 安装

```bash
# Pull the Docker image
docker pull username/subread:2.0.6
```

#### 可用版本

`2.0.6`, `2.0.3`

#### 使用方法

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/subread subread -t 4 reference.fa reads.fq > alignment.sam
```

#### 参数说明

运行 `docker run --rm username/subread subread --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/subread bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/subread subread [options]
```

#### 参考资料

- [http://subread.sourceforge.net/](http://subread.sourceforge.net/)
- Liao, Y. et al. (2013). Nucleic Acids Res, 41(10), e108.


---

## English Documentation

### Subread Sequence Alignment Tool

**Category**: Sequence Alignment

#### Introduction

High-performance read alignment and feature counting tool, includes featureCounts.

#### Installation

```bash
# Pull the Docker image
docker pull username/subread:2.0.6
```

#### Available Versions

`2.0.6`, `2.0.3`

#### Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/subread subread -t 4 reference.fa reads.fq > alignment.sam
```

#### Parameters

Run `docker run --rm username/subread subread --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/subread bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/subread subread [options]
```

#### References

- [http://subread.sourceforge.net/](http://subread.sourceforge.net/)
- Liao, Y. et al. (2013). Nucleic Acids Res, 41(10), e108.
