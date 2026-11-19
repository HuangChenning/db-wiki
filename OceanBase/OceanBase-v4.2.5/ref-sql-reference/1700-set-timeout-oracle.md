---
title: SET_TIMEOUT
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503838.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SET_TIMEOUT

`SET_TIMEOUT` 函数用于设置超时时间并返回新的超时值。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法 

```sql
DBMS_DEBUG.SET_TIMEOUT (
   timeout BINARY_INTEGER) 
  RETURN BINARY_INTEGER;
```



## 参数解释 



| **参数**  |       **解释**        |
|---------|---------------------|
| timeout | 目标会话和调试会话之间通信的超时时间。 |
