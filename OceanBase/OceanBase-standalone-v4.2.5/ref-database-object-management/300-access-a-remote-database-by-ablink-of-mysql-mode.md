---
title: "通过 DBLink 访问远端数据库中的数据"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150333.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 通过 DBLink 访问远端数据库中的数据

#### 注意

受限于 OBClient，当前通过 DBLlink 读取表数据时，会将远端表中 `ENUM` 和 `SET` 类型的列当作 `VARCHAR` 类型列处理。
