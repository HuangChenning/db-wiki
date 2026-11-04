---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ILMOBJECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.99 DBA\_ILMOBJECTS

`DBA_ILMOBJECTS` displays all the Automatic Data Optimization policies and objects in the database.

Many objects inherit policies via their parent objects or because they were created in a particular tablespace. This view provides a mapping between the policies and objects and indicates whether a policy is inherited by an object or is directly specified on it.

Related View

`USER_ILMOBJECTS` displays all the Automatic Data Optimization policies and objects for a user.

Note:

Automatic Data Optimization is supported in Oracle Database 12c Release 2 multitenant environments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Policy name is auto-generated |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object associated with the Automatic Data Optimization policy |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object associated with the Automatic Data Optimization policy |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the subobject associated with the Automatic Data Optimization policy |
| `OBJECT_TYPE` | `VARCHAR2(18)` |  | Object type. Valid values include:  - `INDEX` - `INDEX PARTITION` - `LOB` - `LOB PARTITION` - `TABLE` - `TABLE PARTITION` - `TABLE SUBPARTITION`  Direct policies on Index, Index Partition, LOB, and LOB Partition are not supported in Oracle Database 12c. |
| `INHERITED_FROM` | `VARCHAR2(20)` |  | Indicates if the policy is inherited by the object or subobject, or directly specified on the object or subobject. If the policy is inherited, the level from which the policy is inherited (`TABLE`, `TABLE PARTITION`, `TABLESPACE`) is identified. |
| `TBS_INHERITED_FROM` | `VARCHAR2(30`) |  | The tablespace name, if the policy is inherited from a tablespace |
| `ENABLED` | `VARCHAR2(7)` |  | Indicates if the Automatic Data Optimization policy is enabled for the object (`YES` or `NO`) |
| `DELETED` | `VARCHAR2(7)` |  | Possible values:  - `YES` - Indicates that the policy is deleted for any objects that may be added in the future, but is active for those objects that are currently associated with that policy - `NO` - Indicates that the policy is active |

See Also:

" [USER\_ILMOBJECTS](USER_ILMOBJECTS.md) "