---
title: DBA_OB_TABLET_TO_LS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001697516.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# DBA_OB_TABLET_TO_LS

DBA_OB_TABLET_TO_LS 
========================================


功能 
-------------------

展示本租户的所有 Tablet 列表以及 Tablet 所属的日志流信息。

字段说明 
----------------------



|   字段名称    |   类型   | 是否可以为 NULL |        描述        |
|-----------|--------|------------|------------------|
| TABLET_ID | NUMBER | NO         | TABLET ID        |
| LS_ID     | NUMBER | NO         | TABLET 所属的日志流 ID |
