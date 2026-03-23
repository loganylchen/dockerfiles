# lftp

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### LFTP 文件传输工具

**类别**: 实用工具

#### 简介

功能强大的命令行文件传输程序，支持FTP、HTTP、SFTP等多种协议。

#### 安装

```bash
# Pull the Docker image
docker pull username/lftp:4.9.2
```

#### 可用版本

`4.9.2`

#### 使用方法

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/lftp lftp --help
```

#### 参数说明

运行 `docker run --rm username/lftp lftp --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/lftp bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/lftp lftp [options]
```

#### 参考资料

- [https://lftp.yar.ru/](https://lftp.yar.ru/)


---

## English Documentation

### LFTP File Transfer Tool

**Category**: Utility

#### Introduction

Sophisticated command-line file transfer program supporting FTP, HTTP, SFTP, and more.

#### Installation

```bash
# Pull the Docker image
docker pull username/lftp:4.9.2
```

#### Available Versions

`4.9.2`

#### Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/lftp lftp --help
```

#### Parameters

Run `docker run --rm username/lftp lftp --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/lftp bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/lftp lftp [options]
```

#### References

- [https://lftp.yar.ru/](https://lftp.yar.ru/)
