---
title: DBMS_PLSQL_CODE_COVERAGE
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_PLSQL_CODE_COVERAGE.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_PLSQL_CODE_COVERAGE` package provides an interface for the collection of code coverage data of PL/SQL applications at the basic block level.

This chapter contains the following topics:

### DBMS\_PLSQL\_CODE\_COVERAGE Overview

The `DBMS_PLSQL_CODE_COVERAGE` package provides an interface for collecting code coverage information at the basic block level of PL/SQL applications. A basic block refers to a single entry single exit block of PL/SQL code. PL/SQL developers want to know how well their test infrastructure exercised their code. The coverage tables are created using the `CREATE_COVERAGE_TABLES` procedure.

A typical code coverage run in a session involves calls to:

- START\_COVERAGE
- Run PL/SQL code
- STOP\_COVERAGE

**See Also:**

- [*Oracle Database Development Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADFNS-GUID-35842E6A-630A-418F-8314-6A30F1FBDF83) for more information about using PL/SQL basic block coverage to maintain quality
- [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=LNPLS-GUID-38A315DC-020B-41BD-90CD-DBF4D937EE83) for the `COVERAGE PRAGMA` syntax and semantics
- [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=LNPLS-GUID-DF63BC59-22C2-4BA8-9240-F74D505D5102) for more information about the PLSQL\_OPTIMIZE\_LEVEL compilation parameter

### DBMS\_PLSQL\_CODE\_COVERAGE Security Model

The user must have `EXECUTE` privilege on the DBMS\_PLSQL\_CODE\_COVERAGE package.

The user must have `CREATE` privilege on the unit to collect coverage information about this unit.

Coverage information is not collected for wrapped units.

### Summary of DBMS\_PLSQL\_CODE\_COVERAGE Subprograms

This table lists the `DBMS_PLSQL_CODE_COVERAGE` subprograms and briefly describes them.

Table 1 DBMS\_PLSQL\_CODE\_COVERAGE Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATE\_COVERAGE\_TABLES Procedure | Creates coverage tables |
| START\_COVERAGE Function | Starts the coverage data collection in the user’s session and returns the RUN\_ID |
| STOP\_COVERAGE Procedure | Ends the current coverage run |

### CREATE\_COVERAGE\_TABLES Procedure

This procedure creates the tables used for coverage data collection.

**Syntax**

```md
DBMS_PLSQL_CODE_COVERAGE.CREATE_COVERAGE_TABLES (
   FORCE_IT     IN BOOLEAN DEFAULT FALSE);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `FORCE_IT` | The default is to raise an error if the coverage tables already exists. If set to TRUE, the tables are dropped silently if the tables already exist, and new tables are created. |

**Exceptions**

Table 2 CREATE\_COVERAGE\_TABLES Exceptions

| Exception | Description |
| --- | --- |
| `COVERAGE_ERROR` | The `FORCE_IT` parameter is FALSE and the tables already exist. |

### START\_COVERAGE Function

This function starts the coverage data collection in the user’s session and returns a unique identifier `RUN_ID` for the run.

**Syntax**

```md
DBMS_PLSQL_CODE_COVERAGE.START_COVERAGE (
   run_comment   IN VARCHAR2)
   RETURN NUMBER;
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `run_comment` | Allows the user to name a run and identify the test. |

### STOP\_COVERAGE Procedure

This procedure ends the current coverage run.

**Syntax**

```md
DBMS_PLSQL_CODE_COVERAGE.STOP_COVERAGE;
```

**Exceptions**

Table 3 STOP\_COVERAGE Exceptions

| Exception | Description |
| --- | --- |
| `COVERAGE_ERROR` | An error is raised if the coverage tables do not exist. |