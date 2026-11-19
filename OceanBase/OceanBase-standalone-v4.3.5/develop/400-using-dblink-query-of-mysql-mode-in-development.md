---
title: "使用 DBLink 查询"
book: "应用开发"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577732.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 使用 DBLink 查询

#### 注意

受限于 OBClient，当前通过 DBLlink 读取表数据时，会将远端表中 `ENUM` 和 `SET` 类型的列当作 `VARCHAR` 类型列处理。
