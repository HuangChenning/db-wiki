---
title: "2 Day + Performance Tuning Guide"
book: "2 Day + Performance Tuning Guide"
doc_id: F32092-02
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tdppt/automatic-database-performance-monitoring.html
tags:
  - oracle
  - 21c
  - 2-day-performance-tuning-guide
---

Automatic Database Diagnostic Monitor (ADDM) automatically detects and reports performance problems with the database. The results are displayed as ADDM findings on the Database Home page in Oracle Enterprise Manager Cloud Control (Cloud Control). Reviewing the ADDM findings enables you to quickly identify the performance problems that require your attention. Before using another performance tuning method described in this guide, first review the results of the ADDM analysis.

Each ADDM finding provides a list of recommendations for reducing the impact of the performance problem. You should review ADDM findings and implement the recommendations every day as part of regular database maintenance. Even when the database is operating at an optimal performance level, you should continue to use ADDM to monitor database performance on an ongoing basis.

This chapter contains the following sections:

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA94245) for information about using the `DBMS_ADVISOR` package to diagnose and tune the database with the Automatic Database Diagnostic Monitor

### Overview of Automatic Database Diagnostic Monitor

ADDM is diagnostic software built into Oracle Database. ADDM examines and analyzes data captured in Automatic Workload Repository (AWR) to determine possible database performance problems. ADDM then does the following:

- Locates the root causes of the performance problems
- Provides recommendations for correcting them
- Quantifies the expected benefits
- Identifies areas where no action is necessary.

This section contains the following topics:

- ADDM Analysis
- ADDM Recommendations
- ADDM for Oracle Real Application Clusters
- ADDM for a Multitenant Environment

#### ADDM Analysis

An ADDM analysis is performed after each AWR snapshot (every hour by default), and the results are saved in the database. You can then view the results using Cloud Control.

The ADDM analysis is performed from the top down, first identifying symptoms and then refining the analysis to reach the root causes of performance problems. ADDM uses the DB time statistic to identify performance problems. Database time (DB) time is the cumulative time spent by the database in processing user requests, including both the wait time and CPU time of all user sessions that are not idle.

The goal of database performance tuning is to reduce the DB time of the system for a given workload. By reducing DB time, the database can support more user requests by using the same or fewer resources. ADDM reports system resources that are using a significant portion of DB time as problem areas and sorts them in descending order by the amount of related DB time spent.

See Also:

" [Time Model Statistics](oracle-database-performance-method.md) " for more information about the DB time statistic

#### ADDM Recommendations

In addition to diagnosing performance problems, ADDM recommends possible solutions. When appropriate, ADDM recommends multiple solutions from which you can choose. ADDM recommendations include the following:

- Hardware changes
	Adding CPUs or changing the I/O subsystem configuration
- Database configuration
	Changing initialization parameter settings
- Schema changes
	Hash partitioning a table or index, or using automatic segment space management (ASSM)
- Application changes
	Using the cache option for sequences or using bind variables
- Using other advisors
	Running SQL Tuning Advisor on high-load SQL statements or running the Segment Advisor on hot objects

ADDM benefits apply beyond production systems. Even on development and test systems, ADDM can provide an early warning of potential performance problems.

Performance tuning is an iterative process. Fixing one problem can cause a bottleneck to shift to another part of the system. Even with the benefit of the ADDM analysis, it can take multiple tuning cycles to reach a desirable level of performance.

#### ADDM for Oracle Real Application Clusters

In an Oracle Real Application Clusters (Oracle RAC) environment, you can use ADDM to analyze the throughput performance of a database cluster. ADDM for Oracle RAC considers DB time as the sum of database times for all database instances and reports findings that are significant at the cluster level. For example, the DB time of each cluster node may be insignificant when considered individually, but the aggregate DB time may be a significant problem for the cluster as a whole.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=RACAD-GUID-42E1B55A-4685-4CED-98CA-1BB576650D1A) for information about using ADDM for Oracle RAC

#### ADDM for a Multitenant Environment

