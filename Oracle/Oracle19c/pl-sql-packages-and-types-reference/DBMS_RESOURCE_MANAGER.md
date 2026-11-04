---
title: DBMS_RESOURCE_MANAGER
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_RESOURCE_MANAGER.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_RESOURCE_MANAGER` package maintains plans, consumer groups, and plan directives. It also provides semantics so that you may group together changes to the plan schema.

This chapter contains the following topics:

**See Also:** For more information on using the Database Resource Manager, see [*Oracle Database Administrator’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADMIN-GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF)

### DBMS\_RESOURCE\_MANAGER Deprecated Subprograms

The SET\_INITIAL\_CONSUMER\_GROUP Procedure has been deprecated with Oracle Database 11 *g*.

- SET\_INITIAL\_CONSUMER\_GROUP Procedure

**Note:** Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

### DBMS\_RESOURCE\_MANAGER Security Model

The invoker must have the `ADMINISTER_RESOURCE_MANAGER` system privilege to execute these procedures.

The procedures to grant and revoke this privilege are in the package [DBMS\_RESOURCE\_MANAGER\_PRIVS](DBMS_RESOURCE_MANAGER_PRIVS.md).

### DBMS\_RESOURCE\_MANAGER Constants

The `DBMS_RESOURCE_MANAGER` package defines several constants for specifying parameter values.

These are shown in the following table.

Table 1 DBMS\_RESOURCE\_MANAGER Constants

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
| `SERVICE_MODULE` | `VARCHAR2(30)` | `SERVICE_MODULE` | Combination of service and module names in this form: *service\_name*.*module\_name* |
| `SERVICE_MODULE_ACTION` | `VARCHAR2(30)` | `SERVICE_MODULE_ACTION` | Combination of service name, module name, and action name, in this form: *service\_name*.*module\_name*.*action\_name* |
| `SERVICE_NAME` | `VARCHAR2(30)` | `SERVICE_NAME` | Service name used by the client to establish a connection |

### Summary of DBMS\_RESOURCE\_MANAGER Subprograms

This table lists the `DBMS_RESOURCE_MANAGER` subprograms and briefly describes them.

Table 2 DBMS\_RESOURCE\_MANAGER Package Subprograms

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

### BEGIN\_SQL\_BLOCK Procedure

This procedure, to be used with parallel statement queuing, indicates the start of a block of SQL statements that should be treated as a group by resource manager.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.BEGIN_SQL_BLOCK;
```

**Usage Notes**

For more information, see [“Parallel Statement Queuing”](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=VLDBG1396) and [“Managing Parallel Statement Queuing with Resource Manager”](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=VLDBG14020) in *Oracle Database VLDB and Partitioning Guide*.

### CALIBRATE\_IO Procedure

This procedure calibrates the I/O capabilities of storage. Calibration status is available from the `V$IO_CALIBRATION_STATUS` view and results for a successful calibration run are located in `DBA_RSRC_IO_CALIBRATE` table.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CALIBRATE_IO (
   num_physical_disks      IN  PLS_INTEGER DEFAULT 1,
   max_latency             IN  PLS_INTEGER DEFAULT 20,
   max_iops                OUT PLS_INTEGER,
   max_mbps                OUT PLS_INTEGER,
   actual_latency          OUT PLS_INTEGER);
```

**Parameters**

Table 3 CALIBRATE\_IO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `num_physical_disks` | Approximate number of physical disks in the database storage. This parameter is used to determine the initial I/O load for the calibration run. |
| `max_latency` | Maximum tolerable latency in milliseconds for database-block-sized IO requests |
| `max_iops` | Maximum number of I/O requests per second that can be sustained. The I/O requests are randomly-distributed, database-block-sized reads. |
| `max_mbps` | Maximum throughput of I/O that can be sustained, expressed in megabytes per second. The I/O requests are randomly-distributed, 1 megabyte reads. |
| `actual_latency` | Average latency of database-block-sized I/O requests at `max_iops` rate, expressed in milliseconds |

**Usage Notes**

- Only users with the SYSDBA privilege can run this procedure. Qualified users must also turn on `timed_statistics`, and ensure `asynch_io` is enabled for datafiles. This can be achieved by setting `filesystemio_options` to either `ASYNCH` or `SETALL`. One can also query the `asynch_io` status by means of the following SQL statement:
	```md
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

**See Also:** [*Oracle Database Performance Tuning Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=TGDBA385) for more information about calibration

**Examples**

Example of using I/O Calibration procedure

```md
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

```md
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

```md
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

### CLEAR\_PENDING\_AREA Procedure

This procedure clears pending changes for the resource manager.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CLEAR_PENDING_AREA;
```

### CREATE\_CATEGORY Procedure

This procedure creates a new consumer group category. The primary purpose of this attribute is to support Exadata I/O Resource Manager category plans.

