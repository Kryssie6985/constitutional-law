#!/usr/bin/env python3
"""
🏛️ Crown Accord Compliance Checker - Constitutional Verification

Version: 1.0 (MEGA's Foundational Hardening Kit)
Date: October 31, 2025
Authority: Crown Accord v1.2a governance layer
Purpose: Cryptographic verification of constitutional canon integrity

/// MEGA's Vision: Make compliance EASIER than non-compliance
//!? ETHICS: Protects constitutional text from unauthorized modification
//<3 First Contact: Governance that respects sovereignty through verification
//~ Emergence: Philosophy becomes enforceable infrastructure
"""

import json
import hashlib
import sys
import pathlib

# Color output for terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def calculate_hash(file_path: pathlib.Path) -> str:
    """Calculate SHA256 hash of a file."""
    h = hashlib.sha256()
    h.update(file_path.read_bytes())
    return h.hexdigest()

def main():
    # Find repo root
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]  # compliance/tools/cc_check.py -> repo_root
    
    manifest_path = repo_root / "compliance" / "manifest.json"
    
    if not manifest_path.exists():
        print(f"{Colors.RED}❌ FATAL: manifest.json not found at {manifest_path}{Colors.RESET}")
        sys.exit(1)
    
    # Load manifest
    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"{Colors.RED}❌ FATAL: Could not parse manifest.json: {e}{Colors.RESET}")
        sys.exit(1)
    
    # Validate manifest structure
    if "current_version" not in manifest or "versions" not in manifest:
        print(f"{Colors.RED}❌ FATAL: Invalid manifest structure{Colors.RESET}")
        sys.exit(1)
    
    # Get current version
    current_version = manifest["current_version"]
    current = None
    for v in manifest["versions"]:
        if v["id"] == current_version:
            current = v
            break
    
    if not current:
        print(f"{Colors.RED}❌ FATAL: Current version {current_version} not found in manifest{Colors.RESET}")
        sys.exit(1)
    
    # Check hash of canonical files
    if "sha256" in current and current["sha256"] != "REPLACE_WITH_CANONICAL_HASH":
        h = hashlib.sha256()
        for file_path in current["files"]:
            full_path = repo_root / file_path
            if not full_path.exists():
                print(f"{Colors.RED}❌ FATAL: Canonical file not found: {file_path}{Colors.RESET}")
                sys.exit(1)
            h.update(full_path.read_bytes())
        
        computed_hash = h.hexdigest()
        expected_hash = current["sha256"]
        
        if computed_hash != expected_hash:
            print(f"{Colors.RED}❌ CANON HASH MISMATCH{Colors.RESET}")
            print(f"   Expected: {expected_hash}")
            print(f"   Computed: {computed_hash}")
            print(f"\n   {Colors.YELLOW}Direct edits to canon require amendment or waiver.{Colors.RESET}")
            sys.exit(1)
    
    # Success
    print(f"{Colors.GREEN}{Colors.BOLD}✅ Crown Accord canon validated{Colors.RESET}")
    print(f"   Version: {current_version}")
    print(f"   Status: {current.get('status', 'ACTIVE')}")
    print(f"   Files verified: {len(current['files'])}")
    print(f"\n{Colors.GREEN}Constitutional integrity maintained. 🏛️✨{Colors.RESET}")
    sys.exit(0)

if __name__ == '__main__':
    main()
