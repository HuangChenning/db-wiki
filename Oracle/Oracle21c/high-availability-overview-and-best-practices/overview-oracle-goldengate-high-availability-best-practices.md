---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-oracle-goldengate-high-availability-best-practices.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 21 Overview of Oracle GoldenGate Best Practices

Configure Oracle GoldenGate using Oracle MAA best practices to get the highest availability and performance out of your Oracle GoldenGate deployment.

Oracle GoldenGate provides the following benefits:

- Uni-directional or bi-directional replication, allowing reads and updates in any replicated database.
- Data movement is in real-time, reducing latency.
- Replicated databases can run on different hardware platforms, database versions, and different database or application configurations, allowing for online migration. This flexibility also allows online database and application upgrades.
- Source and target replicated databases are online, ensuring zero downtime application switchover during outages and planned maintenance activities is possible. Note that application switchover must be customized, rather than using a built-in feature, such as Transparent Application Continuity.
- MAA Oracle GoldenGate Hub (MAA GGHub) can reduce the complexity and system resource utilization by moving GoldenGate software and processes off of the Exadata database servers.
- Dependable disaster recovery solutions by replicating data across different geographic locations. This allows for failover during regional outages or data center problems, minimizing recovery time objectives (RTO) and fulfilling recovery point objectives (RPO).

The following table highlights various Oracle GoldenGate configuration best practices and MAA Platinum best practices.

Table 21-1 Oracle GoldenGate Use Cases and Best Practices

