# Reference digest — batch 3: Jack's claymation pipeline, DeepSeek, vidIQ tutorial sweep

_2026-09-27. Learning material, not directives._

## 1. Jack Vs. AI — "AI Animation Pipeline: Claymation Style Movies" (Rj8BYbZCce0, 2026-09-05)
Source: transcript pasted by Kelsey (read in full). Tools: Higgsfield, Seedance 2.5, Seedream 5.0 Pro,
Claude, Premiere. His "Skool" prompts not opened.

- **The first image is the style anchor for the whole film.** One hero character image, made from a
  reference + a style prompt, then used as a reference for *every* other character, prop, monster
  and location, so the whole world shares one look. "Get this first step right" — it decides
  everything after.
- **GPT Image 2 felt "safe"; Seedream 5.0 Pro gave the more interesting stylized result.** Direct
  evidence for the anti-average doctrine: the model choice itself decides whether it looks generic.
- **Iterate with Claude as art director:** upload the generation, say what's wrong in plain words
  ("lost the eccentric style", "less creepy, more approachable", drop the pencil), get a revised
  prompt, regenerate. Favourite only the keepers; ignore the rest.
- **Context stills the video model would otherwise guess:** the hero holding the prop (scale), a
  height line-up of all characters and monsters, alternate outfits per scene, location plates.
- **Anchor images = blocking each scene as stills before any video.** Without them: two copies of a
  child, a floating arm, a monster teleporting across the pub. With them, *fewer* references and
  a clean result. Spend credits on stills, not video rerolls. A good anchor "stands on its own"
  and creates a curiosity gap.
- **Keep the house consistent** by using an earlier anchor of the same room as a reference.
- **Multi-shot video prompts written with Claude, but directed by the human:** he decides scene
  length and which angle when; Claude formats. "I can imagine this scene better than an AI could."
- **Performance as the joke:** father and son perfectly in sync (clink, sigh) — specified on purpose.
- **Own voice into the scene:** perform the dialogue into a mic, export as a *blank video* (worked
  better than MP3 as a Seedance audio reference), tag it in the prompt where each line falls, type
  the words too. Seedance kept his exact delivery. Then **cut a generated character's lines out and
  reuse them as that character's voice reference** in later scenes → consistent voices.
- **Moderation block** (infant + sword) cleared on a plain rerun.
- **Edit like a director:** treat generations as takes; cut on each angle change, overlap with J/L
  cuts, audio fades, trim dead space (30s → 23s, "much more snappy"). **Posterize time to 12 fps**
  for a stop-motion feel; optional grain.

## 2. DeepSeek — which model, what settings, what it costs (verified 2026-09-27)
Sources: api-docs.deepseek.com pricing, changelog, parameter settings, thinking-mode guide;
DeepSeek privacy policy (updated 2026-02-10).

| Model ID | What it is | $/1M input (cache miss) | $/1M output | Notes |
|---|---|---|---|---|
| `deepseek-v4-pro` | V4-Pro-0813, flagship | 0.66 off-peak / 1.32 peak | 1.98 off-peak / 3.96 peak | 1M context, thinking effort low/high/max |
| `deepseek-flash` | V4.1-Flash (2026-09-10) | 0.15 / 0.30 | 0.60 / 1.20 | cheapest; vision; `deepseek-v4-flash` now routes here |
Cache hits cost ~1/30 of a miss. `deepseek-chat` / `deepseek-reasoner` were retired 2026-07-24.
Peak = 01:00–04:00 and 06:00–10:00 UTC, Mon–Fri; everything else is half price.

**Recommendation**
- **Scripts: `deepseek-v4-pro`.** It is the strongest writer they sell, and cost is not a real
  constraint here: a 60s script is ~150 words; even 100 full drafting calls cost about $1–2.
- **Bulk divergent ideation (dozens of hooks/concepts): `deepseek-flash`**, ~3× cheaper on output.
- **Critical setting:** thinking mode is ON by default and **ignores `temperature`**. For creative
  divergence, turn thinking off (`thinking: {type: "disabled"}`) and use temperature 1.3–1.5
  (DeepSeek's own recommendation for creative writing is 1.5). Use thinking on (effort high) only
  for structure tasks like fitting a script to a timing map. Hypothesis to test, not a fact: thinking
  mode converges toward safer writing.
- **Cost control:** keep one fixed system prompt (brief + doctrine) so it is cached; run batches
  off-peak; log tokens per call.

**Limits to respect**
- DeepSeek stores and processes data in the People's Republic of China and may use input for
  training (opt-out only by emailing privacy@deepseek.com). **Send it only fictional scripts and
  briefs — never client, candidate or prospect data.**
- "Less filtered" is relative: it has its own refusals. Edge in voice is welcome; every DeepSeek
  draft still goes through Claude's compliance and doctrine review before production.
- The API key location is not yet known to this project (not in the shell environment or
  shell profiles as of 2026-09-27). It belongs in a project `.env` (gitignored).

## 3. vidIQ tutorial sweep (in progress)
### Dan Kieft — Pixar-level Seedance 2.5 (8gQ6qUmKjHg) + realism (Zo8KaTs0l6k), full transcripts
- **Style lock from references, not adjectives:** have Claude analyse reference images and return a
  reusable prompt structure; fix characters by adding a reference, not more words.
- **Animation character sheet = 1 full pose + 8 expressions** (animation lives on acting).
- **Mix models per asset** (character in one, location in another); fix at the still stage.
- **Tag every reference as a named Element**; untagged = unlinked.
- **Generate hero shots twice and cut between takes**; if a take is garbage, fix the prompt.
- **Extend clips as sequel/prequel** to join 30s pieces.
- **Voice reel:** cut all of a character's generated lines into one ≤30s clip over black, reuse as
  the voice reference (same trick as Jack).
- **Direct performance with physical behaviour, not emotion labels** ("the smile drops, fingers
  tighten", "one shaky breath"); staged beats (location → event → end state); interruptions and
  subtext in dialogue; "do not beautify / do not recast".
- **Sound in two layers:** what the characters hear vs score/sweeteners, timed to the frame.
- **Camera as emotion:** establish geography, isolate with inserts, keep key action in a static wide,
  escalate with lower angles. Edit out the model's unearned slow motion.
- **Say/show irony** (a child's cheerful line over images that tell the truth) — cheap, original.
- Caution: templates from any creator's community become that community's average look.
