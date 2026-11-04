# 清单

`convert.py` 读一份 JSON。`out` 是库根，也就是将要出现 `catalog.md` 的目录。在本仓库里它是 `dameng/dm7` 这样的版本目录。

```json
{
  "product": "达梦数据库 DM7",
  "version": "DM7",
  "tags": ["dameng", "dm7"],
  "out": "/absolute/path/dameng/dm7",
  "books": [
    {
      "slug": "dmdbchk",
      "title": "DM7 dmdbchk使用手册",
      "summary": "用 dmdbchk 检查数据文件、索引和对象。",
      "group": "工具",
      "kind": "chm",
      "source": "/absolute/path/DM7帮助文档.chm",
      "topic": "~htm/dmdbchk使用手册.htm",
      "chapters": [
        {"title": "1 功能简介", "stem": "01-功能简介"}
      ]
    }
  ]
}
```

| 字段 | 要求 |
| --- | --- |
| `product` | 目录大标题用的产品名，脚本会接上「文档目录」 |
| `version` | 写入 frontmatter 时始终加引号，例如 `DM7`、`DM8` |
| `tags` | 至少一个，再自动加上该书 `slug` |
| `group` | 中文栏名。同一栏的书在清单里排在一起 |
| `summary` | 一句中文，说明这本手册覆盖什么。不能是「待补。」 |
| `kind` | `pdf` 或 `chm` |
| `source` | 磁盘上的绝对路径，用草稿里的原值 |
| `topic` | 仅 CHM。`.hhc` 里的内部路径，例如 `~htm/前言.htm` |
| `split_level` | 可省略。PDF 书签从哪一层拆成章节，默认是能拆出至少两章的最浅层 |
| `chapters[].title` | 与书签或 `h1` 原文一致。删掉的章节不会写出 |
| `chapters[].stem` | 可省略。缺省时用两位序号加标题 |

`slug` 匹配 `^[a-z0-9][a-z0-9-]*$`。`skipped` 只是草稿里的说明，转换时忽略。

PDF 不需要 `topic`。章节文件名在一本书内唯一；中文标题可以留在文件名里。
