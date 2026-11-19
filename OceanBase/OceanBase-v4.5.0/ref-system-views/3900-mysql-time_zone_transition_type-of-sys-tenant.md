---
title: mysql.time_zone_transition_type
book: "系统视图"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004477455.html"
tags:
  - oceanbase
  - distributed
  - ref-system-views
---

# mysql.time_zone_transition_type

<main id="notice" type='explain'>
<h4>说明</h4>
<p>该视图从 V1.4 版本开始引入。</p>
</main>

## 功能描述

展示时区转换类型（SYSTEM_VIEW）。

## 字段说明

|      **字段名称**      |   **类型**   | **是否可以为 NULL** |  **描述**   |
|--------------------|------------|----------------|-----------|
| Time_zone_id       | bigint(20) | NO             | 时区 ID     |
| Transition_type_id | bigint(20) | NO             | 时区转换类型 ID |
| Offset             | bigint(20) | NO             | 时区偏移      |
| Is_DST             | bigint(20) | NO             | 是否为夏令时    |
| Abbreviation       | varchar(8) | NO             | 缩写        |
