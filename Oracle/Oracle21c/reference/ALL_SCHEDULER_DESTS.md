---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_DESTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.41 ALL\_SCHEDULER\_DESTS

`ALL_SCHEDULER_DESTS` displays information about the destination objects for jobs accessible to the current user.

Related Views

- `DBA_SCHEDULER_DESTS` displays information about all destination objects for jobs in the database.
- `USER_SCHEDULER_DESTS` displays information about the destination objects for jobs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of this destination object |
| `DESTINATION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of this destination object |
| `DESTINATION_TYPE` | `VARCHAR2(8)` |  | Type of this destination object:  - `EXTERNAL` - `DATABASE` |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether this destination object is enabled (`TRUE`) or disabled (`FALSE`) |