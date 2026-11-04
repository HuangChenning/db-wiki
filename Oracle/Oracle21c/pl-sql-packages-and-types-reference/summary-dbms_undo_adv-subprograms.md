---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/summary-dbms_undo_adv-subprograms.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 192.1 Summary of DBMS\_UNDO\_ADV Subprograms

This topic lists the `DBMS_UNDO_ADV` subprograms in alphabetical order and briefly describes them.

Table 192-1 DBMS\_UNDO\_ADV Package Subprograms

| Subprogram | Description |
| --- | --- |
| [BEST\_POSSIBLE\_RETENTION](best_possible_retention-function.md) Function | Returns the best possible value for the `undo_retention` parameter that the current undo tablespace can satisfy in order to maximize the usage of the current undo tablespace based on the historical information of the given period. |
| [LONGEST QUERY](longest_query-function.md) Function | This function returns the duration of the longest query, in seconds, for a given period. |
| [RBU\_MIGRATION](rbu_migration-function.md) Function | Estimates the undo tablespace needed for migration from manual to automatic undo management. |
| [REQUIRED\_RETENTION](required_retention-function.md) Function | Returns the required value for the `undo_retention` parameter to satisfy the longest query based on undo statistics available for a given period. |
| [REQUIRED\_UNDO\_SIZE](required_undo_size-function.md) Function | Returns the required undo tablespace size in MB to satisfy a certain undo retention value based on undo statistics available for a given period. |
| [UNDO\_ADVISOR](undo_advisor-function.md) Function | Uses the advisor framework to check if there is any problem with the current instance. It also provides recommendations. |
| [UNDO\_AUTOTUNE](undo_autotune-function.md) Function | Determines whether auto-tuning of undo retention is enabled for the current undo tablespace. |
| [UNDO\_HEALTH](undo_health-function.md) Function | Checks whether there is any problem with the current setting of undo retention and undo tablespace size based on the historical information of a given period and provides recommendations to fix the problem. |
| [UNDO\_INFO](undo_info-function.md) Function | Retrieves information about the undo tablespace of the current instance. |