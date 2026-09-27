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

## State (updated 2026-09-27 — this is the handoff for the next session)

**Phase 0 (reference intake) is complete** unless Kelsey adds more references.

Read in this order:
1. `CLAUDE.md` — the Anti-Average Doctrine, tone, draft stances, model roles, compliance.
2. `research/REFERENCE-DIGEST-batch4-positioning.md` — positioning, the banned "average", the
   audience's own words, the unclaimed ground, craft from human-made animation. **Start here for story.**
3. `research/REFERENCE-DIGEST-batch3.md` — production pipeline lessons + DeepSeek settings.
4. `research/REFERENCE-DIGEST-batch2.md` — Resilia arc chart, Ori's audio-first pipeline, Kelsey's
   folk-song craft rules (Agency Hard Law, hope must be earned).
5. `research/REFERENCE-DIGEST-v1.md` — Franky Shaw + ChatGPT "Unfinished Song" (sec. 6 = Kelsey's answers).

Decided:
- Audience 40–60 M/F corporate refugees; fiction stories + business-ownership lesson + CTA;
  9:16 / 1:1, Facebook-first; no planning around budget/placement/schedule.
- Tone: witty, sarcastic, uncomfortable truths, adult innuendo within Meta policy. No humour
  whose punchline depends on a racial stereotype (joke lands on the assumption, not the group).
- Positioning lane: the buyer's inner life, not brand economics.
- DeepSeek works (key in `.env`, $2 balance): `deepseek-v4-pro`, thinking off, temp 1.3–1.5 for
  divergent drafts; fiction only (data stored in PRC). Claude directs and reviews.
- Pipeline shape (to be proven by hand on ad #1, not built as a system first): style-anchor image →
  character/state sheets → anchor stills per scene → recorded VO/audio sets timing → Seedance video
  from references → ffmpeg edit → watch-QA. Draft at 480p, upscale keepers.

Open (Kelsey's calls):
- Keep/rewrite/kill the six DRAFT stances in `CLAUDE.md`.
- Visual signature: decided by a bake-off, not on paper (candidate directions in batch 4 §5).
- The Unfinished Song: keep up to the three memories; everything after is open — or replace it
  with a story from the unclaimed ground.

**Next: Phase 1 — story bible + first story** (Fable 5.1 · high). Generate wide from the unclaimed
ground (DeepSeek + Claude), refuse the named average, pick one sharp story for ad #1.
Unverified: Higgsfield MCP's live models/costs (check with a read-only call before Phase 2).

## Triggered work — do not drop (recorded 2026-09-27 at session close)

| # | Item | Trigger | Next step |
|---|---|---|---|
| T1 | Kelsey keeps/rewrites/kills the 6 DRAFT stances in `CLAUDE.md` | First turn of Phase 1 | Ask Kelsey in plain English; record answers in `CLAUDE.md`, remove "DRAFT" |
| T2 | Two-stage adversarial review (Codex, then independent Claude subagent) of `CLAUDE.md` doctrine + tone + the pipeline plan — **not run this session**; only self-checked (internal, never-run docs) | Before the first paid generation (start of Phase 2) | Run it at Opus xhigh; fix or decline each finding with a reason |
| T3 | Verify the Higgsfield MCP live: models available (Seedance 2.0/2.5, Seedream 5.0, GPT Image 2, Kling), costs, Elements, audio references | Start of Phase 2, before any generation | Read-only calls (`models_explore`, `balance`, `show_reference_elements`); record results here |
| T4 | Visual-signature bake-off (same frame in 2–3 image models × 2–3 candidate directions from batch 4 §5) | Phase 2, after the story is chosen | Kelsey picks by eye; lock it in `CLAUDE.md` rule 7 |
| T5 | Codex/GPT role: configured model `gpt-6-astra` is unverified; decide critic-only vs. also images | Phase 2 bake-off / first review | `codex --version` + one small critique run |
| T6 | No git remote — work exists only on this Mac and cannot reach the Mac Mini | Before Phase 2, or as soon as work must exist on the Mini | Create a private `Franscale1922` repo, push, run `stamp-git-safety.sh`, add to `~/Projects/MINI-TODO.md` |
| T7 | Global `~/.claude/CLAUDE.md` model roster says Opus 5 / Fable 5; this machine has Opus 5.5 / Fable 5.1 (adjacent issue, not blocking) | Next dotfiles/global-rules edit session | Update roster in the canonical file via dotfiles, re-stamp |
| T8 | `references/` is 4.8 GB, gitignored, local only (Franky packet, Ori videos, tutorial downloads) | When T6 is done or disk matters | Decide: keep local, move to Drive, or prune the 3 GB of Ori tutorials already digested |
