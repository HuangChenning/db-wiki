---
title: LTRIM
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702895.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# LTRIM

## 声明

```sql
LTRIM(str)
```

## 说明

删除字符串左侧的空格。

## 示例

```sql
obclient> SELECT LTRIM('    obclient    ') AS ltrim;
+--------------+
| ltrim        |
+--------------+
| obclient     |
+--------------+
1 row in set 
```
