---
title: "空间索引"
book: "系统原理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150158.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 空间索引

OceanBase 数据库支持创建常规索引的语法创建空间索引，但使用 `SPATIAL` 关键字。

创建空间索引的相关约束如下：

- 创建空间索引的列定义中必须包含 `NOT NULL` 约束。
- 在创建了索引之后，比较的时候使用列定义中的 `SRID` 所对应的坐标系。空间索引存储了几何对象的 MBR（Minimum Bounding Rectangle）构建，MBR 的比较方式也依赖于 `SRID`。
- 创建了空间索引的列最好是已经定义了 `SRID`，否则在该列上建的空间索引在查询时无法生效。

## 相关文档

有关创建空间索引的详细信息，请参见 [创建空间索引](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504585)。
