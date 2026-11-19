---
title: high_priority_net_thread_count
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700933.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# high_priority_net_thread_count

`high_priority_net_thread_count` 用于设置高优先级网络线程数。

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 0          |
| 取值范围             | \[0, 64\] |
| 是否重启 OBServer 节点生效 | 是          |

该配置项的取值为 `0` 时，表示关闭该功能。
