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
# 聚合当前目录所有日志
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data

# 指定输出目录
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data -o /data/reports

# 仅分析特定工具
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data -m fastqc star

# 自定义报告标题
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data -t "My Project"
```

#### 支持的工具

FastQC, STAR, HISAT2, salmon, kallisto, RSEM, StringTie, Picard, Qualimap 等 100+ 工具。

#### 常见问题

**Q: 需要什么输入文件？**
A: 各工具生成的日志文件，如 FastQC 的 .zip、STAR 的 Log.final.out 等。

**Q: 如何自定义报告？**
A: 使用配置文件 multiqc_config.yaml 或命令行参数如 `-t` 设置标题。

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
# Aggregate all logs in current directory
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data

# Specify output directory
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data -o /data/reports

# Analyze only specific tools
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data -m fastqc star

# Custom report title
docker run --rm -v /path/to/data:/data username/multiqc multiqc /data -t "My Project"
```

#### Supported Tools

FastQC, STAR, HISAT2, salmon, kallisto, RSEM, StringTie, Picard, Qualimap, and 100+ other tools.

#### FAQ

**Q: What input files are needed?**
A: Log files from various tools, like FastQC .zip, STAR Log.final.out, etc.

**Q: How to customize the report?**
A: Use multiqc_config.yaml file or command-line options like `-t` for title.

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
