---
title: "创建动态分区表"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578253.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建动态分区表

#### 说明

- 需要预创建多个分区时，分区边界的间隔为 `TIME_UNIT`。
- 首个预创建的分区边界为现存最大分区边界按 `TIME_UNIT` 向上取整。

#### 说明

建表后预创建分区和删除过期分区的动作不会立刻执行，需要等待下一次动态分区管理任务自动调度，或者手动调度一次动态分区管理任务。详细介绍，参见 [动态分区管理任务](500-dynamic-partition-management-task-of-oracle-mode.md)。
