---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_METADATA_PROPERTIES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_METADATA_PROPERTIES` describes OLAP metadata properties in the database that are accessible to the current user.

Related Views

- `DBA_METADATA_PROPERTIES` describes OLAP metadata properties in the database.
- `USER_METADATA_PROPERTIES` describes OLAP metadata properties in the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the OLAP metadata property |
| `OWNING_OBJECT_ID` | `NUMBER` |  | Dictionary ID of the OLAP metadata property owner |
| `OWNING_TYPE` | `VARCHAR2(23)` |  | Owning type of the OLAP metadata property |
| `PROPERTY_ID` | `NUMBER` |  | Dictionary Id of the OLAP metadata property |
| `PROPERTY_KEY` | `VARCHAR2(128)` |  | Key of the OLAP metadata property |
| `PROPERTY_VALUE` | `CLOB` |  | Value of the OLAP metadata property |
| `PROPERTY_ORDER` | `NUMBER` |  | Order number of the OLAP metadata property |

See Also:

- " [DBA\_METADATA\_PROPERTIES](DBA_METADATA_PROPERTIES.md) "
- " [USER\_METADATA\_PROPERTIES](USER_METADATA_PROPERTIES.md) "