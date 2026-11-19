---
title: "自动分区分裂"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078141.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 自动分区分裂

#### 注意

- 如果是指定多列分区键，需用使用 `PARTITION BY RANGE COLUMNS()`。
- 对预分区键的操作限制等同于分区键。

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP1 版本开始自动分区分裂阈值下限值从 128M 调整为 1M。

#### 注意

表数据量大的场景不建议将 `SIZE` 设置过小，避免产生大量的分区，影响后续分区操作及系统稳定性。

#### 注意

当预先创建分区位点时，必须指定预分区键，否则报错。

#### 说明

若在使用 `ALTER TABLE ... PARTITION BY ...` 语句时没有定义分区规则，则会采用 Online DDL 的方式修改表的自动分区属性，并且不影响原有的分区定义。

#### 注意

如果修改为多列分区键，需用使用 `PARTITION BY RANGE COLUMNS()`。

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP1 版本开始自动分区分裂阈值下限值从 128M 调整为 1M。

#### 注意

表数据量大的场景不建议将 `SIZE` 设置过小，避免产生大量的分区，影响后续分区操作及系统稳定性。

#### 说明

可以使用视图 `information_schema.TABLES` 或者在系统租户中使用 `oceanbase.CDB_TABLES` 查看表的自动分区属性。

#### 说明

其余 DDL 操作与非自动分区表要求一致。

#### 说明

可以使用 `SHOW PARAMETERS LIKE 'enable_auto_split';` 查看自动分区功能是否开启。

#### 说明

对于开启自动分区的表，即使配置项 [global_index_auto_split_policy](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285692) 未启用，创建的全局索引仍会自动分区。
