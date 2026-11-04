---
title: "子查询"
book: "数据查询DQL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_five_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-dql
---

## 子查询

子查询指定了一个派生表，它必须被包围在圆括弧里并且必须被赋予一个表别名。一个子查询也可以是一个 VALUES 列表。

例如用 SELECT 和 VALUES 来表示两个子查询：

```
FROM (SELECT * FROM table1) AS alias_name

FROM (VALUES ('anne', 'smith'), ('bob', 'jones'), ('joe', 'blow')) AS names(first, last)
```