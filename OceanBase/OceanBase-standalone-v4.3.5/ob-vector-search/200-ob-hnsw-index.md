---
title: "HNSW 系列索引"
book: "向量搜索"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005411366.html"
tags:
  - oceanbase
  - standalone
  - ob-vector-search
---

# HNSW 系列索引

#### 注意

HNSW_BQ 索引从 V4.3.5 BP2 版本开始支持。

#### 注意

该参数从 V4.3.5 BP3 版本开始支持，仅在创建 HNSW_BQ 索引时可指定。

#### 注意

如果集群是从旧版本升级到 V4.3.5 BP3 版本，则该参数默认值为 fp32。

#### 注意

该参数从 V4.3.5 BP3 版本开始支持，仅在创建 HNSW_BQ 索引时可指定。

#### 注意

该参数从 V4.3.5 BP3 版本开始支持，仅在创建 HNSW_BQ 索引时可指定。

#### 注意

如果集群是从 V4.3.5 BP2 版本升级到 V4.3.5 BP3 版本，则该参数默认值为 false。

#### 注意

该参数从 V4.3.5 BP3 版本开始支持，仅在创建 HNSW_BQ 索引时可指定。

#### 注意

从 V4.3.5 BP5 版本开始支持使用 `PARAMETERS(similarity=$value)` 子句指定相似度阈值搜索。
