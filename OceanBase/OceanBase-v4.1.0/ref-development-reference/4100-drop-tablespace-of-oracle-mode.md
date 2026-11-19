---
title: DROP TABLESPACE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701426.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DROP TABLESPACE

## 描述

该语句用来删除 TableSpace 逻辑对象，仅在 TableSpace下没有表时可以删除成功。

## 语法

```sql
DROP TABLESPACE tablespace_name;
```

## 参数解释

|       参数        |          描述           |
|-----------------|-----------------------|
| tablespace_name | 指定要删除的 TableSpace 名称。 |

## 示例

删除 TableSpace 对象 `tblspace1`。

```sql
obclient>  DROP TABLESPACE tblspace1;
Query OK, 0 rows affected
```
