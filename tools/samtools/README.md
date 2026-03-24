# Samtools & BCFtools Docker Image

[![Build Status](https://github.com/loganylchen/dockerfiles/actions/workflows/docker-build.yml/badge.svg)](https://github.com/loganylchen/dockerfiles/actions/workflows/docker-build.yml)

Docker image for **samtools** and **bcftools**, the standard tools for manipulating BAM/CRAM/SAM and VCF/BCF files.

## Included Tools

| Tool | Version | Description |
|------|---------|-------------|
| samtools | 1.21 | Utilities for the Sequence Alignment/Map (SAM) format |
| bcftools | 1.21 | Utilities for variant calling and manipulating VCF/BCF files |
| htslib | 1.21 | Underlying library for reading/writing SAM/BAM/CRAM/VCF/BCF |

## Quick Start

```bash
# Pull the image
docker pull btrspg/samtools:1.21

# View a BAM file header
docker run --rm -v /path/to/data:/data btrspg/samtools:1.21 samtools view -H /data/alignment.bam

# Sort a BAM file
docker run --rm -v /path/to/data:/data btrspg/samtools:1.21 \
    samtools sort -o /data/sorted.bam /data/alignment.bam

# Index a BAM file
docker run --rm -v /path/to/data:/data btrspg/samtools:1.21 \
    samtools index /data/alignment.bam

# Call variants with bcftools
docker run --rm -v /path/to/data:/data btrspg/samtools:1.21 \
    bcftools mpileup -f /data/reference.fa /data/alignment.bam | \
    bcftools call -mv -o /data/variants.vcf
```

## Common Use Cases in RNA Modification Detection

### 1. Convert SAM to BAM and sort
```bash
samtools view -bS input.sam | samtools sort -o sorted.bam
samtools index sorted.bam
```

### 2. Filter reads by mapping quality
```bash
samtools view -b -q 20 input.bam -o filtered.bam
```

### 3. Extract reads from specific region
```bash
samtools view -b input.bam chr1:1000-2000 -o region.bam
```

### 4. Get alignment statistics
```bash
samtools flagstat input.bam
samtools stats input.bam | samtools plot-bamstats -p /output/prefix
```

### 5. Merge multiple BAM files
```bash
samtools merge merged.bam sample1.bam sample2.bam sample3.bam
samtools index merged.bam
```

## Build

```bash
docker build -t btrspg/samtools:1.21 .
```

## Build Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `SAMTOOLS_VERSION` | 1.21 | Samtools version |
| `BCFTOOLS_VERSION` | 1.21 | Bcftools version |
| `HTSLIB_VERSION` | 1.21 | HTSlib version |

## Related Images

- `btrspg/minimap2` - Includes samtools alongside minimap2
- `btrspg/nanopolish` - For signal-level analysis

## References

- [Samtools Documentation](http://www.htslib.org/doc/samtools.html)
- [BCFtools Documentation](http://www.htslib.org/doc/bcftools.html)
- [HTSlib Documentation](http://www.htslib.org/)

## License

- Samtools/BCFtools/HTSlib: MIT/BSD-like license
- This Dockerfile: MIT License
