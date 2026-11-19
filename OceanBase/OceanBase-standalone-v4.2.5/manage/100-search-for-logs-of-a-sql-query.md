---
title: "查找特定 SQL 请求的日志"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701855.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 查找特定 SQL 请求的日志

#### 注意

此处的执行 SQL 仅为示意，实际工作中 SQL 一般由应用系统执行，某些情况下出现异常，例如返回错误码，或者耗时很高。应用人员联系运维人员协助定位问题。

#### 注意

如果 `GV$OB_SQL_AUDIT` 查询不到结果，请检查是否关闭了 audit 功能, 即 `enable_sql_audit` 配置项是否设置为了 `False`。有关 `enable_sql_audit` 配置项的详细信息，参见 [enable_sql_audit](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502288)。

#### 注意

本例中通过 `GV$OB_SQL_AUDIT` 视图获取节点 IP 和 TRACE_ID，OceanBase 数据库还提供了其他多种获取方式，例如通过 ODP 的日志，例如通过等待事件相关的视图。

#### 注意

如果在 `observer.log` 中 grep 不到相关日志，可能是因为 `observer.log` 切了文件，可以 `grep YB4206019C9E-0005F55950FFAF04-0-0 observer.log.*`。
