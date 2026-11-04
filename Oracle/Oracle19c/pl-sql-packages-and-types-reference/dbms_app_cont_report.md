---
title: DBMS_APP_CONT_REPORT
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/dbms_app_cont_report.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

This procedure generates a report of ACCHK trace collected while `ACCHK_SET(TRUE)`.

### DBMS\_APP\_CONT\_REPORT Security Model

Applications must have the `EXECUTE` privilege on the `DBMS_APP_CONT_REPORT` package.

### Summary of DBMS\_APP\_CONT\_REPORT Subprograms

This topic lists the `DBMS_APP_CONT_REPORT` subprograms in alphabetical order and briefly describes them.

Table 1 DBMS\_APP\_CONT\_REPORT Package

| Subprogram | Description |
| --- | --- |
| ACCHK\_REPORT Procedure | This procedure provides a report of your run. The data is derived from the \`acchk\` views. |

### ACCHK\_REPORT Procedure

This procedure generates a report of your run. The data is derived from the `acchk` views.

**Syntax**

```md
DBMS_APP_CONT_REPORT.ACCHK_REPORT (
   level                    IN VARCHAR2,
   service_name             IN VARCHAR2);
```

**Parameters**

Table 2 ACCHK\_REPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `level` | These are constants.  - `SUMMARY` -summary report only (default) - `WARNING` -summary and warnings - `FULL` -summary and all workload capture, including where there are no warnings |
| `service_name` | The service name qualifier (Optional).  The value `NULL` applies to all `service_names`. |

**Procedure Exceptions**

The exceptions of `DBMS_APP_CONT_REPORT.ACCHK_REPORT` procedure are as follows:

- `20000` -Invalid report level parameter.

**Example**

```md
SET SERVEROUTPUT ON FORMAT WRAPPED

SET LINESIZE 180
DBMS_APP_CONT_REPORT.ACCHK_REPORT(DBMS_APP_CONT_REPORT.FULL);

SET SERVEROUTPUT ON FORMAT WRAPPED

SET LINESIZE 180
DBMS_APP_CONT_REPORT.ACCHK_REPORT(DBMS_APP_CONT_REPORT.WARNING);

SET SERVEROUTPUT ON FORMAT WRAPPED

SET LINESIZE 180
DBMS_APP_CONT_REPORT.ACCHK_REPORT(DBMS_APP_CONT_REPORT.SUMMARY);
```