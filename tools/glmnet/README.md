# GLMnet Regularized Regression

**Category**: Statistics / Machine Learning

## Introduction

R package for elastic net regularized regression.

## Installation

```bash
docker pull btrspg/glmnet:4.1_8
```

## Available Versions

`4.1_8`, `4.1_7`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/glmnet glmnet --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/glmnet bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/glmnet glmnet [options]
```

## References

- [https://glmnet.stanford.edu/](https://glmnet.stanford.edu/)
