---
title: "启用和关闭并行查询"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078233.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 启用和关闭并行查询

#### 说明

如果希望在查询分区数等于 1 的情况下，能够采用 Hint 的方式进行分区内并行查询，需要对应的 DOP 值大于等于 2。 如果 DOP 值为空或者小于 2 将不启动并行查询。
