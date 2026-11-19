---
title: "列 Skip Index 属性"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077651.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 列 Skip Index 属性

#### 说明

预聚合的本质在于将查询执行阶段的计算提前至数据写入阶段，通过存储预计算的结果来帮助提高查询效率。同时这种方法需要 Compaction 任务进行额外的计算，预聚合的数据也会消耗存储空间。Skip Index 存储在基线数据上，预聚合对应的 Range 内数据发生更新会导致预聚合数据失效，因此频繁的随机更新会导致 Skip Index 失效，降低优化效果。

#### 说明

- 行存表不会默认创建任何类型的 Skip Index，列存表会默认创建 `MIN_MAX` 类型的 Skip Index。
- 对于系统默认创建的 Skip Index 属性，通过 `DESC table_name` 或 `SHOW CREATE TABLE table_name` 命令查看表的列属性时，Skip Index 属性不会展示出来。
- 列存表会默认创建 `MIN_MAX` 类型的 Skip Index，而未默认创建 `SUM` 类型的 Skip Index，是因为 `SUM` 类型的 Skip Index 对旁路导入以及合并任务的性能会有一定影响，如果创建 `SUM` 类型的 Skip Index 对查询性能能带来优化，用户可以考虑显示创建 `SUM` 类型的 Skip Index 来加速查询，但是如果对查询性能没有优化，建议用户删除 `SUM` 类型的 Skip Index。
