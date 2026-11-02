# skills

MetamoL が普段の作業で実際に使っている、AI エージェント用のスキルの一覧です。Claude Code・Codex など、`SKILL.md` を読むエージェントで使えます。スキルはそれぞれ単独のリポジトリで公開しています。

Agent skills for Claude Code, Codex, and other agents that read `SKILL.md`. Each skill lives in its own repository; this one is the list and the Claude Code plugin marketplace.

| スキル | 何をするか |
|---|---|
| [verified-research](https://github.com/MetamoL/verified-research) | Web 調査の答えのすべての主張に、原文どおりの引用つきの出典を付けさせる。引用がページに本当に載っているかをスクリプトで照合し、判断が絡むときは別のエージェントに読み直させる。検索の仕方はモデルに任せる。30問での評価結果は [eval](https://github.com/MetamoL/verified-research/tree/main/eval) |
| [roast-me](https://github.com/MetamoL/roast-me) | 「知っていることを全部使って、容赦なくローストして」に応える。会話や作業記録の実話だけを材料に、頼んだ人の言語で、本人が笑えるローストを書く。公開用に、未公開の情報を抜いた版も作れる |
| [japanese-writing-gemini](https://github.com/MetamoL/japanese-writing-gemini) | 小説や README などの日本語の執筆・大幅改稿を Gemini に任せるとき、Gemini がそれだけで書ける依頼文を作る |
| [japanese-novel-skill](https://github.com/MetamoL/japanese-novel-skill) | AI に日本語の小説を書かせるとき、AI 小説にありがちな癖（主題を語り手が言う、「悟って受け入れて終わる」結末、決まった体の合図で書く感情、全員同じ声の台詞、気取った比喩、頼んでいない設定の追加など）を避けて書かせ、書いた後に「整合・人物と読者・文」の三回に分けて点検させる。日中英の人気の小説スキルが共通して挙げる癖を、日本語の小説向けに作り直したもの |
| [japanese-novel-plot-skill](https://github.com/MetamoL/japanese-novel-plot-skill) | 日本語の小説・Web小説を書かせる前に、一話の筋と場面を設計させる。場面ごとの役割と変化、転回の出どころ、人物ごとの知識と誤解、読者がこの話で得る満足を決める |
| [japanese-novel-continuity-skill](https://github.com/MetamoL/japanese-novel-continuity-skill) | 日本語の長編・Web小説の連載で、人物の持ち物・関係・知識、伏線、能力や資源の制約を台帳で保たせる。作者が確定した話からだけ更新し、AI が足した事実は作者の確認を待つ |

## 導入

**Claude Code**：このリポジトリをマーケットプレイスとして追加し、使いたいスキルを名前で入れます。スキル1本が1つのプラグインです。

```
/plugin marketplace add MetamoL/skills
/plugin install japanese-novel-skill@metamol
```

ほかのスキルも `/plugin install <スキル名>@metamol` で入ります。GitHub の SSH 鍵を設定していない PC で取得に失敗するときは、環境変数 `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` を設定してから Claude Code を起動し直してください。以前の一括プラグイン `metamol-skills` は廃止しました。入れていた場合は、マーケットプレイスを更新すると外れるので、使うスキルを入れ直してください。

**Codex・そのほかのエージェント**：`npx skills add MetamoL/<スキル名>` で入ります（入れるエージェントを選べます。どのプロジェクトでも使うときは `-g` を付けます）。

**手で置く**ときは、各リポジトリをエージェントのスキルフォルダへ clone してください（Claude Code は `~/.claude/skills/<スキル名>/`、Codex は `~/.agents/skills/<スキル名>/`）。verified-research と japanese-novel-skill のスクリプトは Python 3 を使います。PDF を照合するときは `pip install pdfminer.six`、JavaScript で表示するページは `pip install playwright && playwright install chromium` を追加で入れます（必要になったときにスクリプトが案内します）。

## あわせて使っているスキル

自作ではありませんが、毎日使っているものです。

- [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)：計画や判断を質問攻めにして詰める
- [handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff)：会話を次のセッションへの引き継ぎ文書にまとめる
- [writing-for-agents](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents)：スキルや AGENTS.md を書くときの指針

いずれも Matt Pocock さんの [mattpocock/skills](https://github.com/mattpocock/skills) にあります。

## 引退したスキル

以前は別のリポジトリで公開していたスキルです。今は使っていないので一覧から外しましたが、最終版をこのリポジトリの履歴（コミット `4497714`）に残しています。なお、japanese-writing-gemini は今も使っているので上の一覧に戻し、fiction-prose-jp は中身を作り直したうえで japanese-novel-skill に改名して上の一覧に入れました。

| スキル | 何をしていたか |
|---|---|
| ai-writing-skills-jp | 技術文書や記事の「AIくささ」を減らし、読みやすい日本語に整える |
| loop-engineering-jp | AI の実装と検証を分け、停止条件つきで改善を繰り返す |

復活させるときは、このリポジトリで次を実行すると `retired/<名前>/` に元のリポジトリの中身が戻ります。

```
git checkout 4497714 -- retired/<名前>
```

## ライセンス

[LICENSE](LICENSE) のとおりです。自分の環境で使うこと・改変すること・作ったものの利用は自由です。再配布と転載はできません。ただし verified-research は MIT ライセンスで、再配布もできます。
