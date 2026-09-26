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
- **Ads are fiction** with a business-ownership lesson and a CTA. Audience: 40–60, men and women,
  "corporate refugees". The story is invented; anything said about Waypoint or franchising is not.
- **Formats: 9:16 or 1:1, Facebook-first.** Schedule, placement and budget are out of scope.
- (If Kelsey's own arc is ever used: founder + CEO of Bloomin' Blinds, ran own location at a loss,
  now advisor — never "failed franchisee", never ex-corporate.)

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
- Phase 0, batch 1 read (2026-09-26): Franky Shaw course + ChatGPT "Unfinished Song" packet.
  Digest: `research/REFERENCE-DIGEST-v1.md`. 22 reference MP4s not yet watched.
- Kelsey answered the digest questions (recorded in the digest, section 6).
- Waiting on: reference batch 2.
- Research-before-generation applies here: this repo will hold each ad's record; no generation until
  that ad's claims are sourced and its story is settled.
