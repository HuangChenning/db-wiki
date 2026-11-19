---
title: "内存相关的视图"
book: "系统原理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150081.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 内存相关的视图

OceanBase 数据库支持通过视图来查看内存的使用情况。

| 视图            | 描述                              |
|-----------------|-----------------------------------|
| GV\$OB_MEMORY   | OBServer 节点内存标签的统计信息。 |
| GV\$OB_MEMSTORE | MemStore 统计信息。               |
| GV\$OB_KVCACHE  | Kvcache 统计信息。                |
