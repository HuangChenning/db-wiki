---
title: information_schema.GLOBAL_STATUS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699255.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.GLOBAL_STATUS

information_schema.GLOBAL_STATUS
=====================================================


功能
-----------

记录 OceanBase 数据库的全局状态信息。

字段说明
-------------

|    **字段名称**    |    **类型**     | **是否可以为 NULL** |   **描述**    |
|----------------|---------------|----------------|-------------|
| VARIABLE_NAME  | varchar(128)  | NO             | 全局状态对应的变量名称 |
| VARIABLE_VALUE | varchar(1024) | YES            | 全局状态对应的变量内容 |
