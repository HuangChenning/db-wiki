---
title: RESOURCE_VIEW
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5169.htm
tags:
  - oracle
  - 11g
  - reference
---

`RESOURCE_VIEW` contains one row for each resource in the Oracle XML DB repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RES` | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBResource.xsd" Element "Resource") |  | A resource in the repository |
| `ANY_PATH` | `VARCHAR2(4000)` |  | An (absolute) path to the resource |
| `RESID` | `RAW(16)` |  | Resource OID, which is a unique handle to the resource |

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for information about using this view