---
title: location_fetch_concurrency
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700944.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# location_fetch_concurrency

location_fetch_concurrency 用于设置单机 location_cache 刷新的最大并发数。


|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | 整型          |
| 默认值              | 20          |
| 取值范围             | \[1, 1000\] |
| 是否重启 OBServer 节点生效 | 否           |