Starting with Oracle Database 12c, ADDM is enabled by default in the root container of a multitenant container database (CDB). Starting with Oracle Database 19c, you can also use ADDM in a pluggable database (PDB).

Note:

A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.

To use ADDM in a PDB, you must enable automatic snapshots in the PDB by setting the `AWR_PDB_AUTOFLUSH_ENABLED` initialization parameter to `TRUE` and AWR snapshot interval greater than 0.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA-GUID-B4B0899D-90A3-4E19-8654-1D5C34A48FD5) for more information about using ADDM in a multitenant environment

### Configuring Automatic Database Diagnostic Monitor

#### Setting Initialization Parameters to Enable ADDM

Automatic database diagnostic monitoring is enabled by default and is controlled by the `CONTROL_MANAGEMENT_PACK_ACCESS` and the `STATISTICS_LEVEL` initialization parameters.

Set `CONTROL_MANAGEMENT_PACK_ACCESS` to `DIAGNOSTIC+TUNING` (default) or `DIAGNOSTIC` to enable automatic database diagnostic monitoring. Setting `CONTROL_MANAGEMENT_PACK_ACCESS` to `NONE` disables many Oracle Database features, including ADDM, and is strongly discouraged.

Set `STATISTICS_LEVEL` to `TYPICAL` (default) or `ALL` to enable automatic database diagnostic monitoring. Setting `STATISTICS_LEVEL` to `BASIC` disables many Oracle Database features, including ADDM, and is strongly discouraged.

To determine whether ADDM is enabled:

1. Access the Database Home page.
	See " [Accessing the Database Home Page](introduction.md) " for more information.
2. From the Administration menu, select Initialization Parameters.
	If the Database Login page appears, then log in as a user with administrator privileges. The Initialization Parameters page appears.
3. In the Name field, enter `statistics_level` and then click Go.
	The Initialization Parameters table shows the setting of this initialization parameter.
	![statistics_level](img/statistics_level.gif)

> The columns are: Name, Help, Revisions, Value, Comments, Type, Basic, Modified, Dynamic, Category.
>
> The row shows statistics\_level, \[Help\], String, \[Dynamic\], Diagnostics and Statistics.

4. Do one of the following:
	- If the Value list shows ALL or TYPICAL, then do nothing.
		- If the Value list shows BASIC, then select ALL or TYPICAL, and then click Apply.
5. In the Name field, enter `control_management_pack_access`, and then click Go.
	The table shows the setting of this initialization parameter.
6. Do one of the following:
	- If the Value column shows DIAGNOSTIC or DIAGNOSTIC+TUNING, then do nothing.
		- If the Value column shows NONE, then select DIAGNOSTIC or DIAGNOSTIC+TUNING and click Apply.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=REFRN10214) for information about the `STATISTICS_LEVEL` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=REFRN10296) for information about the `CONTROL_MANAGEMENT_PACK_ACCESS` initialization parameter

#### Setting the DBIO\_EXPECTED Parameter

ADDM analysis of I/O performance partially depends on a single argument, `DBIO_EXPECTED`, that describes the expected performance of the I/O subsystem. The value of `DBIO_EXPECTED` is the average time it takes to read a single database block, in microseconds. Oracle Database uses the default value of 10 milliseconds, which is an appropriate value for most hard drives. You can choose a different value based on the characteristics of your hardware.

To determine the correct setting for the `DBIO_EXPECTED` initialization parameter:

1. Measure the average read time of a single database block for your hardware.
	This measurement must be taken for random I/O, which includes seek time if you use standard hard drives. Typical values for hard drives are between 5000 and 20000 microseconds.
	See Also:
	[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA015) to learn how to assess the I/O capability of the storage subsystem
2. Set the value one time for all subsequent ADDM executions.
	For example, if the measured value is 8000 microseconds, then execute the following PL/SQL code as the `SYS` user:
	```
	EXECUTE DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER(
	                     'ADDM', 'DBIO_EXPECTED', 8000);
	```

#### Managing AWR Snapshots

