---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_GG_SUPPORTED_PACKAGES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.342 DBA\_GG\_SUPPORTED\_PACKAGES

`DBA_GG_SUPPORTED_PACKAGES` provides details about supported procedure packages for Oracle GoldenGate replication.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(384)` | `NOT NULL` | Procedure package owner |
| `NAME` | `VARCHAR2(384)` | `NOT NULL` | Procedure package name |
| `FEATURE` | `VARCHAR2(384)` | `NOT NULL` | DBMS feature that the procedure package belongs to |
| `MIN_DB_VERSION` | `VARCHAR2(100)` |  | Minimum database version for the supported package |
| `MAX_DB_VERSION` | `VARCHAR2(100)` |  | Maximum database version for the supported package |
| `MIN_REDO_COMPAT_LEVEL` | `VARCHAR2(100)` |  | Minimum redo compatibility for the supported package |
| `MAX_REDO_COMPAT_LEVEL` | `VARCHAR2(100)` |  | Maximum redo compatibility for the supported package |
| `SUPPORTED_LEVEL` | `VARCHAR2(100)` |  | Supported level of the package |