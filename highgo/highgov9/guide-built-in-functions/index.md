---
title: "窗口函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/index.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 窗口函数

| 函数 | 返回类型 | 描述 |
| --- | --- | --- |
| row\_number() | bigint | 当前行在其分区中的行号， 从 1 计 |
| rank() | bigint | 带间隙的当前行排名； 与该 行的第一个同等行的 row\_number 相同 |
| dense\_rank() | bigint | 不带间隙的当前行排名； 这 个函数计数同等组 |
| percent\_rank() | double precision | 当前行的相对排名： (rank- 1) / (总行数 - 1) |
| cume\_dist() | double precision | 累积分布：(在当前行之前或者平级的分区行数) / 分区行总数 |
| ntile(num\_buckets integer) | integer | 从 1 到参数值的整数范围，尽可能等分分 区 |
| lag(valueanyelement \[, offset integer \[, defaultanyelement \]\]) | 和 value 的类型 相同 | 返回 value ，它在分区内当前 行的之前 offset 个位置的行 上计算；如果没有这样的行，返回 default 替代（必须和 value 类型 相同）。offset 和 default 都是根据当前行计 算的结果。如果忽略它们，则 offset 默认 是 1 ，default 默认是空值 |
| lead(valueanyelement \[, offset integer \[, defaultanyelement \]\]) | 和 value 类型相 同 | 返回 value ，它在分区内当前 行的之后 offset 个位置的行 上计算；如果没有这样的行，返回 default 替代（必须 和 value 类型相同）。offset 和 default 都是 根据当前行计算的结果。如 果忽略它们，则 offset 默认 是 1 ，default 默认是空值 |