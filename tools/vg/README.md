# vg

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### VG 变异图工具

**类别**: 泛基因组

#### 简介

用于构建和分析基因组变异图的工具集，支持图基因组比对。

#### 安装

```bash
# Pull the Docker image
docker pull username/vg:1.59.0
```

#### 可用版本

`1.59.0`, `1.56.0`, `1.53.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/vg vg --help
```

#### 参数说明

运行 `docker run --rm username/vg vg --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/vg bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/vg vg [options]
```

#### 参考资料

- [https://github.com/vgteam/vg](https://github.com/vgteam/vg)


---

## English Documentation

### VG Variation Graph Toolkit

**Category**: Pangenome

#### Introduction

Tools for building and analyzing genome variation graphs with graph-based alignment.

#### Installation

```bash
# Pull the Docker image
docker pull username/vg:1.59.0
```

#### Available Versions

`1.59.0`, `1.56.0`, `1.53.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/vg vg --help
```

#### Parameters

Run `docker run --rm username/vg vg --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/vg bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/vg vg [options]
```

#### References

- [https://github.com/vgteam/vg](https://github.com/vgteam/vg)
