---
title: CLOSE_CURSOR
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286897.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# CLOSE_CURSOR

`CLOSE_CURSOR` 存储过程用于关闭指定的游标。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法

```sql
DBMS_SQL.CLOSE_CURSOR(cursor_id    IN INTEGER);
```

## 参数

|  **参数**   |    **解释**    |
|-----------|--------------|
| cursor_id | 要关闭的游标 ID 号。 |
