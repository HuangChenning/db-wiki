---
title: Optimizing Manageability
book: Database High Availability Overview
doc_id: E17157-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17157/manageability.htm
tags:
  - oracle
  - 11g
  - high-availability-overview
---

## 6 Optimizing Manageability

Complex environments demand coordinated configuration changes, system upgrades, and new application rollouts. The topics in this section describe the tools that can be used to automate and simplify operations in high availability architectures, allowing you to step toward self-managing Oracle databases.

This section contains these topics:

## 6.1 Intelligent Infrastructure

Oracle Database has a sophisticated self-management infrastructure that allows the database to learn about itself and use this information to adapt to workload variations or to automatically remedy almost any potential problem. The self-management infrastructure <sup>Foot 1</sup> includes the following:

- Automatic Workload Repository
	The Automatic Workload Repository (AWR) is a built-in repository that contains performance statistics used by Oracle Database for problem-detection and self-tuning purposes. At regular intervals, Oracle Database makes a snapshot of vital statistics and workload information and stores the snapshots in the AWR. The data contained in the snapshots is then analyzed by the Automatic Database Diagnostic Monitor (ADDM).
	See [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for information about the AWR and ADDM.
- Active Session History
	Transient performance problems are short-lived and do not appear in the ADDM analysis. To address these problems, you can use Active Session History (ASH) to start sampling active sessions when the database starts. In particular, ASH samples can be collected:
	- Before the database is mounted, such as on an Oracle ASM instance.
		- When the database is mounted but not open, such as on an Oracle Data Guard physical standby instance.
		- When the database is mounted but open read-only, such as on an Oracle Active Data Guard physical standby instance (also known as the real-time query feature).
	Note:
	Active session history sampling is available for Oracle Active Data Guard instances and Oracle Automatic Storage Management (ASM) instances. However, not all Intelligent Infrastructure features are available on Oracle Data Guard configurations for this release.
	On a physical standby instance, the ASH data on disk represents activity on the primary database and the ASH data in memory represents activity on the standby database (in `V$ACTIVE_SESSION_HISTORY`). The ASH report prompts you to specify whether to generate the report using data sampled from the primary or standby database.
	See Also:
	- The topic about generating an ASH report on a specific database instance in [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF94211)
	- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB00707) for information about physical standby databases and Oracle Active Data Guard and real-time queries
	- The MAA white paper "Oracle Active Data Guard for Oracle Data Guard 11g Release 1" at `http://www.oracle.com/goto/maa`
- Automatic Maintenance Tasks
	By analyzing the information stored in the AWR, the database can identify the need to perform routine maintenance tasks. The automated maintenance tasks infrastructure (AutoTask) enables Oracle Database to automatically schedule such operations. AutoTask schedules automatic maintenance tasks to run in a set of Oracle Scheduler windows known as maintenance windows. Maintenance windows are those windows that are members of the Oracle Scheduler window group `MAINTENANCE_WINDOW_GROUP`. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) and the [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/toc.htm) for more information.
- Fault diagnosability infrastructure
	Oracle Database includes an advanced fault diagnosability infrastructure for preventing, detecting, diagnosing, and resolving problems. The problems that are targeted are critical errors such as those caused by database code bugs, metadata corruption, and customer data corruption. The diagnosability infrastructure includes:
	- The automatic diagnostic repository (ADR), which is a file-based repository for database diagnostic data such as traces, the alert log, health monitor reports, and more. It has a unified directory structure across multiple instances and multiple products.
		- The incident packaging services that a database administrator can use to automatically and easily gather all diagnostic data (traces, health check reports, SQL test cases, and more) pertaining to a critical error and package the data into a zip file suitable for transmission to Oracle Support Services.
	See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about these components.
- Server-generated alerts
	For problems that cannot be resolved automatically (such as running out of space) and require administrators to be notified, Oracle Database provides server-generated alerts. Oracle Database can monitor itself and send out alerts to notify you of any problem and to recommend how the reported problem can be resolved. This ensures quick problem resolution and helps prevent potential failures.
