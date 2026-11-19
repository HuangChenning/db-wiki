---
title: CLEAR RESTORE SOURCE
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503134.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# CLEAR RESTORE SOURCE

## 描述

该语句用于撤销 `ADD RESTORE SOURCE` 语句加载的路径。

## 权限要求

执行该语句需要当前用户拥有 `ALTER SYSTEM` 权限。

## 语法

```sql
ALTER SYSTEM CLEAR RESTORE SOURCE;
```

## 相关文档

* [ADD RESTORE SOURCE](120.add-restore-source.md)
* [执行指定路径的恢复](../../../../../600.manage/600.backup-and-recovery/600.restore-data/260.initiate-the-specified-path-restore.md)