By default, the Automatic Workload Repository (AWR) generates snapshots of performance data once every hour, and retains the statistics in the workload repository for 8 days. You can change the default values for both the snapshot interval and the retention period.

Oracle recommends that you adjust the AWR retention period to at least one month. You can also extend the period to one business cycle so you can compare data across time frames such as the close of the fiscal quarter. You can also create AWR baselines to retain snapshots indefinitely for important time periods.

The data in the snapshot interval is analyzed by ADDM. ADDM compares the differences between snapshots to determine which SQL statements to capture, based on the effect on the system load. The ADDM analysis shows the number of SQL statements that need to be captured over time.

This section contains the following topics:

- Creating Snapshots
- Modifying Snapshot Settings

##### Creating Snapshots

Manually creating snapshots is usually not necessary because AWR generates snapshots of the performance data once every hour by default. In some cases, however, it may be necessary to manually create snapshots to capture different durations of activity, such as when you want to compare performance data over a shorter period than the snapshot interval.

To create snapshots:

1. Access the Database Home page.
	See " [Accessing the Database Home Page](introduction.md) " for more information.
2. From the Performance menu, select AWR and then select AWR Administration.
	If the Database Login page appears, then log in as a user with administrator privileges. The Automatic Workload Repository page appears.
3. Under Manage Snapshots and Baselines, click the number next to Snapshots.
	The Snapshots page appears with a list of the most recent snapshots.
4. Click Create.
	The Confirmation page appears.
5. Click Yes.
	The Processing: Create Snapshot page is displayed while the snapshot is being taken.
	After the snapshot is taken, the Snapshots page reappears with a Confirmation message.
	The following screenshot of the list of snapshots shows that a snapshot was created at 9:24:25 a.m. The ID of the snapshot is 383.
	![snapshots](img/snapshots.gif)

> The screenshot shows the table of snapshots on the Snapshots page. In the top right corner of the screenshot is the Create button.
>
> In a horizontal row across the top of the table of screenshots are the following GUI elements: Delete button, Actions list (with Create SQL Tuning Set shown), Go button, page scrolling list (with 376-381 of 381 shown).
>
> Underneath the row of GUI elements is the table. The table contains the following columns: Select, ID, Capture Time, Collection Level, Within A Baseline. The values in the ID column are links. Each row of the Select column contains an option button.
>
> Six rows are shown. The values of row 1 are the following: (not selected), 378, Jan 12 2012 7:00:57 AM, TYPICAL, null.
>
> Each row increments the ID by 1, so row 2 is 379, row 3 is 380, and so on. Each snapshot occurs one-half hour after the previous snapshot, except for the last one, which occurs at 9:24:25 AM. The only row selected is the last one. For all of the rows the Collection Level is TYPICAL and the Within a Baseline value is null.
>
> End of description.


##### Modifying Snapshot Settings

### Reviewing the Automatic Database Diagnostic Monitor Analysis

By default, ADDM runs every hour to analyze snapshots taken by AWR during that period. If the database finds performance problems, then it displays the results of the analysis under Diagnostics in the Summary section on the Database Home page.

![diagnostic_sum](img/diagnostic_sum.gif)

> This screenshot shows the Diagnostics portion of the Summary section of the Database Home page.Two label-value pairs appear. The value for the ADDM Findings label is: 4. This value is a link. The values for the Incidents label are icon and value pairs. The four icon-value pairs are: Fatal icon 0, Critical icon 1, Warning icon 0, Escalated icon 0.
>
> End of description.


The ADDM Findings link shows how many ADDM findings were found in the most recent ADDM analysis.

To view ADDM findings:

1. Access the Database Home page.
	See " [Accessing the Database Home Page](introduction.md) " for more information.
2. From the Performance menu, select Advisors Home.
	If the Database Login page appears, then log in as a user with administrator privileges. The Advisor Central page appears.
3. In the Results section of Advisor Tasks, select the most recent ADDM result, and then click View Result.
	The Automatic Database Diagnostic Monitor (ADDM) page appears. The results of the ADDM run are displayed.
	Figure 3-1 The Automatic Database Diagnostic Monitor Page
	![Figure 3-1 The Automatic Database Diagnostic Monitor Page](img/addm_page.gif)

