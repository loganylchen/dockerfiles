# majiq

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### MAJIQ 可变剪接定量

**类别**: 可变剪接

#### 简介

从RNA-seq数据中检测、定量和可视化局部剪接变异的工具。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/majiq:2.5
```

#### 可用版本

`2.5`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/majiq Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/majiq majiq --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/majiq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/majiq majiq [options]
```

#### 参考资料

- [https://majiq.biociphers.org/](https://majiq.biociphers.org/)
- Vaquero-Garcia, J. et al. (2016). eLife, 5, e11752.


---

## English Documentation

### MAJIQ Alternative Splicing Quantification

**Category**: Alternative Splicing

#### Introduction

Tool for detecting, quantifying, and visualizing local splicing variations from RNA-seq data.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/majiq:2.5
```

#### Available Versions

`2.5`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/majiq Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/majiq majiq --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/majiq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/majiq majiq [options]
```

#### References

- [https://majiq.biociphers.org/](https://majiq.biociphers.org/)
- Vaquero-Garcia, J. et al. (2016). eLife, 5, e11752.
