---
title: "字符连接运算符"
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699584.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# 字符连接运算符

OceanBase 数据库支持字符连接运算符。

OceanBase 数据库当前版本所支持的字符连接运算符的详细信息如下表所示。

| 运算符  | 操作数 |  含义   |
|------|-----|-------|
| `||` | 二元  | 连接字符串 |

`||` 可以作为逻辑或运算符，由 `sql_mode` 进行控制：

* 当 `sql_mode` 包含 `PIPES_AS_CONCAT` 时，`||` 为字符连接运算符。

* 当 `sql_mode` 不包含 `PIPES_AS_CONCAT` 时，`||` 为逻辑或运算符。