> This screenshot shows the Database Activity section of the Automatic Database Diagnostic Monitor (ADDM) page.
>
> In the top right corner of the screenshot are the following buttons: Run ADDM, Finding History.
>
> A stacked area chart is shown. The units of the x-axis are hours. The x-coordinates shown range from 4 p.m. on Dec 30 2011 to 2 a.m. on Dec 31 2011. The units of the y-axis are: active sessions. The y-coordinates shown range from 0.0 to 1.75. The following types of information are plotted in the chart: Wait, User I/O, CPU. The chart indicates that all activity spiked between 2:00 p.m. and 4:30 p.m. on December 30.
>
> This screenshot also shows the ADDM Performance Analysis section of the Automatic Database Diagnostic Monitor (ADDM) page.
>
> In the top right of the section are the following buttons: Filters, View Snapshots, View Report, JVM Diagnostics.
>
> 6 label-value pairs appear. The value for the Task Name label is: ADDM:644923168\_1\_1016 The value for the Task Owner label is: SYS. The value for the Average Active Sessions label is: 1.5. The value for the Period Start Time label is: Dec 30, 2011 2:30:04 PM. The value for the End Time label is: Dec 31, 2011 3:00:06 PM.
>
> Underneath this section is a table. The table contains the following columns: Impact (%), Finding, Occurrences (last 24 hrs ending with analysis period). The values in the Finding and Occurrences columns are links. The Impact (%) value is shown as a horizontal bar.
>
> 7 rows are shown in the table. The values of row 1 are: 100, Virtual Memory Paging, 3 0f 49. The values of row 2 are: 65.2, Top SQL Statements, 2 of 49. The values of row 3 are: 7.6, "Scheduler" Wait Class, 2 of 49. The values of row 4 are: 45.5, Shared Pool Latches, 2 of 49. The values of row 5 are: 3.6, "User I/O wait Class", 3 of 49. The values of row 6 are: 2.2, Soft Parse, 3 of 49. The values of row 7 are: 2.2, Hard Parse Due to Sharing Criteria, 3 0f 49.
>
> A collapsed navigation tree for Information Findings is shown.
>
> End of description.

	On the Automatic Database Diagnostic Monitor (ADDM) page, the Database Activity chart shows the database activity during the ADDM analysis period. Database activity types are defined in the legend based on their corresponding colors in the chart. Each icon below the chart represents a different ADDM task, which in turn corresponds to a pair of snapshots saved in AWR.
	In Figure 3-1, stacked area chart in the Database Activity section shows that the most database activity was between 2:00 p.m. to 4:30 p.m. on December 30. During that time, the activity was dominated by CPU and wait classes, with very little I/O happening.
	In the ADDM Performance Analysis section, ADDM findings are listed in descending order, from highest to least impact. The Informational Findings section lists areas that have no performance impact and are for information only.
	![information_findings](img/information_findings.gif)

> An expanded Informational Findings navigation tree is shown. The following wait classes were not consuming significant database time: Application, Commit, Configuration, Network. CPU was not a bottleneck for the instance. Also, session connect and disconnect calls were not consuming significant database time.
>
> End of description.

4. Optionally, click the Zoom icons to shorten or lengthen the analysis period displayed on the chart.
5. To view the ADDM findings in a report, click View Report.
	The View Report page appears.
	You can click Save to File to save the report for later access.

### Interpretation of Automatic Database Diagnostic Monitor Findings

The ADDM analysis results are represented as a set of findings. Each ADDM finding belongs to one of three types:

- Problem
	Findings that describe the root cause of a database performance issue
- Symptom
	Findings that contain information that often leads to one or more problem findings
- Information
	Findings that are used to report areas of the system that do not have a performance impact

Each problem finding is quantified with an estimate of the portion of DB time that resulted from the performance problem.

