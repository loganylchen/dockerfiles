#!/usr/bin/env python3
"""
Generate README.md files for all tools in the repository.
Creates bilingual (Chinese/English) documentation.
"""

import os
import re
import subprocess
from pathlib import Path

# Tool metadata database
TOOL_INFO = {
    # Alignment tools
    "minimap2": {
        "cn_name": "Minimap2 长读段比对工具",
        "en_name": "Minimap2 Long Read Aligner",
        "cn_desc": "用于长读段（PacBio/Oxford Nanopore）序列比对的高效工具，支持DNA和RNA序列比对。",
        "en_desc": "A versatile pairwise aligner for genomic and spliced nucleotide sequences, optimized for long reads (PacBio/Oxford Nanopore).",
        "category": "alignment",
        "references": ["https://github.com/lh3/minimap2", "Li, H. (2018). Bioinformatics, 34(18), 3094-3100."]
    },
    "star": {
        "cn_name": "STAR RNA-seq比对工具",
        "en_name": "STAR RNA-seq Aligner",
        "cn_desc": "超快速通用的RNA-seq比对工具，支持拼接感知比对。",
        "en_desc": "Ultrafast universal RNA-seq aligner with splice-aware alignment support.",
        "category": "alignment",
        "references": ["https://github.com/alexdobin/STAR", "Dobin, A. et al. (2013). Bioinformatics, 29(1), 15-21."]
    },
    "hisat2": {
        "cn_name": "HISAT2 分层索引比对工具",
        "en_name": "HISAT2 Hierarchical Indexing Aligner",
        "cn_desc": "快速敏感的拼接感知比对工具，使用分层索引进行基因组比对。",
        "en_desc": "Fast and sensitive alignment for mapping next-generation sequencing reads.",
        "category": "alignment",
        "references": ["https://daehwankimlab.github.io/hisat2/", "Kim, D. et al. (2019). Nat Methods, 12, 357-360."]
    },
    "kallisto": {
        "cn_name": "Kallisto 伪比对工具",
        "en_name": "Kallisto Pseudo-aligner",
        "cn_desc": "快速RNA-seq定量工具，使用伪比对技术实现超快速转录本丰度估计。",
        "en_desc": "Near-optimal RNA-Seq quantification using pseudoalignment for rapid transcript abundance estimation.",
        "category": "quantification",
        "references": ["https://pachterlab.github.io/kallisto/", "Bray, N.L. et al. (2016). Nat Biotechnol, 34, 525-527."]
    },
    "salmon": {
        "cn_name": "Salmon 转录本定量工具",
        "en_name": "Salmon Transcript Quantifier",
        "cn_desc": "快速准确的无比对转录本定量工具，支持选择性比对和伪比对模式。",
        "en_desc": "Fast and bias-aware quantification of transcript expression using selective alignment.",
        "category": "quantification",
        "references": ["https://github.com/COMBINE-lab/salmon", "Patro, R. et al. (2017). Nat Methods, 14, 417-419."]
    },

    # BED/BAM tools
    "bedtools": {
        "cn_name": "BEDTools 基因组算术工具集",
        "en_name": "BEDTools Genomic Arithmetic Suite",
        "cn_desc": "用于基因组算术运算的强大工具集，支持BED、BAM、VCF等格式的操作。",
        "en_desc": "A powerful toolset for genomic arithmetic operations on BED, BAM, VCF and other genomic file formats.",
        "category": "genomic_utils",
        "references": ["https://bedtools.readthedocs.io/", "Quinlan, A.R. & Hall, I.M. (2010). Bioinformatics, 26(6), 841-842."]
    },
    "bedops": {
        "cn_name": "BEDOPS 高性能基因组操作工具",
        "en_name": "BEDOPS High-Performance Genomic Operations",
        "cn_desc": "高性能基因组数据操作工具集，针对大规模基因组数据分析优化。",
        "en_desc": "High-performance genomic data operations suite optimized for large-scale genomic data analysis.",
        "category": "genomic_utils",
        "references": ["https://bedops.readthedocs.io/"]
    },
    "samtools": {
        "cn_name": "Samtools 序列比对工具",
        "en_name": "Samtools Sequence Alignment Tools",
        "cn_desc": "用于处理SAM/BAM/CRAM格式的序列比对数据的工具集。",
        "en_desc": "Tools for manipulating next-generation sequencing data in SAM/BAM/CRAM formats.",
        "category": "genomic_utils",
        "references": ["http://www.htslib.org/"]
    },

    # RNA-seq analysis
    "stringtie": {
        "cn_name": "StringTie 转录本组装工具",
        "en_name": "StringTie Transcript Assembler",
        "cn_desc": "高效的RNA-seq比对数据转录本组装和定量工具。",
        "en_desc": "A fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.",
        "category": "rna_seq",
        "references": ["https://ccb.jhu.edu/software/stringtie/", "Pertea, M. et al. (2015). Nat Biotechnol, 33, 290-295."]
    },
    "gffcompare": {
        "cn_name": "GffCompare 注释比较工具",
        "en_name": "GffCompare Annotation Comparison Tool",
        "cn_desc": "用于比较和评估转录本组装结果与参考注释的工具。",
        "en_desc": "Compare and evaluate transcript assemblies against reference annotations.",
        "category": "rna_seq",
        "references": ["https://ccb.jhu.edu/software/stringtie/gffcompare.shtml"]
    },
    "gffread": {
        "cn_name": "GffRead GFF/GTF处理工具",
        "en_name": "GffRead GFF/GTF Processing Tool",
        "cn_desc": "用于验证、过滤和转换GFF/GTF注释文件的工具。",
        "en_desc": "A tool for validating, filtering, and converting GFF/GTF annotation files.",
        "category": "genomic_utils",
        "references": ["http://ccb.jhu.edu/software/stringtie/gffread.shtml"]
    },

    # Differential expression
    "deseq2": {
        "cn_name": "DESeq2 差异表达分析",
        "en_name": "DESeq2 Differential Expression Analysis",
        "cn_desc": "基于负二项分布的RNA-seq数据差异基因表达分析R包。",
        "en_desc": "R package for differential gene expression analysis based on the negative binomial distribution.",
        "category": "diff_expr",
        "references": ["https://bioconductor.org/packages/DESeq2/", "Love, M.I. et al. (2014). Genome Biol, 15, 550."]
    },
    "edger": {
        "cn_name": "edgeR 差异表达分析",
        "en_name": "edgeR Differential Expression Analysis",
        "cn_desc": "用于差异表达分析的R包，特别适用于小样本量的RNA-seq数据。",
        "en_desc": "R package for differential expression analysis of RNA-seq data, especially suited for small sample sizes.",
        "category": "diff_expr",
        "references": ["https://bioconductor.org/packages/edgeR/", "Robinson, M.D. et al. (2010). Bioinformatics, 26(1), 139-140."]
    },
    "limma": {
        "cn_name": "limma 线性模型分析",
        "en_name": "limma Linear Models for Microarray",
        "cn_desc": "用于基因表达数据分析的R包，支持微阵列和RNA-seq数据。",
        "en_desc": "R package for analyzing gene expression data from microarrays and RNA-seq using linear models.",
        "category": "diff_expr",
        "references": ["https://bioconductor.org/packages/limma/", "Ritchie, M.E. et al. (2015). Nucleic Acids Res, 43(7), e47."]
    },

    # Python tools
    "biopython": {
        "cn_name": "Biopython 生物计算工具",
        "en_name": "Biopython Biological Computation Tools",
        "cn_desc": "用于生物计算的Python工具集，提供序列分析、结构生物学等功能。",
        "en_desc": "Python tools for biological computation including sequence analysis and structural biology.",
        "category": "python_bio",
        "references": ["https://biopython.org/", "Cock, P.J. et al. (2009). Bioinformatics, 25(11), 1422-1423."]
    },
    "deeptools": {
        "cn_name": "deepTools 高通量测序可视化",
        "en_name": "deepTools NGS Visualization",
        "cn_desc": "用于分析和可视化高通量测序数据的Python工具集。",
        "en_desc": "Python tools for analyzing and visualizing high-throughput sequencing data.",
        "category": "python_bio",
        "references": ["https://deeptools.readthedocs.io/", "Ramirez, F. et al. (2016). Nucleic Acids Res, 44(W1), W160-W165."]
    },
    "multiqc": {
        "cn_name": "MultiQC 质控报告聚合工具",
        "en_name": "MultiQC Quality Control Report Aggregator",
        "cn_desc": "聚合多个生物信息学工具的质控报告，生成统一的HTML报告。",
        "en_desc": "Aggregate results from multiple bioinformatics tools into a single HTML report.",
        "category": "qc",
        "references": ["https://multiqc.info/", "Ewels, P. et al. (2016). Bioinformatics, 32(19), 3047-3048."]
    },

    # Nanopore tools
    "nanopolish": {
        "cn_name": "Nanopolish Nanopore数据分析",
        "en_name": "Nanopolish Nanopore Data Analysis",
        "cn_desc": "用于Oxford Nanopore测序数据的信号级分析和变异检测工具。",
        "en_desc": "Signal-level analysis and variant calling for Oxford Nanopore sequencing data.",
        "category": "nanopore",
        "references": ["https://github.com/jts/nanopolish", "Loman, N.J. et al. (2015). Nat Methods, 12, 733-735."]
    },
    "f5c": {
        "cn_name": "f5c Nanopore信号处理",
        "en_name": "f5c Nanopore Signal Processing",
        "cn_desc": "高效的Nanopore信号处理工具，支持事件对齐和甲基化检测。",
        "en_desc": "Efficient Oxford Nanopore signal processing for event alignment and methylation detection.",
        "category": "nanopore",
        "references": ["https://github.com/hasindu2008/f5c"]
    },
    "bonito": {
        "cn_name": "Bonito Nanopore碱基调用",
        "en_name": "Bonito Nanopore Basecaller",
        "cn_desc": "Oxford Nanopore官方的GPU加速碱基调用工具，使用神经网络进行高精度碱基调用。",
        "en_desc": "GPU-accelerated basecaller for Oxford Nanopore sequencing data using neural networks.",
        "category": "nanopore",
        "references": ["https://github.com/nanoporetech/bonito"]
    },

    # Variant calling
    "gatk": {
        "cn_name": "GATK 基因组分析工具包",
        "en_name": "GATK Genome Analysis Toolkit",
        "cn_desc": "用于变异检测和基因组分析的综合性工具包，广泛应用于人类基因组学研究。",
        "en_desc": "Comprehensive toolkit for variant discovery and genotyping, widely used in human genomics research.",
        "category": "variant",
        "references": ["https://gatk.broadinstitute.org/", "Van der Auwera, G.A. et al. (2013). Curr Protoc Bioinformatics, 43, 11.10.1-11.10.33."]
    },
    "picard": {
        "cn_name": "Picard 序列数据处理工具",
        "en_name": "Picard Sequence Data Processing Tools",
        "cn_desc": "用于处理高通量测序数据的Java工具集，包括排序、去重等功能。",
        "en_desc": "Java tools for processing high-throughput sequencing data including sorting and duplicate marking.",
        "category": "variant",
        "references": ["https://broadinstitute.github.io/picard/"]
    },
    "freebayes": {
        "cn_name": "FreeBayes 变异检测工具",
        "en_name": "FreeBayes Variant Detection Tool",
        "cn_desc": "基于单倍型的变异检测工具，适用于多种测序平台数据。",
        "en_desc": "Haplotype-based variant detection tool suitable for multiple sequencing platforms.",
        "category": "variant",
        "references": ["https://github.com/freebayes/freebayes"]
    },

    # SRA tools
    "sratools": {
        "cn_name": "SRA Toolkit 序列数据下载工具",
        "en_name": "SRA Toolkit Sequence Data Download Tools",
        "cn_desc": "用于从NCBI序列读取存档(SRA)下载和处理高通量测序数据的工具集。",
        "en_desc": "Tools for downloading and processing high-throughput sequencing data from NCBI Sequence Read Archive.",
        "category": "download",
        "references": ["https://github.com/ncbi/sra-tools"]
    },

    # QC tools
    "fastp": {
        "cn_name": "fastp 快速质控工具",
        "en_name": "fastp Fast Quality Control Tool",
        "cn_desc": "超快速的FASTQ文件质控和预处理工具，支持过滤、修剪、质量检测等功能。",
        "en_desc": "Ultra-fast all-in-one FASTQ preprocessor with quality control, filtering, and trimming.",
        "category": "qc",
        "references": ["https://github.com/OpenGene/fastp", "Chen, S. et al. (2018). iMeta, e20."]
    },
    "qualimap": {
        "cn_name": "QualiMap 质量评估工具",
        "en_name": "QualiMap Quality Assessment Tool",
        "cn_desc": "用于评估测序数据和比对质量的工具集。",
        "en_desc": "Platform-independent application for quality control of alignment sequencing data.",
        "category": "qc",
        "references": ["http://qualimap.conesalab.org/"]
    },

    # Gene annotation
    "clusterprofiler": {
        "cn_name": "clusterProfiler 功能富集分析",
        "en_name": "clusterProfiler Functional Enrichment Analysis",
        "cn_desc": "用于基因功能富集分析和可视化的R包，支持GO和KEGG分析。",
        "en_desc": "R package for gene functional enrichment analysis and visualization (GO, KEGG, etc.).",
        "category": "annotation",
        "references": ["https://bioconductor.org/packages/clusterProfiler/", "Yu, G. et al. (2012). OMICS, 16(5), 284-287."]
    },

    # Other tools
    "subread": {
        "cn_name": "Subread 序列比对工具",
        "en_name": "Subread Sequence Alignment Tool",
        "cn_desc": "高效的读段比对和特征计数工具，包含featureCounts程序。",
        "en_desc": "High-performance read alignment and feature counting tool, includes featureCounts.",
        "category": "alignment",
        "references": ["http://subread.sourceforge.net/", "Liao, Y. et al. (2013). Nucleic Acids Res, 41(10), e108."]
    },
    "vg": {
        "cn_name": "VG 变异图工具",
        "en_name": "VG Variation Graph Toolkit",
        "cn_desc": "用于构建和分析基因组变异图的工具集，支持图基因组比对。",
        "en_desc": "Tools for building and analyzing genome variation graphs with graph-based alignment.",
        "category": "pangenome",
        "references": ["https://github.com/vgteam/vg"]
    },
    "lftp": {
        "cn_name": "LFTP 文件传输工具",
        "en_name": "LFTP File Transfer Tool",
        "cn_desc": "功能强大的命令行文件传输程序，支持FTP、HTTP、SFTP等多种协议。",
        "en_desc": "Sophisticated command-line file transfer program supporting FTP, HTTP, SFTP, and more.",
        "category": "utility",
        "references": ["https://lftp.yar.ru/"]
    },
}

