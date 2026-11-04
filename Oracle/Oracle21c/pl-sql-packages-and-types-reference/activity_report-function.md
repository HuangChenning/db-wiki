---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/activity_report-function.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## ACTIVITY\_REPORT Function

This function reports auto zone map activity for a given time window.

Syntax

```
DBMS_AUTO_ZONEMAP.ACTIVITY_REPORT (
   start_time       IN TIMESTAMP WITH TIME ZONE  DEFAULT NULL,
   end_time         IN TIMESTAMP WITH TIME ZONE  DEFAULT NULL,
   type             IN VARCHAR2  DEFAULT NULL,
   section          IN VARCHAR2  DEFAULT NULL,
   level            IN VARCHAR2  DEFAULT NULL);
 RETURNS CLOB
```

Parameters

Table 36-2 ACTIVITY\_REPORT Function Parameters

| Parameter | Description |
| --- | --- |
| `start_time` | Timestamp from which auto zone map executions are observed for the report. If the value is `NULL`, the function reports everything from the beginning of auto zone map maintenance subject to purging.  The default value is `NULL`. |
| `end_time` | Timestamp until which auto zone map executions are observed for the report. If the value is `NULL`, the function reports everything to the end of auto zone map maintenance subject to purging.  The default value is `NULL`.  Note:  If you specify `NULL` for both `start_time` and `end_time`, the function will display the report from the last run. |
| `type` | Output type of the report. The possible values are `TEXT`, `XML`, and `HTML`.  The default value is `TEXT`. |
| `section` | Particular section in the report. The possible values are: - `SUMMARY`: Very high level numbers summary on new zone map created and maintained for the given time window. - `DETAILS`: Detailed summary report on names and other details of new zone map created and maintained for the given time window. It also includes findings details. - `ALL`: In addition to summary and details, it includes time series based execution / action logs.  The default value is `ALL`. |
| `level` | Format of the report. It represents the level of details with in each section. Possible values are: - `BASIC`: Represents very high level details in executive summary. You will only see numbers on zone map that were created, complete rebuilt and fast rebuilt. In new zone map details section, only new zone map name, date created and base table name re displayed. Under maintenance details section, only zone map name, previous state and current state are displayed. Under findings section, only object name and blacklist reason are displayed. Under action logs section, only important time series based log messages pertaining to zone map creation and maintenance are displayed. - `TYPICAL`: Full overview on executive summary section. Under `new zone map details` section, schema name, column list, and date created are displyed. Under `zone map maintenance details` section, refresh type and date are displayed. In `findings` section, timestamp and exception message are displayed. In `action logs` section more comprehensive logs than basic, which will have information about candidate column list, findings information, and creation DDLs are displayed. This is the default value. - `ALL`: On top of typical level, DOP used for each operation for creating or maintaining zone map, time took to process each DDL and other details in action logs are displayed. All log messages with details on clustering ratios of columns, exception messages and other details are also displayed. |

Return Values

Report in `CLOB` format. The default report format is `TEXT`. Possible formats are `TEXT`, `XML`, and `HTML`.

Usage Notes

- DBMS\_AUTO\_ZONEMAP.ACTIVITY\_REPORT(): returns report for all the execution history of last execution in `TEXT` format and all the sections will be displayed with typical level.
- DBMS\_AUTO\_ZONEMAP.ACTIVITY\_REPORT(systimestamp-2, NULL): returns report for all the execution history for last two days in `TEXT` format and all the sections will be displayed with typical level.
- DBMS\_AUTO\_ZONEMAP.ACTIVITY\_REPORT(NULL, systimestamp-1): returns report for all the execution history from beginning to yesterday in `TEXT` format and all the sections will be displayed with typical level.
- DBMS\_AUTO\_ZONEMAP.ACTIVITY\_REPORT(NULL, NULL, ‘HTML’, ‘DETAILS’, ‘BASIC’): returns last execution’s report in `HTML` format and only details section will be displayed with only basic details in each section
- DBMS\_AUTO\_ZONEMAP.ACTIVITY\_REPORT(systimestamp – 2, systimestmap, ‘TEXT’, ‘ALL’,’TYPICAL’): returns report for last 48 hours in text format and all the sections will be displayed with typical details.