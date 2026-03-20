# gatk

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### GATK 基因组分析工具包

**类别**: 变异检测

#### 简介

用于变异检测和基因组分析的综合性工具包，广泛应用于人类基因组学研究。

#### 安装

```bash
# Pull the Docker image
docker pull username/gatk:4.6.1.0
```

#### 可用版本

`4.6.1.0`, `4.5.0.0`, `4.4.0.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/gatk gatk --help
```

#### 参数说明

运行 `docker run --rm username/gatk gatk --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gatk bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gatk gatk [options]
```

#### 参考资料

- [https://gatk.broadinstitute.org/](https://gatk.broadinstitute.org/)
- Van der Auwera, G.A. et al. (2013). Curr Protoc Bioinformatics, 43, 11.10.1-11.10.33.


---

## English Documentation

### GATK Genome Analysis Toolkit

**Category**: Variant Calling

#### Introduction

Comprehensive toolkit for variant discovery and genotyping, widely used in human genomics research.

#### Installation

```bash
# Pull the Docker image
docker pull username/gatk:4.6.1.0
```

#### Available Versions

`4.6.1.0`, `4.5.0.0`, `4.4.0.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/gatk gatk --help
```

#### Parameters

Run `docker run --rm username/gatk gatk --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/gatk bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/gatk gatk [options]
```

#### References

- [https://gatk.broadinstitute.org/](https://gatk.broadinstitute.org/)
- Van der Auwera, G.A. et al. (2013). Curr Protoc Bioinformatics, 43, 11.10.1-11.10.33.
