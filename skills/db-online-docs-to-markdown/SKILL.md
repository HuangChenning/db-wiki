---
name: db-online-docs-to-markdown
description: >-
  Converts official database HTML manuals into an html-to-md library
  (catalog.md, per-book contents.md, chapter Markdown, and local images, with
  paths relative to html-to-md). Use when downloading, scraping, or converting
  online documentation for Oracle, 达梦, Dameng, DM8, PostgreSQL, MySQL, or
  another database into Markdown for a wiki or RAG.
---

# 在线数据库文档转 html-to-md

正文从官方 HTML 转。本地 PDF 只用来核对版本和文档号。用本技能自带的脚本，保持和已完成的 Oracle、达梦库同一套目录。

脚本目录记为 `SKILL`：本文件所在目录。

## 产出

```
html-to-md/
  catalog.md
  {slug}/contents.md
  {slug}/{章节文件名}.md
  {slug}/img/
```

`catalog.md` 按栏分组。每一本一行：`` `{slug}/contents.md`：官方书名。一句中文范围。 `` 分组名和这一句中文由你写，书名和章节名保持目录页上的原文。路径都相对于 `html-to-md`。清单、脚本留在 `html-to-md` 外面。

章节笔记的 frontmatter 含 `title`、`book`、加引号的 `version`、`source`、`tags`。厂商有文档号时加 `doc_id`。`contents.md` 的条目用目录页上的可见文字。Defuddle 常把每一页的标题收成书名；正文标题若与书名相同，或是「达梦技术文档」，改用目录标题。

## 步骤

### 1. 锁定在线库

记下产品名、版本字符串、输出目录（目录名是 `html-to-md`），以及每一栏的起始 URL。

完成：能指出每个待转栏目的在线地址，并确认它返回的是 HTML 而不是需要登录的空壳。

### 2. 列出手册

Oracle 或达梦先读 [pitfalls.md](references/pitfalls.md) 里对应的一节，再跑 `list_chapters.py`。新站点读该文件的「新站点」一节：先看落地页和其中一章，再决定用哪种模式。

```bash
python3 "$SKILL/scripts/list_chapters.py" --mode oracle --url "https://…/toc.htm"
python3 "$SKILL/scripts/list_chapters.py" --mode dameng --url "https://…/start/"
python3 "$SKILL/scripts/list_chapters.py" --mode relative --url "https://…/toc"
```

按 [manifest.md](references/manifest.md) 写成清单。一本手册一个 `slug`，整库唯一，小写字母、数字和连字符。同一本书里章节文件名（去掉目录后的主干）也唯一；嵌套页摊平到这个文件名。顶栏上的每一栏单独成组，不塞进另一栏的章节里。

完成：清单里每本书都有 `slug`、`title`、一句中文 `summary`、`group`、以 `/` 结尾的 `base_url`，以及章节 `href` + 目录标题。在线文档号和本地 PDF 不一致时，两个号都写进这句 summary。

### 3. 试跑清单

```bash
python3 "$SKILL/scripts/convert.py" --manifest /path/manifest.json --dry-run
```

完成：打印的章节数与目录页一致。`toc.htm` 不出现在章节里，除非它是该书唯一的正文页。

### 4. 转换

```bash
python3 "$SKILL/scripts/convert.py" --manifest /path/manifest.json
```

已有非空章节会跳过。结束后若仍有 `FAIL`，先看行尾的 HTTP 状态：200 的再跑同一条命令补洞；404 从清单删掉再跑，目录会跟着去掉。Defuddle 返回空正文的页会打出 `SKIP`，同样从清单删除。

完成：清单里每一章都有非空 `.md`，stderr 里没有还要补的 `FAIL`。

### 5. 验收

```bash
python3 "$SKILL/scripts/convert.py" --manifest /path/manifest.json --verify
```

完成：输出 `verify ok`。再打开 `catalog.md` 和任意一章，确认目录链接是反引号相对路径，图片是 `img/…`，同书章节链接是 `文件名.md`。用户没要求提交或推送时，验收通过即停。
