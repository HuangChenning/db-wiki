---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRC_CONSUMER_GROUP_CPU_MTH.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.191 V$RSRC\_CONSUMER\_GROUP\_CPU\_MTH

`V$RSRC_CONSUMER_GROUP_CPU_MTH` displays all resource allocation methods defined for resource consumer groups.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(40)` | Name of the CPU resource allocation method |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11892) for information on resource allocation methods
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS050) on defining resource allocation methods for consumer groups with the `DBMS_RESOURCE_MANAGER` package
- " [V$RSRC\_PLAN\_CPU\_MTH](V-RSRC_PLAN_CPU_MTH.md) " for a listing of all resource allocation methods defined for resource plans