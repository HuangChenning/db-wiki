---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CDB_RSRC_PLANS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_CDB_RSRC_PLANS` provides information about all the CDB resource plans.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PLAN_ID` | `NUMBER` | `NOT NULL` | CDB resource plan ID |
| `PLAN` | `VARCHAR2(128)` |  | CDB resource plan name |
| `COMMENTS` | `VARCHAR2(2000)` |  | Text comment on the CDB resource plan |
| `STATUS` | `VARCHAR2(128)` |  | `PENDING` if it is part of the pending area, `NULL` otherwise |
| `MANDATORY` | `VARCHAR2(3)` |  | Whether the resource plan is mandatory. Mandatory plans cannot be deleted. |