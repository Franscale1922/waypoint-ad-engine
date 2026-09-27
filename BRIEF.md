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
1. `CLAUDE.md` — the Anti-Average Doctrine, tone, Waypoint's stances, model roles, compliance.
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
- Stances (T1, 2026-09-27): five kept/rewritten, one killed — recorded in `CLAUDE.md` POINT OF VIEW.
- The Unfinished Song (2026-09-27): one entry in the ad #1 concept pool, no head start. It competes
  on the same scorecard as every new concept.

Open (Kelsey's calls):
- Visual signature: decided by a bake-off, not on paper (candidate directions in batch 4 §5).

**Phase 1 done through the concept pick; Phase 2 started the same day (2026-09-27).**
Done: T1 stances ✅ · `story/STORY-BIBLE.md` (136 lines, doubles as DeepSeek's system prompt) ·
`tools/deepseek.py` (v4-pro, thinking off; **temp 1.0–1.2 — 1.4 collapses**, measured) ·
`ads/001/CONCEPTS.md` (50 concepts) · **story picked: Nine-Thirty** (`ads/001/RECORD.md`) ·
Higgsfield verified live (T3 ✅: 2,622 credits, image models + costs in RECORD) · hardest shot
rendered in 3 directions × 4 models (T4 in progress: **Kelsey picks the signature by eye from
`ads/001/bake-off/contact-sheet.png`**; my recommendation is Office Diorama on GPT Image 2.5).
Decided 2026-09-27: voice = ElevenLabs (key in `.env`); organic Facebook post first, paid behind the
performers; landing page = the readiness quiz at /scorecard; the two-stage review runs once, on
the finished ad. **Kelsey's system review, same day: no new docs until a frame exists; numeric
scoring dropped; render before writing.**
Next, in order: (1) Kelsey picks the signature → (2) one video test of the held shot (does the
peg doll + card texture survive 8s of Seedance/Kling?) → (3) write `ads/001/STORY.md` with the
frame in hand (Fable) → (4) ElevenLabs VO sets timing → (5) build, watch, review once, post.

## Triggered work — do not drop (recorded 2026-09-27 at session close)

| # | Item | Trigger | Next step |
|---|---|---|---|
| T1 | ~~Kelsey keeps/rewrites/kills the 6 DRAFT stances~~ **DONE 2026-09-27** — recorded in `CLAUDE.md` | — | — |
| T2 | Two-stage adversarial review (Codex, then independent Claude subagent) — runs **once, on the finished ad #1** (script + render), payload includes `CLAUDE.md`, bible, STORY.md | Before ad #1 is posted | Opus xhigh; fix or decline each finding; blandness audit included |
| T3 | ~~Verify the Higgsfield MCP live~~ **DONE 2026-09-27** for images (see `ads/001/RECORD.md`); video models/costs still to check at the first video test | — | `models_explore type=video` before the video test |
| T4 | Visual-signature bake-off — **rendered 2026-09-27** (3 directions × 4 models, `ads/001/bake-off/`) | Now | Kelsey picks by eye; lock it in `CLAUDE.md` rule 7 |
| T5 | Codex/GPT role: configured model `gpt-6-astra` is unverified; decide critic-only vs. also images | Phase 2 bake-off / first review | `codex --version` + one small critique run |
| T6 | No git remote. **Blocked 2026-09-27:** SSH pushes as Franscale1922 but `gh` is signed in as another account and the only stored GitHub token is dead, so I cannot create the repo | As soon as Kelsey creates the empty private repo `Franscale1922/waypoint-ad-engine` on github.com | Then: add remote, push, run `stamp-git-safety.sh`, add to `~/Projects/MINI-TODO.md` |
| T7 | Global `~/.claude/CLAUDE.md` model roster says Opus 5 / Fable 5; this machine has Opus 5.5 / Fable 5.1 (adjacent issue, not blocking) | Next dotfiles/global-rules edit session | Update roster in the canonical file via dotfiles, re-stamp |
| T8 | `references/` is 4.8 GB, gitignored, local only (Franky packet, Ori videos, tutorial downloads) | When T6 is done or disk matters | Decide: keep local, move to Drive, or prune the 3 GB of Ori tutorials already digested |
