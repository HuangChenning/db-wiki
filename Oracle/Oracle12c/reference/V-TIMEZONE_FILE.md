---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-TIMEZONE_FILE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$TIMEZONE_FILE` describes the time zone file that is currently in use by the database.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILENAME` | `VARCHAR2(20)` | Time zone file name |
| `VERSION` | `NUMBER` | Time zone file version |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |