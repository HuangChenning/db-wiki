---
title: FORMAT_CALL_STACK
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287167.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# FORMAT_CALL_STACK

`FORMAT_CALL_STACK` 函数用于格式化当前的调用堆栈。

`FORMAT_CALL_STACK` 适用于访问调用堆栈的任何存储过程或触发器，可用于调试。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法

```sql
DBMS_UTILITY.FORMAT_CALL_STACK
RETURN VARCHAR2;
```

## 返回值

返回调用堆栈，最多 2000 个字节。
