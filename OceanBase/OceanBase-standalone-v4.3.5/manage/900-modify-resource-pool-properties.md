---
title: "修改资源池属性"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577612.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 修改资源池属性

#### 注意

- 单条语句只能修改一个属性，如果需要同时修改 `UNIT`、`UNIT_NUM`、`ZONE_LIST` 中两条及以上的属性，需要分多条语句执行。
- 修改 `ZONE_LIST` 时，每次仅支持添加或删除一个 Zone。

#### 注意

如果该资源池已经被租户使用，无法通过修改资源池属性的方式修改，需要通过 `ALTER RESOURCE TENANT` 语句进行修改。

#### 注意

OceanBase 集中式数据库只能修改 `UNIT`。
