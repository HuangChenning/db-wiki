---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CLUSTER_HASH_EXPRESSIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_CLUSTER_HASH_EXPRESSIONS` displays hash functions for all hash clusters accessible to the current user.

Related Views

- `DBA_CLUSTER_HASH_EXPRESSIONS` displays hash functions for all hash clusters in the database.
- `USER_CLUSTER_HASH_EXPRESSIONS` displays hash functions for all hash clusters owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cluster |
| `CLUSTER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the cluster |
| `HASH_EXPRESSION` | `LONG` |  | Text of the hash function of the hash cluster |

See Also:

- " [DBA\_CLUSTER\_HASH\_EXPRESSIONS](DBA_CLUSTER_HASH_EXPRESSIONS.md) "
- " [USER\_CLUSTER\_HASH\_EXPRESSIONS](USER_CLUSTER_HASH_EXPRESSIONS.md) "