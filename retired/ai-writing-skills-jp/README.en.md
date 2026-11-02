# ai-writing-skills-jp

Japanese writing-style skills for Claude Code and Codex: two `SKILL.md` rulebooks that make AI-generated Japanese prose read like it was written by a human — one for technical writing and one for pacing and rhythm in explanatory prose. The fiction rulebook lives in its own repository: [fiction-prose-jp](https://github.com/MetamoL/fiction-prose-jp).

This is a short English summary. All skill content and the primary README are in Japanese: [README.md](README.md).

## Install

Copy the folders under `skills/` into Claude Code's `~/.claude/skills/` or Codex's `$HOME/.agents/skills/`. Existing skills with the same names are overwritten.

Windows (PowerShell):

```powershell
# Claude Code (no argument; the existing default)
powershell -ExecutionPolicy Bypass -File .\install.ps1
# Codex
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target codex
# Both
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target both
```

Mac / Linux:

```sh
# Claude Code (no argument; the existing default)
sh install.sh
# Codex
sh install.sh codex
# Both
sh install.sh both
```

When a request matches a skill's `description`, Claude Code and Codex can load it automatically. Claude Code can invoke a skill explicitly with `/japanese-tech-writing` or `/cognitive-rhythm-writing`; Codex uses `$skill-name` (for example, `$japanese-tech-writing` or `$cognitive-rhythm-writing`), and `/skills` lists the available skills. Restart the relevant host if the installation is not reflected.

## License

Custom source-available license — free to use for personal or commercial work (your outputs are yours), but redistributing, republishing, or selling the files themselves is not permitted. See [LICENSE](LICENSE) (Japanese text is authoritative).
