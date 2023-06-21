#! /bin/bash

set -e

sicelore_jar_lib=/opt/sicelore/Jar
RED='\033[0;31m'
NC='\033[0m'

while getopts "b:n:o:j:g:r:h" arg #选项后面的冒号表示该选项需要参数
do
        case ${arg} in
             b)
                illumina_bam=$OPTARG
                ;;
             n)
                nanopore_fastq_dir=$OPTARG
                ;;
             j)
                junc_bed=$OPTARG
                ;;
             r)
                refflat=$OPTARG
                ;;
             g)
                genome=$OPTARG
                ;;
             o)
                outdir=$OPTARG
                ;;
             h)
                echo  '''
options:
    -b          path to the 10x bam
    -n          nanopore fastq directory, fastq should not be compressed.
    -j          junction bed file
    -r          ref flat file: example: /expt/logan/nanopore_sc_dbmouse/mm_refflat.txt
    -g          genome reference (fasta)
    -o          output directory
    -h          help
                '''
                exit 0
                ;;
             ?)  #当有不认识的选项的时候arg为?
                echo "unkonw argument"
                exit 1
                ;;
        esac
done

tmp_dir=${outdir}/tmp
barcodes=$(dirname $illumina_bam)/filtered_feature_bc_matrix/barcodes.tsv


echo -e "${RED}==============================================================================================${NC}"
echo -e "${RED} Inputs: ${NC}"
echo -e "${RED}==============================================================================================${NC}"
echo -e "10x_bam = ${illumina_bam}"
echo -e "nanopore_fastq_dir = ${nanopore_fastq_dir}"
echo -e "output_directory = ${outdir}"
echo -e "tmp_dir = ${tmp_dir}"
echo -e "10x barcodes file = ${barcodes}"
echo -e "junc_bed = ${junc_bed}"
echo -e "refflat = ${refflat}"
echo -e "genome = ${genome}"
echo -e "${RED}==============================================================================================${NC}"


mkdir -p $outdir $tmp_dir



echo -e "${RED}==============================================================================================${NC}"
echo -e "${RED} Start ${NC}"



java -Xmx150g -jar ${sicelore_jar_lib}/IlluminaParser-1.0.jar \
    --inFileIllumina ${illumina_bam} \
    --tsv ${barcodes} \
    --outFile ${outdir}/parsedForNanopore_v0.2.obj \
    --cellBCflag CB \
    --umiFlag UB \
    --geneFlag GN


java -Xmx150g -jar ${sicelore_jar_lib}/NanoporeReadScanner-0.5.jar \
    -d ${nanopore_fastq_dir} \
    -o ${outdir}/nanopore/

fastq=$(ls ${outdir}/nanopore/passed/*FWD.fastq)

minimap2 -ax splice -uf --MD --sam-hit-only -t 20 \
        --junc-bed ${junc_bed} \
        ${genome} \
        ${fastq} \
        | samtools view -Sb |samtools sort - -o ${outdir}/nanopore/sorted.bam && samtools index ${outdir}/nanopore/sorted.bam

java -Xmx150g -jar ${sicelore_jar_lib}/Sicelore-2.0.jar AddGeneNameTag \
I=${outdir}/nanopore/sorted.bam \
O=${outdir}/nanopore/sorted_GE.bam \
REFFLAT=${refflat} \
GENETAG=GE ALLOW_MULTI_GENE_READS=true USE_STRAND_INFO=true VALIDATION_STRINGENCY=SILENT


samtools index ${outdir}/nanopore/sorted_GE.bam


java -Xmx150g -jar ${sicelore_jar_lib}/Sicelore-2.0.jar AddBamReadSequenceTag  \
I=${outdir}/nanopore/sorted_GE.bam \
O=${outdir}/nanopore/sorted_GEUS.bam \
FASTQDIR=${outdir}/nanopore/passed


samtools index ${outdir}/nanopore/sorted_GEUS.bam

java -jar -Xmx130g ${sicelore_jar_lib}/NanoporeBC_UMI_finder-1.0.jar \
-i ${outdir}/nanopore/sorted_GEUS.bam \
-o ${outdir}/nanopore/GEUS10xAttributes.bam \
-k ${outdir}/parsedForNanopore_v0.2.obj \
--maxUMIfalseMatchPercent 2 \
--maxBCfalseMatchPercent 5 \
--logFile ${outdir}/nanopore/GEUS10xAttributes.log




samtools index ${outdir}/nanopore/GEUS10xAttributes.bam
samtools index ${outdir}/nanopore/GEUS10xAttributes_umifound_.bam






java -jar -Xmx14g ${sicelore_jar_lib}/Sicelore-2.0.jar IsoformMatrix \
DELTA=2 METHOD=STRICT GENETAG=GE \
I=${outdir}/nanopore/GEUS10xAttributes_umifound_.bam \
REFFLAT=${refflat} \
CSV=${barcodes} \
OUTDIR=${outdir}/nanopore/ \
PREFIX=sicread VALIDATION_STRINGENCY=SILENT

java -jar -Xmx14g ${sicelore_jar_lib}/Sicelore-2.0.jar ComputeConsensus \
T=10 \
I=${outdir}/nanopore/GEUS10xAttributes_umifound_.bam \
O=${outdir}/nanopore/consensus.fq \
TMPDIR=${tmp_dir}

minimap2 -ax splice -uf --MD --sam-hit-only -t 4 --junc-bed ${junc_bed} ${genome} ${outdir}/nanopore/consensus.fq \
|samtools view -Sb \
|samtools sort - -o ${outdir}/nanopore/molecule.bam && samtools index  ${outdir}/nanopore/molecule.bam


java -jar -Xmx14g ${sicelore_jar_lib}/Sicelore-2.0.jar AddBamMoleculeTags \
I=${outdir}/nanopore/molecule.bam \
O=${outdir}/nanopore/molecule.tags.bam


samtools index ${outdir}/nanopore/molecule.tags.bam

# add gene name tag

java -jar -Xmx14g ${sicelore_jar_lib}/Sicelore-2.0.jar AddGeneNameTag \
I=${outdir}/nanopore/molecule.tags.bam \
O=${outdir}/nanopore/molecule.tags.GE.bam \
REFFLAT=${refflat} \
GENETAG=GE ALLOW_MULTI_GENE_READS=true USE_STRAND_INFO=true VALIDATION_STRINGENCY=SILENT



samtools index ${outdir}/nanopore/molecule.tags.GE.bam

# generate molecule isoform matrix

java -jar -Xmx14g ${sicelore_jar_lib}/Sicelore-2.0.jar IsoformMatrix DELTA=2 METHOD=STRICT ISOBAM=true GENETAG=GE \
I=${outdir}/nanopore/molecule.tags.GE.bam \
REFFLAT=${refflat} \
CSV=${barcodes} \
OUTDIR=${outdir}/nanopore/ \
PREFIX=sicmol VALIDATION_STRINGENCY=SILENT


samtools index ${outdir}/nanopore/sicmol_isobam.bam

echo -e "${RED}==============================================================================================${NC}"
echo -e "${RED} END ${NC}"