- Advisor framework
	Oracle Database includes a number of advisors for different subsystems in the database to automatically determine how the operation of the corresponding subcomponents could be further optimized. The SQL Tuning Advisor and the SQL Access Advisor, for example, provide recommendations for running SQL statements faster. Memory advisors help to size the various memory components without resorting to trial-and-error techniques. The Segment Advisor handles space-related issues, such as recommending wasted-space reclamation and analyzing growth trends, whereas the Undo Advisor guides you in sizing the undo tablespace correctly. See [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/toc.htm) for more information about using advisors.

## 6.2 Change Assurance

Oracle Database provides automatic capture and replay of workloads before and after changes so that you can analyze the effect of a database or a SQL change:

- Database Replay
	The Database Replay feature enables you to perform real-world testing by capturing the actual database workload on the production system and replaying it on the test system. It also provides analysis and reporting to highlight potential problems (for example, errors encountered and divergence in performance) and recommend ways to remedy the problems.
- SQL Performance Analyzer
	SQL performance regression is always a concern during system changes such as database upgrades, initialization parameter changes, and adding or dropping indexes. The SQL Performance Analyzer feature alleviates this concern by providing a way to assess the effect of a change on the performance of SQL statements by comparing and contrasting their response times before and after the change. SQL Performance Analyzer enables you to capture the SQL workload from the source system, such as the production database, and to replay it on the test system where the change has been applied.

For more information, see [Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/toc.htm).

## 6.3 Oracle Enterprise Manager Grid Control

By reducing the amount of human intervention required to execute routine and repetitive tasks, services become more stable, reliable, and available. This is particularly important when administrators must manage very large numbers of systems as efficiently as possible.

Oracle Enterprise Manager Grid Control is an HTML-based interface that provides the administrator with complete monitoring across the entire Oracle technology stack—business applications, application servers, databases, and the E-Business Suite—and non-Oracle components. If a component of fast application notification (FAN) becomes unavailable or experiences performance problems, then Grid Control displays the automatically generated alert so that the administrator can take the appropriate recovery action.

The components of Grid Control include:

- Oracle Management Service (OMS)
	The OMS feature is now a set of J2EE applications that renders the interface for Grid Control, works with all Management Agents to process monitoring information, and uses the Management Repository as its persistent data store.
- Oracle Management Agents
	These are processes deployed on each monitored host to monitor all targets on the host, communicate that information to the OMS, and maintain the host and its targets.
- Oracle Management Repository
	This is a schema in Oracle Database that contains all available information about administrators, targets, and applications managed by Grid Control.

Communication between Grid Control, the OMS, and Oracle Management Agents is done through HTTP. Also, you can enable Secure Sockets Layer (SSL) to allow secure communications between tiers in firewall-protected environments. The Management Agent uploads collected monitoring data to the OMS, which in turn loads the data into the Management Repository. Changes in a target state (such as an availability state change) result in an alert being generated to Grid Control.

Using Grid Control, an administrator can:

- Monitor architecture components and be alerted when a failure occurs
- View overall system status, such as the number of nodes in the database cluster and their current status
- View alerts aggregated across all instances
- Set thresholds for alert generation for each database on a clusterwide basis
- Monitor performance metrics across all instances
- Perform database clusterwide operations such as backup and recovery
- Interconnect monitoring of cluster databases

See Also:

- [Oracle Enterprise Manager Grid Control Installation and Basic Configuration](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OEMCN) and [Oracle Enterprise Manager Concepts](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OEMCN) for more information about Oracle Enterprise Manager Grid Control
- The "Using Enterprise Manager Grid Control to Implement or Extend High Availability with Oracle Database 11g and Oracle Data Guard" white paper at
	```
	http://www.oracle.com/goto/maa
	```

---

Footnote Legend

Footnote 1: To use many of the self-management features described in this section, you must purchase licenses for Oracle Diagnostics Pack. See Oracle Database Licensing Information for complete licensing information about Oracle management packs.