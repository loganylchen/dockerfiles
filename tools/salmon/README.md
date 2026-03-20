# salmon

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Salmon 转录本定量工具

**类别**: 转录本定量

#### 简介

快速准确的无比对转录本定量工具，支持选择性比对和伪比对模式。

#### 安装

```bash
# Pull the Docker image
docker pull username/salmon:1.10.3
```

#### 可用版本

`1.10.3`, `1.10.0`, `1.9.0`

#### 使用方法

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data username/salmon salmon index -t transcripts.fa
docker run --rm -v /path/to/data:/data username/salmon salmon quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

#### 参数说明

运行 `docker run --rm username/salmon salmon --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/salmon bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/salmon salmon [options]
```

#### 参考资料

- [https://github.com/COMBINE-lab/salmon](https://github.com/COMBINE-lab/salmon)
- Patro, R. et al. (2017). Nat Methods, 14, 417-419.


---

## English Documentation

### Salmon Transcript Quantifier

**Category**: Transcript Quantification

#### Introduction

Fast and bias-aware quantification of transcript expression using selective alignment.

#### Installation

```bash
# Pull the Docker image
docker pull username/salmon:1.10.3
```

#### Available Versions

`1.10.3`, `1.10.0`, `1.9.0`

#### Usage

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data username/salmon salmon index -t transcripts.fa
docker run --rm -v /path/to/data:/data username/salmon salmon quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

#### Parameters

Run `docker run --rm username/salmon salmon --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/salmon bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/salmon salmon [options]
```

#### References

- [https://github.com/COMBINE-lab/salmon](https://github.com/COMBINE-lab/salmon)
- Patro, R. et al. (2017). Nat Methods, 14, 417-419.
