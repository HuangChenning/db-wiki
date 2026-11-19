---
title: mysql.time_zone
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702028.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# mysql.time_zone

mysql.time_zone
====================================


功能
-----------

展示时区相关的信息。

字段说明
-------------

|     **字段名称**     |   **类型**   | **是否可以为  NULL** | **描述** |
|------------------|------------|-----------------|--------|
| Time_zone_id     | bigint(20) | NO              | 时区 ID  |
| Use_leap_seconds | varchar(8) | NO              | 是否使用闰秒 |
