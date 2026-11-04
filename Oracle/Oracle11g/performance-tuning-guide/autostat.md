---
title: Automatic Performance Statistics
book: Performance Tuning Guide
doc_id: E41573-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm
tags:
  - oracle
  - 11g
  - performance-tuning-guide
---

## 5 Automatic Performance Statistics

This chapter discusses the gathering of performance statistics. This chapter contains the following topics:

## 5.1 Overview of Data Gathering

To effectively diagnose performance problems, statistics must be available. Oracle Database generates many types of cumulative statistics for the system, sessions, and individual SQL statements. Oracle Database also tracks cumulative statistics on segments and services. When analyzing a performance problem in any of these scopes, you typically look at the change in statistics (delta value) over the period you are interested in. Specifically, you look at the difference between the cumulative value of a statistic at the start of the period and the cumulative value at the end.

Cumulative values for statistics are generally available through dynamic performance views, such as the `V$SESSTAT` and `V$SYSSTAT` views. Note that the cumulative values in dynamic views are reset when the database instance is shutdown. The Automatic Workload Repository (AWR) automatically persists the cumulative and delta values for most of the statistics at all levels except the session level. This process is repeated on a regular time period and the result is called an AWR snapshot. The delta values captured by the snapshot represent the changes for each statistic over the time period. See "Overview of the Automatic Workload Repository".

A metric is another type of statistic collected by Oracle Database. A metric is defined as the rate of change in some cumulative statistic. That rate can be measured against a variety of units, including time, transactions, or database calls. For example, the number database calls per second is a metric. Metric values are exposed in some `V$` views, where the values are the average over a fairly small time interval, typically 60 seconds. A history of recent metric values is available through `V$` views, and some data is also persisted by AWR snapshots.

A third type of statistical data collected by Oracle is sampled data. The active session history (ASH) sampler performs the sampling. ASH samples the current state of all active sessions. The database collects this data into memory, where you can access it with a `V$` view. AWR snapshot processing also writes it to persistent storage. See "Active Session History".

A powerful tool for diagnosing performance problems is the use of statistical baselines. A statistical baseline is collection of statistic rates usually taken over time period where the system is performing well at peak load. Comparing statistics captured during a period of bad performance to a baseline helps discover specific statistics that have increased significantly and could be the cause of the problem.

AWR supports the capture of baseline data by enabling you to specify and preserve a pair or range of AWR snapshots as a baseline. Carefully consider the time period you choose as a baseline; the baseline should be a good representation of the peak load on the system. In the future, you can compare these baselines with snapshots captured during periods of poor performance.

Oracle Enterprise Manager is the recommended tool for viewing both real time data in the dynamic performance views and historical data from the AWR history tables. Enterprise Manager can also be used to capture operating system and network statistical data that can be correlated with AWR data. For more information, see [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_realtime.htm#TDPPT033).

This section covers the following topics:

- Database Statistics
- Operating System Statistics
- Interpreting Statistics

### 5.1.1 Database Statistics

Database statistics provide information on the type of load on the database and the internal and external resources used by the database. This section describes some of the more important statistics.

#### 5.1.1.1 Wait Events

Wait events are statistics that are incremented by a server process or thread to indicate that it had to wait for an event to complete before being able to continue processing. Wait event data reveals various symptoms of problems that might be impacting performance, such as latch contention, buffer contention, and I/O contention.

To enable easier high-level analysis of the wait events, events are grouped into classes. The classes include: Administrative, Application, Cluster, Commit, Concurrency, Configuration, Idle, Network, Other, Scheduler, System I/O, and User I/O.

The wait classes are based on a common solution that usually applies to fixing a problem with the wait event. For example, exclusive TX locks are generally an application level issue and HW locks are generally a configuration issue.

The following list includes common examples of the waits in some of the classes:

- Application: locks waits caused by row level locking or explicit lock commands
- Commit: waits for redo log write confirmation after a commit
- Idle: wait events that signify the session is inactive, such as `SQL*Net` `message` `from` `client`
- Network: waits for data to be sent over the network
- User I/O: wait for blocks to be read off a disk

Wait event statistics for an instance include statistics for both background and foreground processes. Because you would typically focus your effort in tuning foreground activities, overall instance activity is broken down into foreground and background statistics in the relevant `V$` views to facilitate tuning.

The `V$SYSTEM_EVENT` view shows wait event statistics for the foreground activities of an instance and the wait event statistics for the instance. The `V$SYSTEM_WAIT_CLASS` view shows these foreground and wait event instance statistics after aggregating to wait classes. `V$SESSION_EVENT` and `V$SESSION_WAIT_CLASS` show wait event and wait class statistics at the session level.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/waitevents.htm#REFRN101) for more information about Oracle wait events

#### 5.1.1.2 Time Model Statistics

When tuning an Oracle database, each component has its own set of statistics. To look at the system as a whole, it is necessary to have a common scale for comparisons. For this reason, most Oracle Database advisories and reports describe statistics in terms of time. In addition, the `V$SESS_TIME_MODEL` and `V$SYS_TIME_MODEL` views provide time model statistics. Using the common time instrumentation helps to identify quantitative effects on the database operations.

The most important of the time model statistics is `DB` `time`. This statistics represents the total time spent in database calls and is an indicator of the total instance workload. It is calculated by aggregating the CPU and wait times of all sessions not waiting on idle wait events (non-idle user sessions).

`DB` `time` is measured cumulatively from the time of instance startup. Because `DB` `time` it is calculated by combining the times from all non-idle user sessions, it is possible that the `DB` `time` can exceed the actual time elapsed after the instance started. For example, an instance that has been running for 30 minutes could have four active user sessions whose cumulative `DB` `time` is approximately 120 minutes.

The objective for tuning an Oracle system could be stated as reducing the time that users spend in performing some action on the database, or simply reducing `DB` `time`. Other time model statistics provide quantitative effects (in time) on specific actions, such as logon operations and hard and soft parses.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3015.htm#REFRN30340) to learn about the `V$SESS_TIME_MODEL` and `V$SYS_TIME_MODEL` views

#### 5.1.1.3 Active Session History

The `V$ACTIVE_SESSION_HISTORY` view provides sampled session activity in the instance. Active sessions are sampled every second and are stored in a circular buffer in SGA. Any session that is connected to the database and is waiting for an event that does not belong to the Idle wait class is considered as an active session. This includes any session that was on the CPU at the time of sampling.

Each session sample is a set of rows and the `V$ACTIVE_SESSION_HISTORY` view returns one row for each active session per sample, returning the latest session sample rows first. Because the active session samples are stored in a circular buffer in SGA, the greater the system activity, the smaller the number of seconds of session activity that can be stored in the circular buffer. This means that the duration for which a session sample appears in the `V$` view, or the number of seconds of session activity that is displayed in the `V$` view, is completely dependent on the database activity.

As part of the AWR snapshots, the content of `V$ACTIVE_SESSION_HISTORY` is also flushed to disk. Because the content of this `V$` view can get quite large during heavy system activity, only a portion of the session samples is written to disk.

By capturing only active sessions, a manageable set of data is represented with the size being directly related to the work being performed rather than the number of sessions allowed on the system. Using ASH enables you to examine and perform detailed analysis on both current data in the `V$ACTIVE_SESSION_HISTORY` view and historical data in the `DBA_HIST_ACTIVE_SESS_HISTORY` view, often avoiding the need to replay the workload to gather additional performance tracing information. ASH also contains execution plan information for each captured SQL statement. You can use this information to identify which part of SQL execution contributed most to the SQL elapsed time. The data present in ASH can be rolled up on various dimensions that it captures, including the following:

- SQL identifier of SQL statement
- SQL plan identifier and hash value of the SQL plan used to execute the SQL statement
- SQL execution plan information
- Object number, file number, and block number
- Wait event identifier and parameters
- Session identifier and session serial number
- Module and action name
- Client identifier of the session
- Service hash identifier
- Consumer group identifier

You can gather ASH information over a specified duration into a report. For more information, see "Generating Active Session History Reports".

Active session history sampling is also available for Active Data Guard physical standby instances and Oracle Automatic Storage Management (Oracle ASM) instances. On these instances, the current session activity is collected and displayed in the `V$ACTIVE_SESSION_HISTORY` view, but not written to disk.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1007.htm#REFRN30299) for more information about the `V$ACTIVE_SESSION_HISTORY` view
- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/manageability.htm#HAOVW197) for more information about using ASH in an Active Data Guard physical standby environment

#### 5.1.1.4 System and Session Statistics

A large number of cumulative database statistics are available on a system and session level through the `V$SYSSTAT` and `V$SESSTAT` views.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) to learn about the `V$SYSSTAT` and `V$SESSTAT` views

### 5.1.2 Operating System Statistics

Operating system statistics provide information on the usage and performance of the main hardware components of the system, and the performance of the operating system itself. This information is crucial for detecting potential resource exhaustion, such as CPU cycles and physical memory, and for detecting bad performance of peripherals, such as disk drives.

Operating system statistics are an indication of how the hardware and operating system are working. Many system analysts react to a hardware resource shortage by installing more hardware. This is a reactionary response to a series of symptoms shown in the operating system statistics. It is best to consider operating system statistics as a diagnostic tool, similar to the way doctors use body temperature, pulse rate, and patient pain when making a diagnosis. To help identify bottlenecks, gather operating system statistics for all servers in the system under performance analysis.

Operating system statistics include the following:

- CPU Statistics
- Virtual Memory Statistics
- Disk I/O Statistics
- Network Statistics

See Also:

"Operating System Data Gathering Tools" for information about tools for gathering operating statistics

#### 5.1.2.1 CPU Statistics

CPU utilization is the most important operating system statistic in the tuning process. Get CPU utilization for the entire system and for each individual CPU on multi-processor environments. Utilization for each CPU can detect single-threading and scalability issues.

Most operating systems report CPU usage as time spent in user space or mode and time spent in kernel space or mode. These additional statistics allow better analysis of what is actually being executed on the CPU.

On a system running Oracle Database, where only one application is typically running, the system runs database activity in user space. Activities required to service database requests (such as scheduling, synchronization, I/O, memory management, and process/thread creation and tear down) run in kernel mode. In a system where CPU is fully utilized, a healthy Oracle database runs between 65% and 95% in user space.

