# nanopolish

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Nanopolish Nanopore数据分析

**类别**: Nanopore分析

#### 简介

用于Oxford Nanopore测序数据的信号级分析和变异检测工具。

#### 安装

```bash
# Pull the Docker image
docker pull username/nanopolish:0.14.0
```

#### 可用版本

`0.14.0`, `0.13.3`, `0.13.2`

#### 使用方法

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data username/nanopolish nanopolish reads.fq
```

#### 参数说明

运行 `docker run --rm username/nanopolish nanopolish --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/nanopolish bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/nanopolish nanopolish [options]
```

#### 参考资料

- [https://github.com/jts/nanopolish](https://github.com/jts/nanopolish)
- Loman, N.J. et al. (2015). Nat Methods, 12, 733-735.


---

## English Documentation

### Nanopolish Nanopore Data Analysis

**Category**: Nanopore Analysis

#### Introduction

Signal-level analysis and variant calling for Oxford Nanopore sequencing data.

#### Installation

```bash
# Pull the Docker image
docker pull username/nanopolish:0.14.0
```

#### Available Versions

`0.14.0`, `0.13.3`, `0.13.2`

#### Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data username/nanopolish nanopolish reads.fq
```

#### Parameters

Run `docker run --rm username/nanopolish nanopolish --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/nanopolish bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/nanopolish nanopolish [options]
```

#### References

- [https://github.com/jts/nanopolish](https://github.com/jts/nanopolish)
- Loman, N.J. et al. (2015). Nat Methods, 12, 733-735.
