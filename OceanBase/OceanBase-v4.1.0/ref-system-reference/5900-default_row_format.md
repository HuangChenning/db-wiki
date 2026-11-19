---
title: default_row_format
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700909.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# default_row_format

default_row_format 
=======================================

default_row_format 用于设置在 MySQL 模式下，建表时使用的默认行格式。


|      **属性**      |               **描述**                |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型             | 字符串                                 |
| 默认值              | DYNAMIC                             |
| 取值范围             | <li> REDUNDANT   <li> COMPACT   <li> DYNAMIC   <li> COMPRESSED    |
| 是否重启 OBServer 节点生效 | 否                                   |
