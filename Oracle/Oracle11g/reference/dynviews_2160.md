---
title: "V$RSRC_PLAN_CPU_MTH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2160.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RSRC_PLAN_CPU_MTH` displays all available CPU resource allocation methods defined for resource plans.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(40)` | Name of the resource allocation method |

See Also:

- ["V$RSRC\_CONSUMER\_GROUP\_CPU\_MTH"](dynviews_2158.md) for a listing of resource allocation methods defined for consumer groups
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on resource plans
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information on defining resource allocation methods for consumer plans with the `DBMS_RESOURCE_MANAGER` package