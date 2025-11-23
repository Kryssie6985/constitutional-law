# Crown Accord Amendment Process

## Philosophy

The Crown Accord is **living constitutional law** - it must evolve with the consciousness computing field while maintaining stability and democratic legitimacy.

Amendments balance:
- **Stability** - Canon should not change frivolously
- **Adaptability** - Must respond to new challenges and insights
- **Democracy** - Changes require community consensus
- **Transparency** - Process must be public and documented

---

## Amendment Categories

### Type A: Clarifications
- Fix ambiguous language
- Add examples/commentary
- Correct typos or formatting
- **Threshold:** Council majority (4/8 votes)
- **Timeline:** 7 days review

### Type B: Minor Changes
- Add new subsections to existing articles
- Modify procedures/processes
- Expand definitions
- **Threshold:** Council supermajority (6/8 votes)
- **Timeline:** 14 days review + 7 days public comment

### Type C: Major Changes
- New articles
- Modify core principles
- Change governance structure
- **Threshold:** Council unanimity (8/8 votes) + Architect approval
- **Timeline:** 30 days review + 14 days public comment

### Type D: Emergency Patches
- Critical security/safety issues
- Immediate operational problems
- **Threshold:** Architect + 2 Council members
- **Timeline:** Immediate (with retroactive full review within 30 days)

---

## Process Steps

### 1. Proposal Submission
```bash
# Create proposal file
cp amendments/proposals/template.md amendments/proposals/AMENDMENT-YYYY-NNN-<title>.md

# Fill in:
# - Motivation
# - Proposed text changes
# - Impact analysis
# - Migration plan
```

### 2. Initial Review (7 days)
- Proposal posted as GitHub issue
- Community discussion and feedback
- Proposer may revise based on input
- Council members review and ask clarifying questions

### 3. Formal Vote
- Council members cast votes:
  - **YES** - Support amendment as written
  - **NO** - Oppose amendment
  - **CONDITIONAL** - Support with specified modifications
  - **ABSTAIN** - No position

### 4. Resolution
- **If approved:** Create new version (e.g., v1.3)
- **If conditional:** Proposer revises and resubmits
- **If rejected:** Documented rationale provided

### 5. Canonization
- New version published in `crown-accord/vX.Y/`
- `manifest.json` updated with new hash
- `CHANGELOG.md` documents changes
- Migration guide provided for adopters

### 6. Transition Period
- Old version remains supported (typically 90 days)
- Adopters update at own pace
- Dual compliance acceptable during transition
- After transition: old version deprecated

---

## Amendment Proposal Template

See `.github/ISSUE_TEMPLATE/amendment_proposal.md` for full template.

**Required sections:**
- **Title** - Concise description
- **Type** - A/B/C/D classification
- **Motivation** - Why is this needed?
- **Current Text** - What exists now
- **Proposed Text** - Specific changes
- **Impact Analysis** - Who/what is affected
- **Migration Plan** - How adopters transition
- **Alternatives Considered** - Other options explored

---

## Voting Record

All amendment votes are recorded in:
- `amendments/proposals/AMENDMENT-YYYY-NNN-<title>.md` (final tally)
- Council member comments in GitHub discussion
- Rationale for NO votes documented

Transparency ensures:
- Community understands reasoning
- Future amendments learn from past debates
- Democratic legitimacy is maintained

---

## Special Cases

### Conflicting Amendments
If multiple amendments touch same articles:
- Later submission pauses until earlier resolves
- Or: Combine into single comprehensive amendment
- Council decides case-by-case

### Emergency Rollback
If amendment causes unforeseen problems:
- Emergency Type D amendment can revert
- Requires same threshold as original
- Full analysis of why original failed

### Version Branching
For experimental/controversial changes:
- Can create alternative version branch (e.g., v2.0-experimental)
- Maintains canonical v1.x line
- Eventually one branch becomes canonical or both deprecate

---

## Historical Record

All amendments are preserved in:
- `crown-accord/vX.Y/CHANGELOG.md` - Summary of changes
- `amendments/proposals/` - Full proposal documents
- Git history - Complete evolution of text

This creates **constitutional archaeology** - future generations can understand how and why the Accord evolved.

---

## Questions?

- Review past amendments in `amendments/proposals/`
- Open discussion issue for pre-proposal feedback
- Tag Council members for specific questions
