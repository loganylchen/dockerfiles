#! /usr/bin/env python
#
#  Copyright (c) 2013-2018 University of Pennsylvania
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

# version 3.3 - Adding in function to summarize mismatches from the beginning and end read termini (summarizeEndMismatches.py), and requiring manually specifying retention of intermediate files

import sys
import argparse
import subprocess
import os
import shutil
import datetime
import re
from distutils import spawn

import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("hamr")


def run_command(cmd,stdout=sys.stdout,stderr=sys.stderr):
    if isinstance(cmd,list):
        cmd = ' '.join([f'{i}' for i in cmd])
    log.info(f'Running {cmd}')
    p = subprocess.Popen(cmd,shell=True,stderr=stderr,stdout=stdout)
    return p.communicate()




RSCRIPT = spawn.find_executable("Rscript")
if RSCRIPT is None:
    log.error("***ERROR: Rscript is not found")
    sys.exit("Please install R / Rscript or make sure it is in the PATH")

PYTHON = spawn.find_executable("python")
if PYTHON is None:
    log.error("***ERROR: python is not found")
    sys.exit("Please install / python or make sure it is in the PATH")

SAMTOOLS = spawn.find_executable("samtools")
if SAMTOOLS is None:
    log.error("***ERROR: samtools is not found")
    sys.exit("Please install samtools or make sure it is in the PATH")

BEDTOOLS = spawn.find_executable("bedtools")
if BEDTOOLS is None:
    log.error("***ERROR: coverageBed is not found")
    sys.exit("Please install bedtools 2.2x or make sure it is in the PATH")

hamr_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
# command line arguments
parser = argparse.ArgumentParser(
    description="Takes a bam file that has been sorted with redundant reads removed and generates a HAMR predicted_mods.txt output")
parser.add_argument('bam', help='A sorted bam file consisting of nonredundant reads')
parser.add_argument('genome_fas',
                    help='Genome fasta file; WARNING: remember to index the reference using samtools faifx')
parser.add_argument('output_folder', help='name of folder to put HAMR output')
parser.add_argument('--out_prefix', help='Prefix for HAMR output', default='hamr')
parser.add_argument('--min_qual', help='The minimum quality score of a read to be analyzed', default='30')
parser.add_argument('--min_cov', help='The minimum coverage of a nucleotide to be analyzed', default='10')
parser.add_argument('--seq_err', help='The percentage of mismatches based solely on sequencing error', default='0.05')
parser.add_argument('--hypothesis', help='The hypothesis to be tested, either "H1" or "H4"', default='H4')
parser.add_argument('--max_p', help='The maximum p-value cutoff', default='0.01')
parser.add_argument('--max_fdr', help='The maximum FDR cutoff', default='0.05')
parser.add_argument('--refproportion',
                    help='The proportion of reads that must match the reference nucleotide (from 0 to 1)',
                    default='0.05')
parser.add_argument('--prediction_training_set', help='modification identity training set model file; .RData format',
                    default=hamr_dir + '/' + 'models/euk_trna_mods.Rdata')
parser.add_argument('--target_bed', '-n', action='store', dest='target_bed', nargs='?', default='unspecified',
                    help='Specifies genomic intervals for analysis; e.g. all mRNAs. If unspecified, defaults to whole genome')
parser.add_argument('--paired_ends', '-pe', action='store_true', help='Use this tag to indicate paired-end sequencing')
parser.add_argument('--filter_ends', '-fe', action='store_true',
                    help='Exclude the first and last nucleotides of a read from the analysis')
parser.add_argument('--empirical_hamr_acc_threshold', '-et', action='store_true',
                    help='Calculate the treshold of HAMR accessibility empirically. Otherwise, assumes it is equal to min_cov (reasonable assumption at 10x or more')
parser.add_argument('--type_plot', '-tp', action='store_false',
                    help='Use this tag to include plots of predicted modification type')
parser.add_argument('--retain_tempfiles', '-r', action='store_true', help='Use this tag to keep HAMR temp files')

args = parser.parse_args()

# Raise error if hypothesis has invalid value
if args.hypothesis != 'H1' and args.hypothesis != 'H4':
    raise ValueError('Hypothesis must be H1 or H4.')

# locations of C, Bash, and R scripts

