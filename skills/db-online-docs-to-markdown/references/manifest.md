# 清单

`convert.py` 读一份 JSON。`out` 的目录名必须是 `html-to-md`。`base_url` 以 `/` 结尾。`href` 相对该书 `base_url`，可以带子目录（Oracle 的 `part-i/preface.html`），落地文件只保留最后一段的主干。

```json
{
  "product": "达梦数据库 DM8",
  "version": "DM8",
  "tags": ["dameng", "dm8"],
  "out": "/absolute/path/html-to-md",
  "books": [
    {
      "slug": "start-versions",
      "title": "DM 数据库版本介绍",
      "summary": "版本区别和安装包获取。",
      "group": "快速上手",
      "base_url": "https://eco.dameng.com/document/dm/zh-cn/start/",
      "doc_id": "",
      "chapters": [
        {"href": "dm-version-differences.html", "title": "版本区别"}
      ]
    }
  ]
}
```

| 字段 | 要求 |
| --- | --- |
| `product` | 目录大标题用的产品名，脚本会接上「文档目录」 |
| `version` | 写入 frontmatter 时始终加引号，例如 `DM8`、`19c`、`11.2` |
| `tags` | 至少一个，再自动加上该书 `slug` |
| `group` | 中文栏名。同一栏的书在清单里排在一起，目录按首次出现的栏序输出 |
| `summary` | 一句中文，说明这本手册覆盖什么。文档号写在这里 |
| `doc_id` | 可省略。有官方文档号时写入章节 frontmatter |
| `chapters[].title` | 目录页上的可见文字，用作 `contents.md` 的条目 |
| `chapters[].stem` | 可省略。落地文件名主干；缺省时用 `href` 最后一段去掉扩展名。11.2 把唯一的 `toc.htm` 收成 `content` 时要写 |

`slug` 匹配 `^[a-z0-9][a-z0-9-]*$`。达梦不同栏目可能有同名页面，用栏目前缀避开已有目录：`start-`、`ops-`、`app-`、`sql-`、`faq-`。