# Category descriptions
CATEGORIES = {
    "alignment": {"cn": "序列比对", "en": "Sequence Alignment"},
    "quantification": {"cn": "转录本定量", "en": "Transcript Quantification"},
    "genomic_utils": {"cn": "基因组工具", "en": "Genomic Utilities"},
    "rna_seq": {"cn": "RNA-seq分析", "en": "RNA-seq Analysis"},
    "diff_expr": {"cn": "差异表达", "en": "Differential Expression"},
    "python_bio": {"cn": "Python生物工具", "en": "Python Bio Tools"},
    "qc": {"cn": "质量控制", "en": "Quality Control"},
    "nanopore": {"cn": "Nanopore分析", "en": "Nanopore Analysis"},
    "variant": {"cn": "变异检测", "en": "Variant Calling"},
    "download": {"cn": "数据下载", "en": "Data Download"},
    "annotation": {"cn": "功能注释", "en": "Functional Annotation"},
    "pangenome": {"cn": "泛基因组", "en": "Pangenome"},
    "utility": {"cn": "实用工具", "en": "Utility"},
}


def get_versions(tool_dir):
    """Get versions from versions.txt file."""
    versions_file = tool_dir / "versions.txt"
    if versions_file.exists():
        with open(versions_file) as f:
            versions = [line.strip() for line in f if line.strip() and not line.startswith("#")]
            return versions
    return ["latest"]


