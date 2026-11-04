---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PATH_VIEW.html
tags:
  - oracle
  - 12c
  - reference
---

`PATH_VIEW` contains one row for each unique path to access a resource in the Oracle XML DB repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH` | `VARCHAR2(1024)` |  | An (absolute) path to repository resource `RES` |
| `RES` | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBResource.xsd" Element "Resource") |  | The resource referred to by the `PATH` column |
| `LINK` | `XMLTYPE` |  | Link property |
| `RESID` | `RAW(16)` |  | Resource OID |

See Also:

[Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADXDB5388) for information about using this view