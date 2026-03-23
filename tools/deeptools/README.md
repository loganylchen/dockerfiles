# deeptools

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### deepTools 高通量测序可视化

**类别**: Python生物工具

#### 简介

用于分析和可视化高通量测序数据的Python工具集。

#### 安装

```bash
# Pull the Docker image
docker pull username/deeptools:3.5.4
```

#### 可用版本

`3.5.4`, `3.5.3`, `3.5.2`, `3.5.1`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/deeptools deeptools --help
```

#### 参数说明

运行 `docker run --rm username/deeptools deeptools --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/deeptools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/deeptools deeptools [options]
```

#### 参考资料

- [https://deeptools.readthedocs.io/](https://deeptools.readthedocs.io/)
- Ramirez, F. et al. (2016). Nucleic Acids Res, 44(W1), W160-W165.


---

## English Documentation

### deepTools NGS Visualization

**Category**: Python Bio Tools

#### Introduction

Python tools for analyzing and visualizing high-throughput sequencing data.

#### Installation

```bash
# Pull the Docker image
docker pull username/deeptools:3.5.4
```

#### Available Versions

`3.5.4`, `3.5.3`, `3.5.2`, `3.5.1`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/deeptools deeptools --help
```

#### Parameters

Run `docker run --rm username/deeptools deeptools --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/deeptools bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/deeptools deeptools [options]
```

#### References

- [https://deeptools.readthedocs.io/](https://deeptools.readthedocs.io/)
- Ramirez, F. et al. (2016). Nucleic Acids Res, 44(W1), W160-W165.
