---
title: "V$SYSAUX_OCCUPANTS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3089.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYSAUX_OCCUPANTS` displays `SYSAUX` tablespace occupant information.

| Column | Datatype | Description |
| --- | --- | --- |
| `OCCUPANT_NAME` | `VARCHAR2(64)` | Occupant name |
| `OCCUPANT_DESC` | `VARCHAR2(64)` | Occupant description |
| `SCHEMA_NAME` | `VARCHAR2(64)` | Schema name for the occupant |
| `MOVE_PROCEDURE` | `VARCHAR2(64)` | Name of the move procedure; null if not applicable |
| `MOVE_PROCEDURE_DESC` | `VARCHAR2(64)` | Description of the move procedure |
| `SPACE_USAGE_KBYTES` | `NUMBER` | Current space usage of the occupant (in KB) |