| Use Case | Oracle GoldenGate Best Practices |
| --- | --- |
| Database migration to Oracle Cloud or Exadata Platform | [Zero Downtime Migration (ZDM) with GoldenGate](https://www.oracle.com/database/zero-downtime-migration/) (logical migration)  [Oracle Zero Downtime Migration – Logical Migration Performance Guidelines](https://www.oracle.com/a/tech/docs/zdm-gg-performance.pdf) |
| Database migration requiring minimal or zero downtime  Database migration involving cross platform or different database versions | [Oracle Database Migration with an Oracle GoldenGate Hub Configuration](https://www.oracle.com/a/tech/docs/maa-database-migration-with-a-goldengate-hub.pdf) |
| Deploy Oracle GoldenGate off of the database server in a Hub configuration | [Cloud Within Region: Configuring Oracle GoldenGate Hub for MAA Platinum](cloud-gghub-region.md)  [Cloud Across Regions: Configuring Oracle GoldenGate Hub for MAA Platinum](cloud-gghub-regions.md)  [On-Premises: Configuring Oracle GoldenGate Hub](premises-configuring-oracle-goldengate-hub.md) |
| Install and configure Oracle GoldenGate directly on the Oracle RAC database server or Exadata database system | [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md)  [On-Premises: Oracle GoldenGate Microservices Architecture with Oracle Real Application Clusters Configuration Best Practices](ogg-microservices-premises1.md) |
| Implement MAA Platinum or install and configure Oracle GoldenGate directly on Oracle RAC database servers with Oracle Active Data Guard | Oracle Cloud:  1. [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md) and 2. [Cloud MAA Platinum: Oracle GoldenGate Microservices Architecture Integrated with Active Data Guard](ogg-ma-cloud-rac-and-active-data-guard1.md)  On-premises systems:  1. [On-Premises: Oracle GoldenGate Microservices Architecture with Oracle Real Application Clusters Configuration Best Practices](ogg-microservices-premises1.md) and 2. [On-Premises MAA Platinum: Oracle GoldenGate Microservices Architecture Integrated with Active Data Guard](premises-maa-platinum-oracle-goldengate-microservices-architecture-integrated-active-data-gua.md) |
| Application failover options for Oracle GoldenGate | [Oracle Global Data Services Best Practices](oracle-global-data-services-best-practices.md) and  [Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md) |
| Oracle GoldenGate bidirectional replication and automatic conflict detection and resolution | For Oracle Cloud Service, [Oracle Cloud Infrastructure GoldenGate documentation](https://docs.oracle.com/en/cloud/paas/goldengate-service/index.html)  For on-premises, the latest [Oracle GoldenGate documentation](https://docs.oracle.com/en/database/goldengate/core/index.html)  For these Oracle GoldenGate or Platinum MAA architectures, active-active replication requires conflict detection and resolution, which includes [Automatic Conflict Detection and Resolution (Auto-CDR)](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-automatic-cdr.html) or the manual CompareCols / ResolveConflict (CC/RC) method of conflict detection and resolution. Also see [Manual Conflict Detection and Resolution](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-configure-conflict-detection-and-resolution.html) in Oracle GoldenGate documentation. |

Also see Oracle GoldenGate documentation at: [https://docs.oracle.com/en/middleware/goldengate/core/21.1/](https://docs.oracle.com/en/database/goldengate/core/index.html)

Overview of Oracle GoldenGate and Supporting Technologies

The technologies that are required to replicate data between databases are Oracle GoldenGate and supporting technologies (such as Oracle Grid Infrastructure Agents, ACFS or DBFS, or GoldenGate hub) to ensure that replication will resume after various failures. A brief overview of Oracle GoldenGate and supporting technologies are described here.

Oracle GoldenGate

Oracle GoldenGate provides real-time, log-based change data capture and delivery between homogenous and heterogeneous systems. This technology lets you construct a cost-effective and low-impact real-time data integration and continuous availability solution.

Oracle GoldenGate replicates data from committed transactions with transaction integrity and minimal overhead on your existing infrastructure. The architecture supports multiple data replication topologies, such as one-to-many, many-to-many, cascading, and bidirectional. Its wide variety of use cases includes real-time business intelligence; query offloading; zero-downtime upgrades and migrations; and active-active databases for data distribution, data synchronization, and high availability.

Oracle GoldenGate Microservices Architecture provides REST-enabled services. The REST-enabled services provide remote configuration, administration, and monitoring through HTML5 web pages, command line interfaces, and APIs.

Recommended Oracle GoldenGate 21c (and higher releases) introduces unified build support, so that a single software installation supports capturing and applying replicated data to multiple major Oracle Database versions (11g Release 2 to 21c). This is possible because an Oracle GoldenGate installation includes the required Oracle Database client libraries without requiring a separate database `ORACLE_HOME` installation.

Oracle Grid Infrastructure Agents

Oracle Grid Infrastructure Agents (XAG) are Oracle Grid Infrastructure components that provide the high availability (HA) framework to application resources and resource types managed through the agent management interface, AGCTL. This framework provides a complete, ready-to-use solution that contains pre-defined Oracle Grid Infrastructure resource configurations and agents to integrate applications for complete application HA.

The Oracle Grid Infrastructure Agents provide pre-defined Oracle Clusterware resources for Oracle GoldenGate, Siebel, Oracle PeopleSoft, JD Edwards, and Oracle WebLogic Server, as well as Apache and MySQL applications. Using the agent for Oracle GoldenGate simplifies the creation of dependencies on the source and target databases, the application VIP, and the file system (ACFS or DBFS) mount point. The agent command line utility (AGCTL) is used to start and stop Oracle GoldenGate, and can also be used to relocate Oracle GoldenGate between the nodes in the cluster.

Oracle Database File System (DBFS)

Oracle DBFS can be used to store Oracle GoldenGate files.

The Oracle Database File System (DBFS) creates a file system interface to files stored in the database. DBFS is similar to NFS in that it provides a shared network file system that looks like a local file system. Because the data is stored in the database, the file system inherits all the high availability and disaster recovery capabilities provided by Oracle Database.

With DBFS, the server is the Oracle Database. Files are stored as SecureFiles LOBs. PL/SQL procedures implement file system access primitives such as create, open, read, write, and list directory. The implementation of the file system in the database is called the DBFS SecureFiles Store. The DBFS SecureFiles Store allows users to create file systems that can be mounted by clients. Each file system has its own dedicated tables that hold the file system content.

Oracle Advanced Cluster File System (ACFS)

Oracle ACFS can be used to store Oracle GoldenGate files.

Oracle Advanced Cluster File System (Oracle ACFS) is a multi-platform, scalable file system, and storage management technology that extends Oracle Automatic Storage Management (Oracle ASM) functionality to support all customer files.

Oracle ACFS leverages Oracle Clusterware for cluster membership state transitions and resource-based high availability. Oracle ACFS is bundled into the Oracle Grid Infrastructure (GI) allowing for integrated optimized management of databases, resources, volumes, and file systems.