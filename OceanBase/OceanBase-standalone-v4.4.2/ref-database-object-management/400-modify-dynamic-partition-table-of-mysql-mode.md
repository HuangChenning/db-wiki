---
title: "修改动态分区表"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078136.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 修改动态分区表

#### 说明

`TIME_UNIT` 在建表时指定，指定后不可修改：修改已启用动态分区管理的表时，不能指定 `TIME_UNIT`；为尚未启用动态分区管理的表添加动态分区策略时，需要指定 `TIME_UNIT`。

#### 说明

- 该参数在创建动态分区表时指定，指定后不可修改。
- 修改已启用动态分区管理的表时，无需指定该参数，也不能在修改语句中指定（指定会报错）。
- 为尚未启用动态分区管理的表添加动态分区策略时，需要指定该参数。
- 分区键类型与 `TIME_UNIT` 取值的对应限制，参见 [创建动态分区表](200-create-a-dynamic-partition-table-of-mysql-mode.md)。

#### 说明

- 需要预创建多个分区时，分区边界的间隔为 `TIME_UNIT`。
- 首个预创建的分区边界为现存最大分区边界按 `TIME_UNIT` 向上取整。

#### 说明

修改动态分区管理参数后，预创建分区和删除过期分区不会立刻生效，需要等待下一次动态分区管理任务自动调度，或者手动调度一次动态分区管理任务。详细介绍，参见 [动态分区管理任务](500-dynamic-partition-management-task-of-mysql-mode.md)。

#### 说明

- 为尚未启用动态分区管理的表添加动态分区策略时，需要指定 `TIME_UNIT`。
- 分区键为时间类型时，`TIME_ZONE` 的默认值为 `default`，`BIGINT_PRECISION` 的默认值为 `none`，可以省略。
