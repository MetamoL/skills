# skills

MetamoL が普段の作業で実際に使っている、Claude Code 用のスキルです。

| スキル | 何をするか |
|---|---|
| [verified-research](skills/verified-research/) | Web 調査の答えのすべての主張に、原文どおりの引用つきの出典を付けさせる。引用がページに本当に載っているかをスクリプトで照合し、判断が絡むときは別のエージェントに読み直させる。検索の仕方はモデルに任せる。30問での評価結果は [eval](skills/verified-research/eval/) |
| [roast-me](skills/roast-me/) | 「知っていることを全部使って、容赦なくローストして」に応える。会話や作業記録の実話だけを材料に、頼んだ人の言語で、本人が笑えるローストを書く。公開用に、未公開の情報を抜いた版も作れる |
| [japanese-writing-gemini](skills/japanese-writing-gemini/) | 小説や README などの日本語の執筆・大幅改稿を Gemini に任せるとき、Gemini がそれだけで書ける依頼文を作る |
| [fiction-prose-jp](skills/fiction-prose-jp/) | AI に日本語の小説を書かせるとき、一発で出る本文の質を上げる。連載で AI の稿を直して見つかった癖（オウム返し、重ねた比喩、目の光で語る感情、細切れの段落、足された設定など）を避けて書かせ、書いた後に点検表と付属スクリプトで自分の稿を点検させる。同じ筋で書き比べると、「た」の三連続 8→0、一文段落の連続 4→0、台詞の「……」 5→0、文あたりの読点 0.60→0.53 |

## 導入

Claude Code で次の2行を実行します。

```
/plugin marketplace add MetamoL/skills
/plugin install metamol-skills@metamol
```

1本だけ使いたいときは、`skills/<名前>/` のフォルダを `~/.claude/skills/<名前>/` へコピーしてください。verified-research と fiction-prose-jp の点検スクリプトは Python 3 を使います。PDF を照合するときは `pip install pdfminer.six`、JavaScript で表示するページは `pip install playwright && playwright install chromium` を追加で入れます（必要になったときにスクリプトが案内します）。

## あわせて使っているスキル

自作ではありませんが、毎日使っているものです。

- [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)：計画や判断を質問攻めにして詰める
- [handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff)：会話を次のセッションへの引き継ぎ文書にまとめる
- [writing-for-agents](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents)：スキルや AGENTS.md を書くときの指針

いずれも Matt Pocock さんの [mattpocock/skills](https://github.com/mattpocock/skills) にあります。

## 引退したスキル

以前は別のリポジトリで公開していたスキルです。今は使っていないので一覧から外しましたが、最終版をこのリポジトリの履歴（コミット `4497714`）に残しています。なお、japanese-writing-gemini は今も使っているので上の一覧に戻し、fiction-prose-jp は中身を作り直して上の一覧に入れました。

| スキル | 何をしていたか |
|---|---|
| ai-writing-skills-jp | 技術文書や記事の「AIくささ」を減らし、読みやすい日本語に整える |
| loop-engineering-jp | AI の実装と検証を分け、停止条件つきで改善を繰り返す |

復活させるときは、このリポジトリで次を実行すると `retired/<名前>/` に元のリポジトリの中身が戻ります。

```
git checkout 4497714 -- retired/<名前>
```

## ライセンス

[LICENSE](LICENSE) のとおりです。自分の環境で使うこと・改変すること・作ったものの利用は自由です。再配布と転載はできません。
