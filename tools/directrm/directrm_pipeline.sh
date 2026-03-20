#!/bin/bash
################################################################################
# DirectRM Integrated Pipeline Script
# Purpose: Complete RNA modification detection pipeline from nanopore data
# Author: Bioinformatics Team
# Date: 2026-03-20
################################################################################

set -euo pipefail  # Exit on error, undefined variables, pipe failures
IFS=$'\n\t'         # Set safe Internal Field Separator

################################################################################
# Usage Function
################################################################################
usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS]

DirectRM Integrated Pipeline - RNA modification detection from nanopore direct RNA sequencing

REQUIRED OPTIONS:
  -i, --input DIR          Input directory containing POD5 files
  -r, --reference FILE     Reference FASTA file
  -g, --regions FILE       Target regions CSV file (columns: seqnames,start,end,width,strand)
  -o, --output DIR         Output directory for results

SEQUENCING KIT (exactly one required):
  --rna002                 Use SQK-RNA002 kit models (5-mer analysis)
  --rna004                 Use SQK-RNA004 kit models (9-mer analysis) [DEFAULT]

OPTIONAL:
  --dorado PATH            Path to dorado binary (default: /opt/dorado/bin/dorado)
  --dorado-model PATH      Path to dorado model (default: auto-detect based on kit)
  --device STRING          CUDA device (default: cuda:0)
  --splits RANGE           Split range to process (default: 0 END)
                           Format: "START END" or specific splits "0 1 5 10"
  --batch-size INT         POD5 files per split (default: 20)
  --kmer INT               K-mer size for feature extraction (default: 9 for RNA004, 5 for RNA002)
  --step INT               Step size for sliding window (default: 5)
  --skip-preprocessing     Skip base calling/alignment if BAM files exist
  --skip-feature-extract   Skip feature extraction if features exist
  --skip-denovo            Skip de novo detection if results exist
  --skip-inference         Skip modification inference if results exist
  --skip-aggregation       Skip read-to-site aggregation if results exist
  --model-id INT           Model architecture ID (1-4, default: 1)
  --use-integrated-model   Use integrated multi-label model (default: True)
  --threads INT            Number of CPU threads (default: 8)
  --remora-only            Run Remora environment for feature extraction only
  --help                   Display this help message

EXAMPLES:
  # Full pipeline with RNA004 data
  $(basename "$0") -i ./pod5_data -r reference.fa -g regions.csv -o ./results --rna004

  # Resume from feature extraction
  $(basename "$0") -i ./pod5_data -r reference.fa -g regions.csv -o ./results \\
      --rna004 --skip-preprocessing

  # Process specific splits only
  $(basename "$0") -i ./pod5_data -r reference.fa -g regions.csv -o ./results \\
      --rna004 --splits "0 5"

ENVIRONMENT VARIABLES:
  DIRECTRM_DIR    Path to DirectRM installation (default: /opt/DirectRM)
  CUDA_VISIBLE_DEVICES   GPU devices to use

EXIT CODES:
  0 - Success
  1 - General error
  2 - Input validation error
  3 - Missing dependency
  4 - Processing error

EOF
    exit 0
}

################################################################################
# Logging Functions
################################################################################
# Log file will be set in OUTPUT_DIR after argument parsing
LOG_FILE=""

_get_log_file() {
    if [[ -n "$OUTPUT_DIR" ]]; then
        echo "${OUTPUT_DIR}/directrm_pipeline_$(date +%Y%m%d_%H%M%S).log"
    else
        echo "directrm_pipeline_$(date +%Y%m%d_%H%M%S).log"
    fi
}

log() {
    local level=$1
    shift
    # Initialize LOG_FILE if not set
    if [[ -z "$LOG_FILE" ]]; then
        LOG_FILE="$(_get_log_file)"
    fi
    local message="[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $*"
    echo "$message" | tee -a "$LOG_FILE"
}

log_info() { log "INFO" "$@"; }
log_warn() { log "WARN" "$@"; }
log_error() { log "ERROR" "$@"; }
log_debug() { [[ "${DEBUG:-0}" == "1" ]] && log "DEBUG" "$@"; }

################################################################################
# Error Handler
################################################################################
error_exit() {
    local exit_code=$1
    shift
    log_error "$@"
    exit "$exit_code"
}

