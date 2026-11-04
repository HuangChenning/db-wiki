---
title: Troubleshooting Oracle Clusterware
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/troubleshoot.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## H Troubleshooting Oracle Clusterware

This appendix introduces monitoring the Oracle Clusterware environment and explains how you can enable dynamic debugging to troubleshoot Oracle Clusterware processing, and enable debugging and tracing for specific components and specific Oracle Clusterware resources to focus your troubleshooting efforts.

This appendix includes the following topics:

## Monitoring Oracle Clusterware

You can use Oracle Enterprise Manager to monitor the Oracle Clusterware environment. When you log in to Oracle Enterprise Manager using a client browser, the Cluster Database Home page appears where you can monitor the status of both Oracle Clusterware environments. Monitoring can include such things as:

- Notification if there are any VIP relocations
- Status of the Oracle Clusterware on each node of the cluster using information obtained through the Cluster Verification Utility (`cluvfy`)
- Notification if node applications (nodeapps) start or stop
- Notification of issues in the Oracle Clusterware alert log for the Oracle Cluster Registry, voting disk issues (if any), and node evictions

The Cluster Database Home page is similar to a single-instance Database Home page. However, on the Cluster Database Home page, Oracle Enterprise Manager displays the system state and availability. This includes a summary about alert messages and job activity, and links to all the database and Automatic Storage Management (Oracle ASM) instances. For example, you can track problems with services on the cluster including when a service is not running on all of the preferred instances or when a service response time threshold is not being met.

You can use the Oracle Enterprise Manager Interconnects page to monitor the Oracle Clusterware environment. The Interconnects page shows the public and private interfaces on the cluster, the overall throughput on the private interconnect, individual throughput on each of the network interfaces, error rates (if any) and the load contributed by database instances on the interconnect, including:

- Overall throughput across the private interconnect
- Notification if a database instance is using public interface due to misconfiguration
- Throughput and errors (if any) on the interconnect
- Throughput contributed by individual instances on the interconnect

All of this information also is available as collections that have a historic view. This is useful with cluster cache coherency, such as when diagnosing problems related to cluster wait events. You can access the Interconnects page by clicking the Interconnect tab on the Cluster Database home page.

Also, the Oracle Enterprise Manager Cluster Database Performance page provides a quick glimpse of the performance statistics for a database. Statistics are rolled up across all the instances in the cluster database in charts. Using the links next to the charts, you can get more specific information and perform any of the following tasks:

- Identify the causes of performance issues.
- Decide whether resources must be added or redistributed.
- Tune your SQL plan and schema for better optimization.
- Resolve performance issues

The charts on the Cluster Database Performance page include the following:

- Chart for Cluster Host Load Average: The Cluster Host Load Average chart in the Cluster Database Performance page shows potential problems that are outside the database. The chart shows maximum, average, and minimum load values for available nodes in the cluster for the previous hour.
- Chart for Global Cache Block Access Latency: Each cluster database instance has its own buffer cache in its System Global Area (SGA). Using Cache Fusion, Oracle RAC environments logically combine each instance's buffer cache to enable the database instances to process data as if the data resided on a logically combined, single cache.
- Chart for Average Active Sessions: The Average Active Sessions chart in the Cluster Database Performance page shows potential problems inside the database. Categories, called wait classes, show how much of the database is using a resource, such as CPU or disk I/O. Comparing CPU time to wait time helps to determine how much of the response time is consumed with useful work rather than waiting for resources that are potentially held by other processes.
- Chart for Database Throughput: The Database Throughput charts summarize any resource contention that appears in the Average Active Sessions chart, and also show how much work the database is performing on behalf of the users or applications. The Per Second view shows the number of transactions compared to the number of logons, and the amount of physical reads compared to the redo size for each second. The Per Transaction view shows the amount of physical reads compared to the redo size for each transaction. Logons is the number of users that are logged on to the database.

In addition, the Top Activity drilldown menu on the Cluster Database Performance page enables you to see the activity by wait events, services, and instances. Plus, you can see the details about SQL/sessions by going to a prior point in time by moving the slider on the chart.

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm)

This section includes the following topics:

- Cluster Health Monitor
- OCLUMON Command Reference
- Alert Messages Using Diagnostic Record Unique IDs

### Cluster Health Monitor

The Cluster Health Monitor (CHM) stores real-time operating system metrics in the CHM repository that you can use for later triage with the help of Oracle Support should you have cluster issues.

This section includes the following CHM topics:

- CHM Services
- CHM Repository
- Collecting CHM Data

#### CHM Services

CHM consists of the following services:

- System Monitor Service
- Cluster Logger Service

System Monitor Service

There is one system monitor service on every node. The system monitor service (`osysmond`) is the monitoring and operating system metric collection service that sends the data to the cluster logger service. The cluster logger service receives the information from all the nodes and persists in a CHM repository-based database.

Cluster Logger Service

There is one cluster logger service (`ologgerd`) on only one node in a cluster and another node is chosen by the cluster logger service to house the standby for the master cluster logger service. If the master cluster logger service fails (because the service is not able come up after a fixed number of retries or the node where the master was running is down), the node where the standby resides takes over as master and selects a new node for standby. The master manages the operating system metric database in the CHM repository and interacts with the standby to manage a replica of the master operating system metrics database.

#### CHM Repository

The CHM repository, by default, resides within the Grid Infrastructure home and requires 1 GB of disk space per node in the cluster. You can adjust its size and location, and Oracle supports moving it to shared storage. You manage the CHM repository with OCLUMON.

#### Collecting CHM Data

You can collect CHM data from any node in the cluster by running the `Grid_home` `/bin/diagcollection.pl` script on the node.

Notes:

- Oracle recommends that, when you run the `Grid_home` `/bin/diagcollection.pl` script to collect CHM data, you run the script on all nodes in the cluster to ensure gathering all of the information needed for analysis.
- You must run this script as a privileged user.

To run the data collection script on only the node where the cluster logger service is running:

1. Run the following command to identify the node running the cluster logger service:
	```
	$ Grid_home/bin/oclumon manage -get master
	```
2. Run the following command as a privileged user on the cluster logger service node to collect all the available data in the Grid Infrastructure Management Repository:
	```
	# Grid_home/bin/diagcollection.pl
	```
	The `diagcollection.pl` script creates a file called `chmosData_` `host_name_time_stamp``.tar.gz`, similar to the following:
	```
	chmosData_stact29_20121006_2321.tar.gz
	```

