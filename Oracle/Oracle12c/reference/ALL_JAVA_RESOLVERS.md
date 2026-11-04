---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_JAVA_RESOLVERS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_JAVA_RESOLVERS` displays information about resolvers of the Java classes accessible to the current user.

Related Views

- `DBA_JAVA_RESOLVERS` displays information about resolvers of all Java classes in the database.
- `USER_JAVA_RESOLVERS` displays information about resolvers of the Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Java class object |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class object |
| `TERM_INDEX` | `NUMBER` |  | Index of the resolver term in this row |
| `PATTERN` | `VARCHAR2(4000)` |  | Resolver pattern of the resolver term identified by the `TERM_INDEX` column |
| `SCHEMA` | `VARCHAR2(64)` |  | Resolver schema of the resolver term identified by the `TERM_INDEX` column |

See Also:

- " [DBA\_JAVA\_RESOLVERS](DBA_JAVA_RESOLVERS.md) "
- " [USER\_JAVA\_RESOLVERS](USER_JAVA_RESOLVERS.md) "