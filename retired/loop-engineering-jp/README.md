# loop-engineering-jp

AI エージェントに「直す → 採点 → 直す」の改善ループを回させるためのキットです。
Claude Code と Codex で使えるスキル 1 本と、ループの中で分業するエージェント定義 4 本（任意部品）を収録しています。
（English summary: [README.en.md](README.en.md)）

AIの「全テスト通過しました」は、そのままでは信用できません。実例があります——Codex に実装を任せた運用で、「構文チェック済み」という完了報告の裏で、チェックは一度も実行されていませんでした。発覚したのは、夜間の自動処理が全滅した朝です。

このキットは、**報告を信用しなくても品質が出る構造**をコピーして使える形にしたものです。先に「満点の姿」（北極星）を仕様として固める。機械の検査を先に全部通す。AIの採点は生成役と別のエージェントに出す。「採点結果に関係なく不合格」の失格条件を採点と分けて持つ。全適合・周回上限・停滞検知の3つ組で止める。——「生成する者と裁く者を分けよ」という原則自体は [Anthropic 公式も推奨しているもの](https://www.anthropic.com/engineering/harness-design-long-running-apps)で、このキットはそれを実運用で（事故を踏みながら）手順・テンプレート・数字に落としたものです。

## 収録内容

### スキル

| スキル | 何をするか |
|---|---|
| [`loop-engineering`](skills/loop-engineering/SKILL.md) | 改善ループの設計規範の正本。背骨の3規律（失格条件は採点と分ける／機械の検査が先・AIの採点は別エージェントで／部品は増やさず削る）→ 据え付け手順 → `.claude/harness.md`（常設の点検表）の設置 → 停止条件つきの回し方まで |

### エージェント定義（ループの登場人物・任意部品）

| 役割 | Claude Code | Codex | 規律の要点 |
|---|---|---|---|
| 調査 | [`scout`](agents/scout.md) | [`scout`](agents/codex/scout.toml) | 証拠つきの凝縮報告だけを返す。事実と推測を分離 |
| 独立検証 | [`verifier`](agents/verifier.md) | [`verifier`](agents/codex/verifier.toml) | **評価のみ・修正しない**。生成役と採点役を分ける、ループの要 |
| 設計助言 | [`opus-advisor`](agents/opus-advisor.md) | [`architecture-advisor`](agents/codex/architecture-advisor.toml) | ループが停滞したときの根本原因分析・設計判断 |
| 実装 | [`impl`](agents/impl.md) | [`impl`](agents/codex/impl.toml) | 指示された変更だけを実装。コミット・pushはしない |

「生成する者に自己採点させない」がループ設計の背骨です。Claude Code側のエージェント定義には必要に応じて `model:` を指定できます。Codex側の定義はモデルを固定せず、利用者の設定を引き継ぎます。
公開用のCodex定義は、私家版からの機械コピーではなく、公開利用者向けの責務に設計し直しています。
※ 保守メモ: Claude Code用agentsの `impl`・`verifier` は公開用にプロジェクト名を一般化済み＝私家版からの機械コピー不可（`scout`・`opus-advisor`・`skills/loop-engineering/SKILL.md` は正本と同一）。Codex用agents 4本も公開利用者向けに設計し直しており、私家版からの機械コピー不可です。

## 導入（Claude Code / Codex）

`skills/` 配下を対象ホストのスキル置き場にコピーします。引数なしは従来どおり Claude Code だけへ入れるため、既存の導入方法もそのまま使えます。スクリプトはスキルだけをインストールし、エージェント定義はコピーしません。

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

Claude Codeの保存先は `~/.claude/skills/loop-engineering`、Codexの保存先は `~/.agents/skills/loop-engineering` です。同名のスキルが既にある場合は上書きされます。旧版（スキル名 `harness-engineering`）から更新する場合は、使っているホストの旧フォルダを手動で削除してください。

## 起動とエージェントの導入

Claude Codeでは、「このプロジェクトはループ運用でいく」または「点数が上がるまで改善ループを回して」と依頼すると、`loop-engineering` の説明に応じて起動します。Codexでは、同じ自然言語の依頼に加えて `$loop-engineering` を明示するか、`/skills` からスキルを選べます。スキルの説明に合う依頼なら、明示しなくても起動候補になります。

エージェント定義4本は任意部品です。導入スクリプトでは配らないため、衝突がないことを確認してから必要なホストへ手動でコピーしてください。

| ホスト | コピー元 | コピー先 |
|---|---|---|
| Claude Code | `agents/*.md` | `~/.claude/agents/` |
| Codex | `agents/codex/*.toml` | `~/.codex/agents/` |

Windows (PowerShell) の例:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\agents" | Out-Null
Copy-Item .\agents\*.md "$HOME\.claude\agents\"
New-Item -ItemType Directory -Force "$HOME\.codex\agents" | Out-Null
Copy-Item .\agents\codex\*.toml "$HOME\.codex\agents\"
```

Mac / Linux の例:

```sh
mkdir -p "$HOME/.claude/agents" "$HOME/.codex/agents"
cp agents/*.md "$HOME/.claude/agents/"
cp agents/codex/*.toml "$HOME/.codex/agents/"
```

Codex用の `impl` は作業領域を書き込めます。`scout`・`verifier`・`architecture-advisor` は読み取り専用です。どちらのホストでも、調査・実装・検証の担当を分け、検証担当には受け入れ条件と対象差分を渡してください。

## 使い方

- 「このプロジェクトはループ運用でいく」（または「ハーネスエンジニアリングでいく」）と宣言すると、`.claude/harness.md`（点検表）の据え付けから改善ループの配線までを `loop-engineering` スキルが手順どおりに進めます。
- 「点数が上がるまで改善ループを回して」と頼むと、北極星（満点の姿を定めた仕様）との適合チェックリストで採点と修正のループが停止条件つきで回ります。仕様が無ければ、先にそれを固めるところから始まります。
- エージェントを導入した場合は、利用中のホストが作業内容に応じて使い分けます（調査→scout、検収前→verifier など）。

## ライセンス

独自ライセンス（無料公開・source-available）です。全文は [LICENSE](LICENSE)。**利用は自由**（個人・業務どちらでも。スキルを使って作った成果物は商用含めて利用者のもの）、**本ファイル自体の再配布・転載・販売・自作としての公開は不可**。出典つきの短い引用を伴う紹介・論評は歓迎します。
