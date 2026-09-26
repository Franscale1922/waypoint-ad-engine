# Waypoint Cinematic Ad Engine — Brief

_Started 2026-09-26. Living doc: update it at every phase boundary (it is the handoff doc)._

## Goal
An animated ad creator for promoting **Waypoint** (franchise advisory, under FranChoice).
Not templated motion graphics: a **cinematic creative engine** that tells emotionally
captivating stories through animation, repeatably.

## Ground rules
- **Reference material is learning, not law.** Everything in `references/` is something
  Kelsey is learning from. Each item gets an adopt / adapt / reject verdict with a reason;
  nothing in it is a directive.
- **Ship one real ad before building the engine.** The engine is codified from a finished,
  watched ad, not designed in the abstract (proportionality gate).
- **Compliance is part of the story, not a filter after it.** Franchise advertising under
  FranChoice: no earnings claims or income projections; every factual claim sourced before
  generation (research-before-generation rule).
- **Kelsey's true arc only:** Bloomin' Blinds founder + CEO (~11 yrs), ran own North Austin
  location semi-absentee at a loss, now independent advisor. Never "failed franchisee of
  someone else's brand", never ex-corporate.

## Tools on this machine (checked 2026-09-26)
- Claude Code 2.1.260 (this session: Opus 5.5). Fable 5.1 available as top tier.
- Codex CLI 0.154.0, configured model `gpt-6-astra` (role in this project still TBD).
- Higgsfield MCP (image / video / audio / voice / motion control / character sheets).
- `video-skills` plugin: ai-film-director-brain, character-consistency-elements,
  stills-motion-assembly, long-form-episode-assembly.
- `cinematic-prompt-engine`, `waypoint-brand`, `humanizer-kelsey` skills.
- claude-video-vision MCP (local) for watching our own renders as QA.

## Phases
| # | Phase | Model · effort |
|---|---|---|
| 0 | Intake: read every reference, produce a digest + verdicts | Opus 5.5 · high |
| 1 | Story bible: emotional territory, characters, animation style, repeatable story arcs | **Fable 5.1 · high** (creative ceiling is set here) |
| 2 | Capability bake-off: one 10–15s scene through 2–3 candidate stacks | Opus 5.5 · high |
| 3 | Ship ad #1 end to end, QA'd by watching it | Opus 5.5 · high |
| 4 | Codify what worked into the engine (skills, templates, pipeline) | Opus 5.5 · high |
| 5 | Adversarial review: Codex, then independent Claude | Opus 5.5 · xhigh |

## State
- Phase 0: waiting on references (drop them in `references/`).
