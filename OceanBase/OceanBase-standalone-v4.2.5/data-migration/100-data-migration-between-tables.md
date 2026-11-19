---
title: "表与表之间的数据迁移"
book: "数据迁移"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701737.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 表与表之间的数据迁移

#### 注意

选择的列数量需要与目的表中的列数量保持一致。

#### 功能适用性

`MERGE` 语句暂时只支持 OceanBase 数据库 Oracle 模式。

#### 注意

选择的列数量需要与目标表中的列数量保持一致，并且迁移的数据要符合目标表的数据类型。
