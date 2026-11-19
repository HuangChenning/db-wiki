---
title: ALTER TABLESPACE
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480948.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ALTER TABLESPACE

## 描述

该语句用于修改表空间的属性。

## 语法

```sql
ALTER TABLESPACE tablespace_name
  [ ENCRYPTION USING 'algorithm' ]

algorithm:
  'AES-256' | 'AES-128' | 'AES-192' | 'SM4-CBC'
```

## 参数解释

| **参数**        | **描述**                                           |
|---------------|--------------------------------------------------|
| tablespace_name | 要修改的表空间的名称                                  |
| algorithm     | 加密算法的名称，支持 'AES-256'、'AES-128'、'AES-192' 和 'SM4-CBC' |

## 示例

```sql
-- 创建一个表空间 users
obclient> CREATE TABLESPACE users;

-- 修改表空间加密算法
obclient> ALTER TABLESPACE users ENCRYPTION USING 'AES-256';
```

## 相关文档

- [CREATE TABLESPACE](2600.create-tablespace-of-oracle-mode.md)
- [DROP TABLESPACE](4100.drop-tablespace-of-oracle-mode.md)
