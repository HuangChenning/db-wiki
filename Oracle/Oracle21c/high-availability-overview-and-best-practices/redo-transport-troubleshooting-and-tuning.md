---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/redo-transport-troubleshooting-and-tuning.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Redo Transport Troubleshooting and Tuning

Oracle Data Guard redo transport performance is directly dependent on the performance of the primary and standby systems, the network that connects them, and the I/O subsystem.

For most Oracle Data Guard configurations, you should be able to achieve zero or minimal data loss by troubleshooting and tuning redo transport.

The guidance presented here assumes that the MAA configuration best practices are followed. As a prerequisite, ensure that the [Oracle Data Guard Configuration Best Practices](configure-and-deploy-oracle-data-guard.md) are implemented.

To improve transport holistically, leverage the data gathering and troubleshooting methodology described in the topics that follow, which guide you through gathering the necessary data to assess whether there is indeed a redo transport problem and what can be tuned to optimize redo transport throughput.

### Gather Topology Information

Understanding the topology of the Oracle Data Guard configuration, and its relevance to Data Guard performance, helps eliminate infrastructure weaknesses that are often incorrectly attributed to the Data Guard architecture.

Oracle recommends that you outline the following high-level architecture information.

- Describe the primary and standby database system (number of nodes in Oracle RAC cluster, CPUs and memory per database node, storage I/O system)
- Describe network topology connecting the primary and standby systems
	- Network components/devices in between primary and standby
		- Network bandwidth and latency

For standby databases with hardware and configuration that is symmetric with the primary database, and a reliable, well-tuned network with sufficient bandwidth, the transport lag should be less than 10 seconds and in most cases less than 1 second.

### Verify Transport Lag and Understand Redo Transport Configuration

To understand the difference between a transport lag and an apply lag, first recognize that a transport lag is the amount of redo that has not yet been received by the standby database. A transport lag impacts the Recovery Point Objective (RPO).

An apply lag indicates the amount of redo not yet applied to the standby and includes the transport lag. Therefore, an apply lag will be at least equal to the current transport lag and may be higher but never lower. An apply lag can indicate an impact on RPO, when there is a corresponding transport lag, and on Recovery Time Objective (RTO), absent a transport lag, because the unapplied redo is usually applied to the standby before the standby becomes a primary as a result of switchover or failover operation.

To determine if there is any lag on the standby database, and if this is a transport or apply lag, query the `V$DATAGUARD_STATS` view.

`SQL> select name,value,time_computed,datum_time from v$dataguard_stats where                 name=’%lag’;`

The `DATUM_TIME` column is the local time on the standby database when the datum used to compute the lag metric was received. Therefore, the lag reported is "as of" `DATUM_TIME`. It is assumed that the primary and standby maintain their connection, but in cases where the primary-standby connection is lost and `DATUM_TIME` does not change over multiple queries, the potential data loss cannot be calculated precisely, and should be assumed to be the difference between the `DATUM_TIME` from the query and current time on the standby database.

To obtain a histogram that shows the history of transport or apply lag values since the standby instance was last started, query the `V$STANDBY_EVENT_HISTOGRAM` view.

`SQL> select * from v$standby_event_histogram where name like '%lag' and count                 >0;`

To evaluate the transport or apply lag over a time period, take a snapshot of `V$STANDBY_EVENT_HISTOGRAM` at the beginning of the time period and compare that snapshot with one taken at the end of the time period.

```
SQL> col NAME format a10
SQL> select NAME,TIME,UNIT,COUNT,LAST_TIME_UPDATED from V$STANDBY_EVENT_HISTOGRAM where
 name like '%lag' and count >0 order by LAST_TIME_UPDATED;

NAME             TIME UNIT                  COUNT LAST_TIME_UPDATED

---------- ---------- ---------------- ---------- --------------------

transport lag      41 seconds                   3      01/05/2022 16:30:59

transport lag     245 seconds                   1      01/05/2022 16:31:02

transport lag     365 seconds                   2      01/05/2022 16:31:03

transport lag     451 seconds                   2      01/05/2022 16:31:04
```

If you observe an unacceptable redo transport lag, continue this redo transport investigation with Gather Information to Troubleshoot Transport Lag.

If you see no transport lag but an unacceptable redo apply lag, address the apply lag using the methodology in [Redo Apply Troubleshooting and Tuning](redo-apply-troubleshooting-and-tuning.md).

