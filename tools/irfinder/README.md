# irfinder

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### IRFinder 内含子保留检测

**类别**: 可变剪接

#### 简介

从RNA-seq数据中检测和定量内含子保留事件的工具。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/irfinder:2.0.1
```

#### 可用版本

`2.0.1`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/irfinder Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/irfinder irfinder --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/irfinder bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/irfinder irfinder [options]
```

#### 参考资料

- [https://github.com/RitchieLabIGH/IRFinder](https://github.com/RitchieLabIGH/IRFinder)
- Middleton, R. et al. (2017). Genome Res, 27(10), 1726-1737.


---

## English Documentation

### IRFinder Intron Retention Detector

**Category**: Alternative Splicing

#### Introduction

Tool for detecting and quantifying intron retention events from RNA-seq data.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/irfinder:2.0.1
```

#### Available Versions

`2.0.1`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/irfinder Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/irfinder irfinder --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/irfinder bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/irfinder irfinder [options]
```

#### References

- [https://github.com/RitchieLabIGH/IRFinder](https://github.com/RitchieLabIGH/IRFinder)
- Middleton, R. et al. (2017). Genome Res, 27(10), 1726-1737.
