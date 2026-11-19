---
title: JSON_MERGE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702862.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# JSON_MERGE

## 描述

该函数用于合并多个 JSON 文档。该函数是 JSON_MERGE_PRESERVE() 的同义词。

## 语法

```sql
JSON_MERGE(json_doc, json_doc[, json_doc] ...)
```

## 说明

`json_doc` 参数指定需要合并的 JSON 文档。

## 示例

```sql
obclient> SELECT JSON_MERGE('[1, 2, 3]', '[true, false]', '{"a":100}');
+-------------------------------------------------------+
| JSON_MERGE('[1, 2, 3]', '[true, false]', '{"a":100}') |
+-------------------------------------------------------+
| [1, 2, 3, true, false, {"a": 100}]                    |
+-------------------------------------------------------+
1 row in set

obclient> SELECT JSON_MERGE('{"1": 2}', '[true, false]', '{"a":100}');
+------------------------------------------------------+
| JSON_MERGE('{"1": 2}', '[true, false]', '{"a":100}') |
+------------------------------------------------------+
| [{"1": 2}, true, false, {"a": 100}]                  |
+------------------------------------------------------+
1 row in set

obclient> SELECT JSON_MERGE('{"1": 2}',  '{"a":100}');
+--------------------------------------+
| JSON_MERGE('{"1": 2}',  '{"a":100}') |
+--------------------------------------+
| {"1": 2, "a": 100}                   |
+--------------------------------------+
1 row in set
```
