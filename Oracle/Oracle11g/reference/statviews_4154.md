---
title: DBA_OBJ_AUDIT_OPTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4154.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_OBJ_AUDIT_OPTS` describes auditing options on all objects.

Related View

`USER_OBJ_AUDIT_OPTS` describes auditing options on all objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the object |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Type of the object |
| `ALT` | `VARCHAR2(3)` |  | Auditing `ALTER WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `AUD` | `VARCHAR2(3)` |  | Auditing `AUDIT WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `COM` | `VARCHAR2(3)` |  | Auditing `COMMENT WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `DEL` | `VARCHAR2(3)` |  | Auditing `DELETE WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `GRA` | `VARCHAR2(3)` |  | Auditing `GRANT WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `IND` | `VARCHAR2(3)` |  | Auditing `INDEX WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `INS` | `VARCHAR2(3)` |  | Auditing `INSERT WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `LOC` | `VARCHAR2(3)` |  | Auditing `LOCK WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `REN` | `VARCHAR2(3)` |  | Auditing `RENAME WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `SEL` | `VARCHAR2(3)` |  | Auditing `SELECT WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `UPD` | `VARCHAR2(3)` |  | Auditing `UPDATE WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `REF` | `CHAR(3)` |  | This column is obsolete and maintained for backward compatibility. The value of this column is always `-/-` |
| `EXE` | `VARCHAR2(3)` |  | Auditing `EXECUTE WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `CRE` | `VARCHAR2(3)` |  | Auditing `CREATE WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `REA` | `VARCHAR2(3)` |  | Auditing `READ WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `WRI` | `VARCHAR2(3)` |  | Auditing `WRITE WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `FBK` | `VARCHAR2(3)` |  | Auditing `FLASHBACK WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4007.htm#SQLRF01107) for more information about the SQL `AUDIT` statement
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG0635) to learn how to find information about audited activities