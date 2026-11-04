# 站点差异

`list_chapters.py` 只读目录 HTML。章节正文交给 `convert.py` 里的 Defuddle。

## Oracle

库地址：

- 11.2：`https://docs.oracle.com/cd/E11882_01/`，章节是扁平的 `name.htm`
- 12.2 / 19 / 21：`https://docs.oracle.com/en/database/oracle/oracle-database/{版本}/{代码}/toc.htm`

用 `--mode oracle`。它会丢掉 `toc.htm`、重复链接，以及链接文字 `Next` / `Previous`。分页文字若留在结果里，真正的前言标题会被挤掉。

19c 的 ASM（`ostmg`）在目录里用站点根绝对路径，图片在 `images/*.gif` 而不是 `/img/`。`--mode oracle` 会用目录 URL 的路径剥掉书本前缀，嵌套页在转换时摊平为文件名。同书链接也改写成这个文件名的 `.md`，因为落地目录是平的。摊平前确认主干名没有撞车。

有的书唯一正文是 `index.html`（SQL*Plus Release Notes）。`--mode oracle` 若返回空列表，打开目录页看真正的正文文件，把那一个 `href` 写进清单。`./index.html` 这种分页链接不是这份正文。

11.2 若一本书抽不出章节，把 `toc.htm` 作为唯一章节写进清单，落地名用 `content.md`（`href` 仍写 `toc.htm`，并在清单里加 `"stem": "content"`）。

在线文档号经常新于本地 PDF。summary 里两个都写。`preface.html`、`book-index.html` 可能是 404；只写着 “Part … / JavaScript must be enabled” 的分页标题没有正文。这两种都不要留在清单里。

## 达梦

顶栏是六个独立栏目，每个栏目一份侧栏，`base_url` 不同：

- 产品手册 `…/pm/`
- 快速上手 `…/start/`
- 运维指南 `…/ops/`
- 应用开发指南 `…/app-dev/`
- SQL 开发指南 `…/sql-dev/`
- 常见问题 `…/faq/`

只转用户给出的那个 URL，会漏掉其余栏目。每个栏目单独跑：

```bash
python3 "$SKILL/scripts/list_chapters.py" --mode dameng --url "https://eco.dameng.com/document/dm/zh-cn/start/"
```

侧栏在页面里出现两遍（桌面和移动）。解析在分组标题第二次出现时停下。分组标题的标记是 `font-weight:800;">`。只保留相对 `.html`；指向 `/` 或 `http` 的是站点外壳。

文件名混用 `-`、`_`，并且可以含 `+`（`c_c++_odbc.html`）。`slug` 加栏目前缀，避免和产品手册里的 `installation`、`sql-language` 撞名。

`download.dameng.com` 上的图经常是无后缀的 gzip（文件头 `1f 8b`），或把 BMP（文件头 `BM`）存成 `.jpg`，或直接返回 HTML 404。转换脚本会解压 gzip、按文件头补后缀，并丢掉 HTML 响应。图的替代文字若是「删除目录」，改用文件名主干。

同栏链接按该栏的 `base_url` 改写。跨栏链接保持原 URL。

## 新站点

1. 抓落地页 HTML，找出真正列出章节的那一次请求。目录若是前端再请求来的，以那次请求的 URL 作为 `--url`。
2. 先跑 `--mode relative`。结果里混有页眉页脚，只把正文目录的链接抄进清单。
3. 抽一章，看 Defuddle 正文是否从文章开始、侧栏有没有卷进来。侧栏卷进来就换目录标记，不要整库开转。
4. 下第一张图，看前几个字节：gzip、HTML、或和后缀不符的位图。确认后再跑全库。
5. 章节链接是嵌套路径时，先统计文件名主干。主干冲突的书保持子目录，并在清单里为冲突章写 `"stem"`，转换脚本用 `stem` 做文件名。
