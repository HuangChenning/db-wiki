---
title: information_schema.CHARACTER_SETS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699247.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.CHARACTER_SETS

information_schema.CHARACTER_SETS
======================================================

功能
-----------

展示 OceanBase 数据库的字符集信息。

字段说明
-------------

|       **字段名称**       |    **类型**    | **是否可以为 NULL** | **描述**  |
|----------------------|--------------|----------------|---------|
| CHARACTER_SET_NAME   | varchar(128) | NO             | 字符集名称   |
| DEFAULT_COLLATE_NAME | varchar(128) | NO             | 字符集比对方法 |
| DESCRIPTION          | varchar(64)  | NO             | 字符集描述描述 |
| MAXLEN               | bigint(20)   | NO             | 字符集最大长度 |
