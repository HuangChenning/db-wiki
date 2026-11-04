---
title: ALL_DEF_AUDIT_OPTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1068.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DEF_AUDIT_OPTS` contains default object-auditing options that will be applied when objects are created. The output for each column takes one of the following forms:

- `-/-`: no default auditing
- `S/-`: auditing whenever successful
- `-/S`: auditing whenever not successful

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
| `REF` | `CHAR(3)` |  | This column is obsolete and maintained for backward compatibility. The value of this column is always `-/-` |
| `EXE` | `VARCHAR2(3)` |  | Auditing `EXECUTE WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `FBK` | `VARCHAR2(3)` |  | Auditing `FLASHBACK WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |
| `REA` | `VARCHAR2(3)` |  | Auditing `READ WHENEVER SUCCESSFUL` / `UNSUCCESSFUL` |