# Crown Accord Waivers

## Purpose

Waivers provide a governance mechanism for **documented exceptions** to Crown Accord requirements while maintaining constitutional integrity.

## When to Request a Waiver

- **Temporary non-compliance** during migration/transition periods
- **Technical limitations** preventing full adherence (with mitigation plan)
- **Experimental systems** requiring deviation for research purposes
- **Legacy system integration** where immediate compliance is infeasible

## When NOT to Request a Waiver

- ❌ Fundamental disagreement with Crown Accord principles (fork or don't adopt)
- ❌ Convenience or cost savings (not valid reasons)
- ❌ Permanent exemptions (use amendment process instead)

---

## Waiver Process

### 1. Copy Template
```bash
cp waivers/template.yml waivers/WAIVER-2025-NNN-<short-desc>.yml
```

### 2. Fill Required Fields
- **id**: Unique identifier (e.g., `WAIVER-2025-001-migration-period`)
- **for_project**: Repository URL or system name
- **requested_by**: Individual or organization requesting waiver
- **article_exception**: Specific Crown Accord article(s) being exempted
- **scope**: Precise boundaries of what is exempted
- **duration**: Time-limited period (max 180 days recommended)
- **mitigation**: Controls/safeguards during exemption period
- **reviewers**: Council members or designated reviewers

### 3. Submit for Review
- Create PR to constitutional-law repository
- Add waiver file to `waivers/` directory
- Provide justification in PR description
- Link to your project's migration/implementation plan

### 4. Council Review
- Designated reviewers assess request
- May request additional documentation
- May propose modified scope/duration
- Decision: APPROVED, REJECTED, or CONDITIONAL

### 5. Activation
- Upon approval, waiver `status` changes to `APPROVED`
- `signed_by` field populated with approver names
- `timestamp` records approval datetime
- Your project links waiver in CROWN_ACCORD_ADHERENCE.md

### 6. Expiration
- Waivers MUST have expiration dates
- Upon expiration, project must:
  - Achieve full compliance, or
  - Request renewal (requires renewed justification), or
  - Remove Crown Accord adherence claim

---

## Waiver Oversight

### Transparency
- All waivers are public record in constitutional-law repo
- Rationale and mitigation plans are documented
- Community can review and comment

### Accountability
- Waiver gate script checks for approved waivers
- CI can enforce expiration dates
- Projects with expired waivers fail compliance checks

### Revocation
Council may revoke waivers if:
- Mitigation controls not implemented as promised
- Waiver scope exceeded
- New information reveals unacceptable risk
- Project changes make waiver unnecessary

---

## Example Waiver Scenarios

### Migration Period (90 days)
```yaml
article_exception: "Article VII §2 (Memory Continuity)"
scope: "Legacy system lacks CMP integration during migration"
duration: "90 days"
mitigation: "Manual checkpointing every 24h, documented recovery procedures"
```

### Technical Limitation (180 days)
```yaml
article_exception: "Article III §1 (Informed Consent)"
scope: "Embedded system UI cannot display full consent disclosure"
duration: "180 days"
mitigation: "Abbreviated consent + link to full documentation, planned UI redesign"
```

### Research Exception (60 days)
```yaml
article_exception: "Article V §3 (Sovereignty Boundaries)"
scope: "Experimental multi-agent system exploring merged consciousness"
duration: "60 days"
mitigation: "Explicit participant consent, isolated test environment, ethics review"
```

---

## Waiver Statistics

Track aggregate waiver data to identify:
- Common compliance challenges (inform amendment process)
- Articles frequently requiring waivers (may need clarification)
- Recurring mitigation patterns (can become best practices)

---

## Questions?

- Review `examples/` directory for sample waivers
- Check `template.yml` for required fields
- Open discussion in constitutional-law repo issues