The `V$OSSTAT` view captures machine-level information in the database, making it easier for you to determine if hardware-level resource issues exist. The `V$SYSMETRIC_HISTORY` view shows a one-hour history of the Host CPU Utilization metric, a representation of percentage of CPU usage at each one-minute interval. The `V$SYS_TIME_MODEL` view supplies statistics on the CPU usage by the Oracle database. Using both sets of statistics enable you to determine whether the Oracle database or other system activity is the cause of the CPU problems.

#### 5.1.2.2 Virtual Memory Statistics

Virtual memory statistics should mainly be used as a check to validate that there is very little paging or swapping activity on the system. System performance degrades rapidly and unpredictably when paging or swapping occurs.

Individual process memory statistics can detect memory leaks due to a programming failure to deallocate memory taken from the process heap. These statistics are necessary to validate that memory usage does not increase after the system has reached a steady state after startup. This problem is particularly acute on shared server applications on middle tier computers where session state may persist across user interactions, and on completion state information that is not fully deallocated.

#### 5.1.2.3 Disk I/O Statistics

Because the database resides on a set of disks, the performance of the I/O subsystem is very important to the performance of the database. Most operating systems provide extensive statistics on disk performance. The most important disk statistics are the current response time and the length of the disk queues. These statistics show if the disk is performing optimally or if the disk is being overworked.

Measure the normal performance of the I/O system; typical values for a single block read range from 5 to 20 milliseconds, depending on the hardware used. If the hardware shows response times much higher than the normal performance value, then it is performing badly or is overworked. This is your bottleneck. If disk queues start to exceed two, then the disk is a potential bottleneck of the system.

Oracle Database also maintains a consistent set of I/O statistics for the I/O calls it issues. These statistics are captured for both single and multi block read and write operations in the following dimensions:

- Consumer group
	When Oracle Database Resource Manager is enabled, the `V$IOSTAT_CONSUMER_GROUP` view captures I/O statistics for all consumer groups that are part of the currently enabled resource plan. The database samples cumulative statistics every hour and stores them as historical statistics in the AWR.
- Database file
	I/O statistics of database files that are or have been accessed are captured in the `V$IOSTAT_FILE` view.
- Database function
	I/O statistics for database functions (such as the LGWR and DBWR) are captured in the `V$IOSTAT_FUNCTION` view.

See Also:

["Identifying I/O Problems Using V$ Views"](instance_tune.md) to learn how to use views in Oracle Database to identify I/O problems

#### 5.1.2.4 Network Statistics

You can use network statistics in much the same way as disk statistics to determine if a network or network interface is overloaded or not performing optimally. In today's networked applications, network latency can be a large portion of the actual user response time. For this reason, these statistics are a crucial debugging tool.

Oracle Database maintains a set of network I/O statistics in the `V$IOSTAT_NETWORK` view.

See Also:

["Identifying Network Issues"](instance_tune.md) to learn how to use the `V$IOSTAT_NETWORK` view to identify network issues

#### 5.1.2.5 Operating System Data Gathering Tools

Table 5-1 shows the various tools for gathering operating statistics on UNIX. For Windows, use the Performance Monitor tool.

Table 5-1 UNIX Tools for Operating Statistics

| Component | UNIX Tool |
| --- | --- |
| CPU | sar, vmstat, mpstat, iostat |
| Memory | sar, vmstat |
| Disk | sar, iostat |
| Network | netstat |

### 5.1.3 Interpreting Statistics

When initially examining performance data, you can formulate potential theories by examining your statistics. One way to ensure that your interpretation of the statistics is correct is to perform cross-checks with other data. This establishes whether a statistic or event is really of interest. Also, because foreground activities are tunable, it is better to first analyze the statistics from foreground activities before analyzing the statistics from background activities.

Some pitfalls are discussed in the following sections:

- Hit ratios
	When tuning, it is common to compute a ratio that helps determine whether there is a problem. Such ratios include the buffer cache hit ratio, the soft-parse ratio, and the latch hit ratio. Do not use these ratios as definitive identifiers of whether a performance bottleneck exists. Rather, use them as indicators. To identify whether a bottleneck exists, examine other related evidence. See ["Calculating the Buffer Cache Hit Ratio"](memory.md).
- Wait events with timed statistics
	Setting `TIMED_STATISTICS` to `true` at the instance level directs the database to gather wait time for events, in addition to available wait counts. This data is useful for comparing the total wait time for an event to the total elapsed time between the data collections. For example, if the wait event accounts for only 30 seconds out of a 2-hour period, then little is to be gained by investigating this event, although it may be the highest ranked wait event when ordered by time waited. However, if the event accounts for 30 minutes of a 45-minute period, then the event is worth investigating. See ["Wait Events"](instance_tune.md).
	Note:
	Timed statistics are automatically collected for the database if the initialization parameter `STATISTICS_LEVEL` is set to `TYPICAL` or `ALL`. If `STATISTICS_LEVEL` is set to `BASIC`, then you must set `TIMED_STATISTICS` to `TRUE` to enable collection of timed statistics. Note that setting `STATISTICS_LEVEL` to `BASIC` disables many automatic features and is not recommended.
	If you explicitly set `DB_CACHE_ADVICE`, `TIMED_STATISTICS`, or `TIMED_OS_STATISTICS`, either in the initialization parameter file or by using `ALTER_SYSTEM` or `ALTER` `SESSION`, then the explicitly set value overrides the value derived from `STATISTICS_LEVEL`.
- Comparing Oracle Database statistics with other factors
	When looking at statistics, it is important to consider other factors that influence whether the statistic is of value. Such factors include the user load and the hardware capability. Even an event that had a wait of 30 minutes in a 45-minute period might not be indicative of a problem if you discover that there were 2000 users on the system, and the host hardware was a 64-node computer.
- Wait events without timed statistics
	If `TIMED_STATISTICS` is false, then the amount of time waited for an event is not available. Therefore, it is only possible to order wait events by the number of times each event was waited for. Although the events with the largest number of waits might indicate the potential bottleneck, they might not be the main bottleneck. This can happen when an event is waited for a large number of times, but the total time waited for that event is small. The converse is also true: an event with fewer waits might be a problem if the wait time is a significant proportion of the total wait time. Without having the wait times to use for comparison, it is difficult to determine whether a wait event is really of interest.
- Idle wait events
	Oracle Database uses some wait events to indicate if the Oracle server process is idle. Typically, these events are of no value when investigating performance problems, and they should be ignored when examining the wait events. See ["Idle Wait Events"](instance_tune.md).
- Computed statistics
	When interpreting computed statistics (such as rates, statistics normalized over transactions, or ratios), it is important to cross-verify the computed statistic with the actual statistic counts. This confirms whether the derived rates are really of interest: small statistic counts usually can discount an unusual ratio. For example, on initial examination, a soft-parse ratio of 50% generally indicates a potential tuning area. If, however, there was only one hard parse and one soft parse during the data collection interval, then the soft-parse ratio would be 50%, even though the statistic counts show this is not an area of concern. In this case, the ratio is not of interest due to the low raw statistic counts.
	See Also:
	- ["Setting the Level of Statistics Collection"](instance_tune.md) to learn about the `STATISTICS_LEVEL` settings
	- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams254.htm#REFRN10214) for information about the `STATISTICS_LEVEL` initialization parameter

## 5.2 Overview of the Automatic Workload Repository

The Automatic Workload Repository (AWR) collects, processes, and maintains performance statistics for problem detection and self-tuning purposes. This data is both in memory and stored in the database. The gathered data can be displayed in both reports and views.

The statistics collected and processed by AWR include:

- Object statistics that determine both access and usage statistics of database segments
- Time model statistics based on time usage for activities, displayed in the `V$SYS_TIME_MODEL` and `V$SESS_TIME_MODEL` views
- Some of the system and session statistics collected in the `V$SYSSTAT` and `V$SESSTAT` views
- SQL statements that are producing the highest load on the system, based on criteria such as elapsed time and CPU time
- ASH statistics, representing the history of recent sessions activity

