---
title: "文件外部表"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077311.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 文件外部表

#### 注意

一旦使用手动映射，所有列都必须显式定义映射，默认顺序映射将失效。

#### 注意

- 在使用 `sfile://` 时，系统会对文件大小进行一致性校验。如果同一个逻辑路径下的文件在 OBServer 节点上的大小不一致，系统将报错 `OB_INVALID_EXTERNAL_FILE`，以避免因数据不一致导致结果错误。
- 对于 V4.4.2 版本，从 V4.4.2 BP2 版本开始在 `CREATE EXTERNAL TABLE` 语法本地 Location 格式中加入了对 `sfile://` 协议头的支持。

#### 说明

在 OceanBase 的 MySQL 模式 下，外部表不支持使用 `ZEROFILL` 列属性。
