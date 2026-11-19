---
title: "V$OB_TENANT_MEMORY"
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699245.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# V$OB_TENANT_MEMORY

V$OB_TENANT_MEMORY 
=======================================

功能 
-----------------------

展示当前 OBServer 节点进程中每个租户的内存使用状况。

字段说明 
-------------------------



|   字段名称    |     类型      | 是否可以为 NULL |    描述     |
|-----------|-------------|------------|-----------|
| TENANT_ID | bigint(20)  | NO         | 租户 ID     |
| SVR_IP    | varchar(46) | NO         | 服务器 IP 地址 |
| SVR_PORT  | bigint(20)  | NO         | 服务器端口号    |
| HOLD      | bigint(20)  | NO         | 租户已使用内存   |
| FREE      | bigint(21)  | NO         | 租户剩余内存    |
