---
title: SET_IDENTIFIER
book: "PL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006306462.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# SET_IDENTIFIER

`SET_IDENTIFIER` 过程用于在会话中设置客户端 ID。

## 语法

```sql
DBMS_SESSION.SET_IDENTIFIER (
client_id VARCHAR(65535));
```

## 参数说明

`client_id` 指定当前数据库会话的应用程序标识符（区分大小写）。此参数的最大字节数为 64 字节。如果输入的数值超过 64 个字节，则会截断多出的字节。

## 使用说明

`SET_IDENTIFIER` 过程将会话的客户端 ID 设置为指定值。

`SET_IDENTIFIER` 过程可由 `PUBLIC` 执行。

## 示例

```sql
obclient> BEGIN
    DBMS_SESSION.SET_IDENTIFIER('1234');
END;
```
