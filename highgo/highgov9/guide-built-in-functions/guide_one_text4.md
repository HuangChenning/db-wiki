---
title: "聚集函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_one_text4.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 聚集函数

和大多数其他关系数据库产品一样，HGDB 支持聚集函数。一个聚集函数从多个输入行中计算出一个结果。

| 函数 | 描述 | 例子 |
| --- | --- | --- |
| count | 计数 | SELECT count(id) FROM(values(3),(1),(2)) AS t(id); |
| sum | 求和 | SELECT sum(id) FROM(values(3),(1),(2)) AS t(id); |
| avg | 均值 | SELECT avg(id) FROM(values(3),(1),(2)) AS t(id); |
| max | 最大值 | SELECT max(id) FROM(values(3),(1),(2)) AS t(id); |
| min | 最小值 | SELECT min(id) FROM(values(3),(1),(2)) AS t(id); |