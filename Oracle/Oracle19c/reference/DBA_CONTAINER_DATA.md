---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_CONTAINER_DATA.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.220 DBA\_CONTAINER\_DATA

`DBA_CONTAINER_DATA` displays default (user-level) and object-specific `CONTAINER_DATA` attributes for container data objects.

Objects created with the `CONTAINER_DATA` clause include `CONTAINER_DATA` attributes.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user whose attribute is described by this row |
| `DEFAULT_ATTR` | `CHAR2(1)` |  | An indicator of whether the attribute is a default attribute |
| `OWNER` | `VARCHAR2(128)` |  | Name of the object owner if the attribute is object-specific |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object if the attribute is object-specific |
| `ALL_CONTAINERS` | `VARCHAR2(1)` |  | An indicator of whether this attribute applies to all containers |
| `CONTAINER_NAME` | `VARCHAR2(128)` |  | Name of a container included in this attribute if it does not apply to all containers |