When a specific problem has multiple causes, ADDM may report multiple findings. In this case, the impacts of these multiple findings can contain the same portion of DB time. Because performance problems can overlap, summing the impacts of the reported findings can yield a number higher than 100% of DB time. For example, if a system performs many read I/O operations, ADDM may report a SQL statement responsible for 50% of DB time due to I/O activity as one finding, and an undersized buffer cache responsible for 75% of DB time as another finding.

A problem finding can be associated with a list of recommendations for reducing the impact of a performance problem. Each recommendation has a benefit that is an estimate of the portion of DB time that can be saved if the recommendation is implemented. When multiple recommendations are associated with an ADDM finding, the recommendations may contain alternatives for solving the same problem. In this case, the sum of the benefits may be higher than the impact of the finding. You do not need to apply all the recommendations to solve the same problem.

Recommendations are composed of actions and rationales. You must apply all the actions of a recommendation to gain its estimated benefit. The rationales explain why the set of actions are recommended, and provide additional information for implementing them. An ADDM action may present multiple solutions. If this is the case, then choose the easiest solution to implement.

### Implementing Automatic Database Diagnostic Monitor Recommendations

This section describes how to implement ADDM recommendations. ADDM findings are displayed in the Automatic Database Diagnostic Monitor (ADDM) page under ADDM Performance Analysis.

To implement ADDM recommendations:

1. Access the Database Home page.
	See " [Accessing the Database Home Page](introduction.md) " for more information.
2. From the Performance menu, select Advisors Home.
	If the Database Login page appears, then log in as a user with administrator privileges. The Advisor Central page appears.
3. In the Results section of Advisor Tasks, select the most recent ADDM result, then click View Result.
	The Automatic Database Diagnostic Monitor (ADDM) page appears.
4. In the Database Activity section, click the chart icon for the ADDM run to investigate.
	The data in the ADDM Performance Analysis section changes based on the ADDM run that you selected.
5. In the ADDM Performance Analysis table, click the ADDM finding that has the greatest impact.
	In the following screenshot of the ADDM Performance Analysis table, the finding with the greatest impact is Top SQL Statements.
	![perf_analysis](img/perf_analysis.gif)

> This screenshot contains a table. The table contains the following columns: Impact (%), Finding, Occurrences (last 24 hours). The values in the Finding and Occurrences columns are links. Values in the Impact column are shown as a horizontal bar and labeled with a number.
>
> In the ADDM Performance Analysis section, 4 ADDM Findings are listed.
>
> The first ADDM Finding shows that SQL statements are consuming significant database time. The impact of this finding is 83.7%.
>
> The second ADDM Finding shows that the "Scheduler" Wait Class was consuming significant database time. The impact of this finding is 23.4%.
>
> The third ADDM Finding shows that Log File Switches were consuming significant database time. The impact of this finding is 3.5%.
>
> The fourth ADDM Finding shows that an Undersize Buffer Cache was consuming significant database time. The impact of this finding was 2.1%.
>
> End of description.

	The Performance Finding Details page appears.
	In the following screen shot of the Performance Finding Details page, five recommendations are shown. The first is estimated to have a maximum benefit of up to 26.7% of DB time in the analysis period. The second recommendation is estimated to have a maximum benefit of up to 10.9% of DB time, the third also has a maximum of 10.9%, the fourth has a maximum of 9.9%, and the fifth has a maximum of 5%.
	![perf_finding_details](img/perf_finding_details.gif)

