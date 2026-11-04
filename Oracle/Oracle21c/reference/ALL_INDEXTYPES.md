---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_INDEXTYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.240 ALL\_INDEXTYPES

`ALL_INDEXTYPES` displays information about the indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPES` displays information about all indextypes in the database.
- `USER_INDEXTYPES` displays information about the indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the indextype |
| `IMPLEMENTATION_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Name of the schema for the indextype implementation (that is, containing the indextype operators) |
| `IMPLEMENTATION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the indextype implementation type |
| `INTERFACE_VERSION` | `NUMBER` |  | Version of the indextype interface |
| `IMPLEMENTATION_VERSION` | `NUMBER` | `NOT NULL` | Version of the indextype implementation |
| `NUMBER_OF_OPERATORS` | `NUMBER` |  | Number of operators associated with the indextype |
| `PARTITIONING` | `VARCHAR2(10)` |  | Kinds of local partitioning supported by the indextype:  - `NONE` - Indextype does not support local domain indexes - `RANGE` - Indextype can support range partitioned local user managed domain indexes - `LOCAL` - Indextype can support local system managed domain indexes (range, list, hash, or interval) |
| `ARRAY_DML` | `VARCHAR2(3)` |  | Indicates whether the indextype supports array DML (`YES`) or not (`NO`) |
| `MAINTENANCE_TYPE` | `VARCHAR2(14)` |  | Indicates whether the indextype is system-managed (`SYSTEM_MANAGED`) or user-managed (`USER_MANAGED`) |

See Also:

- " [DBA\_INDEXTYPES](DBA_INDEXTYPES.md) "
- " [USER\_INDEXTYPES](USER_INDEXTYPES.md) "