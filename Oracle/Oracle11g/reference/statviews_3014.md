---
title: DBA_ADVISOR_DIR_INSTANCES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3014.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_DIR_INSTANCES` provides information about all global instances for a directive.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DIRECTIVE_ID` | `NUMBER` | `NOT NULL` | Unique id for directive. The directive management engine automatically generates ID numbers. |
| `INSTANCE_ID` | `NUMBER` | `NOT NULL` | Unique id for the directive instance. The directive management engine automatically generates ID numbers. |
| `INSTANCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | A user-assigned name for the directive instance. |
| `DATA` | `CLOB` | `NOT NULL` | An XML document that gives meaningful default values for all parts of the directive. |