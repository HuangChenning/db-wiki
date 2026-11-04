---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_DICTIONARY_LOAD.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.52 V$LOGMNR\_DICTIONARY\_LOAD

`V$LOGMNR_DICTIONARY_LOAD` displays information about LogMiner dictionaries for all active LogMiner sessions on the system.

Each query of this view will return one row for each attached LogMiner session. This view will not show valid information for LogMiner adhoc query clients.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | LogMiner session ID |
| `LOGMNR_UID` | `NUMBER` | LogMiner dictionary UID |
| `ACTION#` | `NUMBER` | Reserved for internal use |
| `OPCODE` | `NUMBER` | Reserved for internal use |
| `COMMAND` | `VARCHAR2(161)` | Current command being executed |
| `CURRENT_STATE` | `VARCHAR2(32)` | Summary information if `LOADED` = `ACTIVE` |
| `COMPLETED_ACTIONS` | `NUMBER` | The steps completed so far |
| `TOTAL_ACTIONS` | `NUMBER` | Total steps to complete |
| `LOADED` | `VARCHAR2(7)` | Status of the dictionary load:  - `YES` - dictionary has been loaded - `NO` - dictionary has not been loaded - `ACTIVE` - dictionary is in the process of being loaded |
| `PERCENT_DONE` | `NUMBER` | Percentage of the dictionary that has been loaded |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |