---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_OBJECTS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.295 ALL\_OBJECTS\_AE

Dropped objects appear in this view with `OBJECT_TYPE` `=` `NON-EXISTENT`.

Related Views

- `DBA_OBJECTS_AE` describes all objects (across all editions) in the database.
- `USER_OBJECTS_AE` describes the objects (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the subobject (for example, partition) |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Dictionary object number of the object |
| `DATA_OBJECT_ID` | `NUMBER` |  | Dictionary object number of the segment which contains the object |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Type of the object |
| `CREATED` | `DATE` | `NOT NULL` | Timestamp for the creation of the object |
| `LAST_DDL_TIME` | `DATE` | `NOT NULL` | Timestamp for the last modification of the object and dependent objects resulting from a DDL statement (including grants and revokes) |
| `TIMESTAMP` | `VARCHAR2(19)` |  | Timestamp for the specification of the object (character data) |
| `STATUS` | `VARCHAR2(7)` |  | Status of the object:  - `VALID` - `INVALID` - `N/A` |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether the object is temporary (the current session can see only data that it placed in this object itself) (`Y`) or not (`N`) |
| `GENERATED` | `VARCHAR2(1)` |  | Indicates whether the name of this object was system-generated (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether this is a secondary object created by the `ODCIIndexCreate` method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `NAMESPACE` | `NUMBER` | `NOT NULL` | Namespace for the object |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the edition in which the object is actual |
| `SHARING` | `VARCHAR2(18)` |  | Values:  - `DATA` `LINK` - If the object is data-linked or a data link to an object in the root - `METADATA` `LINK` - If the object is metadata-linked or a metadata link to an object in the root - `EXTENDED` `DATA` `LINK` - If the object is extended-data-linked or an extended data link to an object in the root - `NONE` - If none of the above applies |
| `EDITIONABLE` | `VARCHAR2(1)` |  | Values:  - `Y` - For objects marked EDITIONABLE - `N` - For objects marked NONEDITIONABLE - `NULL` - For objects whose type is not editionable in the database |
| `ORACLE_MAINTAINED` | `VARCHAR2(1)` |  | Denotes whether the object was created, and is maintained, by Oracle-supplied scripts (such as catalog.sql or catproc.sql). An object for which this column has the value `Y` must not be changed in any way except by running an Oracle-supplied script. |
| `APPLICATION` | `VARCHAR2(1)` |  | Indicates whether the object is an Application common object (`Y`) or not (`N`) |
| `DEFAULT_COLLATION` | `VARCHAR2(100)` |  | Default collation for the object |
| `DUPLICATED` | `VARCHAR2(1)` |  | Indicates whether this object is duplicated on this shard (`Y`) or not (`N`) |
| `SHARDED` | `VARCHAR2(1)` |  | Indicates whether this object is sharded (`Y`) or not (`N`) |
| `IMPORTED_OBJECT` | `VARCHAR2(1)` |  | Indicates whether this object is imported (`Y`) or not (`N`) |
| `CREATED_APPID` | `NUMBER` |  | ID of the Application that created the object |
| `CREATED_VSNID` | `NUMBER` |  | ID of the Application Version that created the object |
| `MODIFIED_APPID` | `NUMBER` |  | ID of the Application that last modified the object |
| `MODIFIED_VSNID` | `NUMBER` |  | ID of the Application Version that last modified the object |

See Also:

- " [DBA\_OBJECTS\_AE](DBA_OBJECTS_AE.md) "
- " [USER\_OBJECTS\_AE](USER_OBJECTS_AE.md) "