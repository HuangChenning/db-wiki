---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EVENT_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.218 V$EVENT\_NAME

| Column | Datatype | Description |
| --- | --- | --- |
| `EVENT#` | `NUMBER` | Number of the wait event |
| `EVENT_ID` | `NUMBER` | Identifier of the wait event |
| `NAME` | `VARCHAR2(64)` | Name of the wait event. Names that appear in this column remain stable across Oracle Database releases, and they can be relied on by customer scripts. |
| `PARAMETER1` | `VARCHAR2(64)` | Description of the first parameter for the wait event |
| `PARAMETER2` | `VARCHAR2(64)` | Description of the second parameter for the wait event |
| `PARAMETER3` | `VARCHAR2(64)` | Description of the third parameter for the wait event |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the class of the wait event |
| `WAIT_CLASS#` | `NUMBER` | Number of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the class of the wait event  See Also: " [Classes of Wait Events](classes-of-wait-events.md) " for a description of the different wait event classes |
| `DISPLAY_NAME` | `VARCHAR2(64)` | A clearer and more descriptive name for the wait event that appears in the `NAME` column. Names that appear in the `DISPLAY_NAME` column can change across Oracle Database releases, therefore customer scripts should not rely on names that appear in the `DISPLAY_NAME` column across releases. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |