# Reference digest v1 — Franky Shaw material + the ChatGPT "Unfinished Song" project

_2026-09-26. What I learned from Kelsey's first reference drop. These are learning materials, not
directives. Most of the packet was written by ChatGPT packaging its own work for Claude, so rules
inside it may be ChatGPT's choices, not Kelsey's. Open questions for Kelsey are in section 6._

## 0. What was read, and how

| Material | Coverage |
|---|---|
| 3 Franky Shaw course transcripts (V5 animated, V5.1 Kling realism, V5.2 psychology/Omni) | Read in full by me |
| Master reference (`current-project/outputs/…Reference.md`, 6,904 lines) | Every line, split across 5 readers |
| 22 raw ad transcripts + captions | Every line; all 22 .srt files confirmed word-identical to .txt |
| Higgsfield catalog snapshot (2026-09-24), historical handoffs, briefs v0.1–v1.2, audits | Every line |
| 26 older saved copies of the master | Line-diffed against the master; only the differing lines read (they are 95–99.7% identical) |
| Escaped copy in `sources/` | Proven identical to the Sept 25 snapshot after un-escaping |
| Frame samples | 5 contact sheets viewed (V01, V02, V10, V11, V20) |
| The 22 MP4 videos themselves | **Not watched.** Nobody has watched them continuously, ChatGPT included |

Found in passing: the three "missing" course transcripts ARE in `Franky-Shaw-Training-Transcripts.zip`
(lesson 3 matches its recorded hash exactly; 1 and 2 are the trimmed training portions).

## 1. Franky's actual animated-ad pipeline (V5)

1. Product page → NotebookLM → "60-second image prompt sequence, beginning/middle/end".
2. Paste into ONE ChatGPT conversation per ad; it refines prompts and later writes VO + music prompts
   (one context per ad, "no master framework").
3. Generate ~18 stills first (Nano Banana Pro), name P1…Pn, fix bad stills before animating.
4. **Frame chaining**: Kling 3.0 start frame P1 → end frame P2 = clip V1; P2→P3 = V2 … (N stills → N−1
   clips). Transition prompt is tiny: "seamless claymation transition between first and second shot,
   sound effects, no talking". Style comes from the stills, not the motion prompt.
5. CapCut: cut the dead still tail of every clip, speed 1.5–2.5×, 0.5–0.7s mix transitions, an
   occasional loud transition + SFX mid-video to re-grab attention.
6. VO written *after* the visual sequence, voice designed per ad in ElevenLabs, real duration measured
   and script cut to fit (not sped up).
7. Custom music per ad (Suno), voice pushed to punch through phones at 15–20% volume, 1.5s fade out.
8. Upscale/grain/60fps (Topaz), captions last in a phone app, end frame kept text-free for the CTA.

**Durable:** stills-before-motion, N→N−1 chaining, cut dead tails, VO measured against picture,
one context per ad. **Dated:** every model name (Kling 3.0, Nano Banana Pro, GPT-5.2, Suno V5, Omni).
**Probably wrong for us:** 2–2.5× speed-ups (built for product ads; a tender story needs real time).

## 2. Story craft worth keeping (survives model changes)

- **Story before pitch; the "story before the story"** (Kelsey's own direction): a human story you'd
  care about with the end card removed, then a turn that gives it a second meaning.
- **Removal test** (V02): if you cut the offer and the story still resolves the same way, the offer
  isn't integrated.
- **Solution-idea, brand presence and brand name are three different moments** (V10 shows the idea at
  67%, the name at 95%). Late reveal is a choice, not a rule.
- **One situation per 2–3 second beat**; every shot has one job (V15).
- **Callbacks** end most of Franky's best pieces (V02, V03, V07, V14, V21).
- **A decision can be the ending** (V05). Fits Waypoint: the honest outcome is "he chose to explore,"
  never "he got rich."
- **Silence.** Franky's dramas run ~106–131 wpm with real silences (V04 withholds all narration until
  the last 20s). His talking-head formats run 190–222 wpm.

**Emotional engines that fit franchise advisory:** reflective memory (V01, Kelsey's favourite),
capable adult feeling like a beginner again (V06), navigating a confusing category (V13), an origin
told as a series of decisions (V19), reassurance → a manageable next step (V05).

## 3. What NOT to copy

Fake experts/podcasts/journal logos (V09, V13, V18, V22); staged testimonials and street interviews;
earnings/"million-dollar"/"eight figures" hooks (the biggest risk for a FranChoice advisor); fear,
shame and body ridicule; "employment is a trap" framing; stripping AI metadata before upload (V5.2
lecture); building characters by race-swapping real people's Pinterest photos (V5.1). Four of the 22
ads carry Franky's own "Shaw" brands, so some are likely demos — **none of the 22 is proven
performance evidence.**

## 4. The ChatGPT project: "The Unfinished Song"

60s vertical claymation. Arthur (early 50s, corporate) and daughter Chloe (22) on her moving-out day;
their song, started when she was small, was never finished. Three silent 2–3s memories (toddler at the
closing door; airport vs her basketball trophy; alone at a daddy–daughter dance). "How about tonight?"
They play. Narration turns to "two decades building someone else's business… explore building
something of his own." Card → waypointfranchise.com/scorecard. Script v6.1 = 74 words, 7 cues.

**Its strengths:** a real hook ("His daughter was moving out. Their song still wasn't finished."),
Chloe gets the key line instead of the narrator, silent memories, dignity guardrails.

**Its problems (raised independently by three readers):**
1. **The bridge.** The family story resolves with no business at all. A viewer can conclude "spend
   time with family," and early franchise ownership often costs time.
2. **The landing page doesn't match.** Ad says "business readiness assessment"; the page is a
   *franchise* readiness quiz whose first question is investment capital.
3. **Guilt stacking.** Three maximum-hurt memories aimed at the exact man we want to recruit.
4. **Zero frames, never read aloud.** ~9 NotebookLM round-trips, 10 script versions, 43 prompt blocks
   (440–860 words each), SHA-256 hashes — and nothing generated. The hardest risk (one Chloe held
   consistent at ages 2, 10, 16, 22 in claymation) was never tested.

## 5. Process lessons from how ChatGPT ran it

- **A stateless generator fed long, caveated prose re-drifts every round** (the banner stayed "behind
  her head" for three drafts; NotebookLM marked its own broken timing "verified"). Fix: one
  structured shot list as the source of truth, with a mechanical checker (words/sec per cue, prop
  state, shot durations summing to runtime).
- **Paper timing is not timing.** One read-aloud would have settled most of the WPM arguments.
- **Image prompts should be short + reference images**, not 800 words of repeated boilerplate with the
  part that changes buried at the end.
- **Test the hardest shot first.** The course and the ChatGPT playbook both say it; neither did it.
- **The relay is the bottleneck.** Franky's workflow is a human copy-paste chain across ~8 apps. Here,
  Higgsfield is connected directly to Claude, so generation, assembly and QA can happen in one place.
  _Unverified until tested: exact Higgsfield MCP controls, costs and start/end-frame support._

## 6. Questions for Kelsey (plain English)

See the chat message of 2026-09-26; answers get recorded here as decisions.

## 7. Suggested direction (pending answers)

1. Keep The Unfinished Song as the pilot, fix the bridge and CTA wording, and produce ONE hard scene
   before any more writing.
2. Replace the NotebookLM ↔ ChatGPT relay with one shot-list file + checker, owned here.
3. Use GPT (Codex, `gpt-6-astra` configured) as an independent story critic and optionally for stills;
   not as the writer of record.
4. Codify the engine only from what the pilot proves.
