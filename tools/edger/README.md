# edger

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### edgeR 差异表达分析

**类别**: 差异表达

#### 简介

用于差异表达分析的R包，特别适用于小样本量的RNA-seq数据。

#### 安装

```bash
# Pull the Docker image
docker pull username/edger:4.2.1
```

#### 可用版本

`4.2.1`, `4.0.16`, `3.42.4`

#### 使用方法

```bash
# 运行 R 脚本进行差异表达分析
docker run --rm -v /path/to/data:/data username/edger Rscript analysis.R
```

##### R 脚本示例

```r
# 加载包
library(edgeR)

# 读取数据
counts <- read.csv("counts.csv", row.names=1)
group <- factor(c(1,1,1,2,2,2))

# 创建 DGEList 对象
dge <- DGEList(counts=counts, group=group)

# 计算标准化因子 (TMM)
dge <- calcNormFactors(dge, method="TMM")

# 估计离散度
dge <- estimateDisp(dge)

# 精确检验
et <- exactTest(dge, pair=c(1,2))

# 查看结果
topTags(et)

# 保存结果
write.csv(topTags(et, n=Inf), "results.csv")

# 绘制 MD 图
pdf("mdplot.pdf")
plotMD(et)
dev.off()
```

##### 常用函数

| 函数 | 说明 |
|------|------|
| `DGEList()` | 创建 DGEList 对象 |
| `calcNormFactors()` | 计算标准化因子 |
| `estimateDisp()` | 估计离散度 |
| `exactTest()` | 精确检验 |
| `topTags()` | 提取显著基因 |
| `plotMD()` | 绘制 MD 图 |

#### 常见问题

**Q: TMM 标准化是什么？**
A: 加权修剪均值标准化，用于消除样本间组成差异。

**Q: 适合小样本量吗？**
A: 是的，edgeR 特别适合 3-5 个重复的小样本量分析。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/edger bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/edger Rscript [script.R]
```

#### 参考资料

- [https://bioconductor.org/packages/edgeR/](https://bioconductor.org/packages/edgeR/)
- Robinson, M.D. et al. (2010). Bioinformatics, 26(1), 139-140.


---

## English Documentation

### edgeR Differential Expression Analysis

**Category**: Differential Expression

#### Introduction

R package for differential expression analysis of RNA-seq data, especially suited for small sample sizes.

#### Installation

```bash
# Pull the Docker image
docker pull username/edger:4.2.1
```

#### Available Versions

`4.2.1`, `4.0.16`, `3.42.4`

#### Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/edger Rscript analysis.R
```

##### R Script Example

```r
# Load package
library(edgeR)

# Read data
counts <- read.csv("counts.csv", row.names=1)
group <- factor(c(1,1,1,2,2,2))

# Create DGEList object
dge <- DGEList(counts=counts, group=group)

# Calculate normalization factors (TMM)
dge <- calcNormFactors(dge, method="TMM")

# Estimate dispersion
dge <- estimateDisp(dge)

# Exact test
et <- exactTest(dge, pair=c(1,2))

# View results
topTags(et)

# Save results
write.csv(topTags(et, n=Inf), "results.csv")

# Plot MD plot
pdf("mdplot.pdf")
plotMD(et)
dev.off()
```

##### Common Functions

| Function | Description |
|----------|-------------|
| `DGEList()` | Create DGEList object |
| `calcNormFactors()` | Calculate normalization factors |
| `estimateDisp()` | Estimate dispersion |
| `exactTest()` | Exact test |
| `topTags()` | Extract significant genes |
| `plotMD()` | Plot MD plot |

#### FAQ

**Q: What is TMM normalization?**
A: Weighted trimmed mean normalization to remove compositional bias between samples.

**Q: Suitable for small sample sizes?**
A: Yes, edgeR is particularly suitable for small sample sizes (3-5 replicates).

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/edger bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/edger Rscript [script.R]
```

#### References

- [https://bioconductor.org/packages/edgeR/](https://bioconductor.org/packages/edgeR/)
- Robinson, M.D. et al. (2010). Bioinformatics, 26(1), 139-140.
