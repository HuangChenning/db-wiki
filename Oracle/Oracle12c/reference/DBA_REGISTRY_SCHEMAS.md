---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_REGISTRY_SCHEMAS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_REGISTRY_SCHEMAS` lists the primary and ancillary schemas included in the component registry. The ancillary schemas that are listed in this view are the same schemas that would be included in the `OTHER_SCHEMAS` column of the `DBA_REGISTRY` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(30)` |  | Component namespace |
| `COMP_ID` | `VARCHAR2(30)` |  | Component identifier |
| `SCHEMA` | `VARCHAR2(128)` |  | User that contains the objects for the component |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1)

See Also:

- " [DBA\_REGISTRY](DBA_REGISTRY.md) "
- " [USER\_REGISTRY](USER_REGISTRY.md) "