To limit the amount of data you want collected:

```
# Grid_home/bin/diagcollection.pl -collect -chmos
   -incidenttime inc_time -incidentduration duration
```

In the preceding command, the format for the `-incidenttime` parameter is `MM/DD/YYYY24HH:MM:SS` and the format for the `-incidentduration` parameter is `HH:MM`. For example:

```
# Grid_home/bin/diagcollection.pl -collect -crshome
   Grid_home -chmoshome Grid_home -chmos -incidenttime 07/14/201201:00:00
   -incidentduration 00:30
```

### OCLUMON Command Reference

The OCLUMON command-line tool is included with CHM and you can use it to query the CHM repository to display node-specific metrics for a specified time period. You can also use `oclumon` to query and print the durations and the states for a resource on a node during a specified time period. These states are based on predefined thresholds for each resource metric and are denoted as red, orange, yellow, and green, indicating decreasing order of criticality. For example, you can query to show how many seconds the CPU on a node named `node1` remained in the RED state during the last hour. You can also use OCLUMON to perform miscellaneous administrative tasks, such as changing the debug levels, querying the version of CHM, and changing the metrics database size.

This section details the following OCLUMON commands:

- `oclumon debug`
- `oclumon dumpnodeview`
- `oclumon manage`
- `oclumon version`

#### oclumon debug

Use the `oclumon debug` command to set the log level for the CHM services.

Syntax

```
oclumon debug [log daemon module:log_level] [version]
```

Parameters

Table H-1 oclumon debug Command Parameters

| Parameter | Description |
| --- | --- |
| ``` log daemon module:log_level ``` | Use this option change the log level of daemons and daemon modules. Supported daemons are:     `osysmond`   `ologgerd`   `client`   `all`  Supported daemon modules are:     `osysmond`: `CRFMOND`, `CRFM`, and `allcomp`   `ologgerd`: `CRFLOGD`, `CRFLDBDB`, `CRFM`, and `allcomp`   `client`: `OCLUMON`, `CRFM`, and `allcomp`   `all`: `CRFM,allcomp`  Supported `log_level` values are `0`, `1`, `2`, and `3`. |
| ``` version ``` | Use this option to display the versions of the daemons. |

Example

The following example sets the log level of the system monitor service (`osysmond`):

```
$ oclumon debug log osysmond CRFMOND:3
```

#### oclumon dumpnodeview

Use the `oclumon dumpnodeview` command to view log information from the system monitor service in the form of a node view.

A node view is a collection of all metrics collected by CHM for a node at a point in time. CHM attempts to collect metrics every second on every node. Some metrics are static while other metrics are dynamic.

A node view consists of seven views when you display verbose output:

- SYSTEM: Lists system metrics such as CPU COUNT, CPU USAGE, and MEM USAGE
- TOP CONSUMERS: Lists the top consuming processes in the following format:
	```
	metric_name: 'process_name(process_identifier) utilization'
	```
- PROCESSES: Lists process metrics such as PID, name, number of threads, memory usage, and number of file descriptors
- DEVICES: Lists device metrics such as disk read and write rates, queue length, and wait time per I/O
- NICS: Lists network interface card metrics such as network receive and send rates, effective bandwidth, and error rates
- FILESYSTEMS: Lists file system metrics, such as total, used, and available space
- PROTOCOL ERRORS: Lists any protocol errors

You can generate a summary report that only contains the SYSTEM and TOP CONSUMERS views.

"Metric Descriptions" lists descriptions for all the metrics associated with each of the views in the preceding list.

Note:

Metrics displayed in the TOP CONSUMERS view are described in Table H-4, "PROCESSES View Metric Descriptions".

Example H-1 shows an example of a node view.

Syntax

```
oclumon dumpnodeview [[-allnodes] | [-n node1 node2] [-last "duration"] | 
[-s "time_stamp" -e "time_stamp"] [-v] [-warning]] [-h]
```

Parameters

Table H-2 oclumon dumpnodeview Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -allnodes ``` | Use this option to dump the node views of all the nodes in the cluster. |
| ``` -n node1 node2 ``` | Specify one node (or several nodes in a space-delimited list) for which you want to dump the node view. |
| ``` -last "duration" ``` | Use this option to specify a time, given in HH24:MM:SS format surrounded by double quotation marks (`""`), to retrieve the last metrics. For example:  ``` "23:05:00" ``` |
| ``` -s "time_stamp" -e "time_stamp" ``` | Use the `-s` option to specify a time stamp from which to start a range of queries and use the `-e` option to specify a time stamp to end the range of queries. Specify time in YYYY-MM-DD HH24:MM:SS format surrounded by double quotation marks (`""`).  ``` "2011-05-10 23:05:00" ```  Note: You must specify these two options together to obtain a range. |
| ``` -v ``` | Displays verbose node view output. Without -v you only see SYSTEM and |
| ``` -warning ``` | Use this option to print the node views with warnings, only. |
| ``` -h ``` | Displays online help for the `oclumon dumpnodeview` command. |

Usage Notes

- The default is to continuously dump node views. To stop continuous display, use Ctrl+C on Linux and Esc on Windows.
- Both the local system monitor service (`osysmond`) and the cluster logger service (`ologgerd`) must be running to obtain node view dumps.

Examples

The following example dumps node views from `node1`, `node2`, and `node3` collected over the last twelve hours:

```
$ oclumon dumpnodeview -n node1 node2 node3 -last "12:00:00"
```

The following example displays node views from all nodes collected over the last fifteen minutes:

```
$ oclumon dumpnodeview -allnodes -last "00:15:00"
```

Metric Descriptions

This section includes descriptions of the metrics in each of the seven views that make up a node view listed in the following tables.

Table H-3 SYSTEM View Metric Descriptions

| Metric | Description |
| --- | --- |
| ``` #pcpus ``` | Number of physical CPUs in the system |
| ``` #vcpus ``` | Number of logical compute units |
| ``` chipname ``` | Type of CPU |
| ``` cpuht ``` | CPU hyperthreading enabled (Y) or disabled (N) |
| ``` cpu ``` | Average CPU utilization per processing unit within the current sample interval (%). |
| ``` cpuq ``` | Number of processes waiting in the run queue within the current sample interval |
| ``` physmemfree ``` | Amount of free RAM (KB) |
| ``` physmemtotal ``` | Amount of total usable RAM (KB) |
| ``` mcache ``` | Amount of physical RAM used for file buffers plus the amount of physical RAM used as cache memory (KB)  Note: This metric is not available on Solaris or Windows systems. |
| ``` swapfree ``` | Amount of swap memory free (KB) |
| ``` swaptotal ``` | Total amount of physical swap memory (KB) |
| ``` ior ``` | Average total disk read rate within the current sample interval (KB per second) |
| ``` iow ``` | Average total disk write rate within the current sample interval (KB per second) |
| ``` ios ``` | Average total disk I/O operation rate within the current sample interval (I/O operations per second) |
| ``` swpin ``` | Average swap in rate within the current sample interval (KB per second)  Note: This metric is not available on Windows systems. |
| ``` swpout ``` | Average swap out rate within the current sample interval (KB per second)  Note: This metric is not available on Windows systems. |
| ``` pgin ``` | Average page in rate within the current sample interval (pages per second) |
| ``` pgout ``` | Average page out rate within the current sample interval (pages per second) |
| ``` netr ``` | Average total network receive rate within the current sample interval (KB per second) |
| ``` netw ``` | Average total network send rate within the current sample interval (KB per second) |
| ``` procs ``` | Number of processes |
| ``` rtprocs ``` | Number of real-time processes |
| ``` #fds ``` | Number of open file descriptors  Number of open handles on Windows |
| ``` #sysfdlimit ``` | System limit on number of file descriptors  Note: This metric is not available on Windows systems. |
| ``` #disks ``` | Number of disks |
| ``` #nics ``` | Number of network interface cards |
| ``` nicErrors ``` | Average total network error rate within the current sample interval (errors per second) |

Table H-4 PROCESSES View Metric Descriptions

| Metric | Description |
| --- | --- |
| ``` name ``` | The name of the process executable |
| ``` pid ``` | The process identifier assigned by the operating system |
| ``` #procfdlimit ``` | Limit on number of file descriptors for this process  Note: This metric is not available on Windows, Solaris, AIX, and HP-UX systems. |
| ``` cpuusage ``` | Process CPU utilization (%)  Note: The utilization value can be up to 100 times the number of processing units. |
| ``` memusage ``` | Process private memory usage (KB) |
| ``` shm ``` | Process shared memory usage (KB)  Note: This metric is not available on Windows, Solaris, and AIX systems. |
| ``` workingset ``` | Working set of a program (KB)  Note: This metric is only available on Windows. |
| ``` #fd ``` | Number of file descriptors open by this process  Number of open handles by this process on Windows |
| ``` #threads ``` | Number of threads created by this process |
| ``` priority ``` | The process priority |
| ``` nice ``` | The nice value of the process |

Table H-5 DEVICES View Metric Descriptions

| Metric | Description |
| --- | --- |
| ``` ior ``` | Average disk read rate within the current sample interval (KB per second) |
| ``` iow ``` | Average disk write rate within the current sample interval (KB per second) |
| ``` ios ``` | Average disk I/O operation rate within the current sample interval (I/O operations per second) |
| ``` qlen ``` | Number of I/O requests in wait state within the current sample interval |
| ``` wait ``` | Average wait time per I/O within the current sample interval (msec) |
| ``` type ``` | If applicable, identifies what the device is used for. Possible values are `SWAP`, `SYS`, `OCR`, `ASM`, and `VOTING`. |

Table H-6 NICS View Metric Descriptions

| Metric | Description |
| --- | --- |
| ``` netrr ``` | Average network receive rate within the current sample interval (KB per second) |
| ``` netwr ``` | Average network sent rate within the current sample interval (KB per second) |
| ``` neteff ``` | Average effective bandwidth within the current sample interval (KB per second) |
| ``` nicerrors ``` | Average error rate within the current sample interval (errors per second) |
| ``` pktsin ``` | Average incoming packet rate within the current sample interval (packets per second) |
| ``` pktsout ``` | Average outgoing packet rate within the current sample interval (packets per second) |
| ``` errsin ``` | Average error rate for incoming packets within the current sample interval (errors per second) |
| ``` errsout ``` | Average error rate for outgoing packets within the current sample interval (errors per second) |
| ``` indiscarded ``` | Average drop rate for incoming packets within the current sample interval (packets per second) |
| ``` outdiscarded ``` | Average drop rate for outgoing packets within the current sample interval (packets per second) |
| ``` inunicast ``` | Average packet receive rate for unicast within the current sample interval (packets per second) |
| ``` type ``` | Whether PUBLIC or PRIVATE |
| ``` innonunicast ``` | Average packet receive rate for multi-cast (packets per second) |
| ``` latency ``` | Estimated latency for this network interface card (msec) |

Table H-7 FILESYSTEMS View Metric Descriptions

| Metric | Description |
| --- | --- |
| ``` name ``` | Name of the file system |
| ``` mount ``` | Mount point where the file system is mounted |
| ``` type ``` | Type of the file system that is mounted, whether it is Local or NTFS or EXT2 |
| ``` total ``` | Total amount of space (KB) |
| ``` used ``` | Amount of used space (KB) |
| ``` available ``` | Amount of available space (KB) |
| ``` used% ``` | Percentage of used space (%) |
| ``` mft% ``` | Percentage of master file table utilization |
| ``` ifree% ``` | Percentage of free file nodes (%)  Note: This metric is not available on Windows systems. |

Table H-8 PROTOCOL ERRORS View Metric Descriptions <sup>Foot 1</sup>

| Metric | Description |
| --- | --- |
| ``` IPHdrErr ``` | Number of input datagrams discarded due to errors in their IPv4 headers |
| ``` IPAddrErr ``` | Number of input datagrams discarded because the IPv4 address in their IPv4 header's destination field was not a valid address to be received at this entity |
| ``` IPUnkProto ``` | Number of locally-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol |
| ``` IPReasFail ``` | Number of failures detected by the IPv4 reassembly algorithm |
| ``` IPFragFail ``` | Number of IPv4 discarded datagrams due to fragmentation failures |
| ``` TCPFailedConn ``` | Number of times that TCP connections have made a direct transition to the CLOSED state from either the SYN-SENT state or the SYN-RCVD state, plus the number of times that TCP connections have made a direct transition to the LISTEN state from the SYN-RCVD state |
| ``` TCPEstRst ``` | Number of times that TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE-WAIT state |
| ``` TCPRetraSeg ``` | Total number of TCP segments retransmitted |
| ``` UDPUnkPort ``` | Total number of received UDP datagrams for which there was no application at the destination port |
| ``` UDPRcvErr ``` | Number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port |