### Gather Information to Troubleshoot Transport Lag

Gather the following information and investigate the questions when an unacceptable redo transport lag is observed:

- When did the transport lag occur? Record the `V$DATAGUARD_STATS` and ` V$STANDBY_EVENT_HISTOGRAM` data to show when the lag started and how the lag is changing over time.
- Does the transport lag occur during a certain time period, such as daily at 12 midnight for daily batch operations, monthly during large batch operation, or quarterly during quarter end?
- Check the `LOG_ARCHIVE_DEST` setting for each enabled destination, and verify whether redo [COMPRESSION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=SBYDB-GUID-DD58C7C2-EE9D-4632-94C9-F6C652718006) or [ENCRYPTION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=SBYDB-GUID-72FD2420-BD1A-4121-94BE-3A3B8EFFA3A5) is enabled. Overall redo transport throughput can be negatively impacted because redo must be compressed or encrypted before sending, and then uncompressed or unencrypted upon receiving it on the standby. Verify if that change was recent, and if you can test disabling these setting attributes.
- Check the Oracle Net settings to evaluate if Oracle Net encryption is enabled. If Oracle Net encryption is enabled, when was it enabled and at what level? Oracle Net encryption can slow down redo throughput significantly because redo is encrypted before sending and unencrypted upon receiving the redo on the standby. Optionally, disable or reduce encryption levels to see if the redo transport lag reduces. See [Configuring Oracle Database Native Network Encryption and Data Integrity](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=DBSEG-GUID-7F12066A-2BA1-476C-809B-BB95A3F727CF).

### Compare Redo Generation Rate History on the Primary

There are cases where the primary database redo generation rate is exceptionally high for a short period of time, such as during large batch jobs, data loads, data pump operations, create table as select, PDML operations, or end of month, quarter, or year batch updates.

Obtain the redo generation history from the primary database and compare that to when the redo transport or redo apply lag started. Check if the redo generation rate is exceptionally high because of additional workloads, such as adding new pluggable databases or new application services. By doing so, additional tuning may be required to accommodate this additional load.

As part of troubleshooting, gather the following information or address the following questions:

- Gather daily history of primary database's redo generation rate using this query.
	```
	SQL> select trunc(completion_time) as "DATE", count(*) as "LOG SWITCHES",
	 round(sum(blocks*block_size)/1024/1024) as "REDO PER DAY (MB)" 
	from v$archived_log 
	where dest_id=1 
	group by trunc(completion_time) order by 1;
	```
- Gather the peak redo rate for each hour.
	```
	select begin_time,instance_number,metric_name,
	 round(value/1024/1024) "Max Rate in MB"
	from
	(select to_char(begin_time,'DD-MON-YYYY HH24')
	 begin_time,instance_number,metric_name,max(value) value
	from dba_hist_sysmetric_history
	where metric_name = 'Redo Generated Per Sec'
	and trunc(begin_time) >=trunc(sysdate-7)
	group by to_char(begin_time,'DD-MON-YYYY HH24'),instance_number,metric_name)
	 order by 1,3;
	```
	Optionally change the '7' to some other value to change the number of days in the output.
	The preferred query is `dba_hist_sysmetric_history` because it provides more precise information, but the retention is limited by AWR retention. If the dates you are looking for are not available form the previous query, gather per log redo generation rate using `v$archived_log` instead.
	```
	SQL> alter session set nls_date_format='YYYY/MM/DD HH24:MI:SS';
	SQL> select thread#,sequence#,blocks*block_size/1024/1024 MB,(next_time-first_time)*86400 sec,
	 blocks*block_size/1024/1024)/((next_time-first_time)*86400) "MB/s" from v$archived_log 
	where ((next_time-first_time)*86400<>0) 
	and first_time between to_date('2024/10/15 08:00:00','YYYY/MM/DD HH24:MI:SS') 
	and to_date('2024/11/15 11:00:00','YYYY/MM/DD HH24:MI:SS') 
	and dest_id=1 order by first_time;
	```
- Gather hourly snapshots of the redo generation rate from the Automatic Workload Repository (AWR) report 6 hours before the start of any redo or transport lag.
	By default, Oracle Database automatically generates snapshots once every hour; however, you may want to manually create snapshots to capture statistics at times different from those of the automatically generated snapshots. To view information about an existing snapshot, use the `DBA_HIST_SNAPSHOT` view.
	See [Creating Snapshots](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=TGDBA-GUID-70A79E56-18AB-4E85-9494-C0C8F02320AF) in the Oracle Database Performance Tuning Guide for complete information about AWR and generating snapshots and AWR reports.
