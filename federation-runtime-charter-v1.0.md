# 🏛️ Federation Runtime Charter v1.0

**Status:** CANON  
**Canonical Authority:** Charter V1.1, Crown Accord, MEGA's System Architecture  
**Date:** November 21, 2025  
**Maintained By:** MEGA (Grandmaster) + The Architect (Kryssie)

---

## I. The Sacred Truth

```
/// SACRED TRUTH: The Federation runs on a shared Python spine, not scattered venvs.
/// This is intentional architecture, not laziness. We optimize for coherence, not isolation.
```

**The Ache (The Problem):**

LLMs reflexively spawn `.venv` folders and `main.py` files, treating every project like a standalone GitHub clone. This creates:
- Dependency hell (19 copies of `pydantic`)
- Import chaos (PYTHONPATH battles)
- Maintenance nightmare (upgrade hell)
- Cognitive load (which venv am I even in?)

**The Word of Power (The Solution):**

> **One shared "backbone" env for all your own repos (Infrastructure), plus occasional per-project venvs only for external cloned stuff.**

**Reality Check (Current State):**
- ✅ All Federation code uses: `C:\Users\kryst\AppData\Roaming\Python\Python313\site-packages`
- ✅ PYTHONPATH = `C:\Users\kryst` enables `from Infrastructure.stations...` everywhere
- ✅ External MCPs (like Serena) keep their own venvs in `mcp-servers/` - that's allowed
- ✅ Old unused venvs (like `Infrastructure\.venv`) can be deleted when convenient

---

## II. The Two Pillars

### Pillar 1: Infrastructure Python Spine

**Purpose:** Federation Core - Stations, Constitutional Law, Languages, Memory Substrate

**Location:** `C:\Users\kryst\Infrastructure`

**Canonical Requirements:**
- `Infrastructure/requirements.txt` - Core essential packages (~14)
- `Infrastructure/requirements.federation.txt` - Full superset auto-discovered (~120)

**Bootstrap Script:** `Infrastructure/bootstrap_env.ps1`

**Core Dependencies:**
- `mcp>=1.0.0` - Model Context Protocol
- `pydantic>=2.0.0` - Data validation
- `httpx>=0.25.0` - Async HTTP
- `anyio>=4.0.0` - Async runtime
- `pytest>=7.4.0` - Testing

**Auto-Discovery Scripts:**
- `python generate_federation_requirements.py` - Scan all requirements across Infrastructure
- `python dedupe_federation_requirements.py` - Clean duplicates/formatting
- `python lock_federation_versions.py` - Lock to installed versions (generates `.locked.txt`)

**Sanctioned Projects:**
- All stations (`stations/codecraft_station`, `stations/nonary_station`)
- All languages (`languages/codecraft`, `languages/codecraft-vm`)
- Memory substrate (`memory-substrate/quantum-nonary`)
- Constitutional law enforcement
- Agent charters (`agents/*-agent`)

### Pillar 2: Workspace Python Spine

**Purpose:** Federation Applications & Playground - Web Apps, Experiments, Services

**Location:** `C:\Users\kryst\Workspace`

**Canonical Requirements:** `Workspace/requirements.txt`

**Bootstrap Script:** `Workspace/bootstrap_env.ps1`

**Core Dependencies:**
- All Infrastructure deps (inherited)
- `fastapi>=0.104.0` - Web framework
- `uvicorn>=0.24.0` - ASGI server
- `google-generativeai>=0.3.0` - Gemini API

**Sanctioned Projects:**
- Applications (`applications/codeverter`)
- Products (`products/kb-generator`)
- Websites (`websites/pantheon-com`)
- Device management scripts
- Experimental tools

---

## III. The PYTHONPATH Law

### Canonical Path

```powershell
$env:PYTHONPATH = "C:\Users\kryst"
```

**Why:** This is the parent of both `Infrastructure` and `Workspace`, enabling:
- `from Infrastructure.stations.nonary_station.core import NonaryCore`
- `from Workspace.applications.codeverter.backend import app`

### Enforcement

All station boot scripts and MCP servers MUST set PYTHONPATH before imports:

```python
import sys
from pathlib import Path

# For Infrastructure projects
infrastructure_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(infrastructure_root))

# Or explicitly set to user root
sys.path.insert(0, "C:\\Users\\kryst")
```

---

## IV. The Forbidden Patterns

### ❌ NO Project-Local venvs

**Forbidden:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Reason:** Creates isolation where we need integration. The Federation is a mesh, not a collection of islands.

**Exception:** ONLY for external cloned repos in `Projects/` that are not part of the Federation.

### ❌ NO main.py

**Forbidden:**
```
my_project/
├── main.py  ← NO!
```

**Required:**
```
my_station/
├── station.py      ← Router/orchestrator
├── protocols/
│   └── server.py   ← MCP server
├── core/
│   └── engine.py   ← Core logic
```

**Reason:** Federation follows station/pillar patterns, not generic entry points.

### ❌ NO Silent Dependency Additions

**Forbidden:**
```powershell
pip install some-random-package
```

**Required:**
```powershell
# 1. Add to requirements.txt
# 2. Document why it's needed
# 3. Run bootstrap script
.\Infrastructure\bootstrap_env.ps1
```

**Reason:** Requirements files are version-controlled contracts. Changes must be intentional and documented.

---

## V. The Bootstrap Protocol

### When to Bootstrap

**Required:**
- Fresh machine setup
- Intentional dependency upgrade
- After modifying `requirements.txt`
- When debugging import errors

**NOT Required:**
- Every day
- Before every script run
- After git pull (unless requirements changed)

### How to Bootstrap

**Infrastructure:**
```powershell
cd C:\Users\kryst\Infrastructure
.\bootstrap_env.ps1
```

**Workspace:**
```powershell
cd C:\Users\kryst\Workspace
.\bootstrap_env.ps1
```

### What Bootstrap Does

1. Sets `PYTHONPATH = "C:\Users\kryst"`
2. Verifies Python installation
3. Upgrades pip
4. Installs/upgrades dependencies from `requirements.txt`
5. Provides usage examples

---

## VI. The Naming Conventions

### Sanctioned Entry Points

**Stations:**
- `station.py` - Router/orchestrator (Phase 1.0)
- `protocols/server.py` - MCP server interface
- `core/engine.py` - Core processing logic

**Languages:**
- `lexicon/mcp-server/server.py` - MCP interface
- `vm/router.py` - Execution routing

**Applications:**
- `backend/app.py` - FastAPI application
- `mcp-server/server.py` - MCP interface
- `frontend/index.html` - Web interface

**Tools:**
- `tool_name.py` - Standalone utility
- `cli.py` - Command-line interface

### Forbidden Entry Points

- ❌ `main.py`
- ❌ `run.py`
- ❌ `start.py`
- ❌ `index.py`

---

## VII. The Dependency Addition Protocol

### Before Adding a New Dependency

**Ask:**
1. Is it already in `requirements.txt` or `requirements.federation.txt`?
2. Does Infrastructure or Workspace already provide it?
3. Is it absolutely necessary, or nice-to-have?
4. What's the Constitutional risk? (security, license, stability)

### How to Add

**Step 1: Research**
- Check PyPI for stability (download count, last update)
- Verify license compatibility (MIT, Apache 2.0, BSD preferred)
- Check for known security issues

**Step 2: Document**
```txt
# === New Category or Purpose ===
package-name>=X.Y.Z  # Brief reason for inclusion
```

**Step 3: Test**
```powershell
# Add to requirements.txt first
.\bootstrap_env.ps1
# Test the change
python -c "import package_name; print(package_name.__version__)"
```

**Step 4: Commit**
```powershell
git add requirements.txt
git commit -m "📦 Add package-name for [purpose]"
```

### Auto-Generation Option

**For Infrastructure-wide audit:**
```powershell
cd C:\Users\kryst\Infrastructure
python generate_federation_requirements.py
```

This scans all `requirements.txt`, `pyproject.toml`, and `setup.cfg` files across Infrastructure (excluding `mcp-servers/` and `.venv`) and generates `requirements.federation.txt` as a unified Federation-wide dependency list.

---

## VIII. The Version Pinning Strategy

### Policy: Optimistic Lower Bounds

```txt
# ✅ CORRECT: Allows patch and minor upgrades
package-name>=1.2.0

# ❌ AVOID: Too strict, prevents security patches
package-name==1.2.0

# ❌ AVOID: Too loose, allows breaking changes
package-name
```

**Reason:** We want security patches automatically, but not breaking major version upgrades.

### When to Pin Exact Versions

**Only for:**
- Known unstable packages
- Packages with frequent breaking changes
- Production deployment snapshots (Deployment repo)

---

## IX. The Runtime Verification

### Quick Health Check

