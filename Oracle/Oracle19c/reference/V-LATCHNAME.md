---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-LATCHNAME.html
tags:
  - oracle
  - 19c
  - reference
---

## 8.32 V$LATCHNAME

`V$LATCHNAME` displays information about decoded latch names for the latches shown in `V$LATCH`.

The rows of `V$LATCHNAME` have a one-to-one correspondence to the rows of `V$LATCH`.

| Column | Datatype | Description |
| --- | --- | --- |
| `LATCH#` | `NUMBER` | Latch number |
| `NAME` | `VARCHAR2(64)` | Latch name |
| `DISPLAY_NAME` | `VARCHAR2(64)` | A clearer and more descriptive name for the latch that appears in the `NAME` column. Names that appear in the `DISPLAY_NAME` column can change across Oracle Database releases, therefore customer scripts should not rely on names that appear in the `DISPLAY_NAME` column across releases. |
| `HASH` | `NUMBER` | Latch hash |
| `TYPE` | `VARCHAR2(4)` | Type of the latch (`SGA`, `PDB`, or `OSP`): |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$LATCH](V-LATCH.md) "