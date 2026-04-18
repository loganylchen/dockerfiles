# FastQC

Quality control tool for high-throughput sequencing data.

- Source: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
- License: GPL-3.0

## Usage

```bash
docker run --rm -v "$PWD:/data" <image> fastqc sample.fastq.gz -o /data
```
