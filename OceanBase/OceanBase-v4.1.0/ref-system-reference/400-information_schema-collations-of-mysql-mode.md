---
title: information_schema.COLLATIONS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699249.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.COLLATIONS

information_schema.COLLATIONS
==================================================

功能
-----------

展示每个字符集的比对方法信息。

字段说明
-------------

|      **字段名称**      |    **类型**    | **是否可以为 NULL** |                           |
|--------------------|--------------|----------------|---------------------------|
| COLLATION_NAME     | varchar(128) | NO             | 比对方法名称                    |
| CHARACTER_SET_NAME | varchar(128) | NO             | 和 collation 关联的字符集名称      |
| ID                 | bigint(20)   | NO             | collation 的 ID            |
| IS_DEFAULT         | varchar(4)   | NO             | collation 是否是对应字符集的默认比对方法 |
| IS_COMPILED        | varchar(4)   | NO             | 字符集是否被编译到服务器中             |
| SORTLEN            | bigint(20)   | NO             | 排序字符集需要用到的内存大小            |
