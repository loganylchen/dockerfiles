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
# 1. 构建转录本索引
docker run --rm -v /path/to/data:/data username/kallisto \
    kallisto index -i transcripts.idx transcripts.fa

# 2. 双端数据定量
docker run --rm -v /path/to/data:/data username/kallisto \
    kallisto quant -i transcripts.idx -o output -b 100 R1.fq R2.fq

# 3. 单端数据定量
docker run --rm -v /path/to/data:/data username/kallisto \
    kallisto quant -i transcripts.idx -o output --single -l 200 -s 20 reads.fq
```

#### 主要参数

| 参数 | 说明 |
|------|------|
| `index` | 构建索引 |
| `quant` | 定量分析 |
| `-i` | 索引文件 |
| `-o` | 输出目录 |
| `-b` | Bootstrap 样本数 |
| `--single` | 单端模式 |
| `-l/-s` | 片段长度和标准差 |

#### 常见问题

**Q: 为什么需要 bootstrap？**
A: Bootstrap 用于估计表达量的不确定性，用于后续差异分析。

**Q: 输出的 TPM 和 counts 有什么区别？**
A: TPM 是归一化的表达量，counts 是原始计数。差异分析建议使用 counts。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/kallisto bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/kallisto kallisto [command] [options]
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
# 1. Build transcript index
docker run --rm -v /path/to/data:/data username/kallisto \
    kallisto index -i transcripts.idx transcripts.fa

# 2. Paired-end quantification
docker run --rm -v /path/to/data:/data username/kallisto \
    kallisto quant -i transcripts.idx -o output -b 100 R1.fq R2.fq

# 3. Single-end quantification
docker run --rm -v /path/to/data:/data username/kallisto \
    kallisto quant -i transcripts.idx -o output --single -l 200 -s 20 reads.fq
```

#### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `index` | Build index |
| `quant` | Quantification |
| `-i` | Index file |
| `-o` | Output directory |
| `-b` | Number of bootstrap samples |
| `--single` | Single-end mode |
| `-l/-s` | Fragment length and std dev |

#### FAQ

**Q: Why is bootstrap needed?**
A: Bootstrap estimates uncertainty in expression levels for downstream differential analysis.

**Q: Difference between TPM and counts?**
A: TPM is normalized expression, counts are raw. Use counts for differential analysis.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/kallisto bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/kallisto kallisto [command] [options]
```

#### References

- [https://pachterlab.github.io/kallisto/](https://pachterlab.github.io/kallisto/)
- Bray, N.L. et al. (2016). Nat Biotechnol, 34, 525-527.
