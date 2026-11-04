---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/tuning-SQL-Plus.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This chapter provides information about how to tune SQL\*Plus for better performance. It discusses the following topics:

For information about tuning Oracle Database, see the [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=TGDBA).

### 9.1 About Tracing Statements

You can automatically get a report on the execution path used by the SQL optimizer and the statement execution statistics. The report is generated after successful SQL DML (that is, SELECT, DELETE, UPDATE and INSERT) statements. It is useful for monitoring and tuning the performance of these statements.

SQL\*Plus report output may differ for DML if dynamic sampling is in effect.

#### 9.1.1 Controlling the Autotrace Report

You can control the report by setting the AUTOTRACE system variable.

| Autotrace Setting | Result |
| --- | --- |
| SET AUTOTRACE OFF | No AUTOTRACE report is generated. This is the default. |
| SET AUTOTRACE ON EXPLAIN | The AUTOTRACE report shows only the optimizer execution path. |
| SET AUTOTRACE ON STATISTICS | The AUTOTRACE report shows only the SQL statement execution statistics. |
| SET AUTOTRACE ON | The AUTOTRACE report includes both the optimizer execution path and the SQL statement execution statistics. |
| SET AUTOTRACE TRACEONLY | Like SET AUTOTRACE ON, but suppresses the printing of the user's query output, if any. If STATISTICS is enabled, query data is still fetched, but not printed. |

To use this feature, you must create a PLAN\_TABLE table in your schema and then have the PLUSTRACE role granted to you. DBA privileges are required to grant the PLUSTRACE role. For information on how to grant a role and how to create the PLAN\_TABLE table, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF).

For more information about the roles and the PLAN\_TABLE, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF) and the AUTOTRACE variable of the [SET](SET.md) command.

Note:

SQL\*Plus AUTOTRACE does not support switching containers with the ALTER SESSION SET CONTAINER option. Statistical data gathered in this case may be inconsistent.

Example 9-1 Creating a PLAN\_TABLE

Run the following commands from your SQL\*Plus session to create the PLAN\_TABLE in the HR schema:

```
CONNECT HR 
@$ORACLE_HOME/rdbms/admin/utlxplan.sql 

Table created.
```

Example 9-2 Creating the PLUSTRACE Role

Run the following commands from your SQL\*Plus session to create the PLUSTRACE role and grant it to the DBA:

```
CONNECT / AS SYSDBA 
@$ORACLE_HOME/sqlplus/admin/plustrce.sql 

drop role plustrace;

Role dropped.

create role plustrace;

Role created.

grant plustrace to dba with admin option;

Grant succeeded.
```

Example 9-3 Granting the PLUSTRACE Role

Run the following commands from your SQL\*Plus session to grant the PLUSTRACE role to the HR user:

```
CONNECT / AS SYSDBA 
GRANT PLUSTRACE TO HR; 

Grant succeeded.
```

#### 9.1.2 Execution Plan

The Execution Plan shows the SQL optimizer's query execution path. Execution Plan output is generated using EXPLAIN PLAN and DBMS\_XPLAN.

#### 9.1.3 Statistics

The statistics are recorded by the server when your statement executes and indicate the system resources required to execute your statement. The results include the following statistics.

| Database Statistic Name | Description |
| --- | --- |
| recursive calls | Number of recursive calls generated at both the user and system level. Oracle Database maintains tables used for internal processing. When Oracle Database needs to make a change to these tables, it internally generates an internal SQL statement, which in turn generates a recursive call. |
| db block gets | Number of times a CURRENT block was requested. |
| consistent gets | Number of times a consistent read was requested for a block |
| physical reads | Total number of data blocks read from disk. This number equals the value of "physical reads direct" plus all reads into buffer cache. |
| redo size | Total amount of redo generated in bytes |
| bytes sent through Oracle Net Services to client | Total number of bytes sent to the client from the foreground processes. |
| bytes received through Oracle Net Services from client | Total number of bytes received from the client over Oracle Net. |
| Oracle Net Services round-trips to/from client | Total number of Oracle Net messages sent to and received from the client |
| sorts (memory) | Number of sort operations that were performed completely in memory and did not require any disk writes |
| sorts (disk) | Number of sort operations that required at least one disk write |
| rows processed | Number of rows processed during the operation |

