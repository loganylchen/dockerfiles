# pod5

**Category**: Nanopore Signal / File Format

## Introduction

Oxford Nanopore POD5 file format Python API and CLI tools. Inspect,
convert (fast5 <=> pod5), subset, merge, repack, and update `.pod5` files.

## Installation

```bash
docker pull btrspg/pod5:0.3.39
```

## Available Versions

`0.3.39`

## Usage

```bash
# Show pod5 summary / read info
docker run --rm -v /path/to/data:/data btrspg/pod5 pod5 inspect summary reads.pod5

# Convert fast5 -> pod5
docker run --rm -v /path/to/data:/data btrspg/pod5 pod5 convert fast5 input.fast5 --output reads.pod5

# Merge / subset
docker run --rm -v /path/to/data:/data btrspg/pod5 pod5 merge in1.pod5 in2.pod5 --output merged.pod5
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/pod5 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/pod5 pod5 [subcommand] [options]
```

## References

- [https://github.com/nanoporetech/pod5-file-format](https://github.com/nanoporetech/pod5-file-format)
- [https://pod5-file-format.readthedocs.io](https://pod5-file-format.readthedocs.io)
