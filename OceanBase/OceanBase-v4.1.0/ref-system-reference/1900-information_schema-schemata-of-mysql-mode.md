---
title: information_schema.SCHEMATA
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702012.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.SCHEMATA

information_schema.SCHEMATA 
==========================================

功能 
-----------

展示数据库元信息。

字段说明 
-------------



|          **字段名称**          |    **类型**    | **是否可以为 NULL** | **描述**  |
|----------------------------|--------------|----------------|---------|
| CATALOG_NAME               | varchar(3)   | NO             | 固定值 def |
| SCHEMA_NAME                | varchar(128) | NO             | 数据库名    |
| DEFAULT_CHARACTER_SET_NAME | varchar(7)   | NO             | 默认字符集   |
| DEFAULT_COLLATION_NAME     | varchar(18)  | NO             | 默认比对规则  |
| SQL_PATH                   | null         | NO             | NULL    |
| DEFAULT_ENCRYPTION         | varchar(2)   | NO   | 默认是否加密    |
