---
title: "修改资源池属性"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701884.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 修改资源池属性

#### 注意

如果该资源池已经被租户使用，无法通过修改资源池属性的方式修改，需要通过 `ALTER RESOURCE TENANT` 语句进行修改。

#### 注意

OceanBase 集中式数据库只能修改 `UNIT`。