The client referred to in the statistics is SQL\*Plus. Oracle Net refers to the generic process communication between SQL\*Plus and the server, regardless of whether Oracle Net is installed. You cannot change the default format of the statistics report.

For a more complete list of database statistics, see [Statistics Descriptions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=REFRN-GUID-2FBC1B7E-9123-41DD-8178-96176260A639). For more information about the statistics and how to interpret them, see [Gathering Database Statistics](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=TGDBA-GUID-CBB1716F-2B20-4575-ADCE-94E33BEA53EF).

```
LAST_NAME                     SALARY JOB_TITLE
------------------------- ---------- -----------------------------------
King                           24000 President
De Haan                        17000 Administration Vice President
Kochhar                        17000 Administration Vice President
Partners                       13500 Sales Manager
Russell                        14000 Sales Manager
Hartstein                      13000 Marketing Manager
6 rows selected.
 
Execution Plan
----------------------------------------------------------
Plan hash value: 2988506077
------------------------------------------------------------------------------
| Id  | Operation          | Name     | Rows | Bytes | Cost (%CPU)| Time     |
------------------------------------------------------------------------------
|   0 | SELECT STATEMENT   |          |    6 |   360 |     6  (17)| 00:00:01 |
|*  1 |  HASH JOIN         |          |    6 |   360 |     6  (17)| 00:00:01 |
|*  2 |   TABLE ACCESS FULL| EMPLOYEES|    6 |   204 |     3   (0)| 00:00:01 |
|   3 |   TABLE ACCESS FULL| JOBS     |   19 |   494 |     2   (0)| 00:00:01 |
------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
   1 - access("E"."JOB_ID"="J"."JOB_ID")
   2 - filter("E"."SALARY">12000)
 
Note
-----
   - dynamic sampling used for this statement
 
Statistics
----------------------------------------------------------
          0  recursive calls
          0  db block gets
         10  consistent gets
          0  physical reads
          0  redo size
        706  bytes sent via Oracle Net Services to client
        496  bytes received via Oracle Net Services from client
          2  Oracle Net Services roundtrips to/from client
          0  sorts (memory)
          0  sorts (disk)
          6  rows processed
```
```
6 rows selected.
 
Execution Plan
----------------------------------------------------------
Plan hash value: 2988506077
 
------------------------------------------------------------------------------
| Id  | Operation          | Name     | Rows | Bytes | Cost (%CPU)| Time     |
------------------------------------------------------------------------------
|   0 | SELECT STATEMENT   |          |    6 |   360 |     6  (17)| 00:00:01 |
|*  1 |  HASH JOIN         |          |    6 |   360 |     6  (17)| 00:00:01 |
|*  2 |   TABLE ACCESS FULL| EMPLOYEES|    6 |   204 |     3   (0)| 00:00:01 |
|   3 |   TABLE ACCESS FULL| JOBS     |   19 |   494 |     2   (0)| 00:00:01 |
------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
   1 - access("E"."JOB_ID"="J"."JOB_ID")
   2 - filter("E"."SALARY">12000)
 
Note
-----
   - dynamic sampling used for this statement
 
Statistics
----------------------------------------------------------
          0  recursive calls
          0  db block gets
         10  consistent gets
          0  physical reads
          0  redo size
        706  bytes sent via Oracle Net Services to client
        496  bytes received via Oracle Net Services from client
          2  Oracle Net Services roundtrips to/from client
          0  sorts (memory)
          0  sorts (disk)
          6  rows processed
```

