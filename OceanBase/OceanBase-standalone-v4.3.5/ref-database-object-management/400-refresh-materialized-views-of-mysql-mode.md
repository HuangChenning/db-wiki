---
title: "刷新物化视图"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578268.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 刷新物化视图

#### 说明

刷新物化视图也会自动更新其所有索引。

#### 注意

- 由于 `REFRESH FAST` 方法利用物化视图日志中的记录信息来确定需要增量刷新的内容，因此在使用增量刷新刷新物化视图时，需要在创建物化视图之前就创建基表的物化视图日志（mlog）。
- 增量刷新物化视图中使用的列都必须在 mlog 里。

有关创建物化视图日志的信息，请参见 [物化视图日志](200-materialized-views-log-of-mysql-mode.md)。对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始支持物化视图日志自动管理功能。如果开启自动管理 mlog，那么在创建增量刷新物化视图前，用户无需创建基表的 mlog，OceanBase 数据库会自动创建对应的 mlog 或更新已存在的 mlog 表定义使其包含新建物化视图依赖的列。详细信息，参见 [物化视图日志自动管理](250-automatic-management-materialized-views-log-of-mysql-mode.md)。

#### 说明

由于嵌套物化视图不支持实时物化视图，所以在 `FROM` 表为物化视图时，无法使用实时物化视图。

#### 说明

对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始支持 `MAX` 和 `MIN` 聚合增量刷新。

#### 说明

对于 OceanBase 数据库 V4.3.5 版本，从 V4.3.5 BP5 版本开始 `MIN`/`MAX` 聚合函数参数支持非基本列，`GROUP BY` 列中支持使用非基本列。

#### 说明

- 对于 OceanBase 数据库 V4.3.5 版本，物化视图增量刷新多表连接从 V4.3.5 BP3 版本开始支持外连接（`LEFT JOIN`/`RIGHT JOIN`）。
- 外连接使用限制：连接树需要是等价于 `INNER JOIN` 在先，`LEFT JOIN` 在后的左深连接树。

#### 注意

对于 OceanBase 数据库 V4.3.5 版本：

- 在 V4.3.5 BP5 之前版本 `FROM` 表均需存在主键，且主键在 `SELECT` 中输出。
- 从 V4.3.5 BP5 版本开始删除对多表连接增量刷新物化视图要求基表上有主键的要求。

#### 说明

- 为了使简单连接物化视图在增量刷新和实时物化视图中获得较好的性能，推荐按照以下方式为物化视图及其依赖基表创建索引：
  1.  为每张表的连接键创建索引，用于提升增量更新和实时物化视图中表的连接性能。
  2.  为物化视图中各基表主键列创建索引。
- 随着物化视图中 `JOIN` 表数量的增加，物化视图的增量刷新性能和实时物化视图查询性能通常会有所下降。

#### 说明

对于 V4.3.5 版本，从 V4.3.5 BP5 版本开始支持带有外连接的聚合物化视图的增量刷新。

#### 说明

对于 OceanBase 数据库 V4.3.5 版本，变量 `mview_refresh_dop` 从 V4.3.5 BP1 版本开始引入。

#### 注意

设置 Global 级别的变量对当前 Session 无效，需要重新登录建立新的 Session 才会生效。

#### 说明

视图 `DBA_MVIEWS` 查看物化视图并行度只能查看针对物化视图指定的的并行度。

- 字段 `REFRESH_DOP` 为非 0 时，物化视图后台刷新任务将使用 `REFRESH_DOP` 对应的并行度。
- 当 `REFRESH_DOP` 为 0 时，将使用设置 Global（全局）级别的 `mview_refresh_dop` 的值。

#### 说明

物化视图的所有者和租户管理员用户才可以执行刷新操作。

#### 注意

如果未显式指定并行度，且 `mview_refresh_dop` 变量为 0 或 1 时，不开启并行刷新。

#### 说明

可以通过视图 `DBA_SCHEDULER_JOBS` 查看物化视图后台刷新的任务情况。更多查看物化视图信息，参见 [查询物化视图](600-view-materialized-views-of-mysql-mode.md)。

#### 说明

下述并行度优先级依次降低。

#### 注意

如果创建物化视图时未显式指定并行度，且 `mview_refresh_dop` 变量为 0 或 1 时，后台刷新任务不开启并行刷新。

#### 说明

对于 OceanBase 数据库 V4.3.5 版本，从 V4.3.5 BP5 版本开始支持基于无主键的物化视图创建嵌套物化视图。

#### 注意

由于 `mv1` 经历过全量刷新，因此直接对 `mv2` 进行增量刷新会报错，必须先进行一次全量刷新。

#### 说明

对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始支持物化视图日志自动管理功能。如果开启自动管理 mlog，那么在创建实时物化视图前，用户无需创建基表的 mlog，OceanBase 数据库会自动创建对应的 mlog 或更新已存在的 mlog 表定义使其包含新建物化视图依赖的列。详细信息，参见 [物化视图日志自动管理](250-automatic-management-materialized-views-log-of-mysql-mode.md)。
