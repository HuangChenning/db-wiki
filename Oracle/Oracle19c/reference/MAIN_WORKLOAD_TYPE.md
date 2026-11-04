---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MAIN_WORKLOAD_TYPE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.195 MAIN\_WORKLOAD\_TYPE

`MAIN_WORKLOAD_TYPE` specifies the main workload type for a database or PDB.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MAIN_WORKLOAD_TYPE = { OLTP \| ANALYTICS }` |
| Default value | `OLTP` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

This parameter is supported only for Oracle Exadata. See [Oracle Exadata System Software User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=SAGUG-GUID-101960A2-7D0B-4252-B155-48EF90170BE6) for more information about setting this parameter