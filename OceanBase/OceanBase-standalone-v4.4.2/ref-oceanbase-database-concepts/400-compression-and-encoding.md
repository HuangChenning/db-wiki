---
title: "压缩与编码"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077751.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 压缩与编码

#### 说明

由于 zlib 不同小版本的压缩算法可能存在对同一数据进行压缩后，出现压缩结果不一致的情况，为了避免 OceanBase 数据库在升级过程中出现无法恢复副本数据的问题，对于 V4.3.x 版本，从 V4.3.0 版本开始，OceanBase 数据库不再支持 `zlib_1.0` 压缩算法。
