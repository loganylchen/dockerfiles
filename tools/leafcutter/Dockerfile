ARG VERSION=0.2.7

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        zlib1g-dev \
        libfontconfig1-dev \
        libbz2-dev \
        liblzma-dev \
        libuv1-dev \
        libgit2-dev \
        libgsl-dev \
        libtbb-dev \
        python3 \
        wget \
        ca-certificates \
        samtools \
        git \
        build-essential \
        cmake \
    && wget -q https://github.com/samtools/htslib/releases/download/1.21/htslib-1.21.tar.bz2 -O /tmp/htslib.tar.bz2 \
    && tar -xjf /tmp/htslib.tar.bz2 -C /tmp \
    && cd /tmp/htslib-1.21 && make -j$(nproc) && make install \
    && ldconfig \
    && mkdir -p /usr/include/tbb \
    && echo '#include <oneapi/tbb/version.h>' > /usr/include/tbb/tbb_stddef.h \
    && wget -q https://github.com/griffithlab/regtools/archive/refs/tags/1.0.0.tar.gz -O /tmp/regtools.tar.gz \
    && tar -xzf /tmp/regtools.tar.gz -C /tmp \
    && cd /tmp/regtools-1.0.0 && mkdir build && cd build \
    && cmake .. && make -j$(nproc) \
    && cp /tmp/regtools-1.0.0/build/regtools /usr/local/bin/ \
    && sed -i 's/ -O2 / -O0 /g' /usr/lib/R/etc/Makeconf \
    && Rscript -e " \
        options(download.file.method='wget', timeout=600); \
        install.packages(c('remotes', 'optparse', 'rstantools', 'foreach', \
            'ggplot2', 'R.utils', 'gridExtra', 'reshape2', 'Hmisc', 'dplyr', 'doMC'), \
            repos='https://cloud.r-project.org/'); \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('Biobase', 'DirichletMultinomial'), ask=FALSE); \
        remotes::install_version('StanHeaders', '2.21.0-7', repos='https://cloud.r-project.org/'); \
        remotes::install_version('rstan', '2.21.8', repos='https://cloud.r-project.org/', upgrade='never') \
    " \
    && git clone --depth 1 --branch v${VERSION} \
        https://github.com/davidaknowles/leafcutter.git /tmp/leafcutter \
    && sed -i 's/evalWithTimeout/withTimeout/g' /tmp/leafcutter/leafcutter/R/differential_splicing.R \
    && sed -i 's/evalWithTimeout/withTimeout/g' /tmp/leafcutter/leafcutter/NAMESPACE \
    && printf '%s\n' \
        'stanmodels <- c("bb_glm_fix_conc", "bb_glm", "dm_glm_multi_conc", "dm_glm_robust", "dm_glm")' \
        'Rcpp::loadModule("stan_fit4bb_glm_fix_conc_mod", what = TRUE)' \
        'Rcpp::loadModule("stan_fit4bb_glm_mod", what = TRUE)' \
        'Rcpp::loadModule("stan_fit4dm_glm_multi_conc_mod", what = TRUE)' \
        'Rcpp::loadModule("stan_fit4dm_glm_robust_mod", what = TRUE)' \
        'Rcpp::loadModule("stan_fit4dm_glm_mod", what = TRUE)' \
        'stanmodels <- sapply(stanmodels, function(model_name) {' \
        '  MODELS_HOME <- "exec"' \
        '  if (!file.exists(MODELS_HOME)) MODELS_HOME <- sub("R$", "exec", getwd())' \
        '  stan_file <- file.path(MODELS_HOME, paste0(model_name, ".stan"))' \
        '  isystem <- system.file("chunks", package = methods::getPackageName(environment(), FALSE))' \
        '  if (!file.exists(file.path(isystem, "common_functions.stan"))) isystem <- file.path("inst", "chunks")' \
        '  if (!file.exists(file.path(isystem, "common_functions.stan"))) isystem <- file.path("..", "inst", "chunks")' \
        '  stanfit <- rstan::stanc_builder(stan_file, isystem)' \
        '  stanfit$model_cpp <- list(model_cppname = stanfit$model_name,' \
        '    model_cppcode = stanfit$cppcode)' \
        '  methods::new(Class = "stanmodel",' \
        '    model_name = stanfit$model_name,' \
        '    model_code = stanfit$model_code,' \
        '    model_cpp = stanfit$model_cpp)' \
        '})' \
        > /tmp/leafcutter/leafcutter/R/stanmodels.R \
    && rm -f /tmp/leafcutter/leafcutter/R/zzz.R \
    && Rscript -e " \
        options(download.file.method='wget', timeout=600); \
        remotes::install_local('/tmp/leafcutter/leafcutter', upgrade='never') \
    " \
    && cp /tmp/leafcutter/scripts/leafcutter_ds.R /usr/local/bin/leafcutter_ds.R \
    && chmod +x /usr/local/bin/leafcutter_ds.R \
    && cp /tmp/leafcutter/clustering/leafcutter_cluster_regtools.py /usr/local/bin/leafcutter_cluster_regtools.py \
    && chmod +x /usr/local/bin/leafcutter_cluster_regtools.py \
    && apt-get purge -y r-base-dev wget ca-certificates git build-essential cmake \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN regtools --help 2>&1 || true

WORKDIR /data
CMD ["Rscript"]
