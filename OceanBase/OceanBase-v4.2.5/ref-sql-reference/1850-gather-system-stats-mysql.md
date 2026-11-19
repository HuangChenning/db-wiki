---
title: GATHER_SYSTEM_STATS
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503596.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# GATHER_SYSTEM_STATS

`GATHER_SYSTEM_STATS` 过程用于收集系统统计信息。

## 语法

```sql
DBMS_STATS.GATHER_SYSTEM_STATS();
```

## 异常情况

|    错误码    |        描述     |
|-----------|------------------|
| HY000    | 输入的系统统计信息名称错。 |

## 使用说明

要执行该过程，用户必须具备 `SUPER` 权限或者是 `root` 用户。

## 示例

执行 `DBMS_STATS.GATHER_SYSTEM_STATS` 过程收集系统统计信息，如 CPU 速度、磁盘 I/O 性能和网络吞吐量：

```sql
BEGIN
    -- 收集系统统计信息
    DBMS_STATS.GATHER_SYSTEM_STATS();
END;
/
```
