# limma

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### limma 线性模型分析

**类别**: 差异表达

#### 简介

用于基因表达数据分析的R包，支持微阵列和RNA-seq数据。

#### 安装

```bash
# Pull the Docker image
docker pull username/limma:3.60.4
```

#### 可用版本

`3.60.4`, `3.58.1`, `3.56.2`

#### 使用方法

```bash
# 运行 R 脚本进行差异表达分析
docker run --rm -v /path/to/data:/data username/limma Rscript analysis.R
```

##### RNA-seq 分析示例 (voom)

```r
# 加载包
library(limma)
library(edgeR)

# 读取数据
counts <- read.csv("counts.csv", row.names=1)
group <- factor(c("control", "control", "treated", "treated"))

# 创建 DGEList 并进行 voom 转换
dge <- DGEList(counts=counts)
dge <- calcNormFactors(dge)
v <- voom(dge, design=model.matrix(~group), plot=TRUE)

# 拟合线性模型
fit <- lmFit(v, design=model.matrix(~group))
fit <- eBayes(fit)

# 提取结果
results <- topTable(fit, coef="grouptreated", number=Inf, adjust="BH")

# 保存结果
write.csv(results, "results.csv")
```

##### 常用函数

| 函数 | 说明 |
|------|------|
| `lmFit()` | 拟合线性模型 |
| `eBayes()` | 经验贝叶斯统计 |
| `topTable()` | 提取差异表达基因 |
| `voom()` | RNA-seq 数据转换 |
| `makeContrasts()` | 创建比较矩阵 |

#### 常见问题

**Q: 什么时候应该用 limma 而不是 DESeq2？**
A: limma-voom 适合大样本量和复杂实验设计，DESeq2 适合小样本量。

**Q: voom 转换是什么？**
A: 将 RNA-seq 计数数据转换为适合线性模型的 log2-CPM 数据。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/limma bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/limma Rscript [script.R]
```

#### 参考资料

- [https://bioconductor.org/packages/limma/](https://bioconductor.org/packages/limma/)
- Ritchie, M.E. et al. (2015). Nucleic Acids Res, 43(7), e47.


---

## English Documentation

### limma Linear Models for Microarray

**Category**: Differential Expression

#### Introduction

R package for analyzing gene expression data from microarrays and RNA-seq using linear models.

#### Installation

```bash
# Pull the Docker image
docker pull username/limma:3.60.4
```

#### Available Versions

`3.60.4`, `3.58.1`, `3.56.2`

#### Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/limma Rscript analysis.R
```

##### RNA-seq Analysis Example (voom)

```r
# Load packages
library(limma)
library(edgeR)

# Read data
counts <- read.csv("counts.csv", row.names=1)
group <- factor(c("control", "control", "treated", "treated"))

# Create DGEList and apply voom
dge <- DGEList(counts=counts)
dge <- calcNormFactors(dge)
v <- voom(dge, design=model.matrix(~group), plot=TRUE)

# Fit linear model
fit <- lmFit(v, design=model.matrix(~group))
fit <- eBayes(fit)

# Extract results
results <- topTable(fit, coef="grouptreated", number=Inf, adjust="BH")

# Save results
write.csv(results, "results.csv")
```

##### Common Functions

| Function | Description |
|----------|-------------|
| `lmFit()` | Fit linear model |
| `eBayes()` | Empirical Bayes statistics |
| `topTable()` | Extract DE genes |
| `voom()` | RNA-seq data transformation |
| `makeContrasts()` | Create contrast matrix |

#### FAQ

**Q: When to use limma vs DESeq2?**
A: limma-voom is better for large sample sizes and complex designs, DESeq2 for small samples.

**Q: What is voom transformation?**
A: Transforms RNA-seq counts to log2-CPM data suitable for linear modeling.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/limma bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/limma Rscript [script.R]
```

#### References

- [https://bioconductor.org/packages/limma/](https://bioconductor.org/packages/limma/)
- Ritchie, M.E. et al. (2015). Nucleic Acids Res, 43(7), e47.
