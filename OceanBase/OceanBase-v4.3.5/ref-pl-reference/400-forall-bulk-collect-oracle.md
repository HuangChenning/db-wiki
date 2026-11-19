---
title: "FORALL 与 BULK COLLECT"
book: "PL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005358600.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# FORALL 与 BULK COLLECT

#### 功能适用性

该内容仅适用于 OceanBase 数据库企业版 Oracle 模式。

#### 注意

虽然 `MERGE INTO` 支持在 `FORALL` 中使用，但 SQL 引擎目前不支持 `MERGE INTO` 的 array binding，会降级为 `FOR` 循环执行。

#### 注意

动态 SQL 中的 `FORALL` 不支持 `IN OUT` 绑定变量。

#### 说明

语句未返回任何行时，PL/SQL 不抛出 NO_DATA_FOUND，目标集合为空，需在代码中判断集合是否为空。
