---
title: "V$RSRC_CONSUMER_GROUP_CPU_MTH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2158.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RSRC_CONSUMER_GROUP_CPU_MTH` displays all resource allocation methods defined for resource consumer groups.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(40)` | Name of the CPU resource allocation method |

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on resource allocation methods
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) on defining resource allocation methods for consumer groups with the `DBMS_RESOURCE_MANAGER` package
- ["V$RSRC\_PLAN\_CPU\_MTH"](dynviews_2160.md) for a listing of all resource allocation methods defined for resource plans