---
title: "单表查询"
book: "应用开发"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577771.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 单表查询

#### 注意

`WHERE` 和 `HAVING` 的区别是，`WHERE` 是在分组前对数据进行筛选，而 `HAVING` 是在分组后的结果里进行筛选，最后返回整个 SQL 的查询结果。

#### 说明

大于等于（\\=）和小于等于（\\=）与之类似。

#### 说明

OceanBase 数据库 Oracle 模式中满足以下条件，会将 `like` 改成 `=` 比较：

- `pattern` 不包含 `%` 或 `_` 通配符，没有 `escape`。
- 字段类型不是 `LOB`。Oracle 模式下 `LOB` 类型不支持 `=` 比较，因此不可转换。
- `pattern`不是固定长度的 `char` 或 `nchar` 类型。

#### 注意

当数据库字集为 ASCII 时一个汉字需要两个 `_`；当字符集为 GBK 时只需要一个 `_`。

#### 注意

区间查询的两个临界值不要调换位置，只能是大于等于左边的值，并且小于等于右边的值。

#### 注意

- `[NOT] IN` 集合中的值类型必须一致或相互兼容。
- `[NOT] IN` 集合中的值不支持通配符。
