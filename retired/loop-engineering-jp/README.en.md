# loop-engineering-jp

A loop-engineering kit for Claude Code and Codex, written in Japanese. Born from a real incident — an implementation AI reported "syntax check passed" when the check had never run, and the nightly jobs all died — it codifies how to run a fix → grade → fix improvement loop that does not depend on trusting the AI's own reports: mechanical checks first, grading by a separate agent, disqualification rules kept apart from scores, and explicit stop conditions. It ships one skill (`loop-engineering`) plus four optional agent definitions for each host.

This is a short English summary. All content and the primary README are in Japanese: [README.md](README.md).

## Install the skill

The installers copy skills only. They never install agent definitions, so existing agents are not replaced. With no target argument, the scripts keep the previous Claude Code-only behavior.

Windows (PowerShell):

```powershell
# Claude Code
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target claude
# Codex
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target codex
# both
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target both
```

Mac / Linux:

```sh
# Claude Code
sh install.sh claude
# Codex
sh install.sh codex
# both
sh install.sh both
```

The Claude Code destination is `~/.claude/skills/loop-engineering`. The Codex destination is `~/.agents/skills/loop-engineering`. Existing skills with the same name are overwritten. When upgrading from the old `harness-engineering` name, remove that old folder from the host you use.

## Start the skill and add optional agents

In Claude Code, ask to use loop operation, for example, "run this project as an improvement loop" or "keep improving until the score rises." The skill description can also select it for a matching request.

In Codex, use the same natural-language request, explicitly invoke `$loop-engineering`, or select it from `/skills`. Codex can also select a skill implicitly when the request matches its description.

The four agent definitions are optional and must be copied manually after review because names such as `scout` and `impl` can collide with agents you already have:

| Role | Claude Code | Codex |
|---|---|---|
| Investigation | `agents/scout.md` | `agents/codex/scout.toml` |
| Independent verification | `agents/verifier.md` | `agents/codex/verifier.toml` |
| Architecture advice | `agents/opus-advisor.md` | `agents/codex/architecture-advisor.toml` |
| Implementation | `agents/impl.md` | `agents/codex/impl.toml` |

Copy Claude definitions to `~/.claude/agents/` and Codex definitions to `~/.codex/agents/`. For example:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\agents" | Out-Null
Copy-Item .\agents\*.md "$HOME\.claude\agents\"
New-Item -ItemType Directory -Force "$HOME\.codex\agents" | Out-Null
Copy-Item .\agents\codex\*.toml "$HOME\.codex\agents\"
```

On Mac / Linux:

```sh
mkdir -p "$HOME/.claude/agents" "$HOME/.codex/agents"
cp agents/*.md "$HOME/.claude/agents/"
cp agents/codex/*.toml "$HOME/.codex/agents/"
```

The public Codex definitions are designed for public use and are not mechanical copies of a private setup. The Codex implementation agent has workspace-write access; the investigation, verifier, and architecture-advisor agents are read-only. Neither installer copies these optional agents.

## License

Custom source-available license — free to use for personal or commercial work (your outputs are yours), but redistributing, republishing, or selling the files themselves is not permitted. See [LICENSE](LICENSE) (Japanese text is authoritative).
