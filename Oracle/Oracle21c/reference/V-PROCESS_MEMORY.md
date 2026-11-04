---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROCESS_MEMORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.130 V$PROCESS\_MEMORY

`V$PROCESS_MEMORY` displays dynamic PGA memory usage by named component categories for each process.

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | Oracle process identifier |
| `SERIAL#` | `NUMBER` | Oracle process serial number |
| `CATEGORY` | `VARCHAR2(15)` | Category name. Categories include "SQL", "PL/SQL", "OLAP" and "JAVA". Special categories are "Freeable" and "Other". Freeable memory has been allocated to the process by the operating system, but has not been allocated to a category. "Other" memory has been allocated to a category, but not to one of the named categories. |
| `ALLOCATED` | `NUMBER` | Bytes of PGA memory allocated by the process for the category. For the "Freeable" category, it is the amount of free PGA memory eligible to be released to the operating system. |
| `USED` | `NUMBER` | Bytes of PGA memory used by the process for the category. For "Freeable", the value is zero. For "Other", the value is NULL for performance reasons. |
| `MAX_ALLOCATED` | `NUMBER` | Maximum bytes of PGA memory ever allocated by the process for the category. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |