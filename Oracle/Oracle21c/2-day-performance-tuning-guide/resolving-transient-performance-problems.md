---
title: "2 Day + Performance Tuning Guide"
book: "2 Day + Performance Tuning Guide"
doc_id: F32092-02
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tdppt/resolving-transient-performance-problems.html
tags:
  - oracle
  - 21c
  - 2-day-performance-tuning-guide
---

Transient performance problems are short-lived and typically do not appear in the Automatic Database Diagnostic Monitor (ADDM) analysis. ADDM tries to report the most significant performance problems during an analysis period in terms of their effect on database time (DB time). If a problem lasts for a brief time, then its severity might be averaged out or minimized by other performance problems in the entire analysis period. Therefore, the problem may not appear in the ADDM findings. Whether or not a performance problem is captured by ADDM depends on its duration compared to the interval between the Automatic Workload Repository (AWR) snapshots.

If a performance problem lasts for a significant portion of the time between snapshots, then it is captured by ADDM. For example, if the snapshot interval is one hour, then a performance problem that lasts 30 minutes should not be considered a transient performance problem because its duration represents a significant portion of the snapshot interval and is likely to be captured by ADDM.

On the other hand, a performance problem that lasts 2 minutes could be transient because its duration is a small portion of the snapshot interval and probably does not appear in the ADDM findings. For example, if the system was slow between 10:00 p.m. and 10:10 p.m., and if the ADDM analysis for the time period between 10:00 p.m. and 11:00 p.m. does not show a problem, then a transient problem may have occurred for only a few minutes of the 10-minute interval.

This chapter contains the following sections:

- Overview of Active Session History
- Running Active Session History Reports
- Active Session History Reports
- [Diagnosing Serious Performance Problems in Real Time](unresolvable-reference.md)

### Overview of Active Session History

To capture a detailed history of database activity, Oracle Database samples active sessions each second with the Active Session History (ASH) sampler. AWR snapshot processing collects the sampled data into memory and writes it to persistent storage. ASH is an integral part of the Oracle Database self-management framework and is extremely useful for diagnosing performance problems.

ASH gathers sampled data at the session level rather than at the instance level. By capturing statistics for only active sessions, ASH collects a manageable set of data. The size of this data is directly related to the work being performed, rather than to the size of the entire database instance.

Sampled data captured by ASH can be aggregated based on the dimensions in the data, including the following:

- SQL identifier of a SQL statement
- Object number, file number, and block number
- Wait event identifier and parameters
- Session identifier and session serial number
- Module and action name
- Client identifier of the session
- Service hash identifier

You can run ASH reports to analyze transient performance problems with the database that only occur during specific times. This technique is especially useful when you are trying to do either of the following:

- Resolve transient performance problems that may last for only a short period of time, such as why a particular job or session is not responding when the rest of the instance is performing as usual
- Perform scoped or targeted performance analysis by various dimensions or their combinations, such as time, session, module, action, or SQL identifier

See Also:

- " [Active Session History Statistics](oracle-database-performance-method.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA276) for more detailed information about ASH reports

### Running Active Session History Reports

This section describes how to generate ASH reports using Oracle Enterprise Manager Cloud Control (Cloud Control).

To run ASH reports:

1. Access the Database Home page.
	See " [Accessing the Database Home Page](introduction.md) " for more information.
2. From the Performance menu, select Performance Home.
	If the Database Login page appears, then log in as a user with administrator privileges. The Performance page appears.
3. Under Average Active Sessions, click Run ASH Report.
	The Run ASH Report page appears.
4. Enter the date and time for the start and end of the time period when the transient performance problem occurred.
	In this example, database activity increased between 9:15 p.m. and 9:20 p.m., so an ASH report should be created for that time period.
	![run_ash](img/run_ash.gif)

> The screenshot shows the Run ASH Report page.
>
> The Generate Report button is on the upper right of the screen.
>
> The Start Date field has the value 1/17/12. A calendar icon is next to the field.
>
> The End Date field has the value 1/17/12. A calendar icon is next to the field.
>
> The Start Time and End Time groups have lists for hours and minutes and option buttons for AM and PM. The start time value is 9:15 PM. The End Time value is 9:20 PM.
>
> The Filter list shows the value SID. Next to the list is an empty text field.
>
> End of description.

5. Click Generate Report.
	The Processing: View Report page appears while the report is being generated.
	After the report is generated, the ASH report appears under Report Results on the Run ASH Report page.
	![ash_report](img/ash_report.gif)

> The screenshot shows the beginning of the Report Results section of the Run Ash Report page. The report is entitled ASH Report for EMPDB/empdb. To the right of the title is the Save to File button.At the top of the report is a table with the following columns: DB Name, DB Id, Instance, Inst Num, Release, RAC, and Host. The table has one row, which shows the following values: EMPDB, 647168497, empdb, 1, 12.1.0.0.1, NO, and dbhost.The next table has the following columns: CPUs, SGA Size, Buffer Cache, Shared Pool, and ASH Buffer Size. The table has one row, which shows the following values: 2, 1,019M (100%), 68M (6.7%), 408M (40.0%), and 4.0M (0.4%).The next table has the following columns: null, Sample Time, and Data Source. The table contains 7 rows. The values in the rows are the following:
>
> - Row 1: Analysis Begin Time, 17-Jan-12 09:15:32, V$ACTIVE\_SESSION\_HISTORY
> - Row 2: Analysis End Time, 17-Jan-12 09:20:32, V$ACTIVE\_SESSION\_HISTORY
> - Row 3: Elapsed Time, 5.0 (mins), null
> - Row 4: Sample Count, 431, null
> - Row 5: Average Active Sessions, 1.44, null
> - Row 6: Avg. Active Session per CPU, 0.72, null
> - Row 7: Report Target, None specified, null
>
> Below the table is the heading "ASH Report." The following links appear below the heading: Top Events, Load Profile, Top SQL, Top PL/SQL, Top Java, Top Call Types, Top Sessions, Top Objects/Files/Latches, Activity Over Time.
>
> End of description.

	See Also:
	" Active Session History Reports " for descriptions of some of the reports.
6. Optionally, click Save to File to save the report in HTML format for future analysis.

### Active Session History Reports

You can use an ASH report to identify the source of transient performance problems. The report is divided into titled sections. The following sections of the ASH report are useful places to begin the investigation:

- Top Events
- Load Profile
- Top SQL
- Top Sessions
- Top DB Objects/Files/Latches
- Activity Over Time

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA276) for more detailed information about ASH reports

#### Top Events

The Top Events section of the report describes the top wait events of the sampled session activity categorized by user, background, and priority. Use this information to identify the wait events that may be the cause of the transient performance problem.

The Top Events section of the report contains the following subsections:

- Top User Events
- Top Background Events

##### Top User Events

The Top User Events subsection of the report lists the top wait events from client processes that accounted for the highest percentages of sampled session activity.

Figure 8-1 shows that most database activity is consumed by the `CPU + Wait for CPU` event. The Wait for CPU is the time the process spent in the operating system run queue. The `%Event` column shows the percentage of DB time consumed by this event. In this example, over 30 percent of DB time was spent either on the CPU or waiting to get on it. The Load Profile section should be examined next to determine the type of activity that is causing this CPU consumption.

Figure 8-1 Top User Events

![Figure 8-1 Top User Events](img/ash_top_user_events.gif)

> The screenshot shows the Top User Events section of the report results.
>
> The table has the following columns: Event, Event Class, % Event, and Avg Active Sessions. The rows of the table have the following values:
>
> - Row 1: CPU + Wait for CPU, CPU, 30.56, 1.10
> - Row 2: db file sequential read, User I/O, 23.64, 0.85
> - Row 3: flashback buf free by RVWR, Configuration, 3.32, 0.12
> - Row 4: latch: shared pool, Concurrency, 1.02, 0.04
>
> End of description.


##### Top Background Events

The Top Background Events subsection lists the top wait events from the background events that accounted for the highest percentages of sampled session activity.

The example in Figure 8-2 shows that 22.81 percent of sampled session activity is consumed by the `CPU + Wait for CPU` event.

Figure 8-2 Top Background Events

![Figure 8-2 Top Background Events](img/top_back_events.gif)

> The screenshot shows the Top Background Events section of the report results.
>
> The table has the following columns: Event, Event Class, % Activity, Avg Active Sessions. The rows of the table have the following values:
>
> - Row 1: CPU + Wait for CPU, CPU, 22.81, 0.82
> - Row 2: log file parallel write, System I/O, 8.22, 0.30
> - Row 3: control file parallel write, System I/O, 3.05, 0.11
> - Row 4: control file sequential read, System I/O, 1.11, 0.04
> - Row 5: db file sequential read, User I/O, 1.11, 0.04
>
> End of description.


#### Load Profile

The Load Profile section of the report describes the load analyzed in the sampled session activity. Use the information in this section to identify the service, client, or SQL command type that may be the cause of the transient performance problem.

