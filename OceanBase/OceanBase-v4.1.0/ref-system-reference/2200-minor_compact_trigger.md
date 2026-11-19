---
title: minor_compact_trigger
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700966.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# minor_compact_trigger

minor_compact_trigger 用于控制分层转储触发向下一层下压的阈值。当该层的 Mini SSTable 总数达到设定的阈值时，所有 SSTable 都会被下压到下一层，组成新的 Minor SSTable。


|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 整型        |
| 默认值              | 2         |
| 取值范围             | \[0, 16\] |
| 是否重启 OBServer 节点生效 | 否         |



当 minor_compact_trigger 的值为 0 时，OceanBase 数据库仍会进行分层转储，即此时 MemTable 仍然会 Dump 为 Mini SSTable，但后续会立即调度下压合并生成新的 Minor SSTable，替代原有的 Minor SSTable。
