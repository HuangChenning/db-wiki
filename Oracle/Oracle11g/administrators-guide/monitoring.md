---
title: Monitoring Database Operations
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/monitoring.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 8 Monitoring Database Operations

It is important that you monitor the operation of your database on a regular basis. Doing so not only informs you of errors that have not yet come to your attention but also gives you a better understanding of the normal operation of your database. Being familiar with normal behavior in turn helps you recognize when something is wrong.

In this chapter:

- Monitoring Errors and Alerts
- Monitoring Performance

## Monitoring Errors and Alerts

The following sections explain how to monitor database errors and alerts. It contains the following topics:

- Monitoring Errors with Trace Files and the Alert Log
- Monitoring Database Operations with Server-Generated Alerts

Note:

The easiest and best way to monitor the database for errors and alerts is with the Database Home page in Enterprise Manager. This section provides alternate methods for monitoring, using data dictionary views, PL/SQL packages, and other command-line facilities.

### Monitoring Errors with Trace Files and the Alert Log

Each server and background process can write to an associated trace file. When an internal error is detected by a process, it dumps information about the error to its trace file. Some of the information written to a trace file is intended for the database administrator, and other information is for Oracle Support Services. Trace file information is also used to tune applications and instances.

Note:

Critical errors also create incidents and incident dumps in the Automatic Diagnostic Repository. See [Chapter 9, "Managing Diagnostic Data"](diag.md) for more information.

The alert log is a chronological log of messages and errors, and includes the following items:

- All internal errors (`ORA-00600`), block corruption errors (`ORA-01578`), and deadlock errors (`ORA-00060`) that occur
- Administrative operations, such as `CREATE`, `ALTER`, and `DROP` statements and `STARTUP`, `SHUTDOWN`, and `ARCHIVELOG` statements
- Messages and errors relating to the functions of shared server and dispatcher processes
- Errors occurring during the automatic refresh of a materialized view
- The values of all initialization parameters that had nondefault values at the time the database and instance start

Oracle Database uses the alert log to record these operations as an alternative to displaying the information on an operator's console (although some systems also display information on the console). If an operation is successful, a "completed" message is written in the alert log, along with a timestamp.

The alert log is maintained as both an XML-formatted file and a text-formatted file. You can view either format of the alert log with any text editor or you can use the ADRCI utility to view the XML-formatted version of the file with the XML tags stripped.

Check the alert log and trace files of an instance periodically to learn whether the background processes have encountered errors. For example, when the log writer process (LGWR) cannot write to a member of a log group, an error message indicating the nature of the problem is written to the LGWR trace file and the alert log. Such an error message means that a media or I/O problem has occurred and should be corrected immediately.

Oracle Database also writes values of initialization parameters to the alert log, in addition to other important statistics.

The alert log and all trace files for background and server processes are written to the Automatic Diagnostic Repository, the location of which is specified by the `DIAGNOSTIC_DEST` initialization parameter. The names of trace files are operating system specific, but each file usually includes the name of the process writing the file (such as LGWR and RECO).

See Also:

- [Chapter 9, "Managing Diagnostic Data"](diag.md) for information on the Automatic Diagnostic Repository.
- ["Alert Log"](diag.md) for additional information about the alert log.
- ["Viewing the Alert Log"](diag.md)
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/adrci.htm#SUTIL700) for information on the ADRCI utility.
- Your operating system specific Oracle documentation for information about the names of trace files

#### Controlling the Size of Trace Files

You can control the maximum size of all trace files (excluding the alert log) using the initialization parameter `MAX_DUMP_FILE_SIZE`, which limits the file to the specified number of operating system blocks. To control the size of an alert log, you must manually delete the file when you no longer need it. Otherwise the database continues to append to the file.

You can safely delete the alert log while the instance is running, although you should consider making an archived copy of it first. This archived copy could prove valuable if you should have a future problem that requires investigating the history of an instance.

#### Controlling When Oracle Database Writes to Trace Files

Background processes always write to a trace file when appropriate. In the case of the ARCn background process, it is possible, through an initialization parameter, to control the amount and type of trace information that is produced. This behavior is described in ["Controlling Trace Output Generated by the Archivelog Process"](archredo.md). Other background processes do not have this flexibility.

