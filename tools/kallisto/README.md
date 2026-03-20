# kallisto

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### Kallisto 伪比对工具

**类别**: 转录本定量

#### 简介

快速RNA-seq定量工具，使用伪比对技术实现超快速转录本丰度估计。

#### 安装

```bash
# Pull the Docker image
docker pull username/kallisto:0.52.0
```

#### 可用版本

`0.52.0`, `0.51.1`, `0.50.1`, `0.48.0`

#### 使用方法

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data username/kallisto kallisto index -t transcripts.fa
docker run --rm -v /path/to/data:/data username/kallisto kallisto quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

#### 参数说明

运行 `docker run --rm username/kallisto kallisto --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/kallisto bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/kallisto kallisto [options]
```

#### 参考资料

- [https://pachterlab.github.io/kallisto/](https://pachterlab.github.io/kallisto/)
- Bray, N.L. et al. (2016). Nat Biotechnol, 34, 525-527.


---

## English Documentation

### Kallisto Pseudo-aligner

**Category**: Transcript Quantification

#### Introduction

Near-optimal RNA-Seq quantification using pseudoalignment for rapid transcript abundance estimation.

#### Installation

```bash
# Pull the Docker image
docker pull username/kallisto:0.52.0
```

#### Available Versions

`0.52.0`, `0.51.1`, `0.50.1`, `0.48.0`

#### Usage

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data username/kallisto kallisto index -t transcripts.fa
docker run --rm -v /path/to/data:/data username/kallisto kallisto quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

#### Parameters

Run `docker run --rm username/kallisto kallisto --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/kallisto bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/kallisto kallisto [options]
```

#### References

- [https://pachterlab.github.io/kallisto/](https://pachterlab.github.io/kallisto/)
- Bray, N.L. et al. (2016). Nat Biotechnol, 34, 525-527.
