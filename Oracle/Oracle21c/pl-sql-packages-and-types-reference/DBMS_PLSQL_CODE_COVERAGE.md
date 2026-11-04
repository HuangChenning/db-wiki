---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_PLSQL_CODE_COVERAGE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 134 DBMS\_PLSQL\_CODE\_COVERAGE

The `DBMS_PLSQL_CODE_COVERAGE` package provides an interface for the collection of code coverage data of PL/SQL applications at the basic block level.

### 134.1 DBMS\_PLSQL\_CODE\_COVERAGE Overview

The ` DBMS_PLSQL_CODE_COVERAGE` package provides an interface for collecting code coverage information at the basic block level of PL/SQL applications. A basic block refers to a single entry single exit block of PL/SQL code. PL/SQL developers want to know how well their test infrastructure exercised their code. The coverage tables are created using the `CREATE_COVERAGE_TABLES` procedure.

A typical code coverage run in a session involves calls to:

- `START_COVERAGE`
- Run PL/SQL code
- `STOP_COVERAGE`

The `GET_BLOCK_MAP` function helps you calculate your total coverage.

See Also:

- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS-GUID-35842E6A-630A-418F-8314-6A30F1FBDF83) for more information about using PL/SQL basic block coverage to maintain quality
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNPLS-GUID-38A315DC-020B-41BD-90CD-DBF4D937EE83) for the `COVERAGE PRAGMA` syntax and semantics
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNPLS-GUID-DF63BC59-22C2-4BA8-9240-F74D505D5102) for more information about the PLSQL\_OPTIMIZE\_LEVEL compilation parameter

### 134.2 DBMS\_PLSQL\_CODE\_COVERAGE Security Model

The user must have `EXECUTE` privilege on the DBMS\_PLSQL\_CODE\_COVERAGE package.

The user must have `CREATE` privilege on the unit to collect coverage information about this unit.

PL/SQL basic block coverage data is collected when program units use `INTERPRETED` compilation ( parameter set `PLSQL_CODE_TYPE                 ` = `INTERPRETED`). PL/SQL basic block coverage data is not collected when program units use `NATIVE` compilation. You can disable the `NATIVE` compiler by setting the parameter `PLSQL_OPTIMIZE_LEVEL` <= `1`. Regardless of the compilation mode, coverage data for wrapped units is not collected.

### 134.3 DBMS\_PLSQL\_CODE\_COVERAGE Constants

The `DBMS_PLSQL_CODE_COVERAGE` package provides constants that are used with the `namespace` parameter of the `GET_BLOCK_MAP` function.

These constants are described in the following table.

Table 134-1 DBMS\_PLSQL\_CODE\_COVERAGE Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `function_namespace` | `NUMBER` | `1` | Specifies the function namespace |
| `package_spec_namespace` | `NUMBER` | `1` | Specifies the package specification namespace |
| `package_body_namespace` | `NUMBER` | `2` | Specifies the package definition (body) namespace |
| `procedure_namespace` | `NUMBER` | `1` | Specifies the procedure namespace |
| `trigger_namespace` | `NUMBER` | 3 | Specifies the trigger namespace |
| `type_spec_namespace` | `NUMBER` | `1` | Specifies the type specification namespace |
| `type_body_namespace` | `NUMBER` | `2` | Specifies the type definition (body) namespace |

### 134.4 DBMS\_PLSQL\_CODE\_COVERAGE Data Structures

Record Types

- MAP\_REC Record Type

Table Types

- T\_MAP\_REC Table Type

#### 134.4.1 MAP\_REC Record Type

The MAP\_REC record type defines the PL/SQL basic block location in the source code.

Syntax

```
TYPE map_rec IS RECORD (
    procedure_name VARCHAR2(32767),
    block_num      NUMBER,
    line           NUMBER,
    col            NUMBER,
    not_feasible   NUMBER);
```

Fields

Table 134-2 MAP\_REC Fields

| Field | Description |
| --- | --- |
| `procedure_name` | The name of the procedure containing the basic block |
| `block_num` | Identifies the basic block |
| `line` | Starting line of the basic block |
| `col` | Starting column of the basic block |
| `not_feasible` | Not\_feasible marking of the basic block |

#### 134.4.2 T\_MAP\_REC Table Type

The T\_MAP\_REC table type specifies the collection of PL/SQL basic blocks in a unit.

Syntax

```
TYPE t_map_rec IS TABLE OF map_rec;
```

### 134.5 Summary of DBMS\_PLSQL\_CODE\_COVERAGE Subprograms

This table lists the `DBMS_PLSQL_CODE_COVERAGE` subprograms and briefly describes them.

Table 134-3 DBMS\_PLSQL\_CODE\_COVERAGE Package Subprograms

| Subprogram | Description |  |
| --- | --- | --- |
| CREATE\_COVERAGE\_TABLES Procedure | Creates coverage tables |  |
| GET\_BLOCK\_MAP Function | Gets the mapping of basic blocks to PL/SQL source |  |
| START\_COVERAGE Function | Starts the coverage data collection in the user’s session and returns the RUN\_ID |  |
| STOP\_COVERAGE Procedure | Ends the current coverage run |  |

#### 134.5.1 CREATE\_COVERAGE\_TABLES Procedure

This procedure creates the tables used for coverage data collection.

Syntax

```
DBMS_PLSQL_CODE_COVERAGE.CREATE_COVERAGE_TABLES (
   FORCE_IT     IN BOOLEAN DEFAULT FALSE);
```

Parameters

| Parameter | Description |
| --- | --- |
| `FORCE_IT` | The default is to raise an error if the coverage tables already exists. If set to TRUE, the tables are dropped silently if the tables already exist, and new tables are created. |

Exceptions

Table 134-4 CREATE\_COVERAGE\_TABLES Exceptions

| Exception | Description |
| --- | --- |
| `COVERAGE_ERROR` | The `FORCE_IT` parameter is FALSE and the tables already exist. |

#### 134.5.2 GET\_BLOCK\_MAP Function

This function gets the mapping of basic blocks to PL/SQL source.

Syntax

```
DBMS_PLSQL_CODE_COVERAGE.GET_BLOCK_MAP(
                       unit_owner IN VARCHAR2,
                       unit_name  IN VARCHAR2,
                       namespace  IN POSITIVE)
  RETURN T_MAP_REC;
```

Table 134-5 Parameters

| Parameter | Description |
| --- | --- |
| `unit_owner` | The owner of the unit. The unit owner is case insensitive. If the unit\_owner is empty or NULL, then it defaults to the current schema. |
| `unit_name` | The unit whose mapping is to be gotten. The unit\_name is case insensitive. |
| `namespace` | Namespace to which this unit\_name gets resolved. See DBMS\_PLSQL\_CODE\_COVERAGE Constants for a list of valid namespace values. |

#### 134.5.3 START\_COVERAGE Function

This function starts the coverage data collection in the user’s session and returns a unique identifier `RUN_ID` for the run.

Syntax

```
DBMS_PLSQL_CODE_COVERAGE.START_COVERAGE (
   run_comment   IN VARCHAR2) 
   RETURN NUMBER;
```

Parameters

| Parameter | Description |
| --- | --- |
| `run_comment` | Allows the user to name a run and identify the test. |

#### 134.5.4 STOP\_COVERAGE Procedure

This procedure ends the current coverage run.

Syntax

```
DBMS_PLSQL_CODE_COVERAGE.STOP_COVERAGE;
```

Exceptions

Table 134-6 STOP\_COVERAGE Exceptions

| Exception | Description |
| --- | --- |
| `COVERAGE_ERROR` | An error is raised if the coverage tables do not exist. |