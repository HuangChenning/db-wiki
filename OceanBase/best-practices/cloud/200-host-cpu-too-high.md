---
title: "主机 CPU 使用率过高"
book: "云"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003471277.html"
tags:
  - oceanbase
  - best-practices
  - cloud
---

# 主机 CPU 使用率过高

#### 说明

**CPU 占比 (%)** 表示该 SQL 的总 CPU 时间占所有 SQL 总 CPU 时间的百分比。CPU 占比越大，表明其消耗的 CPU 资源越多。

#### 说明

- execute_time：计划的执行时间。
- get_plan_time：生成执行计划的时间。
- total_wait_time_micro：执行过程所有等待的总时间。

#### 注意

- 与 OBServer 有所不同，OAS 将获取执行计划的时间加入了 CPU 时间。
- 由于 SQL 解析时间通常比较短，所以没有包含在 CPU 时间内。
