---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-PATCHES.html
tags:
  - oracle
  - 12c
  - reference
---

`V$PATCHES` shows the patches applied on an Oracle ASM instance and the list of patches applied to an Oracle Grid infrastructure home directory.

Note:

If this view is queried in an RDBMS instance, no patch information is returned.

| Column | Datatype | Description |
| --- | --- | --- |
| `PATCH_ID` | `NUMBER` | Patch identifier |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |