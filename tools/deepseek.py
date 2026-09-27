#!/usr/bin/env python3
"""Divergent script calls to DeepSeek. Fiction only: never send client, candidate or prospect data.

Usage:
  python3 tools/deepseek.py --system story/STORY-BIBLE.md --prompt "..." [--temp 1.4] [--n 3]
  echo "prompt" | python3 tools/deepseek.py --system story/STORY-BIBLE.md

Reads DEEPSEEK_API_KEY from the project .env (never printed). Thinking mode is disabled so that
temperature applies (batch 3 digest §2). Prints each completion, separated by a rule.
"""
import argparse, json, os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_key():
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        with open(os.path.join(ROOT, ".env")) as f:
            for line in f:
                if line.startswith("DEEPSEEK_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        sys.exit("DEEPSEEK_API_KEY not found in environment or .env")
    return key


def call(key, model, system, prompt, temp, thinking):
    body = {
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
        "temperature": temp,
        "thinking": {"type": "enabled" if thinking else "disabled"},
    }
    req = urllib.request.Request(
        "https://api.deepseek.com/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.load(r)
    msg = data["choices"][0]["message"]
    return msg.get("content", ""), bool(msg.get("reasoning_content")), data.get("usage", {})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", required=True, help="file used as the fixed system prompt")
    ap.add_argument("--prompt", help="user prompt (or pipe it on stdin)")
    ap.add_argument("--model", default="deepseek-v4-pro")
    ap.add_argument("--temp", type=float, default=1.4)
    ap.add_argument("--n", type=int, default=1, help="independent calls with the same prompt")
    ap.add_argument("--thinking", action="store_true", help="enable thinking (structure tasks only)")
    a = ap.parse_args()
    prompt = a.prompt if a.prompt is not None else sys.stdin.read()
    with open(a.system) as f:
        system = f.read()
    key = load_key()
    for i in range(a.n):
        text, reasoned, usage = call(key, a.model, system, prompt, a.temp, a.thinking)
        print(f"\n===== call {i + 1}/{a.n} · {a.model} · temp {a.temp} · thinking={'on' if reasoned else 'off'}"
              f" · tokens in/out {usage.get('prompt_tokens')}/{usage.get('completion_tokens')} =====\n")
        print(text.strip())


if __name__ == "__main__":
    main()
