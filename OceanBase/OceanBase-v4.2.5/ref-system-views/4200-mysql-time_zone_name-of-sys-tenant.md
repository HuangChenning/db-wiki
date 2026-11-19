---
title: mysql.time_zone_name
book: "系统视图"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501097.html"
tags:
  - oceanbase
  - distributed
  - ref-system-views
---

# mysql.time_zone_name

<main id="notice" type='explain'>
<h4>说明</h4>
<p>该视图从 V1.4 版本开始引入。</p>
</main>

## 功能描述

展示 timezone 名称信息（SYSTEM_VIEW）。

## 字段说明

|     字段名称     |     类型      | 是否可以为 NULL |  描述   |
|--------------|-------------|------------|-------|
| Name         | varchar(64) | NO         | 时区名称  |
| Time_zone_id | bigint(20)  | NO         | 时区 ID |
