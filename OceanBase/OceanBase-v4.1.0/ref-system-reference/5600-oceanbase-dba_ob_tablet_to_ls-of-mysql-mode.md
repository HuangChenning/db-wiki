---
title: oceanbase.DBA_OB_TABLET_TO_LS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699268.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.DBA_OB_TABLET_TO_LS

oceanbase.DBA_OB_TABLET_TO_LS 
==================================================


功能 
-------------------

展示本租户的所有 Tablet 列表以及 Tablet 所属的日志流信息。

字段说明 
----------------------



|   字段名称    |     类型     | 是否可以为 NULL |        描述        |
|-----------|------------|------------|------------------|
| TABLET_ID | bigint(20) | NO         | TABLET ID        |
| LS_ID     | bigint(1)  | NO         | TABLET 所属的日志流 ID |
