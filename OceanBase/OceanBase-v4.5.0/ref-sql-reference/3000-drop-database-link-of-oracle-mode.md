---
title: DROP DATABASE LINK
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480951.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DROP DATABASE LINK

## 描述

删除已创建的数据库链接（即 `dblink`）。

>**说明**
>
>要删除已创建的数据库链接，您必须具有 `DROP DATABASE LINK` 系统权限。

## 语法

```sql
DROP DATABASE LINK dblink_name
```

## 参数说明

`dblink_name` 为要删除的数据库链接的名称。

## 示例

```sql
obclient> DROP DATABASE LINK ob_dblink;
```
