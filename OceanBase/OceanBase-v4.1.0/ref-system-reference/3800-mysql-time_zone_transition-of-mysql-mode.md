---
title: mysql.time_zone_transition
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702030.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# mysql.time_zone_transition

mysql.time_zone_transition
===============================================

功能
-----------

展示时区转换信息的系统视图。

字段说明
-------------

|      **字段名称**      |   **类型**   | **是否可以为 NULL** |  **描述**   |
|--------------------|------------|----------------|-----------|
| Time_zone_id       | bigint(20) | NO             | 时区 ID     |
| Transition_time    | bigint(20) | NO             | 时区转换时间    |
| Transition_type_id | bigint(20) | NO             | 时区转换类型 ID |
