# LAFITE

Low-abundance Aware Full-length Isoform clusTEr

## Description

LAFITE is designated to identify high-consensus full-length isoforms from Nanopore Direct RNA-seq data. LAFITE combines multiple features from reference annotation and DRS reads (TSS, TES, splicing junction, and read polyadenylation event) and is more sensitive to Low-abundance transcripts.

## Usage

```bash
lafite -b BAM -g GTF -f GENOME -o OUTPUT [OPTIONS]
```

### Required Arguments

- `-b BAM`: Path to the alignment file in BAM format
- `-g GTF`: Path to the reference gene annotation in GTF format
- `-f GENOME`: Path to the reference genome fasta
- `-o OUTPUT`: Path to the output file

### Optional Arguments

- `-B BEDTOOLS`: Path to the executable bedtools (default: bedtools in PATH)
- `-n MIN_COUNT_TSS_TES`: Minimum number of reads supporting a alternative TSS or TES (default: 3)
- `-i MIS_INTRON_LENGTH`: Length cutoff for correcting unexpected small intron (default: 150)
- `-c MIN_NOVEL_TRANS_COUNT`: Minimum occurrences required for a isoform from novel loci (default: 3)
- `-s MIN_SINGLE_EXON_COVERAGE`: Minimum read coverage required for a novel single-exon transcript (default: 4)
- `-l MIN_SINGLE_EXON_LEN`: Minimum length for single-exon transcript (default: 100)
- `-L LABEL`: Name prefix for output transcripts (default: LAFT)
- `-p POLYA`: Path to the file contains read Polyadenylation event
- `-m POLYA_MOTIF_FILE`: Path to the polya motif file
- `-r RELATIVE_ABUNDANCE_THRESHOLD`: Minimum abundance of the predicted multi-exon transcripts (default: 0.01)
- `-j SHORT_SJ_TAB`: Path to the short read splice junction file
- `-w SJ_CORRECTION_WINDOW`: Edit distance to reference splicing site (default: 40)
- `-t THREAD`: Number of the threads (default: 4)

## Example

```bash
# With Nanopolish polyadenylation result
lafite -b alignment.bam -g reference.gtf -f reference.fa -o output.gtf -t 8 -p nanopolish_polya.txt

# Without Nanopolish, using Poly(A) motif file
lafite -b alignment.bam -g reference.gtf -f reference.fa -o output.gtf -t 8 -m polya_motifs.txt
```

## Prerequisites

- bedtools
- minimap2 (for alignment)
- samtools (for BAM processing)
- nanopolish (optional, for polyadenylation analysis)

## References

- GitHub: https://github.com/TF-Chan-Lab/LAFITE
- PyPI: https://pypi.org/project/LAFITE/

## Version

- 1.0.2
