---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_APP_STATEMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.109 DBA\_APP\_STATEMENTS

`DBA_APP_STATEMENTS` describes all statements from all the applications in the application container.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates.  Possible values include: - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n=1 if the row originates in root) |
| `STATEMENT_ID` | `NUMBER` |  | Statement ID |
| `CAPTURE_TIME` | `DATE` | `NOT NULL` | Time of capture of the application statement |
| `APP_STATEMENT` | `CLOB` |  | Application statement |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application whose statement was captured |
| `APP_STATUS` | `VARCHAR2(12)` |  | Status of the application when the statement was captured |
| `PATCH_NUMBER` | `NUMBER` |  | Patch number of patch installation when the statement was captured |
| `VERSION_NUMBER` | `NUMBER` |  | Version number when the statement was captured |
| `SESSION_ID` | `NUMBER` |  | Unique session ID when the statement was captured |
| `OPCODE` | `NUMBER` | `NOT NULL` | Operation code indicating the statement type |