The view `DBA_RSRC_CATEGORIES` defines the currently defined categories. The `ADMINISTRATIVE`, `INTERACTIVE`, `BATCH`, `MAINTENANCE`, and `OTHER` categories are available.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_CATEGORY (
   category    IN    VARCHAR2,
   comment     IN    VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 4 CREATE\_CATEGORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `category` | Name of consumer group category |
| `comment` | User comment |

### CREATE\_CDB\_PLAN Procedure

Creates entries which define consolidation resource plans.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN (
   plan                    IN    VARCHAR2(32),
   comment                 IN    VARCHAR2(2000) DEFAULT NULL);
```

**Parameters**

Table 5 CREATE\_CDB\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `comment` | User comment |

**Usage Notes**

This procedure can be run only from the CDB root (`CDB$ROOT`).

### CREATE\_CDB\_PLAN\_DIRECTIVE Procedure

This procedure creates the plan directives of the consolidation resource plan. Plan directives specify the resource allocation policy for pluggable databases (PDBs).

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE (
   plan                    IN    VARCHAR2,
   pluggable_database      IN    VARCHAR2,
   comment                 IN    VARCHAR2 (2000) DEFAULT '',
   shares                  IN    NUMBER          DEFAULT NULL,
   utilization_limit       IN    NUMBER          DEFAULT NULL,
   parallel_server_limit   IN    NUMBER          DEFAULT NULL,
   memory_limit            IN    NUMBER          DEFAULT 100,
   memory_min              IN    NUMBER          DEFAULT 0);
```

**Parameters**

Table 6 CREATE\_CDB\_PLAN\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `pluggable_database` | Name of the PDB |
| `comment` | User comment |
| `shares` | Specifies the share of resource allocation for the PDB. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The `shares` parameter is also used for Parallel Statement Queuing. If no share is specified, the default is obtained from the default directive, specified through UPDATE\_CDB\_DEFAULT\_DIRECTIVE Procedure. |
| `utilization_limit` | Specifies the maximum percentage of the CDB's CPU and Exadata I/O resources that the PDB can utilize.  CPU Resource Manager and Exadata I/O Resource Manager can also be limited by setting the `CPU_COUNT` parameter for the PDB. |
| `parallel_server_limit` | Parallel servers that the PDB can use after which parallel statements are queued. Alternatively, you can set the `parallel_servers_target` at the PDB level.  A PDB can set a lower limit for parallel execution servers than the limit specified in the CDB resource plan. When the `PARALLEL_SERVERS_TARGET` initialization parameter is set in a PDB, and parallel execution server limit is specified for a PDB in the CDB resource plan, then the lower limit is used.  For example, assume that the `parallel_servers_target` initialization parameter is set to `100` in the CDB root and `parallel_server_limit` is set to 70 for `hrpdb` in the CDB resource plan. Also, assume that `hrpdb` has its `parallel_servers_target` initialization parameter set to 50. In this case, the limit for parallel execution servers for hrpdb is 50, because 50 is lower than the CDB resource plan limit of 70 for `hrpdb`.  Note:  Oracle recommends, that you use `parallel_servers_target` parameter instead of `parallel_servers_limit` in a CDB resource plan. |
| `memory_limit` | This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. |
| `memory_min` | This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. |

**Usage Notes**

- The default value for `shares`, `utilization_limit`, and `parallel_server_limit` is `NULL`. When a user specifies `NULL`, or does not specify a value, this indicates that the default value should be used.
- This procedure can be run only from the CDB root (`CDB$ROOT`).

### CREATE\_CDB\_PROFILE\_DIRECTIVE Procedure

This procedure creates the performance profile directives of the consolidation resource plan. The directives specify the resource allocation policy for pluggable databases (PDBs) that use the performance profile.

For a PDB to use the new performance profile, the PDB must have the `DB_PERFORMANCE_PROFILE` initialization parameter set to the profile name.

This procedure provides an easy way to specify the directive for a large number of PDBs with the same resource requirements. Each PDB with a `DB_PERFORMANCE_PROFILE` initialization parameter set to the performance profile name inherits the settings specified by this directive, including the shares, utilization limit, and so on.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE (
   plan                    IN    VARCHAR2,
   profile                 IN    VARCHAR2,
   comment                 IN    VARCHAR2 (2000) DEFAULT '',
   shares                  IN    NUMBER          DEFAULT NULL,
   utilization_limit       IN    NUMBER          DEFAULT NULL,
   parallel_server_limit   IN    NUMBER          DEFAULT NULL,
   memory_limit            IN    NUMBER          DEFAULT 100,
   memory_min              IN    NUMBER          DEFAULT 0);
```

**Parameters**

Table 7 CREATE\_CDB\_PROFILE\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `profile` | Name of the performance profile |
| `comment` | User comment |
| `shares` | Specifies the share of resource allocation for PDBs that use the performance profile. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The `shares` parameter is also used for Parallel Statement Queuing. If no share is specified, the default is obtained from the default directive, specified through UPDATE\_CDB\_DEFAULT\_DIRECTIVE Procedure. |
| `utilization_limit` | Specifies the maximum percentage of CPU Resource Manager and Exadata I/O Resource Manager that PDBs that use the performance profile can utilize. |
| `parallel_server_limit` | Specifies the maximum percentage of `parallel_servers_target` parallel servers that PDBs that use the performance profile can use. |
| `memory_limit` | This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. |
| `memory_min` | This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. |

### CREATE\_CONSUMER\_GROUP Procedure

This procedure creates entries which define resource consumer groups.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_CONSUMER_GROUP (
   consumer_group  IN VARCHAR2,
   comment         IN VARCHAR2 DEFAULT NULL,
   cpu_mth         IN VARCHAR2 DEFAULT NULL,
   mgmt_mth        IN VARCHAR2 DEFAULT 'ROUND-ROBIN',
   category        IN VARCHAR2 DEFAULT 'OTHER');
```

**Parameters**

Table 8 CREATE\_CONSUMER\_GROUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `consumer_group` | Name of the consumer group |
| `comment` | User comment |
| `cpu_mth` | Name of CPU resource allocation method (deprecated) |
| `mgmt_mth` | Name of CPU resource allocation method |
| `category` | Describes the category of the consumer group. The primary purpose of this attribute is to support Exadata I/O Resource Manager category plans. The view `DBA_RSRC_CATEGORIES` defines the currently defined categories. Categories can be modified, using the CREATE\_CATEGORY Procedure, UPDATE\_CATEGORY Procedure, and DELETE\_CATEGORY Procedure. |

### CREATE\_PENDING\_AREA Procedure

This procedure makes changes to resource manager objects.

All changes to the plan schema must be done within a pending area. The pending area can be thought of as a “scratch” area for plan schema changes. The administrator creates this pending area, makes changes as necessary, possibly validates these changes, and only when the submit is completed do these changes become active.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA;
```

**Usage Notes**

You may, at any time while the pending area is active, view the current plan schema with your changes by selecting from the appropriate user views.

At any time, you may clear the pending area if you want to stop the current changes. You may also call the `VALIDATE` procedure to confirm whether the changes you have made are valid. You do not have to perform your changes in a given order to maintain a consistent group of entries. These checks are also implicitly done when the pending area is submitted.

**Note:** Oracle allows “orphan” consumer groups (in other words, consumer groups that have no plan directives that refer to them). This is in anticipation that an administrator may want to create a consumer group that is not currently being used, but will be used in the future.

For resource plans, the following rules must be adhered to, and they are checked whenever the validate or submit procedures are executed:

- No plan schema may contain any loops.
- All plans and consumer groups referred to by plan directives must exist.
- All plans must have plan directives that refer to either plans or consumer groups.
- All percentages in any given level must not add up to greater than 100 for the emphasis resource allocation method.
- No plan may be deleted that is currently being used as a top plan by an active instance.
- The plan directive parameter, `parallel_degree_limit_p1`, may only appear in plan directives that refer to consumer groups (that is, not at subplans).
- There cannot be more than 28 plan directives coming from any given plan (that is, no plan can have more than 28 children).
- There cannot be more than 28 consumer groups in any active plan schema.
- Plans and consumer groups use the same namespace; therefore, no plan can have the same name as any consumer group.
- There must be a plan directive for `OTHER_GROUPS` somewhere in any active plan schema.This ensures that a session not covered by the currently active plan is allocated resources as specified by the `OTHER_GROUPS` directive.

**Note:** These rules are not applicable for CDB resource plans.

If any of the preceding rules are broken when checked by the `VALIDATE` or `SUBMIT` procedures, then an informative error message is returned. You may then make changes to fix one or more problems and reissue the validate or submit procedures.

### CREATE\_PLAN Procedure

This procedure creates entries which define resource plans.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_PLAN (
   plan                       IN   VARCHAR2,
   comment                    IN   VARCHAR2 DEFAULT NULL,
   cpu_mth                    IN   VARCHAR2 DEFAULT NULL, -- deprecated
   active_sess_pool_mth       IN   VARCHAR2 DEFAULT 'ACTIVE_SESS_POOL_ABSOLUTE',
   parallel_degree_limit_mth  IN   VARCHAR2 DEFAULT
                                      'PARALLEL_DEGREE_LIMIT_ABSOLUTE',
   queueing_mth               IN   VARCHAR2 DEFAULT 'FIFO_TIMEOUT',
   mgmt_mth                   IN   VARCHAR2 DEFAULT 'EMPHASIS',
   sub_plan                   IN   BOOLEAN DEFAULT FALSE,
   max_iops                   IN   NUMBER DEFAULT NULL,
   max_mbps                   IN   NUMBER DEFAULT NULL);
```

**Parameters**

Table 9 CREATE\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the resource plan |
| `comment` | User comment |
| `cpu_mth` | Allocation method for CPU resources (deprecated) |
| `active_sess_pool_mth` | Active session pool resource allocation method. Limits the number of active sessions. All other sessions are inactive and wait in a queue to be activated. `ACTIVE_SESS_POOL_ABSOLUTE` is the default and only method available. |
| `parallel_degree_limit_mth` | Resource allocation method for specifying a limit on the degree of parallelism of any operation. `PARALLEL_DEGREE_LIMIT_ABSOLUTE` is the default and only method available. |
| `queueing_mth` | Queuing resource allocation method. Controls order in which queued inactive sessions will execute. `FIFO_TIMEOUT` is the default and only method available |
| `mgmt_mth` | Resource allocation method for specifying how much resources (for example, CPU or I/O) each consumer group or sub-plan gets  - `EMPHASIS` - for multilevel plans that use percentages to specify how I/O resources are distributed among consumer groups - `RATIO` - for single-level plans that use ratios to specify how I/O resources are distributed |
| `sub_plan` | If `TRUE`, indicates that this plan is only intended for use as a sub-plan. Sub-plans are not required to have an `OTHER_GROUPS` directive. Default is `FALSE`. |
| `max_iops` | Nonoperative |
| `max_mbps` | Nonoperative |

**Usage Notes**

If you want to use any default resource allocation method, then you do not need to specify it when creating or updating a plan.

### CREATE\_PLAN\_DIRECTIVE Procedure

This procedure creates resource plan directives.

**Note:** The parameters `max_utilization_limit` and `parallel_target_percentage` are deprecated with Oracle Database 11 *g* Release 1 (11.1.0.1), and are replaced by `utilization_limit` and `parallel_server_limit`.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE (
   plan                         IN VARCHAR2,
   group_or_subplan             IN VARCHAR2,
   comment                      IN VARCHAR2 DEFAULT NULL,
   cpu_p1                       IN NUMBER   DEFAULT NULL, -- deprecated
   cpu_p2                       IN NUMBER   DEFAULT NULL, -- deprecated
   cpu_p3                       IN NUMBER   DEFAULT NULL, -- deprecated
   cpu_p4                       IN NUMBER   DEFAULT NULL, -- deprecated
   cpu_p5                       IN NUMBER   DEFAULT NULL, -- deprecated
   cpu_p6                       IN NUMBER   DEFAULT NULL, -- deprecated
   cpu_p7                       IN NUMBER   DEFAULT NULL, -- deprecated
   cpu_p8                       IN NUMBER   DEFAULT NULL, -- deprecated
   active_sess_pool_p1          IN NUMBER   DEFAULT NULL,
   queueing_p1                  IN NUMBER   DEFAULT NULL,
   parallel_degree_limit_p1     IN NUMBER   DEFAULT NULL,
   switch_group                 IN VARCHAR2 DEFAULT NULL,
   switch_time                  IN NUMBER   DEFAULT NULL,
   switch_estimate              IN BOOLEAN  DEFAULT FALSE,
   max_est_exec_time            IN NUMBER   DEFAULT NULL,
   undo_pool                    IN NUMBER   DEFAULT NULL,
   max_idle_time                IN NUMBER   DEFAULT NULL,
   max_idle_blocker_time        IN NUMBER   DEFAULT NULL,
   switch_time_in_call          IN NUMBER   DEFAULT NULL, -- deprecated
   mgmt_p1                      IN NUMBER   DEFAULT NULL,
   mgmt_p2                      IN NUMBER   DEFAULT NULL,
   mgmt_p3                      IN NUMBER   DEFAULT NULL,
   mgmt_p4                      IN NUMBER   DEFAULT NULL,
   mgmt_p5                      IN NUMBER   DEFAULT NULL,
   mgmt_p6                      IN NUMBER   DEFAULT NULL,
   mgmt_p7                      IN NUMBER   DEFAULT NULL,
   mgmt_p8                      IN NUMBER   DEFAULT NULL,
   switch_io_megabytes          IN NUMBER   DEFAULT NULL,
   switch_io_reqs               IN NUMBER   DEFAULT NULL,
   switch_for_call              IN BOOLEAN  DEFAULT NULL,
   max_utilization_limit        IN NUMBER   DEFAULT NULL,  -- deprecated
   parallel_target_percentage   IN NUMBER   DEFAULT NULL,  -- deprecated
   parallel_server_limit        IN NUMBER   DEFAULT NULL,
   utilization_limit            IN NUMBER   DEFAULT NULL,
   switch_io_logical            IN NUMBER   DEFAULT NULL,
   switch_elapsed_time          IN NUMBER   DEFAULT NULL,
   shares                       IN NUMBER   DEFAULT NULL,
   parallel_stmt_critical       IN VARCHAR2 DEFAULT NULL,
   session_pga_limit            IN NUMBER   DEFAULT NULL,
   pq_timeout_action            IN NUMBER   DEFAULT NULL,
   parallel_queue_timeout       IN NUMBER   DEFAULT NULL,);
```

**Note:** Oracle recommends that you use `shares` instead of `mgmt_p*`.

**Parameters**

Table 10 CREATE\_PLAN\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the resource plan |
| `group_or_subplan` | Name of the consumer group or subplan |
| `comment` | Comment for the plan directive |
| `cpu_p1` | – deprecated: use `mgmt_p1` or, even better, shares instead |
| `cpu_p2` | – deprecated: use `mgmt_p2` or, even better, shares instead |
| `cpu_p3` | – deprecated: use `mgmt_p3` or, even better, shares instead |
| `cpu_p4` | – deprecated: use `mgmt_p4` or, even better, shares instead |
| `cpu_p5` | – deprecated: use `mgmt_p5` or, even better, shares instead |
| `cpu_p6` | – deprecated: use `mgmt_p6` or, even better, shares instead |
| `cpu_p7` | – deprecated: use `mgmt_p7` or, even better, shares instead |
| `cpu_p8` | – deprecated: use `mgmt_p8` or, even better, shares instead |
| `active_sess_pool_p1` | Specifies maximum number of sessions that can currently have an active call |
| `queueing_p1` | Specified time (in seconds) after which a call in the inactive session queue (waiting for execution) will time out. Default is `NULL`, which means unlimited. |
| `parallel_degree_limit_p1` | Specifies a limit on the degree of parallelism for any operation. Default is `NULL`, which means unlimited. If the value is 0, then all operations will be serial. |
| `switch_group` | Specifies consumer group to switch to, once a switch condition is met. If the group name is `CANCEL_SQL`, then the current call is canceled when the switch condition is met. If the group name is `KILL_SESSION`, then the session is killed when the switch condition is met. If the group name is `LOG_ONLY`, then no action is taken other than recording this event via SQL monitor.Default is `NULL`. |
| `switch_time` | Specifies the time on CPU (not elapsed time) that a session can execute before an action is taken. Default is `NULL`, which means unlimited. As with other switch directives, if `switch_for_call` is `TRUE`, the number of CPUs is accumulated from the start of a call. Otherwise, the number of CPUs is accumulated for the length of the session. |
| `switch_estimate` | If `TRUE`, tells Oracle to use its execution time estimate to automatically switch the consumer group of an operation before beginning its execution. This is used in conjunction with the `switch_time` directive.  Default value is `FALSE`. |
| `max_est_exec_time` | Specifies the maximum execution time (in CPU seconds) allowed for a session. If the optimizer estimates that an operation will take longer than `MAX_EST_EXEC_TIME`, the operation is not started and ORA-07455 is issued. If the optimizer does not provide an estimate, this directive has no effect. Default is `NULL`, which means unlimited. |
| `undo_pool` | Limits the size in kilobytes of the undo records corresponding to uncommitted transactions by this consumer group |
| `max_idle_time` | Indicates the maximum session idle time. Default is `NULL`, which means unlimited. |
| `max_idle_blocker_time` | Maximum amount of time in seconds that a session can be idle while blocking another session’s acquisition of a resource |
| `switch_time_in_call` | Deprecated. If this parameter is specified, `switch_time` is set to `switch_time_in_call` (in seconds) and `switch_for_call` is effectively set to `TRUE`. It is better to use `switch_time` and `switch_for_call`. |
| `mgmt_p1` | Resource allocation value for level 1 (replaces `cpu_p1`):  - `EMPHASIS` - specifies the resource percentage at the first level - `RATIO` - specifies the weight of resource usage |
| `mgmt_p2` | Resource allocation value for level 2 (replaces `cpu_p2`)  - `EMPHASIS` - specifies the resource percentage at the second level - `RATIO` - non-applicable |
| `mgmt_p3` | Resource allocation value for level 3 (replaces `cpu_p3`)  - `EMPHASIS` - specifies the resource percentage at the third level - `RATIO` - non-applicable |
| `mgmt_p4` | Resource allocation value for level 4 (replaces `cpu_p4`)  - `EMPHASIS` - specifies the resource percentage at the fourth level - `RATIO` - non-applicable |
| `mgmt_p5` | Resource allocation value for level 5 (replaces `cpu_p5`)  - `EMPHASIS` - specifies the resource percentage at the fifth level - `RATIO` - non-applicable |
| `mgmt_p6` | Resource allocation value for level 6 (replaces `cpu_p6`)  - `EMPHASIS` - specifies the resource percentage at the sixth level - `RATIO` - non-applicable |
| `mgmt_p7` | Resource allocation value for level 7 (replaces `cpu_p7`)  - `EMPHASIS` - specifies the resource percentage at the seventh level - `RATIO` - non-applicable |
| `mgmt_p8` | Resource allocation value for level 8 (replaces `cpu_p8`)  - `EMPHASIS` - specifies the resource percentage at the eighth level - `RATIO` - non-applicable |
| `switch_io_megabytes` | Specifies the amount of I/O (in MB) that a session can issue before an action is taken. Default is `NULL`, which means unlimited. As with other switch directives, if `switch_for_call` is `TRUE`, the number of CPUs is accumulated from the start of a call. Otherwise, the number of CPUs is accumulated for the length of the session. |
| `switch_io_reqs` | Specifies the number of I/O requests that a session can issue before an action is taken. Default is `NULL`, which means unlimited. As with other switch directives, if `switch_for_call` is `TRUE`, the number of CPUs is accumulated from the start of a call. Otherwise, the number of CPUs is accumulated for the length of the session. |
| `switch_for_call` | Specifies that if an action is taken because of the `switch_time`, `switch_io_megabytes`, `switch_io_reqs`, `switch_io_logical` or `switch_elapsed_time` parameters, the consumer group is restored to its original consumer group at the end of the top call. Default is `NULL`, which means that the original consumer group is not restored at the end of the top call. |
| `max_utilization_limit` | – deprecated: use `utilization_limit` instead |
| `parallel_target_percentage` | – deprecated: use `parallel_sever_limit` instead |
| `parallel_queue_timeout` | Specifies the time (in seconds) that a parallel statement may remain in its Consumer Group's parallel statement queue before it is removed and terminated with an error (ORA- 07454).  Note:  You can use the `pq_timeout_action` parameter to specify the action to be taken when a parallel statement is removed from the queue. |
| `parallel_sever_limit` | Specifies the maximum percentage of `parallel_servers_target` parallel servers that the Consumer Group can use, after which parallel statements are queued. |
| `utilization_limit` | Resource limit. Currently it includes CPU and I/O for Exadata.  For CPU, this limits the CPU utilization for the consumer group.  For Exadata I/O, this limits the disk utilization for the consumer group.  This does not apply to parallel servers. |
| `switch_io_logical` | Number of logical IOs that will trigger the action specified by `switch_group`. As with other switch directives, if `switch_for_call` is `TRUE`, the number of logical IOs is accumulated from the start of a call. Otherwise, the number of logical IOs is accumulated for the length of the session. |
| `switch_elapsed_time` | Elapsed time that will trigger the action specified by `switch_group`. As with other switch directives, if `switch_for_call` is `TRUE`, the elapsed time is accumulated from the start of a call. Otherwise, the elapsed time is accumulated for the length of the session. |
| `shares` | Specifies the share of resource allocation for the consumer group. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each consumer group. The `shares` parameter is also used for Parallel Statement Queuing. If CPU Resource Manager and Exadata I/O Resource Manager are enabled, then the default value is `1`. |
| `parallel_stmt_critical` | If set to `BYPASS_QUEUE`, parallel statements from the Consumer Group are not queued, regardless of the `PARALLEL_DEGREE_POLICY` parameter value.  If set to `QUEUE`, all the parallel statements from the consumer group, irrespective of the `parallel_degree_policy` parameter value, are eligible for queuing.  Default is `FALSE`, which means that parallel statements are eligible for queuing, based on the `parallel_degree_policy` parameter value. |
| `session_pga_limit` | Maximum amount of untunable PGA (in MB) that a session in this consumer group can allocate before being terminated. `NULL` (default) indicates no limit.  SQL operations that allocate tunable PGA (operations that can opt to use temp space) are not controlled by this limit. |
| `pq_timeout_action` | Specifies the action to be taken when a parallel statement is removed from the queue due to `parallel_queue_timeout`.  The values are:  - `CANCEL` - The parallel statement is terminated with error `ORA-7454` - `RUN` - The SQL statement runs immediately, and might get downgraded if parallel servers are unavailable  The default action of this parameter is `CANCEL`. |

**Usage Notes**

- All parameters default to `NULL`.
- For `max_idle_time` and `max_idle_blocker_time`, `PMON` will check these limits once a minute. If it finds a session that has exceeded one of the limits, it will forcibly kill the session and clean up all its state.
- The parameter `switch_for_call` is mostly useful for three-tier applications where the mid-tier server is implementing session pooling. By using `switch_for_call`, the resource usage of one client will not affect a future client that happens to be executed on the same session.
- An error is thrown if `PQ_TIMEOUT_ACTION` is specified, but `PARALLEL_QUEUE_TIMEOUT` is not specified.
- Specifies the action to be taken when a parallel statement is removed from the queue.

### CREATE\_SIMPLE\_PLAN Procedure

This procedure creates a single-level resource plan containing up to eight consumer groups in one step. You do not need to create a pending area manually before creating a resource plan, or use the `CREATE_CONSUMER_GROUP` and `CREATE_RESOURCE_PLAN_DIRECTIVES` procedures separately.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN (
   simple_plan      IN  VARCHAR2  DEFAULT NULL,
   consumer_group1  IN  VARCHAR2  DEFAULT NULL,
   group1_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group2  IN  VARCHAR2  DEFAULT NULL,
   group2_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group3  IN  VARCHAR2  DEFAULT NULL,
   group3_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group4  IN  VARCHAR2  DEFAULT NULL,
   group4_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group5  IN  VARCHAR2  DEFAULT NULL,
   group5_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group6  IN  VARCHAR2  DEFAULT NULL,
   group6_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group7  IN  VARCHAR2  DEFAULT NULL,
   group7_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group8  IN  VARCHAR2  DEFAULT NULL,
   group8_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   group1_percent   IN  NUMBER    DEFAULT NULL,
   group2_percent   IN  NUMBER    DEFAULT NULL,
   group3_percent   IN  NUMBER    DEFAULT NULL,
   group4_percent   IN  NUMBER    DEFAULT NULL,
   group5_percent   IN  NUMBER    DEFAULT NULL,
   group6_percent   IN  NUMBER    DEFAULT NULL,
   group7_percent   IN  NUMBER    DEFAULT NULL,
   group8_percent   IN  NUMBER    DEFAULT NULL);
```

**Parameters**

Table 11 CREATE\_SIMPLE\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `simple_plan` | Name of the resource plan |
| `consumer_group1` | Name of the consumer group |
| `group1_cpu` | Percentage for group (deprecated) |
| `consumer_group2` | Name of the consumer group |
| `group2_cpu` | Percentage for group (deprecated) |
| `consumer_group3` | Name of the consumer group |
| `group3_cpu` | Percentage for group (deprecated) |
| `consumer_group4` | Name of the consumer group |
| `group4_cpu` | Percentage for group (deprecated) |
| `consumer_group5` | Name of the consumer group |
| `group5_cpu` | Percentage for group (deprecated) |
| `consumer_group6` | Name of the consumer group |
| `group6_cpu` | Percentage for group (deprecated) |
| `consumer_group7` | Name of the consumer group |
| `group7_cpu` | Percentage for group (deprecated) |
| `consumer_group8` | `OTHER_GROUPS` - all sessions that aren’t mapped to a consumer group. |
| `group8_cpu` | Percentage for group (deprecated) |
| `group1_percent` | Percentage of resources allocated for this consumer group |
| `group2_percent` | Percentage of resources allocated for this consumer group |
| `group3_percent` | Percentage of resources allocated for this consumer group |
| `group4_percent` | Percentage of resources allocated for this consumer group |
| `group5_percent` | Percentage of resources allocated for this consumer group |
| `group6_percent` | Percentage of resources allocated for this consumer group |
| `group7_percent` | Percentage of resources allocated for this consumer group |
| `group8_percent` | Percentage of resources allocated to other groups |

### DELETE\_CATEGORY Procedure

This procedure deletes an existing resource consumer group category.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_CATEGORY (
   category        IN    VARCHAR2);
```

**Parameters**

Table 12 DELETE\_CATEGORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `category` | Name of consumer group category |

### DELETE\_CDB\_PLAN Procedure

This procedure deletes the consolidation resource plan.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN (
   plan    IN    VARCHAR2(32)   DEFAULT NULL);
```

**Parameters**

Table 13 DELETE\_CDB\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |

**Usage Notes**

This procedure can be run only from the CDB root (`CDB$ROOT`).

### DELETE\_CDB\_PLAN\_DIRECTIVE Procedure

This procedure deletes the plan directives of the consolidation resource plan. Once the plan directive is deleted, the pluggable database will get the default resource allocation.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE (
   plan                    IN    VARCHAR2(32)   DEFAULT NULL,
   pluggable_database      IN    VARCHAR2(32)   DEFAULT NULL);
```

**Parameters**

Table 14 DELETE\_CDB\_PLAN\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `pluggable_database` | Name of the pluggable database in which the plan directive is to be deleted |

**Usage Notes**

This procedure can be run only from the CDB root (`CDB$ROOT`).

### DELETE\_CDB\_PROFILE\_DIRECTIVE Procedure

This procedure deletes the performance profile directive of the consolidation resource plan. Once the directive is deleted, the pluggable databases (PDBs) that use the performance profile use the default resource allocation.

For a PDB to use a performance profile, the PDB must have the `DB_PERFORMANCE_PROFILE` initialization parameter set to the performance profile name.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_CDB_PROFILE_DIRECTIVE (
   plan          IN    VARCHAR2(32)   DEFAULT NULL,
   profile       IN    VARCHAR2(32)   DEFAULT NULL);
```

**Parameters**

Table 15 DELETE\_CDB\_PROFILE\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `profile` | Name of the performance profile directive to be deleted |

**Usage Notes**

This procedure can be run only from the CDB root (`CDB$ROOT`).

### DELETE\_CONSUMER\_GROUP Procedure

This procedure deletes entries which define resource consumer groups.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_CONSUMER_GROUP (
   consumer_group IN VARCHAR2);
```

**Parameters**

Table 16 DELETE\_CONSUMER\_GROUP Procedure Parameters

| Parameters | Description |
| --- | --- |
| `consumer_group` | Name of the consumer group to be deleted |

### DELETE\_PLAN Procedure

This procedure deletes the specified plan as well as all the plan directives to which it refers.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_PLAN (
   plan IN VARCHAR2);
```

**Parameters**

Table 17 DELETE\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the resource plan to delete |

### DELETE\_PLAN\_CASCADE Procedure

This procedure deletes the specified plan and all of its descendants (plan directives, subplans, consumer groups). Mandatory objects and directives are not deleted.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_PLAN_CASCADE (
   plan IN VARCHAR2);
```

**Parameters**

Table 18 DELETE\_PLAN\_CASCADE Procedure Parameters

| Parameters | Description |
| --- | --- |
| `plan` | Name of the plan |

**Usage Notes**

If `DELETE_PLAN_CASCADE` encounters any error, then it rolls back the operation, and nothing is deleted.

### DELETE\_PLAN\_DIRECTIVE Procedure

This procedure deletes resource plan directives.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DELETE_PLAN_DIRECTIVE (
   plan              IN VARCHAR2,
   group_or_subplan  IN VARCHAR2);
```

**Parameters**

Table 19 DELETE\_PLAN\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the resource plan |
| `group_or_subplan` | Name of the group or subplan |

### DEQUEUE\_PARALLEL\_STATEMENT Procedure

This procedure dequeues a parallel statement from the parallel statement queue.

If the `PARALLEL_DEGREE_POLICY` initialization parameter is set to `AUTO` or `ADAPTIVE`, then parallel statement queuing is enabled. If a parallel statement is in the parallel statement queue, then you can use this procedure to dequeue the parallel statement so that it runs immediately.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.DEQUEUE_PARALLEL_STATEMENT (
   session_id      IN  PLS_INTEGER,
   session_serial  IN  PLS_INTEGER,
   inst_id         IN  PLS_INTEGER  DEFAULT NULL,
   sql_id          IN  VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 20 DEQUEUE\_PARALLEL\_STATEMENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `session_id` | The session id of the session running the parallel statement to be dequeued. |
| `session_serial` | The serial number of the session. |
| `inst_id` | Instance ID where the session is running.  If `NULL`, then the current instance is used. |
| `sql_id` | The SQL ID of the session’s statement to dequeue. If the session is running SQL with a different SQL ID, then the statement is not dequeued. |

### END\_SQL\_BLOCK Procedure

This procedure, to be used with parallel statement queuing, indicates the end of a block of SQL statements that should be treated as a group by resource manager.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.END_SQL_BLOCK;
```

**Usage Notes**

For more information, see [“Parallel Statement Queuing”](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=VLDBG1396) and [“Managing Parallel Statement Queuing with Resource Manager”](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=VLDBG14020) in *Oracle Database VLDB and Partitioning Guide*.

### SET\_CONSUMER\_GROUP\_MAPPING Procedure

This procedure adds, deletes, or modifies entries that map sessions to consumer groups, based on the session’s login and runtime attributes.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING(
   attribute        IN VARCHAR2,
   value            IN VARCHAR2,
   consumer_group   IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 21 SET\_CONSUMER\_GROUP\_MAPPING Procedure Parameters

| Parameters | Description |
| --- | --- |
| `attribute` | Mapping attribute to add or modify. It can be one of the Constants listed. |
| `value` | Attribute value to match. This includes both absolute mapping and regular expressions. |
| `consumer_group` | Name of the mapped consumer group, or `NULL` to delete a mapping |

**Usage Notes**

- If no mapping exists for the given attribute and value, a mapping to the given consumer group will be created. If a mapping already exists for the given attribute and value, the mapped consumer group will be updated to the one given. If the `consumer_group` argument is `NULL`, then any mapping from the given attribute and value will be deleted.
- The subprogram supports simple regex expressions for the `value` parameter. It implements the same semantics as the SQL `'LIKE'` operator. Specifically, it uses `'%'` as amulticharacter wildcard and `'_'` as a single character wildcard. The ` ''` character can be used to escape the wildcards. Note that wildcards can only be used if the attribute is one of the following:
	- `CLIENT_OS_USER`
		- `CLIENT_PROGRAM`
		- `CLIENT_MACHINE`
		- `MODULE_NAME`
		- `MODULE_NAME_ACTION`
		- `SERVICE_MODULE`
		- `SERVICE_MODULE_ACTION`
- Consumer group mapping comparisons for `DBMS_RESOURCE_MANAGER.CLIENT_PROGRAM` are performed by stripping the `@` sign and following characters from `V$SESSION.PROGRAM` before comparing it to the `CLIENT_PROGRAM` value supplied.

### SET\_CONSUMER\_GROUP\_MAPPING\_PRI Procedure

Multiple attributes of a session can be used to map the session to a consumer group. This procedure prioritizes the attribute mappings.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI(
   explicit               IN NUMBER,
   oracle_user            IN NUMBER,
   service_name           IN NUMBER,
   client_os_user         IN NUMBER,
   client_program         IN NUMBER,
   client_machine         IN NUMBER,
   module_name            IN NUMBER,
   module_name_action     IN NUMBER,
   service_module         IN NUMBER,
   service_module_action  IN NUMBER,
   client_id              IN NUMBER DEFAULT 11);
```

**Parameters**

Table 22 SET\_CONSUMER\_GROUP\_MAPPING\_PRI Procedure Parameters

| Parameters | Description |
| --- | --- |
| `explicit` | Priority of the explicit mapping |
| `oracle_user` | Priority of the Oracle user name mapping |
| `service_name` | Priority of the client service name mapping |
| `client_os_user` | Priority of the client operating system user name mapping |
| `client_program` | Priority of the client program mapping |
| `client_machine` | Priority of the client machine mapping |
| `module_name` | Priority of the application module name mapping |
| `module_name_action` | Priority of the application module name and action mapping |
| `service_module` | Priority of the service name and application module name mapping |
| `module_name_action` | Priority of the service name, application module name, and application action mapping |
| `client_id` | Client identifier |

**Usage Notes**

- This procedure requires that you include the pseudo-attribute `explicit` as an argument. It must be set to
	1. It indicates that explicit consumer group switches have the highest priority. You explicitly switch consumer groups with these package procedures:
	- `DBMS_SESSION`.`SWITCH_CURRENT_CONSUMER_GROUP`
		- `DBMS_RESOURCE_MANAGER`.`SWITCH_CONSUMER_GROUP_FOR_SESS`
		- `DBMS_RESOURCE_MANAGER`.`SWITCH_CONSUMER_GROUP_FOR_USER`
- Each priority value must be a unique integer from 1 to 11. Together, they establish an ordering where 1 is the highest priority and 11 is the lowest.

### SET\_INITIAL\_CONSUMER\_GROUP Procedure

This deprecated procedure sets the initial resource consumer group for a user.

The initial consumer group of a user is the consumer group to which any session created by that user initially belongs.

**Note:** This procedure is deprecated in Release 11gR1. While the procedure remains available in the package, Initial Consumer Group is set by the session-to-consumer group mapping rules.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.SET_INITIAL_CONSUMER_GROUP (
   user             IN   VARCHAR2,
   consumer_group   IN   VARCHAR2);
```

**Parameters**

Table 23 SET\_INITIAL\_CONSUMER\_GROUP Procedure Parameters

| Parameters | Description |
| --- | --- |
| `user` | Name of the user |
| `consumer_group` | User’s initial consumer group |

**Usage Notes**

- The `ADMINISTER_RESOURCE_MANAGER` or the `ALTER` `USER` system privilege are required to be able to execute this procedure. The user, or `PUBLIC`, must be directly granted switch privilege to a consumer group before it can be set to be the user’s initial consumer group. Switch privilege for the initial consumer group cannot come from a role granted to that user.
	**Note:** These semantics are similar to those for `ALTER` `USER` `DEFAULT` `ROLE`.
- If the initial consumer group for a user has never been set, then the user’s initial consumer group is automatically the consumer group: `DEFAULT_CONSUMER_GROUP`.
- `DEFAULT_CONSUMER_GROUP` has switch privileges granted to `PUBLIC`; therefore, all users are automatically granted switch privilege for this consumer group. Upon deletion of a consumer group, all users having the deleted group as their initial consumer group now have `DEFAULT_CONSUMER_GROUP` as their initial consumer group. All currently active sessions belonging to a deleted consumer group are switched to `DEFAULT_CONSUMER_GROUP`.

### SUBMIT\_PENDING\_AREA Procedure

This procedure submits pending changes for the resource manager. It clears the pending area after validating and committing the changes (if valid).

**Note:** A call to `SUBMIT_PENDING_AREA` may fail even if `VALIDATE_PENDING_AREA` succeeds. This may happen if a plan being deleted is loaded by an instance after a call to `VALIDATE_PENDING_AREA`, but before a call to `SUBMIT_PENDING_AREA`.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA;
```

### SWITCH\_CONSUMER\_GROUP\_FOR\_SESS Procedure

This procedure changes the resource consumer group of a specific session. It also changes the consumer group of any parallel execution servers that are related to the top user session. This procedure is RAC instance specific. You need to connect to the PDB in same RAC instance where the session to be switched is running, and then run this procedure.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS (
   session_id      IN NUMBER,
   session_serial  IN NUMBER,
   consumer_group  IN VARCHAR2);
```

**Parameters**

Table 24 SWITCH\_CONSUMER\_GROUP\_FOR\_SESS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `session_id` | SID column from the view `V$SESSION` |
| `session_serial` | `SERIAL#` column from view `V$SESSION`. |
| `consumer_group` | Name of the consumer group to which to switch |

**Note:** Specifying a value of `'KILL_SESSION'` for the `CONSUMER_GROUP` parameter is not permitted. It will return error \`ORA-29366: invalid CONSUMER\_GROUP argument

```md
specified\`.
{: .infoboxnote}
```

### SWITCH\_CONSUMER\_GROUP\_FOR\_USER Procedure

This procedure changes the resource consumer group for all sessions with a given user ID. It also changes the consumer group of any parallel execution servers that are related to the top user session.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER (
   user            IN VARCHAR2,
   consumer_group  IN VARCHAR2);
```

**Parameters**

Table 25 SWITCH\_CONSUMER\_GROUP\_FOR\_USER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `user` | Name of the user |
| `consumer_group` | Name of the consumer group to which to switch |

**Usage Notes**

- The SWITCH\_CONSUMER\_GROUP\_FOR\_SESS Procedure and the `SWITCH_CONSUMER_GROUP_FOR_USER` procedures let you raise or lower the allocation of CPU resources of certain sessions or users. This provides a functionality similar to the `nice` command on UNIX.
- These procedures cause the session to be moved into the newly specified consumer group immediately.

### SWITCH\_PLAN Procedure

This procedure sets the current resource manager plan.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.SWITCH_PLAN(
   plan_name                     IN   VARCHAR2,
   sid                           IN   VARCHAR2 DEFAULT '*',
   allow_scheduler_plan_switches IN   BOOLEAN DEFAULT TRUE);
```

**Parameters**

Table 26 SWITCH\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan_name` | Name of the plan to which to switch. Passing in an empty string (‘’) for the `plan_name`, disables the resource manager |
| `sid` | The `sid` parameter is relevant only in an Oracle Real Application Clusters environment. This parameter lets you change the plan for a particular instance. Specify the `sid` of the instance where you want to change the plan. Or specify ‘\*’ if you want Oracle to change the plan for all instances. |
| `allow_scheduler_plan_switches` | `FALSE` - disables automated plan switches by the job scheduler at window boundaries. To reenable automated plan switches, switch\_plan must be called again by the administrator with `allow_scheduler_plan_switches` set to `TRUE`. By default automated plan switches by the job scheduler are enabled. |

### UPDATE\_CATEGORY Procedure

This procedure updates an existing resource consumer group category.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_CATEGORY (
   category        IN    VARCHAR2,
   new_comment     IN    VARCHAR2  DEFAULT NULL);
```

**Parameters**

Table 27 UPDATE\_CATEGORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `category` | Name of consumer group category |
| `new_comment` | User comment |

**Usage Notes**

To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_CDB\_AUTOTASK\_DIRECTIVE Procedure

This procedure updates the plan directives with regard to automated maintenance tasks in the CDB root (`CDB$ROOT`).

By default, all maintenance tasks occur directly in the PDBs themselves.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_CDB_AUTOTASK_DIRECTIVE (
   plan                        IN    VARCHAR2,
   new_comment                 IN    VARCHAR2       DEFAULT NULL,
   new_shares                  IN    NUMBER         DEFAULT NULL,
   new_utilization_limit       IN    NUMBER         DEFAULT NULL,
   new_parallel_server_limit   IN    NUMBER         DEFAULT NULL,
   new_memory_limit            IN    NUMBER         DEFAULT NULL,
   new_memory_min              IN    NUMBER         DEFAULT NULL);
```

**Parameters**

Table 28 UPDATE\_CDB\_AUTOTASK\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `new_comment` | New user comment |
| `new_shares` | Specifies the new share of resource allocation for CDB root’s automated maintenance tasks |
| `new_utilization_limit` | Specifies the new maximum percentage of CPU that automated maintenance tasks in the CDB root can utilize |
| `new_parallel_server_limit` | Specifies the new maximum percentage of `parallel_servers_target` parallel servers that automated maintenance tasks in the CDB root are allowed to use |
| `new_memory_limit` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |
| `new_memory_min` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |

**Usage Notes**

- By default for automated maintenance tasks, the values are
	- `shares`: `-1`
		- `utilization_limit`: `90`
		- `parallel_server_limit`: `100`
- The `shares` = `-1` means that the automated maintenance tasks get an allocation of 20% of the system. If the user specifies the `shares`, it behaves the same properties as the other CDB plan directive functions. If the user does not change the shares or later changes it back to `-1`, autotask will get 20% of the system.
- This procedure can be run only from the CDB root.
- To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_CDB\_DEFAULT\_DIRECTIVE Procedure

This procedure updates the plan directives of the consolidation resource plan.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE (
   plan                        IN    VARCHAR2    DEFAULT NULL,
   new_comment                 IN    VARCHAR2    DEFAULT NULL,
   new_shares                  IN    NUMBER      DEFAULT NULL,
   new_utilization_limit       IN    NUMBER      DEFAULT NULL,
   new_parallel_server_limit   IN    NUMBER      DEFAULT NULL,
   new_memory_limit            IN    NUMBER      DEFAULT NULL,
   new_memory_min              IN    NUMBER      DEFAULT NULL);
```

**Parameters**

Table 29 UPDATE\_CDB\_DEFAULT\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `new_commnent` | New user comment |
| `new_shares` | Specifies the share of resource allocation for the pluggable database. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The `new_shares` parameter is also used for Parallel Statement Queuing. |
| `new_utilization_limit` | Specifies the maximum percentage of CPU that the pluggable database can utilize. |
| `new_parallel_server_limit` | Specifies the maximum percentage of `parallel_servers_target` parallel servers that the pluggable database can use. |
| `new_memory_limit` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |
| `new_memory_min` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |

**Usage Notes**

- By default, the default values are
	- `new_shares`: 1
		- `utilization_limit`: 100
		- `parallel_server_limit`: 100
- Note that the default values are `NULL`. This has the same meaning as in UPDATE\_CDB\_PLAN\_DIRECTIVE Procedure. If the user does not specify a value, the value will not be modified.
- This procedure can be run only from the CDB root (`CDB$ROOT`).
- To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_CDB\_PLAN Procedure

This procedure updates the consolidation resource plan.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN (
   plan                        IN    VARCHAR2(32),
   new_comment                 IN    VARCHAR2(2000)   DEFAULT NULL);
```

**Parameters**

Table 30 UPDATE\_CDB\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `new_comment` | User comment |

**Usage Notes**

- This procedure can be run only from the CDB root (`CDB$ROOT`).
- To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_CDB\_PLAN\_DIRECTIVE Procedure

Updates the plan directives for a consolidation resource plan. Plan directives specify the resource allocation policy for pluggable databases (PDBs).

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN_DIRECTIVE (
   plan                        IN    VARCHAR2 (30),
   pluggable_database          IN    VARCHAR2 (30)
   new_comment                 IN    VARCHAR2 (200)  DEFAULT NULL,
   new_shares                  IN    NUMBER          DEFAULT NULL,
   new_utilization_limit       IN    NUMBER          DEFAULT NULL,
   new_parallel_server_limit   IN    NUMBER          DEFAULT NULL,
   new_memory_limit            IN    NUMBER          DEFAULT NULL,
   new_memory_min              IN    NUMBER          DEFAULT NULL);
```

**Parameters**

Table 31 UPDATE\_CDB\_PLAN\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `pluggable_database` | Name of the pluggable database |
| `new_comment` | New user comment |
| `new_shares` | The share of resource allocation for the pluggable database  CPU Resource Manager is enabled by specifying shares for each PDB. The `shares` parameter is also used for Parallel Statement Queuing. If no share is specified, the default is obtained from the default directive, specified through the UPDATE\_CDB\_DEFAULT\_DIRECTIVE Procedure. |
| `new_utilization_limit` | The new maximum percentage of CPU that the pluggable database can utilize |
| `new_parallel_server_limit` | The new maximum percentage of `parallel_servers_target` parallel servers that the pluggable database can use |
| `new_memory_limit` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |
| `new_memory_ min` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |

**Usage Notes**

- The default value for the `new_*` parameters is `NULL` which indicates that the existing value is left unchanged. If the user does not specify one of the arguments when calling this function, the value is not modified.
- This procedure can be run only from the CDB root (`CDB$ROOT`).
- To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_CDB\_PROFILE\_DIRECTIVE Procedure

This procedure updates the performance profile directives of the consolidation resource plan. The directives specify the resource allocation policy for pluggable databases (PDBs) that use the performance profile.

For a PDB to use a performance profile, the PDB must have the `DB_PERFORMANCE_PROFILE` initialization parameter set to the performance profile name.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_CDB_PROFILE_DIRECTIVE (
   plan                        IN    VARCHAR2,
   profile                     IN    VARCHAR2,
   new_comment                 IN    VARCHAR2 (2000) DEFAULT '',
   new_shares                  IN    NUMBER          DEFAULT NULL,
   new_utilization_limit       IN    NUMBER          DEFAULT NULL,
   new_parallel_server_limit   IN    NUMBER          DEFAULT NULL,
   new_memory_limit            IN    NUMBER          DEFAULT 100,
   new_memory_min              IN    NUMBER          DEFAULT 0);
```

**Parameters**

Table 32 UPDATE\_CDB\_PROFILE\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the consolidation plan |
| `profile` | Name of the performance profile |
| `new_comment` | New user comment |
| `new_shares` | The share of resource allocation for the PDBs that use the performance profile |
| `new_utilization_limit` | The new maximum percentage of CPU that PDBs that use the performance profile can use |
| `new_parallel_server_limit` | The new maximum percentage of `parallel_servers_target` parallel servers that PDBs that use the performance profile can use |
| `new_memory_limit` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |
| `new_memory_ min` | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |

**Usage Notes**

- This procedure can be run only from the CDB root (`CDB$ROOT`).
- To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_CONSUMER\_GROUP Procedure

This procedure updates entries which define resource consumer groups.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_CONSUMER_GROUP (
   consumer_group  IN VARCHAR2,
   new_comment     IN VARCHAR2 DEFAULT NULL,
   new_cpu_mth     IN VARCHAR2 DEFAULT NULL,
   new_mgmt_mth    IN VARCHAR2 DEFAULT NULL,
   new_category    IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 33 UPDATE\_CONSUMER\_GROUP Procedure Parameter

| Parameter | Description |
| --- | --- |
| `consumer_group` | Name of consumer group |
| `new_comment` | New user comment |
| `new_cpu_mth` | Name of new method for CPU resource allocation (deprecated) |
| `new_mgmt_mth` | Name of new method for CPU resource allocation |
| `new_category` | New consumer group category |

**Usage Notes**

- If the parameters to the `UPDATE_CONSUMER_GROUP` procedure are not specified, then they remain unchanged in the data dictionary.
- To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_PLAN Procedure

This procedure updates entries which define resource plans.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_PLAN (
   plan                               IN VARCHAR2,
   new_comment                        IN VARCHAR2 DEFAULT NULL,
   new_cpu_mth                        IN VARCHAR2 DEFAULT NULL, -- deprecated
   new_active_sess_pool_mth           IN VARCHAR2 DEFAULT NULL,
   new_parallel_degree_limit_mth      IN VARCHAR2 DEFAULT NULL,
   new_queueing_mth                   IN VARCHAR2 DEFAULT NULL,
   new_mgmt_mth                       IN VARCHAR2 DEFAULT NULL,
   new_sub_plan                       IN BOOLEAN DEFAULT FALSE,
   new_max_iops                       IN NUMBER DEFAULT NULL,
   new_max_mbps                       IN NUMBER DEFAULT NULL);
```

**Parameters**

Table 34 UPDATE\_PLAN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of resource plan |
| `new_comment` | New user comment |
| `new_cpu_mth` | Name of new allocation method for CPU resources (deprecated) |
| `new_active_sess_pool_mth` | Name of new method for maximum active sessions |
| `new_parallel_degree_limit_mth` | Name of new method for degree of parallelism |
| `new_queueing_mth` | Specifies type of queuing policy to use with active session pool feature |
| `new_mgmt_mth` | Resource allocation method for specifying how much resources (for example, CPU or I/O) each consumer group or sub-plan gets  - `EMPHASIS` - for multilevel plans that use percentages to specify how I/O resources are distributed among consumer groups. - `RATIO` - for single-level plans that use ratios to specify how I/O resources are distributed. |
| `new_sub_plan` | New setting for whether the plan is only intended for use as a sub-plan |
| `new_max_iops` | Nonoperative |
| `new_max_mbps` | Nonoperative |

**Usage Notes**

- If the parameters to UPDATE\_PLAN Procedure are not specified, then they remain unchanged in the data dictionary.
- If you want to use any default resource allocation method, then you do not need to specify it when creating or updating a plan.
- To clear (reset to the directive’s default value), use the value `-1`.

### UPDATE\_PLAN\_DIRECTIVE Procedure

This procedure updates resource plan directives.

**Note:** The parameters `new_max_utilization_limit` and `new_parallel_target_percentage` are deprecated with Oracle Database 11g Release 1 (12.1.0.1), and are replaced by `new_utilization_limit` and `new_parallel_server_limit`.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.UPDATE_PLAN_DIRECTIVE (
   plan                             IN VARCHAR2,
   group_or_subplan                 IN VARCHAR2,
   new_comment                      IN VARCHAR2 DEFAULT NULL,
   new_cpu_p1                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_cpu_p2                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_cpu_p3                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_cpu_p4                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_cpu_p5                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_cpu_p6                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_cpu_p7                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_cpu_p8                       IN NUMBER   DEFAULT NULL, -- deprecated
   new_active_sess_pool_p1          IN NUMBER   DEFAULT NULL,
   new_queueing_p1                  IN NUMBER   DEFAULT NULL,
   new_parallel_degree_limit_p1     IN NUMBER   DEFAULT NULL,
   new_switch_group                 IN VARCHAR2 DEFAULT NULL,
   new_switch_time                  IN NUMBER   DEFAULT NULL,
   new_switch_estimate              IN BOOLEAN  DEFAULT FALSE,
   new_max_est_exec_time            IN NUMBER   DEFAULT NULL,
   new_undo_pool                    IN NUMBER   DEFAULT NULL,
   new_max_idle_time                IN NUMBER   DEFAULT NULL,
   new_max_idle_blocker_time        IN NUMBER   DEFAULT NULL,
   switch_time_in_call              IN NUMBER   DEFAULT NULL, -- deprecated
   new_mgmt_p1                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p2                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p3                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p4                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p5                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p6                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p7                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p8                      IN NUMBER   DEFAULT NULL,
   new_switch_io_megabytes          IN NUMBER   DEFAULT NULL,
   new_switch_io_reqs               IN NUMBER   DEFAULT NULL,
   new_switch_for_call              IN BOOLEAN  DEFAULT NULL,
   new_max_utilization_limit        IN NUMBER   DEFAULT NULL,
   new_parallel_target_percentage   IN NUMBER   DEFAULT NULL,
   new_parallel_queue_timeout       IN NUMBER   DEFAULT NULL,
   new_parallel_server_limit        IN NUMBER   DEFAULT NULL,
   new_utilization_limit            IN NUMBER   DEFAULT NULL,
   new_switch_io_logical            IN NUMBER   DEFAULT NULL,
   new_switch_elapsed_time          IN NUMBER   DEFAULT NULL,
   new_shares                       IN NUMBER   DEFAULT NULL,
   new_parallel_stmt_critical       IN VARCHAR2 DEFAULT NULL,
   new_session_pga_limit            IN NUMBER   DEFAULT NULL,
   new_pq_timeout_action            IN NUMBER   DEFAULT NULL);
```

**Parameters**

Table 35 UPDATE\_PLAN\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `plan` | Name of the resource plan |
| `group_or_subplan` | Name of the consumer group or subplan |
| `new_comment` | Comment for the plan directive |
| `new_cpu_p1` | Deprecated - use `new_mgmt_p1` instead |
| `new_cpu_p2` | Deprecated - use `new_mgmt_p2` instead |
| `new_cpu_p3` | Deprecated - use `new_mgmt_p3` instead |
| `new_cpu_p4` | Deprecated- use `new_mgmt_p4` instead |
| `new_cpu_p5` | Deprecated - use `new_mgmt_p5` instead |
| `new_cpu_p6` | Deprecated- use `new_mgmt_p6` instead |
| `new_cpu_p7` | Deprecated- use `new_mgmt_p7` instead |
| `new_cpu_p8` | Deprecated- use `new_mgmt_p8` instead |
| `new_active_sess_pool_p1` | Specifies maximum number of concurrently active sessions for a consumer group. Default is `NULL`, which means unlimited. |
| `new_queueing_p1` | Specified time (in seconds) after which a job in the inactive session queue (waiting for execution) will time out. Default is `NULL`, which means unlimited. |
| `new_parallel_degree_limit_p1` | Specifies a limit on the degree of parallelism for any operation. Default is `NULL`, which means unlimited. |
| `new_switch_group` | Specifies consumer group to which this session is switched if other switch criteria are met. Default is `NULL`. If the group name is ‘ `CANCEL_SQL` ’, the current call will be canceled when other switch criteria are met. If the group name is ‘ `KILL_SESSION` ’, the session will be killed when other switch criteria are met. |
| `new_switch_time` | Specifies time (in CPU seconds) that a session can execute before an action is taken. Default is `NULL`, which means unlimited. |
| `new_switch_estimate` | If `TRUE`, tells Oracle to use its execution time estimate to automatically switch the consumer group of an operation before beginning its execution. Default is `FALSE`. |
| `new_max_est_exec_time` | Specifies the maximum execution time (in CPU seconds) allowed for a session. If the optimizer estimates that an operation will take longer than `MAX_EST_EXEC_TIME`, the operation is not started and ORA-07455 is issued. If the optimizer does not provide an estimate, this directive has no effect. Default is `NULL`, which means unlimited. |
| `new_undo_pool` | Limits the size in kilobytes of the undo records corresponding to uncommitted transactions by this consumer group |
| `new_max_idle_time` | Indicates the maximum session idle time. Default is `NULL`, which means unlimited. |
| `new_max_idle_blocker_time` | Maximum amount of time in seconds that a session can be idle while blocking another session’s acquisition of a resource |
| `new_switch_time_in_call` | Deprecated. If this parameter is specified, `new_switch_time` will be effectively set to `new_switch_time_in_call` and `new_switch_for_call` will be effectively set to `TRUE`. |
| `new_mgmt_p1` | Resource allocation value for level 1 (replaces `new_cpu_p1`):  - `EMPHASIS` - specifies the resource percentage at the first level - `RATIO` - specifies the weight of resource usage |
| `new_mgmt_p2` | Resource allocation value for level 2 (replaces `new_cpu_p2`)  - `EMPHASIS` - specifies the resource percentage at the second level - `RATIO` - non-applicable |
| `new_mgmt_p3` | Resource allocation value for level 3 (replaces `new_cpu_p3`)  - `EMPHASIS` - specifies the resource percentage at the third level - `RATIO` - non-applicable |
| `new_mgmt_p4` | Resource allocation value for level 4 (replaces `new_cpu_p4`)  - `EMPHASIS` - specifies the resource percentage at the fourth level - `RATIO` - non-applicable |
| `new_mgmt_p5` | Resource allocation value for level 5 (replaces `new_cpu_p5`)  - `EMPHASIS` - specifies the resource percentage at the fifth level - `RATIO` - non-applicable |
| `new_mgmt_p6` | Resource allocation value for level 6 (replaces `new_cpu_p6`)  - `EMPHASIS` - specifies the resource percentage at the sixth level - `RATIO` - non-applicable |
| `new_mgmt_p7` | Resource allocation value for level 7 (replaces `new_cpu_p7`)  - `EMPHASIS` - specifies the resource percentage at the seventh level - `RATIO` - non-applicable |
| `new_mgmt_p8` | Resource allocation value for level 8 (replaces `new_cpu_p8`)  - `EMPHASIS` - specifies the resource percentage at the eighth level - `RATIO` - non-applicable |
| `new_switch_io_megabytes` | Specifies the amount of I/O (in MB) that a session can issue before an action is taken. Default is `NULL`, which means unlimited. |
| `new_switch_io_reqs` | Specifies the number of I/O requests that a session can issue before an action is taken. Default is `NULL`, which means unlimited. |
| `new_switch_for_call` | Specifies that if an action is taken because of the `new_switch_time`, `new_switch_io_megabytes`, or `new_switch_io_reqs` parameters, the consumer group is restored to its original consumer group at the end of the top call. Default is `FALSE`, which means that the original consumer group is not restored at the end of the top call. |
| `new_max_utilization_limit` | Deprecated - use `new_utilization_limit` instead |
| `new_parallel_target_percentage` | Deprecated - use `new_parallel_server_limit` instead |
| `new_parallel_server_limit` | Parallel server limit. Setting this overwrites the limit for parallel server set by `utilization_limit`. |
| `new_utilization_limit` | Resource limit. For CPU, this limits the CPU utilization for the consumer group. For parallel servers, this limits the parallel servers used as a percentage of `parallel_servers_target`. |
| `new_switch_elapsed_time` | Elapsed time that will trigger the action specified by `switch_group`. As with other switch directives, if `new_switch_for_call` is `TRUE`, the elapsed time is accumulated from the start of a call. Otherwise, the elapsed time is accumulated for the length of the session. |
| `new_shares` | Specifies the share of resource allocation for the pluggable database. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The `shares` parameter is also used for Parallel Statement Queuing. If CPU Resource Manager and Exadata I/O Resource Manager are enabled, then the default value is `1`. |
| `new_parallel_stmt_critical` | If set to `BYPASS_QUEUE`, parallel statements from this consumer group are not queued.  If set to `QUEUE`, all the parallel statements, irrespective of the `parallel_degree_policy` parameter value, from the consumer group get queued.  Default is `FALSE`, which means that certain parallel statements are eligible for queuing depending upon the `parallel_degree_policy` parameter value. |
| `new_session_pga_limit` | Maximum amount of PGA in MB that sessions in this consumer group can allocate before being terminated. `NULL` (default) indicates no change. |
| `new_parallel_queue_timeout` | Specifies the time (in seconds) that a parallel statement may remain in its Consumer Group's parallel statement queue before it is removed.  The default action of this parameter is `ERROR`. This action can be altered using the `new_pq_timeout_action` parameter. |
| `new_pq_timeout_action` | Specifies the action to be taken when a parallel statement is removed from the queue due to `new_parallel_queue_timeout`.  The values are:  - `CANCEL` - The SQL statement is terminated with error `ORA-7454` - `RUN` - The SQL statement runs immediately, and might get downgraded if parallel servers are unavailable |

**Usage Notes**

- If the parameters for `UPDATE_PLAN_DIRECTIVE` are left unspecified, then they remain unchanged in the data dictionary.
- For `new_max_idle_time` and `new_max_idle_blocker_time`, `PMON` will check these limits once a minute. If it finds a session that has exceeded one of the limits, it will forcibly kill the session and clean up all its state.
- The parameter `new_switch_time_in_call` is mostly useful for three-tier applications where the mid-tier server is implementing session pooling. By turning on `new_switch_time_in_call`, the resource usage of one client will not affect the consumer group of a future client that happens to be executed on the same session.
- To clear (reset to the directive’s default value), use the value `-1`.

### VALIDATE\_PENDING\_AREA Procedure

This procedure validates pending changes for the resource manager.

**Syntax**

```md
DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA;
```