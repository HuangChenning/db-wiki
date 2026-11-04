---
title: ALL_INDEXTYPES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1113.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_INDEXTYPES` displays information about the indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPES` displays information about all indextypes in the database.
- `USER_INDEXTYPES` displays information about the indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the indextype |
| `IMPLEMENTATION_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Name of the schema for the indextype implementation (that is, containing the indextype operators) |
| `IMPLEMENTATION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the indextype implementation type |
| `INTERFACE_VERSION` | `NUMBER` |  | Version of the indextype interface |
| `IMPLEMENTATION_VERSION` | `NUMBER` | `NOT NULL` | Version of the indextype implementation |
| `NUMBER_OF_OPERATORS` | `NUMBER` |  | Number of operators associated with the indextype |
| `PARTITIONING` | `VARCHAR2(10)` |  | Kinds of local partitioning supported by the indextype: - `NONE` - Indextype does not support local domain indexes - `RANGE` - Indextype can support range partitioned local user managed domain indexes - `LOCAL` - Indextype can support local system managed domain indexes (both range and list partitioned) |
| `ARRAY_DML` | `VARCHAR2(3)` |  | Indicates whether the indextype supports array DML (`YES`) or not (`NO`) |
| `MAINTENANCE_TYPE` | `VARCHAR2(14)` |  | Indicates whether the indextype is system-managed (`SYSTEM_MANAGED`) or user-managed (`USER_MANAGED`) |

See Also:

- ["DBA\_INDEXTYPES"](statviews_4085.md)
- ["USER\_INDEXTYPES"](statviews_5327.md)