---
title: "向量搜索核心功能"
book: OceanBase AI
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077148.html"
tags:
  - oceanbase
  - standalone
  - ob-vector-search
---

# 向量搜索核心功能

OceanBase 提供了存储、索引、搜索 Embedding 向量数据的能力。具体包括：

[TABLE]

## 使用限制和说明

- OceanBase 默认采用 NULL first 比较模式，所以对 NULL 值进行排序时会将其放至最前，建议查询的时候加上 `NOT NULL` 条件。
