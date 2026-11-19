---
title: "数值比较规则"
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504028.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# 数值比较规则

数值数据包括定点数、浮点数和零。本节主要介绍数值数据的比较规则。

OceanBase 数据库的数值数据比较规则如下：

* 较大的值大于较小的值。例如：`5.5 > 2.1`。

* 负数均小于零。例如：`-3 < 0；-200 < -1`。

* 正数均大于零。例如： `20 > 0；100 > 1`。

有关数值数据比较规则的更多信息，请参见 [数值类型的优先级](../100.built-in-data-types-of-oracle-mode/300.numeric-data-type-of-oracle-mode/500.numeric-priority-of-oracle-mode.md)。
