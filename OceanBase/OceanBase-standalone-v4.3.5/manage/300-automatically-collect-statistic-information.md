---
title: "自动统计信息收集"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578466.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 自动统计信息收集

#### 说明

- 对于 OceanBase 数据库 V4.3.5 版本，从 V4.3.5 BP1 版本开始维护窗口 `SATURDAY_WINDOW` 和 `SUNDAY_WINDOW` 的任务默认开始时间和最大收集时长由 **默认开始时间 6:00，最大收集时长 20 小时** 变更为 **默认开始时间为 22:00，最大收集时长 4 小时**。
- 对于 OceanBase 数据库 V4.2.5 版本，从 V4.2.5 BP2 版本开始维护窗口 `SATURDAY_WINDOW` 和 `SUNDAY_WINDOW` 的任务默认开始时间和最大收集时长由 **默认开始时间 6:00，最大收集时长 20 小时** 变更为 **默认开始时间为 22:00，最大收集时长 4 小时**。

#### 注意

在 Oracle 模式用户租户中执行以下语句时，需要使用对应的 sys 用户执行。

#### 注意

在 Oracle 模式用户租户中执行以下语句时，需要使用对应的 sys 用户执行。

#### 注意

设置各维护窗口的 `NEXT_DATE` 时，指定的日期必须与窗口名称所代表的星期一致。例如，`MONDAY_WINDOW` 的 `NEXT_DATE` 必须设置为周一的日期，`FRIDAY_WINDOW` 必须设置为周五的日期，以此类推。

#### 注意

在 Oracle 模式用户租户中执行以下语句时，需要使用对应的 sys 用户执行。