rnapileup = hamr_dir + "/" + "rnapileup"  # C-script
filter_pileup = hamr_dir + "/" + "filter_pileup"  # C-script
rnapileup2mismatchbed = hamr_dir + "/" + "rnapileup2mismatchbed"  # C-script
mismatchbed2table = hamr_dir + "/" + "mismatchbed2table.sh"  # Shell script
detect_mods_definite = hamr_dir + "/" + "detect_mods.R"  # R script
classify_mods = hamr_dir + "/" + "classify_mods.R"  # Rscript
coverageBed_depth_histogram = hamr_dir + "/" + "coverageBed_depth_histogram.pl"  # perl script
get_chr_lengths_from_bam = hamr_dir + "/" + "get_chr_lengths_from_BAM.sh"  # Shell script
plot_mod_type = hamr_dir + "/" + "summ_mod_type_fromBed.R"  # R script
summarizeEndMismatches = hamr_dir + "/" + "summarizeEndMismatches.py"  # python script

log.info(f'rnapileup: {rnapileup}')
log.info(f'filter_pileup: {filter_pileup}')
log.info(f'rnapileup2mismatchbed: {rnapileup2mismatchbed}')
log.info(f'mismatchbed2table: {mismatchbed2table}')
log.info(f'detect_mods_definite: {detect_mods_definite}')
log.info(f'classify_mods: {classify_mods}')
log.info(f'coverageBed_depth_histogram: {coverageBed_depth_histogram}')
log.info(f'get_chr_lengths_from_bam: {get_chr_lengths_from_bam}')
log.info(f'plot_mod_type: {plot_mod_type}')
log.info(f'summarizeEndMismatches: {summarizeEndMismatches}')

# get flags
pairedends = ""
if args.paired_ends:
    pairedends = "--paired"

# Check for output directory and make it if neccessary
output_folder = args.output_folder
tmpDIR = os.path.join(output_folder, 'HAMR_temp')
os.makedirs(tmpDIR, exist_ok=True)

# get the date and time (unqiue string in case multiple HAMR runs output to same temp folder)
now = datetime.datetime.now()
datelist = [str(now.year), str(now.month), str(now.day), str(now.hour), str(now.minute), str(now.second),
            str(now.microsecond)]
rightnow = "_".join(datelist)
rTag = tmpDIR + '/' + rightnow + '.HAMR.' + args.out_prefix  # date included in file
# rTag=tmpDIR + '/' + 'HAMR.' + args.out_prefix

###################################################################################################################################

##run HAMR

# Input BAM steps

run_mode = "genome-wide"
inputBAM = args.bam
bamForAnalysis = inputBAM
if (args.target_bed != 'unspecified'):
    run_mode = 'targeted'
    target_bed = args.target_bed
    log.info(f'Target BED is specified: {target_bed}')

    # check target bed format (i.e. bed6, bed9, or bed12)
    log.info(f'Restricting BAM to regions in {target_bed}')
    bam_constrained = os.path.join(output_folder ,'hamr.constrained.bam')
    run_command(f'{SAMTOOLS} view -b {inputBAM} -L {target_bed} -o {bam_constrained}')
    run_command(f'{SAMTOOLS} index {bam_constrained}')
    bamForAnalysis = bam_constrained


log.info(f'Analyzing ({inputBAM}, {run_mode})')






# Pileup mismatches

log.info(f'Running RNApileup {rnapileup}')
rawpileup = rTag + '.pileup.raw'
with open(rawpileup, 'w') as frawpileup:
    run_command(f'{rnapileup} {bamForAnalysis} {args.genome_fas} {pairedends}', stdout=frawpileup)

log.info('Running filter_pileup...')
filteredpileup = rTag + '.pileup.filtered'
with open(filteredpileup, 'w') as ffilteredpileup:
    run_command(f'{filter_pileup}, {rawpileup}, {args.min_qual}, {args.filter_ends}',stdout=ffilteredpileup)


log.info("Filter coverage...")
## this will output ALL sites with read depth >= min_cov
## this will be the total # of sites for HAMR analysis
filteredpileupcov = rTag + '.pileup.filtered.' + str(args.min_cov)
with open(filteredpileupcov, 'w') as ffilteredpileupcov:
    run_command('awk $4>= {args.min_cov} {filteredpileup} ', stdout=ffilteredpileupcov)


