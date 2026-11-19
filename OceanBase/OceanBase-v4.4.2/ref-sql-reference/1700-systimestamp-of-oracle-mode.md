---
title: SYSTIMESTAMP
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288526.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SYSTIMESTAMP

## 描述

该函数返回系统当前日期和时间，返回值的秒的小数位包含 `6` 位精度，且包含当前时区信息。

  <main id="notice" type='notice'>
    <h4>注意</h4>
    <p>该函数不依赖于当前会话时区，而是依赖于当前数据库服务器所在操作系统的时区。</p>
  </main>

## 语法

```sql
SYSTIMESTAMP
```

## 返回类型

返回 `TIMESTAMP WITH TIME ZONE` 数据类型。

## 示例

返回系统当前日期且包含当前时区信息。

```sql
obclient> SELECT SYSTIMESTAMP FROM DUAL;
+-------------------------------------+
| SYSTIMESTAMP                        |
+-------------------------------------+
| 18-NOV-21 10.32.27.176575 AM +08:00 |
+-------------------------------------+
1 row in set
```
