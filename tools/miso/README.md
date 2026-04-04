# miso

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### MISO 剪接异构体分析

**类别**: 可变剪接

#### 简介

用于估计RNA-seq数据中可变剪接事件PSI值的概率模型工具。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/miso:0.5.4
```

#### 可用版本

`0.5.4`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/miso Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/miso miso --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/miso bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/miso miso [options]
```

#### 参考资料

- [https://miso.readthedocs.io/](https://miso.readthedocs.io/)
- Katz, Y. et al. (2010). Nat Methods, 7(12), 1009-1015.


---

## English Documentation

### MISO Mixture of Isoforms Analysis

**Category**: Alternative Splicing

#### Introduction

Probabilistic framework for estimating percent-spliced-in (PSI) values of alternatively spliced exons from RNA-seq.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/miso:0.5.4
```

#### Available Versions

`0.5.4`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/miso Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/miso miso --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/miso bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/miso miso [options]
```

#### References

- [https://miso.readthedocs.io/](https://miso.readthedocs.io/)
- Katz, Y. et al. (2010). Nat Methods, 7(12), 1009-1015.
