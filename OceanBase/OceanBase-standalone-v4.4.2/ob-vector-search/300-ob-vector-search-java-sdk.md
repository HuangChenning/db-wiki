---
title: "Java SDK 接口说明"
book: OceanBase AI
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077517.html"
tags:
  - oceanbase
  - standalone
  - ob-vector-search
---

# Java SDK 接口说明

#### 说明

对于更复杂的类型、约束等，可自行使用 OceanBase JDBC 的接口进行创建，而不使用 obvec_jdbc。

#### 注意

IsAutoInc 需要在 IsPrimary 为真的情况才生效。

#### 注意

IsNullable 默认是假，与 MySQL 行为不同。

#### 注意

obvec_jdbc 仅支持创建向量索引，需要创建其他索引需使用 OceanBase JDBC。
