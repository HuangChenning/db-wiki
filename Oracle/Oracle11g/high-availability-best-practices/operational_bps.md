---
title: Operational Prerequisites to Maximizing Availability
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/operational_bps.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 2 Operational Prerequisites to Maximizing Availability

Use operational best practices to provide a successful MAA implementation.

This chapter contains the following topics:

## 2.1 Understand Availability and Performance SLAs

Understand and document your high availability and performance service-level agreements (SLAs) and create an outage and solution matrix:

- Document the business's cost of downtime, Recovery Time Objectives (RTO or recovery time) and Recovery Point Objectives (RPO or data loss tolerance) for the outages described in [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/toc.htm).
- Build an outage and solution matrix similar those shown in [Table 13-1, "Recovery Times and Steps for Unscheduled Outages on the Primary Site"](outage.md) and [Table 14-1, "Solutions for Scheduled Outages on the Primary Site"](schedule_outage.md).

## 2.2 Implement a High Availability Environment

Implement a high availability environment to achieve the optimal high availability architecture:

- Install or update your software with the latest certified patch sets
- Configure your software using best practices
- Document your choices and configuration

## 2.3 Validate Your Performance and Availability SLAs

Validate and automate repair operations to ensure that you meet your target HA service-level agreements (SLAs). You should validate the backup, restore, and recovery operations and periodically evaluate all repair operations for various types of possible outages (see [Table 13-1](outage.md) for more information).

If you use Oracle Data Guard for disaster recovery and data protection, Oracle recommends that you perform periodic switchover operations or conduct full application and database failover tests. Also, periodically execute Application and Data Guard switchovers to fully validate all role transition procedures. For more information see Section 2.8, "Execute Data Guard Role Transitions".

## 2.4 Set up and Use Security Best Practices

Corporate data can be at grave risk if placed on a system or database that does not have proper security measures in place. A well-defined security policy can help protect your systems from unwanted access and protect sensitive corporate information from sabotage. Proper data protection reduces the chance of outages due to security breaches. For more information, see the [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/toc.htm).

## 2.5 Establish Change Control Procedures

Institute procedures that manage and control changes as a way to maintain the stability of the system and to ensure that no changes are incorporated in the primary database unless they have been rigorously evaluated on your test systems.

Review the changes and get feedback and approval from your change management team, which should include representatives for any component that affects the business requirements, functionality, performance, and availability of your system. For example, the team can include representatives for end-users, applications, databases, networks, and systems.

## 2.7 Use Proper Testing and Patching Practices

Proper testing and patching are important prerequisites for preventing instability. You must validate any change in your test systems thoroughly before applying it to your production environment. These practices involve the following:

- Configuring the Test System and QA Environments
- Performing Pre-production Validation Steps

### 2.7.1 Configuring the Test System and QA Environments

The test system should be a close replica of the production and standby environment and workload to execute functional tests, performance tests, and availability tests (for more information, see [Table 13-1](outage.md)). Any changes should be validated in the test environment first, including evaluating the effect of changes and the fallback procedures before introducing the changes in the production environment.

With a properly configured test system, many problems can be avoided because changes are validated with an equivalent production and standby database configuration containing a full data set and using a workload framework to mimic production (for example, using Oracle Real Application Testing).

Do not try to reduce costs by eliminating the test system because that decision ultimately affects the stability and the availability of your production applications. Using only a subset of system resources for testing and QA has the tradeoffs shown in Table 2-1.

Table 2-1 Tradeoffs for Different Test and QA Environments

