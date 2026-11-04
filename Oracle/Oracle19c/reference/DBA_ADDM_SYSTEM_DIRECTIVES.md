---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_ADDM_SYSTEM_DIRECTIVES.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.11 DBA\_ADDM\_SYSTEM\_DIRECTIVES

`DBA_ADDM_SYSTEM_DIRECTIVES` displays information about global instances for ADDM system directives.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INSTANCE_ID` | `NUMBER` | `NOT NULL` | Unique ID for the directive instance. The directive management engine automatically generates ID numbers. |
| `INSTANCE_NAME` | `VARCHAR2(128)` | `NOT NULL` | User-assigned name for the directive instance. |
| `DIRECTIVE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the ADDM system directive, shown in the language used by the current session |