---
title: "使用数据编码和压缩"
book: "系统管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150262.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 使用数据编码和压缩

#### 说明

由于 zlib 不同小版本的压缩算法可能存在对同一数据进行压缩后，出现压缩结果不一致的情况，为了避免 OceanBase 数据库在升级过程中出现无法恢复副本数据的问题，从 V4.2.2 版本开始，OceanBase 数据库不再支持 `zlib_1.0` 压缩算法。

#### 说明

如果希望尽快完成数据的重写，可以将 `progressive_merge_num` 的值设置为 `1` 后，手动发起一次合并，手动发起合并的操作请参见 [手动触发合并](400-manually-trigger-a-merge.md)。
