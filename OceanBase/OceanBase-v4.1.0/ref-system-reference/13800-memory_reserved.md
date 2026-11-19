---
title: memory_reserved
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699329.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# memory_reserved

`memory_reserved` 用于设置系统底层模块预留的内存容量大小，为了保障一些基础模块能够正常运行，一定会多预留 `memory_reserved` 以供使用。

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 容量单位       |
| 默认值              | 500M       |
| 取值范围             | \[10M, +∞) |
| 是否重启 OBServer 节点生效 | 否          |
