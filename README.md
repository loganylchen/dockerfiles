# Dockerfiles for Bioinformatics Tools

A collection of **99** Dockerfiles for bioinformatics tools, maintained by [Yuelong CHEN](mailto:yuelong.chen.btr@gmail.com).

## Quick Start

```bash
# Pull an image
docker pull btrspg/<tool>:<version>

# Build locally
cd tools/<tool>
docker build --build-arg VERSION=<version> -t <tool>:<version> .
```

## Tools by Category

### Sequence Alignment (序列比对)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [hisat2](tools/hisat2/) | Python | `2.2.1` | [Link](https://daehwankimlab.github.io/hisat2/) |
| [minimap2](tools/minimap2/) | Java | `2.30`, `2.29`, `2.28`, `2.27`, `2.26`, `2.25` | [Link](https://github.com/lh3/minimap2) |
| [star](tools/star/) | Compiled | `2.7.11b`, `2.7.10b` | [Link](https://github.com/alexdobin/STAR) |
| [subread](tools/subread/) | Compiled | `2.0.6`, `2.0.3` | [Link](http://subread.sourceforge.net/) |

### Transcript Quantification (转录本定量)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [kallisto](tools/kallisto/) | Compiled | `0.52.0`, `0.51.1`, `0.50.1`, `0.48.0` | [Link](https://pachterlab.github.io/kallisto/) |
| [nanocount](tools/nanocount/) | Python | `1.1.0.post2`, `1.0.0.post6` | [Link](https://github.com/a-slide/NanoCount) |
| [rnasieve](tools/rnasieve/) | Python | `0.1.4` |  |
| [salmon](tools/salmon/) | Compiled | `1.11.4`, `1.10.0`, `1.9.0` | [Link](https://github.com/COMBINE-lab/salmon) |

### RNA-seq Analysis (RNA-seq分析)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [bambu](tools/bambu/) | R/Bioc | `3.4.0`, `3.2.6`, `3.0.8` | [Link](https://bioconductor.org/packages/bambu/) |
| [flair](tools/flair/) | Python | `2.0.0`, `1.7.0` | [Link](https://github.com/BrooksLabUCSC/flair) |
| [gffcompare](tools/gffcompare/) | Compiled | `0.12.10`, `0.12.9`, `0.12.6` | [Link](https://ccb.jhu.edu/software/stringtie/gffcompare.shtml) |
| [puree](tools/puree/) | Python | `5a0a702535e79e37b071971063e72fa697540818` | [Link](https://github.com/skandlab/PUREE) |
| [sicelore](tools/sicelore/) | Python | `1.0` | [Link](https://github.com/ucagenomix/sicelore) |
| [stringtie](tools/stringtie/) | Compiled | `2.2.3`, `2.2.1`, `2.1.7` | [Link](https://ccb.jhu.edu/software/stringtie/) |

### Alternative Splicing (可变剪接)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [aspli](tools/aspli/) | R/Bioc | `2.14.0` | [Link](https://bioconductor.org/packages/ASpli/) |
| [dexseq](tools/dexseq/) | R/Bioc | `1.50.0` | [Link](https://bioconductor.org/packages/DEXSeq/) |
| [irfinder](tools/irfinder/) | R/Bioc | `2.0.1` | [Link](https://github.com/RitchieLabIGH/IRFinder) |
| [isoformswitchanalyzer](tools/isoformswitchanalyzer/) | R/Bioc | `2.4.0`, `2.2.0` | [Link](https://bioconductor.org/packages/IsoformSwitchAnalyzeR/) |
| [junctionseq](tools/junctionseq/) | R/Bioc | `1.26.0` | [Link](https://bioconductor.org/packages/JunctionSeq/) |
| [lafite](tools/lafite/) | Python | `1.0.2`, `1.0.1` | [Link](https://github.com/pythseq/LAFITE) |
| [leafcutter](tools/leafcutter/) | Compiled | `0.2.9` | [Link](https://github.com/davidaknowles/leafcutter) |
| [majiq](tools/majiq/) | Python | `2.5` | [Link](https://majiq.biociphers.org/) |
| [miso](tools/miso/) | Python | `0.5.4` | [Link](https://miso.readthedocs.io/) |
| [psinanopore](tools/psinanopore/) | R/Bioc | `1.0` | [Link](https://github.com/RouhanifardLab/PsiNanopore) |
| [psisigma](tools/psisigma/) | R/Bioc | `1.9` | [Link](https://github.com/wososa/PSI-Sigma) |
| [regtools](tools/regtools/) | Compiled | `1.0.0`, `0.5.2` | [Link](https://github.com/griffithlab/regtools) |
| [rmats](tools/rmats/) | R/Bioc | `4.3.0`, `4.2.0`, `4.1.2` | [Link](https://rnaseq-mats.sourceforge.io/) |
| [rmatsturbo](tools/rmatsturbo/) | R/Bioc | `4.3.0`, `4.2.0`, `4.1.2` | [Link](https://github.com/Xinglab/rmats-turbo) |
| [rnaseqlib](tools/rnaseqlib/) | Python | `1.1.2` | [Link](https://github.com/yarden/rnaseqlib) |
| [sgseq](tools/sgseq/) | R/Bioc | `1.38.0` | [Link](https://bioconductor.org/packages/SGSeq/) |
| [spladder](tools/spladder/) | Python | `3.0.4` | [Link](https://github.com/ratschlab/spladder) |
| [splicetools](tools/splicetools/) | Python | `main` |  |
| [suppa](tools/suppa/) | Python | `2.3` | [Link](https://github.com/comprna/SUPPA) |
| [whippet](tools/whippet/) | Compiled | `1.6.1` | [Link](https://github.com/timbitz/Whippet.jl) |

### Differential Expression (差异表达)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [deseq2](tools/deseq2/) | R/Bioc | `1.44.0`, `1.42.1`, `1.40.2` | [Link](https://bioconductor.org/packages/DESeq2/) |
| [edger](tools/edger/) | R/Bioc | `4.2.1`, `4.0.16`, `3.42.4` | [Link](https://bioconductor.org/packages/edgeR/) |
| [limma](tools/limma/) | R/Bioc | `3.60.4`, `3.58.1`, `3.56.2` | [Link](https://bioconductor.org/packages/limma/) |
| [sva](tools/sva/) | R/Bioc | `3.52.0`, `3.50.0`, `3.48.0` | [Link](https://bioconductor.org/packages/sva/) |

### RNA Modification (RNA修饰)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [differr](tools/differr/) | R/Bioc | `0.2` | [Link](https://github.com/bartongroup/differr_nanopore_DRS) |
| [directrm](tools/directrm/) | Python | `1.0` | [Link](https://github.com/yuxinPenny/DirectRM) |
| [drummer](tools/drummer/) | Python | `92bb35a4a2b22ff304f5e4bcbc9fa6985f18a12e` | [Link](https://github.com/DepledgeLab/DRUMMER) |
| [eligos2](tools/eligos2/) | R/Bioc | `2.1.0` | [Link](https://gitlab.com/piroonj/eligos2) |
| [epinano](tools/epinano/) | R/Bioc | `1.2.0` | [Link](https://github.com/novoalab/EpiNano) |
| [gloritools](tools/gloritools/) | Python | `1.0.0` | [Link](https://github.com/liucongcas/GLORI-tools) |
| [hamr](tools/hamr/) | R/Bioc | `3.3` | [Link](https://github.com/GregoryLab/HAMR) |
| [modtect](tools/modtect/) | Python | `1.7.5.1` | [Link](https://github.com/ktan8/ModTect) |
| [nanocompore](tools/nanocompore/) | Python | `2.2.0`, `2.0.0` | [Link](https://github.com/tlacombe/nanocompore) |
| [nanocompore1](tools/nanocompore1/) | Python | `1.0.4` | [Link](https://github.com/tlacombe/nanocompore) |
| [rnam5c](tools/rnam5c/) | Python | `409be6485bcdd160f6c57e386ef71ff3ecb8e2f6` | [Link](https://www.nature.com/articles/s41594-019-0218-x) |
| [rnamodivt](tools/rnamodivt/) | R/Bioc | `48df2c04ee063c96aaefde64df915a867528f93e` | [Link](https://www.nature.com/articles/s41592-021-01280-7) |
| [xpore](tools/xpore/) | Python | `2.1`, `2.0` | [Link](https://github.com/GoekeLab/xpore) |

### Cell Deconvolution (细胞解卷积)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [bayesprism](tools/bayesprism/) | R/Bioc | `2.2.3` | [Link](https://github.com/Danko-Lab/BayesPrism) |
| [bisque](tools/bisque/) | R/Bioc | `1.0.5` | [Link](https://github.com/cozygene/bisque) |
| [deconvseq](tools/deconvseq/) | R/Bioc | `0.2.3` | [Link](https://github.com/rosedu1/deconvSeq) |
| [estimate](tools/estimate/) | R/Bioc | `1.0.13` | [Link](https://r-forge.r-project.org) |
| [immunedeconv](tools/immunedeconv/) | R/Bioc | `2.1.0`, `2.0.3` | [Link](https://github.com/omnideconv/immunedeconv) |
| [music](tools/music/) | R/Bioc | `1.0.0` | [Link](https://github.com/xuranw/MuSiC) |
| [scaden](tools/scaden/) | Python | `1.1.2` | [Link](https://github.com/KevinMenden/scaden) |
| [tape](tools/tape/) | Python | `1.1.2` | [Link](https://github.com/poseidonchan/TAPE) |
| [tidyestimate](tools/tidyestimate/) | R/Bioc | `1.1.1`, `1.0.4` | [Link](https://github.com/KaiAragaki/tidyestimate) |
| [xcell](tools/xcell/) | R/Bioc | `1.1.0` | [Link](https://xcell.ucsf.edu/) |

### Gene Fusion (基因融合)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [aeron](tools/aeron/) | Python | `c77c73a4bdeb6fb21fa7522239b2276e27ea10f8` | [Link](https://www.biorxiv.org/content/10.1101/2020.01.27.921338v1) |
| [genion](tools/genion/) | Compiled | `1.1.1` | [Link](https://github.com/vpc-ccg/genion) |
| [jaffal](tools/jaffal/) | R/Bioc | `2.3`, `2.2` | [Link](https://github.com/Oshlack/JAFFA) |
| [longgf](tools/longgf/) | Compiled | `0.1.2` | [Link](https://github.com/WGLab/LongGF) |

### Coding Potential (编码潜力预测)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [cpat](tools/cpat/) | Python | `3.0.4`, `3.0.3` | [Link](https://github.com/liguowang/cpat) |
| [cpc2](tools/cpc2/) | Python | `1.0.1` | [Link](https://github.com/gao-lab/CPC2_standalone) |

### Nanopore Analysis (Nanopore分析)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [bonito](tools/bonito/) | Python | `0.8.1`, `0.7.3`, `0.6.2` | [Link](https://github.com/nanoporetech/bonito) |
| [f5c](tools/f5c/) | Compiled | `1.6`, `1.5`, `1.4`, `1.3`, `1.2`, `1.1` | [Link](https://github.com/hasindu2008/f5c) |
| [nanopolish](tools/nanopolish/) | Python | `0.14.0` | [Link](https://github.com/jts/nanopolish) |
| [slow5tools](tools/slow5tools/) | Compiled | `1.4.0`, `1.3.0`, `1.2.0`, `1.1.0`, `1.0.0`, `0.9.0` | [Link](https://github.com/hasindu2008/slow5tools) |

### Variant Calling (变异检测)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [gatk](tools/gatk/) | R/Bioc | `4.6.1.0`, `4.5.0.0`, `4.4.0.0` | [Link](https://gatk.broadinstitute.org/) |
| [picard](tools/picard/) | Java | `3.2.0`, `3.1.1`, `3.0.0` | [Link](https://broadinstitute.github.io/picard/) |

### Genomic Utilities (基因组工具)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [bedops](tools/bedops/) | Compiled | `2.4.41`, `2.4.40` | [Link](https://bedops.readthedocs.io/) |
| [bedtools](tools/bedtools/) | Python | `2.31.1`, `2.31.0`, `2.30.0` | [Link](https://bedtools.readthedocs.io/) |
| [gffread](tools/gffread/) | Compiled | `0.12.7`, `0.12.6` | [Link](http://ccb.jhu.edu/software/stringtie/gffread.shtml) |
| [hmmer](tools/hmmer/) | Compiled | `3.4`, `3.3.2` | [Link](https://eddylab.org/software/hmmer/) |
| [samtools](tools/samtools/) | Compiled | `1.23.1`, `1.22`, `1.21.1`, `1.19` | [Link](http://www.htslib.org/) |

### Quality Control (质量控制)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [fastp](tools/fastp/) | Compiled | `1.3.1`, `1.3.0`, `1.2.0`, `1.1.0`, `1.0.1`, `1.0.0`, `0.26.0`, `0.24.0`, `0.23.2` | [Link](https://github.com/OpenGene/fastp) |
| [multiqc](tools/multiqc/) | Python | `1.24.1`, `1.21`, `1.19` | [Link](https://multiqc.info/) |
| [qualimap](tools/qualimap/) | Python | `2.3` | [Link](http://qualimap.conesalab.org/) |
| [rnaseqc](tools/rnaseqc/) | Python | `2.4.2` | [Link](https://github.com/getzlab/rnaseqc) |

### Functional Annotation (功能注释)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [clusterprofiler](tools/clusterprofiler/) | R/Bioc | `4.12.6`, `4.10.1`, `4.8.3` | [Link](https://bioconductor.org/packages/clusterProfiler/) |
| [ensembldb](tools/ensembldb/) | R/Bioc | `2.32.0` | [Link](https://bioconductor.org/packages/ensembldb/) |
| [genekitr](tools/genekitr/) | R/Bioc | `1.2.8` | [Link](https://github.com/GangLiLab/genekitr) |
| [genomicfeatures](tools/genomicfeatures/) | R/Bioc | `1.62.0` | [Link](https://bioconductor.org/packages/GenomicFeatures/) |

### Coexpression Network (共表达网络)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [wgcna](tools/wgcna/) | R/Bioc | `1.73`, `1.72_5` | [Link](https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/) |

### Statistics / Machine Learning (统计/机器学习)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [glmnet](tools/glmnet/) | R/Bioc | `4.1_8`, `4.1_7` | [Link](https://glmnet.stanford.edu/) |
| [mime](tools/mime/) | R/Bioc | `9a9f6ac89851bf631f9df3868b2fa624bed49df2` |  |

### Protein Structure (蛋白质结构)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [autodockvina](tools/autodockvina/) | Python | `1.2.5` | [Link](https://github.com/ccsb-scripps/AutoDock-Vina) |
| [iupred2a](tools/iupred2a/) | Python | `2a` | [Link](https://iupred.elte.hu/) |
| [meeko](tools/meeko/) | Python | `0.7.1` | [Link](https://github.com/forlilab/meeko) |
| [mgltools](tools/mgltools/) | Python | `1.5.7` | [Link](https://ccsb.scripps.edu/mgltools/) |
| [signalp](tools/signalp/) | Compiled | `5.0b` | [Link](https://services.healthtech.dtu.dk/services/SignalP-5.0/) |

### Python Bio Tools (Python生物工具)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [biopython](tools/biopython/) | Python | `1.84`, `1.83`, `1.82` | [Link](https://biopython.org/) |
| [deeptools](tools/deeptools/) | Python | `3.5.6`, `3.5.5`, `3.5.3`, `3.5.2` | [Link](https://deeptools.readthedocs.io/) |

### Pangenome (泛基因组)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [vg](tools/vg/) | Compiled | `1.59.0`, `1.56.0`, `1.53.0` | [Link](https://github.com/vgteam/vg) |

### Data Download (数据下载)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [sratools](tools/sratools/) | Compiled | `3.1.1`, `3.0.10`, `3.0.7` | [Link](https://github.com/ncbi/sra-tools) |

### Utility (实用工具)

| Tool | Type | Versions | Reference |
|------|------|----------|-----------|
| [lftp](tools/lftp/) | Compiled | `4.9.2` | [Link](https://lftp.yar.ru/) |

## Notes

- Docker Hub: [`btrspg`](https://hub.docker.com/u/btrspg)
- All images include label: `maintainer=Yuelong CHEN <yuelong.chen.btr@gmail.com>`
- Images are built and pushed via GitHub Actions
- For detailed usage, check `README.md` in each tool's directory

## Contributing

If you find any issues or want to add new tools, please open an issue or submit a pull request.
