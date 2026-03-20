# multiqc

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### MultiQC 质控报告聚合工具

**类别**: 质量控制

#### 简介

聚合多个生物信息学工具的质控报告，生成统一的HTML报告。

#### 安装

```bash
# Pull the Docker image
docker pull username/multiqc:1.24.1
```

#### 可用版本

`1.24.1`, `1.21`, `1.19`

#### 使用方法

```bash
# Quality control
docker run --rm -v /path/to/data:/data username/multiqc multiqc -i input.fq -o output.html
```

#### 参数说明

运行 `docker run --rm username/multiqc multiqc --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/multiqc bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/multiqc multiqc [options]
```

#### 参考资料

- [https://multiqc.info/](https://multiqc.info/)
- Ewels, P. et al. (2016). Bioinformatics, 32(19), 3047-3048.


---

## English Documentation

### MultiQC Quality Control Report Aggregator

**Category**: Quality Control

#### Introduction

Aggregate results from multiple bioinformatics tools into a single HTML report.

#### Installation

```bash
# Pull the Docker image
docker pull username/multiqc:1.24.1
```

#### Available Versions

`1.24.1`, `1.21`, `1.19`

#### Usage

```bash
# Quality control
docker run --rm -v /path/to/data:/data username/multiqc multiqc -i input.fq -o output.html
```

#### Parameters

Run `docker run --rm username/multiqc multiqc --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/multiqc bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/multiqc multiqc [options]
```

#### References

- [https://multiqc.info/](https://multiqc.info/)
- Ewels, P. et al. (2016). Bioinformatics, 32(19), 3047-3048.
