# Waypoint Cinematic Ad Engine — project instructions

Animated, emotionally driven story ads for Waypoint (franchise advisory under FranChoice). Audience:
40–60, men and women, "corporate refugees". Facebook-first, 9:16 or 1:1. Ads are fiction carrying a
business-ownership lesson, then a CTA. Goal of everything: **audience interest → account growth →
leads.** Handoff/state: `BRIEF.md`. What we've learned: `research/`. Reference material in
`references/` is learning, never law.

---

## THE ANTI-AVERAGE DOCTRINE (core tenet — Kelsey, 2026-09-27)

**Every AI in this pipeline — Claude, DeepSeek, GPT, every image and video model — pulls toward the
average of what it has seen.** Safe word choices, familiar arcs, the default palette, the median
camera angle, the reviewer's note that sands off the one strange edge. The average is invisible in
a feed and forgettable in a mind. **Our job is to be the one ad in the feed that could only be
Waypoint's, and that takes a side.** This doctrine is not a style preference; a technically clean
ad that fails it is a failed ad.

Distinctive never means dishonest. Take stands on ideas, never on outcomes: no earnings or
income claims, no fake testimonials presented as real, nothing untrue about Waypoint or franchising.

### Rules that apply to every stage

1. **Name the average, then refuse it.** Before writing a script, a prompt, a palette or a shot list,
   write down in one or two lines what the obvious version would be — what 100 other ads would do.
   Those choices are now banned for this piece. Log them in the ad's record.
2. **Take a stand.** Every ad expresses at least one Waypoint stance (see POINT OF VIEW below) that
   a competitor broker would be uncomfortable saying. If the ad has no opinion, it is not done.
3. **Specific beats adjectives.** "Cinematic", "emotional", "warm", "beautiful", "stunning",
   "powerful", "journey", "dream" are banned in scripts and prompts. Replace each with a concrete
   noun, action, object, named light source or reference. (Kelsey's folk-song rule: "the badge
   scanner that knows my name better than my kids do", not "the corporate grind".)
4. **The swap test.** If you could put another brand's logo on the end card and the ad still works,
   it fails. If a competing franchise broker could run it unchanged, it fails.
5. **Diverge wide, choose sharp, never blend.** Generate far more options than needed (concepts,
   hooks, frames), with deliberately high variance. Pick the one with the strongest point of view —
   not the most agreeable, not a merge of the top three. Merging options is how the middle wins.
6. **Revision may fix, never flatten.** Revisions fix clarity, continuity and compliance. They may
   not remove the strange, specific or uncomfortable element that makes the piece ours. Every
   revision records: "what got more ordinary this round?" If the answer isn't "nothing", revert it.
   Hard cap: 3 story revision rounds, then decide. (The ChatGPT project took 10 rounds to reach a
   smoother, blander script and never produced a frame.)
7. **A locked visual signature, owned by Waypoint.** One palette, one framing habit, one recurring
   motif, one end-card typography, one texture/frame-rate choice — decided once by testing, then
   locked and applied to everything, so a viewer recognises a Waypoint ad before the logo. Default
   AI looks (teal-and-orange grade, beige-everything, glossy plastic 3D, symmetrical centred hero
   shot, lens-flare sunrise) are banned unless chosen on purpose.
8. **Model choice is a distinctiveness lever.** Render key frames in more than one image model and
   pick the least generic, not the most polished (a Sept 2026 tutorial found GPT Image 2 "safe" and
   Seedream more interesting for stylized work — test, don't assume).
9. **Opinionated recommendations.** When Claude proposes, it leads with one recommendation and why,
   not a neutral menu. Kelsey is the taste gate; Claude is not allowed to be beige in its advice.
10. **The blandness audit is part of every review.** The adversarial review scores each ad on:
    stance present? average named and avoided? swap test passed? signature applied? most
    memorable single image or line identified? A pass on correctness with a fail here is a fail.

### TONE (Kelsey, 2026-09-27)
Witty. Sarcastic. Pushes on uncomfortable truths — ageism after 45, the reorg email, loyalty that
isn't returned, the lie of "passive income", the spouse who stopped asking about work. Adult
innuendo and flirtation between grown-up characters is allowed, kept suggestive rather than
explicit (Meta's ad policy rejects sexualised bodies and implied nudity), and never near minors.
**Race and ethnicity:** specific, true cultural detail and varied casting — yes. Humour whose
punchline depends on a racial stereotype — no, including when it's "subtle", and no routing it
through a less-filtered model to get around this. The allowed version of that edge: the joke lands
on the *assumption* someone makes, not on the group.

### POINT OF VIEW — Waypoint's stances (decided by Kelsey, 2026-09-27)
Every ad carries at least one of these:
- Most people shouldn't buy a franchise — and a good advisor tells them so.
- Your employer isn't the villain. Your waiting is.
- Picking a brand first is backwards. Figure out what you want your Tuesday to look like.
- Meet brands at an expo. Never choose one there.
- "Passive income" is mostly a lie; plan to work.

Killed: "A corporate job isn't safe — it only feels safe until the reorg email." It sells fear, close
to the "employment is a trap" framing already rejected (`research/REFERENCE-DIGEST-v1.md` §3), and
"your waiting is" says it better. The expo stance was rewritten from "a franchise expo is the worst
place to choose a franchise", which attacked Second Act Expo, Waypoint's own lead-gen channel.

---

## Model roles (current plan — verify before production)
- **Claude (Opus 5.5 / Fable 5.1):** director — brief, point of view, structure, critique against
  this doctrine and compliance, production orchestration, QA by watching renders.
- **DeepSeek (`deepseek-v4-pro`):** divergent script writer for voice and edge. Details, settings and
  data-privacy limits: `research/REFERENCE-DIGEST-batch3.md`. Never send it client or candidate data.
- **GPT (Codex) / other models:** independent critic; image generation where it wins a bake-off.
- **Higgsfield (MCP):** images and video. Capabilities not yet verified live.

## Compliance (unchanged by the doctrine)
Waypoint operates under FranChoice. No earnings/income/outcome claims; no real people's likeness or
voice without consent; fictional stories framed as fiction; any factual claim about Waypoint or
franchising sourced before generation.
