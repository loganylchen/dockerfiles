# PSI-Sigma Splicing Quantification

**Category**: Alternative Splicing

## Introduction

Tool for percent-spliced-in (PSI) based alternative splicing quantification and analysis.

## Installation

```bash
docker pull btrspg/psisigma:1.9
```

## Available Versions

`1.9`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/psisigma Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/psisigma bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/psisigma psisigma [options]
```

## References

- [https://github.com/wososa/PSI-Sigma](https://github.com/wososa/PSI-Sigma)
- Lin, K.T. & Krainer, A.R. (2019). Proc Natl Acad Sci USA, 116(33), 16357-16366.