> This screenshot shows the top portion of the Performance Finding Details: Top SQL Statements page.
>
> In the upper right of the screenshot are the following buttons: Finding History.
>
> 6 label-value pairs appear. The value for the Finding label is: SQL statements consuming significant database time were found. These statements offer a good opportunity for performance improvement. The value for the Impact (Active Sessions) label is:.4. The value for the Percentage of Finding's Impact (%) label is: 69.3. The value is displayed as a horizontal bar. The value for the Period Start Time label is: Dec 30, 2011 3:30:31 PM. The value for the End Time label is: Dec 30, 2011 4:00:45 PM. The value for the Filtered label is: No. The Filters button appears next to this value.
>
> This screenshot shows the Recommendations section of the page. This section has the Schedule SQL Tuning Advisor button and a table.
>
> Above the table are the following options: Select All, Select None, Show All Details, Hide All Details.
>
> The table contains the following columns: Select, Details, Category, and Benefit (%). The value of the Select column is a check box. The value of the Details column is a collapsible navigation tree. The value of the Benefit column is a horizontal bar chart with an associated number.
>
> 5 rows are shown in the table. The values of row 1 are: not selected, Show, SQL Tuning, and 29.7. The values of row 2 are: selected, Show, SQL Tuning, and 10.9. The values of row 3 are: not selected, Show, SQL Tuning, and 10.9. The values of row 4 are: not selected, Show, SQL Tuning, and 9.9. The values of row 5 are: selected, Show, SQL Tuning, and 5.
>
> End of description.

6. Under Recommendations, click Show to review the recommendations and required actions for each recommendation.
	The Category column displays the category of the recommendation. The Benefit (%) column displays the estimated benefit of implementing the recommendation.
	Figure 3-2 shows the recommendations for the first item in the Recommendations table.
	Figure 3-2 Recommendations on the Performance Finding Details Page
	![Figure 3-2 Recommendations on the Performance Finding Details Page](img/addm_rec.gif)

> This screenshot shows the Recommendations section of the Performance Finding Details page.
>
> Underneath the section title is the following left-justified button: Schedule SQL Tuning Advisor.
>
> The following left-justified links are shown in a row: Select All, Select None, Show All Details, Hide All Details.
>
> Underneath the row of links is a table. The table contains the following columns: Select, Details, Category, and Benefit (%). Values in the Details column are displayed as a collapsible navigation tree. Values in the Benefit column are displayed as a horizontal bar chart with an associated number.
>
> 3 rows are shown in the table. The values of row 1 are: null, Hide, SQL Tuning, and 26.7. Under row 1 are 7 label-value pairs that show the actions to perform for the recommendation in row 1 and rationales for the actions. The first two labels are Action and the other five labels are Rationale. The value of the first action label is: Run SQL Tuning Advisor on the SELECT statement with the SQL\_ID "ddthrb7j9a63f". Additionally, investigate this statement for possible performance improvements. You can supplement the information given here with an ASH report for this SQL\_ID. Under that text are two buttons: Run Advisor Now, Filters. Below the buttons are two label-value pairs. The value for the SQL Text label is: SELECT E.LAST\_NAME, D.DEPARTMENT\_NAME FROM HR\_EMPLOYEES E, HR.DEPARTMENTS D WHER.... The value for the SQL\_ID label is: ddthrb7j9a63f.
>
> The value of the second Action label is: Use bigger fetch arrays while fetching results from the SELECT statement with SQL\_ID "ddthrb7j9a63f". After that sentence are two label-value pairs. The value for the SQL Text label is: SELECT E.LAST\_NAME, D.DEPARTMENT\_NAME FROM HR\_EMPLOYEES E, HR.DEPARTMENTS D WHER.... The value for the SQL\_ID label is: ddthrb7j9a63f.
>
> The value of the first rationale is: The SQL spent 70% of its database time on CPU, I/O and Cluster waits. This part of the database time may be improved by the SQL Tuning Advisor. Look at data given below and an ASH report for further performance improvements. The value of the second rationale is: Database time for this SQL was divided as follows: 100% for SQL execution, 0% for parsing, 0% for PL/SQL execution and 0% for Java execution. The value of the third rationale is: SQL statement with SQL\_ID "ddthrb7j9a63f" was executed 130081 times and had an average elapsed time of 0.00098 seconds. The value of the fourth rationale is: Waiting for event "buffer busy waits" in wait class "Concurrency" accounted for 18% of the database time spent in processing the SQL statement with SQL\_ID "ddthrb7j9a63f". The value of the fifth rationale is: Top level calls to execute the PL/SQL statement with SQL\_ID "3575p6hzg9gat" are responsible for 100% of the database time spent on the SELECT statement with SQL\_ID "ddthrb7j9a63f". After the last rationale are two label-value pairs. The value for the SQL Text label is: DECLARE n number; v\_employees\_last name.... The value for the SQL\_ID label is: 3575p6hzg9gat.
>
> The values of row 2 are: null (a checked box is shown), Show, SQL Tuning, and 10.9. The values of row 3 are: null, Show, SQL Tuning, and 10.9.
>
> End of description.

