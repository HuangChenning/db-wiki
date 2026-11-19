---
title: SOUNDEX
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018245.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SOUNDEX

## 声明

```sql
SOUNDEX(str)
```

## 说明

将输入的字符串转换成一个编码，用于表示字符串的发音。该函数常用于在数据库中进行模糊查询或者匹配发音相似的字符串。

## 示例

```sql
obclient> SELECT SOUNDEX('a');
+--------------+
| SOUNDEX('a') |
+--------------+
| A000         |
+--------------+
1 row in set
```
