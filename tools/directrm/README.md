# DirectRM Docker Image

RNA modification detection from Nanopore direct RNA sequencing data using deep learning.

## Version

- **DirectRM**: v1.0 (default) - use `--build-arg VERSION=<tag|branch|commit>` to specify
- **Dorado**: 0.6.2 - use `--build-arg DORADO_VERSION=<version>` to specify
- **CUDA**: 11.8 (runtime) with cuDNN 8

## Tools Included

| Tool | Version | Description |
|------|---------|-------------|
| DirectRM | v1.0 | RNA modification detection (ac4C, m1A, m5C, m7G, m6A, pseudouridine) |
| Dorado | 0.6.2 | Base calling for Nanopore data |
| Remora | latest | Feature extraction for modification detection |
| Samtools | latest | BAM/SAM file processing |

## Supported Sequencing Kits

- **SQK-RNA002** (5-mer chemistry)
- **SQK-RNA004** (9-mer chemistry)

## Environment Isolation

This image uses Conda to manage two isolated environments, both using CUDA 11.8:

- **directrm**: Python 3.11, PyTorch 2.1.2+cu118
  - faiss-gpu==1.8.0, transformers==4.38.2
  - xgboost, einops, statsmodels, biopython, pysam

- **remora**: Python 3.9, PyTorch 2.3.0+cu118
  - CUDA 11.8 compatible for consistent runtime

## Build

```bash
# Build with default versions (DirectRM: v1.0, Dorado: 0.6.2)
docker build -t directrm:latest tools/directrm/

# Build with specific DirectRM tag/branch
docker build --build-arg VERSION=v1.0 -t directrm:v1.0 tools/directrm/

# Build with specific Dorado version
docker build --build-arg DORADO_VERSION=0.6.2 -t directrm:latest tools/directrm/

# Available DirectRM versions (see tools/directrm/versions.txt):
#   v1.0
```

## Usage

### Using the Integrated Pipeline (Recommended)

```bash
docker run --gpus all -v /path/to/data:/data directrm:v1.0 \
    /opt/directrm_pipeline.sh \
    --input /data/pod5_data \
    --reference /data/reference.fa \
    --regions /data/target_regions.csv \
    --output /data/results \
    --rna004
```

**Required arguments:**
- `--input DIR`: Input directory containing POD5 files
- `--reference FILE`: Reference FASTA file
- `--regions FILE`: Target regions CSV file (columns: seqnames,start,end,width,strand)
- `--output DIR`: Output directory for results

**Sequencing kit:**
- `--rna002`: Use SQK-RNA002 kit models (5-mer analysis)
- `--rna004`: Use SQK-RNA004 kit models (9-mer analysis) [DEFAULT]

### Base Calling with Dorado

```bash
# RNA002 kit
docker run --gpus all -v /data:/data directrm:v1.0 \
    dorado basecaller rna002_70bps_hac@v3 /data/pod5_dir | \
    samtools sort -o /data/calls.bam

# RNA004 kit
docker run --gpus all -v /data:/data directrm:v1.0 \
    dorado basecaller rna004_130bps_hac@v3.0.1 /data/pod5_dir | \
    samtools sort -o /data/calls.bam
```

### DirectRM Python Scripts

```bash
# Run preprocessing in DirectRM environment
docker run --gpus all -v /data:/data directrm:v1.0 \
    directrm_run /opt/DirectRM/scripts/preprocessing.py --help

# Run feature extraction
docker run --gpus all -v /data:/data directrm:v1.0 \
    directrm_run /opt/DirectRM/scripts/feature_extraction.py --help
```

### Feature Extraction with Remora

```bash
docker run --gpus all -v /data:/data directrm:v1.0 \
    remora_run call_mods --bam /data/input.bam --output /data/mods.bam
```

## Pipeline Steps

The `directrm_pipeline.sh` script implements the complete workflow:

1. **Preprocessing**: Base calling and alignment with Dorado
2. **Feature Extraction**: Extract signal-level features with Remora
3. **De Novo Detection**: Identify candidate modification sites
4. **Inference**: Predict modification probabilities with DirectRM
5. **Aggregation**: Combine results across reads

## Model Files

The image includes the directory structure for DirectRM models:

```
/opt/DirectRM/model/
├── RNA002/           # For SQK-RNA002 kit (5-mer)
│   ├── id3_binary/   # De novo detection model
│   ├── ml1/, ml2/    # Integrated inference models
│   └── *_m1/, *_m2/  # Individual modification models
└── RNA004/           # For SQK-RNA004 kit (9-mer)
    └── (same structure)
```

**Note**: Model files must be downloaded separately and mounted into the image.

## Data Files

- `/opt/DirectRM/5mer_levels_v1.txt` - RNA002 k-mer levels
- `/opt/DirectRM/9mer_levels_v1.txt` - RNA004 k-mer levels

## Requirements

- Docker with NVIDIA Container Toolkit
- GPU with CUDA support (compute capability >= 7.0)
- At least 16GB VRAM recommended
- Input: POD5 files for full pipeline, or pre-basecalled BAM files

## Environment Variables

- `DIRECTRM_DIR`: Path to DirectRM installation (default: /opt/DirectRM)
- `CUDA_VISIBLE_DEVICES`: GPU devices to use

## Wrapper Scripts

- `directrm_run`: Run Python scripts in the DirectRM conda environment
- `remora_run`: Run Remora commands in the Remora conda environment

## References

- [DirectRM GitHub](https://github.com/yuxinPenny/DirectRM)
- [Dorado Documentation](https://github.com/nanoporetech/dorado)
- [Remora GitHub](https://github.com/nanoporetech/remora)
