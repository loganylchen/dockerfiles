# lafite

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### lafite

**类别**: 通用

#### 简介

lafite 生物信息学工具

#### 安装

```bash
# Pull the Docker image
docker pull username/lafite:1.0.2
```

#### 可用版本

`1.0.2`, `1.0.1`, `1.0.0`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/lafite lafite --help
```

#### 参数说明

运行 `docker run --rm username/lafite lafite --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/lafite bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/lafite lafite [options]
```

#### 参考资料



---

## English Documentation

### lafite

**Category**: General

#### Introduction

lafite bioinformatics tool

#### Installation

```bash
# Pull the Docker image
docker pull username/lafite:1.0.2
```

#### Available Versions

`1.0.2`, `1.0.1`, `1.0.0`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/lafite lafite --help
```

#### Parameters

Run `docker run --rm username/lafite lafite --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/lafite bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/lafite lafite [options]
```

#### References

