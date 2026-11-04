---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PATH_VIEW.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.215 PATH\_VIEW

`PATH_VIEW` contains one row for each unique path to access a resource in the Oracle XML DB repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH` | `VARCHAR2(1024)` |  | An (absolute) path to repository resource `RES` |
| `RES` | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBResource.xsd" Element "Resource") |  | The resource referred to by the `PATH` column |
| `LINK` | `XMLTYPE` |  | Link property |
| `RESID` | `RAW(16)` |  | Resource OID |

See Also:

[Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-14598A45-6DFA-4FB9-AB2E-CC5B23C6F6D4) for information about using this view