def detect_tool_type(dockerfile_path):
    """Detect tool type from Dockerfile content."""
    with open(dockerfile_path) as f:
        content = f.read().lower()

    if "r-base" in content or "rscript" in content or "biocmanager" in content:
        return "r"
    elif "python" in content or "pip" in content:
        return "python"
    elif "java" in content or "openjdk" in content or "temurin" in content:
        return "java"
    else:
        return "compiled"


def get_install_command(tool_name, version, tool_type):
    """Generate installation command example."""
    if tool_type == "r":
        return f"docker pull username/{tool_name}:{version}"
    else:
        return f"docker pull username/{tool_name}:{version}"


def get_usage_example(tool_name, tool_type, tool_info):
    """Generate usage example based on tool type."""
    category = tool_info.get("category", "general")

    examples = {
        "alignment": f"""```bash
# Basic alignment
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} -t 4 reference.fa reads.fq > alignment.sam
```""",
        "quantification": f"""```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} index -t transcripts.fa
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```""",
        "diff_expr": f"""```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data username/{tool_name} Rscript analysis.R
```""",
        "qc": f"""```bash
# Quality control
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} -i input.fq -o output.html
```""",
        "nanopore": f"""```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} reads.fq
```""",
    }

    return examples.get(category, f"""```bash
# Basic usage
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} --help
```""")


