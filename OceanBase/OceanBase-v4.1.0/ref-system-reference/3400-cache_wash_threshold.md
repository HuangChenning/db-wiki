---
title: cache_wash_threshold
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702084.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# cache_wash_threshold

cache_wash_threshold 
=========================================

cache_wash_threshold 用于设置触发缓存清理的容量阈值。如果内存空间小于指定值时，内存空间将被清理。


|      **属性**      |  **描述**  |
|------------------|----------|
| 参数类型             | 容量单位     |
| 默认值              | 4GB      |
| 取值范围             | \[0, +∞) |
| 是否重启 OBServer 节点生效 | 否        |
