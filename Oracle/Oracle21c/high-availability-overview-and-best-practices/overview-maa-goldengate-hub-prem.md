---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-maa-goldengate-hub-prem.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Overview of MAA GoldenGate Hub

To achieve the highest levels of availability, resulting in zero or near-zero downtime for both unplanned outages and planned maintenance activities, customers frequently use the combination of Oracle Real Application Clusters (Oracle RAC), Oracle Active Data Guard, and Oracle GoldenGate.

This architecture, typically referred as Platinum MAA or Never Down Architecture, delivers near zero Recovery Time Objective (RTO, or downtime incurred during outage) and potentially zero or near zero Recovery Point Objective (RPO, or data loss potential).

Traditionally, Oracle GoldenGate is installed and run locally on the database server that the GoldenGate processes connect to. When used with Oracle Grid Infrastructure Standalone Agent (XAG), Oracle GoldenGate processes can be configured to seamlessly relocate or fail over between Oracle RAC nodes and follow Oracle Active Data Guard switchover and failovers.

Using MAA Oracle GoldenGate Hub (MAA GGHub) moves the GoldenGate software and processes off of the Exadata database servers, reducing complexity and system resource utilization. MAA GGHub centralizes Oracle GoldenGate management and offloads the majority of the Oracle GoldenGate processing and associated CPU and storage resource utilization from Exadata system resources. Connectivity between the GoldenGate processes and the databases they operate against is managed with Oracle Net Services.

Extreme availability that delivers zero or near zero downtime (RTO=0 or near zero), and zero or near zero data loss (RPO=0 or near zero), typically requires the following Platinum MAA architecture where:

1. A source database and target database in an Oracle GoldenGate architecture that allows your application to fail over immediately in cases of disaster (database, cluster, or site failure) or switch over in cases of database or application upgrade. This architecture enables the potential RTO of zero or near zero for disaster scenarios and database and application upgrade maintenance.
2. Each source and target database is deployed on Exadata systems so that any local failures are tolerated or recovered almost instantly.
3. Each source and target database is configured with a standby database with Data Guard Fast-Start Failover so that any failure of the database results in activating a new primary database in seconds to minutes. If synchronous (SYNC) transport is leveraged with Maximum Availability Protection mode, zero data loss Data Guard failover is achieved.
4. Oracle GoldenGate replication is configured using MAA GGHub between the source and target databases. Bi-directional replication is commonly configured where the target database replicates other data back to the source using a second GoldenGate configuration.
5. Any standby that becomes a primary database because of Data Guard switchover or failover automatically resynchronizes with its target GoldenGate database. If zero data loss Data Guard switchover or failover occurs, GoldenGate resychronization ensures zero data loss across the distributed database environment.
6. GoldenGate is configured with Automatic Conflict Detection and Resolution, which is required after any Data Guard failover operation occurs.

To achieve an MAA Platinum solution on-premises, you follow these high level steps:

1. Deploy or migrate your database onto Exadata Database Machine
2. Add symmetric standby databases.
3. Configure and deploy Oracle Data Guard Fast Start Failover using the Oracle MAA best practice recommendations in [Configure Fast Start Failover](configure-and-deploy-oracle-data-guard.md).
4. Set up MAA GGHub, which is detailed in the topics that follow.
5. Configure Bidirectional Replication and Automatic Conflict Detection and Resolution. See [Bi-Directional Replication](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-configuring-bi-directional-replication.html) and [Automatic Conflict Detection and Resolution](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-automatic-cdr.html).
6. Decide on application failover options such as Global Data Services (see [Oracle Global Data Services Best Practices](oracle-global-data-services-best-practices.md)), or use your own customized application failover.