log.info("Tabulating terminal mismatch frequency...")
endMismatches = output_folder + '/' + args.out_prefix + '.endMismatches.txt'
with open(endMismatches, 'w') as fendMismatches:
    run_command(f'{PYTHON} {summarizeEndMismatches} {filteredpileupcov}', stdout=fendMismatches)


log.info('Running rnapileup2mismatchbed...')
# convert pileups into BED file with entry corresponding to the observed (ref nuc) --> (read nucleotide) transitions
mismatchbed = rTag + '.mismatch.bed'
with open(mismatchbed, 'w') as fmismatchbed:
    run_command([rnapileup2mismatchbed, filteredpileupcov], stdout=fmismatchbed, )
fmismatchbed.close()

log.info("converting mismatch BED to nucleotide frequency table...")
# mismatchbed2table outputs all sites with at least 1 non-ref nuc
final_bed_file = mismatchbed
freq_table = rTag + '.freqtable.txt'
with open(freq_table, 'w') as txt_output:
    run_command([mismatchbed2table, final_bed_file], stdout=txt_output, )


log.info("filtering out sites based on non-ref/ref proportions...")
final_freq_table = rTag + '.freqtable.final.txt'
min_ref_pct = args.refproportion
with open(final_freq_table, 'w') as outf :
    run_command(
    ['awk', '{cov=$5+$6+$7+$8;nonref=$9; ref=cov-nonref; if (ref/cov>=' + min_ref_pct + ') print;}', freq_table],stdout=outf)


# OUTPUT steps

log.info("testing for statistical significance...")
last_tmp_file = final_freq_table
raw_file = output_folder + '/' + args.out_prefix + '.raw.txt'
with  open(raw_file, 'w') as outfn:
    run_command(
    [RSCRIPT, detect_mods_definite, last_tmp_file, args.seq_err, args.hypothesis, args.max_p, args.max_fdr,
     args.refproportion], stdout=outfn)


log.info("predicting modification identity...")
ps1 = subprocess.Popen(('grep', 'TRUE', raw_file), stdout=subprocess.PIPE, )
true_mods = subprocess.Popen(('wc', '-l'), stdin=ps1.stdout, stdout=subprocess.PIPE).communicate()[0].rstrip()
ps1.stdout.close()
true_mods = int(true_mods)
log.info(f'Total {true_mods} true modifications')
prediction_file = output_folder + '/' + args.out_prefix + '.mods.txt'
if (true_mods > 0):
    with open(prediction_file, 'w') as outfn:
        run_command([RSCRIPT, classify_mods, raw_file, args.prediction_training_set], stdout=outfn,
                          )
else:
    # tabulate number of HAMR accessible bases and then exit
    threshold = int(args.min_cov)
    filt_pileup_file = filteredpileupcov
    retOut = subprocess.check_output(['awk', 'END{print NR}', filt_pileup_file])
    HAMR_accessible_bases = int(retOut)
    # print summary file
    mods_per_acc_bases_file = output_folder + '/' + args.out_prefix + ".hamr_acc_bases.txt"
    with open(mods_per_acc_bases_file, 'w') as outfn:
        mods_per_acc_bases = 0
        outfn.write('sample\tmods\thamr_accessible_bases\tmods_per_million_accessible_bases\n')
        outfn.write(args.out_prefix + '\t' + str(true_mods) + '\t' + str(HAMR_accessible_bases) + '\t' + str(
            mods_per_acc_bases) + '\n')

    log.warning(
        f'''No HAMR modifications predicted, output will contain raw table and number of HAMR accessible bases only
        \nAssuming min_cov of {args.min_cov} as threshold for HAMR accessibility
        \nHAMR analysis complete
        \n\n------------------------------\n''')

log.info("converting output to bed format...")
bed_file = output_folder + '/' + args.out_prefix + ".mods.bed"
with open(bed_file, 'w') as outfn:
    run_command(['awk', 'FNR > 1 {print $1"\t"$2"\t"(1+$2)"\t"$1";"$2"\t"$16"\t"$3}', prediction_file],
                      stdout=outfn,)


