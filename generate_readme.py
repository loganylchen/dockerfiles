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

    # Alternative splicing
    "aspli": {
        "cn_name": "ASpli 可变剪接分析",
        "en_name": "ASpli Alternative Splicing Analysis",
        "cn_desc": "用于RNA-seq数据中可变剪接事件检测和定量的R/Bioconductor包。",
        "en_desc": "R/Bioconductor package for analysis, detection, and quantification of alternative splicing events from RNA-seq data.",
        "category": "splicing",
        "references": ["https://bioconductor.org/packages/ASpli/", "Mancini, E. et al. (2021). Bioinformatics, 37(18), 2884-2891."]
    },
    "dexseq": {
        "cn_name": "DEXSeq 差异外显子使用分析",
        "en_name": "DEXSeq Differential Exon Usage Analysis",
        "cn_desc": "检测RNA-seq数据中差异外显子使用情况的R/Bioconductor包。",
        "en_desc": "R/Bioconductor package for testing differential exon usage in RNA-seq data.",
        "category": "splicing",
        "references": ["https://bioconductor.org/packages/DEXSeq/", "Anders, S. et al. (2012). Genome Res, 22(10), 2008-2017."]
    },
    "irfinder": {
        "cn_name": "IRFinder 内含子保留检测",
        "en_name": "IRFinder Intron Retention Detector",
        "cn_desc": "从RNA-seq数据中检测和定量内含子保留事件的工具。",
        "en_desc": "Tool for detecting and quantifying intron retention events from RNA-seq data.",
        "category": "splicing",
        "references": ["https://github.com/RitchieLabIGH/IRFinder", "Middleton, R. et al. (2017). Genome Res, 27(10), 1726-1737."]
    },
    "junctionseq": {
        "cn_name": "JunctionSeq 差异剪接分析",
        "en_name": "JunctionSeq Differential Junction Analysis",
        "cn_desc": "分析RNA-seq外显子连接和差异剪接使用情况的R/Bioconductor包。",
        "en_desc": "R/Bioconductor package for analyzing differential junction and exon usage from RNA-seq data.",
        "category": "splicing",
        "references": ["https://bioconductor.org/packages/JunctionSeq/", "Hartley, S.W. & Mullikin, J.C. (2016). Nucleic Acids Res, 44(16), e127."]
    },
    "leafcutter": {
        "cn_name": "Leafcutter 内含子剪接分析",
        "en_name": "Leafcutter Intron Splicing Analysis",
        "cn_desc": "基于内含子使用的轻量级可变剪接定量和差异分析工具。",
        "en_desc": "Lightweight tool for quantifying and testing differential intron usage as a proxy for splicing.",
        "category": "splicing",
        "references": ["https://github.com/davidaknowles/leafcutter", "Li, Y.I. et al. (2018). Nat Genet, 50, 151-158."]
    },
    "majiq": {
        "cn_name": "MAJIQ 可变剪接定量",
        "en_name": "MAJIQ Alternative Splicing Quantification",
        "cn_desc": "从RNA-seq数据中检测、定量和可视化局部剪接变异的工具。",
        "en_desc": "Tool for detecting, quantifying, and visualizing local splicing variations from RNA-seq data.",
        "category": "splicing",
        "references": ["https://majiq.biociphers.org/", "Vaquero-Garcia, J. et al. (2016). eLife, 5, e11752."]
    },
    "miso": {
        "cn_name": "MISO 剪接异构体分析",
        "en_name": "MISO Mixture of Isoforms Analysis",
        "cn_desc": "用于估计RNA-seq数据中可变剪接事件PSI值的概率模型工具。",
        "en_desc": "Probabilistic framework for estimating percent-spliced-in (PSI) values of alternatively spliced exons from RNA-seq.",
        "category": "splicing",
        "references": ["https://miso.readthedocs.io/", "Katz, Y. et al. (2010). Nat Methods, 7(12), 1009-1015."]
    },
    "psisigma": {
        "cn_name": "PSI-Sigma 剪接定量",
        "en_name": "PSI-Sigma Splicing Quantification",
        "cn_desc": "基于百分比剪接纳入(PSI)值的可变剪接定量分析工具。",
        "en_desc": "Tool for percent-spliced-in (PSI) based alternative splicing quantification and analysis.",
        "category": "splicing",
        "references": ["https://github.com/wososa/PSI-Sigma", "Lin, K.T. & Krainer, A.R. (2019). Proc Natl Acad Sci USA, 116(33), 16357-16366."]
    },
    "rnaseqlib": {
        "cn_name": "RNAseqLib RNA-seq分析库",
        "en_name": "RNAseqLib RNA-seq Analysis Library",
        "cn_desc": "用于分析剪接模式和从GTF文件创建基因注释的RNA-seq工具库。",
        "en_desc": "RNA-seq library for analyzing splicing patterns and creating gene annotations from GTF files.",
        "category": "splicing",
        "references": ["https://github.com/yarden/rnaseqlib"]
    },
    "sgseq": {
        "cn_name": "SGSeq 剪接图分析",
        "en_name": "SGSeq Splice Graph Analysis",
        "cn_desc": "用于从RNA-seq数据分析外显子使用和剪接位点模式的R/Bioconductor包。",
        "en_desc": "R/Bioconductor package for splice graph analysis of exon usage and splice site patterns from RNA-seq data.",
        "category": "splicing",
        "references": ["https://bioconductor.org/packages/SGSeq/", "Goldstein, L.D. et al. (2016). BMC Bioinformatics, 17, 464."]
    },
    "spladder": {
        "cn_name": "SplAdder 可变剪接检测",
        "en_name": "SplAdder Alternative Splicing Detection",
        "cn_desc": "从RNA-seq比对中检测、定量和分析可变剪接事件的工具。",
        "en_desc": "Tool for detecting, quantifying, and analyzing alternative splicing events from RNA-seq alignments.",
        "category": "splicing",
        "references": ["https://github.com/ratschlab/spladder", "Kahles, A. et al. (2016). Bioinformatics, 32(12), i39-i48."]
    },
    "whippet": {
        "cn_name": "Whippet 快速剪接分析",
        "en_name": "Whippet Fast Splicing Analysis",
        "cn_desc": "基于Julia语言的快速RNA-seq剪接事件分析工具，计算PSI值。",
        "en_desc": "Fast Julia-based RNA-seq splicing analysis tool for quantifying percent-spliced-in (PSI) values.",
        "category": "splicing",
        "references": ["https://github.com/timbitz/Whippet.jl", "Sterne-Weiler, T. et al. (2018). Mol Cell, 72(1), 187-200."]
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

    # RNA modification
    "differr": {
        "cn_name": "Differr RNA修饰检测",
        "en_name": "Differr RNA Modification Detection",
        "cn_desc": "从直接RNA测序数据中检测差异修饰的RNA位点。",
        "en_desc": "Detects differentially modified RNA sites from direct RNA-seq data.",
        "category": "rna_mod",
        "references": ["https://github.com/bartongroup/differr_nanopore_DRS"]
    },
    "directrm": {
        "cn_name": "DirectRM RNA修饰检测",
        "en_name": "DirectRM RNA Modification Detection",
        "cn_desc": "使用深度学习从Nanopore直接RNA测序中检测RNA修饰。",
        "en_desc": "Detects RNA modifications from Nanopore dRNA-seq using deep learning.",
        "category": "rna_mod",
        "references": ["https://github.com/yuxinPenny/DirectRM"]
    },
    "drummer": {
        "cn_name": "DRUMMER RNA修饰分析",
        "en_name": "DRUMMER RNA Modification Analysis",
        "cn_desc": "从RNA-seq比对数据中分析RNA修饰模式。",
        "en_desc": "Analyzes RNA modification patterns from RNA-seq alignments.",
        "category": "rna_mod",
        "references": ["https://github.com/DepledgeLab/DRUMMER"]
    },
    "eligos2": {
        "cn_name": "ELIGOS2 RNA修饰鉴定",
        "en_name": "ELIGOS2 RNA Modification Identification",
        "cn_desc": "从直接RNA测序数据中鉴定RNA修饰。",
        "en_desc": "Identifies RNA modifications from direct RNA-seq data.",
        "category": "rna_mod",
        "references": ["https://gitlab.com/piroonj/eligos2"]
    },
    "epinano": {
        "cn_name": "EpiNano RNA修饰分析",
        "en_name": "EpiNano RNA Modification Analysis",
        "cn_desc": "利用Nanopore测序分析RNA修饰和序列变异。",
        "en_desc": "Analyzes RNA modifications and sequence variants from Nanopore sequencing.",
        "category": "rna_mod",
        "references": ["https://github.com/novoalab/EpiNano"]
    },
    "hamr": {
        "cn_name": "HAMR RNA修饰高通量鉴定",
        "en_name": "HAMR High-throughput RNA Modification Detection",
        "cn_desc": "利用高通量测序检测和定量RNA修饰。",
        "en_desc": "Detects and quantifies RNA modifications using high-throughput sequencing.",
        "category": "rna_mod",
        "references": ["https://github.com/GregoryLab/HAMR"]
    },
    "modtect": {
        "cn_name": "ModTect RNA修饰检测",
        "en_name": "ModTect RNA Modification Detection",
        "cn_desc": "从Nanopore测序数据中检测RNA修饰。",
        "en_desc": "Detects RNA modifications from Nanopore sequencing data.",
        "category": "rna_mod",
        "references": ["https://github.com/ktan8/ModTect"]
    },
    "nanocompore": {
        "cn_name": "Nanocompore RNA修饰比较分析",
        "en_name": "Nanocompore RNA Modification Comparison",
        "cn_desc": "从直接RNA测序中检测差异RNA修饰。",
        "en_desc": "Detects differential RNA modifications from direct RNA-seq.",
        "category": "rna_mod",
        "references": ["https://github.com/tlacombe/nanocompore"]
    },
    "nanocompore1": {
        "cn_name": "Nanocompore 1.x RNA修饰检测",
        "en_name": "Nanocompore 1.x RNA Modification Detection",
        "cn_desc": "Nanopore直接RNA测序的RNA修饰检测工具（1.x版本）。",
        "en_desc": "RNA modification detection from Nanopore dRNA-seq (v1.x branch).",
        "category": "rna_mod",
        "references": ["https://github.com/tlacombe/nanocompore"]
    },
    "rnam5c": {
        "cn_name": "RNA-m5C 甲基化分析",
        "en_name": "RNA-m5C Methylation Analysis",
        "cn_desc": "分析RNA中m5C甲基化修饰。",
        "en_desc": "Analyzes m5C methylation modifications in RNA from sequencing data.",
        "category": "rna_mod",
        "references": ["https://www.nature.com/articles/s41594-019-0218-x"]
    },
    "rnamodivt": {
        "cn_name": "RNAModivt RNA修饰综合分析",
        "en_name": "RNAModivt RNA Modification Integrated Analysis",
        "cn_desc": "系统校准表观转录组图谱的RNA修饰综合分析流程。",
        "en_desc": "Comprehensive pipeline for RNA modification analysis with systematic calibration.",
        "category": "rna_mod",
        "references": ["https://www.nature.com/articles/s41592-021-01280-7"]
    },
    "xpore": {
        "cn_name": "xPore 直接RNA修饰检测",
        "en_name": "xPore Direct RNA Modification Detection",
        "cn_desc": "从直接RNA测序中鉴定差异RNA修饰。",
        "en_desc": "Identifies differential RNA modifications from direct RNA sequencing.",
        "category": "rna_mod",
        "references": ["https://github.com/GoekeLab/xpore"]
    },

    # Deconvolution
    "bayesprism": {
        "cn_name": "BayesPrism 细胞类型解卷积",
        "en_name": "BayesPrism Cell Type Deconvolution",
        "cn_desc": "基于贝叶斯模型的bulk RNA-seq细胞类型解卷积工具。",
        "en_desc": "Bayesian cell type deconvolution from bulk RNA-seq data.",
        "category": "deconvolution",
        "references": ["https://github.com/Danko-Lab/BayesPrism"]
    },
    "bisque": {
        "cn_name": "Bisque 转录组解卷积",
        "en_name": "Bisque Transcriptomic Deconvolution",
        "cn_desc": "基于参考的bulk RNA-seq细胞类型解卷积工具。",
        "en_desc": "Reference-based cell type deconvolution from bulk RNA-seq.",
        "category": "deconvolution",
        "references": ["https://github.com/cozygene/bisque"]
    },
    "deconvseq": {
        "cn_name": "DeconvSeq 解卷积分析",
        "en_name": "DeconvSeq Deconvolution Analysis",
        "cn_desc": "RNA-seq数据的免疫细胞解卷积工具。",
        "en_desc": "Immune cell deconvolution from RNA-seq data.",
        "category": "deconvolution",
        "references": ["https://github.com/rosedu1/deconvSeq"]
    },
    "estimate": {
        "cn_name": "ESTIMATE 肿瘤纯度评估",
        "en_name": "ESTIMATE Tumor Purity Estimation",
        "cn_desc": "估计肿瘤样本中基质细胞和免疫细胞含量。",
        "en_desc": "Estimates stromal and immune content in tumor samples.",
        "category": "deconvolution",
        "references": ["https://r-forge.r-project.org"]
    },
    "immunedeconv": {
        "cn_name": "ImmuneDeconv 免疫细胞解卷积",
        "en_name": "ImmuneDeconv Immune Cell Deconvolution",
        "cn_desc": "从转录组数据中解卷积免疫细胞群。",
        "en_desc": "Deconvolution of immune cell populations from transcriptomic data.",
        "category": "deconvolution",
        "references": ["https://github.com/omnideconv/immunedeconv"]
    },
    "music": {
        "cn_name": "MuSiC 细胞类型解卷积",
        "en_name": "MuSiC Cell Type Deconvolution",
        "cn_desc": "基于单细胞转录组的bulk组织解卷积。",
        "en_desc": "Bulk tissue deconvolution via single-cell transcriptomics.",
        "category": "deconvolution",
        "references": ["https://github.com/xuranw/MuSiC"]
    },
    "scaden": {
        "cn_name": "SCADEN 深度学习解卷积",
        "en_name": "SCADEN Deep Learning Deconvolution",
        "cn_desc": "使用深度学习的单细胞参考细胞类型解卷积。",
        "en_desc": "Cell type deconvolution using deep learning with single-cell reference.",
        "category": "deconvolution",
        "references": ["https://github.com/KevinMenden/scaden"]
    },
    "tidyestimate": {
        "cn_name": "TidyEstimate 肿瘤估值工具",
        "en_name": "TidyEstimate Tumor Estimation Tool",
        "cn_desc": "ESTIMATE的Tidy接口，用于肿瘤纯度分析。",
        "en_desc": "Tidy interface to ESTIMATE for tumor purity analysis.",
        "category": "deconvolution",
        "references": ["https://github.com/KaiAragaki/tidyestimate"]
    },
    "xcell": {
        "cn_name": "xCell 细胞类型评分",
        "en_name": "xCell Cell Type Scoring",
        "cn_desc": "从基因表达数据推断免疫和基质细胞类型。",
        "en_desc": "Infers immune and stromal cell types from gene expression data.",
        "category": "deconvolution",
        "references": ["https://xcell.ucsf.edu/"]
    },

    # Coding potential
    "cpat": {
        "cn_name": "CPAT 编码潜力预测",
        "en_name": "CPAT Coding Potential Assessment",
        "cn_desc": "预测转录本是否具有蛋白质编码潜力。",
        "en_desc": "Predicts whether transcripts have protein-coding potential.",
        "category": "coding_potential",
        "references": ["https://github.com/liguowang/cpat"]
    },
    "cpc2": {
        "cn_name": "CPC2 编码潜力分类器",
        "en_name": "CPC2 Coding Potential Classifier",
        "cn_desc": "将序列分类为蛋白编码或非编码。",
        "en_desc": "Classifies sequences as protein-coding or non-coding.",
        "category": "coding_potential",
        "references": ["https://github.com/gao-lab/CPC2_standalone"]
    },

    # Protein structure / molecular docking
    "autodockvina": {
        "cn_name": "AutoDock Vina 分子对接",
        "en_name": "AutoDock Vina Molecular Docking",
        "cn_desc": "用于计算药物发现的分子对接软件。",
        "en_desc": "Molecular docking software for computational drug discovery.",
        "category": "protein_struct",
        "references": ["https://github.com/ccsb-scripps/AutoDock-Vina"]
    },
    "iupred2a": {
        "cn_name": "IUPred2a 蛋白无序性预测",
        "en_name": "IUPred2a Protein Disorder Prediction",
        "cn_desc": "预测蛋白质中的内在无序区域。",
        "en_desc": "Predicts intrinsically disordered regions in proteins.",
        "category": "protein_struct",
        "references": ["https://iupred.elte.hu/"]
    },
    "meeko": {
        "cn_name": "Meeko 分子准备工具",
        "en_name": "Meeko Molecular Preparation Tool",
        "cn_desc": "为自动化对接工作流准备分子结构。",
        "en_desc": "Prepares molecular structures for automated docking workflows.",
        "category": "protein_struct",
        "references": ["https://github.com/forlilab/meeko"]
    },
    "mgltools": {
        "cn_name": "MGLTools 分子可视化套件",
        "en_name": "MGLTools Molecular Visualization Suite",
        "cn_desc": "用于蛋白质结构分析的分子图形和计算工具。",
        "en_desc": "Molecular graphics and computational tools for protein structure analysis.",
        "category": "protein_struct",
        "references": ["https://ccsb.scripps.edu/mgltools/"]
    },
    "signalp": {
        "cn_name": "SignalP 信号肽预测",
        "en_name": "SignalP Signal Peptide Prediction",
        "cn_desc": "预测蛋白质序列中的信号肽。",
        "en_desc": "Predicts signal peptides in protein sequences.",
        "category": "protein_struct",
        "references": ["https://services.healthtech.dtu.dk/services/SignalP-5.0/"]
    },

    # Gene fusion
    "aeron": {
        "cn_name": "AERON 基因融合检测",
        "en_name": "AERON Gene Fusion Detection",
        "cn_desc": "利用长读段进行转录本定量和基因融合检测。",
        "en_desc": "Transcript quantification and gene-fusion detection using long reads.",
        "category": "fusion",
        "references": ["https://www.biorxiv.org/content/10.1101/2020.01.27.921338v1"]
    },
    "jaffal": {
        "cn_name": "JAFFA 基因融合检测",
        "en_name": "JAFFA Gene Fusion Detection",
        "cn_desc": "从RNA-seq数据中检测基因融合事件。",
        "en_desc": "Detects gene fusion events from RNA-seq data.",
        "category": "fusion",
        "references": ["https://github.com/Oshlack/JAFFA"]
    },
    "longgf": {
        "cn_name": "LongGF 长读段融合检测",
        "en_name": "LongGF Long Read Fusion Detection",
        "cn_desc": "从长读段比对中生成基因融合GTF文件。",
        "en_desc": "Generates gene fusion GTF files from long read BAM alignments.",
        "category": "fusion",
        "references": ["https://github.com/WGLab/LongGF"]
    },
    "genion": {
        "cn_name": "GeniON 基因融合检测",
        "en_name": "GeniON Gene Fusion Detection",
        "cn_desc": "快速序列变异和基因融合检测工具。",
        "en_desc": "Fast sequence variant and gene fusion detection tool.",
        "category": "fusion",
        "references": ["https://github.com/vpc-ccg/genion"]
    },

    # RNA-seq tools (additional)
    "bambu": {
        "cn_name": "Bambu 转录本组装工具",
        "en_name": "Bambu Transcript Assembly Tool",
        "cn_desc": "利用长读段RNA-seq数据进行异构体发现和定量。",
        "en_desc": "Isoform discovery and quantification from long-read RNA-seq data.",
        "category": "rna_seq",
        "references": ["https://bioconductor.org/packages/bambu/"]
    },
    "flair": {
        "cn_name": "FLAIR 转录本注释工具",
        "en_name": "FLAIR Transcript Annotation Tool",
        "cn_desc": "利用长读段进行全长RNA异构体测序和注释。",
        "en_desc": "Full-length RNA isoform sequencing and annotation from long reads.",
        "category": "rna_seq",
        "references": ["https://github.com/BrooksLabUCSC/flair"]
    },
    "sicelore": {
        "cn_name": "SiCeLoRe 单细胞长读段",
        "en_name": "SiCeLoRe Single Cell Long Reads",
        "cn_desc": "利用长读段进行单细胞转录组重建。",
        "en_desc": "Single-cell transcriptome reconstruction from long reads.",
        "category": "rna_seq",
        "references": ["https://github.com/ucagenomix/sicelore"]
    },

    # More splicing tools
    "isoformswitchanalyzer": {
        "cn_name": "IsoformSwitchAnalyzeR 异构体切换分析",
        "en_name": "IsoformSwitchAnalyzeR Isoform Switch Analysis",
        "cn_desc": "分析异构体切换的功能后果。",
        "en_desc": "Analyzes functional consequences of isoform switches.",
        "category": "splicing",
        "references": ["https://bioconductor.org/packages/IsoformSwitchAnalyzeR/"]
    },
    "lafite": {
        "cn_name": "LAFITE 全长异构体聚类",
        "en_name": "LAFITE Full-length Isoform Clustering",
        "cn_desc": "从Nanopore直接RNA测序中聚类全长异构体。",
        "en_desc": "Full-length isoform clustering from Nanopore direct RNA-seq.",
        "category": "splicing",
        "references": ["https://github.com/pythseq/LAFITE"]
    },
    "psinanopore": {
        "cn_name": "PsiNanopore Nanopore剪接分析",
        "en_name": "PsiNanopore Nanopore Splicing Analysis",
        "cn_desc": "从Nanopore测序分析剪接纳入百分比。",
        "en_desc": "Analyzes percent-spliced-in from Nanopore sequencing.",
        "category": "splicing",
        "references": ["https://github.com/RouhanifardLab/PsiNanopore"]
    },
    "regtools": {
        "cn_name": "RegTools 调控突变分析",
        "en_name": "RegTools Regulatory Mutation Analysis",
        "cn_desc": "整合DNA-seq和RNA-seq数据分析突变对基因表达调控和剪接的影响。",
        "en_desc": "Integrates DNA-seq and RNA-seq data to identify mutations associated with regulatory effects on gene expression.",
        "category": "splicing",
        "references": ["https://github.com/griffithlab/regtools"]
    },
    "rmats": {
        "cn_name": "rMATS 可变剪接定量",
        "en_name": "rMATS Alternative Splicing Quantification",
        "cn_desc": "从RNA-seq数据中检测和定量可变剪接事件。",
        "en_desc": "Detects and quantifies alternative splicing events from RNA-seq data.",
        "category": "splicing",
        "references": ["https://rnaseq-mats.sourceforge.io/"]
    },
    "rmatsturbo": {
        "cn_name": "rMATS-turbo 快速剪接分析",
        "en_name": "rMATS-turbo Fast Splicing Analysis",
        "cn_desc": "高性能的可变剪接事件检测工具。",
        "en_desc": "High-performance alternative splicing event detection.",
        "category": "splicing",
        "references": ["https://github.com/Xinglab/rmats-turbo"]
    },
    "splicetools": {
        "cn_name": "SpliceTools 剪接工具集",
        "en_name": "SpliceTools Splicing Tools Suite",
        "cn_desc": "用于分析RNA剪接位点和连接的工具。",
        "en_desc": "Tools for analyzing RNA splice sites and junctions.",
        "category": "splicing",
        "references": []
    },
    "suppa": {
        "cn_name": "SUPPA 剪接变异定量",
        "en_name": "SUPPA Splicing Variation Quantification",
        "cn_desc": "分析和比较可变剪接事件。",
        "en_desc": "Analyzes and compares alternative splicing events.",
        "category": "splicing",
        "references": ["https://github.com/comprna/SUPPA"]
    },

    # Quantification
    "nanocount": {
        "cn_name": "NanoCount 长读段定量",
        "en_name": "NanoCount Long Read Quantification",
        "cn_desc": "长读段测序的转录本丰度估计。",
        "en_desc": "Transcript abundance estimation for long-read sequencing.",
        "category": "quantification",
        "references": ["https://github.com/a-slide/NanoCount"]
    },
    "slow5tools": {
        "cn_name": "slow5tools SLOW5格式工具",
        "en_name": "slow5tools SLOW5 Format Tools",
        "cn_desc": "处理Nanopore测序SLOW5格式文件的工具。",
        "en_desc": "Tools for manipulating SLOW5 files from nanopore sequencing.",
        "category": "nanopore",
        "references": ["https://github.com/hasindu2008/slow5tools"]
    },

    # Annotation
    "ensembldb": {
        "cn_name": "EnsemblDB 基因注释库",
        "en_name": "EnsemblDB Gene Annotation Database",
        "cn_desc": "Ensembl基因组特征数据库的R/Bioconductor包。",
        "en_desc": "R/Bioconductor package for Ensembl genomic feature databases.",
        "category": "annotation",
        "references": ["https://bioconductor.org/packages/ensembldb/"]
    },
    "genekitr": {
        "cn_name": "GeneKitr 基因功能分析",
        "en_name": "GeneKitr Gene Functional Analysis",
        "cn_desc": "用于基因组分析的功能富集和可视化工具。",
        "en_desc": "Functional enrichment and visualization for genomic analysis.",
        "category": "annotation",
        "references": ["https://github.com/GangLiLab/genekitr"]
    },
    "genomicfeatures": {
        "cn_name": "GenomicFeatures 基因组特征工具",
        "en_name": "GenomicFeatures Genomic Feature Tools",
        "cn_desc": "用于基因组特征和注释的R/Bioconductor工具。",
        "en_desc": "R/Bioconductor tools for genomic features and annotations.",
        "category": "annotation",
        "references": ["https://bioconductor.org/packages/GenomicFeatures/"]
    },

    # Differential expression (additional)
    "sva": {
        "cn_name": "SVA 批效应移除",
        "en_name": "SVA Batch Effect Removal",
        "cn_desc": "用于移除批效应的替代变量分析工具。",
        "en_desc": "Surrogate variable analysis for removing batch effects.",
        "category": "diff_expr",
        "references": ["https://bioconductor.org/packages/sva/"]
    },

    # QC
    "rnaseqc": {
        "cn_name": "RNA-SeQC RNA-seq质控",
        "en_name": "RNA-SeQC RNA-seq Quality Control",
        "cn_desc": "RNA-seq实验的综合质量控制工具。",
        "en_desc": "Comprehensive quality control for RNA-seq experiments.",
        "category": "qc",
        "references": ["https://github.com/getzlab/rnaseqc"]
    },

    # Genomic utils (additional)
    "hmmer": {
        "cn_name": "HMMER 序列搜索工具",
        "en_name": "HMMER Sequence Search Tools",
        "cn_desc": "基于隐马尔可夫模型的蛋白质和核酸序列分析工具。",
        "en_desc": "Hidden Markov Model tools for protein and nucleotide sequence analysis.",
        "category": "genomic_utils",
        "references": ["https://eddylab.org/software/hmmer/"]
    },
    "gloritools": {
        "cn_name": "GLORI-tools 基因组分析工具",
        "en_name": "GLORI-tools Genomic Analysis Tools",
        "cn_desc": "基因组和转录组分析流程工具。",
        "en_desc": "Tools for genomic and transcriptomic analysis pipelines.",
        "category": "rna_mod",
        "references": ["https://github.com/liucongcas/GLORI-tools"]
    },

    # Coexpression / network
    "glmnet": {
        "cn_name": "GLMnet 正则化回归",
        "en_name": "GLMnet Regularized Regression",
        "cn_desc": "弹性网络正则化回归的R包。",
        "en_desc": "R package for elastic net regularized regression.",
        "category": "statistics",
        "references": ["https://glmnet.stanford.edu/"]
    },
    "wgcna": {
        "cn_name": "WGCNA 加权基因共表达",
        "en_name": "WGCNA Weighted Gene Coexpression",
        "cn_desc": "加权基因共表达网络分析。",
        "en_desc": "Weighted gene coexpression network analysis.",
        "category": "coexpression",
        "references": ["https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/"]
    },

    # Machine learning
    "mime": {
        "cn_name": "MIME 多指标机器学习",
        "en_name": "MIME Multi-Index Machine Learning",
        "cn_desc": "用于生物标志物发现的机器学习工具。",
        "en_desc": "Machine learning tools for biomarker discovery.",
        "category": "statistics",
        "references": []
    },
    "tape": {
        "cn_name": "TAPE 转录组自编码器",
        "en_name": "TAPE Transcriptome Autoencoder",
        "cn_desc": "用于单细胞转录组学的深度学习工具。",
        "en_desc": "Deep learning for single-cell transcriptomics.",
        "category": "deconvolution",
        "references": ["https://github.com/poseidonchan/TAPE"]
    },

    # Other
    "puree": {
        "cn_name": "PUREE 比对过滤工具",
        "en_name": "PUREE Alignment Filtering Tool",
        "cn_desc": "RNA-seq比对数据的纯化和过滤。",
        "en_desc": "Purifies and filters RNA-seq alignments.",
        "category": "rna_seq",
        "references": ["https://github.com/skandlab/PUREE"]
    },
    "rnasieve": {
        "cn_name": "RNAsieve 转录本定量",
        "en_name": "RNAsieve Transcript Quantification",
        "cn_desc": "RNA序列的快速过滤和定量。",
        "en_desc": "Fast filtering and quantification of RNA sequences.",
        "category": "quantification",
        "references": []
    },
    "nanopolish": {
        "cn_name": "Nanopolish Nanopore数据分析",
        "en_name": "Nanopolish Nanopore Data Analysis",
        "cn_desc": "Oxford Nanopore测序数据的信号级分析和变异检测工具。",
        "en_desc": "Signal-level analysis and variant calling for Oxford Nanopore sequencing data.",
        "category": "nanopore",
        "references": ["https://github.com/jts/nanopolish"]
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
    "splicing": {"cn": "可变剪接", "en": "Alternative Splicing"},
    "rna_mod": {"cn": "RNA修饰", "en": "RNA Modification"},
    "deconvolution": {"cn": "细胞解卷积", "en": "Cell Deconvolution"},
    "coding_potential": {"cn": "编码潜力预测", "en": "Coding Potential"},
    "protein_struct": {"cn": "蛋白质结构", "en": "Protein Structure"},
    "fusion": {"cn": "基因融合", "en": "Gene Fusion"},
    "coexpression": {"cn": "共表达网络", "en": "Coexpression Network"},
    "statistics": {"cn": "统计/机器学习", "en": "Statistics / Machine Learning"},
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
        return f"docker pull btrspg/{tool_name}:{version}"
    else:
        return f"docker pull btrspg/{tool_name}:{version}"


def get_usage_example(tool_name, tool_type, tool_info):
    """Generate usage example based on tool type."""
    category = tool_info.get("category", "general")

    examples = {
        "alignment": f"""```bash
# Basic alignment
docker run --rm -v /path/to/data:/data btrspg/{tool_name} {tool_name} -t 4 reference.fa reads.fq > alignment.sam
```""",
        "quantification": f"""```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data btrspg/{tool_name} {tool_name} index -t transcripts.fa
docker run --rm -v /path/to/data:/data btrspg/{tool_name} {tool_name} quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```""",
        "diff_expr": f"""```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data btrspg/{tool_name} Rscript analysis.R
```""",
        "qc": f"""```bash
# Quality control
docker run --rm -v /path/to/data:/data btrspg/{tool_name} {tool_name} -i input.fq -o output.html
```""",
        "splicing": f"""```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/{tool_name} Rscript analysis.R
```""",
        "nanopore": f"""```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data btrspg/{tool_name} {tool_name} reads.fq
```""",
    }

    return examples.get(category, f"""```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/{tool_name} {tool_name} --help
```""")


def generate_readme(tool_name, tool_dir, tool_info=None):
    """Generate English-only README.md for a tool."""
    if tool_info is None:
        tool_info = {
            "en_name": tool_name,
            "en_desc": f"{tool_name} bioinformatics tool",
            "category": "general",
            "references": []
        }

    dockerfile_path = tool_dir / "Dockerfile"
    tool_type = detect_tool_type(dockerfile_path)
    versions = get_versions(tool_dir)
    category = tool_info.get("category", "general")
    category_info = CATEGORIES.get(category, {"cn": "General", "en": "General"})

    readme_content = f"""# {tool_info['en_name']}

**Category**: {category_info['en']}

## Introduction

{tool_info['en_desc']}

## Installation

```bash
docker pull btrspg/{tool_name}:{versions[0]}
```

## Available Versions

{', '.join(f'`{v}`' for v in versions)}

## Usage

{get_usage_example(tool_name, tool_type, tool_info)}

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/{tool_name} bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/{tool_name} {tool_name} [options]
```

## References

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
