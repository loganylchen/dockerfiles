# clusterprofiler

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### clusterProfiler 功能富集分析

**类别**: 功能注释

#### 简介

用于基因功能富集分析和可视化的R包，支持GO和KEGG分析。

#### 安装

```bash
# Pull the Docker image
docker pull username/clusterprofiler:4.12.6
```

#### 可用版本

`4.12.6`, `4.10.1`, `4.8.3`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/clusterprofiler clusterprofiler --help
```

#### 参数说明

运行 `docker run --rm username/clusterprofiler clusterprofiler --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/clusterprofiler bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/clusterprofiler clusterprofiler [options]
```

#### 参考资料

- [https://bioconductor.org/packages/clusterProfiler/](https://bioconductor.org/packages/clusterProfiler/)
- Yu, G. et al. (2012). OMICS, 16(5), 284-287.


---

## English Documentation

### clusterProfiler Functional Enrichment Analysis

**Category**: Functional Annotation

#### Introduction

R package for gene functional enrichment analysis and visualization (GO, KEGG, etc.).

#### Installation

```bash
# Pull the Docker image
docker pull username/clusterprofiler:4.12.6
```

#### Available Versions

`4.12.6`, `4.10.1`, `4.8.3`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/clusterprofiler clusterprofiler --help
```

#### Parameters

Run `docker run --rm username/clusterprofiler clusterprofiler --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/clusterprofiler bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/clusterprofiler clusterprofiler [options]
```

#### References

- [https://bioconductor.org/packages/clusterProfiler/](https://bioconductor.org/packages/clusterProfiler/)
- Yu, G. et al. (2012). OMICS, 16(5), 284-287.