Gathering database statistics using the AWR is enabled by default and is controlled by the `STATISTICS_LEVEL` initialization parameter. The `STATISTICS_LEVEL` parameter should be set to the `TYPICAL` or `ALL` to enable statistics gathering by the AWR. The default setting is `TYPICAL`. Setting `STATISTICS_LEVEL` to `BASIC` disables many Oracle Database features, including the AWR, and is not recommended. If `STATISTICS_LEVEL` is set to `BASIC`, you can still manually capture AWR statistics using the `DBMS_WORKLOAD_REPOSITORY` package. However, because in-memory collection of many system statistics—such as segments statistics and memory advisor information—will be disabled, the statistics captured in these snapshots may not be complete. For information about the `STATISTICS_LEVEL` initialization parameter, see [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams254.htm#REFRN10214).

### 5.2.1 Snapshots

Snapshots are sets of historical data for specific time periods that are used for performance comparisons by ADDM. By default, Oracle Database automatically generates snapshots of the performance data once every hour and retains the statistics in the workload repository for 8 days. You can also manually create snapshots, but this is usually not necessary. The data in the snapshot interval is then analyzed by the Automatic Database Diagnostic Monitor (ADDM). For information about ADDM, see ["Overview of the Automatic Database Diagnostic Monitor"](diag.md).

AWR compares the difference between snapshots to determine which SQL statements to capture based on the effect on the system load. This reduces the number of SQL statements that must be captured over time.

For information about managing snapshots, see "Managing Snapshots".

### 5.2.2 Baselines

A baseline contains performance data from a specific time period that is preserved for comparison with other similar workload periods when performance problems occur. The snapshots contained in a baseline are excluded from the automatic AWR purging process and are retained indefinitely.

There are several types of available baselines in Oracle Database:

- Fixed Baselines
- Moving Window Baseline
- Baseline Templates

#### 5.2.2.1 Fixed Baselines

A fixed baseline corresponds to a fixed, contiguous time period in the past that you specify. Before creating a fixed baseline, carefully consider the time period you choose as a baseline, because the baseline should represent the system operating at an optimal level. In the future, you can compare the baseline with other baselines or snapshots captured during periods of poor performance to analyze performance degradation over time.

See Also:

"Managing Baselines" for information about managing fixed baselines

#### 5.2.2.2 Moving Window Baseline

A moving window baseline corresponds to all AWR data that exists within the AWR retention period. This is useful when using adaptive thresholds because the database can use AWR data in the entire AWR retention period to compute metric threshold values.

Oracle Database automatically maintains a system-defined moving window baseline. The default window size for the system-defined moving window baseline is the current AWR retention period, which by default is 8 days. If you are planning to use adaptive thresholds, consider using a larger moving window—such as 30 days—to accurately compute threshold values. You can resize the moving window baseline by changing the number of days in the moving window to a value that is equal to or less than the number of days in the AWR retention period. Therefore, to increase the size of a moving window, you must first increase the AWR retention period accordingly.

See Also:

"Modifying the Window Size of the Default Moving Window Baseline" for information about resizing the moving window baseline

#### 5.2.2.3 Baseline Templates

You can also create baselines for a contiguous time period in the future using baseline templates. There are two types of baseline templates: single and repeating.

You can use a single baseline template to create a baseline for a single contiguous time period in the future. This technique is useful if you know beforehand of a time period that you intend to capture in the future. For example, you may want to capture the AWR data during a system test that is scheduled for the upcoming weekend. In this case, you can create a single baseline template to automatically capture the time period when the test occurs.

You can use a repeating baseline template to create and drop baselines based on a repeating time schedule. This is useful if you want Oracle Database to automatically capture a contiguous time period on an ongoing basis. For example, you may want to capture the AWR data during every Monday morning for a month. In this case, you can create a repeating baseline template to automatically create baselines on a repeating schedule for every Monday, and automatically remove older baselines after a specified expiration interval, such as one month.

See Also:

"Managing Baseline Templates" for information about managing baseline templates

### 5.2.3 Adaptive Thresholds

Adaptive thresholds enable you to monitor and detect performance issues while minimizing administrative overhead. Adaptive thresholds can automatically set warning and critical alert thresholds for some system metrics using statistics derived from metric values captured in the moving window baseline. The statistics for these thresholds are recomputed weekly and might result in new thresholds as system performance evolves over time. In addition to recalculating thresholds weekly, adaptive thresholds might compute different thresholds values for different times of the day or week based on periodic workload patterns.

For example, many databases support an online transaction processing (OLTP) workload during the day and batch processing at night. The performance metric for response time per transaction can be useful for detecting degradation in OLTP performance during the day. However, a useful OLTP threshold value is almost certainly too low for batch workloads, where long-running transactions might be common. As a result, threshold values appropriate to OLTP might trigger frequent false performance alerts during batch processing. Adaptive thresholds can detect such a workload pattern and automatically set different threshold values for the daytime and nighttime.

Note:

In Oracle Database 11g Release 2 (11.2), Oracle Database automatically determines the appropriate time groupings for a database. However, before Oracle Database 11g Release 2 (11.2), time groupings were specified manually by the database administrator.

There are two types of adaptive thresholds:

- Percentage of maximum: The threshold value is computed as a percentage multiple of the maximum value observed for the data in the moving window baseline.
- Significance level: The threshold value is set to a statistical percentile that represents how unusual it is to observe values above the threshold value based the data in the moving window baseline. Specify one of the following percentiles:
	- High (.95): Only 5 in 100 observations are expected to exceed this value.
		- Very High (.99): Only 1 in 100 observations are expected to exceed this value.
		- Severe (.999): Only 1 in 1,000 observations are expected to exceed this value.
		- Extreme (.9999): Only 1 in 10,000 observations are expected to exceed this value.
	Note:
	When you specify Severe (.999) or Extreme (.9999), Oracle Database performs an internal calculation to set the threshold value. In some cases, Oracle Database cannot establish the threshold value at these levels using the data in the baseline, and the significance level threshold is not set.
	If you are not receiving alerts as expected, and you specified a Severe (.999) or Extreme (.9999) significance level threshold, then you can try setting the significance level threshold to a lower value, such as Very High (.99) or High (.95). Alternatively, you can set a percentage of maximum threshold instead of a significance level threshold. If you change the threshold and find that you are receiving too many alerts, then you can try increasing the number of occurrences to cause an alert.

Percentage of maximum thresholds are most useful when a system is sized for peak workloads, and you want to be alerted when the current workload volume is approaching or exceeding previous high values. Metrics that have an unknown but definite limiting value are good candidates for these settings. For example, the redo generated per second metric is typically a good candidate for a percentage of maximum threshold.

Significance level thresholds are most useful for metrics that should exhibit statistically stable behavior when the system is operating normally, but might vary over a wide range when the system is performing poorly. For example, the response time per transaction metric should be stable for a well-tuned OLTP system, but may fluctuate widely when performance issues arise. Significance level thresholds are meant to generate alerts when conditions produce both unusual metric values and unusual system performance.

Note:

The primary interface for managing baseline metrics is Oracle Enterprise Manager. To create an adaptive threshold for a baseline metric, use Oracle Enterprise Manager, as described in [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_degrade.htm#TDPPT334).

See Also:

"Moving Window Baseline"

### 5.2.4 Space Consumption

The space consumed by the AWR is determined by several factors:

- Number of active sessions in the system at any given time
- Snapshot interval
	The snapshot interval determines the frequency at which snapshots are captured. A smaller snapshot interval increases the frequency, which increases the volume of data collected by the AWR.
- Historical data retention period
	The retention period determines how long this data is retained before being purged. A longer retention period increases the space consumed by the AWR.

By default, snapshots are captured once every hour and are retained in the database for 8 days. With these default settings, a typical system with an average of 10 concurrent active sessions can require approximately 200 to 300 MB of space for its AWR data. It is possible to change the default values for both snapshot interval and retention period. See "Modifying Snapshot Settings" to learn how to modify AWR settings.

The AWR space consumption can be reduced by the increasing the snapshot interval and reducing the retention period. When reducing the retention period, note that several Oracle Database self-managing features depend on AWR data for proper functioning. Not having enough data can affect the validity and accuracy of these components and features, including:

- Automatic Database Diagnostic Monitor
- SQL Tuning Advisor
- Undo Advisor
- Segment Advisor

If possible, Oracle recommends that you set the AWR retention period large enough to capture at least one complete workload cycle. If your system experiences weekly workload cycles, such as OLTP workload during weekdays and batch jobs during the weekend, you do not need to change the default AWR retention period of 8 days. However if your system is subjected to a monthly peak load during month end book closing, you may have to set the retention period to one month.

Under exceptional circumstances, you can turn off automatic snapshot collection by setting the snapshot interval to 0. Under this condition, the automatic collection of the workload and statistical data is stopped and much of the Oracle Database self-management functionality is not operational. In addition, you cannot manually create snapshots. For this reason, Oracle strongly recommends that you do not turn off automatic snapshot collection.

## 5.3 Managing the Automatic Workload Repository

This section describes how to manage the AWR and contains the following topics:

- Managing Snapshots
- Managing Baselines
- Managing Baseline Templates
- Transporting Automatic Workload Repository Data
- Using Automatic Workload Repository Views
- Generating Automatic Workload Repository Reports
- Generating Automatic Workload Repository Compare Periods Reports
- Generating Active Session History Reports
- Using Active Session History Reports

See Also:

"Overview of the Automatic Workload Repository" for a description of the AWR

### 5.3.1 Managing Snapshots

By default, Oracle Database generates snapshots once every hour, and retains the statistics in the workload repository for 8 days. When necessary, you can use `DBMS_WORKLOAD_REPOSITORY` procedures to manually create, drop, and modify the snapshots. To invoke these procedures, a user must be granted the DBA role.

The primary interface for managing snapshots is Oracle Enterprise Manager. Whenever possible, you should manage snapshots using Oracle Enterprise Manager, as described in [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_auto.htm#TDPPT025). If Oracle Enterprise Manager is unavailable, you can manage snapshots using the `DBMS_WORKLOAD_REPOSITORY` package, as described in the following sections:

- Creating Snapshots
- Dropping Snapshots
- Modifying Snapshot Settings

See Also:

- "Snapshots" for more information about snapshots
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_workload_repos.htm#ARPLS093) for detailed information on the `DBMS_WORKLOAD_REPOSITORY` package

#### 5.3.1.1 Creating Snapshots

You can manually create snapshots with the `CREATE_SNAPSHOT` procedure to capture statistics at times different than those of the automatically generated snapshots. For example:

```
BEGIN
  DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT ();
END;
/
```

In this example, a snapshot for the instance is created immediately with the flush level specified to the default flush level of `TYPICAL`. You can view this snapshot in the `DBA_HIST_SNAPSHOT` view.

#### 5.3.1.2 Dropping Snapshots

You can drop a range of snapshots using the `DROP_SNAPSHOT_RANGE` procedure. To view a list of the snapshot IDs along with database IDs, check the `DBA_HIST_SNAPSHOT` view. For example, you can drop the following range of snapshots:

```
BEGIN
  DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE (low_snap_id => 22, 
                           high_snap_id => 32, dbid => 3310949047);
END;
/
```

In the example, the range of snapshot IDs to drop is specified from 22 to 32. The optional database identifier is `3310949047`. If you do not specify a value for `dbid`, the local database identifier is used as the default value.

Active Session History data (ASH) that belongs to the time period specified by the snapshot range is also purged when the `DROP_SNAPSHOT_RANGE` procedure is called.

#### 5.3.1.3 Modifying Snapshot Settings

You can adjust the interval, retention, and captured Top SQL of snapshot generation for a specified database ID, but note that this can affect the precision of the Oracle Database diagnostic tools.

The `INTERVAL` setting affects how often the database automatically generates snapshots. The `RETENTION` setting affects how long the database stores snapshots in the workload repository. The `TOPNSQL` setting affects the number of Top SQL to flush for each SQL criteria (Elapsed Time, CPU Time, Parse Calls, sharable Memory, and Version Count). The value for this setting is not affected by the statistics/flush level and will override the system default behavior for the AWR SQL collection. It is possible to set the value for this setting to `MAXIMUM` to capture the complete set of SQL in the shared SQL area, though by doing so (or by setting the value to a very high number) may lead to possible space and performance issues because there will more data to collect and store. To adjust the settings, use the `MODIFY_SNAPSHOT_SETTINGS` procedure. For example:

```
BEGIN
  DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS( retention => 43200, 
                 interval => 30, topnsql => 100, dbid => 3310949047);
END;
/
```

In this example, the retention period is specified as 43200 minutes (30 days), the interval between each snapshot is specified as 30 minutes, and the number of Top SQL to flush for each SQL criteria as 100. If NULL is specified, the existing value is preserved. The optional database identifier is `3310949047`. If you do not specify a value for `dbid`, the local database identifier is used as the default value. You can check the current settings for your database instance with the `DBA_HIST_WR_CONTROL` view.

### 5.3.2 Managing Baselines

This section describes how to manage baselines. The primary interface for managing baselines is Oracle Enterprise Manager. Whenever possible, you should manage baselines using Oracle Enterprise Manager, as described in [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_degrade.htm#TDPPT230). If Oracle Enterprise Manager is unavailable, you can manage baselines using the `DBMS_WORKLOAD_REPOSITORY` package, as described in the following sections:

- Creating a Baseline
- Dropping a Baseline
- Renaming a Baseline
- Displaying Baseline Metrics
- Modifying the Window Size of the Default Moving Window Baseline

See Also:

- "Baselines" for more information about baselines
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_workload_repos.htm#ARPLS093) for detailed information on the `DBMS_WORKLOAD_REPOSITORY` package

#### 5.3.2.1 Creating a Baseline

This section describes how to create a baseline using an existing range of snapshots.

To create a baseline:

1. Review the existing snapshots in the `DBA_HIST_SNAPSHOT` view to determine the range of snapshots to use.
2. Use the `CREATE_BASELINE` procedure to create a baseline using the desired range of snapshots:
	```
	BEGIN
	    DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE (start_snap_id => 270, 
	                   end_snap_id => 280, baseline_name => 'peak baseline', 
	                   dbid => 3310949047, expiration => 30);
	END;
	/
	```
	In this example, `270` is the start snapshot sequence number and `280` is the end snapshot sequence. The name of baseline is `peak baseline`. The optional database identifier is `3310949047`. If you do not specify a value for `dbid`, then the local database identifier is used as the default value. The optional `expiration` parameter is set to `30`, so the baseline will expire and be dropped automatically after 30 days. If you do not specify a value for `expiration`, the baseline will never expire.

The system automatically assign a unique baseline ID to the new baseline when the baseline is created. The baseline ID and database identifier are displayed in the `DBA_HIST_BASELINE` view.

#### 5.3.2.2 Dropping a Baseline

This section describes how to drop an existing baseline. Periodically, you may want to drop a baseline that is no longer used to conserve disk space. The snapshots associated with a baseline are retained indefinitely until you explicitly drop the baseline or the baseline has expired.

To drop a baseline:

1. Review the existing baselines in the `DBA_HIST_BASELINE` view to determine the baseline to drop.
2. Use the `DROP_BASELINE` procedure to drop the desired baseline:
	```
	BEGIN
	  DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE (baseline_name => 'peak baseline',
	                  cascade => FALSE, dbid => 3310949047);
	END;
	/
	```
	In the example, the name of baseline is `peak baseline`. The `cascade` parameter is set to `FALSE`, which specifies that only the baseline is dropped. Setting this parameter to `TRUE` specifies that the drop operation will also remove the snapshots associated with the baseline. The optional `dbid` parameter specifies the database identifier, which in this example is `3310949047`. If you do not specify a value for `dbid`, then the local database identifier is used as the default value.

#### 5.3.2.3 Renaming a Baseline

This section describes how to rename a baseline.

To rename a baseline:

1. Review the existing baselines in the `DBA_HIST_BASELINE` view to determine the baseline to rename.
2. Use the `RENAME_BASELINE` procedure to rename the desired baseline:
	```
	BEGIN
	    DBMS_WORKLOAD_REPOSITORY.RENAME_BASELINE (
	                   old_baseline_name => 'peak baseline', 
	                   new_baseline_name => 'peak mondays', 
	                   dbid => 3310949047);
	END;
	/
	```
	In this example, the name of the baseline is renamed from `peak baseline`, as specified by the `old_baseline_name` parameter, to `peak mondays`, as specified by the `new_baseline_name` parameter. The optional `dbid` parameter specifies the database identifier, which in this example is `3310949047`. If you do not specify a value for `dbid`, then the local DBID is the default value.

#### 5.3.2.4 Displaying Baseline Metrics

This section describes how to display metric threshold settings during the time period captured in a baseline. When used with adaptive thresholds, a baseline contains AWR data that the database can use to compute metric threshold values. The `SELECT_BASELINE_METRICS` function enables you to display the summary statistics for metric values in a baseline period.

To display metric information in a baseline:

1. Review the existing baselines in the `DBA_HIST_BASELINE` view to determine the baseline for which you want to display metric information.
2. Use the `SELECT_BASELINE_METRICS` function to display the metric information for the desired baseline:
	```
	BEGIN
	    DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_METRICS (
	                   baseline_name => 'peak baseline', 
	                   dbid => 3310949047,
	                   instance_num => '1');
	END;
	/
	```
	In this example, the name of baseline is `peak baseline`. The optional `dbid` parameter specifies the database identifier, which in this example is `3310949047`. If you do not specify a value for `dbid`, then the local database identifier is used as the default value. The optional `instance_num` parameter specifies the instance number, which in this example is `1`. If you do not specify a value for `instance_num`, then the local instance is used as the default value.

#### 5.3.2.5 Modifying the Window Size of the Default Moving Window Baseline

This section describes how to modify the window size of the default moving window baseline. For information about the default moving window baseline, see "Moving Window Baseline".

To resize the default moving window baseline, use the `MODIFY_BASELINE_WINDOW_SIZE` procedure:

```
BEGIN
    DBMS_WORKLOAD_REPOSITORY.MODIFY_BASELINE_WINDOW_SIZE (
                   window_size => 30, 
                   dbid => 3310949047);
END;
/
```

The `window_size` parameter is used to specify the new window size, in number of days, for the default moving window size. In this example, the `window_size` parameter is set to 30. The window size must be set to a value that is equal to or less than the value of the AWR retention setting. To set a window size that is greater than the current AWR retention period, you must first increase the value of the `retention` parameter, as described in "Modifying Snapshot Settings".

In this example, the optional `dbid` parameter specifies the database identifier is `3310949047`. If you do not specify a value for `dbid`, then the local database identifier is used as the default value.

### 5.3.3 Managing Baseline Templates

This section describes how to manage baseline templates. You can automatically create baselines to capture specified time periods in the future using baseline templates. For information about baseline templates, see "Baseline Templates".

The primary interface for managing baseline templates is Oracle Enterprise Manager. Whenever possible, you should manage baseline templates using Oracle Enterprise Manager, as described in [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_degrade.htm#TDPPT230). If Oracle Enterprise Manager is unavailable, you can manage baseline templates using the `DBMS_WORKLOAD_REPOSITORY` package, as described in the following sections:

- Creating a Single Baseline Template
- Creating a Repeating Baseline Template
- Dropping a Baseline Template

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_workload_repos.htm#ARPLS093) for detailed information on the `DBMS_WORKLOAD_REPOSITORY` package

#### 5.3.3.1 Creating a Single Baseline Template

This section describes how to create a single baseline template. You can use a single baseline template to create a baseline during a single, fixed time interval in the future. For example, you can create a single baseline template to generate a baseline that is captured on April 2, 2009 from 5:00 p.m. to 8:00 p.m.

To create a single baseline template, use the `CREATE_BASELINE_TEMPLATE` procedure:

```
BEGIN
    DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE (
                   start_time => '2009-04-02 17:00:00 PST', 
                   end_time => '2009-04-02 20:00:00 PST', 
                   baseline_name => 'baseline_090402', 
                   template_name => 'template_090402', expiration => 30, 
                   dbid => 3310949047);
END;
/
```

The `start_time` parameter specifies the start time for the baseline to be created. The `end_time` parameter specifies the end time for the baseline to be created. The `baseline_name` parameter specifies the name of the baseline to be created. The `template_name` parameter specifies the name of the baseline template. The optional `expiration` parameter specifies the expiration, in number of days, for the baseline. If unspecified, then the baseline never expires. The optional `dbid` parameter specifies the database identifier. If unspecified, then the local database identifier is used as the default value.

In this example, a baseline template named `template_090402` is created that will generate a baseline named `baseline_090402` for the time period from 5:00 p.m. to 8:00 p.m. on April 2, 2009 on the database with a database ID of `3310949047`. The baseline will expire after 30 days.

#### 5.3.3.2 Creating a Repeating Baseline Template

This section describes how to create a repeating baseline template. A repeating baseline template can be used to automatically create baselines that repeat during a particular time interval over a specific period in the future. For example, you can create a repeating baseline template to generate a baseline that repeats every Monday from 5:00 p.m. to 8:00 p.m. for the year 2009.

To create a repeating baseline template, use the `CREATE_BASELINE_TEMPLATE` procedure:

```
BEGIN
    DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE (
                   day_of_week => 'monday', hour_in_day => 17,
                   duration => 3, expiration => 30,
                   start_time => '2009-04-02 17:00:00 PST', 
                   end_time => '2009-12-31 20:00:00 PST', 
                   baseline_name_prefix => 'baseline_2009_mondays_', 
                   template_name => 'template_2009_mondays',
                   dbid => 3310949047);
END;
/
```

The `day_of_week` parameter specifies the day of the week on which the baseline will repeat. The `hour_in_day` parameter specifies the hour in the day when the baseline will start. The `duration` parameter specifies the duration, in number of hours, that the baseline will last. The `expiration` parameter specifies the number of days to retain each created baseline. If set to `NULL`, then the baselines never expires. The `start_time` parameter specifies the start time for the baseline to be created. The `end_time` parameter specifies the end time for the baseline to be created. The `baseline_name_prefix` parameter specifies the name of the baseline prefix that will be appended to the data information when the baseline is created. The `template_name` parameter specifies the name of the baseline template. The optional `dbid` parameter specifies the database identifier. If unspecified, then the local database identifier is used as the default value.

In this example, a baseline template named `template_2009_mondays` is created that will generate a baseline on every Monday from 5:00 p.m. to 8:00 p.m. beginning on April 2, 2009 at 5:00 p.m. and ending on December 31, 2009 at 8:00 p.m. on the database with a database ID of `3310949047`. Each of the baselines will be created with a baseline name with the prefix `baseline_2009_mondays_` and will expire after 30 days.

#### 5.3.3.3 Dropping a Baseline Template

This section describes how to drop an existing baseline template. Periodically, you may want to remove baselines templates that are no longer used to conserve disk space.

To drop a baseline template:

1. Review the existing baselines in the `DBA_HIST_BASELINE_TEMPLATE` view to determine the baseline template you want to drop.
2. Use the `DROP_BASELINE_TEMPLATE` procedure to drop the desired baseline template:
	```
	BEGIN
	  DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE_TEMPLATE (
	                   template_name => 'template_2009_mondays',
	                   dbid => 3310949047);
	END;
	/
	```
	The `template_name` parameter specifies the name of the baseline template that will be dropped. In the example, the name of baseline template that will be dropped is `template_2009_mondays`. The optional `dbid` parameter specifies the database identifier, which in this example is `3310949047`. If you do not specify a value for `dbid`, then the local database identifier is used as the default value.

### 5.3.4 Transporting Automatic Workload Repository Data

Oracle Database enables you to transport AWR data between systems. This is useful in cases where you want to use a separate system to perform analysis of the AWR data. To transport AWR data, you must first extract the AWR snapshot data from the database on the source system, then load the data into the database on the target system, as described in the following sections:

- Extracting AWR Data
- Loading AWR Data

#### 5.3.4.1 Extracting AWR Data

The `awrextr.sql` script extracts the AWR data for a range of snapshots from the database into a Data Pump export file. After it is created, you can transport this dump file to another database where you can load the extracted data. To run the `awrextr.sql` script, you must be connected to the database as the `SYS` user.

To extract AWR data:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrextr.sql
	```
	A list of the databases in the AWR schema is displayed.
2. Specify the database from which the AWR data will be extracted:
	```
	Enter value for db_id: 1377863381
	```
	In this example, the database with the database identifier of `1377863381` is selected.
3. Specify the number of days for which you want to list snapshot IDs.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
4. Define the range of snapshots for which AWR data will be extracted by specifying a beginning and ending snapshot ID:
	```
	Enter value for begin_snap: 30
	Enter value for end_snap: 40
	```
	In this example, the snapshot with a snapshot ID of 30 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 40 is selected as the ending snapshot.
5. A list of directory objects is displayed.
	Specify the directory object pointing to the directory where the export dump file will be stored:
	```
	Enter value for directory_name: DATA_PUMP_DIR
	```
	In this example, the directory object `DATA_PUMP_DIR` is selected.
6. Specify the prefix for name of the export dump file (the `.dmp` suffix will be automatically appended):
	```
	Enter value for file_name: awrdata_30_40
	```
	In this example, an export dump file named `awrdata_30_40` will be created in the directory corresponding to the directory object you specified:
	```
	Dump file set for SYS.SYS_EXPORT_TABLE_01 is:
	C:\ORACLE\PRODUCT\11.1.0.5\DB_1\RDBMS\LOG\AWRDATA_30_40.DMP
	Job "SYS"."SYS_EXPORT_TABLE_01" successfully completed at 08:58:20
	```
	Depending on the amount of AWR data that must be extracted, the AWR extract operation may take a while to complete. After the dump file is created, you can use Data Pump to transport the file to another system.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_overview.htm#SUTIL100) for information about using Data Pump

#### 5.3.4.2 Loading AWR Data

After the export dump file is transported to the target system, you can load the extracted AWR data using the `awrload.sql` script. The `awrload.sql` script will first create a staging schema where the snapshot data is transferred from the Data Pump file into the database. The data is then transferred from the staging schema into the appropriate AWR tables. To run the `awrload.sql` script, you must be connected to the database as the `SYS` user.

To load AWR data:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrload.sql
	```
	A list of directory objects is displayed.
2. Specify the directory object pointing to the directory where the export dump file is located:
	```
	Enter value for directory_name: DATA_PUMP_DIR
	```
	In this example, the directory object `DATA_PUMP_DIR` is selected.
3. Specify the prefix for name of the export dump file (the `.dmp` suffix will be automatically appended):
	```
	Enter value for file_name: awrdata_30_40
	```
	In this example, the export dump file named `awrdata_30_40` is selected.
4. Specify the name of the staging schema where the AWR data will be loaded:
	```
	Enter value for schema_name: AWR_STAGE
	```
	In this example, a staging schema named `AWR_STAGE` will be created where the AWR data will be loaded.
5. Specify the default tablespace for the staging schema:
	```
	Enter value for default_tablespace: SYSAUX
	```
	In this example, the `SYSAUX` tablespace is selected.
6. Specify the temporary tablespace for the staging schema:
	```
	Enter value for temporary_tablespace: TEMP
	```
	In this example, the `TEMP` tablespace is selected.
7. A staging schema named `AWR_STAGE` will be created where the AWR data will be loaded. After the AWR data is loaded into the `AWR_STAGE` schema, the data will be transferred into the AWR tables in the `SYS` schema:
	```
	Processing object type TABLE_EXPORT/TABLE/CONSTRAINT/CONSTRAINT
	Completed 113 CONSTRAINT objects in 11 seconds
	Processing object type TABLE_EXPORT/TABLE/CONSTRAINT/REF_CONSTRAINT
	Completed 1 REF_CONSTRAINT objects in 1 seconds
	Job "SYS"."SYS_IMPORT_FULL_03" successfully completed at 09:29:30
	... Dropping AWR_STAGE user
	End of AWR Load
	```
	Depending on the amount of AWR data that must be loaded, the AWR load operation may take a while to complete. After the AWR data is loaded, the staging schema will be dropped automatically.

### 5.3.5 Using Automatic Workload Repository Views

Typically, you would view the AWR data through Oracle Enterprise Manager or AWR reports. However, you can also view the statistics using the following views:

- `V$ACTIVE_SESSION_HISTORY`
	This view displays active database session activity, sampled once every second. See "Active Session History".
- `V$` metric views provide metric data to track the performance of the system
	The metric views are organized into various groups, such as event, event class, system, session, service, file, and tablespace metrics. These groups are identified in the `V$METRICGROUP` view.
- `DBA_HIST` views
	The `DBA_HIST` views displays historical data stored in the database. This group of views includes:
	- `DBA_HIST_ACTIVE_SESS_HISTORY` displays the history of the contents of the in-memory active session history for recent system activity
		- `DBA_HIST_BASELINE` displays information about the baselines captured on the system, such as the time range of each baseline and the baseline type
		- `DBA_HIST_BASELINE_DETAILS` displays details about a specific baseline
		- `DBA_HIST_BASELINE_TEMPLATE` displays information about the baseline templates used by the system to generate baselines
		- `DBA_HIST_DATABASE_INSTANCE` displays information about the database environment
		- `DBA_HIST_DB_CACHE_ADVICE` displays historical predictions of the number of physical reads for the cache size corresponding to each row
		- `DBA_HIST_DISPATCHER` displays historical information for each dispatcher process at the time of the snapshot
		- `DBA_HIST_DYN_REMASTER_STATS` displays statistical information about the dynamic remastering process
		- `DBA_HIST_IOSTAT_DETAIL` displays historical I/O statistics aggregated by file type and function
		- `DBA_HIST_SHARED_SERVER_SUMMARY` displays historical information for shared servers, such as shared server activity, common queues and dispatcher queues
		- `DBA_HIST_SNAPSHOT` displays information on snapshots in the system
		- `DBA_HIST_SQL_PLAN` displays the SQL execution plans
		- `DBA_HIST_WR_CONTROL` displays the settings for controlling AWR
		See Also:
		[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for information about dynamic and static data dictionary views

### 5.3.6 Generating Automatic Workload Repository Reports

An AWR report shows data captured between two snapshots (or two points in time). The AWR reports are divided into multiple sections. The HTML report includes links that can be used to navigate quickly between sections. The content of the report contains the workload profile of the system for the selected range of snapshots.

The primary interface for generating AWR reports is Oracle Enterprise Manager. Whenever possible, you should generate AWR reports using Oracle Enterprise Manager, as described in [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_auto.htm#TDPPT032). If Oracle Enterprise Manager is unavailable, you can generate AWR reports by running SQL scripts, as described in the following sections:

- Generating an AWR Report
- Generating an Oracle RAC AWR Report
- Generating an AWR Report on a Specific Database Instance
- Generating an Oracle RAC AWR Report on Specific Database Instances
- Generating an AWR Report for a SQL Statement
- Generating an AWR Report for a SQL Statement on a Specific Database Instance

To run these scripts, you must be granted the DBA role.

Note:

If you run a report on a database that does not have any workload activity during the specified range of snapshots, calculated percentages for some report statistics can be less than 0 or greater than 100. This result simply means that there is no meaningful value for the statistic.

#### 5.3.6.1 Generating an AWR Report

The `awrrpt.sql` SQL script generates an HTML or text report that displays statistics for a range of snapshot IDs.

To generate an AWR report:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrrpt.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: text
	```
	In this example, a text report is chosen.
3. Specify the number of days for which you want to list snapshot IDs.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
4. Specify a beginning and ending snapshot ID for the workload repository report:
	```
	Enter value for begin_snap: 150
	Enter value for end_snap: 160
	```
	In this example, the snapshot with a snapshot ID of 150 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 160 is selected as the ending snapshot.
5. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrrpt_1_150_160
	```
	In this example, the default name is accepted and an AWR report named `awrrpt_1_150_160` is generated.

#### 5.3.6.2 Generating an Oracle RAC AWR Report

The `awrgrpt.sql` SQL script generates an HTML or text report that displays statistics for a range of snapshot IDs using the current database identifier and all available database instances in an Oracle Real Application Clusters (Oracle RAC) environment.

Note:

In an Oracle RAC environment, you should always try to generate an HTML report (instead of a text report) because they are much easier to read.

To generate an AWR report in an Oracle RAC environment:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrgrpt.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
3. Specify the number of days for which you want to list snapshot IDs.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last day are displayed.
4. Specify a beginning and ending snapshot ID for the workload repository report:
	```
	Enter value for begin_snap: 150
	Enter value for end_snap: 160
	```
	In this example, the snapshot with a snapshot ID of 150 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 160 is selected as the ending snapshot.
5. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrrpt_rac_150_160.html
	```
	In this example, the default name is accepted and an AWR report named `awrrpt_rac_150_160.html` is generated.

#### 5.3.6.3 Generating an AWR Report on a Specific Database Instance

The `awrrpti.sql` SQL script generates an HTML or text report that displays statistics for a range of snapshot IDs using a specific database and instance. This script enables you to specify a database identifier and instance for which the AWR report will be generated.

To generate an AWR report on a specific database instance:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrrpti.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: text
	```
	In this example, a text report is chosen.
	A list of available database identifiers and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	```
3. Enter the values for the database identifier (`dbid)` and instance number (`inst_num)`:
	```
	Enter value for dbid: 3309173529
	Using 3309173529 for database Id
	Enter value for inst_num: 1
	```
4. Specify the number of days for which you want to list snapshot IDs.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
5. Specify a beginning and ending snapshot ID for the workload repository report:
	```
	Enter value for begin_snap: 150
	Enter value for end_snap: 160
	```
	In this example, the snapshot with a snapshot ID of 150 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 160 is selected as the ending snapshot.
6. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrrpt_1_150_160
	```
	In this example, the default name is accepted and an AWR report named `awrrpt_1_150_160` is generated on the database instance with a database ID value of `3309173529`.

#### 5.3.6.4 Generating an Oracle RAC AWR Report on Specific Database Instances

The `awrgrpti.sql` SQL script generates an HTML or text report that displays statistics for a range of snapshot IDs using specific databases and instances running in an Oracle RAC environment. This script enables you to specify database identifiers and a comma-delimited list of database instances for which the AWR report will be generated.

Note:

In an Oracle RAC environment, you should always try to generate an HTML report (instead of a text report) because they are much easier to read.

To generate an AWR report on a specific database instance in an Oracle RAC environment:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrgrpti.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
	A list of available database identifiers and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	 3309173529        2 TINT251      tint252      samp252
	```
3. Enter the value for the database identifier (`dbid)`:
	```
	Enter value for dbid: 3309173529
	Using 3309173529 for database Id
	```
4. Enter the value for the instance numbers (`instance_numbers_or_all`) of the Oracle RAC instances you want to include in the report:
	```
	Enter value for instance_numbers_or_all: 1,2
	```
5. Specify the number of days for which you want to list snapshot IDs.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
6. Specify a beginning and ending snapshot ID for the workload repository report:
	```
	Enter value for begin_snap: 150
	Enter value for end_snap: 160
	```
	In this example, the snapshot with a snapshot ID of 150 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 160 is selected as the ending snapshot.
7. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrrpt_rac_150_160.html
	```
	In this example, the default name is accepted and an AWR report named `awrrpt_rac_150_160.html` is generated on the database instance with a database ID value of `3309173529`.

#### 5.3.6.5 Generating an AWR Report for a SQL Statement

The `awrsqrpt.sql` SQL script generates an HTML or text report that displays statistics of a particular SQL statement for a range of snapshot IDs. Run this report to inspect or debug the performance of a SQL statement.

To generate an AWR report for a particular SQL statement:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrsqrpt.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
3. Specify the number of days for which you want to list snapshot IDs.
	```
	Enter value for num_days: 1
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the previous day are displayed.
4. Specify a beginning and ending snapshot ID for the workload repository report:
	```
	Enter value for begin_snap: 146
	Enter value for end_snap: 147
	```
	In this example, the snapshot with a snapshot ID of 146 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 147 is selected as the ending snapshot.
5. Specify the SQL ID of a particular SQL statement to display statistics:
	```
	Enter value for sql_id: 2b064ybzkwf1y
	```
	In this example, the SQL statement with a SQL ID of `2b064ybzkwf1y` is selected.
6. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrrpt_1_146_147.html
	```
	In this example, the default name is accepted and an AWR report named `awrrpt_1_146_147` is generated.

#### 5.3.6.6 Generating an AWR Report for a SQL Statement on a Specific Database Instance

The `awrsqrpi.sql` SQL script generates an HTML or text report that displays statistics of a particular SQL statement for a range of snapshot IDs using a specific database and instance.This script enables you to specify a database identifier and instance for which the AWR report will be generated. Run this report to inspect or debug the performance of a SQL statement on a specific database and instance.

To generate an AWR report for a particular SQL statement on a specified database instance:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrsqrpi.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
	A list of available database identifiers and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	```
3. Enter the values for the database identifier (`dbid)` and instance number (`inst_num)`:
	```
	Enter value for dbid: 3309173529
	Using 3309173529 for database Id
	Enter value for inst_num: 1
	Using 1 for instance number
	```
4. Specify the number of days for which you want to list snapshot IDs.
	```
	Enter value for num_days: 1
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the previous day are displayed.
5. Specify a beginning and ending snapshot ID for the workload repository report:
	```
	Enter value for begin_snap: 146
	Enter value for end_snap: 147
	```
	In this example, the snapshot with a snapshot ID of 146 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 147 is selected as the ending snapshot.
6. Specify the SQL ID of a particular SQL statement to display statistics:
	```
	Enter value for sql_id: 2b064ybzkwf1y
	```
	In this example, the SQL statement with a SQL ID of `2b064ybzkwf1y` is selected.
7. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrrpt_1_146_147.html
	```
	In this example, the default name is accepted and an AWR report named `awrrpt_1_146_147` is generated on the database instance with a database ID value of `3309173529`.

### 5.3.7 Generating Automatic Workload Repository Compare Periods Reports

While an AWR report shows AWR data between two snapshots (or two points in time), the AWR Compare Periods report shows the difference between two periods (or two AWR reports, which equates to four snapshots). Using the AWR Compare Periods report helps you to identify detailed performance attributes and configuration settings that differ between two time periods.

For example, if the application workload is known to be stable between 10:00 p.m. and midnight every night, but the performance on a particular Thursday was poor between 10:00 p.m. and 11:00 p.m., generating an AWR Compare Periods report for Thursday from 10:00 p.m. to 11:00 p.m. and Wednesday from 10:00 p.m. to 11:00 p.m. should identify configuration settings, workload profile, and statistics that were different in these time periods. Based on the differences, you can more easily diagnose the cause of the performance degradation. The two time periods selected for the AWR Compare Periods Report can be of different durations because the report normalizes the statistics by the amount of time spent on the database for each time period, and presents statistical data ordered by the largest difference between the periods.

The AWR Compare Periods reports are divided into multiple sections. The HTML report includes links that can be used to navigate quickly between sections. The content of the report contains the workload profile of the system for the selected range of snapshots.

The primary interface for generating AWR Compare Periods reports is Oracle Enterprise Manager. Whenever possible, you should generate AWR Compare Periods reports using Oracle Enterprise Manager, as described in [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_degrade.htm#TDPPT091). If Oracle Enterprise Manager is unavailable, you can generate AWR Compare Periods reports by running SQL scripts, as described in the following sections:

- Generating an AWR Compare Periods Report
- Generating an Oracle RAC AWR Compare Periods Report
- Generating an AWR Compare Periods Report on a Specific Database Instance
- Generating an Oracle RAC AWR Compare Periods Report on Specific Database Instances

To run these scripts, you must be granted the DBA role.

#### 5.3.7.1 Generating an AWR Compare Periods Report

The `awrddrpt.sql` SQL script generates an HTML or text report that compares detailed performance attributes and configuration settings between two selected time periods.

To generate an AWR Compare Periods report:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrddrpt.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
3. Specify the number of days for which you want to list snapshot IDs in the first time period.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
4. Specify a beginning and ending snapshot ID for the first time period:
	```
	Enter value for begin_snap: 102
	Enter value for end_snap: 103
	```
	In this example, the snapshot with a snapshot ID of 102 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 103 is selected as the ending snapshot for the first time period.
5. Specify the number of days for which you want to list snapshot IDs in the second time period.
	```
	Enter value for num_days2: 1
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the previous day are displayed.
6. Specify a beginning and ending snapshot ID for the second time period:
	```
	Enter value for begin_snap2: 126
	Enter value for end_snap2: 127
	```
	In this example, the snapshot with a snapshot ID of 126 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 127 is selected as the ending snapshot for the second time period.
7. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrdiff_1_102_1_126.txt
	```
	In this example, the default name is accepted and an AWR report named `awrdiff_1_102_126` is generated.

#### 5.3.7.2 Generating an Oracle RAC AWR Compare Periods Report

The `awrgdrpt.sql` SQL script generates an HTML or text report that compares detailed performance attributes and configuration settings between two selected time periods using the current database identifier and all available database instances in an Oracle RAC environment.

Note:

In an Oracle RAC environment, you should always try to generate an HTML report (instead of a text report) because they are much easier to read.

To generate an AWR Compare Periods report in an Oracle RAC environment:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrgdrpt.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
3. Specify the number of days for which you want to list snapshot IDs in the first time period.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
4. Specify a beginning and ending snapshot ID for the first time period:
	```
	Enter value for begin_snap: 102
	Enter value for end_snap: 103
	```
	In this example, the snapshot with a snapshot ID of 102 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 103 is selected as the ending snapshot for the first time period.
5. Specify the number of days for which you want to list snapshot IDs in the second time period.
	```
	Enter value for num_days2: 1
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the previous day are displayed.
6. Specify a beginning and ending snapshot ID for the second time period:
	```
	Enter value for begin_snap2: 126
	Enter value for end_snap2: 127
	```
	In this example, the snapshot with a snapshot ID of 126 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 127 is selected as the ending snapshot for the second time period.
7. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrracdiff_1st_1_2nd_1.html
	```
	In this example, the default name is accepted and an AWR report named `awrrac_1st_1_2nd_1.html` is generated.

#### 5.3.7.3 Generating an AWR Compare Periods Report on a Specific Database Instance

The `awrddrpi.sql` SQL script generates an HTML or text report that compares detailed performance attributes and configuration settings between two selected time periods on a specific database and instance. This script enables you to specify a database identifier and instance for which the AWR Compare Periods report will be generated.

To generate an AWR Compare Periods report on a specified database instance:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrddrpi.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: text
	```
	In this example, a text report is chosen.
3. A list of available database identifiers and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	```
	Enter the values for the database identifier (`dbid)` and instance number (`inst_num)` for the first time period:
	```
	Enter value for dbid: 3309173529
	Using 3309173529 for Database Id for the first pair of snapshots
	Enter value for inst_num: 1
	Using 1 for Instance Number for the first pair of snapshots
	```
4. Specify the number of days for which you want to list snapshot IDs in the first time period.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
5. Specify a beginning and ending snapshot ID for the first time period:
	```
	Enter value for begin_snap: 102
	Enter value for end_snap: 103
	```
	In this example, the snapshot with a snapshot ID of 102 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 103 is selected as the ending snapshot for the first time period.
6. Enter the values for the database identifier (`dbid)` and instance number (`inst_num)` for the second time period:
	```
	Enter value for dbid2: 3309173529
	Using 3309173529 for Database Id for the second pair of snapshots
	Enter value for inst_num2: 1
	Using 1 for Instance Number for the second pair of snapshots
	```
7. Specify the number of days for which you want to list snapshot IDs in the second time period.
	```
	Enter value for num_days2: 1
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the previous day are displayed.
8. Specify a beginning and ending snapshot ID for the second time period:
	```
	Enter value for begin_snap2: 126
	Enter value for end_snap2: 127
	```
	In this example, the snapshot with a snapshot ID of 126 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 127 is selected as the ending snapshot for the second time period.
9. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrdiff_1_102_1_126.txt
	```
	In this example, the default name is accepted and an AWR report named `awrdiff_1_102_126` is generated on the database instance with a database ID value of `3309173529`.

#### 5.3.7.4 Generating an Oracle RAC AWR Compare Periods Report on Specific Database Instances

The `awrgdrpi.sql` SQL script generates an HTML or text report that compares detailed performance attributes and configuration settings between two selected time periods using specific databases and instances in an Oracle RAC environment. This script enables you to specify database identifiers and a comma-delimited list of database instances for which the AWR Compare Periods report will be generated.

Note:

In an Oracle RAC environment, you should always try to generate an HTML report (instead of a text report) because they are much easier to read.

To generate an AWR Compare Periods report on a specified database instance in an Oracle RAC environment:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/awrgdrpi.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
3. A list of available database identifiers and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	 3309173529        2 TINT251      tint252      samp252
	 3309173529        3 TINT251      tint253      samp253
	 3309173529        4 TINT251      tint254      samp254
	```
	Enter the values for the database identifier (`dbid)` and instance number (`instance_numbers_or_all)` for the first time period:
	```
	Enter value for dbid: 3309173529
	Using 3309173529 for Database Id for the first pair of snapshots
	Enter value for inst_num: 1,2
	Using instances 1 for the first pair of snapshots
	```
4. Specify the number of days for which you want to list snapshot IDs in the first time period.
	```
	Enter value for num_days: 2
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the last 2 days are displayed.
5. Specify a beginning and ending snapshot ID for the first time period:
	```
	Enter value for begin_snap: 102
	Enter value for end_snap: 103
	```
	In this example, the snapshot with a snapshot ID of 102 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 103 is selected as the ending snapshot for the first time period.
6. A list of available database identifiers and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	 3309173529        2 TINT251      tint252      samp252
	 3309173529        3 TINT251      tint253      samp253
	 3309173529        4 TINT251      tint254      samp254
	INSTNUM1
	-----------------------------------------------------
	1,2
	```
	Enter the values for the database identifier (`dbid2)` and instance numbers (`instance_numbers_or_all2`) for the second time period:
	```
	Enter value for dbid2: 3309173529
	Using 3309173529 for Database Id for the second pair of snapshots
	Enter value for instance_numbers_or_all2: 3,4
	```
7. Specify the number of days for which you want to list snapshot IDs in the second time period.
	```
	Enter value for num_days2: 1
	```
	A list of existing snapshots for the specified time range is displayed. In this example, snapshots captured in the previous day are displayed.
8. Specify a beginning and ending snapshot ID for the second time period:
	```
	Enter value for begin_snap2: 126
	Enter value for end_snap2: 127
	```
	In this example, the snapshot with a snapshot ID of 126 is selected as the beginning snapshot, and the snapshot with a snapshot ID of 127 is selected as the ending snapshot for the second time period.
9. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name awrracdiff_1st_1_2nd_1.html
	```
	In this example, the default name is accepted and an AWR report named `awrrac_1st_1_2nd_1.html` is generated.

### 5.3.8 Generating Active Session History Reports

Use Active Session History (ASH) reports to perform analysis of:

- Transient performance problems that typically last for a few minutes
- Scoped or targeted performance analysis by various dimensions or their combinations, such as time, session, module, action, or `SQL_ID`

Transient performance problems are short-lived and do not appear in the Automatic Database Diagnostics Monitor (ADDM) analysis. ADDM tries to report the most significant performance problems during an analysis period in terms of their impact on DB time. If a particular problem lasts for a very short duration, then its severity might be averaged out or minimized by other performance problems in the analysis period. Therefore, the problem may not appear in the ADDM findings. Whether a performance problem is captured by ADDM depends on its duration compared to the interval between the AWR snapshots.

If a performance problem lasts for a significant portion of the time between snapshots, it will be captured by ADDM. For example, if the snapshot interval is set to one hour, a performance problem that lasts for 30 minutes should not be considered as a transient performance problem because its duration represents a significant portion of the snapshot interval and will likely be captured by ADDM.

However, a performance problem that lasts for only 2 minutes could be a transient performance problem because its duration represents a small portion of the snapshot interval and will likely not show up in the ADDM findings. For example, if the user notifies you that the system was slow between 10:00 p.m. and 10:10 p.m., but the ADDM analysis for the time period between 10:00 p.m. and 11:00 p.m. does not show a performance problem, a transient performance problem probably occurred that lasted for only a few minutes of the 10-minute interval reported by the user.

The ASH reports are divided into multiple sections. The HTML report includes links that can be used to navigate quickly between sections. The content of the report contains ASH information used to identify blocker and waiter identities and their associated transaction identifiers and SQL for a specified duration. For more information on ASH, see "Active Session History".

The primary interface for generating ASH reports is Oracle Enterprise Manager. Whenever possible, you should generate ASH reports using Oracle Enterprise Manager, as described in [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_transient.htm#TDPPT066). If Oracle Enterprise Manager is unavailable, you can generate ASH reports by running SQL scripts, as described in the following sections:

- Generating an ASH Report
- Generating an ASH Report on a Specific Database Instance
- Generating an Oracle RAC ASH Report

#### 5.3.8.1 Generating an ASH Report

The `ashrpt.sql` SQL script generates an HTML or text report that displays ASH information for a specified duration.

To generate an ASH report:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/ashrpt.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: text
	```
	In this example, a text report is chosen.
3. Specify the begin time in minutes before the system date:
	```
	Enter value for begin_time: -10
	```
	In this example, 10 minutes before the current time is selected.
4. Enter the duration in minutes that the report for which you want to capture ASH information from the begin time.
	```
	Enter value for duration:
	```
	In this example, the default duration of system date minus begin time is accepted.
5. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name ashrpt_1_0310_0131.txt
	```
	In this example, the default name is accepted and an ASH report named `ashrpt_1_0310_0131` is generated. The report will gather ASH information beginning from 10 minutes before the current time and ending at the current time.

#### 5.3.8.2 Generating an ASH Report on a Specific Database Instance

The `ashrpti.sql` SQL script generates an HTML or text report that displays ASH information for a specified duration for a specified database and instance. This script enables you to specify a database and instance before setting the time frame to collect ASH information.

To generate an ASH report on a specified database instance:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/ashrpti.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
3. A list of available database IDs and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	```
	Enter the values for the database identifier (`dbid)` and instance number (`inst_num)`:
	```
	Enter value for dbid: 3309173529
	Using 3309173529 for database id
	Enter value for inst_num: 1
	```
4. This step is applicable only if you are generating an ASH report on an Active Data Guard physical standby instance. If this is not the case, you may skip this step.
	To generate an ASH report on a physical standby instance, the standby database must be opened read-only. The ASH data on disk represents activity on the primary database and the ASH data in memory represents activity on the standby database.
	Specify whether to generate the report using data sampled from the primary or standby database:
	```
	You are running ASH report on a Standby database.
	To generate the report over data sampled on the Primary database, enter 'P'.
	Defaults to 'S' - data sampled in the Standby database.
	Enter value for stdbyflag:
	Using Primary (P) or Standby (S): S
	```
	In this example, the default value of Standby (S) is selected.
5. Specify the begin time in minutes before the system date:
	```
	Enter value for begin_time: -10
	```
	In this example, 10 minutes before the current time is selected.
6. Enter the duration in minutes that the report for which you want to capture ASH information from the begin time.
	```
	Enter value for duration:
	```
	In this example, the default duration of system date minus begin time is accepted.
7. Specify the slot width in seconds that will be used in the Activity Over Time section of the report:
	```
	Enter value for slot_width:
	```
	In this example, the default value is accepted. For more information about the Activity Over Time section and how to specify the slot width, see "Activity Over Time".
8. Follow the instructions as explained in the subsequent prompts and enter values for the following report targets:
	- `target_session_id`
		- `target_sql_id`
		- `target_wait_class`
		- `target_service_hash`
		- `target_module_name`
		- `target_action_name`
		- `target_client_id`
		- `target_plsql_entry`
9. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name ashrpt_1_0310_0131.txt
	```
	In this example, the default name is accepted and an ASH report named `ashrpt_1_0310_0131` is generated. The report will gather ASH information on the database instance with a database ID value of `3309173529` beginning from 10 minutes before the current time and ending at the current time.

#### 5.3.8.3 Generating an Oracle RAC ASH Report

The `ashrpti.sql` SQL script generates an HTML or text report that displays ASH information for a specified duration for specified databases and instances in an Oracle RAC environment. Only ASH data that is written to disk will be used to generate the report. This report will only use ASH samples from the last 10 minutes that are found in the `DBA_HIST_ACTIVE_SESS_HISTORY` table.

To generate an ASH report in an Oracle RAC environment:

1. At the SQL prompt, enter:
	```
	@$ORACLE_HOME/rdbms/admin/ashrpti.sql
	```
2. Specify whether you want an HTML or a text report:
	```
	Enter value for report_type: html
	```
	In this example, an HTML report is chosen.
3. A list of available database IDs and instance numbers are displayed:
	```
	Instances in this Workload Repository schema
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	   DB Id    Inst Num DB Name      Instance     Host
	----------- -------- ------------ ------------ ------------
	 3309173529        1 MAIN         main         examp1690
	 3309173529        1 TINT251      tint251      samp251
	 3309173529        2 TINT251      tint252      samp252
	 3309173529        3 TINT251      tint253      samp253
	 3309173529        4 TINT251      tint254      samp254
	```
	Enter the values for the database identifier (`dbid)` and instance number (`inst_num)`:
	```
	Enter value for dbid: 3309173529
	Using database id: 3309173529
	Enter instance numbers. Enter 'ALL' for all instances in an Oracle
	RAC cluster or explicitly specify list of instances (e.g., 1,2,3).
	Defaults to current instance.
	Enter value for inst_num: ALL
	Using instance number(s): ALL
	```
4. Specify the begin time in minutes before the system date:
	```
	Enter value for begin_time: -1:10
	```
	In this example, 1 hour and 10 minutes before the current time is selected.
5. Enter the duration in minutes that the report for which you want to capture ASH information from the begin time:
	```
	Enter value for duration: 10
	```
	In this example, the duration is set to 10 minutes.
6. Specify the slot width in seconds that will be used in the Activity Over Time section of the report:
	```
	Enter value for slot_width:
	```
	In this example, the default value is accepted. For more information about the Activity Over Time section and how to specify the slot width, see "Activity Over Time".
7. Follow the instructions as explained in the subsequent prompts and enter values for the following report targets:
	- `target_session_id`
		- `target_sql_id`
		- `target_wait_class`
		- `target_service_hash`
		- `target_module_name`
		- `target_action_name`
		- `target_client_id`
		- `target_plsql_entry`
8. Enter a report name, or accept the default report name:
	```
	Enter value for report_name: 
	Using the report name ashrpt_rac_0310_0131.txt
	```
	In this example, the default name is accepted and an ASH report named `ashrpt_rac_0310_0131` is generated. The report will gather ASH information on all instances belonging to the database with a database ID value of `3309173529` beginning from 1 hour and 10 minutes before the current time and ending at 1 hour before the current time.

### 5.3.9 Using Active Session History Reports

After generating an ASH report, you can review the contents to identify transient performance problems.

The contents of the ASH report are divided into the following sections:

- Top Events
- Load Profile
- Top SQL
- Top PL/SQL
- Top Java
- Top Sessions
- Top Objects/Files/Latches
- Activity Over Time

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/monitor.htm#RACAD987) for information about sections in the ASH report that are specific to Oracle Real Application Clusters (Oracle RAC)

#### 5.3.9.1 Top Events

The Top Events section describes the top wait events of the sampled session activity categorized by user, background, and priority. Use the information in this section to identify the wait events that may be the cause of the transient performance problem.

The Top Events section contains the following subsections:

- Top User Events
	This subsection lists the top wait events from user processes that accounted for the highest percentages of sampled session activity.
- Top Background Events
	This subsection lists the top wait events from backgrounds that accounted for the highest percentages of sampled session activity.
- Top Event P1/P2/P3
	This subsection lists the wait event parameter values of the top wait events that accounted for the highest percentages of sampled session activity, ordered by the percentage of total wait time (% Event). For each wait event, values in the P1 Value, P2 Value, P3 Value column correspond to wait event parameters displayed in the Parameter 1, Parameter 2, and Parameter 3 columns.

#### 5.3.9.2 Load Profile

The Load Profile section describes the load analyzed in the sampled session activity. Use the information in this section to identify the service, client, or SQL command type that may be the cause of the transient performance problem.

The Load Profile section contains the following subsections:

- Top Service/Module
	This subsection lists the services and modules that accounted for the highest percentages of sampled session activity.
- Top Client IDs
	This subsection lists the clients that accounted for the highest percentages of sampled session activity based on their client ID, which is the application-specific identifier of the database session.
- Top SQL Command Types
	This subsection lists the SQL command types, such as `SELECT` or `UPDATE`, that accounted for the highest percentages of sampled session activity.
- Top Phases of Execution
	This subsection lists the phases of execution, such as SQL, PL/SQL, and Java compilation and execution, that accounted for the highest percentages of sampled session activity.

#### 5.3.9.3 Top SQL

The Top SQL section describes the top SQL statements of the sampled session activity. Use this information to identify high-load SQL statements that may be the cause of the transient performance problem.

The Top SQL section contains the following subsections:

- Top SQL with Top Events
- Top SQL with Top Row Sources
- Top SQL Using Literals
- Top Parsing Module/Action
- Complete List of SQL Text

##### 5.3.9.3.1 Top SQL with Top Events

The Top SQL with Top Events subsection lists the SQL statements that accounted for the highest percentages of sampled session activity and the top wait events that were encountered by these SQL statements. The Sampled # of Executions column shows how many distinct executions of a particular SQL statement were sampled.

##### 5.3.9.3.2 Top SQL with Top Row Sources

The Top SQL with Top Row Sources subsection lists the SQL statements that accounted for the highest percentages of sampled session activity and their detailed execution plan information. You can use this information to identify which part of the SQL execution contributed significantly to the SQL elapsed time.

##### 5.3.9.3.3 Top SQL Using Literals

The Top SQL Using Literals subsection lists the SQL statements using literals that accounted for the highest percentages of sampled session activity. You should review the statements listed in this report to determine whether the literals can be replaced with bind variables.

##### 5.3.9.3.4 Top Parsing Module/Action

The Top Parsing Module/Action subsection lists the module and action that accounted for the highest percentages of sampled session activity while parsing the SQL statement.

##### 5.3.9.3.5 Complete List of SQL Text

The Complete List of SQL Text subsection displays the entire text of the Top SQL statements shown in this section.

#### 5.3.9.4 Top PL/SQL

The Top PL/SQL section lists the PL/SQL procedures that accounted for the highest percentages of sampled session activity. The PL/SQL Entry Subprogram column lists the application's top-level entry point into PL/SQL. The PL/SQL Current Subprogram column lists the PL/SQL subprogram being executed at the point of sampling. If the value of this column is `SQL`, then the % Current column shows the percentage of time spent executing SQL for this subprogram.

#### 5.3.9.5 Top Java

The Top Java section describes the top Java programs in the sampled session activity.

#### 5.3.9.6 Top Sessions

The Top Sessions section describes the sessions that were waiting for a particular wait event. Use this information to identify the sessions that accounted for the highest percentages of sampled session activity, which may be the cause of the transient performance problem.

The Top Sessions section contains the following subsections:

- Top Sessions
- Top Blocking Sessions
- Top Sessions Running PQs

##### 5.3.9.6.1 Top Sessions

The Top Session subsection lists the sessions that were waiting for a particular wait event that accounted for the highest percentages of sampled session activity.

##### 5.3.9.6.2 Top Blocking Sessions

The Top Blocking Sessions subsection lists the blocking sessions that accounted for the highest percentages of sampled session activity.

##### 5.3.9.6.3 Top Sessions Running PQs

The Top Sessions Running PQs subsection lists the sessions running parallel queries (PQs) that were waiting for a particular wait event, which accounted for the highest percentages of sampled session activity.

#### 5.3.9.7 Top Objects/Files/Latches

The Top Objects/Files/Latches section provides additional information about the most commonly-used database resources and contains the following subsections:

- Top DB Objects
- Top DB Files
- Top Latches

##### 5.3.9.7.1 Top DB Objects

The Top DB Objects subsection lists the database objects (such as tables and indexes) that accounted for the highest percentages of sampled session activity.

##### 5.3.9.7.2 Top DB Files

The Top DB Files subsection lists the database files that accounted for the highest percentages of sampled session activity.

##### 5.3.9.7.3 Top Latches

The Top Latches subsection lists the latches that accounted for the highest percentages of sampled session activity.

Latches are simple, low-level serialization mechanisms to protect shared data structures in the System Global Area (SGA). For example, latches protect the list of users currently accessing the database and the data structures describing the blocks in the buffer cache. A server or background process acquires a latch for a very short time while manipulating or looking at one of these structures. The implementation of latches is operating system-dependent, particularly regarding whether and how long a process waits for a latch.

#### 5.3.9.8 Activity Over Time

The Activity Over Time section is one of the most informative sections of the ASH report. This section is particularly useful for longer time periods because it provides in-depth details about activities and workload profiles during the analysis period. The Activity Over Time section is divided into 10 time slots. The size of each time slot varies based on the duration of the analysis period. The first and last slots are usually odd-sized. All inner slots are equally sized and can be compared to each other. For example, if the analysis period lasts for 10 minutes, then all time slots will 1 minute each. However, if the analysis period lasts for 9 minutes and 30 seconds, then the outer slots may be 15 seconds each and the inner slots will be 1 minute each.

Each of the time slots contains information regarding that particular time slot, as described in Table 5-2.

Table 5-2 Activity Over Time

| Column | Description |
| --- | --- |
| Slot Time (Duration) | Duration of the slot |
| Slot Count | Number of sampled sessions in the slot |
| Event | Top three wait events in the slot |
| Event Count | Number of ASH samples waiting for the wait event |
| % Event | Percentage of ASH samples waiting for wait events in the entire analysis period |

When comparing the inner slots, perform a skew analysis by identifying spikes in the Event Count and Slot Count columns. A spike in the Event Count column indicates an increase in the number of sampled sessions waiting for a particular event. A spike in the Slot Count column indicates an increase in active sessions, because ASH data is sampled from active sessions only and a relative increase in database workload. Typically, when the number of active session samples and the number of sessions associated with a wait event increases, the slot may be the cause of the transient performance problem.

To generate the ASH report with a user-defined slot size, run the `ashrpti.sql` script, as described in "Generating an ASH Report on a Specific Database Instance".