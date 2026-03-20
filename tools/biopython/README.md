# biopython

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Biopython 生物计算工具

**类别**: Python生物工具

#### 简介

用于生物计算的Python工具集，提供序列分析、结构生物学等功能。

#### 安装

```bash
# Pull the Docker image
docker pull username/biopython:1.84
```

#### 可用版本

`1.84`, `1.83`, `1.82`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/biopython biopython --help
```

#### 参数说明

运行 `docker run --rm username/biopython biopython --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/biopython bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/biopython biopython [options]
```

#### 参考资料

- [https://biopython.org/](https://biopython.org/)
- Cock, P.J. et al. (2009). Bioinformatics, 25(11), 1422-1423.


---

## English Documentation

### Biopython Biological Computation Tools

**Category**: Python Bio Tools

#### Introduction

Python tools for biological computation including sequence analysis and structural biology.

#### Installation

```bash
# Pull the Docker image
docker pull username/biopython:1.84
```

#### Available Versions

`1.84`, `1.83`, `1.82`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/biopython biopython --help
```

#### Parameters

Run `docker run --rm username/biopython biopython --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/biopython bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/biopython biopython [options]
```

#### References

- [https://biopython.org/](https://biopython.org/)
- Cock, P.J. et al. (2009). Bioinformatics, 25(11), 1422-1423.
