---
title: oceanbase.DBA_OB_DATABASES
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700863.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.DBA_OB_DATABASES

oceanbase.DBA_OB_DATABASES 
===============================================


功能 
-------------------

展示租户的数据库元信息。

字段说明 
----------------------



|     字段名称      |      类型       | 是否可以为 NULL |             描述             |
|---------------|---------------|------------|----------------------------|
| DATABASE_NAME | varchar(128)  | NO         | 数据库名                       |
| IN_RECYCLEBIN | varchar(3)    | NO         | 数据库是否在回收站中：<li> `YES` <li> `NO` |
| COLLATION     | varchar(128)  | NO         | 数据库缺省 COLLATION            |
| READ_ONLY     | varchar(3)    | NO   | <li>YES：只读<li>NO：可读/写    |
| COMMENT       | varchar(2048) | NO         | 数据库的描述                     |
