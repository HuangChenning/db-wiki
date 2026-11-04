---
title: "时间日期函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_one_text6.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 时间日期函数

| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| age(timestamp, timestamp) | interval | 减去参数，生成一个使用年、月（而不是只用 日）的“符号 化”的结果 | age(timestamp ‘2001-04-10’,timestamp’ 1957-06-13’) | 43 年 9月 27 日 |
| age(timestamp ) | interval | 从 current\_date（在 午夜）减去 | age(timestamp ‘ 1957-06-13’) | 43 years 8 mons 3days |
| clock\_timesta mp() | timestamp withtime zone | 当前日期和时间 （在语句执行期 间变化）；见第 8.9.4 节 |  |  |
| current\_date | date | 当前日期；见第 8.9.4 节 |  |  |
| current\_time | time withtime zone | 当前时间（一天 中的时间）；见第 8.9.4 节 |  |  |
| current\_timest | timestamp | 当前日期和时间 |  |  |
| date\_part(text, timestamp) | doubleprecision | 获得子域（等价 于 extract）；见第 8.9.1 节 | date\_part(‘hour’, timestamp’2001-02-1620:38:40’) | 20 |
| date\_part(text, interval) | interval) doubleprecision | 获得子域（等价于 extract）；见第 8.9.1 节 | date\_part(‘month’, interval ‘2years 3 months’) |  |
| date\_trunc(text,timestamp) | timestamp | 截断到指定精 度；见第 8.9.2 节 | date\_trunc(‘hour’, timestamp’2001-02-1620:38:40’) | 2001-02-1620:00:00 |
| now() | timestamp withtime zone | 当前日期和时间 （当前事务的开 始）；见第 8.9.4 节 |  |  |
| to\_timestamp( doubleprecision) | timestamp withtime zone | 把 Unix 时间（从 1970-01-01 00:00:00+00 开 始的秒）转换成 timestamp | to\_timestamp(128 4352323) | 2010-09-1304:32:03+00 |
| timeofday() | text | 当前日期和时间 （像clock\_timestamp， 但是作为一个 text 字符串）； |  |  |
| make\_date(yea rint, month int, day int) | date | 从年、月、日域创 建日期 | make\_date(2013, 7, 15) | 2013-07-15 |