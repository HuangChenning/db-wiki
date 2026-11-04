---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_TESTCASES.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.67 V$SQL\_TESTCASES

`V$SQL_TESTCASES` displays information about test cases exported by SQL Test Case Builder.

You can use this view in conjunction with the `V$DIAG_INCIDENT` view. Join the `INCIDENT_ID` column in this view with the `INCIDENT_ID` column in `V$DIAG_INCIDENT` to view information about the test case associated with a particular incident.

The `V$SQL_TESTCASES` view requires the existence of a TCB root directory named `SQL_TCB_DIR`. This view will not contain any rows if a TCB root directory does not exist, or if the TCB root directory exists with a name other than `SQL_TCB_DIR`. The operating system directory to which the TCB root directory refers must be writable by the owner of the Oracle Database binaries.

- In Oracle Autonomous Database environments, the TCB root directory is created automatically on each POD during provisioning.
- For on-premises databases, a user who has been granted the `DBA` role must explicitly create the TCB root directory. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-3E77892C-9259-4361-93FC-0C643AA51A88) for more information.

| Column | Datatype | Description |
| --- | --- | --- |
| `TESTCASE_NAME` | `VARCHAR2(512)` | Test case name |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement in the test case |
| `SQL_TEXT` | `VARCHAR2(1000)` | First 1000 characters of text for the SQL statement in the test case |
| `SQL_TEXT_FULL` | `CLOB` | Full text for the SQL statement in the test case, exposed as a CLOB column |
| `INCIDENT_ID` | `NUMBER` | ID for the incident associated with the test case |
| `PROBLEM_TYPE` | `NUMBER` | Type of problem for the incident associated with the test case. Possible values:  - `1`: Performance problem (`PROBLEM_TYPE_PERFORMANCE`) - `2`: Inconsistent results (`PROBLEM_TYPE_WRONG_RESULTS`) - `3`: Crash in compilation (`PROBLEM_TYPE_COMPILATION_ERROR`) - `4`: Crash in execution (`PROBLEM_TYPE_EXECUTION_ERROR`)  These numeric values, and their associated constant values shown in parentheses, correspond to the numeric and constant values for problem type constants in the `DBMS_SQLDIAG` package. See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-CEACAAE2-F425-496C-9FD3-40B208035060__CEGJCDDJ) for more information. |
| `CREATION_DATE` | `TIMESTAMP(6)` | Creation time for the incident associated with the test case |
| `STATUS` | `VARCHAR2(10)` | Current status for the incident associated with the test case. Possible values:  - `COMPLETE`: The test case export completed successfully - `INCOMPLETE`: The test case export failed due to an error |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$DIAG\_INCIDENT](V-DIAG_INCIDENT.md) "