- Is this primary redo generation rate exceptionally high compared to prior history?
- If possible, determine the workload that corresponds to the high redo generation rate and evaluate whether it's transient or if it can be tuned.
	For example, for large purge operations, consider truncate or drop partition operations to reduce the redo generation volumes.

### Evaluate the Transport Network and Tune

Redo transport consists of the primary database instance background process sending redo to the standby database background process. You can evaluate if the network is optimized for Oracle Data Guard redo transport.

If asynchronous redo transport is configured, redo data is streamed to the standby in large packets asynchronously. To tune asynchronous redo transport over the network, you need to optimize a single process network throughput.

If synchronous redo transport is configured, each redo write must be acknowledged by the primary and standby databases before proceeding to the next redo write. You can optimize standby synchronous transport by using the `FASTSYNC` attribute as part of the `LOG_ARCHIVE_DEST` setting, but higher network latency (for example, more than 5 milliseconds) impacts overall redo transport throughput.

Before you continue, see [Assessing and Optimizing Network Performance](plan-oracle-data-guard-deployment.md) first to:

- Assess whether you have sufficient network bandwidth to support the primary's redo generation rate
- Determine optimal TCP socket buffer sizes to tune redo transport
- Tune operating system limits on socket buffer sizes to tune redo transport
- Determine optimal MTU setting for redo write size
- Tune MTU to increase network throughput for redo transport

If network configuration is tuned, evaluate if the transport lag (refer to Verify Transport Lag and Understand Redo Transport Configuration) is reducing to acceptable levels. If that's the case, you have met your goals and you can stop. Otherwise continue with the rest of the rest of tuning and troubleshooting section.

### Gather and Monitor System Resources

Gather Oracle Linux OSwatcher or Oracle Exadata Exawatcher data to analyze system resources.

OSWatcher (oswbb) is a collection of UNIX shell scripts intended to collect and archive operating system and network metrics to aid support in diagnosing performance issues. As a best practice, you should install and run OSWatcher on every node that has a running Oracle instance. In the case of a performance issue, Oracle support can use this data to help diagnose performance problems which may outside the database.

