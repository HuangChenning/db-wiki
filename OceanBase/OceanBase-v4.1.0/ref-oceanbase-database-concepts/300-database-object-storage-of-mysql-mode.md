---
title: "数据库对象存储"
book: "系统概念"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702411.html"
tags:
  - oceanbase
  - distributed
  - ref-oceanbase-database-concepts
---

# 数据库对象存储

OceanBase 数据库将一些数据库对象的数据存储在一个或者多个 SSTable 中，一个 SSTable 包含一个或多个宏块，每个宏块中包含一个或多个微块，每个微块包含一行或者多行。有些数据库对象，例如视图、虚拟表等，由于只有元数据信息，所以不会存储实际的数据。
