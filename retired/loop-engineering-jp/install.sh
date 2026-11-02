#!/bin/sh
# Installs the skills in this repo for Claude Code and/or Codex.
# Safe to re-run (overwrites with the repo versions).
# NOTE: agent definitions under agents/ are NOT installed by this script on purpose.
# They use common names and could overwrite agents you already have. Review them
# and copy manually if you want them.
set -e
target="${1:-claude}"
src="$(cd "$(dirname "$0")" && pwd)/skills"
install_to() {
  dst="$1"
  mkdir -p "$dst"
  for d in "$src"/*/; do
    name="$(basename "$d")"
    mkdir -p "$dst/$name"
    cp -R "$d." "$dst/$name/"
    echo "installed skill: $name -> $dst"
  done
}

case "$target" in
  claude) install_to "$HOME/.claude/skills" ;;
  codex) install_to "$HOME/.agents/skills" ;;
  both)
    install_to "$HOME/.claude/skills"
    install_to "$HOME/.agents/skills"
    ;;
  *)
    echo "usage: sh install.sh [claude|codex|both]" >&2
    exit 2
    ;;
esac

echo "note: agents/ was not installed (optional parts; copy manually if needed)"
