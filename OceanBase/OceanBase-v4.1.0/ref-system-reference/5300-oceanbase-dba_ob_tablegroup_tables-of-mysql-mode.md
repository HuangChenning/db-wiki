---
title: oceanbase.DBA_OB_TABLEGROUP_TABLES
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699265.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.DBA_OB_TABLEGROUP_TABLES

oceanbase.DBA_OB_TABLEGROUP_TABLES 
=======================================================


功能 
-------------------

展示 TABLEGROUP、TABLE 关联关系。不展示不在 TABLEGROUP 中的 TABLE。

字段说明 
----------------------



|      字段名称       |      类型      | 是否可以为 NULL |      描述       |
|-----------------|--------------|------------|---------------|
| TABLEGROUP_NAME | varchar(128) | NO         | 表组名           |
| OWNER           | varchar(128) | NO         | TABLE 所属的数据库名 |
| TABLE_NAME      | varchar(256) | NO         | TABLE 名       |
