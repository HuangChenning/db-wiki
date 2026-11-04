---
title: ALL_OBJECTS_AE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1159.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_OBJECTS_AE` describes the objects (across all editions) accessible to the current user. Dropped objects appear in this view with `OBJECT_TYPE` `=` `NON-EXISTENT`.

Related Views

- `DBA_OBJECTS_AE` describes all objects (across all editions) in the database.
- `USER_OBJECTS_AE` describes the objects (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(30)` |  | Name of the subobject (for example, partition) |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Dictionary object number of the object |
| `DATA_OBJECT_ID` | `NUMBER` |  | Dictionary object number of the segment which contains the object |
| `OBJECT_TYPE` | `VARCHAR2(19)` |  | Type of the object |
| `CREATED` | `DATE` | `NOT NULL` | Timestamp for the creation of the object |
| `LAST_DDL_TIME` | `DATE` | `NOT NULL` | Timestamp for the last modification of the object and dependent objects resulting from a DDL statement (including grants and revokes) |
| `TIMESTAMP` | `VARCHAR2(19)` |  | Timestamp for the specification of the object (character data) |
| `STATUS` | `VARCHAR2(7)` |  | Status of the object: - `VALID` - `INVALID` - `N/A` |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether the object is temporary (the current session can see only data that it placed in this object itself) (`Y`) or not (`N`) |
| `GENERATED` | `VARCHAR2(1)` |  | Indicates whether the name of this object was system-generated (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether this is a secondary object created by the `ODCIIndexCreate` method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `NAMESPACE` | `NUMBER` | `NOT NULL` | Namespace for the object |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Name of the edition in which the object is actual |

See Also:

- ["DBA\_OBJECTS\_AE"](statviews_4159.md)
- ["USER\_OBJECTS\_AE"](statviews_5377.md)