The Top Service/Module subsection lists the services and modules that accounted for the highest percentages of sampled session activity. A service is a group of related database tasks that share common functionality, quality expectations, and priority. Services are a convenient way to monitor multiple applications. The `SYS$USERS` and `SYS$BACKGROUND` services are always defined.

Figure 8-3 shows that over half of the database activity is consumed by the `SYS$USERS` service running the SQL\*Plus module. In this example, it appears that the user is running high-load SQL that is causing the performance problem indicated in Figure 8-1. The Top SQL section of the report should be analyzed next to determine whether a particular type of SQL statement makes up the load.

Figure 8-3 Top Service/Module

![Figure 8-3 Top Service/Module](img/ash_top_service_module.gif)

> The screenshot shows the Top Service/Module section of the report results.
>
> The table contains the following columns: Service, Module, % Activity, Action, and % Action. The rows of the table have the following values:
>
> - Row 1: SYS$USERS, SQL\*Plus, 54.66, EMP\_DML, 27.33
> - Row 2: null, null, null, SALES\_INFO, 27.33
> - Row 3: SYS$BACKGROUND, UNNAMED, 35.83, UNNAMED, 35.83
> - Row 4: null, MMON\_SLAVE, 4:16, Auto-Flush Slave Action, 2.86
> - Row 5: null, null, null, Auto ADDM Slave Action, and 1.29
> - Row 6: SYS$USERS, UNNAMED, 2.31, UNNAMED, and 2.31
> - Row 7: emagent@dbhost (TNS V1-V3), 1.57, UNNAMED, 1.57
>
> End of description.


See Also:

- " [Monitoring Top Services](monitoring-real-time-database-performance.md) "
- " [Monitoring Top Modules](monitoring-real-time-database-performance.md) "

#### Top SQL

The Top SQL section of the report describes the top SQL statements of the sampled session activity. Use this information to identify high-load SQL statements that may be the cause of the transient performance problem. The Top SQL with Top Events subsection lists the SQL statements that accounted for the highest percentages of sampled session activity. The Sampled # of Executions column shows how many distinct executions of a particular SQL statement were sampled. To view the text of the SQL statements, click the SQL ID link.

Figure 8-4 shows that over half of DB time is consumed by three DML statements. These statements were run in the SQL\*Plus module shown in Figure 8-3. The Top Sessions section should be analyzed to identify the sessions running these statements.

Figure 8-4 Top SQL with Top Events

![Figure 8-4 Top SQL with Top Events](img/ash_top_sql.gif)

> The screenshot shows the Top SQL with Top Events section of the report results.
>
> The table contains the following columns: SQL ID, Planhash, Sampled # of Executions, % Activity, Event, % Event, Top Row Source, % RwSrc, SQL Text. Values in the SQL ID column are links. The rows of the table have the following values:
>
> - Row 1: 31h2wmu3q47u6, 4090065844, 277, 26.22, CPU + Wait for CPU, 26.13, TABLE ACCESS - FULL, 19.94, SELECT /\*+ ORDERED USE\_NL(c)
> - Row 2: 3djkjtba139ct, 1426549735, 148, 13.76, db file sequential read, 12.00, \*\* Row Source Not Available \*\*, 12.00, INSERT INTO EMPLOYEES VALUES
> - Row 3: null, null, null, null, flashback buf free by RVWR, 1.39, \*\* Row Source Not Available \*\*,1.39, null
> - Row 4: 7u628xsamhqka, 781635435, 127, 11.82, db file sequential read, 9.70, DELETE, 9.70, DELETE FROM EPLOYEES WHERE EM...
> - Row 5: null, null, null, null, flashback buf free by RVWR, 1.75, DELETE, 1.75, null
>
> End of description.


See Also:

- " [Monitoring Top SQL](monitoring-real-time-database-performance.md) "

#### Top Sessions

The Top Sessions section lists the sessions that were waiting for the wait event that accounted for the highest percentages of sampled session activity. Use this information to identify the sessions that may be the cause of the performance problem.

The `# Samples Active` column shows the number of ASH samples in which the session was found waiting for that particular event. The percentage is calculated based on wall-clock time.

In Figure 8-5, the `# Samples Active` column shows that of the 300 times that ASH sampled database activity, the `HR` session (SID 123) performed a sequential read 243 times and a flashback operation 36 times. So, `HR` was active at least 93% of the time. The session consumed 27% of the total activity (much less than 93%) because other sessions, including the `SH` session, were also active.

It appears that the `HR` and `SH` sessions were running the high-load SQL statement in Figure 8-4. You should investigate this session to determine whether it is performing a legitimate operation and tune the SQL statement if possible. If tuning the SQL is not possible, and if a session is causing an unacceptable performance impact on the system, then consider terminating the session.

