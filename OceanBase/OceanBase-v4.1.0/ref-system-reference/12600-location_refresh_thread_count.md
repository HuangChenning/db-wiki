---
title: location_refresh_thread_count
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700945.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# location_refresh_thread_count

`location_refresh_thread_count` 用于设置 OBServer 节点从 Root Service 中获取分区位置信息的线程数量。

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 整型        |
| 默认值              | 4         |
| 取值范围             | \[2, 64\] |
| 是否重启 OBServer 节点生效 | 否         |
