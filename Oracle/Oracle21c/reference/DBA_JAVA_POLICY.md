---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_JAVA_POLICY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.132 DBA\_JAVA\_POLICY

`DBA_JAVA_POLICY` describes Java security permissions for all users in the database.

Related View

`USER_JAVA_POLICY` describes Java security permissions for the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `KIND` | `VARCHAR2(8)` |  | Indicates whether the permission is a positive (`GRANT`) or a limitation (`RESTRICT`) |
| `GRANTEE` | `VARCHAR2(128)` | `NOT NULL` | Name of the user, schema, or role to which the permission object is assigned |
| `TYPE_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema in which the permission object is loaded |
| `TYPE_NAME` | `VARCHAR2(4000)` |  | Permission class type, which is designated by a string containing the full class name, such as, `java.io.FilePermission` |
| `NAME` | `VARCHAR2(4000)` |  | Target attribute (name) of the permission object. This name is used when defining the permission. |
| `ACTION` | `VARCHAR2(4000)` |  | Action attribute for this permission. Many permissions expect a null value if no action is appropriate for the permission. |
| `ENABLED` | `VARCHAR2(8)` |  | Indicates whether the permission is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `SEQ` | `NUMBER` |  | Sequence number used to identify this row. This number should be supplied when disabling, enabling, or deleting the permission. |

See Also:

" [USER\_JAVA\_POLICY](USER_JAVA_POLICY.md) "