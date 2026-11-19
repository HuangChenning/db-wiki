---
title: "Redo 日志"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077738.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# Redo 日志

#### 注意

集中式版仅包含一个 OBServer 节点，不涉及多副本数据一致性。

#### 说明

OceanBase 数据库在事务层支持并行回放 REDO 日志和并行提交 REDO 日志。
