# LFTP File Transfer Tool

**Category**: Utility

## Introduction

Sophisticated command-line file transfer program supporting FTP, HTTP, SFTP, and more.

## Installation

```bash
docker pull btrspg/lftp:4.9.2
```

## Available Versions

`4.9.2`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/lftp lftp --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/lftp bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/lftp lftp [options]
```

## References

- [https://lftp.yar.ru/](https://lftp.yar.ru/)
