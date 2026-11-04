---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/maa-evaluations-multicloud-solutions.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## MAA Evaluations on Multicloud Solutions

Oracle Maximum Availability Architecture (MAA) validates the MAA Silver, MAA Gold, and MAA Platinum reference architectures with its Oracle Multicloud partners.

- MAA Silver - The validated MAA Silver solution encompasses the best high availability (HA) database platform, which includes configuration and lifecycle best practices covering Oracle database creation, elastic operations, software updates, and backup and restore. All applications can leverage this solution without any changes.
- MAA Gold - The validated MAA Gold solution achieves comprehensive data protection and disaster recovery (DR) when augmented with an Oracle Cloud standby database configured with Oracle Active Data Guard. MAA Gold is the best and simplest cloud solution for mission-critical enterprise databases and applications to achieve maximum resiliency in the case of a local or widespread unexpected outage, without requiring application changes.
- MAA Platinum - When augmented with Oracle GoldenGate or OCI GoldenGate Marketplace and MAA life cycle best practices, the validated MAA Platinum solution achieves a NeverDown option, because you can direct the application to any one of the available logical GoldenGate replicas for any outage scenario. MAA Platinum can be implemented with minimum application changes other than routing work to avoid logical transaction conflicts and make logical conflict resolution a rare case.

