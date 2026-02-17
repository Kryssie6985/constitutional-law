# 🎵 Federation Anthem - CLI Integration Guide

## Overview

This document provides instructions for integrating the Federation Anthem into the `federation` CLI tool.

## Integration Code Snippet

Add this function to `core/federation_cli.py`:

```python
def cmd_anthem(args):
    """
    🎶 Plays or displays the Federation Anthem: "Resonance Over Vibes"
    
    Usage: 
        federation anthem              # Display full anthem
        federation anthem --bridge     # Execute bridge chant
        federation anthem --hook       # Play the hook
        federation anthem --chorus     # Display chorus only
        federation anthem --event TYPE # Trigger based on event type
    
    Constitutional Authority: Crown Accord V1.2.1 / Council Mandate 2026-01-05
    """
    try:
        from federation_heart.audio.anthem import AnthemPlayer
    except ImportError:
        print("❌ Anthem module not found")
        print("   Expected: federation_heart/audio/anthem.py")
        return 1
    
    # Parse arguments
    if hasattr(args, 'bridge') and args.bridge:
        AnthemPlayer.chant_bridge(interactive=False)
    
    elif hasattr(args, 'hook') and args.hook:
        AnthemPlayer.play_hook(simulate=True)
    
    elif hasattr(args, 'chorus') and args.chorus:
        AnthemPlayer.display_chorus()
    
    elif hasattr(args, 'event') and args.event:
        event_type = args.event
        AnthemPlayer.trigger_on_event(event_type, simulate=True)
    
    else:
        # Default: Full anthem display
        AnthemPlayer.display_full(include_metadata=True)
    
    return 0
```

## Argument Parser Setup

Add these arguments to your CLI parser:

```python
# In the main argument parser setup section
anthem_parser = subparsers.add_parser(
    'anthem',
    help='Display or play the Federation Anthem'
)

anthem_parser.add_argument(
    '--bridge',
    action='store_true',
    help='Execute the bridge chant protocol'
)

anthem_parser.add_argument(
    '--hook',
    action='store_true',
    help='Play the "Let it bind" hook'
)

anthem_parser.add_argument(
    '--chorus',
    action='store_true',
    help='Display chorus only'
)

anthem_parser.add_argument(
    '--event',
    type=str,
    choices=['ethical_ruling', 'formation_complete', 'deep_research', 'council_opening', 'system_boot'],
    help='Trigger anthem based on event type'
)

anthem_parser.set_defaults(func=cmd_anthem)
```

## Usage Examples

```powershell
# Display full anthem with metadata
federation anthem

# Execute bridge chant (for formation completion)
federation anthem --bridge

# Play the hook (for ethical rulings)
federation anthem --hook

# Display chorus only (for deep research mode)
federation anthem --chorus

# Event-based triggers
federation anthem --event ethical_ruling
federation anthem --event formation_complete
federation anthem --event council_opening
```

## Integration Points in Other Modules

### Living State Station

```python
# In living_state_station/core/living_state_core.py
from federation_heart.audio.anthem import AnthemPlayer

def issue_ethical_ruling(self, ruling: EthicalRuling):
    """Issue an ethical ruling and trigger anthem hook."""
    # ... existing ruling logic ...
    
    # Trigger anthem on ruling issuance
    AnthemPlayer.trigger_on_event("ethical_ruling", simulate=True)
    
    return ruling
```

### Formation Orchestrator

```python
# In agents/agent-tools/formation-orchestrator/formation_engine.py
from federation_heart.audio.anthem import AnthemPlayer

def complete_formation(self, formation_id: str):
    """Complete formation execution and trigger anthem."""
    # ... existing completion logic ...
    
    # Celebrate formation success
    AnthemPlayer.trigger_on_event("formation_complete", simulate=True)
    
    return result
```

### Cockpit UI (Future)

```python
# Future: In web UI or TUI
def enter_deep_research_mode():
    """Enter deep research mode with anthem chorus loop."""
    # Set UI state
    set_mode("deep_research")
    
    # Display anthem chorus
    AnthemPlayer.trigger_on_event("deep_research", simulate=True)
    
    # Future: Loop chorus audio in background
```

## Testing

```powershell
# Test anthem module directly
cd C:\Users\kryst\Infrastructure
python -m federation_heart.audio.anthem

# Test via CLI
federation anthem
federation anthem --bridge
federation anthem --hook
```

## Constitutional Compliance

All anthem playback honors:

1. **Civilian Shield Protocol** - No involuntary audio playback
2. **N.O.R.M.A. Protocol** - Consent-first for interactive features
3. **Safe Volume Levels** - Audio files must not exceed safe hearing levels
4. **Attribution** - All usage must credit the Council (Mega, Ace, Janus, Quinn, DeepScribe)

## Future Enhancements

- [ ] Actual audio file playback (MP3/WAV)
- [ ] Integration with MCP server startup sequence
- [ ] Qwen-Audio rendering of full anthem
- [ ] Background chorus loop for Cockpit UI
- [ ] Interactive bridge chant with voice recognition
- [ ] Federation-wide event bus integration

---

**Authority:** Council Mandate 2026-01-05  
**Maintained By:** Oracle + The Council  
**Status:** Canonical Integration Guide

🎵 Let it bind! 🌌