| Test Environment | Benefits and Tradeoffs |
| --- | --- |
| Full Replica of Production and Standby Systems | Validate all patches and software changes.  Validate all functional tests.  Full performance validation at production scale.  Full HA validation. |
| Full Replica of Production Systems | Validate all patches and software changes.  Validate all functional tests.  Full performance validation at production scale.  Full HA validation minus the standby system.  No functional, performance, HA and disaster recovery validation with standby database. |
| Standby System | Validate most patches and software changes. Validate all functional tests.  Full performance validation if using Data Guard Snapshot Standby but this can extend recovery time if a failover is required.  Role transition validation.  Resource management and scheduling is required if standby and test databases exist on the same system. |
| Shared System Resource | Validate most patches and software changes. Validate all functional tests.  This environment may be suitable for performance testing if enough system resources can be allocated to mimic production.  Typically, however, the environment includes a subset of production system resources, compromising performance testing/validation.  Resource management and scheduling is required. |
| Smaller or Subset of the system resources | Validate all patches and software changes. Validate all functional tests.  No performance testing at production scale.  Limited full-scale high availability evaluations. |
| Different hardware or platform system resources but same operating system | Validate most patches and software changes. Limited firmware patching test.  Validate all functional tests unless limited by new hardware features.  Limited production scale performance tests.  Limited full-scale high availability evaluations. |

See Also:

[Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/rat_intro.htm#RATUG101)

### 2.7.2 Performing Pre-production Validation Steps

Pre-production validation and testing of software patches or any change is an important way to maintain stability. The high-level pre-production validation steps are:

1. Review the patch or upgrade documentation or any document relevant to that change. Evaluate the possibility of performing a rolling upgrade if your SLAs require zero or minimal downtime. Evaluate any rolling upgrade opportunities to minimize or eliminate planned downtime. Evaluate whether the patch qualifies for Standby-First Patching.
	Note:
	Standby-First Patch enables you to apply a patch initially to a physical standby database while the primary database remains at the previous software release (this applies to certain types of patches and does not apply to Oracle patch sets and major release upgrades; use the Data Guard transient logical standby method for patch sets and major releases). Once you are satisfied with the change, then perform a switchover to the standby database. The fallback is to switchback if required. Alternatively, you can proceed to the following step and apply the change to your production environment. For more information, see "Oracle Patch Assurance - Data Guard Standby-First Patch Apply" in My Oracle Support Note 1265700.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1265700.1`
2. Validate the application in a test environment and ensure the change meets or exceeds your functionality, performance, and availability requirements. Automate the procedure and be sure to also document and test a fallback procedure. This requires comparing metrics captured before and after patch application on the test and against metrics captured on the production system. Real Application Testing may be used to capture the workload on the production system and replay it on the test system. AWR and SQL Performance Analyzer may be used to assess performance improvement or regression resulting from the patch.
	Validate the new software on a test system that mimics your production environment, and ensure the change meets or exceeds your functionality, performance, and availability requirements. Automate the patch or upgrade procedure and ensure fallback. Being thorough during this step eliminates most critical issues during and after the patch or upgrade.
	See Section 2.7.1, "Configuring the Test System and QA Environments" for more information about configuring your test system.
3. Optionally, use the Oracle Real Application Testing option that enables you to perform real-world testing of Oracle Database. Oracle Real Application Testing captures production workloads and assesses the impact of system changes before production deployment; thus, Oracle Real Application Testing minimizes the risk of instabilities associated with changes. Oracle GoldenGate can also be used as another logical replica to apply changes.
	See Section 2.7.1, "Configuring the Test System and QA Environments" for more information about configuring your test system.
4. If applicable, perform final pre-production validation of all changes on a Data Guard standby database before applying them to production. Apply the change in an Oracle Data Guard environment, if applicable. For more information about Data Guard transient logical standby method, see [Section 14.2.6, "Database Upgrades"](schedule_outage.md).
5. Apply the change in your production environment.

See Also:

- [Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/rat_intro.htm#RATUG101)
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB00708) for complete information about Converting a Physical Standby Database into a Snapshot Standby Database
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rollup.htm#SBYDB4884) for more information about Performing a Rolling Upgrade With an Existing Physical Standby Database
- Oracle GoldenGate For Windows and UNIX Administrator's Guide for more information about Oracle GoldenGate
- The MAA white paper, "Database Rolling Upgrades Made Easy by Using a Data Guard Physical Standby Database", from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`
- See "Oracle Patch Assurance - Data Guard Standby-First Patch Apply" in My Oracle Support Note 1265700.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1265700.1`

## 2.8 Execute Data Guard Role Transitions

When you have a standby database(s), it is important to ensure that the operations and DBA teams are well prepared to use the standby database(s) at anytime when the primary database is down or underperforming, according to a predetermined threshold. By reacting and executing efficiently, which includes detection and making the decision to failover, overall downtime can be reduced from hours to minutes.

If you use Oracle Data Guard for disaster recovery and data protection, Oracle recommends that you perform periodic switchover operations every quarter or conduct full application and database failover tests. For more information about configuring Oracle Data Guard and role transition best practices, see [Chapter 9, "Configuring Oracle Data Guard"](config_dg.md) and [Section 9.4.1, "Oracle Data Guard Switchovers Best Practices."](config_dg.md)

See:

My Oracle Support provides notes for Data Guard switchovers:
- If you are using SQL\*Plus, see "11.2 Data Guard Physical Standby Switchover Best Practices using SQL\*Plus" in My Oracle Support Note 1304939.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1304939.1`
- If you are using the Data Guard Broker or Enterprise Manager, see "11.2 Data Guard Physical Standby Switchover Best Practices using the Broker" in My Oracle Support Note 1305019.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1305019.1`

## 2.9 Establish Escalation Management Procedures

Establish escalation management procedures so repair is not hindered. Most repair solutions, when conducted properly are automatic and transparent with the MAA solution. The challenges occur when the primary database or system is not meeting availability or performance SLAs and failover procedures are not automatic as in the case with some Data Guard failover scenarios. Downtime can be prolonged if proper escalation policies are not followed and decisions are not made quickly.

Availability is the top priority, and a contingency plan should be created to gather sufficient data for future Root Cause Analysis (RCA).

For more information about MAA outage and repair, check the MAA web page on the Oracle Technology Network (OTN) at

`http://www.oracle.com/goto/maa`

## 2.10 Configure Monitoring and Service Request Infrastructure for High Availability

To maintain your High Availability environment, you should configure the monitoring infrastructure that can detect and react to performance and high availability related thresholds. Also, where available, Oracle can detect failures, dispatch field engineers, and replace failing hardware without customer involvement.

### 2.10.1 Configure Monitoring Infrastructure for High Availability

You should configure and use Enterprise Manager and the monitoring infrastructure that detects and reacts to performance and high availability related thresholds to avoid potential downtime. The monitoring infrastructure assists you with monitoring for High Availability and enables you to do the following:

- Monitor system, network, application, database and storage statistics
- Monitor performance and service statistics
- Create performance and high availability thresholds as early warning indicators of system or application problems

See Also:

- [Chapter 12, "Monitoring for High Availability"](monitor.md)
- [Oracle Enterprise Manager Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=EMADM9021) for information about detecting and reacting to potential problems and failures

### 2.10.2 Configure Service Request Infrastructure

In addition to monitoring infrastructure with Enterprise Manager in the Oracle HA environment where available, Oracle can detect failures, dispatch field engineers, and replace failing hardware without customer involvement. For example, Oracle Auto Service Request (ASR) is a secure, scalable, customer-installable software solution available as a feature. The software resolves problems faster by using auto-case generation for Oracle's Sun server and storage systems when specific hardware faults occur.

See Also:

See "Oracle Auto Service Request" in My Oracle Support Note 1185493.1 at

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1185493.1`

## 2.11 Check the Latest MAA Best Practices

MAA solutions continue to emerge for all platforms and for different Exadata Database Machine releases. Periodically check the MAA web page on the Oracle Technology Network (OTN) at

`http://www.oracle.com/goto/maa`