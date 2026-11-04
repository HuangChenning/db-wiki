---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_SECONDARY_OBJECTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.70 ALL\_SECONDARY\_OBJECTS

`ALL_SECONDARY_OBJECTS` provides information about secondary objects associated with domain indexes accessible to the user.

This view is only relevant for domain indexes. And currently, the secondary objects can only be tables.

Related Views

- `DBA_SECONDARY_OBJECTS` provides information about all secondary objects that are associated with domain indexes in the database.
- `USER_SECONDARY_OBJECTS` provides information about secondary objects associated with domain indexes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the domain index |
| `INDEX_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the domain index |
| `SECONDARY_OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the secondary object created by the domain index |
| `SECONDARY_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the secondary object created by the domain index |
| `SECONDARY_OBJDATA_TYPE` | `VARCHAR2(20)` |  | Type of the secondary object created by the domain index |

See Also:

- " [DBA\_SECONDARY\_OBJECTS](DBA_SECONDARY_OBJECTS.md) "
- " [USER\_SECONDARY\_OBJECTS](USER_SECONDARY_OBJECTS.md) "