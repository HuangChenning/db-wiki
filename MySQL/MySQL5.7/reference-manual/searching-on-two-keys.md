---
title: "3.6.7 Searching on Two Keys"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/searching-on-two-keys.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 3.6.7 Searching on Two Keys

An [`OR`](logical-operators.md) using a single key is well optimized, as is the handling of [`AND`](logical-operators.md).

The one tricky case is that of searching on two different keys combined with [`OR`](logical-operators.md):

```
SELECT field1_index, field2_index FROM test_table
WHERE field1_index = '1' OR  field2_index = '1'
```

This case is optimized. See [Section 8.2.1.3, “Index Merge Optimization”](index-merge-optimization.md).

You can also solve the problem efficiently by using a [`UNION`](union.md) that combines the output of two separate [`SELECT`](select.md) statements. See [Section 13.2.9.3, “UNION Clause”](union.md).

Each [`SELECT`](select.md) searches only one key and can be optimized:

```
SELECT field1_index, field2_index
    FROM test_table WHERE field1_index = '1'
UNION
SELECT field1_index, field2_index
    FROM test_table WHERE field2_index = '1';
```