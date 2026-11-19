---
title: information_schema.SESSION_STATUS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702013.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.SESSION_STATUS

information_schema.SESSION_STATUS 
======================================================


功能 
-----------

记录 Session 的状态信息，如当前活跃连接数，数据库活跃时间（Uptime）等。

字段说明 
-------------



|    **字段名称**    |    **类型**     | **是否可以为 NULL** |   **描述**    |
|----------------|---------------|----------------|-------------|
| VARIABLE_NAME  | varchar(128)  | NO             | Session 状态名 |
| VARIABLE_VALUE | varchar(1024) | YES            | Session 状态值 |