7. If additional information is available about why the set of actions was recommended, then click Additional Information, or review the content displayed under Additional Information.
	For example, the following screenshot shows an Undersized Buffer Cache finding that contains additional information that indicates the recommended value of the `DB_CACHE_SIZE` initialization parameter.
	![addm_addit_info](img/addm_addit_info.gif)

> This screenshot shows the Performance Finding Details: Undersized Buffer Cache page.
>
> Under the page title are the following label-value pairs:
>
> - Finding: he buffer cache was undersized causing significant additional read I/O.
> 	Associated with the finding is the Finding History button.
> - Impact (Active Sessions):.01
> - Impact (%): 2.1
> - Period Start Time: Jan 20, 2012 4:00:40 PM PST
> - Period Duration (minutes): 29.5
> - Filtered: No
> 	Associated with the filtered value is the Filters button.
>
> In the Recommendations section are the links Show All Details and Hide All Details. A table contains the following columns: Details, Category, and Benefit (%).
>
> Underneath the row of links is a table. The table contains the following columns: Details, Category, and Benefit (%). Values in the Details column are displayed as a collapsible navigation tree. Values in the Benefit column are displayed as a horizontal bar chart with an associated number.
>
> The table has one row. The values of row are: Hide, DB Configuration, and 2.1. Below that row is the following additional information about the finding: Action, "Increase the buffer cache size by setting the value of parameter DB\_CACHE\_SIZE to 160M." After the text are the following buttons: Implement, and Filters.
>
> The Additional Information section contains the following message: The value of parameter "db\_cache\_size" was "96 M" during the analysis period.
>
> In the Findings Path section, the Expand All and Collapse All links appear in the upper left. The table has the following columns: Findings, Impact (%), and Additional Information. The first row has the values: "The buffer cache was undersized causing significant additional read I/O," 2.1 (shown as a bar chart), and an Additional Information link. The second row has the values: "Wait class 'User I/O' was consuming significant database time," 2.1 (shown as a bar chart with an associated number), and null.
>
> End of description.

8. To view the history of a finding, click Finding History.
	The Finding History page appears. The following screenshot shows the Finding History page for the top SQL statements.
	![finding_history](img/finding_history.gif)

> This screenshot shows the top portion of the Finding History: Top SQL by DB Time page.
>
> In the top left corner of the screenshot are the following elements: View list, calendar icon, Go button, and Filters button. The value shown in the View list is Jan 19, 2012.
>
> A stacked area chart is shown. The units of the x-axis are hours. The x-coordinates shown range from 7:00 p.m. on January 19, 2012 to 7 p.m. on January 20. The units of the y-axis are: active sessions. The y-coordinates shown range from 0.0 to 2.0. The following types of information are plotted in the chart: Other Load on System, and Impact of Finding. The session activity spiked between 2 p.m. and 5 p.m. on January 20. The time from 1 p.m. to 4 p.m. is included in a rectangle.
>
> Underneath the chart is a slider.
>
> This screenshot includes a Detail for Selected 3 Hour Interval section.
>
> Underneath the section title are the following left-justified links: Show All Details, and Hide All Details.
>
> Underneath the links is a table. The table contains the following columns: Details, Finding Details, Impact (Active Sessions), and Start Date. Values in the Details column are displayed as a navigation tree. Values in the Finding Details column are displayed as links.
>
> Five rows are shown in the table. The values of row 1 are: Show, ADDM:399937146\_1\_99, 0.5, and Jan 20, 2009 2:30:56 PM PST. Each subsequent row shows the same Finding Details value, except with the last two digits increased by one (100, 101, etc.). The Impact values ranged from.21 to 1.87.
>
> End of description.

	The Finding History page shows how often a particular finding has occurred in a selected 3-hour interval. You can use this information to determine whether the finding was a transient or a persistent problem in the system. Based on this information, you can determine whether the actions associated with the finding should be implemented.
	The Active Sessions stacked area chart shows the impact of the finding and of the other loads on the system. You can change the display as follows:
	1. To move the 3-hour interval, click and drag the shaded box in the Active Sessions chart.
		2. To change dates, enter the desired date in the View field, and then click Go.
		3. To view details about a finding, under Detail for Selected 3 Hour Interval, click the link in the Finding Details column to display the Performance Finding Details page for the corresponding ADDM finding.