This option is useful when you are tuning a large query, but do not want to see the query report.

Note:

Your output may vary depending on the server version and configuration.

Example 9-4 Tracing Statements for Performance Statistics and Query Execution Path

If the SQL buffer contains the following statement:

```
SELECT E.LAST_NAME, E.SALARY, J.JOB_TITLE
FROM EMPLOYEES E, JOBS J
WHERE E.JOB_ID=J.JOB_ID AND E.SALARY>12000;
```

The statement can be automatically traced when it is run:

```
SET AUTOTRACE ON
/
```

Example 9-5 Tracing Statements Without Displaying Query Data

To trace the same statement without displaying the query data, enter:

```
SET AUTOTRACE TRACEONLY
/
```

### 9.2 About Collecting Timing Statistics

Use the SQL\*Plus TIMING command to collect and display data on the amount of computer resources used to run one or more commands or blocks. TIMING collects data for an elapsed period of time, saving the data on commands run during the period in a timer.

See the [TIMING](TIMING.md) command, and About Tracing Statements for information about using AUTOTRACE to collect statistics.

To delete all timers, enter CLEAR TIMING.

### 9.3 Tracing Parallel and Distributed Queries

When you trace a statement in a parallel or distributed query, the Execution Plan output depends on the statement you use.

Example 9-6 Tracing Statements With Parallel Query Option

To trace a parallel query running the parallel query option:

```
create table D2_t1 (unique1 number) parallel -
(degree 6);

Table created.

create table D2_t2 (unique1 number) parallel -
(degree 6);

Table created.

create unique index d2_i_unique1 on d2_t1(unique1);

Index created.

set long 500 longchunksize 500
SET AUTOTRACE ON EXPLAIN
SELECT /*+ INDEX(B,D2_I_UNIQUE1) USE_NL(B) ORDERED -
*/ COUNT (A.UNIQUE1)
FROM D2_T2 A, D2_T1 B
WHERE A.UNIQUE1 = B.UNIQUE1;

Execution Plan
----------------------------------------------------------
Plan hash value: 107954098
 
--------------------------------------------------------------------------------------------------------------
| Id  | Operation                 | Name    | Rows |Bytes| Cost(%CPU)| Time     |    TQ  |IN-OUT| PQ Distrib |
--------------------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT          |         |    1 |  26 |    1   (0)| 00:00:01 |        |      |            |
|   1 |  SORT AGGREGATE           |         |    1 |  26 |           |          |        |      |            |
|   2 |   PX COORDINATOR          |         |      |     |           |          |        |      |            |
|   3 |    PX SEND QC (RANDOM)    | :TQ10001|    1 |  26 |           |          |  Q1,01 | P->S | QC (RAND)  |
|   4 |     SORT AGGREGATE        |         |    1 |  26 |           |          |  Q1,01 | PCWP |            |
|   5 |      NESTED LOOPS         |         |    1 |  26 |    1   (0)| 00:00:01 |  Q1,01 | PCWP |            |
|   6 |       PX RECEIVE          |         |      |     |           |          |  Q1,01 | PCWP |            |
|   7 |        PX SEND BROADCAST  | :TQ10000|      |     |           |          |  Q1,00 | P->P | BROADCAST  |
|   8 |         PX BLOCK ITERATOR |         |    1 |  13 |    0   (0)| 00:00:01 |  Q1,00 | PCWC |            |
|   9 |          TABLE ACCESS FULL| D2_T2   |    1 |  13 |    0   (0)| 00:00:01 |  Q1,00 | PCWP |            |
|  10 |       PX BLOCK ITERATOR   |         |    1 |  13 |    2   (0)| 00:00:01 |  Q1,01 | PCWC |            |
|* 11 |        TABLE ACCESS FULL  | D2_T1   |    1 |  13 |    2   (0)| 00:00:01 |  Q1,01 | PCWP |            |
--------------------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
  11 - filter("A"."UNIQUE1"="B"."UNIQUE1")
 
Note
-----
   - dynamic sampling used for this statement
```

