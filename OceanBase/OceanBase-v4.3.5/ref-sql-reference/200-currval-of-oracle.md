---
title: "CURRVAL(SEQ) 函数"
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004376620.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# CURRVAL(SEQ) 函数

`CURRVAL(SEQ)` 函数用于返回序列的当前值。

## 使用示例

要使用 `CURRVAL`，首先需要创建一个序列。以下是创建序列和使用 `CURRVAL` 的步骤和示例。

**步骤一：创建序列**

```shell
obclient> CREATE CURRVAL students_seq;
```

**步骤二：使用 NEXTVAL 插入新数据**

```shell
obclient> INSERT INTO students (id, name) VALUES (students_seq.NEXTVAL, 'John Doe');
```

**步骤三：使用 CURRVAL 获取当前值**

```shell
obclient> SELECT currval('students_seq') FROM DUAL;
```