log.info("calculating number of HAMR-accessible bases...")
if not args.empirical_hamr_acc_threshold:
    # tablulate number of bases at or above min_cov
    threshold = int(args.min_cov)
    filt_pileup_file = filteredpileupcov
    retOut = subprocess.check_output(['awk', 'END{print NR}', filt_pileup_file])
    HAMR_accessible_bases = int(retOut)
    # num_bases_with_min_cov=int(retOut)
    # HAMR_accessible_bases=int(num_bases_with_min_cov)

else:
    # calculate threshold for HAMR-accessibility unless manually specified
    log.info(   "calculating threshold of HAMR-accessibility...")
    min_cov_file = output_folder + '/' + args.out_prefix + ".min_cov.txt"
    with open(min_cov_file, 'w') as outfn:
        threshold = subprocess.check_output(
            ['awk', '{if (NR==1) next; cov=$9+$10; if (NR==2) thres=cov; if (cov < thres) thres=cov; }END{ print thres+0;}',
             prediction_file])
        threshold = int(threshold)
        log.info(  "HAMR accessibility threshold=" + str(threshold))
        outfn.write(args.out_prefix + '\t' + str(threshold) + '\n')


    # tablulate number of bases at or above threshold
    log.info("calculating number of HAMR-accessible bases...")
    hamr_acc_bases_file = output_folder + '/' + args.out_prefix + ".hamr_acc_bases.txt"
    with open(hamr_acc_bases_file, 'w') as outfn:
        HAMR_accessible_bases = subprocess.check_output(
            ['awk', '{if ($4>=' + str(threshold) + ') ++a}END{print a}', filteredpileup])
        HAMR_accessible_bases = int(HAMR_accessible_bases);
        outfn.write(args.out_prefix + '\t' + str(HAMR_accessible_bases) + '\n')

    log.info(f'HAMR accessible bases= {HAMR_accessible_bases}')

# output mods within normalization universe (if -n specified). Else skip this step
if args.target_bed != 'unspecified':
    log.info("Counting modifications in each feature of target bed file...")
    counts_file = output_folder + '/' + args.out_prefix + "." + "featureCounts.bedPlus1"
    positiveCounts_file = output_folder + '/' + args.out_prefix + "." + "positiveFeatureCounts.txt"
    with open(counts_file, 'w') as infn:
        run_command([BEDTOOLS, 'intersect', '-c', '-s', '-b', bed_file, '-a', args.target_bed], stdout=infn,)

    with open(positiveCounts_file, 'w') as infn:
        awk_parameters = ''''BEGIN {OFS="\t";FS="\t"} {if ($' + str(target_bed_colnum + 1) + ' > 0) print $0}'''
        run_command(['awk', awk_parameters, counts_file], stdout=infn)



# plot modification identity (if -tp is specified)
if (args.type_plot):
    log.info("plotting summary of modification types...")
    plot_file = output_folder + '/' + args.out_prefix + ".mod_type.pdf"
    run_command(['Rscript', plot_mod_type, bed_file, plot_file])

# print summary file
mods_per_acc_bases_file = output_folder + '/' + args.out_prefix + ".hamr_acc_bases.txt"
with open(mods_per_acc_bases_file, 'w') as outfn:
    mods_per_acc_bases = float(true_mods) / float(HAMR_accessible_bases) * 1000000
    outfn.write('sample\tmods\thamr_accessible_bases\tmods_per_million_accessible_bases\n')
    outfn.write(
        args.out_prefix + '\t' + str(true_mods) + '\t' + str(HAMR_accessible_bases) + '\t' + str(mods_per_acc_bases) + '\n')

# conclusion message
log.info(f"HAMR analysis complete\n\n------------------------------\n")
log.info(f"HAMR accessible sites analyzed (read depth>={threshold}): {HAMR_accessible_bases}" )
log.info(f"Modification sites found: {true_mods}")
# final_freq_table contains sites with ref / non-ref nucleotide mixtures
log.info(f"Sites used for analysis:  {final_freq_table}")
log.info(f"Statistical testing results: {raw_file}")
log.info(f"Modification sites + predicted types saved to:  {prediction_file}")

# remove temp files
if not args.retain_tempfiles:
    shutil.rmtree(tmpDIR)
