---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_RESOURCE_MANAGER.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 148 DBMS\_RESOURCE\_MANAGER

The `DBMS_RESOURCE_MANAGER` package maintains plans, consumer groups, and plan directives. It also provides semantics so that you may group together changes to the plan schema.

This chapter contains the following topics:

See Also:

For more information on using the Database Resource Manager, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF)

### 148.1 DBMS\_RESOURCE\_MANAGER Deprecated Subprograms

The SET\_INITIAL\_CONSUMER\_GROUP Procedure has been deprecated with Oracle Database 11g.

- SET\_INITIAL\_CONSUMER\_GROUP Procedure

Note:

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

### 148.2 DBMS\_RESOURCE\_MANAGER Security Model

The invoker must have the `ADMINISTER_RESOURCE_MANAGER` system privilege to execute these procedures.

The procedures to grant and revoke this privilege are in the package [DBMS\_RESOURCE\_MANAGER\_PRIVS](DBMS_RESOURCE_MANAGER_PRIVS.md).

### 148.3 DBMS\_RESOURCE\_MANAGER Constants

The `DBMS_RESOURCE_MANAGER` package defines several constants for specifying parameter values.

These are shown in the following table.

Table 148-1 DBMS\_RESOURCE\_MANAGER Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `CLIENT_ID` | `VARCHAR2(30)` | `CLIENT_ID` | Client identifier of the session |
| `CLIENT_MACHINE` | `VARCHAR2(30)` | `CLIENT_MACHINE` | Name of the computer from which the client is making the connection |
| `CLIENT_OS_USER` | `VARCHAR2(30)` | `CLIENT_OS_USER` | Operating system user name of the client that is logging in |
| `CLIENT_PROGRAM` | `VARCHAR2(30)` | `CLIENT_PROGRAM` | Name of the client program used to log in to the server |
| `MODULE_NAME` | `VARCHAR2(30)` | `MODULE_NAME` | Module name in the currently running application as set by the [SET\_MODULE Procedure](DBMS_APPLICATION_INFO.md) in the [DBMS\_APPLICATION\_INFO](DBMS_APPLICATION_INFO.md) package, or the equivalent OCI attribute setting |
| `MODULE_NAME_ACTION` | `VARCHAR2(30)` | `MODULE_NAME_ACTION` | A combination of the current module and the action being performed as set by either of the following procedures in the [DBMS\_APPLICATION\_INFO](DBMS_APPLICATION_INFO.md) package, or their equivalent OCI attribute setting:  - [SET\_MODULE Procedure](DBMS_APPLICATION_INFO.md) - [SET\_ACTION Procedure](DBMS_APPLICATION_INFO.md)  The attribute is specified as the module name followed by a period (.), followed by the action name (module\_name.action\_name). |
| `ORACLE_FUNCTION` | `VARCHAR2(30)` | `ORACLE_FUNCTION` | Function the session is currently executing. Valid functions are the `BACKUP`, `COPY`, `DATALOAD`, and `INMEMORY`. `BACKUP` is set for sessions that are doing backup operations using `RMAN`. `COPY` is set for sessions that are doing image copies using `RMAN`. `DATALOAD` is set for sessions that are loading data using Oracle Data Pump. |
| `ORACLE_USER` | `VARCHAR2(30)` | `ORACLE_USER` | Oracle Database user name |
| `SERVICE_MODULE ` | `VARCHAR2(30)` | `SERVICE_MODULE ` | Combination of service and module names in this form: service\_name.module\_name |
| `SERVICE_MODULE_ACTION ` | `VARCHAR2(30)` | `SERVICE_MODULE_ACTION ` | Combination of service name, module name, and action name, in this form: service\_name.module\_name.action\_name |
| `SERVICE_NAME ` | `VARCHAR2(30)` | `SERVICE_NAME ` | Service name used by the client to establish a connection |

