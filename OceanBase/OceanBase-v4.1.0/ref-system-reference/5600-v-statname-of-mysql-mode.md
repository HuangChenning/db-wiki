---
title: "V$STATNAME"
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701987.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# V$STATNAME

V$STATNAME
===============================

功能
-----------

展示所有统计事件的相关定义。

字段说明
-------------

|   **字段名称**   |   **类型**    | **是否可以为 NULL** |   **描述**    |
|--------------|-------------|----------------|-------------|
| CON_ID       | bigint(20)  | NO             | 租户的 ID      |
| STAT_ID      | bigint(20)  | NO             | 统计事件的 ID    |
| STATISTICS#  | bigint(20)  | NO             | 统计事件的下标     |
| NAME         | varchar(64) | NO             | 统计事件的名称     |
| DISPLAY_NAME | varchar(64) | NO             | 统计事件的别名     |
| CLASS        | bigint(20)  | NO             | 统计事件所属类型别名称 |
