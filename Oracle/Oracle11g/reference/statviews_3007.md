---
title: DBA_ADDM_TASK_DIRECTIVES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3007.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADDM_TASK_DIRECTIVES` displays information about all ADDM task directives in the database.

Related View

`USER_ADDM_TASK_DIRECTIVES` displays information about all ADDM task directives in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` |  | An ADDM advisor task identifier to which the directive instance is associated |
| `TASK_NAME` | `VARCHAR2(30)` |  | An ADDM advisor task to which the directive instance is associated |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | Database user who owns the ADDM task instance |
| `SEQ_ID` | `NUMBER` | `NOT NULL` | Unique ID for the directive instance. The directive management engine automatically generates ID numbers. |
| `INSTANCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | A user-assigned name for the ADDM task directive instance |
| `DIRECTIVE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the ADDM task directive, shown in the language used by the current session |