---
title: AP FAQ
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577295.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# AP FAQ

#### 说明

上述代码中 `cpu_count` 表示创建租户时指定的 `min_cpu`。

#### 说明

`alter table t1 drop column group(all columns, each column);` 执行后，不用担心没有任何 Group 来承载数据，所有列会被放到一个叫做 `DEFAUTL COLUMN GROUP` 的默认 Group 中。

#### 注意

对于列存表来说，如果存在大量的更新操作，并且没有及时合并，查询性能会受到影响。因此，推荐在批量导入数据后发起一次合并操作，以获得最优的查询性能。而少量更新操作对性能影响不大。