Example 9-7 To monitor disk reads and buffer gets.

```
SET AUTOTRACE TRACEONLY STATISTICS
```

The following shows typical results:

```
Statistics
----------------------------------------------------------
        467  recursive calls
         27  db block gets
        147  consistent gets
         20  physical reads
       4548  redo size
        502  bytes sent via Oracle Net Services to client
        496  bytes received via Oracle Net Services from client
          2  Oracle Net Services roundtrips to/from client
         14  sorts (memory)
          0  sorts (disk)
          1  rows processed
```

If consistent gets or physical reads are high relative to the amount of data returned, it indicates that the query is expensive and needs to be reviewed for optimization. For example, if you are expecting less than 1,000 rows back and consistent gets is 1,000,000 and physical reads is 10,000, further optimization is needed.

Note:

You can also monitor disk reads and buffer gets using V$SQL or TKPROF.

### 9.4 Execution Plan Output in Earlier Databases

Execution Plan output from Oracle Database 9i Release 2 (9.2) or earlier is different.

Each line of the Execution Plan has a sequential line number. SQL\*Plus also displays the line number of the parent operation.

The Execution Plan consists of four columns displayed in the following order:

| Column Name | Description |
| --- | --- |
| `ID_PLUS_EXP` | Shows the line number of each execution step. |
| `PARENT_ID_PLUS_EXP` | Shows the relationship between each step and its parent. This column is useful for large reports. |
| `PLAN_PLUS_EXP` | Shows each step of the report. |
| `OBJECT_NODE_PLUS_EXP` | Shows database links or parallel query servers used. |

The format of the columns may be altered with the COLUMN command. For example, to stop the PARENT\_ID\_PLUS\_EXP column being displayed, enter

```
COLUMN PARENT_ID_PLUS_EXP NOPRINT
```

The Execution Plan output is generated using the EXPLAIN PLAN command.

When you trace a statement in a parallel or distributed query, the Execution Plan shows the cost based optimizer estimates of the number of rows (the cardinality). In general, the cost, cardinality and bytes at each node represent cumulative results. For example, the cost of a join node accounts for not only the cost of completing the join operations, but also the entire costs of accessing the relations in that join.

Lines marked with an asterisk (\*) denote a parallel or remote operation. Each operation is explained in the second part of the report. See [Distributed Transactions Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-C1B373BA-410E-4F38-8522-F72A74665919) for more information on parallel and distributed operations.

The second section of this report consists of three columns displayed in the following order

| Column Name | Description |
| --- | --- |
| `ID_PLUS_EXP` | Shows the line number of each execution step. |
| `OTHER_TAG_PLUS_EXP` | Describes the function of the SQL statement in the OTHER\_PLUS\_EXP column. |
| `OTHER_PLUS_EXP` | Shows the text of the query for the parallel server or remote database. |

The format of the columns may be altered with the COLUMN command.

### 9.5 About SQL\*Plus Script Tuning

Most performance benefit comes from tuning SQL queries executed in a script. This is done with tools like SQL\*Plus's AUTOTRACE command. It involves restructuring queries to make best use of the Oracle Database SQL optimizer. For information about Tuning SQL statements, see the [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=TGDBA).

The performance gains made by tuning SQL\*Plus-specific commands are smaller, but could be important for some applications. The following system variables and commands can influence SQL\*Plus performance.

#### 9.5.1 COLUMN NOPRINT

COLUMN NOPRINT turns off screen output and printing of the column heading and all values selected for the column.

It is better to remove an unneeded column from a SELECT then it is to use COLUMN NOPRINT to stop it displaying. Removing the column from the query means the SQL engine does not need to process it, or need to transfer the column data back to SQL\*Plus.

#### 9.5.2 SET APPINFO OFF

