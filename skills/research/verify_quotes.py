"""回答の脚注にある「URL＋原文の引用」を、ページの原文と突き合わせる。

脚注の書式（1行に1つ）:
    [^1]: https://example.com/page 「ページにそのまま載っている文」
引用の途中を省くときは … でつなぐ（各部分が順番どおりに載っていれば一致）。

使い方:
    python verify_quotes.py answer.md
    python verify_quotes.py --text URL   # ページ本文をそのまま表示（引用はここから写す）
    python verify_quotes.py --selftest
すべて一致なら終了コード 0、載っていない引用があれば 1。
"""
import gzip
import html
import re
import sys
import unicodedata
import urllib.request

# URL は裸でも [名前](URL) でもよい（モデルによって書き方が揺れるため）
FOOTNOTE = re.compile(r'^\[\^([^\]]+)\]:\s*(?:\[[^\]]*\]\()?(https?://[^\s)]+)\)?\s*[「"“](.+)[」"”]\s*$')


def norm(text):
    # 全角半角・大小文字・空白の違いを無視する（日本語は語の間に空白がないので空白は全部消す）
    text = unicodedata.normalize('NFKC', text).lower()
    text = text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', '', text)


def page_text(raw):
    raw = re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>', ' ', raw)
    return html.unescape(re.sub(r'<[^>]+>', ' ', raw))


def contains(page, quote):
    pos = 0
    for part in re.split(r'…|\.\.\.', quote):
        part = norm(part)
        if not part:
            continue
        pos = page.find(part, pos)
        if pos < 0:
            return False
        pos += len(part)
    return True


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=20) as res:
        if 'pdf' in res.headers.get('Content-Type', ''):
            raise ValueError('PDFは未対応')
        data = res.read()
        if res.headers.get('Content-Encoding') == 'gzip':
            data = gzip.decompress(data)
        charset = res.headers.get_content_charset() or 'utf-8'
    return data.decode(charset, errors='replace')


def unchecked_links(raw, footnote_urls):
    # 未確認より上の本文に、脚注で照合されないリンクがあれば照合のすり抜けとして数える
    found = []
    for line in raw:
        if '未確認' in line:
            break
        if line.startswith('[^'):
            continue
        for url in re.findall(r'https?://[^\s)\]」>]+', line):
            if url not in footnote_urls:
                print(f'本文に脚注のないリンク（照合されない）{url}')
                found.append(url)
    return found


def check(path):
    cache = {}
    with open(path, encoding='utf-8') as f:
        raw = f.read().splitlines()
    lines = [m.groups() for m in map(FOOTNOTE.match, raw) if m]
    if not lines:
        print('脚注が見つかりません（書式: [^1]: URL 「引用」）')
        return 1
    loose = len(unchecked_links(raw, {url for _, url, _ in lines}))
    bad = 0
    for label, url, quote in lines:
        try:
            if url not in cache:
                cache[url] = norm(page_text(fetch(url)))
            text = cache[url]
        except Exception as e:  # 取得できないページは「載っていない」とは別に扱う
            print(f'[^{label}] 取得失敗 ({e}) {url}')
            bad += 1
            continue
        if len(text) < 200:
            print(f'[^{label}] 本文が取れない（JavaScript で表示するページの可能性）{url}')
            bad += 1
        elif contains(text, quote):
            print(f'[^{label}] OK')
        else:
            print(f'[^{label}] 引用が見つからない {url}\n    「{quote}」')
            bad += 1
    print(f'{len(lines) - bad}/{len(lines)} 件が一致')
    return 1 if bad or loose else 0


def selftest():
    page = norm(page_text('<p>東京都最低賃金は<b>10月1日</b>から\n時間額1,280円</p><script>x</script>'))
    assert contains(page, '時間額１，２８０円')
    assert contains(page, '東京都最低賃金は…1,280円')
    assert not contains(page, '1,280円…東京都')
    assert not contains(page, 'x')
    assert FOOTNOTE.match('[^1]: https://a.example/b 「引用」').groups() == ('1', 'https://a.example/b', '引用')
    assert FOOTNOTE.match('[^2]: [名前](https://a.example/b) 「引用」').groups() == ('2', 'https://a.example/b', '引用')
    body = ['結論 [公式](https://a.example/b)', '別 https://c.example/d', '**未確認**', 'https://e.example/f']
    assert unchecked_links(body, {'https://a.example/b'}) == ['https://c.example/d']
    print('selftest ok')
    return 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1:] == ['--selftest']:
        sys.exit(selftest())
    if len(sys.argv) == 3 and sys.argv[1] == '--text':
        print(re.sub(r'\s+', ' ', page_text(fetch(sys.argv[2]))).strip())
        sys.exit(0)
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(check(sys.argv[1]))
