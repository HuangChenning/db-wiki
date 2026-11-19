---
title: "NULL 值"
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702710.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# NULL 值

`NULL` 值表示"无数据"。

`NULL` 不区分大小写。同义词是 `\N`（区分大小写）。请注意，`NULL` 值与数字 0 和空字符串 `''` 不同。

当使用 `ORDER BY` 进行排序时，对于升序排序，`NULL` 值排在其他值之前；对于降序排序，`NULL` 值排在其他值之后。
