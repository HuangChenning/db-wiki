---
title: log_disk_utilization_threshold
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700961.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# log_disk_utilization_threshold

`log_disk_utilization_threshold` 用于设置租户日志盘利用率阈值，当租户日志盘使用量超过租户日志盘空间总量乘以该值时，进行日志文件重用。

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 80         |
| 取值范围             | \[10, 99\] |
| 是否重启 OBServer 节点生效 | 否          |

`log_disk_utilization_threshold` 的取值应该小于 `log_disk_utilization_limit_threshold` 的取值。有关 `log_disk_utilization_limit_threshold` 的详细介绍，请参见 [log_disk_utilization_limit_threshold](../400.tenant-level-configuration-items/1600.log_disk_utilization_limit_threshold.md)。
