---
title: DBA_INVALID_OBJECTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4087.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_INVALID_OBJECTS` describes all invalid objects in the database. You can use this view to identify invalid objects before and after a database upgrade.

This view eliminates old versions of object types. It only includes the object type it if is the latest version.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(30)` |  | Name of the subobject (for example, partition) |
| `OBJECT_ID` | `NUMBER` |  | Dictionary object number of the object |
| `DATA_OBJECT_ID` | `NUMBER` |  | Dictionary object number of the segment that contains the object.  Note: `OBJECT_ID` and `DATA_OBJECT_ID` display data dictionary metadata. Do not confuse these numbers with the unique 16-byte object identifier (object ID) that Oracle Database assigns to row objects in object tables in the system. |
| `OBJECT_TYPE` | `VARCHAR2(19)` |  | Type of the object (such as `TABLE`, `INDEX`) |
| `CREATED` | `DATE` |  | Timestamp for the creation of the object |
| `LAST_DDL_TIME` | `DATE` |  | Timestamp for the last modification of the object and dependent objects resulting from a DDL statement (including grants and revokes) |
| `TIMESTAMP` | `VARCHAR2(19)` |  | Timestamp for the specification of the object (character data) |
| `STATUS` | `VARCHAR2(7)` |  | Status of the object: - `VALID` - `INVALID` - `N/A` |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether the object is temporary (the current session can see only data that it placed in this object itself) (`Y`) or not (`N`) |
| `GENERATED` | `VARCHAR2(1)` |  | Indicates whether the name of this object was system-generated (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether this is a secondary object created by the `ODCIIndexCreate` method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `NAMESPACE` | `NUMBER` |  | Namespace for the object |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Name of the edition in which the object is actual |