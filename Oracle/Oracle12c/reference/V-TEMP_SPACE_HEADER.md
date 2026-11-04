---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-TEMP_SPACE_HEADER.html
tags:
  - oracle
  - 12c
  - reference
---

`V$TEMP_SPACE_HEADER` displays aggregate information per file per LOCALLY MANAGED temporary tablespace regarding how much space is currently being used and how much is free as identified in the space header.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the temporary tablespace |
| `FILE_ID` | `NUMBER` |  | Absolute file number |
| `BYTES_USED` | `NUMBER` |  | How many bytes are in use |
| `BLOCKS_USED` | `NUMBER` |  | How many blocks are in use |
| `BYTES_FREE` | `NUMBER` |  | How many bytes are free |
| `BLOCKS_FREE` | `NUMBER` |  | How many blocks are free |
| `RELATIVE_FNO` | `NUMBER` |  | The relative file number for the file |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |