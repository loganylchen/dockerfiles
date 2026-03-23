# Dockerfiles for Bioinformatics Tools

A collection of Dockerfiles for bioinformatics tools, maintained by [Yuelong CHEN](mailto:yuelong.chen.btr@gmail.com).

## ✅ Verified Tools

These tools have been tested and verified to build successfully:

| Tool | Version | Description | Status |
|------|---------|-------------|--------|
| **aeron** | c77c73a | Transcript quantification and gene-fusion detection using long reads | ✅ Fixed |
| **bedops** | 2.4.42 | Genomic interval analysis toolkit | ✅ Fixed |
| **differr** | 0.2 | Differential expression analysis | ✅ Fixed |
| **epinano** | 1.2.5 | Detection of RNA modifications from Nanopore DRS | ✅ Fixed |
| **fastp** | 0.24.0 | Ultrafast FASTQ preprocessing | ✅ Fixed |
| **gffcompare** | 0.12.10 | GFF/GTF comparison and classification | ✅ Fixed |
| **gffread** | 0.12.7 | GFF/GTF utility | ✅ Fixed |
| **genion** | 1.1.1 | Gene fusion detection | ✅ Fixed |
| **jaffal** | 2.2, 2.3 | Fusion gene detection from long reads | ✅ Fixed |
| **kallisto** | 0.52.0 | Near-optimal RNA-Seq quantification | ✅ Fixed |
| **lafite** | 1.0.2 | Full-length isoform clustering from Nanopore DRS | ✅ Verified |
| **meeko** | 0.7.1 | Interface for AutoDock | ✅ Verified |

## 📋 TODO - Tools Needing Fixes

These tools have known build issues and need to be fixed:

| Tool | Version | Issue | Priority |
|------|---------|-------|----------|
| **gloritools** | latest | wget download fails | 🔴 High |
| **mgltools** | 1.5.7 | wget download fails (SourceForge) | 🔴 High |

## 📦 All Available Tools

| Tool Name | Reference | Version List |
|-----------|-----------|--------------|
| aeron | [AERON: Transcript quantification and gene-fusion detection using long reads](https://www.biorxiv.org/content/10.1101/2020.01.27.921338v1.full) | ![aeron Version](https://img.shields.io/badge/aeron-c77c73a4bdeb6fb21fa7522239b2276e27ea10f8-blue) |
| autodock vina | | |
| bambu | [Context-aware transcript quantification from long-read RNA-seq data with Bambu](https://www.nature.com/articles/s41592-023-01908-w) | ![bambu Version](https://img.shields.io/badge/bambu-3.8.3-blue) ![bambu Version](https://img.shields.io/badge/bambu-3.4.0-blue) ![bambu Version](https://img.shields.io/badge/bambu-3.2.4-blue) |
| bedops | | ![bedops Version](https://img.shields.io/badge/bedops-2.4.42-blue) ![bedops Version](https://img.shields.io/badge/bedops-2.4.41-blue) ![bedops Version](https://img.shields.io/badge/bedops-2.4.40-blue) |
| bedtools | | ![bedtools Version](https://img.shields.io/badge/bedtools-2.31.1-blue) ![bedtools Version](https://img.shields.io/badge/bedtools-2.31.0-blue) ![bedtools Version](https://img.shields.io/badge/bedtools-2.30.0-blue) |
| biopython | [Biopython: freely available Python tools for computational molecular biology and bioinformatics](http://dx.doi.org/10.1093/bioinformatics/btp163) | ![biopython Version](https://img.shields.io/badge/biopython-1.85-blue) ![biopython Version](https://img.shields.io/badge/biopython-1.84-blue) ![biopython Version](https://img.shields.io/badge/biopython-1.83-blue) ![biopython Version](https://img.shields.io/badge/biopython-1.82-blue) |
| bisque | | |
| bonito | [https://github.com/nanoporetech/bonito](https://github.com/nanoporetech/bonito) | ![bonito Version](https://img.shields.io/badge/bonito-0.9.0-blue) ![bonito Version](https://img.shields.io/badge/bonito-0.8.1-blue) ![bonito Version](https://img.shields.io/badge/bonito-0.7.3-blue) |
| bayesprism | | |
| clusterprofiler | | ![clusterprofiler Version](https://img.shields.io/badge/clusterprofiler-4.14.0-blue) ![clusterprofiler Version](https://img.shields.io/badge/clusterprofiler-4.10.0-blue) ![clusterprofiler Version](https://img.shields.io/badge/clusterprofiler-4.8.1-blue) ![clusterprofiler Version](https://img.shields.io/badge/clusterprofiler-4.6.0-blue) |
| CPC2 | | ![CPC2 Version](https://img.shields.io/badge/CPC2-1.0.1-blue) |
| CPAT | | ![CPAT Version](https://img.shields.io/badge/CPAT-3.0.5-blue) ![CPAT Version](https://img.shields.io/badge/CPAT-3.0.4-blue) ![CPAT Version](https://img.shields.io/badge/CPAT-2.0.0-blue) ![CPAT Version](https://img.shields.io/badge/CPAT-1.2.4-blue) |
| deconvseq | | |
| deeptools | | |
| DESeq2 | | ![DESeq2 Version](https://img.shields.io/badge/DESeq2-1.46.0-blue) ![DESeq2 Version](https://img.shields.io/badge/DESeq2-1.42.0-blue) ![DESeq2 Version](https://img.shields.io/badge/DESeq2-1.40.2-blue) ![DESeq2 Version](https://img.shields.io/badge/DESeq2-1.38.0-blue) |
| differr | | ![differr Version](https://img.shields.io/badge/differr-0.2-blue) |
| DRUMMER | | |
| edger | | ![edger Version](https://img.shields.io/badge/edger-4.4.0-blue) |
| eligos2 | | |
| ensembldb | | |
| epinano | | ![epinano Version](https://img.shields.io/badge/epinano-1.2.5-blue) |
| estimate | | ![estimate Version](https://img.shields.io/badge/estimate-1.0.13-blue) |
| f5c | | |
| fastp | [Ultrafast one-pass FASTQ data preprocessing, quality control, and deduplication using fastp](https://doi.org/10.1002/imt2.107) | ![fastp Version](https://img.shields.io/badge/fastp-0.24.0-blue) ![fastp Version](https://img.shields.io/badge/fastp-0.23.2-blue) |
| flair | [Detecting haplotype-specific transcript variation in long reads with FLAIR2](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-024-03301-y) | ![flair Version](https://img.shields.io/badge/flair-2.0.0-blue) ![flair Version](https://img.shields.io/badge/flair-1.7.0-blue) ![flair Version](https://img.shields.io/badge/flair-1.6.4-blue) |
| GATK | | ![GATK Version](https://img.shields.io/badge/GATK-3.8-blue) |
| genekitr | | |
| genion | | ![genion Version](https://img.shields.io/badge/genion-1.1.1-blue) |
| genomicfeatures | | |
| gffcompare | | ![gffcompare Version](https://img.shields.io/badge/gffcompare-0.12.10-blue) ![gffcompare Version](https://img.shields.io/badge/gffcompare-0.12.9-blue) ![gffcompare Version](https://img.shields.io/badge/gffcompare-0.12.6-blue) |
| gffread | [https://github.com/gpertea/gffread](https://ccb.jhu.edu/software/stringtie/gff.shtml) | ![gffread Version](https://img.shields.io/badge/gffread-0.12.7-blue) ![gffread Version](https://img.shields.io/badge/gffread-0.12.1-blue) |
| glmnet | | ![glmnet Version](https://img.shields.io/badge/glmnet-4.18-blue) ![glmnet Version](https://img.shields.io/badge/glmnet-4.11-blue) |
| gloritools | | |
| hamr | [HAMR: high-throughput annotation of modified ribonucleotides](https://rnajournal.cshlp.org/content/19/12/1684) | ![hamr Version](https://img.shields.io/badge/hamr-0a04208eae481137e0081dd90b9c1a40bc49c9f3-blue) |
| hisat2 | [Graph-based genome alignment and genotyping with HISAT2 and HISAT-genotype](https://www.nature.com/articles/s41587-019-0201-4) | ![hisat2 Version](https://img.shields.io/badge/hisat2-2.2.1-blue) ![hisat2 Version](https://img.shields.io/badge/hisat2-2.2.0-blue) ![hisat2 Version](https://img.shields.io/badge/hisat2-2.1.0-blue) |
| HMMER | | ![HMMER Version](https://img.shields.io/badge/HMMER-3.4-blue) ![HMMER Version](https://img.shields.io/badge/HMMER-3.3.2-blue) ![HMMER Version](https://img.shields.io/badge/HMMER-3.3.1-blue) |
| immunedeconv | | ![immunedeconv Version](https://img.shields.io/badge/immunedeconv-2.1.2-blue) |
| IsoformSwitchAnalyzeR | | ![IsoformSwitchAnalyzeR Version](https://img.shields.io/badge/IsoformSwitchAnalyzeR-2.6.0-blue) ![IsoformSwitchAnalyzeR Version](https://img.shields.io/badge/IsoformSwitchAnalyzeR-2.2.0-blue) |
| iupred2a | | ![iupred2a Version](https://img.shields.io/badge/iupred2a-20251022-blue) |
| jaffal | | ![jaffal Version](https://img.shields.io/badge/jaffal-2.3-blue) ![jaffal Version](https://img.shields.io/badge/jaffal-2.2-blue) |
| kallisto | | ![kallisto Version](https://img.shields.io/badge/kallisto-0.52.0-blue) ![kallisto Version](https://img.shields.io/badge/kallisto-0.51.1-blue) ![kallisto Version](https://img.shields.io/badge/kallisto-0.50.1-blue) |
| lafite | | ![lafite Version](https://img.shields.io/badge/lafite-1.0.2-blue) |
| lftp | [https://lftp.yar.ru](https://lftp.yar.ru) | ![lftp Version](https://img.shields.io/badge/lftp-latest-blue) |
| limma | | ![limma Version](https://img.shields.io/badge/limma-3.62.1-blue) ![limma Version](https://img.shields.io/badge/limma-3.62.0-blue) |
| longgf | | |
| meeko | | ![meeko Version](https://img.shields.io/badge/meeko-0.7.1-blue) |
| mgltools | | |
| mime | | ![mime Version](https://img.shields.io/badge/mime-9a9f6ac89851bf631f9df3868b2fa624bed49df2-blue) |
| minimap2 | | |
| modtect | | |
| multiqc | | ![multiqc Version](https://img.shields.io/badge/multiqc-1.32-blue) ![multiqc Version](https://img.shields.io/badge/multiqc-1.31-blue) |
| music | | |
| nanocount | | |
| nanopolish | [A complete bacterial genome assembled de novo using only nanopore sequencing data](https://www.nature.com/articles/nmeth.3444) | ![nanopolish Version](https://img.shields.io/badge/nanopolish-0.14.0-blue) ![nanopolish Version](https://img.shields.io/badge/nanopolish-0.13.3-blue) |
| picard | | ![picard Version](https://img.shields.io/badge/picard-3.4.0-blue) ![picard Version](https://img.shields.io/badge/picard-3.3.0-blue) |
| psinanopore | | |
| PUREE | | ![PUREE Version](https://img.shields.io/badge/PUREE-5a0a702535e79e37b071971063e72fa697540818-blue) |
| qualimap | [Qualimap 2 advanced multi-sample quality control for high-throughput sequencing data](http://qualimap.bioinfo.cipf.es/) | ![qualimap Version](https://img.shields.io/badge/qualimap-2.3-blue) ![qualimap Version](https://img.shields.io/badge/qualimap-2.2.2d-blue) |
| R deconvolution | | |
| R deg | | |
| R grn | | |
| R ml | | |
| R tumor purity | | |
| R validation | | |
| R wgcna | | |
| rmats | [Multivariate Analysis of Transcript Splicing (MATS)](https://rnaseq-mats.sourceforge.io/) | ![rmats Version](https://img.shields.io/badge/rmats-4.3.0-blue) ![rmats Version](https://img.shields.io/badge/rmats-4.2.0-blue) |
| rmats turbo | [rmats turbo](https://github.com/Xinglab/rmats-turbo/tree/master) | ![rmats turbo Version](https://img.shields.io/badge/rmats%20turbo-4.3.0-blue) |
| rna-seqc | | ![rna-seqc Version](https://img.shields.io/badge/rna-seqc-2.4.2-blue) ![rna-seqc Version](https://img.shields.io/badge/rna-seqc-2.3.5-blue) |
| rnam5c | [Genome-wide identification of mRNA 5-methylcytosine in mammals](https://www.nature.com/articles/s41594-019-0218-x) | ![rnam5c Version](https://img.shields.io/badge/rnam5c-4c6656b-blue) |
| rnamodivt | [Systematic calibration of epitranscriptomic maps using a synthetic modification-free RNA library](https://www.nature.com/articles/s41592-021-01280-7) | ![rnamodivt Version](https://img.shields.io/badge/rnamodivt-48df2c0-blue) |
| rnasieve | | |
| salmon | | ![salmon Version](https://img.shields.io/badge/salmon-1.10.3-blue) ![salmon Version](https://img.shields.io/badge/salmon-1.10.2-blue) |
| scaden | [Deep learning–based cell composition analysis from tissue expression profiles](https://www.science.org/doi/10.1126/sciadv.aba2619) | ![scaden Version](https://img.shields.io/badge/scaden-1.1.2-blue) |
| sicelore | [High throughput error corrected Nanopore single cell transcriptome sequencing](https://doi.org/10.1038/s41467-020-17800-6) | ![sicelore Version](https://img.shields.io/badge/sicelore-2.0-blue) |
| signalp | | ![signalp Version](https://img.shields.io/badge/signalp-5.0b-blue) |
| slow5tools | | |
| splicetools | | ![splicetools Version](https://img.shields.io/badge/splicetools-e7c81ca-blue) |
| sratools | [https://github.com/ncbi/sra-tools](https://github.com/ncbi/sra-tools) | ![sratools Version](https://img.shields.io/badge/sratools-3.2.1-blue) |
| star | [STAR ultrafast universal RNA-seq aligner](https://academic.oup.com/bioinformatics/article/29/1/15/272537) | ![star Version](https://img.shields.io/badge/star-2.7.11b-blue) |
| stringtie | [Improved transcriptome assembly using a hybrid of long and short reads with StringTie](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009730) | ![stringtie Version](https://img.shields.io/badge/stringtie-3.0.0-blue) |
| subread | [Subread package high-performance read alignment, quantification and mutation discovery](https://subread.sourceforge.net/) | ![subread Version](https://img.shields.io/badge/subread-2.1.1-blue) |
| suppa | [SUPPA2 fast, accurate, and uncertainty-aware differential splicing analysis across multiple conditions](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-018-1417-1) | ![suppa Version](https://img.shields.io/badge/suppa-2.3-blue) |
| sva | | ![sva Version](https://img.shields.io/badge/sva-3.54.0-blue) |
| tape | [Deep autoencoder for interpretable tissue-adaptive deconvolution and cell-type-specific gene analysis](https://www.nature.com/articles/s41567-022-34550-9) | ![tape Version](https://img.shields.io/badge/tape-1.1.2-blue) |
| tidyestimate | | ![tidyestimate Version](https://img.shields.io/badge/tidyestimate-1.1.1-blue) |
| vg | [Variation graph toolkit improves read mapping by representing genetic variation in the reference](https://www.nature.com/articles/nbt.4227) | ![vg Version](https://img.shields.io/badge/vg-1.63.1-blue) |
| wgcna | | ![wgcna Version](https://img.shields.io/badge/wgcna-1.73-blue) |
| xcell | | ![xcell Version](https://img.shields.io/badge/xcell-1.3-blue) |

## 🔧 Usage

### Pull Images

```bash
docker pull loganylchen/<tool>:<version>
```

### Build Locally

```bash
cd tools/<tool>
docker build -t <tool>:<version> .
```

## 📝 Notes

- All Dockerfiles include maintainer label: `Yuelong CHEN <yuelong.chen.btr@gmail.com>`
- Images are built and pushed via GitHub Actions
- For detailed usage of each tool, check the README.md in each tool's directory

## 🤝 Contributing

If you find any issues or want to add new tools, please open an issue or submit a pull request.

## 📅 Last Updated

- 2026-03-19: Fixed 12 tools, added maintainer labels to all 91 Dockerfiles
