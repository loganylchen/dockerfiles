# spladder

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### SplAdder 可变剪接检测

**类别**: 可变剪接

#### 简介

从RNA-seq比对中检测、定量和分析可变剪接事件的工具。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/spladder:3.0.4
```

#### 可用版本

`3.0.4`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/spladder Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/spladder spladder --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/spladder bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/spladder spladder [options]
```

#### 参考资料

- [https://github.com/ratschlab/spladder](https://github.com/ratschlab/spladder)
- Kahles, A. et al. (2016). Bioinformatics, 32(12), i39-i48.


---

## English Documentation

### SplAdder Alternative Splicing Detection

**Category**: Alternative Splicing

#### Introduction

Tool for detecting, quantifying, and analyzing alternative splicing events from RNA-seq alignments.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/spladder:3.0.4
```

#### Available Versions

`3.0.4`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/spladder Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/spladder spladder --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/spladder bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/spladder spladder [options]
```

#### References

- [https://github.com/ratschlab/spladder](https://github.com/ratschlab/spladder)
- Kahles, A. et al. (2016). Bioinformatics, 32(12), i39-i48.
