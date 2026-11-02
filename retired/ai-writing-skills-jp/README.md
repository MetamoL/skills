# ai-writing-skills-jp

AIに「AIくさくない日本語」を書かせるための、Claude CodeとCodex向けの日本語ライティング支援スキル集です。

文法チェッカーや、単語を禁止するだけのプロンプト集ではありません。書く前の論点設計、生成時の原理、書いた後の機械的な点検手順を `SKILL.md` にまとめ、AIが量産しがちな不自然さを文章の構造から減らします。

## どんな問題を扱うか

LLMに技術解説や記事を書かせると、文法は正しいのに読みにくい文章になることがあります。

- 「本章では〜を扱います」のような本文の進行案内が続く
- 句点で細かく刻んだ短文が並び、文章のリズムが平坦になる
- 「非常に」「まさに」のような、根拠を増やさない強調語が増える
- 事実、理由、判断が混ざり、読者が論理の骨組みを追いにくくなる
- 正確な説明なのに、冒頭や節の途中で読む理由がなくなる

本リポジトリでは、こうした癖を禁止語の置き換えだけで処理せず、読者・結論・根拠・文章の流れを設計し、書き上げた後に点検する工程として扱います。

## 収録スキル

| スキル | 対象 | 役割 |
|---|---|---|
| [`japanese-tech-writing`](skills/japanese-tech-writing/SKILL.md) | 技術文書・書籍原稿・解説記事・報告 | 読者に届く順番で構成し、主張に根拠と適用範囲を付け、水増しを削る |
| [`cognitive-rhythm-writing`](skills/cognitive-rhythm-writing/SKILL.md) | 記事・ブログ・章もの・解説読み物 | 「正確なのに読まれない」文章を症状別に診断し、疑問の流れとリズムを整える |

### `japanese-tech-writing`

文章を書く前に、読者が誰で何を知りたいか、結論は何か、確かなことと推測をどう分けるかを決めます。本文では段落の役割、主張の根拠、適用範囲を確認し、仕上げでは進行案内や言い換えなどの水増しを削ります。

### `cognitive-rhythm-writing`

冒頭で閉じられる、中盤で読み飛ばされる、概念の説明に入ると眠くなる、締めが説教くさくなる、といった症状から原因と処方を引ける規範です。読者の疑問を保ち、説明を追体験に変え、文の長さと確信の濃淡に波を作ります。

2本は独立して使えますが、技術的な正確さを `japanese-tech-writing` で整えたうえで、読み物としての流れを `cognitive-rhythm-writing` で調整する併用を推奨します。

## 導入

`skills/` 配下のフォルダーを、Claude Codeの `~/.claude/skills/` またはCodexの `$HOME/.agents/skills/` にコピーします。同名のスキルが既にある場合は上書きされます。

### Windows（PowerShell）

```powershell
# Claude Code（既定値）
powershell -ExecutionPolicy Bypass -File .\install.ps1

# Codex
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target codex

# Claude CodeとCodexの両方
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target both
```

### macOS / Linux

```sh
# Claude Code（既定値）
sh install.sh

# Codex
sh install.sh codex

# Claude CodeとCodexの両方
sh install.sh both
```

特定のスキルだけを使う場合は、対応するフォルダーを手動でコピーしてください。

## 使い方

導入後は、依頼内容がスキルの `description` に一致すると、Claude CodeやCodexがスキルを読み込めます。反映されない場合は、対象のホストを再起動してください。

Claude Codeで明示的に呼び出す例:

```text
/japanese-tech-writing この機能の解説ドキュメントの構成案を作って
```

```text
/cognitive-rhythm-writing 以下の下書きを診断して、読者が離脱しそうな箇所と直し方を示して
```

Codexでは、利用可能なスキル名を `$` 付きで指定できます。

```text
$japanese-tech-writing と $cognitive-rhythm-writing の規範に従って、以下の技術記事を推敲してください。
```

Claude Code以外のAIツールでも、`SKILL.md` は素のMarkdownとしてシステムプロンプトやカスタム指示に貼り付けて使えます。

## 収録内容

```text
ai-writing-skills-jp/
├── skills/
│   ├── japanese-tech-writing/
│   │   └── SKILL.md
│   └── cognitive-rhythm-writing/
│       └── SKILL.md
├── install.ps1
├── install.sh
├── LICENSE
└── README.md
```

## 対象外

小説・物語本文の文体や、人物の知識、持ち物、距離などの作中整合性を扱うスキルは、別リポジトリの [fiction-prose-jp](https://github.com/MetamoL/fiction-prose-jp) に分離しています。

このスキル集は、指示ひとつで名文を自動生成するものではありません。AIが書いた文章の設計と点検を支援するものであり、内容の正しさや最終的な表現の判断には人間のレビューが必要です。

## 姉妹リポジトリ

- [fiction-prose-jp](https://github.com/MetamoL/fiction-prose-jp) — 小説・物語の本文のための執筆規範
- [loop-engineering-jp](https://github.com/MetamoL/loop-engineering-jp) — AIに改善ループを回させるためのキット
- [video2md](https://github.com/MetamoL/video2md) — YouTube動画から音声と映像の情報をMarkdownへ保存するCLI

## 着想と出典について

読ませる文章の緩急や、本文の自己解説を削るという考え方の一部は、k16shikano氏が公開している執筆規範のgist（[認知リズム](https://gist.github.com/k16shikano/eb2929f13ed19c97188393d297be8432)／[技術文書](https://gist.github.com/k16shikano/fd287c3133457c4fd8f5601d34aa817d)）に触発されています。本リポジトリの本文はすべて自分の言葉で書き下ろしたもので、氏の文章そのものは含みません。

## ライセンス

独自ライセンス（source-available）です。全文は [LICENSE](LICENSE) を確認してください。

- 個人・業務を問わず、導入して使えます。
- 自分または所属組織内で使うための改変ができます。
- このスキルを使って書いた文章や成果物は、商用を含めて利用できます。
- リポジトリへのリンク共有や、出典を示した短い引用を伴う紹介・論評は歓迎します。
- スキル本文（改変版・翻訳版を含む）の再配布・転載・再公開・販売、自作と称すること、著作権表示やライセンス表記を除去することは禁止されています。
