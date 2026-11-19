---
title: "日期时间格式模型"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578469.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 日期时间格式模型

#### 注意

建议您使用 4 位数的年份元素（`YYYY`），较短的年份元素会影响查询优化，因为年份只能在运行时确定。

#### 说明

日期时间函数指的是 `TO_CHAR`、`TO_DATE`、`TO_TIMESTAMP` 和 `TO_TIMESTAMP_TZ`。

#### 注意

- 表格中展示的转化要求输入的字符串日期能够与格式元素相匹配，否则会报错。
- OceanBase 数据库中默认的日期格式为 **DD-MON-RR**，如果要显示为上面的格式，可以通过执行 `ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS';` 修改当前会话的日期时间格式。
