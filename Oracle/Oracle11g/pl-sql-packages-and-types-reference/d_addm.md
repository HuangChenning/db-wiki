---
title: DBMS_ADDM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_addm.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 16 DBMS\_ADDM

The DBMS\_ADDM package facilitates the use of Advisor functionality regarding the Automatic Database Diagnostic Monitor.

See Also:

- Oracle Real Application Clusters Administration and Deployment Guide for more information about ["Automatic Workload Repository in Oracle Real Application Clusters Environments"](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/monitor.htm#RACAD721)
- Oracle Database Performance Tuning Guide for more information about ["Automatic Performance Diagnostics"](https://docs.oracle.com/cd/E11882_01/server.112/e41573/diag.htm#PFGRF026)

This chapter contains the following topics:

- Using DBMS\_ADDM
	- Security Model
- Summary of DBMS\_ADDM Subprograms

---

## Using DBMS\_ADDM

- Security Model

---

### Security Model

The `DBMS_ADDM` package runs with the caller's permission, not the definer's, and then applies the security constraints required by the `DBMS_ADVISOR` package.

See Also:

The [DBMS\_ADVISOR](d_advis.md) package for more information about " [Security Model](d_advis.md) ".

---

## Summary of DBMS\_ADDM Subprograms

Table 16-1 DBMS\_ADDM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ANALYZE\_DB Procedure | Creates an ADDM task for analyzing in database analysis mode and executes it |
| ANALYZE\_INST Procedure | Creates an ADDM task for analyzing in instance analysis mode and executes it. |
| ANALYZE\_PARTIAL Procedure | Creates an ADDM task for analyzing a subset of instances in partial analysis mode and executes it |
| DELETE Procedure | Deletes an already created ADDM task (of any kind) |
| DELETE\_FINDING\_DIRECTIVE Procedure | Deletes a finding directive |
| DELETE\_PARAMETER\_DIRECTIVE Procedure | Deletes a parameter directive |
| DELETE\_SEGMENT\_DIRECTIVE Procedure | Deletes a segment directive |
| DELETE\_SQL\_DIRECTIVE Procedure | Deletes a SQL directive |
| GET\_ASH\_QUERY Function | Returns a string containing the SQL text of an ASH query identifying the rows in ASH with impact for the finding |
| GET\_REPORT Function | Retrieves the default text report of an executed ADDM task |
| INSERT\_FINDING\_DIRECTIVE Procedure | Creates a directive to limit reporting of a specific finding type. |
| INSERT\_PARAMETER\_DIRECTIVE Procedure | Creates a directive to prevent ADDM from creating actions to alter the value of a specific system parameter |
| INSERT\_SEGMENT\_DIRECTIVE Procedure | Creates a directive to prevent ADDM from creating actions to "run Segment Advisor" for specific segments |
| INSERT\_SQL\_DIRECTIVE Procedure | Creates a directive to limit reporting of actions on specific SQL |

---

### ANALYZE\_DB Procedure

This procedure creates an ADDM task for analyzing in database analysis mode and executes it.

Syntax

```
DBMS_ADDM.ANALYZE_DB (
   task_name           IN OUT VARCHAR2,
   begin_snapshot      IN     NUMBER,
   end_snapshot        IN     NUMBER,
   db_id               IN     NUMBER := NULL);
```

Parameters

Table 16-2 ANALYZE\_DB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task to be created |
| `begin_snapshot` | Number of the snapshot that starts the analysis period |
| `end_snapshot` | Number of the snapshot that ends the analysis period |
| `db_id` | Database ID for the database you to analyze. By default, this is the database currently connected |

Return Values

The name of the created task is returned in the `task_name` parameter. It may be different from the value that is given as input (only in cases that name is already used by another task).

Examples

To create an ADDM task in database analysis mode and execute it, with its name in variable `tname`:

```
var tname VARCHAR2(60);
BEGIN
  :tname := 'my_database_analysis_mode_task';
  DBMS_ADDM.ANALYZE_DB(:tname, 1, 2);
END
```

To see a report:

```
SET LONG 100000
SET PAGESIZE 50000
SELECT DBMS_ADDM.GET_REPORT(:tname) FROM DUAL;
```

Note that the return type of a report is a `CLOB`, formatted to fit line size of 80.

---

### ANALYZE\_INST Procedure

This procedure creates an ADDM task for analyzing in instance analysis mode and executes it.

Syntax

```
DBMS_ADDM.ANALYZE_INST (
   task_name           IN OUT VARCHAR2,
   begin_snapshot      IN     NUMBER,
   end_snapshot        IN     NUMBER,
   instance_number     IN     NUMBER := NULL,
   db_id               IN     NUMBER := NULL);
```

Parameters

Table 16-3 ANALYZE\_INST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task to be created |
| `begin_snapshot` | Number of the snapshot that starts the analysis period |
| `end_snapshot` | Number of the snapshot that ends the analysis period |
| `instance_number` | Number of the instance to analyze. By default it is the instance currently connected |
| `db_id` | Database ID for the database you to analyze. By default, this is the database currently connected |

Return Values

The name of the created task is returned in the `task_name` parameter. It may be different from the value that is given as input (only in cases that name is already used by another task).

Usage Notes

On single instance systems (when not using Oracle RAC) the resulting task is identical to using the ANALYZE\_DB procedure.

Examples

To create an ADDM task in instance analysis mode and execute it, with its name in variable `tname`:

```
var tname VARCHAR2(60);
BEGIN
  :tname := 'my_instance_analysis_mode_task';
  DBMS_ADDM.ANALYZE_INST(:tname, 1, 2);
END
```

To see a report:

```
SET LONG 100000
SET PAGESIZE 50000
SELECT DBMS_ADDM.GET_REPORT(:tname) FROM DUAL;
```

Note that the return type of a report is a `CLOB`, formatted to fit line size of 80.

---

### ANALYZE\_PARTIAL Procedure

This procedure creates an ADDM task for analyzing a subset of instances in partial analysis mode and executes it.

Syntax

```
DBMS_ADDM.ANALYZE_PARTIAL (
   task_name           IN OUT VARCHAR2,
   instance_numbers    IN     VARCHAR2,
   begin_snapshot      IN     NUMBER,
   end_snapshot        IN     NUMBER,
   db_id               IN     NUMBER := NULL);
```

Parameters

Table 16-4 ANALYZE\_PARTIAL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task to be created |
| `instance_number` s | Comma separated list of instance numbers to analyze |
| `begin_snapshot` | Number of the snapshot that starts the analysis period |
| `end_snapshot` | Number of the snapshot that ends the analysis period |
| `db_id` | Database ID for the database you to analyze. By default, this is the database currently connected |

Return Values

The name of the created task is returned in the `task_name` parameter. It may be different from the value that is given as input (only in cases that name is already used by another task).

Examples

To create an ADDM task in partial analysis mode and execute it, with its name in variable `tname`:

```
var tname VARCHAR2(60);
BEGIN
  :tname := 'my_partial_analysis_modetask';
  DBMS_ADDM.ANALYZE_PARTIAL(:tname, '1,2,3', 1, 2);
END
```

To see a report:

```
SET LONG 100000
SET PAGESIZE 50000
SELECT DBMS_ADDM.GET_REPORT(:tname) FROM DUAL;
```

Note that the return type of a report is a `CLOB`, formatted to fit line size of 80.

---

### DELETE Procedure

This procedure deletes an already created ADDM task (of any kind). For database analysis mode and partial analysis mode this deletes the local tasks associated with the main task.

Syntax

```
DBMS_ADDM.DELETE (
   task_name           IN VARCHAR2);
```

Parameters

Table 16-5 DELETE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task to be deleted |

Examples

```
BEGIN
  DBMS_ADDM.DELETE ('my_partial_analysis_mode_task');
END
```

---

### DELETE\_FINDING\_DIRECTIVE Procedure

This procedure deletes a finding directive.

Syntax

```
DBMS_ADDM.DELETE_FINDING_DIRECTIVE (
   task_name           IN VARCHAR2,
   dir_name            IN VARCHAR2);
```

Parameters

Table 16-6 DELETE\_FINDING\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it is a system directive. |
| `dir_name` | Name of the directive. All directives must be given unique names. |

---

### DELETE\_PARAMETER\_DIRECTIVE Procedure

This procedure deletes a parameter directive. This removes a specific system directive for parameters. Subsequent ADDM tasks are not affected by this directive.

Syntax

```
DBMS_ADDM.DELETE_PARAMETER_DIRECTIVE (
   task_name           IN VARCHAR2,
   dir_name            IN VARCHAR2);
```

Parameters

Table 16-7 DELETE\_PARAMETER\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it is a system directive. |
| `dir_name` | Name of the directive. All directives must be given unique names. |

Examples

```
BEGIN
   DBMS_ADDM.DELETE_PARAMETER_DIRECTIVE (NULL,'my Parameter directive'); 
END;
```

---

### DELETE\_SEGMENT\_DIRECTIVE Procedure

This procedure deletes a segment directive.

Syntax

```
DBMS_ADDM.DELETE_SEGMENT_DIRECTIVE (
   task_name           IN VARCHAR2,
   dir_name            IN VARCHAR2);
```

Parameters

Table 16-8 DELETE\_SEGMENT\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it is a system directive. |
| `dir_name` | Name of the directive. All directives must be given unique names. |

---

### DELETE\_SQL\_DIRECTIVE Procedure

This procedure deletes a SQL directive.

Syntax

```
DBMS_ADDM.DELETE_SQL_DIRECTIVE (
   task_name           IN VARCHAR2,
   dir_name            IN VARCHAR2);
```

Parameters

Table 16-9 DELETE\_SQL\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it is a system directive. |
| `dir_name` | Name of the directive. All directives must be given unique names. |

---

### GET\_ASH\_QUERY Function

The function returns a string containing the SQL text of an ASH query identifying the rows in ASH with impact for the finding. For most types of findings this identifies the exact rows in ASH corresponding to the finding. For some types of findings the query is an approximation and should not be used for exact identification of the finding's impact or the finding's specific activity.

Syntax

```
DBMS_ADDM.GET_ASH_QUERY (
   task_name           IN   VARCHAR2,
   finding_id          IN   NUMBER)
  RETURN VARCHAR2;
```

Parameters

Table 16-10 GET\_ASH\_QUERY Function Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task |
| `finding` | ID of the finding within the task |

Return Values

A `VARCHAR` containing an ASH query identifying the rows in ASH with impact for the finding

---

### GET\_REPORT Function

This function retrieves the default text report of an executed ADDM task.

Syntax

```
DBMS_ADDM.GET_REPORT (
   task_name           IN VARCHAR2)
  RETURN CLOB;
```

Parameters

Table 16-11 GET\_REPORT Function Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task |

Examples

```
Set long 1000000
Set pagesize 50000
SELECT DBMS_ADDM.GET_REPORT('my_partial_analysis_mode_task') FROM DUAL;
```

---

### INSERT\_FINDING\_DIRECTIVE Procedure

This procedure creates a directive to limit reporting of a specific finding type. The directive can be created for a specific task (only when the task is in `INITIAL` status), or for all subsequently created ADDM tasks (such as a system directive).

Syntax

```
DBMS_ADDM.INSERT_FINDING_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   finding_name          IN VARCHAR2,
   min_active_sessions   IN NUMBER := 0,
   min_perc_impact       IN NUMBER := 0);
```

Parameters

Table 16-12 INSERT\_FINDING\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it applies to all subsequently created ADDM Tasks. |
| `dir_name` | Name of the directive. All directives must be given unique names. |
| `finding_name` | Name of an ADDM finding to which this directive applies. All valid findings names appear in the `NAME` column of view `DBA_ADVISOR_FINDING_NAMES`. |
| `min_active_sessions` | Minimal number of active sessions for the finding. If a finding has less than this number, it is filtered from the ADDM result. |
| `min_perc_impact` | Minimal number for the "percent impact" of the finding relative to total database time in the analysis period. If the finding's impact is less than this number, it is filtered from the ADDM result. |

Examples

A new ADDM task is created to analyze a local instance. However, it has special treatment for 'Undersized SGA' findings. The result of `GET_REPORT` shows only an 'Undersized SGA' finding if the finding is responsible for at least 2 average active sessions during the analysis period, and this constitutes at least 10% of the total database time during that period.

```
var tname VARCHAR2(60);
BEGIN
  DBMS_ADDM.INSERT_FINDING_DIRECTIVE(
   NULL, 
   'Undersized SGA directive',
   'Undersized SGA', 
   2, 
   10); 
  :tname := 'my_instance_analysis_mode_task';
  DBMS_ADDM.ANALYZE_INST(:tname, 1, 2);
END;
```

To see a report containing 'Undersized SGA' findings regardless of the directive:

```
SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;
```

---

### INSERT\_PARAMETER\_DIRECTIVE Procedure

This procedure creates a directive to prevent ADDM from creating actions to alter the value of a specific system parameter. The directive can be created for a specific task (only when the task is in `INITIAL` status), or for all subsequently created ADDM tasks (such as a system directive).

Syntax

```
DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   parameter_name        IN VARCHAR2);
```

Parameters

Table 16-13 INSERT\_PARAMETER\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it applies to all subsequently created ADDM Tasks. |
| `dir_name` | Name of the directive. All directives must be given unique names. |
| `parameter_name` | Specifies the parameter to use. Valid parameter names appear in `V$PARAMETER.` |

Examples

A new ADDM task is created to analyze a local instance. However, it has special treatment for all actions that recommend modifying the parameter ' `sga_target` '. The result of `GET_REPORT` does not show these actions.

```
var tname varchar2(60);
BEGIN
  DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE(
   NULL,
   'my Parameter directive',
   'sga_target'); 
  :tname := 'my_instance_analysis_mode_task';
  DBMS_ADDM.ANALYZE_INST(:tname, 1, 2);
END;
```

To see a report containing all actions regardless of the directive:

```
SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;
```

---

### INSERT\_SEGMENT\_DIRECTIVE Procedure

This procedure creates a directive to prevent ADDM from creating actions to "run Segment Advisor" for specific segments. The directive can be created for a specific task (only when the task is in `INITIAL` status), or for all subsequently created ADDM tasks (such as a system directive).

Syntax

```
DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   owner_name            IN VARCHAR2,
   object_name           IN VARCHAR2 := NULL,
   sub_object_name       IN VARCHAR2 := NULL);
```
```
DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   object_number         IN NUMBER);
```

Parameters

Table 16-14 INSERT\_SEGMENT\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it applies to all subsequently created ADDM Tasks. |
| `dir_name` | Name of the directive. All directives must be given unique names. |
| `owner_name` | Specifies the owner of the segment/s to be filtered. A wildcard is allowed in the same syntax used for "like" constraints. |
| `object_name` | Name of the main object to be filtered. Again, wildcards are allowed. The default value of `NULL` is equivalent to a value of '%'. |
| `sub_object_name` | Name of the part of the main object to be filtered. This could be a partition name, or even sub partitions (separated by a '.'). Again, wildcards are allowed. The default value of `NULL` is equivalent to a value of '%'. |
| `object_number` | Object number of the `SEGMENT` that this directive is to filter, found in views `DBA_OBJECTS` or `DBA_SEGMENTS` |

Examples

A new ADDM task is created to analyze a local instance. However, it has special treatment for all segments that belong to user `SCOTT`. The result of `GET_REPORT` does not show actions for running Segment advisor for segments that belong to `SCOTT`.

```
var tname VARCHAR2(60);
BEGIN
  DBMS_ADDM.INSERT_SEGMENT_DIRECTIVE(NULL,
                                     'my Segment directive',
                                     'SCOTT'); 
  :tname := 'my_instance_analysis_mode_task';
  DBMS_ADDM.ANALYZE_INST(:tname, 1, 2);
END;
```

To see a report containing all actions regardless of the directive:

```
SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;
```

---

### INSERT\_SQL\_DIRECTIVE Procedure

This procedure creates a directive to limit reporting of actions on specific SQL. The directive can be created for a specific task (only when the task is in `INITIAL` status), or for all subsequently created ADDM tasks (such as a system directive).

Syntax

```
DBMS_ADDM.INSERT_SQL_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   sql_id                IN VARCHAR2,
   min_active_sessions   IN NUMBER := 0,
   min_response_time     IN NUMBER := 0);
```

Parameters

Table 16-15 INSERT\_SQL\_DIRECTIVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task this directive applies to. If the value is `NULL`, it applies to all subsequently created ADDM Tasks. |
| `dir_name` | Name of the directive. All directives must be given unique names. |
| `sql_id` | Identifies which SQL statement to filter. A valid value contains exactly 13 characters from '0' to '9' and 'a' to 'z'. |
| `min_active_sessions` | Minimal number of active sessions for the SQL. If a SQL action has less than this number, it is filtered from the ADDM result. |
| `min_response_time` | Minimal value for response time of the SQL (in microseconds). If the SQL had lower response time, it is filtered from the ADDM result. |

Examples

A new ADDM task is created to analyze a local instance. However, it has special treatment for SQL with id 'abcd123456789'. The result of `GET_REPORT` shows only actions for that SQL (actions to tune the SQL, or to investigate application using it) if the SQL is responsible for at least 2 average active sessions during the analysis period, and the average response time was at least 1 second.

```
var tname VARCHAR2(60);
BEGIN
  DBMS_ADDM.INSERT_SQL_DIRECTIVE(
      NULL,
      'my SQL directive',
      'abcd123456789',
      2,
      1000000); 
  :tname := 'my_instance_analysis_mode_task';
  DBMS_ADDM.ANALYZE_INST(:tname, 1, 2);
END;
```

To see a report containing all actions regardless of the directive:

```
SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;
```