Figure 8-5 Top Sessions

![Figure 8-5 Top Sessions](img/ash_top_sessions.gif)

> The table has eight columns. The title of the first column is Sid, Serial#. The titles of the other columns are: % Activity, Event, % Event, User, Program, # Samples Active, XIDs. The table has seven rows.
>
> Row 1 contains the following values: 123,275, 27.33, db file sequential read, 22.44, HR, sqlplus -L@dbh...1 (TNS V1-V3), 243/300 \[81%\], 16.
>
> Row 2 contains the following values: null, null, flashback buf free by RVWR, 3.32, null, null, 36/300 \[12%\], 4.
>
> Row 3 contains the following values: 126,28313, 27.33, CPU + Wait for CPU, 26.78, SH, sqlplus -L@dbh...1 (TNS V1-V3), 290/300 \[97%\], 0.
>
> Row 4 contains the following values: 154,5, 15.24, CPU + Wait for CPU, 11.54, SYS, oracle@dbhost (RVWR), 125/300 \[42%\], 0.
>
> Row 5 contains the following values: null, null, control file parallel write, 2.12, null, null, 23/300 \[8%\], 0.
>
> Row 6 contains the following values: 161,1, 8.31, log file parallel write, 8.22, SYS, oracle@dbhost (LGWR), 89/300 \[30%\], 0.
>
> Row 7 contains the following values: 110,36790, 2.86, CPU + Wait for CPU, 1.11, SYS, oracle@dbhost (M000), 12/300 \[4%\], 0.
>
> End of description.


See Also:

- " [Monitoring Top Sessions](monitoring-real-time-database-performance.md) "
- " [Tuning SQL Statements](tuning-sql-statements.md) "

#### Top DB Objects/Files/Latches

The Top Objects/Files/Latches section provides additional information about the most commonly-used database resources and contains the following subsections:

- Top DB Objects
- Top DB Files
- Top Latches

##### Top DB Objects

The Top DB Objects subsection lists the database objects (such as tables and indexes) that accounted for the highest percentages of sampled session activity.

The example in Figure 8-6 shows that the `hr.departments` and `hr.employees` tables account for a high percentage of activity. Enqueue waits are waits for locks. In this example, the wait is for the TM (table) lock. Sometimes these waits indicate unindexed foreign key constraints. The `buffer busy waits` event records waits for a buffer to become available. These waits indicate that multiple processes are attempting to concurrently access the same buffers in the buffer cache.

Figure 8-6 Top DB Objects

![Figure 8-6 Top DB Objects](img/top_db_objects.gif)

> This screenshot shows the Top DB Objects section.
>
> The table has the following columns: Object ID, % Activity, Event, % Event, Object Name (Type), and Tablespace. The table has two rows.
>
> Row 1 has the following values: 66590, 32.10, enq:TM - contention, 32.10, HR.DEPARTMENTS (TABLE), EXAMPLE.
>
> Row 2 has the following values: 66595, 1.99, buffer busy waits, 1.99, HR.EMPLOYEES (TABLE), EXAMPLE.
>
> End of description.


##### Top DB Files

The Top DB Files subsection lists the database files that accounted for the highest percentages of sampled session activity. Only cluster and I/O events are considered. The `% Event` column breaks down the activity by event, so if multiple rows exist in this table, then the sampled activity is divided among multiple events.

Figure 8-7 shows that about 11 percent of DB time involves waits for the `UNDOTBS` tablespace. This information is consistent with Figure 8-4, which shows significant DML activity from multiple sessions.

Figure 8-7 Top DB Files

![Figure 8-7 Top DB Files](img/ash_top_files.gif)

> The Top DB Files section is shown. The section has a table.
>
> Above the table, a line of text says, "With respect to Cluster and User I/O events only."
>
> The table has the following columns: File ID, Activity (%), Event, % Event, File Name, Tablespace.
>
> The table has one row, which has the following values: 4, 11.54, db file sequential read, 11.54, /disk1/oracle/dbs/emtst/undotbs.dbf, UNDOTBS.
>
> End of description.


##### Top Latches

The Top Latches subsection lists the latches that accounted for the highest percentages of sampled session activity. Latches are simple, low-level serialization mechanisms to protect shared data structures in the System Global Area (SGA).

#### Activity Over Time

The Activity Over Time section of the ASH report is particularly useful for longer time periods because it provides in-depth details about activities and workload profiles during the analysis period. The Activity Over Time section is divided into time slots. The ASH report time span is divided into 10 time slots unless the time period is short or the data is sparse.

