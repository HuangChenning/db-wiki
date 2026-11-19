---
title: location_cache_expire_time
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002178116.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# location_cache_expire_time

location_cache_expire_time 
===============================================

location_cache_expire_time 用于设置分区位置缓存中分区位置信息的过期时长。不建议修改。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 时间类型      |
| 默认值              | 600s      |
| 取值范围             | \[1s, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