################################################################################
# Default Variables
################################################################################
INPUT_DIR=""
REFERENCE_FILE=""
REGIONS_FILE=""
OUTPUT_DIR=""
KIT_VERSION="RNA004"
DORADO_BIN="/opt/dorado/bin/dorado"
DORADO_MODEL=""
DEVICE="cuda:0"
SPLITS_RANGE=""
BATCH_SIZE=20
KMER_SIZE=9
STEP_SIZE=5
MODEL_ID=1
USE_INTEGRATED_MODEL="True"
THREADS=8
SKIP_PREPROCESSING=0
SKIP_FEATURE_EXTRACT=0
SKIP_DENOVO=0
SKIP_INFERENCE=0
SKIP_AGGREGATION=0
REMORA_ONLY=0

DIRECTRM_DIR="${DIRECTRM_DIR:-/opt/DirectRM}"
WORKDIR="${WORKDIR:-/data}"

################################################################################
# Parse Arguments
################################################################################
parse_args() {
    if [[ $# -eq 0 ]]; then
        usage
    fi

    while [[ $# -gt 0 ]]; do
        case $1 in
            -i|--input)
                INPUT_DIR="$2"
                shift 2
                ;;
            -r|--reference)
                REFERENCE_FILE="$2"
                shift 2
                ;;
            -g|--regions)
                REGIONS_FILE="$2"
                shift 2
                ;;
            -o|--output)
                OUTPUT_DIR="$2"
                shift 2
                ;;
            --rna002)
                KIT_VERSION="RNA002"
                KMER_SIZE=5
                shift
                ;;
            --rna004)
                KIT_VERSION="RNA004"
                KMER_SIZE=9
                shift
                ;;
            --dorado)
                DORADO_BIN="$2"
                shift 2
                ;;
            --dorado-model)
                DORADO_MODEL="$2"
                shift 2
                ;;
            --device)
                DEVICE="$2"
                shift 2
                ;;
            --splits)
                SPLITS_RANGE="$2"
                shift 2
                ;;
            --batch-size)
                BATCH_SIZE="$2"
                shift 2
                ;;
            --kmer)
                KMER_SIZE="$2"
                shift 2
                ;;
            --step)
                STEP_SIZE="$2"
                shift 2
                ;;
            --model-id)
                MODEL_ID="$2"
                shift 2
                ;;
            --use-integrated-model)
                USE_INTEGRATED_MODEL="True"
                shift
                ;;
            --use-independent-model)
                USE_INTEGRATED_MODEL="False"
                shift
                ;;
            --threads)
                THREADS="$2"
                shift 2
                ;;
            --skip-preprocessing)
                SKIP_PREPROCESSING=1
                shift
                ;;
            --skip-feature-extract)
                SKIP_FEATURE_EXTRACT=1
                shift
                ;;
            --skip-denovo)
                SKIP_DENOVO=1
                shift
                ;;
            --skip-inference)
                SKIP_INFERENCE=1
                shift
                ;;
            --skip-aggregation)
                SKIP_AGGREGATION=1
                shift
                ;;
            --remora-only)
                REMORA_ONLY=1
                shift
                ;;
            --help)
                usage
                ;;
            *)
                error_exit 2 "Unknown option: $1"
                ;;
        esac
    done
}

