---
title: RETURN
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285303.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# RETURN

`RETURN` 语句终止存储函数的执行，并将结果返回给函数调用者。

`RETURN` 语句的语法如下：

```sql
RETURN expr
```

存储函数中必须至少有一个 `RETURN` 语句。如果函数有多个退出点，则可能有多个 `RETURN` 语句。

存储过程和触发器不使用 `RETURN` 语句，而是使用 `LEAVE` 语句退出程序。