9. Optionally, create a filter to suppress known findings that have been tuned or cannot be tuned further. To create filters for a selected ADDM finding:
	1. Click Filters.
		The Filters for Finding page appears.
		2. Click Create.
		The Create Filter for Finding page appears.
		3. In the Name field, enter a name for the ADDM filter.
		4. In the Active Sessions field, specify the filter criteria in terms of the number of active sessions.
		The database filters the ADDM finding for future ADDM runs if the number of active sessions for the finding is less than the specified filter criteria.
		5. In the % Active Sessions field, specify the filter criteria in terms of percentage of active sessions.
		The database filters the ADDM finding for future ADDM runs if the number of active sessions for the finding is less than the specified filter criteria.
		6. Click OK.
10. Perform the required action of a chosen recommendation.
	Depending on the type of action you choose to perform, various options may be available, such as Implement or Run Advisor Now. These options enable you to implement the recommendation immediately with a single mouse click.
	In the example shown in Figure 3-2, the simplest solution is to click Run Advisor Now to immediately run a SQL Tuning Advisor task on the SQL statement.
	See Also:
	- " [Tuning SQL Statements](tuning-sql-statements.md) "

### Viewing Snapshot Statistics

You can view the data contained in snapshots taken by AWR using Cloud Control. Typically, it is not necessary to review snapshot data because it primarily contains raw statistics. Instead, rely on ADDM, which analyzes statistics to identify performance problems. Snapshot statistics are intended primarily for advanced users, such as DBAs accustomed to using Statspack for performance analysis.

To view snapshot statistics:

1. Access the Database Home page.
	See " [Accessing the Database Home Page](introduction.md) " for more information.
2. From the Performance menu, select AWR and then select AWR Administration.
	If the Database Login page appears, then log in as a user with administrator privileges. The Performance page appears.
3. Under Manage Snapshots and Baselines, click the number next to Snapshots.
	The Snapshots page appears with a list of the most recent snapshots.
4. To view the statistics gathered in a snapshot, click the ID link of the snapshot you want to view.
	The Snapshot Details appears, showing the Details subpage.
	The following screenshot of a Details subpage shows statistics gathered from the previous snapshot (snapshot 386) to the selected snapshot (snapshot 387).
	![snapshot_det](img/snapshot_det.gif)

> This screenshot shows the Details subpage of the Snapshot Details page.
>
> At the top of the subpage are four label-value pairs. The labels and their values are the following:
>
> - Beginning Snapshot ID: 386
> - Beginning Snapshot Capture: Jan 12, 2012 11:00:49 AM
> - Ending Snapshot ID: 387
> - Ending Snapshot Capture: Jan 12, 2012 11:30:56 AM
>
> Below the label-value pairs is a table. The table contains the following columns: Name, Value, Per Second, and Per Transaction.
>
> 24 rows are shown in the table. The values of row 1 are: DB cpu (seconds), 0.00, 0,00, and 0.00. The values of row 2 are: DB time (seconds), 64.25,.04, and 3.78. The remaining rows contain statistics for other activities.
>
> End of description.

5. To view a Workload Repository report of the statistics, click Report.
	The Workload Repository report appears.
6. Optionally, click Save to File to save the report for later access.

See Also:

- " [Resolving Performance Degradation Over Time](resolving-performance-degradation-over-time.md) "