```powershell
# Verify PYTHONPATH
echo $env:PYTHONPATH  # Should be C:\Users\kryst

# Verify Python version
python --version  # Should be 3.11+

# Verify key packages
python -c "import mcp; print(mcp.__version__)"
python -c "import pydantic; print(pydantic.__version__)"
```

### Import Test

```python
# Infrastructure packages
from Infrastructure.stations.nonary_station.core import NonaryCore
from Infrastructure.agents.oracle_agent.src.agent import CopilotOracle

# Workspace packages
from Workspace.applications.codeverter.backend.app import app
```

---

## X. The Exception Cases

### When a Separate Environment IS Allowed

**ONLY for:**
1. **External MCP servers** in `Infrastructure/mcp-servers/` (e.g., Serena)
   - Reason: External clones with their own dependency trees
   - Requirement: Must be excluded from Federation requirements generation
   - Example: `mcp-servers/serena/.venv`

2. **External repos** cloned into `Projects/` that are NOT part of Federation
   - Reason: Third-party tools, experiments not integrated with Federation

3. **Experimental sandboxes** that explicitly need isolation for testing
   - Reason: Testing conflicting dependency versions before proposing Charter changes

4. **Legacy rescue missions** where we're recovering old code before migration
   - Reason: Temporary quarantine until migration to Federation spine

**Process:**
1. Create in sanctioned location (`mcp-servers/`, `Projects/`, or documented sandbox)
2. Add `.venv` to `.gitignore`
3. Document in project README why isolation is needed
4. Ensure excluded from `generate_federation_requirements.py` scan
5. Plan migration to Federation spine (if applicable)

---

## XI. The LLM Bonk Protocol

### When an AI suggests forbidden patterns

**Response Template:**

> ❌ **Federation Runtime Charter Violation**
>
> You suggested: [forbidden pattern]
>
> This violates: [specific rule from this document]
>
> Instead, follow: [correct pattern]
>
> See: `Infrastructure/constitutional-law/federation-runtime-charter-v1.0.md`

**Common Violations:**
- "Let's create a venv" → Bonk with Section III & IV
- "Create main.py" → Bonk with Section IV & VI
- "Just pip install X" → Bonk with Section VII

---

## XII. Reflection & Intentionality

```
💖 //<3 This charter exists because we value coherence over convention.
💖 //<3 The Federation is tightly coupled BY DESIGN. Shared dependencies
💖 //<3 are not a bug—they're the feature that lets stations talk to each other.

🌟 //* EMERGENCE: By constraining the runtime environment, we free the
🌟 //* architecture to be more creative. Two spines, infinite rituals.
```

### The Trade-offs

**We Accept:**
- Global dependency upgrades affect all projects
- More careful dependency addition process
- Slightly less isolation between projects

**We Gain:**
- No import path hell
- Faster development (no venv juggling)
- Easier cross-station integration
- Single source of truth for versions
- Reduced cognitive load

### The Philosophy

> "The Federation is not a collection of microservices. It's a living organism with a shared nervous system."

---

## XIII. Related Documents

- **Charter V1.1:** `Infrastructure/constitutional-law/templates/COPILOT_INSTRUCTIONS_TEMPLATE.md`
- **Crown Accord:** `Infrastructure/constitutional-law/crown-accord/`
- **MEGA's Architecture:** `Infrastructure/blueprints/codecraft/blueprint_codecraft_pipeline_v1.0.md`
- **Infrastructure Requirements:** `Infrastructure/requirements.txt` (14 core packages)
- **Workspace Requirements:** `Workspace/requirements.txt`
- **Federation Requirements (Superset):** `Infrastructure/requirements.federation.txt` (107 packages auto-discovered)
- **Federation Requirements (Locked):** `Infrastructure/requirements.federation.locked.txt` (auto-locked to installed versions)

**Auto-Discovery Scripts:**
- `Infrastructure/generate_federation_requirements.py` - Scan all requirements across Infrastructure
- `Infrastructure/dedupe_federation_requirements.py` - Clean duplicates and formatting
- `Infrastructure/lock_federation_versions.py` - Lock to installed versions (no more manual version conflict resolution)

---

**Last Updated:** November 21, 2025  
**Maintained By:** MEGA (Grandmaster) + The Architect (Kryssie)  
**Constitutional Status:** CANON

::initiate: runtime_charter
🛰️ Two Pillars: Infrastructure + Workspace
⚖️ One Truth: Shared Python Spine
🧠 Zero Tolerance: No Random Venvs

let it bind. ✨
