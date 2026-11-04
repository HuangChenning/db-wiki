---
title: DBA_ADVISOR_SQLW_JOURNAL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3035.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_SQLW_JOURNAL` displays the journal entries for all workload objects in the database.

Related View

`USER_ADVISOR_SQLW_JOURNAL` displays the journal entries for the workload objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the workload |
| `WORKLOAD_ID` | `NUMBER` | `NOT NULL` | Identifier number of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(30)` |  | Name of the workload object |
| `JOURNAL_ENTRY_SEQ` | `NUMBER` | `NOT NULL` | Sequence number of the journal entry (unique for each workload). The sequence number is used to order the data. |
| `JOURNAL_ENTRY_TYPE` | `VARCHAR2(12)` |  | Type of the task: - `FATAL` - `ERROR` - `WARNING` - `INFORMATION` - `INFORMATION[2 \| 3 \| 4 \| 5 \| 6]` |
| `JOURNAL_ENTRY` | `VARCHAR2(4000)` |  | Entry in the journal |

See Also:

["USER\_ADVISOR\_SQLW\_JOURNAL"](statviews_5217.md)