<sup>Footnote 1</sup> All protocol errors are cumulative values since system startup.

Example H-1 Sample Node View

```
----------------------------------------
Node: node1 Clock: '07-17-13 23.33.25' SerialNo:34836
----------------------------------------

SYSTEM:
#pcpus: 12 #vcpus: 12 cpuht: N chipname: Intel(R) cpu: 2.43 cpuq: 2
physmemfree: 56883116 physmemtotal: 74369536 mcache: 13615352 swapfree: 18480408
swaptotal: 18480408 ior: 170 iow: 37 ios: 37 swpin: 0 swpout: 0 pgin: 170
pgout: 37 netr: 40.301 netw: 57.211 procs: 437 rtprocs: 33 #fds: 15008
#sysfdlimit: 6815744 #disks: 9 #nics: 5  nicErrors: 0

TOP CONSUMERS:
topcpu: 'osysmond.bin(9103) 2.59' topprivmem: 'java(26616) 296808'
topshm: 'ora_mman_orcl_4(32128) 1222220' topfd: 'ohasd.bin(7594) 150'
topthread: 'crsd.bin(9250) 43'

PROCESSES:

name: 'mdnsd' pid: 12875 #procfdlimit: 8192 cpuusage: 0.19 privmem: 9300
shm: 8604 #fd: 36 #threads: 3 priority: 15 nice: 0
name: 'ora_cjq0_rdbms3' pid: 12869 #procfdlimit: 8192 cpuusage: 0.39
privmem: 10572 shm: 77420 #fd: 23 #threads: 1 priority: 15 nice: 0
name: 'ora_lms0_rdbms2' pid: 12635 #procfdlimit: 8192 cpuusage: 0.19
privmem: 15832 shm: 49988 #fd: 24 #threads: 1 priority: 15 nice: 0
name: 'evmlogger' pid: 32355 #procfdlimit: 8192 cpuusage: 0.0 privmem: 4600
shm: 8756 #fd: 9 #threads: 3 priority: 15 nice: 0
.
.
.

DEVICES:

xvda ior: 0.798 iow: 193.723 ios: 33 qlen: 0 wait: 0 type: SWAP
xvda2 ior: 0.000 iow: 0.000 ios: 0 qlen: 0 wait: 0 type: SWAP
xvda1 ior: 0.798 iow: 193.723 ios: 33 qlen: 0 wait: 0 type: SYS

NICS:

lo netrr: 35.743  netwr: 35.743  neteff: 71.486  nicerrors: 0 pktsin: 22
pktsout: 22  errsin: 0  errsout: 0  indiscarded: 0  outdiscarded: 0
inunicast: 22 innonunicast: 0  type: PUBLIC
eth0 netrr: 7.607  netwr: 1.363  neteff: 8.971  nicerrors: 0 pktsin: 41  
pktsout: 18  errsin: 0  errsout: 0  indiscarded: 0  outdiscarded: 0  
inunicast: 41  innonunicast: 0  type: PRIVATE latency: <1

FILESYSTEMS:

mount: / type: rootfs total: 155401100 used: 125927608 available: 21452240
used%: 85 ifree%: 93 [ORACLE_HOME CRF_HOME rdbms2 rdbms3 rdbms4 has51]

mount: /scratch type: ext3 total: 155401100 used: 125927608 available: 21452240
used%: 85 ifree%: 93 [rdbms2 rdbms3 rdbms4 has51]

mount: /net/adc6160173/scratch type: ext3 total: 155401100 used: 125927608
 available: 21452240 used%: 85 ifree%: 93 [rdbms2 rdbms4 has51]

PROTOCOL ERRORS:

IPHdrErr: 0 IPAddrErr: 19568 IPUnkProto: 0 IPReasFail: 0 IPFragFail: 0
TCPFailedConn: 931776 TCPEstRst: 76506 TCPRetraSeg: 12258 UDPUnkPort: 29132
UDPRcvErr: 148
```

#### oclumon manage

Use the `oclumon manage` command to view log information from the system monitor service.

Syntax

```
oclumon manage [[-repos {resize size | changesize memory_size | 
reploc new_location [[-maxtime size] | [-maxspace memory_size]]}] | 
[-get key1 key2 ...]]
```

Parameters

