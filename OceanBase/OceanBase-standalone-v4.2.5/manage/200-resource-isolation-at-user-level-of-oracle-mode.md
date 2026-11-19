---
title: "配置租户内资源隔离"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702242.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 配置租户内资源隔离

#### 说明

如果您在创建租户所使用的 Unit 规格时，已将 `MAX_IOPS` 和 `MIN_IOPS` 设置为 16 KB 读对应的 IOPS 值，或者，您不需要控制 IOPS 的资源隔离，请忽略本步骤。

#### 注意

执行 SQL 语句时，并不需要语句中必须包含 `sys.t.`，只需要 `c3` 最终被解析为 `sys.t.c3`，则该 SQL 语句就会绑定到名为 `big_group` 的资源组上执行。例如：`SELECT * FROM sys.t WHERE c3 = 1;`。

#### 说明

如果不需要对资源进行限制，可以使用 `ALTER SYSTEM SET resource_manager_plan = '';` 语句禁用所有资源计划。
