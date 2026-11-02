# skills

MetamoL が普段の作業で実際に使っている、Claude Code 用のスキルです。

| スキル | 何をするか |
|---|---|
| [research](skills/research/) | Web 調査の答えに、原文どおりの引用つきの出典を付けさせる。引用がページに本当に載っているかをスクリプトで照合し、別のエージェントに読み直させる。検索の仕方はモデルに任せる |
| [roast-me](skills/roast-me/) | 会話や作業記録の実話だけを材料に、本人が笑えるローストを書く。公開用に、未公開の情報を抜いた版も作れる |

## 導入

Claude Code で次の2行を実行します。

```
/plugin marketplace add MetamoL/skills
/plugin install metamol-skills@metamol
```

1本だけ使いたいときは、`skills/<名前>/` のフォルダを `~/.claude/skills/<名前>/` へコピーしてください。research は Python 3 を使います（標準ライブラリだけで動きます）。

## あわせて使っているスキル

自作ではありませんが、毎日使っているものです。

- [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)：計画や判断を質問攻めにして詰める
- [handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff)：会話を次のセッションへの引き継ぎ文書にまとめる
- [writing-for-agents](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents)：スキルや AGENTS.md を書くときの指針

いずれも Matt Pocock さんの [mattpocock/skills](https://github.com/mattpocock/skills) にあります。

## 引退したスキル

以前は別のリポジトリで公開していたスキルです。今は使っていないので一覧から外しましたが、最終版をこのリポジトリの履歴（コミット `4497714`）に残しています。

| スキル | 何をしていたか |
|---|---|
| ai-writing-skills-jp | 技術文書や記事の「AIくささ」を減らし、読みやすい日本語に整える |
| fiction-prose-jp | 小説本文のリズムと、持ち物・時刻・人物の知識のつじつまを整える |
| japanese-writing-gemini | README や記事の日本語執筆を Gemini に任せるためのブリーフを作る |
| loop-engineering-jp | AI の実装と検証を分け、停止条件つきで改善を繰り返す |

復活させるときは、このリポジトリで次を実行すると `retired/<名前>/` に元のリポジトリの中身が戻ります。

```
git checkout 4497714 -- retired/<名前>
```

## ライセンス

[LICENSE](LICENSE) のとおりです。自分の環境で使うこと・改変すること・作ったものの利用は自由です。再配布と転載はできません。
