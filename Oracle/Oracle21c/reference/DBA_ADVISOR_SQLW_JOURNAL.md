---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_SQLW_JOURNAL.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.44 DBA\_ADVISOR\_SQLW\_JOURNAL

`DBA_ADVISOR_SQLW_JOURNAL` displays the journal entries for all workload objects in the database.

Related View

`USER_ADVISOR_SQLW_JOURNAL` displays the journal entries for the workload objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the workload |
| `WORKLOAD_ID` | `NUMBER` | `NOT NULL` | Identifier number of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(128)` |  | Name of the workload object |
| `JOURNAL_ENTRY_SEQ` | `NUMBER` | `NOT NULL` | Sequence number of the journal entry (unique for each workload). The sequence number is used to order the data. |
| `JOURNAL_ENTRY_TYPE` | `VARCHAR2(12)` |  | Type of the task:  - `FATAL` - `ERROR` - `WARNING` - `INFORMATION` - `INFORMATION[2 \| 3 \| 4 \| 5 \| 6]` |
| `JOURNAL_ENTRY` | `VARCHAR2(4000)` |  | Entry in the journal |

See Also:

" [USER\_ADVISOR\_SQLW\_JOURNAL](USER_ADVISOR_SQLW_JOURNAL.md) "