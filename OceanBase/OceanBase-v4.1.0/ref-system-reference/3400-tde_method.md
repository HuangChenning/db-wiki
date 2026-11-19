---
title: tde_method
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700977.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# tde_method

tde_method 
===============================

tde_method 用于设置透明表空间加密的方式。


|      **属性**      |             **描述**             |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型             | 字符串类型                          |
| 默认值              | none                           |
| 取值范围             | <li> none：表示无法使用透明表空间加密   <li> internal：表示透明加密采用内部表的形式   <li> bkmi：表示透明加密采用外部 bkmi 的形式    |
| 是否重启 OBServer 节点生效 | 否                              |
