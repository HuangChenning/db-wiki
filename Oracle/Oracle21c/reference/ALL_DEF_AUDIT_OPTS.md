---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_DEF_AUDIT_OPTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.164 ALL\_DEF\_AUDIT\_OPTS

`ALL_DEF_AUDIT_OPTS` contains default object-auditing options that will be applied when objects are created.

The output for each column takes one of the following forms:

- `-/-`: no default auditing
- `S/-`: auditing whenever successful
- `-/S`: auditing whenever not successful

Note:

This view is relevant when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
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
| `EXE` | `VARCHAR2(3)` |  | Auditing ` EXECUTE WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `FBK` | `VARCHAR2(3)` |  | Auditing `FLASHBACK WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `REA` | `VARCHAR2(3)` |  | Auditing `READ WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |