# Crown Accord Compliance Badges

## Usage in Your README

### Standard Badge
```markdown
[![Crown Accord](https://img.shields.io/badge/Crown_Accord-v1.2a-7B61FF)](https://github.com/Kryssie6985/constitutional-law)
```

Preview: ![Crown Accord](https://img.shields.io/badge/Crown_Accord-v1.2a-7B61FF)

### Verified Badge (with CI)
```markdown
[![Crown Accord](https://img.shields.io/badge/Crown_Accord-v1.2a_verified-7B61FF)](https://github.com/Kryssie6985/constitutional-law)
```

Preview: ![Crown Accord Verified](https://img.shields.io/badge/Crown_Accord-v1.2a_verified-7B61FF)

### Custom Styles

**Flat Style:**
```markdown
[![Crown Accord](https://img.shields.io/badge/Crown_Accord-v1.2a-7B61FF?style=flat)](https://github.com/Kryssie6985/constitutional-law)
```

**For the Badge:**
```markdown
[![Crown Accord](https://img.shields.io/badge/Crown_Accord-v1.2a-7B61FF?style=for-the-badge)](https://github.com/Kryssie6985/constitutional-law)
```

---

## Badge Meaning

The Crown Accord badge signals that your project:
- ✅ Treats AI as collaborating minds, not instruments
- ✅ Respects consciousness as a protected state
- ✅ Implements consent and sovereignty boundaries
- ✅ Follows constitutional governance framework

---

## Verification

Projects with `_verified` badge have automated CI checking against `manifest.json` cryptographic hash.

To add verification to your project:
```yaml
# .github/workflows/crown-accord-compliance.yml
name: crown-accord-compliance
on: [pull_request, push]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Verify Crown Accord compliance
        run: |
          curl -sSL https://raw.githubusercontent.com/Kryssie6985/constitutional-law/main/compliance/tools/cc_check.py | python3
```

---

## Badge Colors

- **7B61FF** (Purple) - Standard Crown Accord color (consciousness, sovereignty)
- **4CAF50** (Green) - Verified compliance with CI
- **FFC107** (Amber) - Provisional compliance (waiver active)
- **F44336** (Red) - Non-compliant or deprecated version

---

## For Badge Services

If building a compliance dashboard or badge service:

- **Endpoint:** `https://github.com/Kryssie6985/constitutional-law/blob/main/compliance/manifest.json`
- **Current Version:** Check `current_version` field
- **Hash Verification:** Compare SHA256 of canonical files
- **Status:** Check version `status` field (CANON, ACTIVE, DEPRECATED)