Sets automatic registering of scripts through the DBMS\_APPLICATION\_INFO package. Setting APPINFO OFF prevents administrators monitoring the performance and resource usage of scripts.

If many SQL scripts are being called, then turning APPINFO OFF stops internal SQL\*Plus calls to the database DBMS\_APPLICATION\_INFO package.

#### 9.5.3 SET ARRAYSIZE

Sets the number of rows that SQL\*Plus will fetch from the database at one time. Valid values are 1 to 5000.

The effectiveness of setting ARRAYSIZE depends on how well Oracle Database fills network packets and your network latency and throughput. In recent versions of SQL\*Plus and Oracle Database, ARRAYSIZE may have little effect. Overlarge sizes can easily take more SQL\*Plus memory which may decrease overall performance.

#### 9.5.4 SET DEFINE OFF

SET DEFINE OFF disables the parsing of commands to replace substitution variables with their values.

#### 9.5.5 SET FLUSH OFF

SET FLUSH OFF enables the operating system to buffer output. ON disables buffering and flushes output to the screen. Any benefit from setting FLUSH either ON or OFF depends on your operating system and data. The gain may be marginal.

Use OFF only when you run a script that does not require user interaction and whose output you do not need to see until the script finishes running.

#### 9.5.6 SET LINESIZE

SET LINESIZE sets the total number of characters that SQL\*Plus displays on one line before beginning a new line.

Keep LINESIZE as small as possible to avoid extra memory allocations and memory copying.

However, if LINESIZE is too small, columns that cannot fit next to each other are put on separate lines. This may reduce performance significantly.

#### 9.5.7 SET LONGCHUNKSIZE

SET LONGCHUNKSIZE sets the size of the increments SQL\*Plus uses to retrieve a BLOB, BFILE, CLOB, LONG, NCLOB or XMLType value.

Experiment with different sizes if LONGS or LOBs are being fetched.

#### 9.5.8 SET PAGESIZE

Sets the number of lines on each page of output.

Increase PAGESIZE to avoid printing headings frequently, or set it to 0 to prevent headings being displayed.

#### 9.5.9 SET SERVEROUTPUT

SET SERVEROUTPUT OFF suppresses the display output (DBMS\_OUTPUT.PUT\_LINE) of stored procedures or PL/SQL blocks in SQL\*Plus.

Setting SERVEROUTPUT OFF stops internal SQL\*Plus calls to the DBMS\_OUTPUT package done after user SQL statements.

#### 9.5.10 SET SQLPROMPT

Sets the SQL\*Plus command prompt.

Use the default prompt, "SQL> " to stop variable substitution occurring each time the prompt is displayed.

#### 9.5.11 SET TAB

Determines how SQL\*Plus formats white space in terminal output.

Setting TAB ON causes multiple spaces to be compressed in terminal output. Unless this significantly reduces the written data, the processing required may marginally outweigh any benefit.

#### 9.5.12 SET TERMOUT

SET TERMOUT OFF suppresses the display so that you can spool output from a script without seeing it on the screen.

If both spooling to file and writing to terminal are not required, use SET TERMOUT OFF in SQL scripts to disable terminal output.

#### 9.5.13 SET TRIMOUT ON SET TRIMSPOOL ON

SET TRIMOUT ON or SET TRIMSPOOL ON removes trailing blanks at the end of each displayed or spooled line.

Setting these variables ON can reduce the amount of data written. However, if LINESIZE is optimal, it may be faster to set the variables OFF. The SQL\*Plus output line is blank filled throughout the query processing routines so removing the spaces could take extra effort.

#### 9.5.14 UNDEFINE

Deletes substitution variables that you defined either explicitly (with the DEFINE command) or implicitly (with an argument to the START command or COLUMN NEW\_VAL|OLD\_VAL).

Use the UNDEFINE command to remove unnecessary substitution variables. This can reduce the time taken for any operation that uses '&', new\_value or old\_value variables.