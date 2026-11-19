---
title: PROBE_VERSION
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287129.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# PROBE_VERSION

`PROBE_VERSION` 程序用于返回服务器上 `DBMS_DEBUG` 的版本号。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法

```sql
DBMS_DEBUG.PROBE_VERSION (
major out BINARY_INTEGER,
minor out BINARY_INTEGER);
```

## 参数解释

| **参数** |        **解释**        |
|--------|----------------------|
| major  | 主要版本号。               |
| minor  | 次要版本号（随着功能的增加而迭代版本）。 |