Trace files are written on behalf of server processes whenever critical errors occur. Additionally, setting the initialization parameter `SQL_TRACE = TRUE` causes the SQL trace facility to generate performance statistics for the processing of all SQL statements for an instance and write them to the Automatic Diagnostic Repository.

Optionally, you can request that trace files be generated for server processes. Regardless of the current value of the `SQL_TRACE` initialization parameter, each session can enable or disable trace logging on behalf of the associated server process by using the SQL statement `ALTER SESSION SET SQL_TRACE`. This example enables the SQL trace facility for a specific session:

```
ALTER SESSION SET SQL_TRACE TRUE;
```

Use the `DBMS_SESSION` or the `DBMS_MONITOR` packages to control SQL tracing for a session.

Caution:

The SQL trace facility for server processes can cause significant system overhead resulting in severe performance impact, so you should enable this feature only when collecting statistics.

See Also:

- [Chapter 9, "Managing Diagnostic Data"](diag.md) for more information on how the database handles critical errors, otherwise known as "incidents."

#### Reading the Trace File for Shared Server Sessions

If shared server is enabled, each session using a dispatcher is routed to a shared server process, and trace information is written to the server trace file only if the session has enabled tracing (or if an error is encountered). Therefore, to track tracing for a specific session that connects using a dispatcher, you might have to explore several shared server trace files. To help you, Oracle provides a command line utility program, `trcsess`, which consolidates all trace information pertaining to a user session in one place and orders the information by time.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/sqltrace.htm#PFGRF010) for information about using the SQL trace facility and using `TKPROF` and `trcsess` to interpret the generated trace files

### Monitoring Database Operations with Server-Generated Alerts

A server-generated alert is a notification from the Oracle Database server of an impending problem. The notification may contain suggestions for correcting the problem. Notifications are also provided when the problem condition has been cleared.

Alerts are automatically generated when a problem occurs or when data does not match expected values for metrics, such as the following:

- Physical Reads Per Second
- User Commits Per Second
- SQL Service Response Time

Server-generated alerts can be based on threshold levels or can issue simply because an event has occurred. Threshold-based alerts can be triggered at both threshold warning and critical levels. The value of these levels can be customer-defined or internal values, and some alerts have default threshold levels which you can change if appropriate. For example, by default a server-generated alert is generated for tablespace space usage when the percentage of space usage exceeds either the 85% warning or 97% critical threshold level. Examples of alerts not based on threshold levels are:

- `Snapshot Too Old`
- `Resumable Session Suspended`
- `Recovery Area Space Usage`

An alert message is sent to the predefined persistent queue `ALERT_QUE` owned by the user `SYS`. Oracle Enterprise Manager reads this queue and provides notifications about outstanding server alerts, and sometimes suggests actions for correcting the problem. The alerts are displayed on the Enterprise Manager Database Home page and can be configured to send email or pager notifications to selected administrators. If an alert cannot be written to the alert queue, a message about the alert is written to the Oracle Database alert log.

Background processes periodically flush the data to the Automatic Workload Repository to capture a history of metric values. The alert history table and `ALERT_QUE` are purged automatically by the system at regular intervals.

#### Setting and Retrieving Thresholds for Server-Generated Alerts

You can view and change threshold settings for the server alert metrics using the `SET_THRESHOLD` and `GET_THRESHOLD` procedures of the `DBMS_SERVER_ALERT` PL/SQL package. Examples of using these procedures are provided in the following sections:

- Setting Threshold Levels
- Retrieving Threshold Information

Note:

