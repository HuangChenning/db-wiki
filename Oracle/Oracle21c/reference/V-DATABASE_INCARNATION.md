---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATABASE_INCARNATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.155 V$DATABASE\_INCARNATION

`V$DATABASE_INCARNATION` displays information about all database incarnations.

Oracle creates a new incarnation whenever a database is opened with the `RESETLOGS` option. Records about the current and immediately previous incarnation are also contained in the `V$DATABASE` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `INCARNATION#` | `NUMBER` | Record ID for the branch record in the control file |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs system change number (SCN) for the incarnation of the current row |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp for the incarnation of the current row |
| `PRIOR_RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs SCN for the previous incarnation |
| `PRIOR_RESETLOGS_TIME` | `DATE` | Resetlogs timestamp for the previous incarnation |
| `STATUS` | `VARCHAR2(7)` | Incarnation status:  - `ORPHAN` - Orphan incarnation - `CURRENT` - Current incarnation of the database - `PARENT` - Parent of the current incarnation |
| `RESETLOGS_ID` | `NUMBER` | Branch ID for the incarnation of the current row (used by user-managed recovery/RMAN restore to get unique names for archived logs across incarnations) |
| `PRIOR_INCARNATION#` | `NUMBER` | Parent incarnation record ID if nonzero |
| `FLASHBACK_DATABASE_ALLOWED` | `VARCHAR2(26)` | Indicate whether or not Flashback Database can be performed into SCNs or timestamps in the incarnation. A value of YES means that you can flashback to some point in that incarnation. A value of NO indicates that you cannot flashback into the incarnation. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$DATABASE](V-DATABASE.md) "