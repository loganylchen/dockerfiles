# qualimap

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### QualiMap 质量评估工具

**类别**: 质量控制

#### 简介

用于评估测序数据和比对质量的工具集。

#### 安装

```bash
# Pull the Docker image
docker pull username/qualimap:2.3
```

#### 可用版本

`2.3`, `2.2.2d`

#### 使用方法

```bash
# Quality control
docker run --rm -v /path/to/data:/data username/qualimap qualimap -i input.fq -o output.html
```

#### 参数说明

运行 `docker run --rm username/qualimap qualimap --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/qualimap bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/qualimap qualimap [options]
```

#### 参考资料

- [http://qualimap.conesalab.org/](http://qualimap.conesalab.org/)


---

## English Documentation

### QualiMap Quality Assessment Tool

**Category**: Quality Control

#### Introduction

Platform-independent application for quality control of alignment sequencing data.

#### Installation

```bash
# Pull the Docker image
docker pull username/qualimap:2.3
```

#### Available Versions

`2.3`, `2.2.2d`

#### Usage

```bash
# Quality control
docker run --rm -v /path/to/data:/data username/qualimap qualimap -i input.fq -o output.html
```

#### Parameters

Run `docker run --rm username/qualimap qualimap --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/qualimap bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/qualimap qualimap [options]
```

#### References

- [http://qualimap.conesalab.org/](http://qualimap.conesalab.org/)
