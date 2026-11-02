<!-- codex-environment: 2026-09 -->
# japanese-writing-gemini

人間向けの公開日本語文書をGeminiに書き下ろさせるための、汎用エージェント向けスキルrepo。`SKILL.md`が配布する正本、`README.md`が利用者向け説明、`agents/openai.yaml`はCodex向けの任意メタデータ。Geminiへの送信や利用者環境への自動導入をこのrepoから行わない。

変更時はSKILL.mdの発火条件・承認境界・1ブロック出力、READMEの汎用エージェント説明、Codexメタデータの整合を確認する。技術的な例や導入先は、特定ホストの仕様と照合し、秘密値を含めない。READMEや告知文などの人間向け文章は、別途このスキルを使う対象であり、配布スキルの内部指示へ混ぜない。
