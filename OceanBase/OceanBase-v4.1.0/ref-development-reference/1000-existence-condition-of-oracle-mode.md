---
title: "EXISTS 条件"
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699552.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
