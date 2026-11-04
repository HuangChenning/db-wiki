---
title: DBA_ADDM_SYSTEM_DIRECTIVES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3006.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADDM_SYSTEM_DIRECTIVES` displays information about global instances for ADDM system directives.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INSTANCE_ID` | `NUMBER` | `NOT NULL` | Unique ID for the directive instance. The directive management engine automatically generates ID numbers. |
| `INSTANCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | User-assigned name for the directive instance. |
| `DIRECTIVE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the ADDM system directive, shown in the language used by the current session |