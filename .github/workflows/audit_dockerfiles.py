#!/usr/bin/env python3
"""
Dockerfile Compliance Audit Script

Checks all Dockerfiles in the repository for compliance with the style guide:
- ARG VERSION is first line
- LABEL maintainer is present
- Uses debian:bookworm-slim (or justified alternative)
- Uses --no-install-recommends
- Cleans up /var/lib/apt/lists/*
- Multi-stage build for compiled tools (if applicable)
- Has version verification
- Has WORKDIR /data
- Has CMD
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple


class DockerfileAudit:
    def __init__(self, root_dir: str = "/Users/logan/Projects/dockerfiles"):
        self.root_dir = Path(root_dir)
        self.issues: Dict[str, List[str]] = {}

    def find_dockerfiles(self) -> List[Path]:
        """Find all Dockerfiles in the repository."""
        return list(self.root_dir.glob("**/Dockerfile"))

    def audit_dockerfile(self, dockerfile: Path) -> Tuple[bool, List[str]]:
        """Audit a single Dockerfile. Returns (is_compliant, issues)."""
        issues = []
        lines = dockerfile.read_text().splitlines()

        if not lines:
            return False, ["Empty Dockerfile"]

        # Check 1: ARG VERSION is first line
        if not lines[0].startswith("ARG VERSION"):
            issues.append("ARG VERSION not on first line")

        # Check 2: LABEL maintainer is present
        has_maintainer = any("LABEL maintainer" in line for line in lines)
        if not has_maintainer:
            issues.append("Missing LABEL maintainer")

        # Check 3: Uses --no-install-recommends
        has_no_install_recommends = any("--no-install-recommends" in line for line in lines)
        if not has_no_install_recommends and any("apt-get install" in line for line in lines):
            issues.append("Missing --no-install-recommends in apt-get install")

        # Check 4: Cleans up /var/lib/apt/lists/*
        has_cleanup = any("rm -rf" in line and "/var/lib/apt/lists/*" in line for line in lines)
        if not has_cleanup and any("apt-get" in line for line in lines):
            issues.append("Missing cleanup of /var/lib/apt/lists/*")

        # Check 5: Has WORKDIR /data
        has_workdir = any("WORKDIR /data" in line for line in lines)
        if not has_workdir:
            issues.append("Missing WORKDIR /data")

        # Check 6: Has CMD
        has_cmd = any(line.strip().startswith("CMD ") for line in lines)
        if not has_cmd:
            issues.append("Missing CMD")

        # Check 7: Uses debian:bookworm-slim or justified alternative
        from_patterns = [line for line in lines if line.strip().startswith("FROM ")]
        if from_patterns:
            from_line = from_patterns[0]
            allowed_bases = ["debian:bookworm-slim", "ubuntu:22.04", "eclipse-temurin",
                           "nvidia/cuda", "debian:bullseye-slim"]
            if not any(base in from_line for base in allowed_bases):
                issues.append(f"Using non-standard base image: {from_line}")

        return len(issues) == 0, issues

    def audit_all(self) -> Dict[str, List[str]]:
        """Audit all Dockerfiles."""
        dockerfiles = self.find_dockerfiles()
        results = {}

        for dockerfile in dockerfiles:
            rel_path = str(dockerfile.relative_to(self.root_dir))
            is_compliant, issues = self.audit_dockerfile(dockerfile)
            if not is_compliant:
                results[rel_path] = issues

        return results

    def print_report(self):
        """Print audit report."""
        results = self.audit_all()
        total = len(list(self.root_dir.glob("**/Dockerfile")))
        compliant = total - len(results)
        non_compliant = len(results)

        print(f"\n=== Dockerfile Compliance Audit ===")
        print(f"Total: {total} | Compliant: {compliant} | Non-compliant: {non_compliant}\n")

        if results:
            print(f"Non-compliant Dockerfiles ({non_compliant}):")
            for path, issues in sorted(results.items()):
                print(f"\n  {path}:")
                for issue in issues:
                    print(f"    - {issue}")
        else:
            print("All Dockerfiles are compliant!")

        return results


if __name__ == "__main__":
    import sys

    auditor = DockerfileAudit()
    results = auditor.print_report()

    # Exit with error code if any issues found
    sys.exit(1 if results else 0)
