---
title: LEAVE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699468.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# LEAVE

`LEAVE` 语句用于退出带有指定标签的流程控制语句。如果标签用于最外层的存储程序块，则使用 LEAVE 将退出该程序。

`LEAVE` 语句的语法如下：

```sql
LEAVE label
```

`LEAVE` 语句可以用于 `BEGIN ... END` 块中，以及 `LOOP`、`REPEAT` 和 `WHILE` 循环语句中。
