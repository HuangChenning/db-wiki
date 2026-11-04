---
title: "枚举支持函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_one_text5.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 枚举支持函数

| 函数 | 描述 | 例子 | 例子结果 |
| --- | --- | --- | --- |
| enum\_first(anyenu m) | 返回输入枚举 类型的第一个值 | enum\_first(null::r ainbow) | bow |
| enum\_last(anyenu m) | 返回输入枚举 类型的最后一 个值 | enum\_last(null::ra inbow) | purple |
| enum\_range(anyen um) | 将输入枚举类 型的所有值作 为一个有序的 数组返回 | enum\_range(null::rainbow) | {red,orange,yellow,gr een,blue,purp |