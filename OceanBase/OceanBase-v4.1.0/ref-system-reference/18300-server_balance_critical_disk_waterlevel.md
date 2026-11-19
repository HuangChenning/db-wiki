---
title: server_balance_critical_disk_waterlevel
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699361.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# server_balance_critical_disk_waterlevel

server_balance_critical_disk_waterlevel 用于设置磁盘空间的负载均衡功能的水位线。当磁盘水位线超过阈值时，负载均衡策略将倾向于优先考虑磁盘均衡。

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 80         |
| 取值范围             | \[0, 100\] |
| 是否重启 OBServer 节点生效 | 否          |
