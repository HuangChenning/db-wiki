---
title: oceanbase.CDB_OB_TABLEGROUP_TABLES
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699285.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.CDB_OB_TABLEGROUP_TABLES

oceanbase.CDB_OB_TABLEGROUP_TABLES 
=======================================================


功能 
-------------------

系统租户下展示所有租户的 TABLEGROUP、TABLE 关联关系。不展示不在 TABLEGROUP 中的 TABLE。

字段说明 
----------------------



|      字段名称       |      类型       | 是否可以为 NULL |      描述       |
|-----------------|---------------|------------|---------------|
| TENANT_ID       | bigint(20)    | NO         | 租户 ID         |
| TABLEGROUP_NAME | VARCHAR2(128) | NO         | 表组名           |
| OWNER           | VARCHAR2(128) | NO         | TABLE 所属的数据库名 |
| TABLE_NAME      | VARCHAR2(256) | NO         | TABLE 名       |
