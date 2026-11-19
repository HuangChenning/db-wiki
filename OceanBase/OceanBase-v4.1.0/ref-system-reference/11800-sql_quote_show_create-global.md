---
title: sql_quote_show_create
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183514.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# sql_quote_show_create

sql_quote_show_create 用于设置是否为 `SHOW CREATE TABLE` 和 `SHOW CREATE DATABASE` 语句启动引用标识符。

| **属性** |                                                    **描述**                                                     |
|--------|---------------------------------------------------------------------------------------------------------------|
| 参数类型   | bool                       |
| 默认值    | true                       |
| 取值范围   | <li> true：启用   <li> false：不启用    |
| 生效范围   | <li> GLOBAL   <li> SESSION       |
