---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/RESOURCE_VIEW.html
tags:
  - oracle
  - 12c
  - reference
---

`RESOURCE_VIEW` contains one row for each resource in the Oracle XML DB repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RES` | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBResource.xsd" Element "Resource") |  | A resource in the repository |
| `ANY_PATH` | `VARCHAR2(4000)` |  | An (absolute) path to the resource |
| `RESID` | `RAW(16)` |  | Resource OID, which is a unique handle to the resource |

See Also:

[Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADXDB5388) for information about using this view