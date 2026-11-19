---
title: information_schema.GLOBAL_VARIABLES
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699256.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.GLOBAL_VARIABLES

information_schema.GLOBAL_VARIABLES
========================================================


功能
-----------

记录全局变量信息。

字段说明
-------------

|    **字段名称**    |     **类型**     | **是否可以为 NULL** | **描述** |
|----------------|----------------|----------------|--------|
| VARIABLE_NAME  | varchar(128)   | NO             | 变量名    |
| VARIABLE_VALUE | varchar(65536) | YES            | 变量值    |
