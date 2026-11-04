---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_IOT.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 97 DBMS\_IOT

The `DBMS_IOT` package creates a table into which references to the chained rows for an index-organized table can be placed using the `ANALYZE` command. `DBMS_IOT` can also create an exception table into which references to the rows of an index-organized table that violate a constraint can be placed during the `enable_constraint` operation.

`DBMS_IOT` is not loaded during database installation. To install `DBMS_IOT,` run `dbmsiotc.sql`, available in the `ADMIN` directory.

This chapter contains the following topics:

- Summary of DBMS\_IOT Subprograms
	Note:
	With the introduction of logical-rowids for IOTs with Oracle Database Release 8.1, you no longer need to use the procedures contained in this package which is retained for backward compatibility only. It is however required for servers running with Oracle Database Release 8.0.

### 97.1 Summary of DBMS\_IOT Subprograms

This table lists and briefly describes the `DBMS_IOT` subprograms.

Table 97-1 DBMS\_IOT Package Subprograms

| Subprogram | Description |
| --- | --- |
| BUILD\_CHAIN\_ROWS\_TABLE Procedure | Creates a table into which references to the chained rows for an index-organized table can be placed using the `ANALYZE` command |
| BUILD\_EXCEPTIONS\_TABLE Procedure | Creates an exception table into which rows of an index-organized table that violate a constraint can be placed |

#### 97.1.1 BUILD\_CHAIN\_ROWS\_TABLE Procedure

This procedure creates a table into which references to the chained rows for an index-organized table can be placed using the `ANALYZE` command.

Syntax

```
DBMS_IOT.BUILD_CHAIN_ROWS_TABLE (
   owner               IN VARCHAR2,
   iot_name            IN VARCHAR2,
   chainrow_table_name IN VARCHAR2 default 'IOT_CHAINED_ROWS');
```

Parameters

Table 97-2 BUILD\_CHAIN\_ROWS\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Owner of the index-organized table. |
| `iot_name` | Index-organized table name. |
| `chainrow_table_name` | Intended name for the chained-rows table. |

Usage Notes

You should create a separate chained-rows table for each index-organized table to accommodate its primary key.

Examples

```
CREATE TABLE l(a char(16),b char(16), c char(16), d char(240), 
PRIMARY KEY(a,b,c)) ORGANIZATION INDEX pctthreshold 10 overflow;    
EXECUTE DBMS_IOT.BUILD_CHAIN_ROWS_TABLE('SYS','L','LC');
```

A chained-row table is created with the following columns:

```
Column Name                    Null?    Type  
------------------------------ -------- ----  
OWNER_NAME                              VARCHAR2(30)  
TABLE_NAME                              VARCHAR2(30)  
CLUSTER_NAME                            VARCHAR2(30)  
PARTITION_NAME                          VARCHAR2(30)  
SUBPARTITION_NAME                       VARCHAR2(30)  
HEAD_ROWID                              ROWID  
TIMESTAMP                               DATE  
A                                       CHAR(16)  
B                                       CHAR(16)  
C                                       CHAR(16)
```

#### 97.1.2 BUILD\_EXCEPTIONS\_TABLE Procedure

This procedure creates an exception table.

Rows of an index-organized table that violate a constraint can be placed into this table during the execution of the following SQL statements:

- `ALTER` `TABLE`... `ENABLE` `CONSTRAINT`... `EXCEPTIONS` `INTO`
- `ALTER` `TABLE`... `ADD` `CONSTRAINT`... `EXCEPTIONS` `INTO`

Syntax

```
DBMS_IOT.BUILD_EXCEPTIONS_TABLE (
   owner                 IN VARCHAR2,
   iot_name              IN VARCHAR2,
   exceptions_table_name IN VARCHAR2 default 'IOT_EXCEPTIONS');
```

Parameters

Table 97-3 BUILD\_EXCEPTIONS\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Owner of the index-organized table. |
| `iot_name` | Index-organized table name. |
| `exceptions_table_name` | Intended name for exception-table. |

Usage Notes

You should create a separate exception table for each index-organized table to accommodate its primary key.

Examples

```
EXECUTE DBMS_IOT.BUILD_EXCEPTIONS_TABLE('SYS','L','LE');
```

An exception table for the preceding index-organized table with the following columns:

```
Column Name                    Null?    Type  
------------------------------ -------- ----  
ROW_ID                                  VARCHAR2(30)  
OWNER                                   VARCHAR2(30)  
TABLE_NAME                              VARCHAR2(30)  
CONSTRAINT                              VARCHAR2(30)  
A                                       CHAR(16)  
B                                       CHAR(16)  
C                                       CHAR(16)
```