---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/autonomous-database-dedicated-exadata-infrastructure.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Oracle MAA for Oracle Autonomous Database on Dedicated Exadata Infrastructure

### Autonomous Database Dedicated with Default High Availability Option (MAA Silver)

High availability is suitable for all development, test, and production databases that have high uptime requirements and zero or low data loss tolerance.

By default, Autonomous Database is highly available, incorporating a multi-node configuration to protect against localized software and hardware failures.

Each Autonomous Database application service resides in at least one Oracle Real Application Clusters (Oracle RAC) instance, with the option to fail over to another available Oracle RAC instance for unplanned outages or planned maintenance activities, enabling zero or near-zero downtime.

Autonomous Database automatic backups are stored in Oracle Cloud Infrastructure Object Storage, and are replicated to another available domain if available. For Autonomous Database with Exadata Cloud at Customer, you have the option to back up to NFS, Oracle Cloud Infrastructure Object Storage, or Zero Data Loss Recovery Appliance (ZDLRA); however, replication of those backups in NFS or ZDLRA is the responsibility of the customer.

You can set up Automatic Backups with varying backup retention policy/period or on-demand manual backups including long-term backups. These backups can be used to restore the database in the event of a disaster. See [Backup and Restore Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcm/index.html#articletitle)

To achieve the application uptime SLOs where most months would be zero downtime, see Preparing Application for Seamless Application Failover.

The following table describes the recovery-time objectives and recovery-point objectives (data loss tolerance) for different outages.

Table 34-1 Default High Availability Policy Recovery Time (RTO) and Recovery Point (RPO) Service-level Objectives for Autonomous Database Dedicated

| Failure and Maintenance Events | Database Downtime | Service-level Downtime (RTO) | Potential Service-level Data Loss (RPO) |
| --- | --- | --- | --- |
| Localized events, including:  - Exadata cluster network topology failures - Storage (disk and flash) failures - Database instance failures - Database server failures - Periodic software and hardware maintenance updates | Zero | Near-zero | Zero |
| Events that require restoring from backup because a standby database does not exist:  - Data corruptions - Human error - Full database failures - Complete storage failures - Availability domain (AD) for multi-AD regions | Minutes to hours  (without Autonomous Data Guard) | Minutes to hours  (without Autonomous Data Guard) | 15 minutes for Autonomous Database on Dedicated Infrastructure(without Autonomous Data Guard) |
| Events that require non-rolling software updates or database upgrades | Minutes to an hour for Autonomous Database on Dedicated Infrastructure  (without Autonomous Data Guard) | Minutes to an hour for Autonomous Database on Dedicated Infrastructure  (without Autonomous Data Guard) | Zero |

In the table above, the amount of downtime for events that require restoring from a backup varies depending on the nature of the failure. In the most optimistic case, physical block corruption is detected, and the block is repaired with block media recovery in minutes. In this case, only a small portion of the database is affected with zero data loss. In a more pessimistic case, the entire database or cluster fails, then the database is restored and recovered using the latest database backup, including all archives.

Data loss is limited by the last successful archive log backup, the frequency of which is every 15 minutes for Autonomous Database on Dedicated Exadata Infrastructure. Archive or redo logs are backed up to Oracle Cloud Infrastructure Object Storage, or any supported Autonomous Database on Dedicated Exadata Infrastructure backup destination. Data loss can be seconds, or, at worst minutes of data loss, around the last successful archive log and remaining redo in the online redo logs that were not archived to backup destination.

All local failures incur zero database downtime because of built-in Exadata HA benefit and Oracle Cloud Infrastructure redundancy, and application brownouts are near zero or less 10 seconds. Software and hardware maintenance updates can incur zero database downtime and possible zero application impact because of online updates, Oracle RAC rolling updates, and application failover best practices. See Preparing Application for Seamless Application Failover.

### Autonomous Database Dedicated with Autonomous Data Guard Option (MAA Gold)

Enable Autonomous Data Guard for mission-critical production databases that require better uptime requirements for disasters from data corruptions, and database or site failures, while still reaping the Autonomous Database High Availability Option benefits. Additionally, a read-only standby database provides expanded application services to offload reporting, queries, and some updates.

You can also convert your physical standby database to a snapshot standby, but that impacts your Recovery Time Objective (RTO) if you have to switchover or failover to that specific standby.

Enabling Autonomous Data Guard adds one symmetric standby database to an Exadata rack that is located in the same availability domain, another availability domain, or in another region. The primary and standby database systems are configured symmetrically to ensure that performance service levels are maintained after Data Guard role transitions. Up to two standby databases are supported.

For additional protection, a typical MAA Gold architecture consists of a local standby with automatic failover enabled, and a cross-region standby for disaster recovery. For more information about managing an Autonomous Data Guard configuration, see [View the Status of an Autonomous Data Guard Configuration](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html#GUID-B86D1882-FC9E-41BF-9658-23CFAD91A666)

To meet bound Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) service-level objectives for database, cluster, or even site failures, enable Automatic Failover in the OCI Console Autonomous Data Guard Settings (see Updating Autonomous Data Guard Settings). You can choose which standby you want as the automatic failover target by updating Autonomous Data Guard Settings.

If RPO=0 or zero data loss is required, MAA customers typically deploy a local standby where the standby database is placed within the same availability domain or in a different availability domain in the same region. MAA recommends placing the standby in a separate availability domain if available. The round-trip latency between availability domains is typically less 1 millisecond, which in most cases has minimum application performance impact.

MAA recommends evaluating zero data loss configuration or Maximum Availability protection mode with Data Guard synchronous transport mode to ensure acceptable performance. If your RPO is near zero or minimum data loss is acceptable, you can choose any standby database to enable automatic failover, and configure a fast start failover lag limit to bound maximum data loss before initiating automatic failover.

If the target is a cross-region standby and cross-region disaster recovery orchestration is required, MAA recommends enabling OCI Full Stack Disaster Recovery service where applicable to orchestrate database, application, and possibly network DNS failover and switchover operations. See [Use OCI Full Stack Disaster Recovery on Autonomous Database on Dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/ufcif/index.html).

Backups

Backups are scheduled automatically for the standby database, and they are stored in Oracle Cloud Infrastructure Object Storage.

Autonomous Database with Exadata Cloud at Customer provides you with an option to backup to NFS, Oracle Cloud Infrastructure Object Storage, or Zero Data Loss Recovery Appliance; however, replication of those backups is your responsibility. Those backups can be used to restore databases in the event of a double disaster, where both primary and standby databases are lost.

You can set up Automatic Backups with varying backup retention policy/period or on-demand manual backups including long-term backups. See [Backup and Restore Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcm/index.html#articletitle).

Autonomous Data Guard Recovery Time (RTO) and Recovery Point (RPO) Service-level Objectives

The uptime recovery time objectives (downtime) and recovery point objectives (data loss) are low, as described in the table below.

To achieve the application uptime SLAs where most months would be zero downtime, see Preparing Application for Seamless Application Failover. The target uptime RTO applies to container databases with less 25 pluggable databases and does not include 30 seconds default detection time for automatic failover to standby.

| Failure and Maintenance Events | Service-level Downtime (RTO) <sup>1</sup> | Potential Service-level Data Loss (RPO) |
| --- | --- | --- |
| Localized events, including:  - Exadata cluster network fabric failures - Storage (disk and flash) failures - Database instance failures - Database server failures - Periodic software and hardware maintenance updates on primary or standby | Zero or Near Zero | Zero  Note:  Maintenance is typically applied on the standby first. For database software updates, the standby software is applied first, and after approximately a week the primary database software is updated. |
| Events that require failover to the standby database using Autonomous Data Guard, including:  - Data corruptions (because Active Data Guard has automatic block repair for physical corruptions2, a failover operation is required only for logical corruptions or extensive data corruptions) - Full database failures - Complete storage failures - Availability domain or region failures3 | A few seconds to two minutes <sup>4</sup> | Zero with maximum availability protection mode (uses synchronous redo transport). Most commonly used for intra-region standby databases.  Near zero for maximum performance protection mode (uses asynchronous redo transport). Most commonly used for cross-region standby databases. Also used for intra-regional standby databases and to ensure zero application impact. RPO is typically less than 10 seconds. RPO can be impacted by network bandwidth and workload throughput between primary and standby clusters. |

<sup>1</sup> Service-Level Downtime (RTO) excludes detection time that includes multiple heartbeats to ensure the source is indeed inaccessible before initiating an automatic failover.

<sup>2</sup> The Active Data Guard automatic block repair for physical corruptions feature is only available for Autonomous Data Guard on Dedicated Infrastructure.

<sup>3</sup> Regional failure protection is only available if the standby is located in another region.

<sup>4</sup> The back-end Autonomous Data Guard role transition timings are much faster than indicated by the Cloud Console refresh rates. Automatic Failover must be enabled to bound RTO.

Autonomous Database on Dedicated Infrastructure has been MAA Gold validated and certified. Autonomous Database on Dedicated Infrastructure was validated with a standby database in the same region, and also with a standby database in a different region, and the aboveRTO and RPOs were met when the standby target was symmetric to the primary. RTO and RPOs were met with redo rates of up to 1100 MB/sec.

Depending on workload, you may have to scale your Autonomous Exadata VM Cluster system resource on either the primary or standby clusters. Follow the instructions in [Manage Autonomous Exadata VM Cluster Resources](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcj/index.html#ADBCJ-GUID-574B2EC9-A13B-47EB-92F5-0B4D034A1B12).

#### Updating Autonomous Data Guard Settings

You can update the settings of an Autonomous Data Guard standby from the details page of the primary Autonomous Container Database in the configuration.

Required IAM Policies:

```
use autonomous-container-databases
```

1. Go to the details page of the primary Autonomous Container Database in the Autonomous Data Guard configuration.
	For instructions, see [View Details of an Autonomous Container Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbck/index.html).
2. Click Update Autonomous Data Guard from More actions.
	The Update Autonomous Data Guard dialog displays the current settings for Protection Mode and Automatic Failover.
3. You can make the following updates from this dialog:
	1. Protection mode: Select Maximum performance or Maximum availability from the drop-down list.
		2. Automatic failover: To bound RTO and RPO, automatic failover needs to be enabled.
		If automatic failover is not enabled already, you can enable it by selecting Enable automatic failover. Similarly, you can deselect Enable automatic failover to disable automatic failover for this Autonomous Data Guard setup.
		If one of your standby databases is in the same region as the primary database, and the second is in a different region, the local standby database is prioritized over the remote standby as the automatic failover target. When you enable automatic failover, any of the standby databases is considered for the automatic failover target.
		Note:
		You can not enable Automatic Failover for databases with cross-region Autonomous Data Guard setup on Exadata Cloud@Customer deployments.
		3. Fast start failover lag limit: If automatic failover is enabled and the protection mode is Maximum Performance, the Fast Start Failover lag limit value is displayed in seconds. By default, this value is set to 30 seconds, but you can change it to any value between 5 and 3600 seconds.
4. Save your changes.

#### Autonomous Data Guard Life Cycle Management

1. Setting up Standby or Adding Standby with Automatic Failover: see [Manage Autonomous Data Guard Configuration](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html#articletitle)
2. Monitoring Transport and Apply Lags
	1. You can view the Autonomous Data Guard details by selecting Autonomous Data Guard groups or Autonomous Data Guard associations under Resources. The Autonomous Data Guard table displays information about the peer container database, the current apply lag and transport lag, state, and last role change and creation dates. See [Manage Primary and Standby Databases in an Autonomous Data Guard Configuration](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/hkuka/#articletitle)
		2. Set alarms for `ApplyLag` and `TransportLag` to ensure the standby is in sync and protecting your primary database. See [Using the Console](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/lbdmm/index.html#GUID-B28C699E-0CBC-4843-8AB5-501BB0C160A9)
3. Data Guard Role Transitions or Reinstate Standby: see Switchover or Failover topics in [Manage Autonomous Data Guard Configuration](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html#articletitle)
4. Automatic Failover Notifications can be set up using information in [Events for Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/arfad/index.html)

#### MAA Autonomous Data Guard RTO and RPO Observations

The following table illustrates several configurations that MAA testing and evaluation show achieve Gold MAA tier RTO and RPOs. This was achieved after hundreds of role transitions with various database and cluster outages.

| Primary Cluster | Standby Cluster | PDBs | Data Files | Services | Timing (minutes) |
| --- | --- | --- | --- | --- | --- |
| 2 Node | 2 Node | 1 | 14 | 2 | 1:18 |
| 2 Node | 2 Node | 5 | 50 | 10 | 1:20 |
| 2 Node | 2 Node | 25 | 300 | 250 | 1:44 |
| 4 Node | 4 Node | 1 | 500 | 12 | 1:17 |

Autonomous Data Guard Failover Improvements

The tables below illustrate how role transition times have improved in Oracle 23ai.

Large CDB with Single PDB: Data Guard Failover Improvements

- Data Guard configured with between primary Exadata (4 node RAC) and standby Exadata (4 node RAC) X9
- CDB version 23.4 with one PDB, 500 data files, and 12 services
- Workload running: OLTP Swingbench against PDB during role transition
- Redo rate 100MB/second at CDB level with no lag

| Oracle release | Close to mount | Term recovery | Media recovery | Convert to primary | CDB open | PDB open + srv start | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Oracle 19c (19.22) | 00:14 | 00:17 | 00:05 | 00:01 | 00:06 | 00:50 | 01:17 |
| Oracle 23ai (23.4) Release Label | 00:04 | 00:07 | 00:08 | 00:01 | 00:06 | 00:07 | 00:29  (62% drop) |

CBD with 5 PDBs: Data Guard Failover Improvements

- Data Guard configured with between primary Exadata (2 node RAC) and standby Exadata (2 node RAC)
- CDB version 23.4 with 5x PDB
- 50 total data files spread across the 5 PDBs
- 10 services - 2 per PDB
- Workload running: OLTP Swingbench against each PDB during role transition
- Redo rate ~60MB/second on the CDB
- All improvements in timing have been the result of code fixes

| Oracle release | Close to mount | Term recovery | Media recovery | Convert to primary | CDB open | PDB open + srv start | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ExaCS Oracle 19c (19.18 + fixes) | 00:19 | 00:25 | 00:05 | 00:01 | 00:15 | 00:24 | )1:20 |
| Oracle 23ai (23.4) Release Label | 00:02 | 00:03 | 00:01 | 00:01 | 00:04 | 00:04 | 00:15  (81% drop) |

### Autonomous Database with Autonomous Data Guard Option and Oracle GoldenGate (MAA Platinum)

MAA Platinum with Autonomous Database on Dedicated Infrastructure is configurable. No guaranteed SLAs are provided since the GoldenGate and application failover configuration is manual.

MAA Platinum or Never-Down Architecture, delivers near-zero recovery time objective (RTO, or downtime incurred during an outage) and potentially zero or near zero recover point objective (RPO, or data loss potential).

The MAA Platinum with Autonomous Database on Dedicated Infrastructure ensures:

- RTO = zero or near-zero for all local failures
- RTO = zero or near-zero for disasters, such as database, cluster, or site failures, achieved by redirecting the application to an Autonomous Database with Autonomous Data Guard or Oracle GoldenGate replica
- Zero downtime maintenance for software and hardware updates
- Zero downtime database upgrade or application upgrade by redirecting the application to an upgraded Oracle GoldenGate replica residing in a separate Autonomous Database on Dedicated Infrastructure
- RPO = zero or near-zero data loss, depending on selecting the Oracle Data Guard Maximum Availability or Maximum Performance protection modes with synchronous redo transport in Autonomous Database with Autonomous Data Guard
- Fast re-synchronization and zero or near-zero RPO between Oracle GoldenGate source and target databases after a disaster using Cloud MAA GoldenGate Hub and Oracle GoldenGate best practices
- After any database failure, automatic failover to its standby database occurs automatically using integrated Data Guard Fast-start Failover (FSFO). Subsequently, automatic re-synchronization between Oracle GoldenGate source and target databases resumes from the new primary after a role transition. For synchronous transport, this leads to eventual zero data loss.

Prerequisites:

- Autonomous Database on Dedicated Infrastructure must be running Oracle Database software release 19.20 or later for GoldenGate conflict resolution support
- Autonomous Database with Autonomous Data Guard and automatic failover needs to be configured for fast GoldenGate resynchronization after a disaster
- GoldenGate setup must be done manually according to Cloud MAA best practices
- Application failover to an available GoldenGate replica or a new primary database must be configured. Currently, Global Data Services (GDS) cannot be used with an Autonomous Database in this architecture.

#### Implementing the MAA Platinum Solution

To achieve an MAA Platinum solution, review and leverage the technical briefs and documentation referenced in the following steps.

1. Review [Oracle MAA Platinum Tier for Oracle Exadata](https://www.oracle.com/a/tech/docs/exadata-maa-platinum-focused.pdf) to understand MAA Platinum benefits and use cases.
	1. Decide primary database locations based on application needs. The primary database will reside in Autonomous Database on Dedicated Infrastructure.
		2. Decide standby database location based on fault isolation requirements.
		3. Enable Autonomous Data Guard.
		4. Choose Autonomous Data Guard protection mode based on RPO tolerance, and set up automatic failover.
2. Set up MAA GoldenGate Hub in Oracle cloud.
	1. If all primary databases (GoldenGate replicas) are in the same region, see [Cloud Within Region: Configuring Oracle GoldenGate Hub for MAA Platinum](cloud-gghub-region.md).
		If primary databases (GoldenGate replicas) are spread across 2 regions, see [Cloud Across Regions: Configuring Oracle GoldenGate Hub for MAA Platinum](cloud-gghub-regions.md).
		2. Configure Bidirectional Replication and Automatic Conflict Detection and Resolution. See [Set Up Bidirectional Replication for Oracle GoldenGate Microservices Architecture](https://docs.oracle.com/en/middleware/goldengate/core/21.3/coredoc/quickstart-bidirectional-replication.html) or the latest [Oracle GoldenGate 21c documentation](https://docs.oracle.com/en/middleware/goldengate/core/21.3/mabooks.html).
3. Configure custom application failover options so that your application can fail over automatically in the case of database, cluster, or site failure.

### Preparing Application for Seamless Application Failover

Ensure that network connectivity to Oracle Cloud Infrastructure is reliable so that you can access your tenancy's Autonomous Database resources.

Follow the guidelines to connect to your Autonomous Database (see [Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbbd/index.html#articletitle)). Applications must connect to the predefined service name and download client credentials that include the proper `tnsnsames.ora` and `sqlnet.ora` files. You can also change your specific application service’s `drain_timeout` attribute to fit your requirements.

For more details about enabling continuous application service through planned and unplanned outages, see [Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md).

For Exadata cloud planned maintenance events that require restarting database instances, Oracle automatically relocates services and drain sessions to another available Oracle RAC instance before stopping any Oracle RAC instance. For OLTP applications that follow the MAA checklist, draining and relocating services results in zero application downtime.

Some applications, such as long-running batch jobs or reports, may not be able to drain and relocate gracefully, even with a longer drain timeout. For those applications, Oracle recommends that you schedule the software planned maintenance window excluding these types of activities, or stop these activities before the planned maintenance window. For example, you can reschedule a planned maintenance window so that it is outside your batch windows, or stop batch jobs before a planned maintenance window.

### Multicloud Considerations for Autonomous Data Guard

Autonomous Database on Dedicated Exadata Infrastructure is configured identically in Oracle's multicloud partners.

In Oracle’s multicloud architecture, infrastructure is organized using a parent–child site model. Autonomous Data Guard in Oracle Cloud Infrastructure (OCI) operates within this framework. In Oracle’s multicloud partnerships, the OCI-managed environment functions as the parent site, while the peered environment in the partner’s data center is the child site.

Autonomous Data Guard behaves the same in a multicloud deployment as it does in native OCI, for both local and cross-region standby configurations. In this model, all databases, including standby databases, reside in the multicloud partner’s data center or region (for example, Amazon Web Services (AWS)), while OCI provides orchestration and operational coordination.

With the databases residing in the multicloud partner's site, there are two distinct differences that may impact RTO and RPO:

- The multicloud partner's network peering or OCI network peering is used, and RPO can be impacted if network bandwidth is not sufficient to handle workload or redo generation.
- Data Guard observer (quorum), required for automatic failover, resides on the OCI site for additional fault isolation from primary and standby databases.

MAA Silver and Gold solutions for Autonomous Database on Dedicated Exadata Infrastructure are generally applicable in all of Oracle's multicloud partners that host Oracle Autonomous Database on Dedicated Exadata Infrastructure.

No additional MAA certification on Autonomous Databaseon Dedicated Exadata Infrastructure was conducted in the multilcoud partner's ecosystems. Given the similarities, Oracle MAA and Autonomous Database on Dedicated Exadata Infrastructure engineers expect similar MAA benefits and certifications.