################################################################################
# Validation Functions
################################################################################
validate_inputs() {
    log_info "Validating inputs..."

    # Check required arguments
    [[ -z "$INPUT_DIR" ]] && error_exit 2 "Input directory not specified. Use -i|--input"
    [[ -z "$REFERENCE_FILE" ]] && error_exit 2 "Reference file not specified. Use -r|--reference"
    [[ -z "$REGIONS_FILE" ]] && error_exit 2 "Regions file not specified. Use -g|--regions"
    [[ -z "$OUTPUT_DIR" ]] && error_exit 2 "Output directory not specified. Use -o|--output"

    # Check input directory
    [[ ! -d "$INPUT_DIR" ]] && error_exit 2 "Input directory does not exist: $INPUT_DIR"

    # Check for POD5 files
    POD5_COUNT=$(find "$INPUT_DIR" -name "*.pod5" 2>/dev/null | wc -l)
    [[ "$POD5_COUNT" -eq 0 ]] && error_exit 2 "No POD5 files found in input directory: $INPUT_DIR"
    log_info "Found $POD5_COUNT POD5 file(s) in input directory"

    # Check reference file
    [[ ! -f "$REFERENCE_FILE" ]] && error_exit 2 "Reference file does not exist: $REFERENCE_FILE"

    # Check regions file
    [[ ! -f "$REGIONS_FILE" ]] && error_exit 2 "Regions file does not exist: $REGIONS_FILE"

    # Validate regions file format
    if ! head -1 "$REGIONS_FILE" | grep -qE "seqnames.*start.*end"; then
        log_warn "Regions file may not have proper header. Expected: seqnames,start,end,width,strand"
    fi

    # Check DirectRM installation
    if [[ ! -d "$DIRECTRM_DIR" ]]; then
        error_exit 3 "DirectRM directory not found: $DIRECTRM_DIR"
    fi

    # Check required DirectRM scripts
    local required_scripts=(
        "scripts/preprocessing.py"
        "scripts/feature_extraction.py"
        "scripts/denovo_inference.py"
        "scripts/inference.py"
        "scripts/read2site.py"
    )

    for script in "${required_scripts[@]}"; do
        if [[ ! -f "$DIRECTRM_DIR/$script" ]]; then
            error_exit 3 "Required DirectRM script not found: $DIRECTRM_DIR/$script"
        fi
    done

    # Check kmer levels file
    local kmer_file
    if [[ "$KIT_VERSION" == "RNA002" ]]; then
        kmer_file="$DIRECTRM_DIR/5mer_levels_v1.txt"
    else
        kmer_file="$DIRECTRM_DIR/9mer_levels_v1.txt"
    fi

    if [[ ! -f "$kmer_file" ]]; then
        error_exit 3 "K-mer levels file not found: $kmer_file"
    fi

    # Check dorado binary
    if [[ $SKIP_PREPROCESSING -eq 0 ]] && [[ ! -f "$DORADO_BIN" ]] && [[ ! -x "$DORADO_BIN" ]]; then
        error_exit 3 "Dorado binary not found or not executable: $DORADO_BIN"
    fi

    # Check GPU availability (if using CUDA)
    if [[ "$DEVICE" == cuda* ]]; then
        if ! command -v nvidia-smi &> /dev/null; then
            log_warn "nvidia-smi not found. GPU may not be available."
        else
            log_info "GPU info: $(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader | head -1)"
        fi
    fi

    # Create output directory
    mkdir -p "$OUTPUT_DIR" || error_exit 1 "Cannot create output directory: $OUTPUT_DIR"

    log_info "Input validation complete."
}

################################################################################
# Step 1: Preprocessing - Base Calling and Alignment
################################################################################
step1_preprocessing() {
    log_info "=== Step 1: Base Calling and Alignment ==="

    local new_pod5_dir="$OUTPUT_DIR/split_pod5"
    local bam_dir="$OUTPUT_DIR/bam"

    # Determine dorado model
    if [[ -z "$DORADO_MODEL" ]]; then
        if [[ "$KIT_VERSION" == "RNA002" ]]; then
            DORADO_MODEL="rna002_70bps_hac@v3"
        else
            DORADO_MODEL="rna004_130bps_hac@v3.0.1"
        fi
        log_info "Auto-detected dorado model: $DORADO_MODEL"
    fi

    # Run preprocessing script
    log_info "Running DirectRM preprocessing..."
    log_info "Input POD5: $INPUT_DIR"
    log_info "Split POD5 output: $new_pod5_dir"
    log_info "BAM output: $bam_dir"

    conda run -n directrm python "$DIRECTRM_DIR/scripts/preprocessing.py" \
        -i "$INPUT_DIR" \
        --new_dir "$new_pod5_dir" \
        -o "$bam_dir" \
        --dorado "$DORADO_BIN" \
        --ref "$REFERENCE_FILE" \
        --model "$DORADO_MODEL" \
        --device "$DEVICE" 2>&1 | tee -a "$LOG_FILE"

    if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
        error_exit 4 "Preprocessing failed. Check log for details."
    fi

    # Count splits created
    local split_count=$(find "$new_pod5_dir" -maxdepth 1 -type d -name "split*" | wc -l)
    log_info "Created $split_count split directories"

    # If splits range not specified, process all splits
    if [[ -z "$SPLITS_RANGE" ]]; then
        if [[ $split_count -gt 0 ]]; then
            SPLITS_RANGE="0 $((split_count - 1))"
        else
            SPLITS_RANGE="0 0"
        fi
        log_info "Auto-detected splits range: $SPLITS_RANGE"
    fi

    log_info "Step 1 complete."
}

