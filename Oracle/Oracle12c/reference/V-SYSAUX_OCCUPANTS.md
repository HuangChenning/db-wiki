---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SYSAUX_OCCUPANTS.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | Description |
| --- | --- | --- |
| `OCCUPANT_NAME` | `VARCHAR2(64)` | Occupant name |
| `OCCUPANT_DESC` | `VARCHAR2(64)` | Occupant description |
| `SCHEMA_NAME` | `VARCHAR2(64)` | Schema name for the occupant |
| `MOVE_PROCEDURE` | `VARCHAR2(64)` | Name of the move procedure; null if not applicable |
| `MOVE_PROCEDURE_DESC` | `VARCHAR2(64)` | Description of the move procedure |
| `SPACE_USAGE_KBYTES` | `NUMBER` | Current space usage of the occupant (in KB) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |