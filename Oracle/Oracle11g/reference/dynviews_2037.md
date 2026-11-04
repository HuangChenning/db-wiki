---
title: "V$LOGMNR_DICTIONARY_LOAD"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2037.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGMNR_DICTIONARY_LOAD` displays information about LogMiner dictionaries for all active LogMiner sessions on the system. Each query of this view will return one row for each attached LogMiner session. This view will not show valid information for LogMiner adhoc query clients.

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
| `LOADED` | `VARCHAR2(7)` | Status of the dictionary load: - `YES` - dictionary has been loaded - `NO` - dictionary has not been loaded - `ACTIVE` - dictionary is in the process of being loaded |
| `PERCENT_DONE` | `NUMBER` | Percentage of the dictionary that has been loaded |