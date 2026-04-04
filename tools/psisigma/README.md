# psisigma

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### PSI-Sigma 剪接定量

**类别**: 可变剪接

#### 简介

基于百分比剪接纳入(PSI)值的可变剪接定量分析工具。

#### 安装

```bash
# Pull the Docker image
docker pull btrspg/psisigma:1.9
```

#### 可用版本

`1.9`

#### 使用方法

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/psisigma Rscript analysis.R
```

#### 参数说明

运行 `docker run --rm btrspg/psisigma psisigma --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/psisigma bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/psisigma psisigma [options]
```

#### 参考资料

- [https://github.com/wososa/PSI-Sigma](https://github.com/wososa/PSI-Sigma)
- Lin, K.T. & Krainer, A.R. (2019). Proc Natl Acad Sci USA, 116(33), 16357-16366.


---

## English Documentation

### PSI-Sigma Splicing Quantification

**Category**: Alternative Splicing

#### Introduction

Tool for percent-spliced-in (PSI) based alternative splicing quantification and analysis.

#### Installation

```bash
# Pull the Docker image
docker pull btrspg/psisigma:1.9
```

#### Available Versions

`1.9`

#### Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/psisigma Rscript analysis.R
```

#### Parameters

Run `docker run --rm btrspg/psisigma psisigma --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/psisigma bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/psisigma psisigma [options]
```

#### References

- [https://github.com/wososa/PSI-Sigma](https://github.com/wososa/PSI-Sigma)
- Lin, K.T. & Krainer, A.R. (2019). Proc Natl Acad Sci USA, 116(33), 16357-16366.