def generate_readme(tool_name, tool_dir, tool_info=None):
    """Generate README.md for a tool."""
    if tool_info is None:
        tool_info = {
            "cn_name": tool_name,
            "en_name": tool_name,
            "cn_desc": f"{tool_name} 生物信息学工具",
            "en_desc": f"{tool_name} bioinformatics tool",
            "category": "general",
            "references": []
        }

    dockerfile_path = tool_dir / "Dockerfile"
    tool_type = detect_tool_type(dockerfile_path)
    versions = get_versions(tool_dir)
    category = tool_info.get("category", "general")
    category_info = CATEGORIES.get(category, {"cn": "通用", "en": "General"})

    readme_content = f"""# {tool_name}

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### {tool_info['cn_name']}

**类别**: {category_info['cn']}

#### 简介

{tool_info['cn_desc']}

#### 安装

```bash
# Pull the Docker image
docker pull username/{tool_name}:{versions[0]}
```

#### 可用版本

{', '.join(f'`{v}`' for v in versions)}

#### 使用方法

{get_usage_example(tool_name, tool_type, tool_info)}

#### 参数说明

运行 `docker run --rm username/{tool_name} {tool_name} --help` 查看完整参数列表。

#### 示例

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/{tool_name} bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} [options]
```

#### 参考资料

"""

    for ref in tool_info.get("references", []):
        if ref.startswith("http"):
            readme_content += f"- [{ref}]({ref})\n"
        else:
            readme_content += f"- {ref}\n"

    readme_content += f"""

---

## English Documentation

### {tool_info['en_name']}

**Category**: {category_info['en']}

#### Introduction

{tool_info['en_desc']}

#### Installation

```bash
# Pull the Docker image
docker pull username/{tool_name}:{versions[0]}
```

#### Available Versions

{', '.join(f'`{v}`' for v in versions)}

#### Usage

{get_usage_example(tool_name, tool_type, tool_info)}

#### Parameters

Run `docker run --rm username/{tool_name} {tool_name} --help` to see the full parameter list.

#### Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data username/{tool_name} bash

# Run with data volume
docker run --rm -v /path/to/data:/data username/{tool_name} {tool_name} [options]
```

#### References

"""

    for ref in tool_info.get("references", []):
        if ref.startswith("http"):
            readme_content += f"- [{ref}]({ref})\n"
        else:
            readme_content += f"- {ref}\n"

    return readme_content


def main():
    """Generate README files for all tools."""
    tools_dir = Path("tools")

    for tool_dir in sorted(tools_dir.iterdir()):
        if not tool_dir.is_dir():
            continue

        tool_name = tool_dir.name
        dockerfile = tool_dir / "Dockerfile"

        if not dockerfile.exists():
            print(f"Skipping {tool_name}: No Dockerfile found")
            continue

        # Get tool info or use defaults
        tool_info = TOOL_INFO.get(tool_name, None)

        # Generate README
        readme_content = generate_readme(tool_name, tool_dir, tool_info)

        # Write README
        readme_path = tool_dir / "README.md"
        with open(readme_path, "w") as f:
            f.write(readme_content)

        print(f"Generated README for {tool_name}")


if __name__ == "__main__":
    main()
