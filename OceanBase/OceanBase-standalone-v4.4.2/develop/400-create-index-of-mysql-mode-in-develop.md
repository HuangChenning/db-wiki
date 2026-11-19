---
title: "创建索引"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077450.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 创建索引

#### 说明

本文主要介绍使用 `CREATE INDEX` 语句创建索引，多值索引除外。多值索引仅支持在创建表时创建。其他创建索引的方式请参见 [CREATE TABLE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286449) 或 [ALTER TABLE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286496) 语句。

#### 说明

您可以使用 `SHOW INDEX FROM table_name;` 语句查看表中索引的信息，其中 `table_name` 为表名。
