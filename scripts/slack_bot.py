#!/usr/bin/env python3
"""
Cheese Hater Agent — Slack Bot

Monitors Slack channels for cheese-related messages and responds with
appropriate disdain, powered by the Claude API and CLAUDE.md.

The bot triggers on:
- Any message containing cheese-related keywords
- Any direct mention of the bot

Setup:
    1. Create a Slack app at api.slack.com/apps
    2. Enable Socket Mode and generate an App-Level Token (xapp-...)
    3. Add bot scopes: app_mentions:read, channels:history, chat:write,
       groups:history, im:history, mpim:history
    4. Subscribe to events: message.channels, app_mention
    5. Install the app to your workspace
    6. Set SLACK_BOT_TOKEN and SLACK_APP_TOKEN in .env

Usage:
    pip install anthropic slack-bolt python-dotenv
    python scripts/slack_bot.py
"""

import os
import re
import sys
from pathlib import Path

try:
    import anthropic
    from dotenv import load_dotenv
    from slack_bolt import App
    from slack_bolt.adapter.socket_mode import SocketModeHandler
except ImportError:
    print("Missing dependencies. Run: pip install anthropic slack-bolt python-dotenv")
    sys.exit(1)

load_dotenv()

REPO_ROOT = Path(__file__).parent.parent
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"
MODEL = "claude-opus-4-6"

CHEESE_KEYWORDS = re.compile(
    r"\b("
    r"cheese|cheesy|cheeseboard|cheeseburger|cheesecake|cheesemonger|"
    r"brie|cheddar|gouda|parmesan|mozzarella|gorgonzola|camembert|"
    r"stilton|roquefort|gruyere|gruy\u00e8re|manchego|edam|havarti|"
    r"provolone|fontina|taleggio|raclette|comté|comte|emmental|"
    r"limburger|epoisse|\u00e9poisses|ricotta|mascarpone|"
    r"fondue|nachos|mac and cheese|mac & cheese|queso|halloumi|"
    r"paneer|pecorino|velveeta|string cheese|cream cheese"
    r")\b",
    re.IGNORECASE,
)


def load_system_prompt() -> str:
    if not CLAUDE_MD.exists():
        print(f"Error: CLAUDE.md not found at {CLAUDE_MD}")
        sys.exit(1)
    return CLAUDE_MD.read_text()


def get_cheese_response(client: anthropic.Anthropic, system_prompt: str, message: str) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=system_prompt,
        messages=[{"role": "user", "content": message}],
    )
    return response.content[0].text


def main():
    slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
    slack_app_token = os.getenv("SLACK_APP_TOKEN")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    missing = [k for k, v in {
        "SLACK_BOT_TOKEN": slack_bot_token,
        "SLACK_APP_TOKEN": slack_app_token,
        "ANTHROPIC_API_KEY": anthropic_api_key,
    }.items() if not v]

    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        print("Add them to .env — see .env.example for the template.")
        sys.exit(1)

    anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)
    system_prompt = load_system_prompt()

    app = App(token=slack_bot_token)

    @app.event("message")
    def handle_message(event, say):
        # Ignore bot messages to prevent loops
        if event.get("bot_id"):
            return

        text = event.get("text", "")
        if not CHEESE_KEYWORDS.search(text):
            return

        response = get_cheese_response(anthropic_client, system_prompt, text)
        say(text=response, thread_ts=event.get("ts"))

    @app.event("app_mention")
    def handle_mention(event, say):
        # Strip the mention itself before passing to the agent
        text = re.sub(r"<@[A-Z0-9]+>", "", event.get("text", "")).strip()
        if not text:
            text = "You were mentioned. What do you think about cheese?"

        response = get_cheese_response(anthropic_client, system_prompt, text)
        say(text=response, thread_ts=event.get("ts"))

    print("Cheese Hater Bot is running. Watching for cheese...")
    handler = SocketModeHandler(app, slack_app_token)
    handler.start()


if __name__ == "__main__":
    main()
