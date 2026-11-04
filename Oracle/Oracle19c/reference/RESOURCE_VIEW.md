---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/RESOURCE_VIEW.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.233 RESOURCE\_VIEW

`RESOURCE_VIEW` contains one row for each resource in the Oracle XML DB repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RES` | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBResource.xsd" Element "Resource") |  | A resource in the repository |
| `ANY_PATH` | `VARCHAR2(4000)` |  | An (absolute) path to the resource |
| `RESID` | `RAW(16)` |  | Resource OID, which is a unique handle to the resource |

See Also:

[Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ADXDB5388) for information about using this view