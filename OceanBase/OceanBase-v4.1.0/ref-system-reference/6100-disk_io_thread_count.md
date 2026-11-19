---
title: disk_io_thread_count
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700911.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# disk_io_thread_count

disk_io_thread_count 
=========================================

disk_io_thread_count 用于设置磁盘 IO 线程数。必须为偶数。


|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 整型        |
| 默认值              | 8         |
| 取值范围             | \[2, 32\] |
| 是否重启 OBServer 节点生效 | 否         |