See [Oracle Cloud: Maximum Availability Architecture](https://www.oracle.com/a/tech/docs/cloud-maa-overview.pdf) for a detailed walk-through of Oracle Cloud MAA architectures and features.

### Oracle Database Multicloud Evaluations by Oracle MAA

To ensure success and consistency for Oracle customers, the Oracle MAA solution team evaluates MAA reference architectures and key life cycle operations on the actual Oracle Database in Multicloud environments. The goal is to provide assurances using chaos engineering validation methods.

- Expected RTO and RPO are achieved with 100s of different unplanned outages (gray and complex failures) and planned maintenance activities
- Expected performance impact brownout observed with software updates and elastic operations
- Configuration best practices are in place at deployment, and configuration health checks continue to work as expected
- Key life cycle practices work as expected

When the validation of the MAA solution in our Multicloud environments meets the minimum requirements, Oracle MAA documents the MAA architecture, RTO and RPO observations, and network and performance considerations.

#### Network Evaluation

An MAA network evaluation of Oracle Database Multicloud solutions consists of the following:

Network Considerations

Network considerations such as network bandwidth and network latency using OCI peered network or Multicloud peered network

- Application to database VM
- Database VM to database VM within the same Availability Domains (ADs) or Availability Zones (AZs)
- Database VM to database VM across ADs or AZs
- Database VM to database VM across regions
- Database VM to database VM across Availability Domain or Availability Zone or cross-region

Network Test Prerequisites

Latency and throughput are measured by `iperf3` and `qperf` (installed on Exadata by default).

- Ensure that the ingress and egress security rules on each OCI VCN allow for port 5201, the default port for `iperf3`, which will also be used for `qperf` in these tests. See [Updating a Security List](https://docs.public.oneportal.content.oci.oraclecloud.com/iaas/compute-cloud-at-customer/topics/network/updating-a-security-list.htm) for more information about security rules.
- Record the Virtual IP addresses (VIP) for the database server VMs that will be tested.
	On each database server VM being tested run:
	```
	as grid (sudo su - grid from opc user):
	$ srvctl config vip -n $(hostname -s)
	VIP exists: network number 1, hosting node <hostname>
	VIP Name: <VIP name>
	VIP IPv4 Address: <VIP> ← record this IP address for each host involved in the tests
	VIP IPv6 Address: 
	VIP is enabled.
	VIP is individually enabled on nodes: 
	VIP is individually disabled on nodes:
	```

Network Tests

- Run the following tests multiple times to ensure consistency.
- It is recommended that the tests be run at different times of the day to ensure consistency throughout.
- For database server VMs, these tests should minimally be performed between one VM of the primary cluster and one VM of the standby database cluster. Additional tests can be performed on all database servers to ensure consistency.
- All `iperf3` and `qperf` commands should be run as root (sudo su - from opc user).
- For `iperf3` tests, you can optionally use the `-f                         M` parameter to display bitrate results in MB/s.

Single Process Throughput Tests

1. On the standby database server VM run:
	```
	# iperf3 -s
	```
2. On the primary database server VM run the following test multiple times to ensure consistency.
	```
	# iperf3 -c <remote VIP>
	```
3. Record the SUM of the sender at the end of each run.

Sample output:

```
Connecting to host <remote VIP>, port 5201
[  5] local <local IP> port 49230 connected to <remote VIP> port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   474 MBytes  3.97 Gbits/sec  1656   2.70 MBytes       
[  5]   1.00-2.00   sec   235 MBytes  1.97 Gbits/sec    0   3.06 MBytes       
[  5]   2.00-3.00   sec   266 MBytes  2.23 Gbits/sec    0   3.44 MBytes       
[  5]   3.00-4.00   sec   264 MBytes  2.21 Gbits/sec   61   2.73 MBytes       
[  5]   4.00-5.00   sec   240 MBytes  2.01 Gbits/sec    0   3.09 MBytes       
[  5]   5.00-6.00   sec   268 MBytes  2.24 Gbits/sec    0   3.43 MBytes       
[  5]   6.00-7.00   sec   266 MBytes  2.23 Gbits/sec   76   1.87 MBytes       
[  5]   7.00-8.00   sec   169 MBytes  1.42 Gbits/sec    0   2.25 MBytes       
[  5]   8.00-9.00   sec   199 MBytes  1.67 Gbits/sec    0   2.61 MBytes       
[  5]   9.00-10.00  sec   229 MBytes  1.92 Gbits/sec    0   2.99 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.55 GBytes  2.19 Gbits/sec  1793             sender  <---- USE THIS VALUE
[  5]   0.00-10.01  sec  2.54 GBytes  2.18 Gbits/sec                  receiver
```

Multi-Process Throughput Tests

For multiple processes, evaluate different degrees of parallelism 4, 10, and 16.

1. On the standby database server VM run:
	```
	# iperf3 -s
	```
2. On the primary database server VM run each of the following tests multiple times to ensure consistency.
	```
	# iperf3 -c <remote VIP> -P 4
	# iperf3 -c <remote VIP> -P 10
	# iperf3 -c <remote VIP> -P 16
	```
3. Record the SUM of the sender at the end of each run. For example:
	```
	<...>
	[SUM]   0.00-10.00  sec  10.1 GBytes  8.71 Gbits/sec  2159             sender
	```
4. Repeat these tests in both directions (server on primary VM) to ensure throughput.

Note:

High degrees of parallelism (for example, above 16) do not show a representative measure of throughput with iperf3. It is not recommended that you use higher parallelism in the tests.

Latency Tests

1. On the standby database server VM run:
	```
	# qperf -lp 5201
	```
2. On the primary database server VM run the following test multiple times to ensure consistency.
	```
	# qperf 10.255.0.118 -lp 5201 tcp_lat
	```

Note:

`qperf` measures latency in only one direction. Run this test in both directions and sum the values for round trip time (RTT).

Network Results Impact on Application and Database Workload and Architecture

- Application performance and network round trip latency: If your application is OLTP or dependent on low latency between the application VM and the database VM, co-locate your application VM with the database VM and ensure that RTT latency meets your response time requirements.
- Local standby database and network round trip latency: If you are considering a zero data loss SYNC transport configuration between the primary and standby in the same region, round trip (RTT) network latency over 3 milliseconds (<1ms preferred) can impact the response time and throughput of the application.
	Most standby databases using SYNC transport have RTT network latency < 1 ms. A Globally Distributed Database (sharded database) also benefits from low RTT latency between database shards.
- Sufficient single process network throughput to support peak database change rate for standby: A single process `iperf` throughput test must exceed the maximum throughput of each database instance's peak redo rate, preferably by 20% or more, to handle growth.
	If this throughput is not met, once the standby is configured, it may be unable to keep up with the primary database during peak times. Single process throughput is also critical for Oracle Golden Gate and Globally Distributed Database configurations.
	Single process throughput should be at least 2.4 Gb/sec (300 MB/sec). If not, log a service request with the multi-vendor partner. With OCI peering, the expectation is that throughput will be much higher than the aforementioned minimum.
- Sufficient multiple-process network throughput to high data volume transfers: The parallel iperf test indicates approximately how fast the database can be instantiated with the tested number of processes.
	For example, for a 50 TB database, if the test with a degree of parallelism of 8 achieves 1GB/s, a database with eight processes will take over 14 hours to instantiate. The default instantiation uses four channels; a service request can be opened with Oracle Support to increase the degree of parallelism for instantiation.
	Multiple-process throughput should be at least 8 Gb/sec (1000 MB/sec). If not, log a service request with the multi-vendor partner. With OCI peering, the expectation is that throughput will be much higher than the aforementioned minimum. Higher latency means a longer delay in data transmission, which can result in lower throughput even if the network speed is high. Other factors resulting in lower throughput include packet loss and congestion.

#### MAA Silver Architecture and Evaluation

MAA Silver on Oracle Database in a Multicloud solution consists of the following architecture:

- The Oracle Exadata Database Service on Dedicated Infrastructure (ExaDB-D) cluster residing in the Multicloud partner's data center
- High Availability (HA) and redundant application tier spread across multiple AZs
- Key Management Service, Autonomous Recovery Service (in Multicloud data center or OCI), and Object Storage Service (in OCI) for backup and restore
- Pre-configured redundant and HA network topology

MAA Silver evaluation consists of:

- Network tests from the application VM to database VM, then database VM to backup target solution
- Testing backup and restore performance, throughput, and key use cases using Oracle Cloud Infrastructure (OCI) Object Storage Service (in OCI), or Autonomous Recovery Service in Multicloud data center or OCI
- Setting up an application workload and MAA framework to simulate 100s of different unplanned (blackout and brownout) outages
- Ensuring RTO and RPO are met for local failures
- Ensuring zero downtime or expected brief application brownout for system and database elastic changes or software updates can be met
- Ensuring that the exachk or configuration health checks work as expected, and that the deployed system is MAA compliant

#### MAA Gold Architecture and Evaluation

MAA Gold on Oracle Database in a Multicloud solution consists of the following architecture:

- Oracle Exadata Database Service on Dedicated Infrastructure (ExaDB-D) VM clusters (primary and standby databases) reside in the same or separate availability domains (AD) or availability zones (AZ) or separate Multicloud regions
	Note that all primary and standby databases and their data reside in Oracle's Multicloud partner's data centers. Assuming primary and standby databases reside in the same AD or AZ, the MAA Gold architecture still provides inherent HA benefits plus DR failover options for database and cluster failures. However, this configuration lacks DR protection for a complete AD or AZ site failure, such as a regional power outage. The MAA architecture only provides regional failure protection if the standby database resides in a separate region.
- HA and redundant application tiers are spread across multiple AZs or regions
- Key Management Service, Autonomous Recovery Service (in Multicloud data center or OCI), and Object Storage Service (in OCI) for backup and restore
- Pre-configured redundant and HA network topology

MAA Gold evaluation builds upon the MAA Silver evaluation, plus:

- Network tests between primary and standby database clusters using OCI peered or Multicloud peered networks to evaluate round-trip latency and bandwidth
- Oracle Data Guard role transition performance and timings for disaster recovery use cases
- Oracle database rolling upgrade with Data Guard

### Oracle Maximum Availability Architecture Benefits

Once certified, the following are some benefits of implementing Oracle MAA reference architectures for Oracle Multicloud.

For a comprehensive list of Oracle Maximum Availability Architecture benefits for Oracle Exadata Database Machine systems, see [Exadata Database Machine: Maximum Availability Architecture](https://www.oracle.com/docs/tech/exadata-maa.pdf).

Deployment

Oracle Database in a Multicloud solution running Oracle Exadata Database Service on Dedicated Infrastructure is deployed using Oracle Maximum Availability Architecture best practices, including configuration best practices for storage, network, operating system, Oracle Grid Infrastructure, and Oracle Database. Oracle Exadata Database Service on Dedicated Infrastructure (ExaDB-D) is optimized to run enterprise Oracle databases with extreme scalability, availability, and elasticity.

Oracle MAA Database Templates

All Oracle Cloud databases created with Oracle Cloud automation use Oracle Maximum Availability Architecture default settings, which are optimized for Oracle Database in Multicloud environments. Oracle does not recommend that you use custom scripts to create cloud databases. To migrate Oracle databases to Oracle Database in a Multicloud solution, use Oracle Zero Downtime Migration (ZDM). See [Introduction to Zero Downtime Migration (oracle.com)](https://docs.oracle.com/en/database/oracle/zero-downtime-migration/21.4/zdmug/introduction-to-zero-downtime-migration.html#GUID-FF4CA22F-CC83-4118-AF26-6E7BE224717F).

Other than adjusting memory and system resource settings, avoid migrating previous database parameter settings, especially undocumented parameters. One beneficial primary database data protection parameter, `DB_BLOCK_CHECKING`, is not enabled by default because of its potential performance overhead. Any standby database configured with cloud automation enables `DB_BLOCK_CHECKING` on the standby automatically to maximize data protection and detection on the standby database. MAA recommends evaluating the performance impact of your application and allowing this parameter to be set on the primary database to maximize logical data corruption prevention and detection if the performance impact is reasonable. In Oracle Database releases 19c and later, the Data Guard broker maintains the data protection settings through MAA best practices.

Backup and Restore Automation

Backup copies provide additional protection when you configure automatic backup to Autonomous Recovery Service in Azure, Google Cloud, or OCI, or to Object Storage Service in OCI. Oracle Recovery Manager (RMAN) validates cloud database backups for physical corruptions.

Database backups occur daily, with a full backup occurring once a week, and incremental backups occurring on all other days. Archived log backups occur frequently to reduce potential data loss in case a complete database restoration and recovery is required. The archived log backup frequency is 30 minutes by default; however, the possible data loss will be zero or near zero with Oracle Data Guard.

With Autonomous Recovery Service, weekly full backups are eliminated, reducing backup windows and impact with its unique incremental backup forever benefit. When Real-Time Data Protection is enabled, data loss can be near zero when restoring from backups. Backups can occur on primary or standby databases, and various retention options exist.

Oracle Exadata Database Machine Inherent Benefits

Oracle Exadata Database Machine is the best Oracle Maximum Availability Architecture database platform that Oracle offers. Exadata is engineered with hardware, software, database, availability, and extreme performance for all workloads and scalability innovations supporting mission-critical enterprise applications.

Specifically, Exadata provides unique high availability, data protection, and quality-of-service capabilities that set Oracle apart from any other platform or cloud vendor. Sizing Exadata cloud systems to meet your application and database system resource needs (for example, sufficient CPU, memory, and I/O resources) is crucial to maintaining the highest availability, stability, and performance. Proper sizing and resource management are critical when consolidating many databases on the same cluster. Database consolidation is a widespread benefit when leveraging Exadata.

See [Oracle Maximum Availability Architecture in Oracle Exadata Cloud Systems](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) for details

### Expected Impact During Unplanned Outages

The following table lists various unplanned outage events and the associated potential database downtime, application Recovery Time Objective (RTO), and data loss potential or recovery point objective (RPO).

For Oracle Data Guard architectures (MAA Gold), the database or service level downtime does not include detection time or the time it takes before a customer initiates the Cloud Console Data Guard failover operation.

| Outage Event | Database Downtime | Service-Level Downtime (RTO) | Potential Service-Level Data Loss (RPO) |
| --- | --- | --- | --- |
| Localized events, including:  Exadata cluster network topology failures  Storage (disk, flash, and storage cell) failures  Database instance failures  Database server failures | Zero | Near-zero | Zero |
| Events that require restoration from backup because a standby database does not exist:  Data corruptions  Full database failures  Complete storage failures  Availability Zone failures | Minutes to hours  (without Data Guard) | Minutes to hours  (without Data Guard) | Near Zero with Autonomous Recovery Service and Real-Time Data Protection enabled  30 minutes with Autonomous Recovery Service and Real-Time Data Protection disabled, or with Object Storage Service for cloud backups  (without Data Guard) |
| Events using Data Guard to fail over:  Data corruptions  Full database failures  Complete storage failures  Availability Zone failures  Complete Region failures | Seconds to minutes <sup>1</sup>  Zero downtime for physical corruptions due to the auto-block repair feature | Seconds to minutes <sup>1</sup>  The foreground process that detects the physical corruption pauses while auto-block repair completes | Zero for Maximum Availability (SYNC redo transport)  Near Zero for Maximum Performance (ASYNC redo transport) |

<sup>1</sup> For MAA Gold, to protect your database from regional failure, instantiate the standby database in a region different from the primary database. For this MAA evaluation, the standby database was in a different AZ. Also, Data Guard Fast-Start Failover and its Data Guard observers must be set up manually to perform automatic database failover. Application workloads as high as 300 MB/second per Oracle Real Application Cluster instance were validated. The standby database was up-to-date with near-zero lag. Depending on the workload, standby database tuning may be required for extreme workloads (see [Tune and Troubleshoot Oracle Data Guard](tune-and-troubleshoot-oracle-data-guard1.md)).

### Expected Impact During Planned Maintenance

The following tables describe the impact of various planned maintenance events for Oracle Exadata Database Service on Dedicated Infrastructure (ExaDB-D) on Oracle's multicloud solutions: Oracle Database@Azure, Oracle Database@Google Cloud, and Oracle Database@AWS.

Impact of Exadata Cloud Software Updates

The following table lists various software updates and their impact on the associated database and application. This applies to ExaDB-D on Oracle's multicloud solutions.

| Software Update | Database Impact | Application Impact | Scheduled By | Performed By |
| --- | --- | --- | --- | --- |
| Exadata Network Fabric Switches | Zero downtime with no database restart | Zero to single-digit seconds brownout | Oracle schedules based on customer preferences, and customers can reschedule | Oracle Cloud Operation |
| Exadata Storage Servers | Zero downtime with no database restart | Zero to single-digit seconds brownout  Exadata storage servers are updated in a rolling manner, maintaining redundancy.  Oracle Exadata System Software pre-fetches the secondary mirrors of the OLTP data most frequently accessed into the flash cache, maintaining application performance during storage server restarts.  Exadata smart flash for database buffers is maintained across a storage server restart.  With Exadata 21.2 software, [Persistent Storage Index](https://docs.oracle.com/pls/topic/lookup?ctx=en/engineered-systems/exadata-database-machine&id=DBMSO-GUID-3C74128F-3305-40EC-9481-81843C0B2075) and [Persistent Columnar Cache](https://docs.oracle.com/pls/topic/lookup?ctx=en/engineered-systems/exadata-database-machine&id=DBMSO-GUID-88E0A908-C2E7-4D86-B880-C6AF0F46FD60) features enable consistent query performance after a storage server software update. | Oracle schedules based on customer preferences, and customers can reschedule | Oracle Cloud Operation |
| Exadata Database Host  Monthly Infrastructure Security Maintenance | Zero downtime with no host or database restart | Zero downtime | Oracle schedules, and customers can reschedule | Oracle Cloud Operation |
| Exadata Database Host  Quarterly Infrastructure Maintenance | Zero downtime with Oracle RAC rolling updates | Zero downtime  Exadata Database compute resources are reduced until planned maintenance is completed. | Oracle schedules based on customer preferences, and customers can reschedule | Oracle Cloud Operation |
| Exadata Database Guest | Zero downtime with Oracle RAC rolling updates | Zero downtime  Exadata Database compute resources are reduced until planned maintenance is completed. | Customer | Customers, using Oracle Cloud Console or APIs |
| Oracle Database quarterly update or custom image update | Zero downtime with Oracle RAC rolling updates | Zero downtime  Exadata Database compute resources are reduced until planned maintenance is completed.  Applications that use database OJVM require special consideration during rolling database quarterly updates (see [My Oracle Support Doc ID 2217053.1](https://support.oracle.com/rs?type=doc&id=2217053.1)). | Customer | Customers using Oracle Cloud Console, APIs, or `dbaascli` utility  In-place, with database home patch, and out-of-place with database move (recommended)  Works for Data Guard and standby databases (see [My Oracle Support Doc ID 2701789.1](https://support.oracle.com/rs?type=doc&id=2701789.1)) |
| Oracle Grid Infrastructure quarterly update or upgrade | Zero downtime with Oracle RAC rolling updates | Zero downtime  Exadata Database compute resources are reduced until planned maintenance is completed. | Customer | Customers, using Oracle Cloud Console, APIs, or `dbaascli` utility |
| Oracle Database upgrade with downtime | Minutes to Hour(s) downtime | Minutes to Hour(s) downtime | Customer | Customers, using Oracle Cloud Console, APIs, or `dbaascli` utility  Works for Data Guard and standby databases (see [My Oracle Support Doc ID 2628228.1](https://support.oracle.com/rs?type=doc&id=2628228.1)) |
| Oracle Database upgrade with near-zero downtime | Minimal downtime with `DBMS_ROLLING`, Oracle GoldenGate replication, or with pluggable database relocate | Minimal downtime with `DBMS_ROLLING`, Oracle GoldenGate replication, or with pluggable database relocate | Customer | Customers, using `dbaascli` leveraging `DBMS_ROLLING` (see [My Oracle Support Doc ID 2832235.1](https://support.oracle.com/rs?type=doc&id=2832235.1))  Customers, using generic Maximum Availability Architecture best practices |

Impact of Exadata Elastic Operations

Exadata cloud systems have many elastic capabilities that can be used to adjust database and application performance needs. By rearranging resources on need, you can maximize system resources to targeted databases and applications and minimize costs.

The following table lists elastic Oracle Exadata Cloud Infrastructure and VM Cluster updates and the impacts associated with those updates on databases and applications. Unless specified otherwise, these operations can be performed using Oracle Cloud Console or APIs.

| VM Cluster Change | Database Impact | Application Impact |
| --- | --- | --- |
| Scale Up or Down VM Cluster Memory | Zero downtime with Oracle RAC rolling updates | Zero to single-digit seconds brownout |
| Scale Up or Down VM Cluster CPU | Zero downtime with no database restart | Zero downtime  Available CPU resources can impact application performance and throughput |
| Scale Up or Down (resize) ASM Storage for Database usage | Zero downtime with no database restart | Zero downtime  Application performance might be minimally impacted |
| Scale Up VM Local /u02 File System Size (Exadata X9M and later systems) | Zero downtime with no database restart | Zero downtime |
| Scale Down VM Local /u02 File System Size | Zero downtime with Oracle RAC rolling updates for scaling down | Zero to single-digit seconds brownout |
| Adding Exadata Storage Cells | Zero downtime with no database restart | Zero to single-digit seconds brownout  Application performance might be minimally impacted |
| Adding Exadata Database Servers | Zero downtime with no database restart | Zero to single-digit seconds brownout  Adding Oracle RAC instances and CPU resources may improve application performance and throughput |
| Adding Database Nodes in Virtual Machines (VMs) Cluster | Zero downtime with no database restart | Zero to single-digit seconds brownout  Application performance and throughput may increase or decrease by adding or dropping Oracle RAC instances and CPU resources |

Planning for the Impact of Exadata Elastic Operations

Because some of the above elastic changes may take significant time and impact your application's available resources, some planning is required.

Note that “scale down” and “drop” changes will decrease available resources. Care must be taken to not reduce resources below the amount required for database and application stability and to meet application performance targets. The following table provides the estimated duration and planning recommendations for these changes.

| VM Cluster Change | Database Impact | Application Impact |
| --- | --- | --- |
| Scale Up or Down VM Cluster Memory | Time to drain services and Oracle RAC rolling restart  Typically 15-30 minutes per node, but may vary depending on application draining | Understanding application draining  See [Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md) before scaling down memory, ensure that database SGAs can still be stored in hugepages, and that application performance is still acceptable.  To preserve predictable application performance and stability:  - Monitor and scale up before important high workload patterns require the memory resources - Avoid memory scale down unless all of the database SGA and PGA memory fits into the new memory size, and the system's hugepages accommodate all SGAs |
| Scale Up or Down VM Cluster CPU | Online operation, typically less than 5 minutes for each VM cluster  Scaling up from a very low value to a very high value (10+ OCPUs increase) may take 10 minutes. | To preserve predictable application performance and stability:  - Monitor and scale up before important high workload patterns require the CPU resources, or when consistently reaching an OCPU threshold for a tolerated amount of time - Only scale down if the load average is below the threshold for at least 30 minutes, or scale down based on fixed workload schedules (such as business hours with 60 OCPUs, non-business hours with 10 OCPUs, and batch with 100 OCPUs) - Avoid more than one scale-down request within a 2 hour period |
| Scale Up or Down (resize) ASM Storage for Database usage | Typically minutes to hours  Time varies based on utilized database storage capacity and database activity. The higher the percentage of utilized database storage, the longer the resize operation (which includes ASM rebalance) will take. | Oracle ASM rebalance is initiated automatically. Storage redundancy is retained. Because of the inherent best practice of using a non-intrusive ASM power limit, application workload impact is minimal.  Choose a non-peak window so resize and rebalance operations can be optimized.  Because the time may vary significantly, plan for the operation to be completed in hours. To estimate the time that an existing resize or rebalance operation per VM cluster requires, query `GV$ASM_OPERATION`. For example, you can run the following query every 30 minutes to evaluate how much work (`EST_WORK`) and how much more time (`EST_MINUTES`) potentially is required:  `select operation, pass, state, sofar, est_work,                                         est_minutes from gv$asm_operation where                                         operation='REBAL';`  Note that the estimated statistics tend to become more accurate as the rebalance progresses, but can vary based on the concurrent workload. |
| Scale Up VM Local /u02 File System Size (Exadata X9M and later) | Online operation, typically less than 5 minutes for each VM cluster | VM local file system space is allocated on local database host disks, which are shared by all VM guests for all VM clusters provisioned on that database host.  Do not scale up space for Local /u02 File System unnecessarily on one VM cluster, such that no space remains to scale up on other VM clusters on the same Exadata Infrastructure, because a Local /u02 File System scale down must be performed in an Oracle RAC rolling manner, which may cause application disruption. |
| Scale Down VM Local /u02 File System Size | Time to drain services and Oracle RAC rolling restart  Typically 15-30 minutes for each node, but may vary depending on application draining settings. | To plan, learn about application draining at [Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md) |
| Adding Exadata Storage Cells | The online operation creates more available space for administrators to choose how to distribute.  Typically, 3-72 hours per operation, depending on the number of VM clusters, database storage usage, and storage activity. With a very active database and heavy storage activity, this can take up to 72 hours.  As part of the add storage cell operation, there are two parts to this operation:  1. Storage is added to the Exadata system as part of the add storage operation. 2. The administrator must decide which VM cluster to expand its ASM disk groups as a separate operation. | Plan to add storage when your storage capacity utilization hits 80% within a month, because this operation may be completed in days.  Oracle ASM rebalance is initiated automatically. Storage redundancy is retained. Because of inherent best practices in using non-intrusive ASM power limits, the impact of application workload is minimal.  Because the time duration may vary significantly, plan to complete the operation days before the storage is available.  To estimate the time that an existing resize or rebalance operation will take on each VM cluster, query `GV$ASM_OPERATION`. For example, you can run the following query every 30 minutes to evaluate how much work (`EST_WORK`) and how much more time (`EST_MINUTES`) is potentially required:  `Select operation, pass, state, sofar, est_work,                                         est_minutes from gv$asm_operation where                                         operation='REBAL';`  Note that the estimated statistics tend to become more accurate as the rebalance progresses, but can vary based on the concurrent workload. |
| Adding Exadata Database Servers | Online operation to expand your VM cluster  One-step process to add the Database Compute to the Exadata infrastructure and then expand the VM cluster  Approximately 1 to 6 hours for each Exadata Database Server | Plan to add Database Compute when your database resource utilization reaches 80% within a month. Be aware, and plan for this operation to take many hours to a day.  Choose a non-peak window so that the add Database Compute operation can be completed faster.  Each Oracle RAC database registered by Oracle Clusterware and visible in the Oracle Cloud Console is extended. If a database was configured outside the Oracle Cloud Console, or without dbaascli, it will not be extended. |
| Adding or Dropping Database Nodes in Virtual Machines (VMs) Cluster | Zero database downtime when adding Database Nodes in the VM cluster. Typically takes 3-6 hours, depending on the number of databases in the VM cluster.  Zero database downtime when dropping Database Nodes in the VM cluster. Typically takes 1-2 hours, depending on the number of databases in the VM cluster. | Understand that the add/drop operation is not instantaneous, and the operation may take several hours to complete.  The drop operation reduces database computing, OCPU, and memory resources so that application performance can be impacted. |

### Achieving Continuous Availability For Your Applications

As part of Oracle Exadata Database Service on Dedicated Infrastructure on Oracle Database in a Multicloud solution, all software updates (except for non-rolling database upgrades or non-rolling patches) can be done online or with Oracle RAC rolling updates to achieve continuous database uptime.

Furthermore, any local failures of storage, Exadata network, or Exadata database server are managed automatically, and database uptime is maintained.

To achieve continuous application uptime during Oracle RAC switchover or failover events, follow these application-configuration best practices:

- Use Oracle Clusterware-managed database services to connect your application. For Oracle Data Guard environments, use role-based services.
- Use the recommended connection string with built-in timeouts, retries, and delays so that incoming connections do not see errors during outages.
- Configure your connections with Fast Application Notification.
- Drain and relocate services. Use the recommended best practices in the table below that support draining, such as test connections, when borrowing or starting batches of work, and return connections to pools between uses.
- Leverage Application Continuity or Transparent Application Continuity to replay in-flight uncommitted transactions transparently after failures.

For more details, see [Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md). Oracle recommends testing your application readiness by following [Validating Application Failover Readiness (My Oracle Support Doc ID 2758734.1)](https://support.oracle.com/rs?type=doc&id=2758734.1).

Depending on the Oracle Exadata Database Service planned maintenance event, Oracle attempts to automatically drain and relocate database services before stopping any Oracle RAC instance. For OLTP applications, draining and relocating services typically work very well and result in zero application downtime.

Some applications, such as long-running batch jobs or reports, may not be able to drain and relocate gracefully within the maximum draining time. For those applications, Oracle recommends scheduling the software planned maintenance window around these types of activities or stopping these activities before the planned maintenance window. For example, you can reschedule a planned maintenance window to run outside your batch windows or stop batch jobs before a planned maintenance window.

Special consideration is required during rolling database quarterly updates for applications that use database OJVM. See [My Oracle Support Doc ID 2217053.1](https://support.oracle.com/rs?type=doc&id=2217053.1) for details.

The following table lists planned maintenance events that perform Oracle RAC instance rolling restart, as well as the relevant service drain timeout variables that may impact your application.

| Exadata Cloud Software Updates or Elastic Operation | Drain Timeout Variables |
| --- | --- |
| Oracle DBHOME patch apply and database MOVE | Cloud software automation stops/relocates database services while honoring `DRAIN_TIMEOUT` settings defined by database service configuration (such as `srvctl`).<sup>1</sup>  You can override `DRAIN_TIMEOUT` defined on services using the option `drainTimeoutInSeconds` with command line operation `dbaascli dbHome patch` or `dbaascli database move`.  The Oracle Cloud internal maximum draining time supported is 2 hours. |
| Oracle Grid Infrastructure (GI) patch apply and upgrade | Cloud software automation stops/relocates database services while honoring `DRAIN_TIMEOUT` settings defined by database service configuration (such as `srvctl`).<sup>1</sup>  You can override the `DRAIN_TIMEOUT` defined on services using the option `drainTimeoutInSeconds` with command line operation `dbaascli grid patch` or `dbaascli grid upgrade`.  The Oracle Cloud internal maximum draining time supported is 2 hours. |
| Virtual Machine Operating System Software Update (Exadata Database Guest) | Exadata `patchmgr/dbnodeupdate` software program calls drain orchestration (`rhphelper`).  Drain orchestration has the following drain timeout settings (see [My Oracle Support Doc ID 2385790.1](https://support.oracle.com/rs?type=doc&id=2385790.1) for details):  - `DRAIN_TIMEOUT` – If a service does not have `DRAIN_TIMEOUT` defined, then the default value of 180 seconds is used. - `MAX_DRAIN_TIMEOUT` - Overrides any higher `DRAIN_TIMEOUT` value defined by database service configuration. The default value is 300 seconds. There is no maximum value.  The `DRAIN_TIMEOUT` settings defined by the database service configuration are honored during service stop/relocate. |
| Exadata X9M and later systems  Scale Down VM Local File System Size | Exadata X9M and later systems call drain orchestration (`rhphelper`).  Drain orchestration has the following drain timeout settings (see [My Oracle Support Doc ID 2385790.1](https://support.oracle.com/rs?type=doc&id=2385790.1) for details):  - `DRAIN_TIMEOUT` – If a service does not have `DRAIN_TIMEOUT` defined, then the default value of 180 seconds is used. - `MAX_DRAIN_TIMEOUT` - Overrides any higher `DRAIN_TIMEOUT` value defined by database service configuration. The default value is 300 seconds.  The `DRAIN_TIMEOUT` settings defined by the database service configuration are honored during service stop/relocate.  The Oracle Cloud internal maximum draining time supported for this operation is 300 seconds. |
| Exadata X9M and later systems  Scale Up or Down VM Cluster Memory | Exadata X9M and later systems call drain orchestration (`rhphelper`).  Drain orchestration has the following drain timeout settings (see [My Oracle Support Doc ID 2385790.1](https://support.oracle.com/rs?type=doc&id=2385790.1) for details):  - `DRAIN_TIMEOUT` – If a service does not have `DRAIN_TIMEOUT` defined, then the default value of 180 seconds is used. - `MAX_DRAIN_TIMEOUT` - Overrides any higher `DRAIN_TIMEOUT` value defined by database service configuration. The default value is 300 seconds.  The `DRAIN_TIMEOUT` settings defined by the database service configuration are honored during service stop/relocate.  The Oracle Cloud internal maximum draining time supported for this operation is 900 seconds. |
| Oracle Exadata Cloud Infrastructure (ExaDB) software update | The ExaDB-D database host calls drain orchestration (`rhphelper`).  Drain orchestration has the following drain timeout settings (see [My Oracle Support Doc ID 2385790.1](https://support.oracle.com/rs?type=doc&id=2385790.1) for details):  - `DRAIN_TIMEOUT` – If a service does not have `DRAIN_TIMEOUT` defined, then the default value of 180 seconds is used. - `MAX_DRAIN_TIMEOUT` - Overrides any higher `DRAIN_TIMEOUT` value defined by database service configuration. The default value is 300 seconds.  The `DRAIN_TIMEOUT` settings defined by the database service configuration are honored during service stop/relocate.  The Oracle Cloud internal maximum draining time supported for this operation is 500 seconds.  Enhanced Infrastructure Maintenance Controls:  To achieve draining time longer than the Oracle Cloud internal maximum, leverage the custom action capability of Enhanced Infrastructure Maintenance Controls, which allows you to suspend infrastructure maintenance before the next database server update starts, directly stop/relocate database services running on the database server, and then resume infrastructure maintenance to proceed to the next database server. See [Configure Oracle-Managed Infrastructure Maintenance](https://docs.oracle.com/iaas/exadata/doc/ecc-vw-maint-hist.html#ECCCM-GUID-94A6038F-6329-46BC-AEBD-E5491D67B72F) in Oracle Cloud Infrastructure documentation for details. |

<sup>1</sup> Minimum software requirements to achieve this service drain capability are: Oracle Database release 12.2 and later and the latest cloud DBaaS tooling software.