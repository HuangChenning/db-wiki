---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REGISTRY_SCHEMAS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.284 DBA\_REGISTRY\_SCHEMAS

`DBA_REGISTRY_SCHEMAS` lists the primary and ancillary schemas included in the component registry. The ancillary schemas that are listed in this view are the same schemas that would be included in the `OTHER_SCHEMAS` column of the `DBA_REGISTRY` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(30)` |  | Component namespace |
| `COMP_ID` | `VARCHAR2(30)` |  | Component identifier |
| `SCHEMA` | `VARCHAR2(128)` |  | User that contains the objects for the component |

See Also:

- " [DBA\_REGISTRY](DBA_REGISTRY.md) "
- " [USER\_REGISTRY](USER_REGISTRY.md) "