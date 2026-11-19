---
title: DROP EVENT
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503348.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DROP EVENT

该语句用于删除事件。

## 语法

```sql
DROP EVENT [IF EXISTS] event_name
```

## 参数解释

| 参数   | 描述     |
|-------|-----------|
|event_name|指定待删除事件的名称。|

## 示例

```shell
obclient> DROP EVENT myevent;
```
