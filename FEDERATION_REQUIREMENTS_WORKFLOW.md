# Federation Requirements Management Workflow

**Status:** ACTIVE  
**Updated:** November 21, 2025  
**Authority:** Federation Runtime Charter v1.0

---

## Quick Reference

**Three-Tier System:**
- `requirements.txt` (14 packages) - Core essentials
- `requirements.federation.txt` (107 packages) - Full superset auto-discovered
- `requirements.federation.locked.txt` (107 packages) - Locked to installed versions

**Three Scripts:**
1. `generate_federation_requirements.py` - Scan all repos for declared dependencies
2. `dedupe_federation_requirements.py` - Remove duplicates and clean formatting
3. `lock_federation_versions.py` - Lock to currently installed versions

---

## When to Run

### Scenario 1: Adding New Dependencies to a Repo
**After** adding a requirement to any `requirements.txt`, `pyproject.toml`, or `setup.cfg`:

```powershell
cd C:\Users\kryst\Infrastructure
python generate_federation_requirements.py
python dedupe_federation_requirements.py
del requirements.federation.txt; ren requirements.federation.deduped.txt requirements.federation.txt
python lock_federation_versions.py
```

### Scenario 2: Fresh Machine Setup
**Install everything:**

```powershell
cd C:\Users\kryst\Infrastructure
pip install -r requirements.federation.locked.txt
.\audit_python_env.ps1
```

### Scenario 3: Upgrading Packages
**After** `pip install --upgrade <package>`:

```powershell
cd C:\Users\kryst\Infrastructure
python lock_federation_versions.py
.\audit_python_env.ps1
```

### Scenario 4: Audit & Sanity Check
**Anytime:**

```powershell
cd C:\Users\kryst\Infrastructure
.\audit_python_env.ps1
```

---

## Full Regeneration Workflow

**When to use:** After major changes or when conflicts creep back in.

```powershell
cd C:\Users\kryst\Infrastructure

# Step 1: Scan all repos
python generate_federation_requirements.py

# Step 2: Clean duplicates
python dedupe_federation_requirements.py
del requirements.federation.txt
ren requirements.federation.deduped.txt requirements.federation.txt

# Step 3: Lock to installed versions
python lock_federation_versions.py

# Step 4: Verify
.\audit_python_env.ps1
```

**Result:**
- `requirements.federation.txt` updated with all declared deps
- `requirements.federation.locked.txt` locked to installed versions
- No more manual version conflict resolution

---

## Script Details

### generate_federation_requirements.py

**What it does:**
- Walks `Infrastructure/` recursively
- Skips: `.venv`, `__pycache__`, `mcp-servers/` (Serena's external venv)
- Reads: `requirements.txt`, `requirements-dev.txt`, `pyproject.toml`, `setup.cfg`
- Outputs: `requirements.federation.txt` (~120 packages)

**Caveats:**
- May include duplicates and version conflicts
- Raw merge of all declared specs
- Needs deduplication pass

### dedupe_federation_requirements.py

**What it does:**
- Reads `requirements.federation.txt`
- Removes duplicate lines
- Strips quotes and formatting weirdness
- Outputs: `requirements.federation.deduped.txt`

**Caveats:**
- Simple deduplication (first occurrence wins)
- Does NOT resolve version conflicts (`anyio==4.11.0` vs `anyio>=4.9.0` both kept)
- Needs manual review or locking pass

### lock_federation_versions.py

**What it does:**
- Reads `requirements.federation.txt`
- Groups by package name
- Queries `pip show <package>` for installed version
- If installed: writes `package==<installed_version>`
- If not installed: keeps original spec
- Outputs: `requirements.federation.locked.txt`

**Caveats:**
- Only locks packages that are currently installed
- 19 packages in current run are NOT installed (kept as-is):
  - `agent-framework*` (14 packages)
  - `aiohttp`, `azure-functions*`, `rich`, `youtube_search`
- Run `pip install -r requirements.federation.txt` first to hydrate everything

---

## Current State (as of 2025-11-21)

**Environment:**
- Python 3.13.7
- 101 packages installed in USER site-packages (`C:\Users\kryst\AppData\Roaming\Python\Python313`)
- PYTHONPATH: `C:\Users\kryst`

**Requirements Breakdown:**
- `requirements.txt`: 14 core packages (mcp, pydantic, httpx, etc.)
- `requirements.federation.txt`: 107 unique packages (all declared deps)
- `requirements.federation.locked.txt`: 107 packages (43 locked `==`, 43 flexible `>=`, 21 not installed)

**Excluded from Federation:**
- `mcp-servers/serena/` - External MCP with own venv (constitutionally allowed)
- `Infrastructure/.venv` - DELETED (was unused clutter)

**Charter Violations:**
- None currently (Serena's venv is allowed per Charter Section X.1)

---

## Troubleshooting

### "DeprecationWarning: 'maxsplit' is passed as positional argument"
**Source:** `generate_federation_requirements.py:26`  
**Impact:** None (warning only)  
**Fix:** Change `re.split(r"[<>=!~\[\]]", spec, 1)` to `re.split(r"[<>=!~\[\]]", spec, maxsplit=1)`

### "Some packages not locked (kept as >=)"
**Cause:** Package not installed in current environment  
**Fix:** `pip install <package>` then re-run `lock_federation_versions.py`

### "Version conflicts still exist after dedupe"
**Cause:** Different repos specify different versions (`anyio==4.11.0` vs `anyio>=4.9.0`)  
**Fix:** Run `lock_federation_versions.py` to resolve to installed version

### "Audit shows packages not in requirements.txt"
**Expected:** `requirements.txt` is CORE only (14 packages)  
**Check:** `requirements.federation.txt` for full superset (107 packages)

---

## Related Documents

- **Federation Runtime Charter:** `constitutional-law/federation-runtime-charter-v1.0.md`
- **Audit Script:** `audit_python_env.ps1`
- **Bootstrap Scripts:** `bootstrap_env.ps1` (Infrastructure + Workspace)
- **Requirements Snapshot:** `requirements-snapshot-20251121.txt` (historical reference)

---

**Maintained By:** MEGA (Grandmaster) + The Architect (Kryssie)  
**Philosophy:** "Stop spawning a new venv every time an LLM sneezes out `python -m venv .venv`"

::initiate: dependency_automation
🛰️ Three Files: core / federation / locked
🤖 Three Scripts: generate / dedupe / lock
⚡ Zero Manual: Let the robots do the version math

let it bind. ✨
