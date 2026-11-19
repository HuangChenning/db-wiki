---
title: "配置租户内资源隔离"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578204.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 配置租户内资源隔离

#### 说明

如果您对 IOPS 的实际性能精度要求不高，可以不进行磁盘性能校准。如果您对 IOPS 的实际性能精度要求高，则需要进行磁盘性能校准。

#### 说明

如果您在创建租户所使用的 Unit 规格时，已将 `MAX_IOPS` 和 `MIN_IOPS` 设置为 16 KB 读对应的 IOPS 值，或者，您不需要控制 IOPS 的资源隔离，请忽略本步骤。

#### 注意

执行 SQL 语句时，并不需要语句中必须包含 `sys.t.`，只需要 `c3` 最终被解析为 `sys.t.c3`，则该 SQL 语句就会绑定到名为 `big_group` 的资源组上执行。例如：`SELECT * FROM sys.t WHERE c3 = 1;`。

#### 说明

通过 Hint 方式指定资源组后，如果资源组不存在，则语句执行时使用默认的资源组 `OTHER_GROUPS`。

#### 说明

如果不需要对资源进行限制，可以使用 `ALTER SYSTEM SET resource_manager_plan = '';` 语句禁用所有资源计划。
