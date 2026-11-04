---
title: DBMS_SCHEDULER
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sched.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 129 DBMS\_SCHEDULER

The `DBMS_SCHEDULER` package provides a collection of scheduling functions and procedures that can be called from any PL/SQL program.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/scheduse.htm#ADMIN034) for more information regarding how to use `DBMS_SCHEDULER`

This chapter contains the following topics:

---

## Data Structures

The `DBMS_SCHEDULER` package defines `OBJECT` types and `TABLE` types.

---

### JOBARG Object Type

This type is used by the `JOB` and `JOBATTR` object types. It represents a job argument in a batch of job arguments.

Syntax

```
TYPE jobarg IS OBJECT (
   arg_position         NUMBER,
   arg_text_value       VARCHAR2(4000),
   arg_anydata_value    ANYDATA,
   arg_operation        VARCHAR2(5));
```

Attributes

Table 129-1 JOBARG Object Type Attributes

| Attribute | Description |
| --- | --- |
| `arg_position` | Position of the argument |
| `arg_text_value` | Value of the argument if the type is `VARCHAR2` |
| `arg_anydata_value` | Value of the argument if the type is `AnyData` |
| `arg_operation` | Type of the operation:  - `SET` - `RESET` |

#### JOBARG Constructor Function

This constructor function constructs a job argument. It is overloaded to construct job arguments with different types of values.

Syntax

Constructs a job argument with a text value.

```
constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_value           IN VARCHAR2)
   RETURN SELF AS RESULT;
```

Constructs a job argument with an `AnyData` value.

```
constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_value           IN ANYDATA)
   RETURN SELF AS RESULT;
```

Constructs a job argument with a `NULL` value.

```
constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_reset           IN BOOLEAN DEFAULT FALSE)
   RETURN SELF AS RESULT;
```

Parameters

Table 129-2 JOBARG Constructor Function Parameters

| Parameter | Description |
| --- | --- |
| `arg_position` | Position of the argument |
| `arg_value` | Value of the argument |
| `arg_reset` | If `arg_reset` is `TRUE`, then the argument at that position is reset.  Setting `arg_reset` to `FALSE` (which is the default) will create an argument with a NULL value. |

---

#### JOBARG\_ARRAY Table Type

Syntax

```
TYPE jobarg_array IS TABLE OF jobarg;
```

---

### JOB Object Type

\*\*\*\* Deprecated. Use the `JOB_DEFINITION` object type instead.

---

#### JOB\_ARRAY Table Type

\*\*\* Deprecated. Use the `JOB_DEFINITION_ARRAY` table type instead.

---

### JOB\_DEFINITION Object Type

This type is used by the `CREATE_JOBS` procedure and represents a job in a batch of jobs.

Syntax

```
TYPE job_definition IS OBJECT (
  job_name                       VARCHAR2(100),
  job_class                      VARCHAR2(32),
  job_style                      VARCHAR2(11),
  program_name                   VARCHAR2(100),
  job_action                     VARCHAR2(4000),
  job_type                       VARCHAR2(20),
  schedule_name                  VARCHAR2(65),
  repeat_interval                VARCHAR2(4000),
  schedule_limit                 INTERVAL DAY TO SECOND,
  start_date                     TIMESTAMP WITH TIME ZONE,
  end_date                       TIMESTAMP WITH TIME ZONE,
  event_condition                VARCHAR2(4000),
  queue_spec                     VARCHAR2(100),
  number_of_arguments            NUMBER,
  arguments                      SYS.JOBARG_ARRAY,
  job_priority                   NUMBER,
  job_weight                     NUMBER,
  max_run_duration               INTERVAL DAY TO SECOND,
  max_runs                       NUMBER,
  max_failures                   NUMBER,
  logging_level                  NUMBER,
  restartable                    VARCHAR2(5),
  stop_on_window_close           VARCHAR2(5),
  raise_events                   NUMBER,
  comments                       VARCHAR2(240),
  auto_drop                      VARCHAR2(5),
  enabled                        VARCHAR2(5),
  follow_default_timezone        VARCHAR2(5),
  parallel_instances             VARCHAR2(5),
  aq_job                         VARCHAR2(5),
  instance_id                    NUMBER,
  credential_name                VARCHAR2(65),
  destination                    VARCHAR2(4000),
  database_role                  VARCHAR2(20),
  allow_runs_in_restricted_mode  VARCHAR2(5));
```

Object Attributes

Table 129-3 provides brief descriptions of the attributes of the `JOB_DEFINITION` object type. For more complete information about these attributes, see the "CREATE\_JOB Procedure" and the "SET\_ATTRIBUTE Procedure".

Table 129-3 JOB\_DEFINITION Object Type Attributes

| Attribute | Description |
| --- | --- |
| `job_name` | Name of the job |
| `job_class` | Name of the job class |
| `job_style` | Style of the job:  - `REGULAR` - `LIGHTWEIGHT` |
| `program_name` | Name of the program that the job runs |
| `job_action` | Inline action of the job. This is either the code for an anonymous PL/SQL block or the name of a stored procedure, external executable, or chain. |
| `job_type` | Job action type (' `PLSQL_BLOCK` ', ' `STORED_PROCEDURE` ', ' `EXECUTABLE` ', or ' `CHAIN` ') |
| `schedule_name` | Name of the schedule that specifies when the job has to execute |
| `repeat_interval` | Inline time-based schedule |
| `schedule_limit` | Maximum delay time between scheduled and actual job start before a job run is canceled |
| `start_date` | Start date and time of the job |
| `end_date` | End date and time of the job |
| `event_condition` | Event condition for event-based jobs |
| `queue_spec` | File watcher name or queue specification for event-based jobs |
| `number_of_arguments` | Number of job arguments |
| `arguments` | Array of job arguments |
| `job priority` | Job priority |
| `job_weight` | \*\*\* Deprecated in Oracle Database 11g Release 2 (11.2). Do not change the value of this attribute from the default, which is 1.  Weight of the job for parallel execution. |
| `max_run_duration` | Maximum run duration of the job |
| `max_runs` | Maximum number of runs before the job is marked as completed |
| `max_failures` | Maximum number of failures tolerated before the job is marked as broken |
| `logging_level` | Job logging level |
| `restartable` | Indicates whether the job is restartable (`TRUE`) or not (`FALSE`) |
| `stop_on_window_exit` | Indicates whether the job is stopped when the window that it runs in ends (`TRUE`) or not (`FALSE`). Equivalent to the `stop_on_window_close` job attribute described in the SET\_ATTRIBUTE Procedure. |
| `raise_events` | State changes that raise events |