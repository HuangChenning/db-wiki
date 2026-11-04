---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_GG_SUPPORTED_PACKAGES.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).