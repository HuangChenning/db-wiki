---
title: mysql.time_zone
book: "系统视图"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284617.html"
tags:
  - oceanbase
  - distributed
  - ref-system-views
---

# mysql.time_zone

<main id="notice" type='explain'>
<h4>说明</h4>
<p>该视图从 V1.4 版本开始引入。</p>
</main>

## 功能描述

展示时区相关的信息。

## 字段说明

|     **字段名称**     |   **类型**   | **是否可以为  NULL** | **描述** |
|------------------|------------|-----------------|--------|
| Time_zone_id     | bigint(20) | NO              | 时区 ID  |
| Use_leap_seconds | varchar(8) | NO              | 是否使用闰秒 |
