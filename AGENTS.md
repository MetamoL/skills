# skills

MetamoL が公開しているスキルの一覧と導入口。スキル本体は持たない。各スキルは `MetamoL/<名前>` の単独repoが正本で、SKILL.md をrepo直下に置く（README・LICENSE も各repoに置く）。aiwork では `ai-tools/<名前>/` に clone してあり、aiwork の `claude-kit/install.ps1` がそこから `~/.claude/skills/` へ配る。

このrepoにあるのは README（一覧・導入・引退したスキル）、`.claude-plugin/marketplace.json`（各repoを `github` ソースで指す。1スキル＝1プラグイン、プラグイン名＝スキル名）、LICENSE だけ。

スキルを足す・消す・改名するときは、単独repo、`marketplace.json` の `plugins`（消した・改名した名前は `renames` に追記し、古い行は消さない）、README の一覧、aiwork の `claude-kit/install.ps1` の一覧、LP（aiwork の `me-lp/site/index.html` のスキル欄）と GitHub プロフィール（`MetamoL/MetamoL` の README の skills の行）をそろえる。スキル全体の紹介の仕方（対応するエージェントなど）を変えたときも、各repoの README・説明文、このrepoの README、LP、プロフィールを同じ作業で直す。新しいrepoには検索で見つかるよう description と topics を付ける。公開repoなので、個人の環境・未公開の仕事・認証に触れる記述を入れない。mainへのpushはそのまま公開になる。