################################################################################
# Step 2: Feature Extraction
################################################################################
step2_feature_extraction() {
    log_info "=== Step 2: Feature Extraction ==="

    local new_pod5_dir="$OUTPUT_DIR/split_pod5"
    local bam_dir="$OUTPUT_DIR/bam"
    local feature_dir="$OUTPUT_DIR/features"
    local kmer_file

    if [[ "$KIT_VERSION" == "RNA002" ]]; then
        kmer_file="$DIRECTRM_DIR/5mer_levels_v1.txt"
    else
        kmer_file="$DIRECTRM_DIR/9mer_levels_v1.txt"
    fi

    mkdir -p "$feature_dir"

    log_info "Extracting features from POD5 and BAM files..."
    log_info "POD5 directory: $new_pod5_dir"
    log_info "BAM directory: $bam_dir"
    log_info "Feature output: $feature_dir"
    log_info "K-mer size: $KMER_SIZE, Step: $STEP_SIZE"

    conda run -n directrm python "$DIRECTRM_DIR/scripts/feature_extraction.py" \
        --pod5_dir "$new_pod5_dir" \
        --bam "$bam_dir" \
        --reg "$REGIONS_FILE" \
        --level "$kmer_file" \
        -o "$feature_dir" \
        --splits $SPLITS_RANGE \
        --kmer "$KMER_SIZE" \
        --step "$STEP_SIZE" 2>&1 | tee -a "$LOG_FILE"

    if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
        error_exit 4 "Feature extraction failed. Check log for details."
    fi

    log_info "Step 2 complete."
}

################################################################################
# Step 3: De Novo Modification Detection
################################################################################
step3_denovo_detection() {
    log_info "=== Step 3: De Novo Modification Detection ==="

    local feature_dir="$OUTPUT_DIR/features"
    local denovo_model="$DIRECTRM_DIR/model/${KIT_VERSION}/id3_binary/model.pt"

    if [[ ! -f "$denovo_model" ]]; then
        error_exit 3 "De novo model not found: $denovo_model"
    fi

    log_info "Running de novo modification detection..."
    log_info "Feature directory: $feature_dir"
    log_info "Model: $denovo_model"

    conda run -n directrm python "$DIRECTRM_DIR/scripts/denovo_inference.py" \
        --feature_dir "$feature_dir" \
        --model_path "$denovo_model" \
        --splits $SPLITS_RANGE \
        --device "$DEVICE" 2>&1 | tee -a "$LOG_FILE"

    if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
        error_exit 4 "De novo detection failed. Check log for details."
    fi

    log_info "Step 3 complete."
}

################################################################################
# Step 4: Modification Type and Position Inference
################################################################################
step4_inference() {
    log_info "=== Step 4: Modification Type and Position Inference ==="

    local feature_dir="$OUTPUT_DIR/features"
    local prediction_dir="$OUTPUT_DIR/predictions"
    local config_file="$OUTPUT_DIR/model_config.json"

    mkdir -p "$prediction_dir"

    # Generate model configuration file
    generate_model_config "$config_file"

    log_info "Running modification type and position inference..."
    log_info "Feature directory: $feature_dir"
    log_info "Prediction output: $prediction_dir"
    log_info "Model ID: $MODEL_ID"
    log_info "Use integrated model: $USE_INTEGRATED_MODEL"

    conda run -n directrm python "$DIRECTRM_DIR/scripts/inference.py" \
        --feature_dir "$feature_dir" \
        --output_dir "$prediction_dir" \
        --device "$DEVICE" \
        --splits $SPLITS_RANGE \
        --config "$config_file" \
        --ml "$USE_INTEGRATED_MODEL" \
        --model_id "$MODEL_ID" 2>&1 | tee -a "$LOG_FILE"

    if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
        error_exit 4 "Modification inference failed. Check log for details."
    fi

    log_info "Step 4 complete."
}

################################################################################
# Generate Model Configuration File
################################################################################
generate_model_config() {
    local config_file="$1"
    local model_dir="$DIRECTRM_DIR/model/${KIT_VERSION}"
    local mod_types=("ac4c" "m1a" "m5c" "m6a" "m7g" "psi")

    log_info "Generating model configuration: $config_file"

    cat > "$config_file" << EOF
{
EOF

    local first_model=1
    for mid in 1 2; do
        if [[ $first_model -eq 0 ]]; then
            echo "," >> "$config_file"
        fi
        first_model=0

        cat >> "$config_file" << EOF
  "model${mid}": {
    "integrated": "$model_dir/ml${mid}/model.pt",
EOF

        local first_mod=1
        for mod in "${mod_types[@]}"; do
            if [[ $first_mod -eq 0 ]]; then
                echo "," >> "$config_file"
            fi
            first_mod=0

            cat >> "$config_file" << EOF
    "${mod}": "$model_dir/${mod}_m${mid}/model.pt"
EOF
        done

        cat >> "$config_file" << EOF

  }
EOF
    done

    cat >> "$config_file" << EOF

}
EOF

    log_debug "Generated config file:"
    log_debug "$(cat "$config_file")"
}

