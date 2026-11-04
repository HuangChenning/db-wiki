---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MAPPED_SQL.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.74 V$MAPPED\_SQL

`V$MAPPED_SQL` lists the SQL statements that are translated and mapped in memory to a different SQL statement for execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SQL_TEXT` | `VARCHAR2(1000)` | First 1000 characters of the original SQL text |
| `SQL_FULLTEXT` | `CLOB` | Full text for the original SQL statement |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the original SQL statement |
| `HASH_VALUE` | `NUMBER` | Hash value of the original SQL statement |
| `MAPPED_SQL_TEXT` | `VARCHAR2(1000)` | First 1000 characters of the mapped SQL text |
| `MAPPED_SQL_FULLTEXT` | `CLOB` | Full text for the mapped SQL statement |
| `MAPPED_SQL_ID` | `VARCHAR2(13)` | SQL identifier of the mapped SQL statement |
| `MAPPED_HASH_VALUE` | `NUMBER` | Hash value of the mapped SQL statement |
| `SQL_TRANSLATION_PROFILE_ID` | `NUMBER` | A non-NULL value specifies the object ID of the SQL translation profile used to translate the SQL statement into the mapped SQL statement |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `TRANSLATION_TIMESTAMP` | `DATE` | Time this SQL statement was translated |
| `TRANSLATION_CPU_TIME` | `NUMBER` | CPU time used to translate this SQL statement |
| `TRANSLATION_ELAPSED_TIME` | `NUMBER` | Elapsed time used to translate this SQL statement |
| `TRANSLATION_METHOD` | `VARCHAR2(10)` | Method used to translate this SQL statement |
| `DICTIONARY_SQL_ID` | `VARCHAR2(13)` | SQL ID of SQL text in custom translation dictionary used to translate this SQL statement |
| `USE_COUNT` | `NUMBER` | Number of times this translation has been used |