---
title: enable_asan_for_memory_context
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702130.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# enable_asan_for_memory_context

`enable_asan_for_memory_context` 在使用 ob_asan 时，用于设置是否允许 ObAsanAllocator（默认 ObAllocator 作为 MemoryContext 的分配器）。

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 布尔类型 |
| 默认值 | False |
| 取值范围 | <li>True：启用<li>False：禁用 |
| 是否重启 OBServer 节点生效 | 否 |