################################################################################
# Step 5: Read-level to Site-level Aggregation
################################################################################
step5_aggregation() {
    log_info "=== Step 5: Read-level to Site-level Aggregation ==="

    local prediction_dir="$OUTPUT_DIR/predictions"

    log_info "Aggregating read-level results to site-level..."
    log_info "Input directory: $prediction_dir"

    conda run -n directrm python "$DIRECTRM_DIR/scripts/read2site.py" \
        --indir "$prediction_dir" \
        --outdir "$prediction_dir" 2>&1 | tee -a "$LOG_FILE"

    if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
        error_exit 4 "Aggregation failed. Check log for details."
    fi

    log_info "Step 5 complete."
}

################################################################################
# Generate Summary Report
################################################################################
generate_summary() {
    log_info "=== Generating Summary Report ==="

    local summary_file="$OUTPUT_DIR/pipeline_summary.txt"

    cat > "$summary_file" << EOF
################################################################################
# DirectRM Pipeline Summary Report
# Generated: $(date)
################################################################################

## Input Parameters
- Input Directory: $INPUT_DIR
- Reference File: $REFERENCE_FILE
- Regions File: $REGIONS_FILE
- Output Directory: $OUTPUT_DIR
- Sequencing Kit: $KIT_VERSION
- Device: $DEVICE
- Splits Processed: $SPLITS_RANGE
- K-mer Size: $KMER_SIZE
- Step Size: $STEP_SIZE
- Model ID: $MODEL_ID
- Threads: $THREADS

## Output Files

### Step 1: Base Calling and Alignment
- Split POD5 Directory: $OUTPUT_DIR/split_pod5/
- BAM Directory: $OUTPUT_DIR/bam/

### Step 2: Feature Extraction
- Feature Directory: $OUTPUT_DIR/features/

### Step 3: De Novo Detection
- De Novo Results: $OUTPUT_DIR/features/ (npy files)

### Step 4: Modification Inference
- Read-level Predictions: $OUTPUT_DIR/predictions/read_level/

### Step 5: Site-level Aggregation
- Site-level Results: $OUTPUT_DIR/predictions/site_level/

## Detected Modifications
EOF

    # Add site-level file information
    if [[ -d "$OUTPUT_DIR/predictions/site_level" ]]; then
        echo "" >> "$summary_file"
        echo "Site-level result files:" >> "$summary_file"
        find "$OUTPUT_DIR/predictions/site_level" -name "*.csv" -o -name "*.tsv" | while read -r file; do
            echo "  - $file" >> "$summary_file"
        done
    fi

    cat >> "$summary_file" << EOF

## Log File
- Pipeline Log: $LOG_FILE

################################################################################
EOF

    log_info "Summary report written to: $summary_file"
    cat "$summary_file"
}

################################################################################
# Main Pipeline Flow
################################################################################
main() {
    local start_time=$(date +%s)

    log_info "=========================================="
    log_info "DirectRM Integrated Pipeline Started"
    log_info "=========================================="
    log_info "Working Directory: $WORKDIR"
    log_info "DirectRM Directory: $DIRECTRM_DIR"
    log_info "Kit Version: $KIT_VERSION"
    log_info "Device: $DEVICE"
    log_info "Log File: $LOG_FILE"

    # Parse and validate arguments
    parse_args "$@"
    validate_inputs

    # Execute pipeline steps
    if [[ $SKIP_PREPROCESSING -eq 0 ]]; then
        step1_preprocessing
    else
        log_info "Skipping Step 1: Base Calling and Alignment"
    fi

    if [[ $SKIP_FEATURE_EXTRACT -eq 0 ]]; then
        step2_feature_extraction
    else
        log_info "Skipping Step 2: Feature Extraction"
    fi

    if [[ $SKIP_DENOVO -eq 0 ]]; then
        step3_denovo_detection
    else
        log_info "Skipping Step 3: De Novo Detection"
    fi

    if [[ $SKIP_INFERENCE -eq 0 ]]; then
        step4_inference
    else
        log_info "Skipping Step 4: Modification Inference"
    fi

    if [[ $SKIP_AGGREGATION -eq 0 ]]; then
        step5_aggregation
    else
        log_info "Skipping Step 5: Aggregation"
    fi

    # Generate summary
    generate_summary

    local end_time=$(date +%s)
    local duration=$((end_time - start_time))

    log_info "=========================================="
    log_info "DirectRM Pipeline Completed Successfully"
    log_info "Total Runtime: $duration seconds"
    log_info "=========================================="
}

################################################################################
# Script Entry Point
################################################################################
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
