---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ADVISOR_DIR_INSTANCES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ADVISOR_DIR_INSTANCES` provides information about all global instances for a directive.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DIRECTIVE_ID` | `NUMBER` | `NOT NULL` | Unique id for directive. The directive management engine automatically generates ID numbers. |
| `INSTANCE_ID` | `NUMBER` | `NOT NULL` | Unique id for the directive instance. The directive management engine automatically generates ID numbers. |
| `INSTANCE_NAME` | `VARCHAR2(128)` | `NOT NULL` | A user-assigned name for the directive instance. |
| `DATA` | `CLOB` | `NOT NULL` | An XML document that gives meaningful default values for all parts of the directive. |