---
title: DROP SEQUENCE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701422.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DROP SEQUENCE

## 描述

该语句用来删除序列。

## 格式

```sql
DROP SEQUENCE [schema. ] sequence_name；
```

## 参数解释

|      参数       |                            描述                             |
|---------------|-----------------------------------------------------------|
| schema.       | 指定包含序列的用户。 如果不指定 `Schema` ，则默认为当前登录用户的序列。 |
| sequence_name | 指定要删除的序列名称。                                               |

## 示例

删除序列 `seq1`。

```sql
obclient> DROP SEQUENCE seq1;
Query OK, 0 rows affected
```
