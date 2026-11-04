---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/HS_INST_CAPS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.199 HS\_INST\_CAPS

`HS_INST_CAPS` contains information about instance-specific capabilities (that is, features).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAP_NUMBER` | `NUMBER ` | `NOT NULL` | Capability number |
| `CAP_DESCRIPTION` | `VARCHAR2(255)` |  | Capability description |
| `CONTEXT` | `NUMBER` |  | Context in which this capability is applicable |
| `TRANSLATION` | `VARCHAR2(255)` |  | Valid for functions; contains translation to FDS dialect |
| `ADDITIONAL_INFO` | `NUMBER` |  | Additional flags for internal use |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS class (for example, ODBC, DB2) |
| `FDS_INST_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS instance |
| `FDS_CLASS_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_INST_ID` | `NUMBER` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |