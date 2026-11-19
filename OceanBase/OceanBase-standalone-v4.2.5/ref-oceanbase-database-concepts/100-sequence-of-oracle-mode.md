---
title: "序列"
book: "系统原理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150127.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 序列

#### 说明

OceanBase 数据库从 V4.2.1 版本开始支持远端序列的访问功能，详细信息请参见 [通过 DBLink 访问远端数据库中的数据](../ref-database-object-management/300-access-a-remote-database-by-a-dblink-of-oracle-mode.md)。

#### 说明

- `MINVALUE` 和 `MAXVALUE` 指定最小值和最大值。
- `START WITH` 指定起始值。
- `INCREMENT BY` 指定步长，可以为负数，默认是 1。
- `CACHE` 是为了性能缓存部分序列值，在并发高的时候使用。
- `CYCLE` 指定序列值是否循环。如果循环，需要指定最大值或最小值。

#### 说明

- 出于性能考虑，OceanBase 数据库建议您使用默认的 `CACHE with NOORDER`方式。
- OceanBase 数据库中，不建议使用 `ORDER with NO CACHE`。这种模式下，每次调用 `NEXTVAL` 都会触发一次内部表 `SELECT` 与 `UPDATE` 操作，会影响数据库的性能。
- 在创建序列时，由于默认的 `CACHE` 值只有 20，需要手动声明一个比较大的值。对于单机 TPS 为 100 时，`CACHE SIZE` 建议设置为 360000。
