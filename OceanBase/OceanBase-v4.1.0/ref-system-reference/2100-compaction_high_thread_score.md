---
title: compaction_high_thread_score
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700965.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# compaction_high_thread_score

`compaction_high_thread_score` 用于设置高优先级 compaction 的工作线程占用 CPU 时间片权重。

|      **属性**      |  **描述**  |
|------------------|----------|
| 参数类型             | 整型       |
| 默认值              | 0        |
| 取值范围             | \[0, 100\] |
| 是否重启 OBServer 节点生效 | 否        |
