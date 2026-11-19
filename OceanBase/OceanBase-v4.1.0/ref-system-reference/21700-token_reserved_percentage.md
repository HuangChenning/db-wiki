---
title: token_reserved_percentage
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702113.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# token_reserved_percentage

token_reserved_percentage 在控制租户 CPU 调度中，用于设置每次预留多少比例的空闲 token 数给租户。


|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 双精度浮点数     |
| 默认值              | 30         |
| 取值范围             | \[0, 100\] |
| 是否重启 OBServer 节点生效 | 否          |