Table H-9 oclumon manage Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -repos {resize size \| changesize memory_size \|  reploc new_location  [[-maxtime size \|   -maxspace memory_size]] ``` | The `-repos` flag is required to specify the following CHM repository-related options:  - `resize` `size`: Use this option to resize the CHM repository to a specified number of seconds between 3600 (one hour) and 259200 (three days) - `changesize` `memory_size`: Use this option to change the CHM repository space limit to a specified number of MB - `reploc` `new_location`: Use this option to change the location of the CHM repository to a specified directory path, and to specify the CHM repository size in terms of elapsed seconds of data capture and a space limit for the new location |
| ``` -get key1 key2 ... ``` | Use this option to obtain CHM repository information using the following keywords:     `repsize`: Current size of the CHM repository, in seconds   `reppath`: Directory path to the CHM repository   `master`: Name of the master node   `replica`: Name of the standby node  You can specify any number of keywords in a space-delimited list following the `-get` flag. |
| ``` -h ``` | Displays online help for the `oclumon manage` command |

Usage Notes

Both the local system monitor service and the master cluster logger service must be running to resize the CHM repository.

Example

The following examples show commands and sample output:

```
$ oclumon manage -repos reploc /shared/oracle/chm
```

The preceding example moves the CHM repository to shared storage.

```
$ oclumon manage -get reppath
CHM Repository Path = /opt/oracle/grid/crf/db/node1
Done

$ oclumon manage -get master
Master = node1
done

$ oclumon manage -get repsize
CHM Repository Size = 86400
Done
```

#### oclumon version

Use the `oclumon version` command to obtain the version of CHM that you are using.

Syntax

```
oclumon version
```

Example

This command produces output similar to the following:

```
Cluster Health Monitor (OS), Version 11.2.0.3.0 - Production Copyright 2011
Oracle. All rights reserved.
```

## Clusterware Log Files and the Unified Log Directory Structure

Oracle Database uses a unified log directory structure to consolidate the Oracle Clusterware component log files. This consolidated structure simplifies diagnostic information collection and assists during data retrieval and problem analysis.

Alert files are stored in the directory structures shown in Table H-10.

Table H-10 Locations of Oracle Clusterware Component Log Files

| Component | Log File Location <sup>Foot 1</sup> |
| --- | --- |
| Cluster Health Monitor (CHM) | The system monitor service and cluster logger service record log information in following locations, respectively:  ``` Grid_home/log/host_name/crfmond Grid_home /log/host_name /crflogd ``` |
| Oracle Database Quality of Service Management (DBQOS) | Oracle Database QoS Management Grid Operations Manager logs:  ``` Grid_home/oc4j/j2ee/home/log/dbwlm/auditing ```  Oracle Database QoS Management trace logs:  ``` Grid_home/oc4j/j2ee/home/log/dbwlm/logging ``` |
| Cluster Ready Services Daemon (CRSD) Log Files | ``` Grid_home /log/host_name /crsd ``` |
| Cluster Synchronization Services (CSS) | ``` Grid_home /log/host_name /cssd ``` |
| Cluster Time Synchronization Service (CTSS) | ``` Grid_home /log/host_name /ctssd ``` |
| Grid Plug and Play | ``` Grid_home /log/host_name /gpnpd ``` |
| Multicast Domain Name Service Daemon (MDNSD) | ``` Grid_home /log/host_name /mdnsd ``` |
| Oracle Cluster Registry | Oracle Cluster Registry tools (OCRDUMP, OCRCHECK, OCRCONFIG) record log information in the following location:<sup>Foot 2</sup>  ``` Grid_home /log/host_name /client ```  Cluster Ready Services records Oracle Cluster Registry log information in the following location:  ``` Grid_home /log/host_name /crsd ``` |
| Oracle Grid Naming Service (GNS) | ``` Grid_home /log/host_name /gnsd ``` |
| Oracle High Availability Services Daemon (OHASD) | ``` Grid_home /log/host_name /ohasd ``` |
| Oracle Automatic Storage Management Cluster File System (Oracle ACFS) | ``` Grid_home /log/host_name /acfsrepl Grid_home/log/host_name/acfsreplroot Grid_home/log/host_name/acfssec Grid_home/log/host_name/acfs ``` |
| Event Manager (EVM) information generated by `evmd` | ``` Grid_home /log/host_name /evmd ``` |
| Cluster Verification Utility (CVU) | ``` Grid_home /log/host_name /cvu ``` |
| Oracle RAC RACG | The Oracle RAC high availability trace files are located in the following two locations:  ``` Grid_home/log/host_name/racg $ORACLE_HOME/log/host_name/racg ```  Core files are in subdirectories of the log directory. Each RACG executable has a subdirectory assigned exclusively for that executable. The name of the RACG executable subdirectory is the same as the name of the executable.  Additionally, you can find logging information for the VIP in `Grid_home` `/log/` `host_name` `/agent/crsd/orarootagent_root` and for the database in `$ORACLE_HOME/log/` `host_name` `/racg`. |
| Server Manager (SRVM) | ``` Grid_home /log/host_name /srvm ``` |
| Disk Monitor Daemon (`diskmon`) | ``` Grid_home /log/host_name /diskmon ``` |
| Grid Interprocess Communication Daemon (GIPCD) | ``` Grid_home /log/host_name /gipcd ``` |

<sup>Footnote 1</sup> The directory structure is the same for Linux, UNIX, and Windows systems.

<sup>Footnote 2</sup> To change the amount of logging, edit the path in the `Grid_home` `/srvm/admin/ocrlog.ini` file.

## Testing Zone Delegation

See Also:

[Appendix E, "CRSCTL Utility Reference"](crsref.md) for information about using the CRSCTL commands referred to in this procedure

Use the following procedure to test zone delegation:

1. Start the GNS VIP by running the following command as `root`:
	```
	# crsctl start ip -A IP_name/netmask/interface_name
	```
	The `interface_name` should be the public interface and netmask of the public network.
2. Start the test DNS server on the GNS VIP by running the following command (you must run this command as `root` if the port number is less than 1024):
	```
	# crsctl start testdns -address address [-port port]
	```
	This command starts the test DNS server to listen for DNS forwarded packets at the specified IP and port.
3. Ensure that the GNS VIP is reachable from other nodes by running the following command as `root`:
	```
	crsctl status ip -A IP_name
	```
4. Query the DNS server directly by running the following command:
	```
	crsctl query dns -name name -dnsserver DNS_server_address
	```
	This command fails with the following error:
	CRS-10023: Domain name look up for name asdf.foo.com failed. Operating system error: Host name lookup failure
	Look at `Grid_home` `/log/` `host_name` `/client/odnsd_*.log` to see if the query was received by the test DNS server. This validates that the DNS queries are not being blocked by a firewall.
5. Query the DNS delegation of GNS domain queries by running the following command:
	```
	crsctl query dns -name name
	```
	Note:
	The only difference between this step and the previous step is that you are not giving the `-dnsserver` `DNS_server_address` option. This causes the command to query name servers configured in `/etc/resolv.conf`. As in the previous step, the command fails with same error. Again, look at `odnsd*.log` to ensure that `odnsd` received the queries. If step 5 succeeds but step 6 does not, then you must check the DNS configuration.
6. Stop the test DNS server by running the following command:
	```
	crsctl stop testdns -address address
	```
7. Stop the GNS VIP by running the following command as `root`:
	```
	crsctl stop ip -A IP_name/netmask/interface_name
	```

## Oracle Trace File Analyzer Collector

The Oracle Trace File Analyzer (TFA) Collector is a tool for targeted diagnostic collection that simplifies diagnostic data collection for Oracle Clusterware, Oracle Grid Infrastructure, and Oracle RAC systems. TFA collects and packages diagnostic data and also has the ability to centralize and automate the collection of diagnostic information.

TFA is installed into the Oracle Grid Infrastructure home when you install, or upgrade to, Oracle Database 11g release 2 (11.2.0.4). The TFA daemon discovers relevant trace file directories and then analyzes the trace files in those directories to determine their file type (whether they are database trace or log files, or Oracle Clusterware trace or log files, for example) and the first and last timestamps of those files. TFA stores this data in a Berkeley database in the Grid home owner's `ORACLE_BASE` directory.

Note:

Oracle does not support TFA with Oracle Database 11g release 2 (11.2.0.4).

The TFA daemon periodically checks for new trace directories to add, such as when a new database instance is created, and also periodically checks whether the trace files metadata need updating. TFA uses this metadata when performing diagnostic data collections.

TFA can perform diagnostic collections in two ways, either on demand or automatically:

- Use `tfactl set` to enable automatic collection of diagnostics upon discovery of a limited set of errors in trace files
	See Also:
	`"tfactl set"`
- The `tfactl diagcollect` command collects trimmed trace files for any component and specific time range
	See Also:
	`"tfactl diagcollect"`

This section includes the following topics:

- Managing the TFA Daemon
- TFA Control Utility Command Reference
- Data Redaction with TFA

### Managing the TFA Daemon

TFA starts automatically whenever a node starts. You can manually start or stop TFA using the following commands:

- `/etc/init.d/init.tfa start`: Starts the TFA daemon
- `/etc/init.d/init.tfa stop`: Stops the TFA daemon
- `/etc/init.d/init.tfa restart`: Stops and then starts the TFA daemon
- `/etc/init.d/init.tfa shutdown`: Stops the TFA daemon and removes entries from the appropriate operating system configuration

If the TFA daemon fails, then the operating system restarts it, automatically.

### TFA Control Utility Command Reference

The TFA control utility, TFACTL, is the command-line interface for TFA, and is located in the `Grid_home` `/tfa/bin` directory. You must run TFACTL as `root` or `sudo`, because that gives access to trace files that normally allow only `root` access. Some commands, such as `tfactl host add`, require strict `root` access.

You can append the `-help` flag to any of the TFACTL commands to obtain online usage information.

This section lists and describes the following TFACTL commands:

- `tfactl print`
- `tfactl purge`
- `tfactl directory`
- `tfactl host`
- `tfactl set`
- `tfactl diagcollect`

#### tfactl print

Use the `tfactl print` command to print information from the Berkeley database.

Syntax

```
tfactl print [status | config | directories | hosts | actions | repository | cookie]
```

Parameters

Table H-11 tfactl print Command Parameters

| Parameter | Description |
| --- | --- |
| ``` status ``` | Prints the status of TFA across all nodes in the cluster, and also prints the TFA version and the port on which it is running. |
| ``` config ``` | Prints the current TFA configuration settings. |
| ``` directories ``` | Lists all the directories that TFA scans for trace or log file data, and shows the location of the trace directories allocated for the database, Oracle ASM, and instance. |
| ``` hosts ``` | Lists the hosts that are part of the TFA cluster, and that can receive clusterwide commands. |
| ``` actions ``` | Lists all the actions submitted to TFA, such as diagnostic collection. By default, `tfactl print actions` only shows actions that are running or that have completed in the last hour. |
| ``` repository ``` | Prints the current location and amount of used space of the repository directory. Initially, the maximum size of the repository directory is the smaller of either 10GB or 50% of available file system space. If the maximum size is exceeded or the file system space gets to 1GB or less, then TFA suspends operations and the repository is closed. Use the `tfactl purge` command to clear collections from the repository. |
| ``` cookie ``` | Generates and prints an identification code for use by the `tfactl set` command. |

Example

The `tfactl print config` returns output similar to the following:

```
Configuration parameter                                Value
------------------------------------------------------------
TFA Version                                          2.5.1.5
Automatic diagnostic collection                          OFF
Trimming of files during diagcollection                   ON
Repository current size (MB) in node1                    526
Repository maximum size (MB) in node1                  10240
Trace Level                                                1
```

In the preceding sample output:

- `Automatic diagnostic collection`: When `ON` (default is `OFF`), if scanning an alert log, then finding specific events in those logs triggers diagnostic collection.
- `Trimming of files during diagcollection`: Determines if TFA will trim large files to contain only data that is within specified time ranges. When this is `OFF`, no trimming of trace files occurs for automatic diagnostic collection.
- `Repository current size in MB`: How much space in the repository is currently used.
- `Repository maximum size in MB`: The maximum size of storage space in the repository. Initially, the maximum size is set to the smaller of either 10GB or 50% of free space in the file system.
- `Trace Level`: `1` is the default, and the values `2`, `3`, and `4` have increasing verbosity. While you can set the trace level dynamically for the running TFA daemon, increasing the trace level significantly impacts the performance of TFA, and should only be done at the request of My Oracle Support.

#### tfactl purge

Use the `tfactl purge` command to delete diagnostic collections from the TFA repository that are older than a specific time.

Syntax

```
tfactl purge -older number[h | d]
```

Specify a number followed by `h` or `d` (to specify a number of hours or days, respectively) to remove files older than the specified time constraint. For example:

```
# tfactl purge -older 30d
```

The preceding command removes files older than 30 days.

#### tfactl directory

Use the `tfactl directory` command to add a directory to, or remove a directory from, the list of directories that will have their trace or log files analyzed. You can also use this command to change the directory permissions. When a directory is added by auto discovery, it is added as public, which means that any file in that directory can be collected by any user that has permission to run the `tfactl diagcollect` command. This is only important when `sudo` is used to allow users other than `root` to run TFACTL commands. If a directory is marked as private, then TFA determines which user is running TFACTL commands and verifies that the user has permissions to see the files in the directory before allowing any files to be collected.

Note:

A user can only add a directory to TFA to which they have read access, and also that TFA auto collections, when configured, run as `root`, and so will always collect all available files.

Syntax

```
tfactl directory [add directory | remove directory | modify directory -private | -public]
```

Parameters

Table H-12 tfactl directory Command Parameters

| Parameter | Description |
| --- | --- |
| ``` add directory ``` | Adds a specific directory |
| ``` remove directory ``` | Removes a specific directory |
| ``` modify directory -private \| -public ``` | Modifies a specific directory to either be private or public, where information can only be collected by users with specific operating system permissions (`-private`), or by anyone with the ability to run the `tfactl diagcollection` command (`-public`) |

Usage Notes

You must add all trace directory names to the Berkeley database, so that TFA will collect file metadata in that directory. The discovery process finds most directories but if new or undiscovered directories are required, then you can add these manually using the `tfactl directory` command. When you add a directory using TFACTL, TFA attempts to determine whether the directory is for the database, Oracle Clusterware, operating system logs, or some other component, and for which database or instance. If TFA cannot determine this information, then it returns an error and requests that you enter the information, similar to the following:

```
# tfactl directory add /tmp

Failed to add directory to TFA. Unable to determine parameters for directory: /tmp
Please enter component for this Directory [RDBMS|CRS|ASM|INSTALL|OS|CFGTOOLS] : RDBMS
Please enter database name for this Directory :MYDB
Please enter instance name for this Directory :MYDB1
```

#### tfactl host

Use the `tfactl host` command to add hosts to, or remove hosts from, the TFA cluster.

Syntax

```
tfactl host [add host_name | remove host_name]
```

Specify a host name to add or remove, as in the following example:

```
# tfactl host add myhost.domain.com
```

Usage Notes

Using the `tfactl host add` command notifies the local TFA about other nodes on your network. When you add a host, TFA contacts that host and, if TFA is running on that host, then both hosts synchronize their host list. TFA authenticates that a host can be added using a cookie. If the host to be added does not have the correct cookie, then you must retrieve that cookie from an existing host in the cluster and set it on the host being added, similar to the following:

```
#tfactl host add node2

Failed to add host: node2 as the TFA cookies do not match.
To add the host successfully, try the following steps:
1. Get the cookie in node1 using:
./tfa_home/bin/tfactl print cookie
2. Set the cookie from Step 1 in node2 using:
  ./tfa_home/bin/tfactl set cookie=<COOKIE>
3. After Step 2, add host again:
 ./tfa_home/bin/tfactl host add node2
```

After you successfully add the host, all clusterwide commands will activate on all nodes registered in the Berkeley database.

#### tfactl set

Use the `tfactl set` command to adjust the manner in which TFA runs.

Syntax

```
tfactl set [autodiagcollect=ON | OFF | cookie=Xn | trimfiles=ON | OFF |
tracelevel=1 | 2 | 3 | 4 | reposizeMB=number | repositorydir=directory] [-c]
```

Parameters

Table H-13 tfactl set Command Parameters

| Parameter | Description |
| --- | --- |
| ``` autodiagcollect=ON \| OFF ``` | When set to `OFF`, which is the default, automatic diagnostic collection is disabled. If set to `ON`, TFA automatically collects diagnostics when certain patterns occur while TFA scans the alert logs.  To set automatic collection for all nodes of the TFA cluster, you must specify the `-c` parameter. |
| ``` cookie=UID ``` | Use the `tfactl print cookie` command to generate the cookie identification. |
| ``` trimfiles=ON \| OFF ``` | When set to `ON`, TFA trims files to only have relevant data when diagnostic collection is done as part of a scan.  Note: When using `tfactl diagcollect`, you determine the time range for trimming with the parameters you specify with that command. Oracle recommends that you not set this parameter to `OFF`, because untrimmed data be very large. |
| ``` tracelevel=1 \| 2 \| 3 \| 4 ``` | Do not change the tracing level unless you are directed to do so by My Oracle Support. |
| ``` -c ``` | Specify this parameter to propagate these settings to all nodes in the TFA configuration. |

Automatic Diagnostic Collection

After TFA initially gathers trace file metadata, the daemon monitors all files that are determined to be alert logs using `tail`, so that TFA can take action when certain strings occur.

By default, these logs are database alert logs, Oracle ASM alert logs, and Oracle Clusterware alert logs. When specific patterns occur in the logs saved to the Berkeley database, automatic diagnostic collection may take place.

Exactly what is collected depends on the pattern that is matched. TFA may just store information on the pattern matched or may initiate local diagnostic collection. Although TFA always monitors the logs and collects information into its database, automatic diagnostic collection only happens if it is enabled first using the `tfactl set` command.

#### tfactl diagcollect

Use the `tfactl diagcollect` command to perform on-demand diagnostic collection. You can configure a number of different parameters to determine how large or detailed a collection you want. You can specify a specific time of an incident or a time range for data to be collected, and determine if whole files that have relevant data should be collected or just a time interval of data from those files.

Note:

If you specify no parameters, then the `tfactl diagcollect` command collects files from all nodes for all components where the file has been updated in the last four hours, and also trims excessive files. If an incident occurred prior to this period, then you can use the parameters documented in this section to target the correct data collection.

Syntax

```
tfactl diagcollect [-all | -database all | database_1,database_2,... | -asm | -crs | -os | -install]
[-node all | local | node_1,node_2,...][-tag description] [-z file_name]
[-since numberh | d | -from "mmm/dd/yyyy hh:mm:ss" -to "mmm/dd/yyyy hh:mm:ss"
| -for "mmm/dd/yyyy hh:mm:ss" [-nocopy] [-nomonitor]]
```

Parameters

Table H-14 tfactl diagcollect Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -all \| -database all  \| database_1,database_2,...  \| -asm \| -crs \| -os \|  -install ``` | You can choose one or more individual components from which to collect trace and log files or choose `-all` to collect all files in the inventory. If you do not specify a time interval, then TFACTL collects files from the last four hours. |
| ``` -node all \| local \| node_1,node_2,... ``` | You can specify a comma-delimited list of nodes from which to collect diagnostic information. Default is `all`. |
| ``` -tag description ``` | Use this parameter to create a subdirectory for the resulting collection in the TFA repository. |
| ``` -z file_name ``` | Use this parameter to specify an output file name. |
| ``` -since numberh \| d \|  -from "mmm/dd/yyyy hh:mm:ss"  -to "mmm/dd/yyyy hh:mm:ss" \|  -for "mmm/dd/yyyy hh:mm:ss" ``` | - Specify the `-since` parameter to collect files that have relevant data for the past specific number of hours (`h`) or days (`d`). By default, using the command with this parameter also trims files that are large and shows files only from the specified interval. - Specify the `-from` and `-to` parameters (you must use these two parameters together) to collect files that have relevant data during a specific time interval, and trim data before this time where files are large. - Specify the `-for` parameter to collect files that have relevant data for the time given. The files TFACTL collects will have timestamps in between which the time you specify after `-for` is included. No data trimming is done for this option.  Note: If you specify both date and time, then you must enclose both values in double quotation marks (`""`). If you specify only the date or the time, then you do not have to enclose the single value in quotation marks. |
| ``` -nocopy ``` | Specify this parameter to stop the resultant trace file collection from being copied back to the initiating node. The file remains in the TFA repository on the executing node. |
| ``` -nomonitor ``` | Specify this parameter to prevent the terminal on which you run the command from displaying the progress of the command. |

Examples

- The following command trims and zips all files updated in the last four hours, including `chmos` and `osw` data, from across the cluster and collects it on the initiating node:
	```
	# tfactl diagcollect
	```
- The following command trims and zips all files updated in the last eight hours, including `chmos` and `osw` data, from across the cluster and collects it on the initiating node:
	```
	# tfactl diagcollect –all –since 8h
	```
- The following command trims and zips all files from databases `hrdb` and `fdb` updated in the last one day and collects it on the initiating node:
	```
	# tfactl diagcollect -database hrdb,fdb -since 1d -z foo
	```
- The following command trims and zips all Oracle Clusterware files, operating system logs, and `chmos` and `osw` data from `node1` and `node2` updated in the last six hours, and collects it on the initiating node.
	```
	# tfactl diagcollect –crs -os -node node1,node2 -since 6h
	```
- The following command trims and zips all Oracle ASM logs from `node1` updated between July 4, 2013 and July 5, 2013 at 21:00, and collects it on the initiating node:
	```
	# tfactl diagcollect -asm -node node1 -from Jul/4/2013 -to "Jul/5/2013 21:00:00"
	```
- The following command trims and zips all log files updated on July 2, 2013 and collect at the initiating node:
	```
	# tfactl diagcollect -for Jul/2/2013
	```
- The following command trims and zips all log files updated from 09:00 on July 2, 2013, to 09:00 on July 3, 2013, which is 12 hours before and after the time specified in the command, and collects it on the initiating node:
	```
	# tfactl diagcollect -for "Jul/2/2013 21:00:00"
	```

### Data Redaction with TFA

You can hide sensitive data by replacing data in files or paths in file names. To use this feature, place a file called `redaction.xml` in the `tfa_home` `/resources` directory. TFA uses the data contained within the `redaction.xml` file to replace strings in file names and contents. The format of the `redaction.xml` file is as follows:

```
<replacements>
<replace>
<before>securestring</before>
<after>nonsecurestring</after>
</replace>
<replace>
<before>securestring2</before>
<after>nonsecurestring2</after>
</replace>
Etc…
</replacements>
```

## Diagnostics Collection Script

Every time an Oracle Clusterware error occurs, run the `diagcollection.pl` script to collect diagnostic information from Oracle Clusterware into trace files. The diagnostics provide additional information so My Oracle Support can resolve problems. Run this script from the following location:

```
Grid_home/bin/diagcollection.pl
```

Note:

You must run this script as the `root` user.

## Oracle Clusterware Alerts

Oracle Clusterware posts alert messages when important events occur. The following is an example of an alert from the CRSD process:

```
2009-07-16 00:27:22.074
[ctssd(12817)]CRS-2403:The Cluster Time Synchronization Service on host stnsp014 is in observer mode.
2009-07-16 00:27:22.146
[ctssd(12817)]CRS-2407:The new Cluster Time Synchronization Service reference node is host stnsp013.
2009-07-16 00:27:22.753
[ctssd(12817)]CRS-2401:The Cluster Time Synchronization Service started on host stnsp014.
2009-07-16 00:27:43.754
[crsd(12975)]CRS-1012:The OCR service started on node stnsp014.
2009-07-16 00:27:46.339
[crsd(12975)]CRS-1201:CRSD started on node stnsp014.
```

The location of this alert log on Linux, UNIX, and Windows systems is in the following directory path, where `Grid_home` is the name of the location where the Oracle Grid Infrastructure is installed: `Grid_home` `/log/` `host_name`.

The following example shows the start of the Oracle Cluster Time Synchronization Service (OCTSS) after a cluster reconfiguration:

```
[ctssd(12813)]CRS-2403:The Cluster Time Synchronization Service on host stnsp014 is in observer mode.
2009-07-15 23:51:18.292
[ctssd(12813)]CRS-2407:The new Cluster Time Synchronization Service reference node is host stnsp013.
2009-07-15 23:51:18.961
[ctssd(12813)]CRS-2401:The Cluster Time Synchronization Service started on host stnsp014.
```

### Alert Messages Using Diagnostic Record Unique IDs

Beginning with Oracle Database 11g release 2 (11.2), certain Oracle Clusterware messages contain a text identifier surrounded by " `(:`" and "`:)` ". Usually, the identifier is part of the message text that begins with " `Details in...`" and includes an Oracle Clusterware diagnostic log file path and name similar to the following example. The identifier is called a DRUID, or Diagnostic Record Unique ID:

```
2009-07-16 00:18:44.472
[/scratch/11.2/grid/bin/orarootagent.bin(13098)]CRS-5822:Agent '/scratch/11.2/grid/bin/orarootagent_root' disconnected from server. Details at (:CRSAGF00117:) in /scratch/11.2/grid/log/stnsp014/agent/crsd/orarootagent_root/orarootagent_root.log.
```

DRUIDs are used to relate external product messages to entries in a diagnostic log file and to internal Oracle Clusterware program code locations. They are not directly meaningful to customers and are used primarily by My Oracle Support when diagnosing problems.

Note:

Oracle Clusterware uses a file rotation approach for log files. If you cannot find the reference given in the file specified in the " `Details in` " section of an alert file message, then this file might have been rolled over to a rollover version, typically ending in `*.l` `number` where `number` is a number that starts at `01` and increments to however many logs are being kept, the total for which can be different for different logs. While there is usually no need to follow the reference unless you are asked to do so by My Oracle Support, you can check the path given for roll over versions of the file. The log retention policy, however, foresees that older logs are to be purged as required by the amount of logs generated.