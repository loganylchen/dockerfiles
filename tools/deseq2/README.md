# deseq2

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### DESeq2 差异表达分析

**类别**: 差异表达

#### 简介

基于负二项分布的RNA-seq数据差异基因表达分析R包。

#### 安装

```bash
# Pull the Docker image
docker pull username/deseq2:1.44.0
```

#### 可用版本

`1.44.0`, `1.42.1`, `1.40.2`

#### 使用方法

```bash
# 运行 R 脚本进行差异表达分析
docker run --rm -v /path/to/data:/data username/deseq2 Rscript analysis.R
```

##### R 脚本示例

```r
# 加载包
library(DESeq2)

# 读取数据
countData <- read.csv("counts.csv", row.names=1)
colData <- read.csv("coldata.csv", row.names=1)

# 创建 DESeqDataSet
dds <- DESeqDataSetFromMatrix(
    countData = countData,
    colData = colData,
    design = ~ condition
)

# 运行分析
dds <- DESeq(dds)

# 获取结果
res <- results(dds, contrast=c("condition", "treated", "control"))

# 保存结果
write.csv(as.data.frame(res), "results.csv")

# 绘制 MA 图
pdf("maplot.pdf")
plotMA(res)
dev.off()
```

##### 常用函数

| 函数 | 说明 |
|------|------|
| `DESeqDataSetFromMatrix()` | 从矩阵创建对象 |
| `DESeq()` | 运行 DESeq2 分析 |
| `results()` | 提取差异表达结果 |
| `lfcShrink()` | 收缩 log2 倍变化 |
| `plotMA()` | 绘制 MA 图 |
| `plotPCA()` | 绘制 PCA 图 |

#### 常见问题

**Q: 输入数据需要什么格式？**
A: 计数矩阵为基因×样本的整数矩阵，样本信息为包含分组信息的数据框。

**Q: 如何选择对比组？**
A: 使用 `contrast=c("condition", "treated", "control")` 指定。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/deseq2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/deseq2 Rscript [script.R]
```

#### 参考资料

- [https://bioconductor.org/packages/DESeq2/](https://bioconductor.org/packages/DESeq2/)
- Love, M.I. et al. (2014). Genome Biol, 15, 550.


---

## English Documentation

### DESeq2 Differential Expression Analysis

**Category**: Differential Expression

#### Introduction

R package for differential gene expression analysis based on the negative binomial distribution.

#### Installation

```bash
# Pull the Docker image
docker pull username/deseq2:1.44.0
```

#### Available Versions

`1.44.0`, `1.42.1`, `1.40.2`

#### Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/deseq2 Rscript analysis.R
```

##### R Script Example

```r
# Load package
library(DESeq2)

# Read data
countData <- read.csv("counts.csv", row.names=1)
colData <- read.csv("coldata.csv", row.names=1)

# Create DESeqDataSet
dds <- DESeqDataSetFromMatrix(
    countData = countData,
    colData = colData,
    design = ~ condition
)

# Run analysis
dds <- DESeq(dds)

# Get results
res <- results(dds, contrast=c("condition", "treated", "control"))

# Save results
write.csv(as.data.frame(res), "results.csv")

# Plot MA plot
pdf("maplot.pdf")
plotMA(res)
dev.off()
```

##### Common Functions

| Function | Description |
|----------|-------------|
| `DESeqDataSetFromMatrix()` | Create object from matrix |
| `DESeq()` | Run DESeq2 analysis |
| `results()` | Extract differential expression |
| `lfcShrink()` | Shrink log2 fold changes |
| `plotMA()` | Plot MA plot |
| `plotPCA()` | Plot PCA plot |

#### FAQ

**Q: What input format is required?**
A: Count matrix as integer genes×samples, and colData with group information.

**Q: How to specify contrast groups?**
A: Use `contrast=c("condition", "treated", "control")`.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/deseq2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/deseq2 Rscript [script.R]
```

#### References

- [https://bioconductor.org/packages/DESeq2/](https://bioconductor.org/packages/DESeq2/)
- Love, M.I. et al. (2014). Genome Biol, 15, 550.
