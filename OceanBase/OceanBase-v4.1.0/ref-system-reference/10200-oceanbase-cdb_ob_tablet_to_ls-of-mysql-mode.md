---
title: oceanbase.CDB_OB_TABLET_TO_LS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699288.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.CDB_OB_TABLET_TO_LS

oceanbase.CDB_OB_TABLET_TO_LS 
==================================================


功能 
-------------------

系统租户下展示所有租户的 Tablet 列表以及 Tablet 所属的日志流信息。

字段说明 
----------------------



|   字段名称    |     类型     | 是否可以为 NULL |        描述        |
|-----------|------------|------------|------------------|
| TENANT_ID | bigint(20) | NO         | 租户 ID            |
| TABLET_ID | bigint(20) | NO         | TABLET ID        |
| LS_ID     | bigint(1)  | NO         | TABLET 所属的日志流 ID |
