---
title: merger_check_interval
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699376.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# merger_check_interval

merger_check_interval 用于设置合并状态检查线程的调度间隔。


|      **属性**      |    **描述**    |
|------------------|--------------|
| 参数类型             | 时间类型         |
| 默认值              | 10m，表示 10 分钟 |
| 取值范围             | \[10s, 60m\] |
| 是否重启 OBServer 节点生效 | 否            |