### 148.4 Summary of DBMS\_RESOURCE\_MANAGER Subprograms

This table lists the `DBMS_RESOURCE_MANAGER` subprograms and briefly describes them.

Table 148-2 DBMS\_RESOURCE\_MANAGER Package Subprograms

| Subprogram | Description |
| --- | --- |
| BEGIN\_SQL\_BLOCK Procedure | Indicates the start of a block of SQL statements to be treated as a group by resource manager |
| CALIBRATE\_IO Procedure | Calibrates the I/O capabilities of storage |
| CLEAR\_PENDING\_AREA Procedure | Clears the work area for the resource manager |
| CREATE\_CATEGORY Procedure | Creates a new resource consumer group category |
| CREATE\_CDB\_PLAN Procedure | Creates entries which define consolidation resource plans. |
| CREATE\_CDB\_PLAN\_DIRECTIVE Procedure | Creates the plan directives of the consolidation resource plan |
| CREATE\_CDB\_PROFILE\_DIRECTIVE Procedure | Creates the performance profile directives of the consolidation resource plan |
| CREATE\_CONSUMER\_GROUP Procedure | Creates entries which define resource consumer groups |
| CREATE\_PENDING\_AREA Procedure | Creates a work area for changes to resource manager objects |
| CREATE\_PLAN Procedure | Creates entries which define resource plans |
| CREATE\_PLAN\_DIRECTIVE Procedure | Creates resource plan directives |
| CREATE\_SIMPLE\_PLAN Procedure | Creates a single-level resource plan containing up to eight consumer groups in one step |
| DELETE\_CATEGORY Procedure | Deletes an existing resource consumer group category |
| DELETE\_CDB\_PLAN Procedure | Deletes the consolidation resource plan |
| DELETE\_CDB\_PLAN\_DIRECTIVE Procedure | Deletes the plan directive of the consolidation resource plan |
| DELETE\_CDB\_PROFILE\_DIRECTIVE Procedure | Deletes the performance profile directive of the consolidation resource plan |
| DELETE\_CONSUMER\_GROUP Procedure | Deletes entries which define resource consumer groups |
| DELETE\_PLAN Procedure | Deletes the specified plan as well as all the plan directives it refers to |
| DELETE\_PLAN\_CASCADE Procedure | Deletes the specified plan as well as all its descendants (plan directives, subplans, consumer groups) |
| DELETE\_PLAN\_DIRECTIVE Procedure | Deletes resource plan directives |
| DEQUEUE\_PARALLEL\_STATEMENT Procedure | Dequeues a parallel statement from the parallel statement queue |
| END\_SQL\_BLOCK Procedure | Indicates the end of a block of SQL statements that should be treated as a group by resource manager |
| SET\_CONSUMER\_GROUP\_MAPPING Procedure | Adds, deletes, or modifies entries for the login and run-time attribute mappings |
| SET\_CONSUMER\_GROUP\_MAPPING\_PRI Procedure | Creates the session attribute mapping priority list |
| SET\_INITIAL\_CONSUMER\_GROUP Procedure | Assigns the initial resource consumer group for a user (Caution: Deprecated Subprogram) |
| SUBMIT\_PENDING\_AREA Procedure | Submits pending changes for the resource manager |
| SWITCH\_CONSUMER\_GROUP\_FOR\_SESS Procedure | Changes the resource consumer group of a specific session |
| SWITCH\_CONSUMER\_GROUP\_FOR\_USER Procedure | Changes the resource consumer group for all sessions with a given user name |
| SWITCH\_PLAN Procedure | Sets the current resource manager plan |
| UPDATE\_CATEGORY Procedure | Updates an existing resource consumer group category |
| UPDATE\_CDB\_AUTOTASK\_DIRECTIVE Procedure | Updates the plan directives with regard to automated maintenance tasks |
| UPDATE\_CDB\_DEFAULT\_DIRECTIVE Procedure | Updates the default values for a consolidation plan |
| UPDATE\_CDB\_PLAN Procedure | Updates the consolidation resource plan |
| UPDATE\_CDB\_PLAN\_DIRECTIVE Procedure | Updates the plan directives for a consolidation resource plan |
| UPDATE\_CDB\_PROFILE\_DIRECTIVE Procedure | Updates the performance profile directives of the consolidation resource plan |
| UPDATE\_CONSUMER\_GROUP Procedure | Updates entries which define resource consumer groups |
| UPDATE\_PLAN Procedure | Updates entries which define resource plans |
| UPDATE\_PLAN\_DIRECTIVE Procedure | Updates resource plan directives |
| VALIDATE\_PENDING\_AREA Procedure | Validates pending changes for the resource manager |

