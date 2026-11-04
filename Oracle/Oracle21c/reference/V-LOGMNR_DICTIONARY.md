---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_DICTIONARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.51 V$LOGMNR\_DICTIONARY

| Column | Datatype | Description |
| --- | --- | --- |
| `DB_NAME` | `VARCHAR2(9)` | Name of the database |
| `DB_ID` | `NUMBER` | Database ID |
| `DB_CREATED` | `DATE` | Creation date of the source database (corresponds to the `CREATED` column in the `V$DATABASE` view) |
| `TIMESTAMP` | `DATE` | Date when the dictionary was created |
| `RESET_SCN` | `NUMBER` | Reset log SCN when the dictionary was created |
| `RESET_SCN_TIME` | `DATE` | Timestamp of the reset log SCN when the dictionary was created |
| `DB_VERSION_TIME` | `DATE` | Version time for the source database (corresponds to the `VERSION_TIME` column in the `V$DATABASE` view) |
| `DB_CHARACTER_SET` | `VARCHAR2(30)` | Character set of the source database |
| `DB_VERSION` | `VARCHAR2(64)` | This column is deprecated. |
| `DB_STATUS` | `VARCHAR2(64)` | This column is deprecated. |
| `DICTIONARY_SCN` | `NUMBER` | Database checkpoint SCN at which the dictionary was created |
| `ENABLED_THREAD_MAP` | `RAW(16)` | This column is deprecated. |
| `DB_TXN_SCN` | `NUMBER` | SCN at which the dictionary was created |
| `FILENAME` | `VARCHAR2(512)` | Dictionary file name |
| `INFO` | `VARCHAR2(32)` | Informational/Status message  `BAD_DATE` indicates that the SCN of the dictionary file does not match the SCN range of the log files |
| `STATUS` | `NUMBER` | A NULL indicates a valid dictionary file for the list of log files. A non-NULL value indicates further information is contained in the INFO column as a text string. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |