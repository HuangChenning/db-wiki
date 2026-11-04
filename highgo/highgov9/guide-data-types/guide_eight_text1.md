---
title: "布尔类型"
book: "数据类型"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_eight_text1.html"
tags:
  - highgo
  - highgo-v9
  - guide-data-types
---

## 布尔类型

HGDB 提供标准的 SQL 类型 boolean。boolean 可以有多个状态：“true（真）”、“false（假）” 和第三种状态 “ unknown（未知）”，未知状态由 SQL 空值表示。

| 名字 | 存储字节 | 描述 |
| --- | --- | --- |
| boolean | 1字节 | 状态为真或假 |

在 SQL 查询中，布尔常量可以表示为 SQL 关键字 TRUE、FALSE、NULL。但是语法分析程序不会把 NULL 自动理解为 boolean 类型，因为它可以是任何类型的，必要时可以将它显示转换为 boolean 类型：NULL::boolean。

boolean 类型的数据类型输入函数接受这些字符串表示“真”状态： `true` 、 `yes` 、 `on` 、 `1` ；接受这些表示为“假”状态： `false` 、 `no` 、 `off` 、 `0` 。这些字符串的唯一前缀也可以接受，例如 `t` 或 `n` 。字符串前端或尾部的空格将被忽略，并且大小写不敏感。

boolean 类型的数据类型输出函数总是发出 `t` 或 `f` 。