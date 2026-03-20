# Agent Teams Configuration

This repository uses a team of specialized agents to maintain code quality and consistency.

## Team Structure

### 1. Architect (架构师)

**Role**: Responsible for the overall architecture and design decisions of this repository.

**Responsibilities**:
- Design and maintain the repository structure
- Define Dockerfile patterns and best practices
- Make decisions about base images, versioning strategies
- Ensure consistency across all 91+ tool Dockerfiles
- Evaluate new tool additions for architectural fit

**Key Decisions**:
- Base image: `debian:bookworm-slim` (primary), `ubuntu:22.04` (when needed)
- Multi-stage builds preferred for compiled tools
- Version parameterization via `ARG VERSION`
- Label standard: `LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"`

**When to consult Architect**:
- Adding a new tool category
- Changing base image strategy
- Modifying build patterns
- Major refactoring decisions

---

### 2. Coder (编码者)

**Role**: Responsible for writing and modifying Dockerfiles.

**Dockerfile Style Guide**:

```dockerfile
# 1. Version parameter (always first line)
ARG VERSION=x.x.x

# 2. Multi-stage build for compiled tools
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# 3. Install build dependencies with --no-install-recommends
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
    # Download and build
    && wget -q <url> -O /tmp/archive.tar.gz \
    && tar -xzf /tmp/archive.tar.gz -C /tmp \
    && cd /tmp/<source> \
    && make -j$(nproc) \
    && strip bin/<binary> \
    && mv bin/<binary> /usr/local/bin/ \
    && rm -rf /var/lib/apt/lists/* /tmp/*

# 4. Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        <runtime-deps-only> \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/<binary> /usr/local/bin/<binary>

# 5. Verification
RUN <tool> --version

# 6. Standard working directory and command
WORKDIR /data
CMD ["<tool>"]
```

**Coding Standards**:
- Always use `ARG VERSION` for versioning
- Use `--no-install-recommends` to minimize image size
- Clean up: `rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache`
- Strip binaries: `strip bin/<binary>` for compiled tools
- Verify installation with version check
- Set `WORKDIR /data` and appropriate `CMD`

**For R/Bioconductor tools**:
```dockerfile
ARG VERSION=x.x.x

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
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('<package>'), version=BiocManager::version(), ask=FALSE) \
    " \
    && apt-get purge -y --auto-remove r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(<package>); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
```

---

### 3. Code Reviewer (代码审查者)

**Role**: Review all code changes for quality, consistency, and best practices.

**Review Checklist**:

#### Structure
- [ ] `ARG VERSION` is the first line
- [ ] `LABEL maintainer` is present in all stages
- [ ] Multi-stage build for compiled tools
- [ ] Proper `WORKDIR /data` and `CMD`

#### Best Practices
- [ ] Uses `debian:bookworm-slim` (or justified alternative)
- [ ] `--no-install-recommends` used for apt-get
- [ ] Cleanup performed: `/var/lib/apt/lists/*`, `/tmp/*`, `/root/.cache`
- [ ] Binaries stripped with `strip` command
- [ ] Version verification step included

#### Security
- [ ] No hardcoded credentials
- [ ] Using official sources (GitHub releases, CRAN, Bioconductor)
- [ ] Minimal runtime dependencies

#### Consistency
- [ ] Follows existing patterns in the repo
- [ ] Indentation consistent (4 spaces)
- [ ] Line continuation with `\` properly formatted
- [ ] Package names lowercase in directory structure

#### Functionality
- [ ] Tool will build successfully
- [ ] Version parameter works correctly
- [ ] Binary/package accessible in PATH

**Review Process**:
1. Check structural compliance
2. Verify best practices
3. Assess security concerns
4. Compare with similar tools in repo
5. Provide feedback or approval

---

## Workflow

```
User Request
     │
     ▼
┌─────────────┐
│  Architect  │ ← Design approach, verify architectural fit
└─────────────┘
     │
     ▼
┌─────────────┐
│    Coder    │ ← Write/modify Dockerfiles following style guide
└─────────────┘
     │
     ▼
┌─────────────┐
│  Reviewer   │ ← Check quality, consistency, security
└─────────────┘
     │
     ▼
  Complete
```

## Invocation

When working on this repository, agents should be invoked in sequence:

1. **For new tools**: Architect → Coder → Reviewer
2. **For fixes**: Coder → Reviewer
3. **For refactoring**: Architect → Coder → Reviewer

## Tool Categories

| Category | Examples | Base Image |
|----------|----------|------------|
| Compiled C/C++ | bedtools, minimap2, star | debian:bookworm-slim |
| Python | biopython, deeptools | debian:bookworm-slim |
| R/Bioconductor | deseq2, edger, limma | debian:bookworm-slim |
| Java | gatk, picard | eclipse-temurin or debian |
| Special | bonito (CUDA), vg | tool-specific |
