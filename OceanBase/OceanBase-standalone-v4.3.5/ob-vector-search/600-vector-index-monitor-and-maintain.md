---
title: "索引维护"
book: "向量搜索"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005411368.html"
tags:
  - oceanbase
  - standalone
  - ob-vector-search
---

# 索引维护

#### 注意

此功能从 V4.3.5 BP3 版本开始支持，如果你的向量数据库从旧版本升级到 V4.3.5 BP3，那么你需要在升级后先手动全表重建所有向量索引，否则升级后可能无法自动执行分区重建任务。

此功能仅支持 HNSW/HNSW_SQ/HNSW_BQ 索引。
