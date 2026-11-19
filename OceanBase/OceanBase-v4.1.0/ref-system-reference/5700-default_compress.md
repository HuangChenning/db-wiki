---
title: default_compress
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700907.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# default_compress

default_compress 
=====================================

default_compress 用于设置在 Oracle 模式下，建表时使用的默认压缩策略。


|      **属性**      |                                  **描述**                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型             | 字符串类型                                                                    |
| 默认值              | ARCHIVE                                                                  |
| 取值范围             | <li> NOCOMPRESS   <li> BASIC   <li> OLTP   <li> QUERY   <li> ARCHIVE    |
| 是否重启 OBServer 节点生效 | 否                                                                        |