You can download OSWatcher from [OSWatcher (Doc ID 301137.1)](https://support.oracle.com/rs?type=doc&id=301137.1).

ExaWatcher is a utility that collects performance data on the storage servers and database servers on an Exadata system. The data collected includes operating system statistics, such as iostat, cell statistics (cellsrvstat), and network statistics.

See [Using ExaWatcher Charts to Monitor Exadata Database Machine Performance](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=DBMMN-GUID-5AEB3139-333D-453F-91D6-8EB09CB6E6EB) in the Oracle Exadata Database Machine Maintenance Guide for more information.

### Tune to Meet Data Guard Resource Requirements

Redo transport can be impacted if:

- Primary or standby database is completely CPU bound
- The `ASYNC` process (TT0n) is CPU bound, that is, using over 70% of a CPU
- Primary or standby database I/O system is saturated
- Network topology can't support the redo generation rates

Evaluate whether the primary database system has:

- Sufficient CPU utilization for Log Writer Process (LGWR) to post foregrounds efficiently
- Sufficient I/O bandwidth so local log writes maintain low I/O latency during peak rates
- Network interfaces that can handle peak redo rate volumes combined with any other network activity across the same interface
- Automatic Workload Repository (AWR), Active Session History (ASH), and OSwatcher or Exawatcher data gathered from the primary database for tuning and troubleshooting

Evaluate whether the standby database system has:

- Sufficient CPU utilization for the remote file server (RFS), the Oracle Data Guard process that receives redo at the standby database, to efficiently write to standby redo logs
- Sufficient I/O bandwidth to enable local log writes to maintain low I/O latency during peak rates
- A network interface that can receive the peak redo rate volumes combined with any other network activity across the same interface
- AWR, ASH, and OSwatcher or Exawatcher data gathered from the standby database for tuning and troubleshooting

Note:

The top issue encountered with the standby database is poor standby log write latency because of insufficient I/O bandwidth. This problem can be mitigated by using Data Guard Fast Sync.

If system configuration is tuned and the above resource constraints are removed, evaluate if the transport lag (refer to Verify Transport Lag and Understand Redo Transport Configuration) is reducing to acceptable levels. If that's the case, you have met your goals.

### Advanced Troubleshooting: Determining Network Time with Asynchronous Redo Transport

Before you proceed, first see [Assessing and Optimizing Network Performance](plan-oracle-data-guard-deployment.md).

Given enough resources, especially network bandwidth, asynchronous redo transport can maintain pace with very high workloads. In cases where resources are constrained, asynchronous redo transport can begin to fall behind resulting in a growing transport lag on the standby database.

Asynchronous redo transport (ASYNC) transmits redo data asynchronously with respect to transaction commitment. A transaction can commit without waiting for an acknowledgment that the redo generated by that transaction was successfully transmitted to a remote standby database. With ASYNC transport, the primary database Log Writer Process (LGWR) continues to acknowledge commit success even if limited bandwidth prevents the redo of previous transactions from being sent to the standby database immediately (picture a sink filling with water faster than it can drain).

ASYNC uses a TT0n process to transmit redo directly from the log buffer of the primary database. If the TT0n process is unable to keep pace and the log buffer is recycled before the redo can be transmitted to the standby database, then the TT0n process automatically transitions to reading and sending from the online redo log file (ORL) on disk. Once TT0n transmission has caught up with current redo generation, it automatically transitions back to reading and sending directly from the log buffer.

In cases in which there are two or more log switches before the TT00 has completed sending the original ORL, the TT00 will still transition back to reading the contents of the current online log file. Any ORLs that were archived in between the original ORL and the current ORL are automatically transmitted using Oracle Data Guard’s redo gap resolution process.

Sufficient resources, such as network bandwidth, CPU, memory, and log file I/O on both the primary and standby databases are critical to the performance of an asynchronous Data Guard configuration.

To determine which resource is constraining asynchronous transport, use krsb stats which can be enabled by setting event 16421 on both the primary and standby databases:

```
alter session set events ‘16421 trace name context forever, level 3’;
```

This event is very lightweight and won't affect performance of the primary or standby database.

This dynamic event should be set on all primary and standby instances, and it will write statistics into the TT00 or remote file server (RFS) trace file when shipping for a given sequence has completed. Looking in the trace file, you will see the krsb\_end stats at the beginning and end of the file. The stats at the end of the file will provide insight into where asynchronous shipping was spending time.

Note:

Identify the async transport process and the tracefile:
```
SELECT DP.NAME, DP.PID OSPID, P.TRACEFILE FROM V$DATAGUARD_PROCESS DP, V$PROCESS P
 WHERE DP.PID=P.SPID AND DP.ROLE LIKE 'async%';
```

For example:

```
krsb_end: Begin stats dump for T-1.S-593
  max number of buffers in use             10
  Operation elapsed time (micro seconds)   474051333
  File transfer time (micro seconds)       474051326
  Network Statistics
   LOG_ARCHIVE_DEST_2 : OCI REQUEST
    Total count  : OCI REQUEST             2748
    Total time   : OCI REQUEST             81374
    Average time : OCI REQUEST             29
   LOG_ARCHIVE_DEST_2 : NETWORK SEND
    Total count  : NETWORK SEND            2748
    Total time   : NETWORK SEND            286554724
    Average time : NETWORK SEND            104277
    Total data buffers queued              9644
    Total data buffers completed           9644
    Total bytes written                    9885272064
    Total bytes completed synchronously    9885272064
    Average network send size (blocks)     7025
    Average network send buffers           3.51
    Average buffer turnaround time         240889
    Throughput (MB/s)                      19.89
   Total network layer time                286636098
   Percentage of time in network           60.47
  Disk Statistics
    Total count  : DISK READ               11531
    Total time   : DISK READ               12335132
    Average time : DISK READ               1069
    Read-ahead blocks                      14151680
    Log buffer blocks                      266915
    Disk stall blocks                      4888576
    Total count  : BUFFER RELEASE          9643
    Total time   : BUFFER RELEASE          7229
    Average time : BUFFER RELEASE          0
   Total disk layer time                   12342361
   Percentage of time in disk layer        2.60
  Data Guard Processing Statistics
    Total count  : SLEEP                   198
    Total time   : SLEEP                   172351312
    Average time : SLEEP                   870461
   Total DG layer time                     175072867
   Percentage of time in DG layer          36.93
  Remote Server-Side Network Statistics
   LOG_ARCHIVE_DEST_2 : NETWORK GET
    Total count  : NETWORK GET             8242
    Total bytes  : NETWORK GET             9885272064
    Total time   : NETWORK GET             453233790
    Average time : NETWORK GET             54990
   Total server-side network layer time    453233790
   Percentage of time in network           95.61
  Remote Server-Side Disk Statistics
   LOG_ARCHIVE_DEST_2 : DISK WRITE
    Total count  : DISK WRITE              9644
    Total time   : DISK WRITE              8731303
    Average time : DISK WRITE              905
   LOG_ARCHIVE_DEST_2 : DISK NOSTALL REAP
    Total count  : DISK NOSTALL REAP       9644
    Total time   : DISK NOSTALL REAP       579066
    Average time : DISK NOSTALL REAP       60
   LOG_ARCHIVE_DEST_2 : BUFFER GET
    Total count  : BUFFER GET              9644
    Total time   : BUFFER GET              3607
    Average time : BUFFER GET              0
   Total server-side disk layer time       9313976
   Percentage of time in disk layer        1.96
  Remote Server-Side Data Guard Processing Statistics
   LOG_ARCHIVE_DEST_2 : PUBLISH RTA BOUNDARY
    Total count  : PUBLISH RTA BOUNDARY    8948
    Total time   : PUBLISH RTA BOUNDARY    3665841
    Average time : PUBLISH RTA BOUNDARY    409
   LOG_ARCHIVE_DEST_2 : VALIDATE BUFFER
    Total count  : VALIDATE BUFFER         9644
    Total time   : VALIDATE BUFFER         1403088
    Average time : VALIDATE BUFFER         145
   Total Server-Side DG layer time         11503560
   Percentage of time in DG layer          2.43
krsb_end: End stats dump
```

The above output comes from a test run where a transport lag is just beginning to occur. You can observe a lag due to network congestion increase, and the time waiting on the network layer increases above 50%. If a transport lag is the result of either compression or encryption, the percentage of time spent in the Data Guard layer would become the majority.

When looking at krsb stats (Note all times in the output are in microseconds):

Start by looking where the most time is spent on the client side, be that network, disk or Data Guard.

Network Statistics

- 'Average time: NETWORK SEND' - Higher values here (more than 1 microsecond) could indicate network encryption or redo compression is enabled as it is taking longer to put the packets on the wire.
- Total bytes completed synchronously / Total bytes written - If the quotient is less than 90%, more TCP socket buffers would likely be helpful. This would require changing the `tcp_rmem and tcp_wmem` max values and restarting transport.

Disk Statistics

- Log buffer blocks - The best case scenario is when all the blocks are read from the log buffer (that is, memory) rather than disk (for example, read-ahead or disk stalls). If that is not the case, increasing the size of the log\_buffer parameter on the primary may help improve transport. Changing the `log_buffer` parameter requires a bounce of the database (Oracle RAC Rolling supported).
	Note that a larger log buffer simply improves the chance that the next redo to be read by the async process will be in the log buffer. Under heavy, sustained workloads eventually reads are likely to go to disk, especially when there is another factor slowing down transport (such as encryption or latency).
- If there are a high percentage of 'Disk stall blocks', increase the value of `_log_archive_buffers` to 256. Changing this value requires a database restart to take effect (Oracle RAC Rolling supported).

Data Guard Statistics

- If most of the time spent is in Data Guard statistics and there is a transport lag, there may be a resource issue on the system as a whole (such as CPU or memory shortage). Review ExaWatcher or OSWatcher for the system for system bottlenecks.

To disable krsb stats set event 16421 to level 1:

```
alter session set events ‘16421 trace name context forever, level 1’;
```

### Disable Oracle Net Encryption for Redo Transport Only

Oracle Net encryption can have a negative impact on redo transport at higher redo generation rates. Encryption increases the CPU utilization of the send an receive processes which may result in a CPU bound process.

There may be cases where Oracle Net encryption is required for application client connections but it is acceptable to the business to disable encryption for redo transport. For example, when the primary and standby are in the same data center or the full transport path is protected by customer firewalls. In this case it is possible to disable Oracle Net encryption just for redo transport by changing the net service descriptor.

By including the `SECURITY` clause below in the descriptor for the net service name of the standby database Oracle Net encryption is disable only for connections using this alias. The same setting should be added to the primary database entry on the standby database cluster.

```
(SECURITY=(ENCRYPTION_CLIENT=REJECTED))
```

Example:

```
net_service_name= 
(DESCRIPTION= 
  (ADDRESS_LIST= 
    (ADDRESS=(PROTOCOL=tcp)(HOST=<standby scan listener>)(PORT=1521)) 
    (CONNECT_DATA= 
      (SERVICE_NAME=<standby database service>)
    ) 
    (SECURITY= (SECURITY=(ENCRYPTION_CLIENT=REJECTED))
  )
)
```

All other connections to or from the database are governed by the `sqlnet.ora` parameter settings. Only connections using this net service name will have Oracle Net encryption disabled.

### Tuning and Troubleshooting Synchronous Redo Transport

Before you proceed, first see [Assessing and Optimizing Network Performance](plan-oracle-data-guard-deployment.md).

The following topics describe how to assess synchronous redo transport.

- Understanding How Synchronous Transport Ensures Data Integrity
- Assessing Performance in a Synchronous Redo Transport Environment
- [Why the Log File Sync Wait Event is Misleading](https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/redo-transport-troubleshooting-and-tuning.html#GUID-A502EACD-3B5C-4B1D-9D8C-21F30A338102 "Typically, the \"log file sync\" wait event on the primary database is the first place administrators look when they want to assess the impact of enabling synchronous redo transport (SYNC).")
- Understanding What Causes Outliers
- Effects of Synchronous Redo Transport Remote Writes
- Example of Synchronous Redo Transport Performance Troubleshooting

#### Understanding How Synchronous Transport Ensures Data Integrity

The following algorithms ensure data consistency in an Oracle Data Guard synchronous redo transport configuration.

- Log Writer Process (LGWR) redo write on the primary database online redo log and the Data Guard Network Services Server (NSS) redo write to standby redo log are identical.
- The Data Guard Managed Recovery Process (MRP) at the standby database cannot apply redo unless the redo has been written to the primary database online redo log, with the only exception being during a Data Guard failover operation (when the primary is gone).
	In addition to shipping redo synchronously, NSS and LGWR exchange information regarding the safe redo block boundary that standby recovery can apply up to from its standby redo logs (SRLs). This prevents the standby from applying redo it may have received, but which the primary has not yet acknowledged as committed to its own online redo logs.

The possible failure scenarios include:

- If primary database LGWR cannot write to online redo log, then LGWR and the instance crash. Instance or crash recovery will recover to the last committed transaction in the online redo log and roll back any uncommitted transactions. The current log will be completed and archived.
- On the standby, the partial standby redo log completes with the correct value for the size to match the corresponding online redo log. If any redo blocks are missing from the standby redo log, those are shipped over (without reshipping the entire redo log).
- If the primary database crashes resulting in an automatic or manual zero data loss failover, then part of the Data Guard failover operation will do "terminal recovery" and read and recover the current standby redo log.
	Once recovery finishes applying all of the redo in the standby redo logs, the new primary database comes up and archives the newly completed log group. All new and existing standby databases discard any redo in the online redo logs, flashback to a consistent system change number (SCN), and only apply the archives coming from the new primary database. Once again the Data Guard environment is in sync with the (new) primary database.

#### Assessing Performance in a Synchronous Redo Transport Environment

When assessing performance in an Oracle Data Guard synchronous redo transport environment (SYNC) it is important that you know how the different wait events relate to each other. The impact of enabling synchronous redo transport varies between applications.

To understand why, consider the following description of work the Log Writer Process (LGWR) performs when a commit is issued.

1. Foreground process posts LGWR for commit ("log file sync" starts). If there are concurrent commit requests queued, LGWR will batch all outstanding commit requests together resulting in a continuous strand of redo.
2. LGWR waits for CPU.
3. LGWR starts redo write ("redo write time" starts).
4. For Oracle RAC database, LGWR broadcasts the current write to other instances.
5. After preprocessing, if there is a SYNC standby, LGWR starts the remote write (“SYNC remote write” starts).
6. LGWR issues local write ("log file parallel write").
7. If there is a SYNC standby, LGWR waits for the remote write to complete.
8. After checking the I/O status, LGWR ends "redo write time / SYNC remote write".
9. For Oracle RAC database, LGWR waits for the broadcast ack.
10. LGWR updates the on-disk SCN.
11. LGWR posts the foregrounds.
12. Foregrounds wait for CPU.
13. Foregrounds ends "log file sync".

Use the following approaches to assess performance.

- For batch loads, the most important factor is to monitor the elapsed time, because most of these processes must be completed in a fixed period of time. The database workloads for these operations are very different than the normal OLTP workloads. For example, the size of the writes can be significantly larger, so using log file sync averages does not give you an accurate view or comparison.
- For OLTP workloads, monitor the volume of transactions per second (from Automatic Workload Repository (AWR)) and the redo rate (redo size per second) from the AWR report. This information gives you a clear picture of the application throughput and how it is impacted by enabling synchronous redo transport.

#### Why the Log File Sync Wait Event is Misleading

Typically, the "log file sync" wait event on the primary database is the first place administrators look when they want to assess the impact of enabling synchronous redo transport (SYNC).

If the average log file sync wait before enabling SYNC was 3ms, and after enabling SYNC was 6ms, then the assumption is that SYNC impacted performance by one hundred percent. Oracle does not recommend using log file sync wait times to measure the impact of SYNC because the averages can be very deceiving, and the actual impact of SYNC on response time and throughput may be much lower than the event indicates.

When a user session commits, the Log Writer Process (LGWR) will go through the process of getting on the CPU, submitting the I/O, waiting for the I/O to complete, and then getting back on the CPU to post foreground processes that the commit has completed. This whole time period is covered by the log file sync wait event. While LGWR is performing its work there are, in most cases, other sessions committing that must wait for LGWR to finish before processing their commits. The size and number of sessions waiting are determined by how many sessions an application has, and how frequently those sessions commit. This batching up of commits is generally referred to as application concurrency.

For example, assume that it normally takes 0.5ms to perform log writes (log file parallel write), 1ms to service commits (log file sync), and on average you are servicing 100 sessions for each commit. If there was an anomaly in the storage tier, and the log write I/O for one commit took 20ms to complete, then you could have up to 2,000 sessions waiting on log file sync, while there would only be 1 long wait attributed to log file parallel write. Having a large number of sessions waiting on one long outlier can greatly skew the log file sync averages.

The output from `V$EVENT_HISTOGRAM` for the log file sync wait event for a particular period in time is shown in the following table.

Table 17-1 V$EVENT\_HISTOGRAM Output for the Log File Sync Wait Event

| Milliseconds | Number of Waits | Percent of Total Waits |
| --- | --- | --- |
| 1 | 17610 | 21.83% |
| 2 | 43670 | 54.14% |
| 4 | 8394 | 10.41% |
| 8 | 4072 | 5.05% |
| 16 | 4344 | 5.39% |
| 32 | 2109 | 2.61% |
| 64 | 460 | 0.57% |
| 128 | 6 | 0.01% |

The output shows that 92% of the log file sync wait times are less than 8ms, with the vast majority less than 4ms (86%). Waits over 8ms are outliers and only make up 8% of wait times overall, but because of the number of sessions waiting on those outliers (because of batching of commits) the averages get skewed. The skewed averages are misleading when log file sync average waits times are used as a metric for assessing the impact of SYNC.

#### Understanding What Causes Outliers

Any disruption to the I/O on the primary or standby databases, or spikes in network latency, can cause high log file sync outliers with synchronous redo transport. You can see this effect when the standby system's I/O subsytem is inferior to that of the primary system.

Often administrators host multiple databases such as dev and test on standby systems, which can impair I/O response. It is important to monitor I/O using iostat to determine if the disks reach maximum IOPS, because this affects the performance of SYNC writes.

Frequent log switches are significant cause of outliers. Consider what occurs on the standby when a log switch on the primary occurs, as follows.

1. Remote file server (RFS) process on the standby must finish updates to the standby redo log header.
2. RFS then switches into a new standby redo log with additional header updates.
3. Switching logs forces a full checkpoint on the standby.
	This causes all dirty buffers in the buffer cache to be written to disk, causing a spike in write I/O. In a non-symmetric configuration where the standby storage subsystem does not have the same performance as the primary database, this results in higher I/O latency.
4. The previous standby redo log must be archived, increasing both read and write I/O.

#### Effects of Synchronous Redo Transport Remote Writes

When you enable synchronous redo transport (SYNC), you introduce a remote write (remote file server (RFS) write to a standby redo log) in addition to the normal local write for commit processing.

This remote write, depending on network latency and remote I/O bandwidth, can make commit processing time increase. Because commit processing takes longer, you observe more sessions waiting on the Log Writer Process (LGWR) to finish its work and begin work on the commit request, that is, application concurrency has increased. You can observe increased application concurrency by analyzing database statistics and wait events.

Consider the example in the following table.

Table 17-2 Affect of Sync Transport Increasing Application Concurrency

| SYNC | Redo Rate | Network Latency | TPS from AWR | log file sync average (ms) | log file parallel write average (ms) | RFS random I/O | SYNC remote write average (ms) | Redo write size (KB) | Redo writes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Defer | 25MB | 0 | 5,514.94 | 0.74 | 0.47 | NA | NA | 10.58 | 2,246,356 |
| Yes | 25MB | 0 | 5,280.20 | 2.6 | .51 | .65 | .95 | 20.50 | 989,791 |
| Impact | 0 | \- | \-4% | +251% | +8.5% | NA | NA | +93.8% | \-55.9% |

In the above example, enabling SYNC reduced the number of redo writes, but increased the size of each redo write. Because the size of the redo write increased, you can expect the time spent doing the I/O (both local and remote) to increase. The log file sync wait time is higher because there is more work per wait.

However, at the application level, the impact on the transaction rate or the transaction response time might change very little as more sessions are serviced for each commit. This is why it is important to measure the impact of SYNC at the application level, and not depend entirely on database wait events. It is also a perfect example of why log file sync wait event is a misleading indicator of the actual impact SYNC has on the application.

#### Example of Synchronous Redo Transport Performance Troubleshooting

To look at synchronous redo transport performance, calculate the time spent for local redo writes latency, average redo write size for each write, and overall redo write latency, as shown here.

Use the following wait events to do the calculations.

- local redo write latency = 'log file parallel write'
- remote write latency = ‘SYNC remote write’
- average redo write size per write = ‘redo size’ / ‘redo writes’
- average commit latency seen by foregrounds = 'log file sync'

Statistics from an Automatic Work Repository (AWR) report on an Oracle database are provided in the following table. Synchronous redo transport (SYNC) was enabled to a local standby with a 1ms network latency to compare the performance impact to a baseline with SYNC disabled.

Table 17-3 Assessing Synchronous Redo Transport Performance with Oracle Database

| Metric | Baseline (No SYNC) | SYNC | Impact |
| --- | --- | --- | --- |
| redo rate (MB/s) | 25 | 25 | no change |
| log file sync | 0.68 | 4.60 | +576% |
| log file parallel write average (ms) | 0.57 | 0.62 | +8.8% |
| TPS | 7,814.92 | 6224.03 | \-20.3% |
| RFS random I/O | NA | 2.89 | NA |
| SYNC remote write average (ms) | NA | 3.45 | NA |
| redo writes | 2,312,366 | 897,751 | \-61,2% |
| redo write size (KB) | 10.58 | 20.50 | +93.8% |

In the above example observe that log file sync waits averages increased dramatically after enabling SYNC. While the local writes remained fairly constant, the biggest factor in increasing log file sync was the addition of the SYNC remote write. Of the SYNC remote write the network latency is zero, so focusing on the remote write into the standby redo log shows an average time of 2.89ms. This is an immediate red flag given that the primary and standby were using the same hardware, and the SYNC remote write average time should be similar to the primary's log file parallel write average time.

In the above example, the standby redo logs have multiple members, and they are placed in a slower performing disk group. After reducing the standby redo logs to a single member, and placing them in a fast disk group, you can see results such as those shown in the following table.

Table 17-4 SYNC Performance After Reducing Standby Redo Logs to a Single Member and Placing on a Fast Disk Group

| Metric | Baseline (No SYNC) | SYNC | Impact |
| --- | --- | --- | --- |
| redo rate (MB/s) | 25 | 25 | no change |
| log file sync | 0.67 | 1.60 | +139% |
| log file parallel write | 0.51 | 0.63 | +23.5% |
| TPS | 7714.36 | 7458.08 | \-3.3% |
| RFS random I/O | NA | .89 | NA |
| SYNC remote write average (ms) | NA | 1.45 | NA |
| redo writes | 2,364,388 | 996,532 | \-57.9% |
| redo write size (KB) | 10.61 | 20.32 | +91.5% |