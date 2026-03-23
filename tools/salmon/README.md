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
# 1. 构建转录本索引
docker run --rm -v /path/to/data:/data username/salmon \
    salmon index -t transcripts.fa -i transcripts_index

# 2. 双端数据定量
docker run --rm -v /path/to/data:/data username/salmon \
    salmon quant -i transcripts_index -l A -1 R1.fq -2 R2.fq -p 8 -o output

# 3. 链特异性 RNA-seq
docker run --rm -v /path/to/data:/data username/salmon \
    salmon quant -i transcripts_index -l ISR -1 R1.fq -2 R2.fq -p 8 -o output

# 4. 启用 GC 偏好校正
docker run --rm -v /path/to/data:/data username/salmon \
    salmon quant -i transcripts_index -l A -1 R1.fq -2 R2.fq --gcBias --seqBias -p 8 -o output
```

#### 主要参数

| 参数 | 说明 |
|------|------|
| `index` | 构建索引 |
| `quant` | 定量分析 |
| `-i` | 索引目录 |
| `-l` | 文库类型 (A=自动检测) |
| `-1/-2` | 输入文件 |
| `-p` | 线程数 |
| `--gcBias` | GC 偏好校正 |
| `--seqBias` | 序列偏好校正 |
| `--validateMappings` | 验证比对 |

#### 文库类型

| 类型 | 说明 |
|------|------|
| `A` | 自动检测（推荐） |
| `ISR` | First-strand / Reverse |
| `ISF` | First-strand / Forward |
| `IU` | Inward Unstranded |

#### 常见问题

**Q: salmon 与 kallisto 如何选择？**
A: salmon 使用选择性比对，kallisto 使用伪比对。两者结果相近，salmon 通常稍快。

**Q: 什么时候需要校正 GC 偏好？**
A: GC 含量偏差较大的数据，建议启用 `--gcBias`。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/salmon bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/salmon salmon [command] [options]
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
# 1. Build transcript index
docker run --rm -v /path/to/data:/data username/salmon \
    salmon index -t transcripts.fa -i transcripts_index

# 2. Paired-end quantification
docker run --rm -v /path/to/data:/data username/salmon \
    salmon quant -i transcripts_index -l A -1 R1.fq -2 R2.fq -p 8 -o output

# 3. Strand-specific RNA-seq
docker run --rm -v /path/to/data:/data username/salmon \
    salmon quant -i transcripts_index -l ISR -1 R1.fq -2 R2.fq -p 8 -o output

# 4. Enable GC bias correction
docker run --rm -v /path/to/data:/data username/salmon \
    salmon quant -i transcripts_index -l A -1 R1.fq -2 R2.fq --gcBias --seqBias -p 8 -o output
```

#### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `index` | Build index |
| `quant` | Quantification |
| `-i` | Index directory |
| `-l` | Library type (A=auto) |
| `-1/-2` | Input files |
| `-p` | Number of threads |
| `--gcBias` | GC bias correction |
| `--seqBias` | Sequence bias correction |
| `--validateMappings` | Validate mappings |

#### Library Types

| Type | Description |
|------|-------------|
| `A` | Auto-detect (recommended) |
| `ISR` | First-strand / Reverse |
| `ISF` | First-strand / Forward |
| `IU` | Inward Unstranded |

#### FAQ

**Q: salmon vs kallisto?**
A: salmon uses selective alignment, kallisto uses pseudoalignment. Similar results, salmon is often faster.

**Q: When to use GC bias correction?**
A: Recommended for data with significant GC content bias using `--gcBias`.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/salmon bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/salmon salmon [command] [options]
```

#### References

- [https://github.com/COMBINE-lab/salmon](https://github.com/COMBINE-lab/salmon)
- Patro, R. et al. (2017). Nat Methods, 14, 417-419.
