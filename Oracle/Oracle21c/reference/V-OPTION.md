---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OPTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.105 V$OPTION

`V$OPTION` displays Oracle Database options and features.

Typically, although not always, options must be separately licensed, whereas features come with the product and are enabled based on the product that is running (for example, Enterprise Edition).

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER` | `VARCHAR2(64)` | Name of the option (or feature) |
| `VALUE` | `VARCHAR2(64)` | Indicates whether the option (or feature) is installed (`TRUE`) or not (`FALSE`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) for more information about Oracle Database options and features