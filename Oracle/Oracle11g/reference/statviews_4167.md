---
title: DBA_OUTLINE_HINTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4167.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_OUTLINE_HINTS` describes the set of hints stored in all outlines in the database.

Related View

`USER_OUTLINE_HINTS` describes the set of hints stored in the outlines owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` |  | Name of the outline |
| `OWNER` | `VARCHAR2(30)` |  | Name of the user who created the outline |
| `NODE` | `NUMBER` |  | ID of the query or subquery to which the hint applies. The top-level query is labeled `1`. Subqueries are assigned sequentially numbered labels, starting with `2`. |
| `STAGE` | `NUMBER` |  | Outline hints can be applied at three different stages during the compilation process. This column indicates the stage at which this hint was applied. |
| `JOIN_POS` | `NUMBER` |  | Position of the table in the join order. The value is `0` for all hints except access method hints, which identify a table to which the hint and the join position apply. |
| `HINT` | `VARCHAR2(512)` |  | Text of the hint |

See Also:

["USER\_OUTLINE\_HINTS"](statviews_5383.md)