Figure 8-8 shows an activity report for the period between 2:10 p.m. and 2:40 p.m. The report indicates that the number of sampled sessions rose sharply in the sixth inner slot (2:24 p.m.) and stayed up. During this period CPU activity and lock enqueue waits increased dramatically.

Figure 8-8 Activity Over Time

![Figure 8-8 Activity Over Time](img/ash_activity_over_time.gif)

> The Activity Over Time section is shown. The section has a table.
>
> The table contains the following columns: Slot Time (Duration), Slot Count, Event, Event Count, % Event. The table has 31 rows.
>
> Row 1 has the values: 14:10:50 (1.2 min), 5, control file sequential read, 4, 0.11.
>
> Row 2 has the values: null, null, CPU + Wait for CPU, 1, 0.03.
>
> Row 3 has the values: 14:12:00 (3.0 min), 9, CPU + Wait for CPU, 5, 0.14.
>
> Row 4 has the values: null, null, control file parallel write, 2, 0.05.
>
> Row 5 has the values: null, null, null event, 1, 0.03.
>
> Row 6 has the values: 14:15:00 (3.0 min), 8, control file parallel write, 4, 0.11.
>
> Row 7 has the values: null, null, control file sequential read, 4, 0.11.
>
> Row 8 has the values: 14:18:00 (3.0 min), 10, control file sequential read, 6, 0.16.
>
> Row 9 has the values: null, null, control file parallel write, 3, 0.08.
>
> Row 10 has the values: null, null, SQL\*Net break/reset to client, 1, 0.03.
>
> Row 11 has the values: 14:21:00 (3.0 min), 14, CPU + Wait for CPU, 5, 0.14.
>
> Row 12 has the values: null, null, control file parallel write, 5, 0.14.
>
> Row 13 has the values: null, null, control file sequential read, 3, 0.08.
>
> Row 14 has the values: 14:24:00 (3.0 min), 275, CPU + Wait for CPU, 95, 2.60.
>
> Row 15 has the values: null, null, enq: TM - contention, 60, 1.64.
>
> Row 16 has the values: null, null, control file sequential read, 36, 0.99.
>
> Row 17 has the values: 14:27:00 (3.0 min), 703, enq: TM - contention, 187, 5.12.
>
> Row 18 has the values: null, null, CPU + Wait for CPU, 175, 4.79.
>
> Row 19 has the values: null, null, log file switch (checkpoint incomplete, 81, 2.22.
>
> Row 20 has the values: 14:30:00 (3.0 min), 737, enq: TM - contention, 210, 5.75.
>
> Row 21 has the values: null, null, CPU + Wait for CPU, 199, 5.45.
>
> Row 22 has the values: null, null, enq: TM - contention, 95, 2.60.
>
> Row 23 has the values: 14:33:00 (3.0 min), 713, enq: TM - contention, 181, 4.96.
>
> Row 24 has the values: null, null, CPU + Wait for CPU, 84, 4.82.
>
> Row 25 has the values: null, null, enq: TM - contention, 95, 2.30.
>
> Row 26 has the values: 14:36:00 (3.0 min), 740, enq: TM - contention, 222, 6.08.
>
> Row 27 has the values: null, null, CPU + Wait for CPU, 212, 5.81.
>
> Row 28 has the values: null, null, enq: TM - contention, 80, 2.19.
>
> Row 29 has the values: 14:39:00 (3.0 min), 437, enq: TM - contention, 126, 3.45.
>
> Row 30 has the values: null, null, CPU + Wait for CPU, 114, 3.12.
>
> Row 31 has the values: null, null, enq: TM - contention, 52, 1.42.
>
> End of description.


Each time slot contains session and wait event activity, as described in Table 8-1.

Table 8-1 Activity Over Time

| Column | Description |
| --- | --- |
| Slot Time (Duration) | Duration of the slot |
| Slot Count | Number of sampled sessions in the slot |
| Event | Top three wait events in the slot |
| Event Count | Number of ASH samples waiting for the wait event |
| % Event | Percentage of ASH samples waiting for wait events in the entire analysis period |

All inner slots are the same number of minutes each for easy comparison. The first and last slots, called outer slots, are odd-sized because they do not have a fixed slot time.

When comparing the inner slots, perform a skew analysis by identifying spikes. A spike in the Slot Count column indicates an increase in active sessions and a relative increase in database workload. A spike in the Event Count column indicates an increase in the number of sampled sessions waiting for an event. Typically, when the number of active session samples and the number of sessions associated with a wait event increase, the slot may be the cause of the transient performance problem.