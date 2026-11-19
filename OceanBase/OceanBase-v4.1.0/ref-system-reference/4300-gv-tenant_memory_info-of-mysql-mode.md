---
title: "GV$OB_TENANT_MEMORY"
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699221.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# GV$OB_TENANT_MEMORY

GV$OB_TENANT_MEMORY 
========================================


功能 
-----------------------

展示集群上每个租户的内存使用状况。

字段说明 
-------------------------



|   字段名称    |     类型      | 是否可以为 NULL |   描述    |
|-----------|-------------|------------|---------|
| TENANT_ID | bigint(20)  | NO         | 租户 ID   |
| SVR_IP    | varchar(46) | NO         | 机器的 IP  |
| SVR_PORT  | bigint(20)  | NO         | 机器端口号   |
| HOLD      | bigint(20)  | NO         | 租户已使用内存 |
| FREE      | bigint(21)  | NO         | 租户剩余内存  |
