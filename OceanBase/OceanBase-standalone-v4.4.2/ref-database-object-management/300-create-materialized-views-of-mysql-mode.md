---
title: "创建物化视图"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078127.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建物化视图

#### 说明

OceanBase 数据库暂时不支持直接修改物化视图的属性，如更新时间、刷新策略等。在这种情况下，可以考虑删除并重新创建物化视图以达到修改物化视图的目的。

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP2 版本开始支持在 `REFRESH` 子句中通过 `REFRESH ... PARALLEL n` 指定刷新并行度。

#### 说明

- OceanBase 数据库支持外表作为物化视图的基表来创建全量刷新物化视图。
- OceanBase 数据库支持在创建物化视图时对基表添加 `AS OF PROCTIME()` 子句，若在创建物化视图基表位置之外的地方使用了 `AS OF PROCTIME()` 则会报错。`AS OF PROCTIME()` 用于指定增量刷新时跳过这张表的刷新，并且 `AS OF PROCTIME()` 的表可以不创建 mlog。
- OceanBase 数据库支持普通视图声明为维度表（`AS OF PROCTIME()`）时，可以作为增量刷新物化视图的基表。

#### 说明

对于非嵌套物化视图来说，不存在级联刷新行为，无论指定为何种刷新策略均无意义，都默认独立刷新。指定的三种刷新策略只在后台任务生效，当手动使用 PL 包（[DBMS_MVIEW.REFRESH](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286701)）调度刷新，按照指定的 PL 参数执行刷新。

#### 注意

对于定义了 `ENABLE QUERY REWRITE` 子句的物化视图并不表示物化视图一定会改写查询。对于不满足查询改写条件的物化视图，不会报错，但不会被用于改写。由于系统变量 `query_rewrite_enabled` 默认值是 `false`，所以默认情况下定义了 `ENABLE QUERY REWRITE` 子句的物化视图并不会被用于改写。

#### 说明

不指定 `mv_column_group_option` 选项时，默认创建行存格式的物化视图。

#### 注意

为物化视图指定主键后，维护/更新物化视图数据时，如果数据不满足主键约束，将导致视图维护失败。

#### 注意

如果一个物化视图进行了全量刷新，那么依赖它的物化视图（嵌套物化视图）在后续进行增量刷新前必须先进行一次全量刷新，否则会报错。

#### 注意

示例中涉及 IP 的命令做了脱敏处理，在验证时应根据自己机器真实 IP 填写。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285634)。

#### 注意

对于 V4.4.2 版本，从 V4.4.2 BP2 版本开始支持在创建增量刷新物化视图时，如果物化视图定义有聚合函数或 `UNION ALL` 算子时，无需手动指定对应依赖列。

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP2 版本开始支持在 `REFRESH` 子句中通过 `REFRESH ... PARALLEL n` 指定刷新并行度。

#### 注意

如果使用了 `NEXT` 子句，刷新计划的时间表达式必须设定在未来的时间点，否则会引发错误。