The most convenient way to set and retrieve threshold values is to use the graphical interface of Enterprise Manager. See [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/montune.htm#ADMQS1014) for instructions.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_server_alert.htm#ARPLS016) for information about the `DBMS_SERVER_ALERT` package

##### Setting Threshold Levels

The following example shows how to set thresholds with the `SET_THRESHOLD` procedure for CPU time for each user call for an instance:

```
DBMS_SERVER_ALERT.SET_THRESHOLD(
 DBMS_SERVER_ALERT.CPU_TIME_PER_CALL, DBMS_SERVER_ALERT.OPERATOR_GE, '8000', 
 DBMS_SERVER_ALERT.OPERATOR_GE, '10000', 1, 2, 'inst1',
 DBMS_SERVER_ALERT.OBJECT_TYPE_SERVICE, 'main.regress.rdbms.dev.us.example.com');
```

In this example, a warning alert is issued when CPU time exceeds 8000 microseconds for each user call and a critical alert is issued when CPU time exceeds 10,000 microseconds for each user call. The arguments include:

- `CPU_TIME_PER_CALL` specifies the metric identifier. For a list of support metrics, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_server_alert.htm#ARPLS016).
- The observation period is set to 1 minute. This period specifies the number of minutes that the condition must deviate from the threshold value before the alert is issued.
- The number of consecutive occurrences is set to 2. This number specifies how many times the metric value must violate the threshold values before the alert is generated.
- The name of the instance is set to `inst1`.
- The constant `DBMS_ALERT.OBJECT_TYPE_SERVICE` specifies the object type on which the threshold is set. In this example, the service name is `main.regress.rdbms.dev.us.example.com`.

##### Retrieving Threshold Information

To retrieve threshold values, use the `GET_THRESHOLD` procedure. For example:

```
DECLARE
 warning_operator         BINARY_INTEGER;
 warning_value            VARCHAR2(60);
 critical_operator        BINARY_INTEGER; 
 critical_value           VARCHAR2(60);
 observation_period       BINARY_INTEGER;
 consecutive_occurrences  BINARY_INTEGER;
BEGIN
 DBMS_SERVER_ALERT.GET_THRESHOLD(
 DBMS_SERVER_ALERT.CPU_TIME_PER_CALL, warning_operator, warning_value,
    critical_operator, critical_value, observation_period, 
    consecutive_occurrences, 'inst1',
 DBMS_SERVER_ALERT.OBJECT_TYPE_SERVICE, 'main.regress.rdbms.dev.us.example.com');
 DBMS_OUTPUT.PUT_LINE('Warning operator:       ' || warning_operator);
 DBMS_OUTPUT.PUT_LINE('Warning value:          ' || warning_value);
 DBMS_OUTPUT.PUT_LINE('Critical operator:      ' || critical_operator);
 DBMS_OUTPUT.PUT_LINE('Critical value:         ' || critical_value);     
 DBMS_OUTPUT.PUT_LINE('Observation_period:     ' || observation_period);
 DBMS_OUTPUT.PUT_LINE('Consecutive occurrences:' || consecutive_occurrences);
END;
/
```

You can also check specific threshold settings with the `DBA_THRESHOLDS` view. For example:

```
SELECT metrics_name, warning_value, critical_value, consecutive_occurrences 
   FROM DBA_THRESHOLDS 
   WHERE metrics_name LIKE '%CPU Time%';
```

#### Viewing Server-Generated Alerts

The easiest way to view server-generated alerts is by accessing the Database Home page of Enterprise Manager. The following discussion presents other methods of viewing these alerts.

If you use your own tool rather than Enterprise Manager to display alerts, you must subscribe to the `ALERT_QUE`, read the `ALERT_QUE`, and display an alert notification after setting the threshold levels for an alert. To create an agent and subscribe the agent to the `ALERT_QUE`, use the `CREATE_AQ_AGENT` and `ADD_SUBSCRIBER` procedures of the `DBMS_AQADM` package.

Next you must associate a database user with the subscribing agent, because only a user associated with the subscribing agent can access queued messages in the secure `ALERT_QUE`. You must also assign the enqueue privilege to the user. Use the `ENABLE_DB_ACCESS` and `GRANT_QUEUE_PRIVILEGE` procedures of the `DBMS_AQADM` package.

Optionally, you can register with the `DBMS_AQ.REGISTER` procedure to receive an asynchronous notification when an alert is enqueued to `ALERT_QUE`. The notification can be in the form of email, HTTP post, or PL/SQL procedure.

To read an alert message, you can use the `DBMS_AQ.DEQUEUE` procedure or `OCIAQDeq` call. After the message has been dequeued, use the `DBMS_SERVER_ALERT.EXPAND_MESSAGE` procedure to expand the text of the message.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information about the `DBMS_AQ`, and `DBMS_AQADM` packages

#### Server-Generated Alerts Data Dictionary Views

The following data dictionary views provide information about server-generated alerts.

| View | Description |
| --- | --- |
| `DBA_THRESHOLDS` | Lists the threshold settings defined for the instance |
| `DBA_OUTSTANDING_ALERTS` | Describes the outstanding alerts in the database |
| `DBA_ALERT_HISTORY` | Lists a history of alerts that have been cleared |
| `V$ALERT_TYPES` | Provides information such as group and type for each alert |
| `V$METRICNAME` | Contains the names, identifiers, and other information about the system metrics |
| `V$METRIC` | Contains system-level metric values |
| `V$METRIC_HISTORY` | Contains a history of system-level metric values |

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for information on static data dictionary views and dynamic performance views

## Monitoring Performance

Monitoring database performance is covered in detail in [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm). Here are some additional topics with details that are not covered in that guide:

- Monitoring Locks
- Monitoring Wait Events
- Performance Monitoring Data Dictionary Views

### Monitoring Locks

Locks are mechanisms that prevent destructive interaction between transactions accessing the same resource. The resources can be either user objects, such as tables and rows, or system objects not visible to users, such as shared data structures in memory and data dictionary rows. Oracle Database automatically obtains and manages necessary locks when executing SQL statements, so you need not be concerned with such details. However, the database also lets you lock data manually.

A deadlock can occur when two or more users are waiting for data locked by each other. Deadlocks prevent some transactions from continuing to work. Oracle Database automatically detects deadlock situations and resolves them by rolling back one of the statements involved in the deadlock, thereby releasing one set of the conflicting row locks.

Oracle Database is designed to avoid deadlocks, and they are not common. Most often they occur when transactions explicitly override the default locking of the database. Deadlocks can affect the performance of your database, so Oracle provides some scripts and views that enable you to monitor locks.

The `utllockt.sql` script displays, in a tree fashion, the sessions in the system that are waiting for locks and the locks that they are waiting for. The location of this script file is operating system dependent.

A second script, `catblock.sql`, creates the lock views that `utllockt.sql` needs, so you must run it before running `utllockt.sql`.

See Also:

- "Performance Monitoring Data Dictionary Views"
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/consist.htm#CNCPT1339) contains more information about locks.

### Monitoring Wait Events

Wait events are statistics that are incremented by a server process to indicate that it had to wait for an event to complete before being able to continue processing. A session could wait for a variety of reasons, including waiting for more input, waiting for the operating system to complete a service such as a disk write, or it could wait for a lock or latch.

When a session is waiting for resources, it is not doing any useful work. A large number of waits is a source of concern. Wait event data reveals various symptoms of problems that might be affecting performance, such as latch contention, buffer contention, and I/O contention.

Oracle provides several views that display wait event statistics. A discussion of these views and their role in instance tuning is contained in [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/instance_tune.htm#PFGRF02410).

### Performance Monitoring Data Dictionary Views

This section lists some of the data dictionary views that you can use to monitor an Oracle Database instance. These views are general in their scope. Other views, more specific to a process, are discussed in the section of this book where the process is described.

| View | Description |
| --- | --- |
| `V$LOCK` | Lists the locks currently held by Oracle Database and outstanding requests for a lock or latch |
| `DBA_BLOCKERS` | Displays a session if it is holding a lock on an object for which another session is waiting |
| `DBA_WAITERS` | Displays a session if it is waiting for a locked object |
| `DBA_DDL_LOCKS` | Lists all DDL locks held in the database and all outstanding requests for a DDL lock |
| `DBA_DML_LOCKS` | Lists all DML locks held in the database and all outstanding requests for a DML lock |
| `DBA_LOCK` | Lists all locks or latches held in the database and all outstanding requests for a lock or latch |
| `DBA_LOCK_INTERNAL` | Displays a row for each lock or latch that is being held, and one row for each outstanding request for a lock or latch |
| `V$LOCKED_OBJECT` | Lists all locks acquired by every transaction on the system |
| `V$SESSION_WAIT` | Lists the resources or events for which active sessions are waiting |
| `V$SYSSTAT` | Contains session statistics |
| `V$RESOURCE_LIMIT` | Provides information about current and maximum global resource utilization for some system resources |
| `V$SQLAREA` | Contains statistics about shared SQL area and contains one row for each SQL string. Also provides statistics about SQL statements that are in memory, parsed, and ready for execution |
| `V$LATCH` | Contains statistics for nonparent latches and summary statistics for parent latches |

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for detailed descriptions of these views