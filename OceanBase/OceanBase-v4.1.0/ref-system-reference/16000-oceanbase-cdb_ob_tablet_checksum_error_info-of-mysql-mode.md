---
title: oceanbase.CDB_OB_TABLET_CHECKSUM_ERROR_INFO
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699313.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.CDB_OB_TABLET_CHECKSUM_ERROR_INFO

## 功能
展示 TABLET 副本之间出现的数据不一致的信息。
## 字段说明
| **字段名称** | **类型** | **是否可以为 NULL** | **描述** |
| --- | --- | --- | --- |
| TENANT_ID | bigint(20) | NO | 租户 ID |
| TABLET_ID | bigint(20) | NO | 出现校验和不一致的 TABLET ID |
