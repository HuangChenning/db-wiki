---
title: "数据类型格式化函数"
book: "常用内置函数"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/type_init.html"
tags:
  - highgo
  - highgo-v45
  - sql-built-in-functions
---

## 数据类型格式化函数

HGDB 格式化函数提供一套强大的工具用于把各种数据类型（日期/时间、整数、浮点、数字）转换成格式化的字符串以及反过来从格式化的字符串转换成指定的数据类型。下表列出了这些函数，这些函数都遵循一个公共的调用规范：第一个参数是待格式化的值，而第二个是一个定义输出或输入格式的模板。

| 函数 | 返回类型 | 描述 | 例子 |
| --- | --- | --- | --- |
| to\_char(timestamp,   text) | text | 把时间戳转成字符串 | to\_char(current\_timestamp,’HH12:MI:SS’) |
| to\_char(interval,text) | text | 把间隔转成字符串 | to\_char(interval’15h 2m 12s’,’HH24:MI:SS’) |
| to\_char(int,text) | text | 把整数转成字符串 | to\_char(125,’999’) |
| to\_char(double precision,text) | text | 把实数或双精度转成字符串 | to\_char(125.8::real,’999D9’) |
| to\_char(numeric,text) | text | 把数组转成字符串 | to\_char(-125.8,’999D99S’) |
| to\_date(text,text) | date | 把字符串转成日期 | to\_date(‘05 Dec 2000’,’DD Mon YYYY’) |
| to\_number(text,text) | numeric | 把字符串转成数字 | to\_number(‘12,454.8-‘,’99G999D9S’) |
| to\_timestamp(text,   text) | timestamp with time zone | 把字符串转成时间戳 | to\_timestamp(‘05 Dec 2000’,’DD Mon YYYY’) |