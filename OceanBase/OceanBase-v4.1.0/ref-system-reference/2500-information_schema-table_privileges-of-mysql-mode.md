---
title: information_schema.TABLE_PRIVILEGES
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702018.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.TABLE_PRIVILEGES

information_schema.TABLE_PRIVILEGES
========================================================

功能
-----------

展示表权限信息。

字段说明
-------------

|    **字段名称**    |    **类型**     | **是否可以为 NULL** | **描述** |
|----------------|---------------|----------------|--------|
| GRANTEE        | varchar(81)   | NO             | 权限描述   |
| TABLE_CATALOG  | varchar(4096) | NO             | 表目录    |
| TABLE_SCHEMA   | varchar(128)  | NO             | 数据库名   |
| TABLE_NAME     | varchar(64)   | NO             | 表名     |
| PRIVILEGE_TYPE | varchar(64)   | NO             | 权限类型   |
| IS_GRANTABLE   | varchar(3)    | NO             | 是否授权   |
