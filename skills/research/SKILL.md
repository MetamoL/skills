---
name: research
description: Web research whose answer must rest on verified sources. Use when the user asks to research, investigate, fact-check, or compare something on the web (調べて, 調査, 根拠, 裏取り), or when an answer depends on facts newer than your training.
---

Search however you judge best: breadth, depth, and query choice are yours. This skill governs only what reaches the user: every claim carries a source the user can audit, and every quote is checked by a script, never by your own say-so.

`verify_quotes.py` sits next to this file. Run it as `python -X utf8 verify_quotes.py ...` (UTF-8 output on Windows consoles too).

## Steps

1. **Collect.** Search widely and in parallel. Prefer the **primary source** (official docs, patch notes, government pages, the paper itself) over anyone describing it. Done when each claim you plan to make has a candidate source page.
2. **Quote from the raw page.** Read each source with `verify_quotes.py --text URL` and copy a sentence **verbatim**. Fetch tools that summarise the page paraphrase it, and a paraphrase fails the check. Done when every claim has a verbatim quote. A page that yields no text (JavaScript, PDF, blocked) is unverifiable: look for the same text at a fetchable copy (RSS feed, official API, mirror), otherwise list it under 未確認 instead of quoting from memory.
3. **Weigh sources** by the rules below. Done when every claim rests on a primary source or on two **independent** sources.
4. **Write the answer** in the user's language: conclusion first, each claim footed `[^N]`, then a short **未確認** list (claims you could not source, sources that disagree and which one you trust and why). Everything above 未確認 is footed, and its links live in footnotes (the script fails a link it cannot check); 未確認 items need no footnote. Footnotes, one per line, exactly:
   `[^1]: https://example.com/page 「verbatim quote」`
   Join omitted parts of a quote with `…`.
5. **Verify.** Save the answer to a temp file and run `verify_quotes.py <file>`. Fix or drop every failing quote and rerun until it exits 0 (a fetch failure may be transient: rerun once before dropping). Unverifiable pages stay only if listed under 未確認.
6. **Cold read**, when the conclusion is a judgment, comparison, or recommendation, or when sources conflict. A plain fact settled by a verified primary-source quote is done at step 5. Hand the answer (not your notes) to a fresh subagent: "For each footnote, open the URL and judge whether the quote actually supports the claim it is attached to. Then search for evidence against the conclusion. Report mismatches and counter-evidence." Fix what it finds and rerun step 5. Without subagents, do this as a separate pass that reads only the answer.

## Weighing sources

- **Primary beats count.** One official page outweighs any number of articles repeating it; when they conflict, the primary source wins and the conflict goes under 未確認.
- **Independent agreement only.** Sources that copy each other (same wording, same numbers, citing the same origin) count as one.
- **How the page was made.** Weight follows the work behind it: measurements, tests, method, or raw data from an author who can be held to it (individuals and YouTubers included) carry weight. Plausible assertion, rankings without method, and mass-produced SEO or AI-written pages carry little even when not wrong; use them only to find what they point at.
- **False premise.** If the question assumes something that does not exist (an "official recommendation" no official page states), answer that it was not found rather than supplying the nearest number. Likewise when the primary source exists but omits the detail asked (a date, a figure): say the primary source does not state it, then give the best secondary evidence labelled as such.
