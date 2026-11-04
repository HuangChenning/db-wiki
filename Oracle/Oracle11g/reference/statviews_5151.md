---
title: PATH_VIEW
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5151.htm
tags:
  - oracle
  - 11g
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

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for information about using this view