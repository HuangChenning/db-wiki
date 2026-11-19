---
title: RTRIM
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701578.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# RTRIM

## 声明

```sql
RTRIM(str)
```

## 说明

删除字符串 `str` 右侧的空格。

## 示例

```sql
obclient> SELECT RTRIM('    obclient    ') AS rtrim;
+--------------+
| rtrim        |
+--------------+
|     obclient |
+--------------+
1 row in set 
```
