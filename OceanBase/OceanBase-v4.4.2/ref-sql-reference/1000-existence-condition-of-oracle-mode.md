---
title: "EXISTS 条件"
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286663.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# EXISTS 条件

EXISTS 条件（EXISTS Condition）用于测试子查询中是否存在指定的行。

## EXISTS 条件语法

EXISTS 条件语法如下：

```sql
EXISTS (subquery)
```

如果子查询至少返回一行，则说明存在您想要的数据。

## 示例

```sql
SELECT dept_id FROM dept d WHERE EXISTS (SELECT * FROM emp e
WHERE d.dept_id = e.dept_id) ORDER BY dept_id;
```