#### 148.4.1 BEGIN\_SQL\_BLOCK Procedure

This procedure, to be used with parallel statement queuing, indicates the start of a block of SQL statements that should be treated as a group by resource manager.

Syntax

```
DBMS_RESOURCE_MANAGER.BEGIN_SQL_BLOCK;
```

Usage Notes

For more information, see ["Parallel Statement Queuing"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=VLDBG1396) and ["Managing Parallel Statement Queuing with Resource Manager"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=VLDBG14020) in Oracle Database VLDB and Partitioning Guide.

#### 148.4.2 CALIBRATE\_IO Procedure

This procedure calibrates the I/O capabilities of storage. Calibration status is available from the `V$IO_CALIBRATION_STATUS` view and results for a successful calibration run are located in `DBA_RSRC_IO_CALIBRATE` table.

Syntax

```
DBMS_RESOURCE_MANAGER.CALIBRATE_IO (
   num_physical_disks      IN  PLS_INTEGER DEFAULT 1,
   max_latency             IN  PLS_INTEGER DEFAULT 20,
   max_iops                OUT PLS_INTEGER,
   max_mbps                OUT PLS_INTEGER,
   actual_latency          OUT PLS_INTEGER);
```

Parameters

Table 148-3 CALIBRATE\_IO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `num_physical_disks` | Approximate number of physical disks in the database storage. This parameter is used to determine the initial I/O load for the calibration run. |
| `max_latency` | Maximum tolerable latency in milliseconds for database-block-sized IO requests |
| `max_iops` | Maximum number of I/O requests per second that can be sustained. The I/O requests are randomly-distributed, database-block-sized reads. |
| `max_mbps` | Maximum throughput of I/O that can be sustained, expressed in megabytes per second. The I/O requests are randomly-distributed, 1 megabyte reads. |
| `actual_latency` | Average latency of database-block-sized I/O requests at `max_iops` rate, expressed in milliseconds |

Usage Notes

- Only users with the SYSDBA privilege can run this procedure. Qualified users must also turn on `timed_statistics`, and ensure `asynch_io` is enabled for datafiles. This can be achieved by setting `filesystemio_options` to either `ASYNCH` or `SETALL`. One can also query the `asynch_io` status by means of the following SQL statement:
	```
	col name format a50
	SELECT name, asynch_io FROM v$datafile f,v$iostat_file i
	  WHERE f.file#        = i.file_no
	  AND   filetype_name  = 'Data File'
	 /
	```
- Only one calibration can be run at a time. If another calibration is initiated at the same time, it will fail.
- For an Oracle Real Application Clusters (Oracle RAC) database, the workload is simultaneously generated from all instances.
- In a multitenant container database (CDB), calibration can only be run from the CDB root (`CDB$ROOT`).
- Calibration is extremely disruptive to the database performance. It is strongly recommended to run calibration only when database users can tolerate severe deterioration to database performance.
- For optimal calibration results, no other database workloads should be running.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=TGDBA385) for more information about calibration

Examples

Example of using I/O Calibration procedure

