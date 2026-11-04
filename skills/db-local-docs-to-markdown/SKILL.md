---
name: db-local-docs-to-markdown
description: >-
  Converts local database PDF and CHM manuals into the same library as the
  online HTML manuals (catalog.md, per-book contents.md, chapter Markdown, and
  local images). Use when converting offline manuals, PDF, CHM, 帮助文档, or
  files under temp/doc for 达梦, Dameng, DM7, Oracle, or another database into
  Markdown for a wiki or RAG.
---

# 本地 PDF / CHM 手册转 Markdown 库

在线 HTML 用 [db-online-docs-to-markdown](../db-online-docs-to-markdown/SKILL.md)。这份技能处理已经落在磁盘上的 PDF 和 CHM，产出同一套目录。不要改用 Marker、MinerU 或 OCR：这些手册是 Word 导出的，文字层和目录是现成的。

脚本目录记为 `SKILL`：本文件所在目录。依赖本机已有的 `python3`（PyMuPDF、lxml）和 `7z`。

## 产出

库根目录就是版本目录，例如 `dameng/dm7/`。不要再套一层 `html-to-md`。

```
{库根}/
  catalog.md
  {slug}/contents.md
  {slug}/{章节文件名}.md
  {slug}/img/
```

`catalog.md` 的写法与达梦 DM8 相同。路径都相对于库根。清单留在库外，例如 `temp/`。

## 步骤

### 1. 锁定本地库

记下产品名、版本字符串、手册所在目录，以及库根（将要写入 `catalog.md` 的目录）。

完成：目录里能看到 `.pdf` 或 `.chm`。扫描页（几乎抽不出文字）不要转，脚本会直接停下。

### 2. 列出手册

```bash
python3 "$SKILL/scripts/list_docs.py" \
  --input /path/to/manuals \
  --product "达梦数据库 DM7" \
  --version DM7 \
  --tags dameng,dm7 \
  --library /path/to/dameng/dm7 \
  --draft /path/to/manifest.json
```

同一本手册若 PDF 和 CHM 都有，草稿会留下 CHM、把 PDF 放进 `skipped`。CHM 里是 Word HTML，段落、标题和表格比 PDF 行框完整。只在 CHM 里没有的书才用 PDF。

文件名在 macOS 上常被存成乱码。用草稿里的 `source` 路径打开文件，不要按终端里看到的名字重新拼路径。显示名由脚本从 GBK 还原。

完成：草稿里每本书都有 `slug`、`title`、`group`、`kind`、`source`，以及从书签或 `h1` 拆出的章节。`summary` 仍是「待补。」

### 3. 改清单

按 [manifest.md](references/manifest.md) 改草稿。给每本书写一句中文 `summary`。`slug` 用小写字母、数字和连字符，整库唯一。同一栏的书排在一起，`catalog.md` 按书在清单里第一次出现的栏序输出。

`目录` 这一条是纸质目录，脚本已经丢掉。不要把它加回去。前言要留。

完成：清单里没有「待补」，也没有仍要转换的重复本。

### 4. 试跑清单

```bash
python3 "$SKILL/scripts/convert.py" --manifest /path/to/manifest.json --dry-run
```

完成：打印的章节数与草稿一致。一本工具书通常是「前言 + 若干章」，不是每一个 `1.1` 小节一个文件。

### 5. 转换

```bash
python3 "$SKILL/scripts/convert.py" --manifest /path/to/manifest.json
```

已有非空章节会跳过。某一章抽不出正文时，脚本打出 `WARN` 并丢掉这一章，其余继续。整本书没有正文才算 `FAIL`。

完成：stderr 里没有还要补的 `FAIL`。

### 6. 验收

```bash
python3 "$SKILL/scripts/convert.py" --manifest /path/to/manifest.json --verify
```

完成：输出 `verify ok`。再打开 `catalog.md` 和任意一章，确认目录链接是反引号相对路径，图片是 `img/…`，同书章节链接是 `文件名.md`。`source` 指向库内相对路径，PDF 带 `#page=`，CHM 带主题路径。用户没要求提交或推送时，验收通过即停。

版式和取舍见 [pitfalls.md](references/pitfalls.md)。
