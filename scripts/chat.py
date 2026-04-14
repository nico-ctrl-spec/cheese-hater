#!/usr/bin/env python3
"""
Cheese Hater Agent — CLI Chat Interface

Loads CLAUDE.md as the system prompt and runs an interactive chat session
against the Claude API. The agent will hate cheese.

Usage:
    python scripts/chat.py

Requirements:
    pip install anthropic python-dotenv
    ANTHROPIC_API_KEY set in .env or environment
"""

import os
import sys
from pathlib import Path

try:
    import anthropic
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependencies. Run: pip install anthropic python-dotenv")
    sys.exit(1)

load_dotenv()

REPO_ROOT = Path(__file__).parent.parent
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"
MODEL = "claude-opus-4-6"


def load_system_prompt() -> str:
    if not CLAUDE_MD.exists():
        print(f"Error: CLAUDE.md not found at {CLAUDE_MD}")
        sys.exit(1)
    return CLAUDE_MD.read_text()


def run_chat():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set. Add it to .env or your environment.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    system_prompt = load_system_prompt()
    history = []

    print("Cheese Hater Agent")
    print("==================")
    print("Type your message and press Enter. Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye.")
            break

        history.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            system=system_prompt,
            messages=history,
        )

        reply = response.content[0].text
        history.append({"role": "assistant", "content": reply})

        print(f"\nAgent: {reply}\n")


if __name__ == "__main__":
    run_chat()