```
SET SERVEROUTPUT ON
DECLARE
  lat  NUMBER;
  iops INTEGER;
  mbps INTEGER;
BEGIN
-- DBMS_RESOURCE_MANAGER.CALIBRATE_IO (<DISKS>, <MAX_LATENCY>, iops, mbps, lat);
   DBMS_RESOURCE_MANAGER.CALIBRATE_IO (2, 10, iops, mbps, lat);
 
end;
/
```

View for I/O calibration results

```
SQL> desc V$IO_CALIBRATION_STATUS
  Name                                      Null?    Type
  ----------------------------------------- -------- ----------------------------
  STATUS                                             VARCHAR2(13)
  CALIBRATION_TIME                                   TIMESTAMP(3)
 
SQL> desc gv$io_calibration_status
  Name                                      Null?    Type
  ----------------------------------------- -------- ----------------------------
  INST_ID                                            NUMBER
  STATUS                                             VARCHAR2(13)
  CALIBRATION_TIME                                   TIMESTAMP(3)
 
Column explanation:
-------------------
STATUS:
  IN PROGRESS   : Calibration in Progress (Results from previous calibration
                  run displayed, if available)
  READY         : Results ready and available from earlier run
  NOT AVAILABLE : Calibration results not available.
 
CALIBRATION_TIME: End time of the last calibration run
```

DBA table that stores I/O Calibration results

```
SQL> desc DBA_RSRC_IO_CALIBRATE
  Name                                      Null?    Type
  ----------------------------------------- -------- ----------------------------
  START_TIME                                         TIMESTAMP(6)
  END_TIME                                           TIMESTAMP(6)
  MAX_IOPS                                           NUMBER
  MAX_MBPS                                           NUMBER
  MAX_PMBPS                                          NUMBER
  LATENCY                                            NUMBER
  NUM_PHYSICAL_DISKS                                 NUMBER
 
comment on table DBA_RSRC_IO_CALIBRATE is
'Results of the most recent I/O calibration'
/
comment on column DBA_RSRC_IO_CALIBRATE.START_TIME is
'start time of the most recent I/O calibration'
/
comment on column DBA_RSRC_IO_CALIBRATE.END_TIME is
'end time of the most recent I/O calibration'
/
comment on column DBA_RSRC_IO_CALIBRATE.MAX_IOPS is
'maximum number of data-block read requests that can be sustained per second'
/
comment on column DBA_RSRC_IO_CALIBRATE.MAX_MBPS is
'maximum megabytes per second of maximum-sized read requests that can be
sustained'
/
comment on column DBA_RSRC_IO_CALIBRATE.MAX_PMBPS is
'maximum megabytes per second of large I/O requests that
can be sustained by a single process'
/
comment on column DBA_RSRC_IO_CALIBRATE.LATENCY is
'latency for data-block read requests'
/
comment on column DBA_RSRC_IO_CALIBRATE.NUM_PHYSICAL_DISKS is
'number of physical disks in the storage subsystem (as specified by user)'
/
```

#### 148.4.3 CLEAR\_PENDING\_AREA Procedure

This procedure clears pending changes for the resource manager.

Syntax

```
DBMS_RESOURCE_MANAGER.CLEAR_PENDING_AREA;
```

#### 148.4.4 CREATE\_CATEGORY Procedure

This procedure creates a new consumer group category. The primary purpose of this attribute is to support Exadata I/O Resource Manager category plans.

The view `DBA_RSRC_CATEGORIES` defines the currently defined categories. The `ADMINISTRATIVE`, `INTERACTIVE`, `BATCH`, `MAINTENANCE`, and `OTHER` categories are available.

Syntax

```
DBMS_RESOURCE_MANAGER.CREATE_CATEGORY (
   category    IN    VARCHAR2,
   comment     IN    VARCHAR2 DEFAULT NULL);
```

Parameters

Table 148-4 CREATE\_CATEGORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `category` | Name of consumer group category |