---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-multitenant-best-practices.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 42 Overview of Oracle Multitenant Best Practices

Oracle Multitenant is Oracle's strategic product for database consolidation.

The benefits of the Oracle Multitenant architecture include:

- Access isolation between individual Pluggable Databases (PDBs) stored in the same Container Database (CDB)
- Ability to manage many databases with the simplicity of managing just one CDB that contains many PDBs. By backing up your CDB, updating the CDB software or setting up a standby CDB for disaster recovery, you are essentially reducing the complexity and steps by administrating one CDB instead of applying the same administrative steps on many independent databases. You reduce administrative tasks, steps and errors.
- Sharing of system resources to reduce CAPEX with the flexibility to set resource limits for things like memory, I/O and on a per PDB level
- Flexibility to operate on an individual PDB, for example relocating a single PDB into another container and upgrading just that PDB
- Rapid cloning and provisioning
- Tight integration with Oracle RAC

The following table highlights various Oracle Multinenant configuration and operational best practices. All best practices should be used for on-premises environments. Many of them have been automated in Oracle Cloud Infrastructure (OCI).

Table 42-1 Oracle Multitenant configuration and operational best practices

| Use Case | Best Practices | Oracle Cloud Infrastructure Support |
| --- | --- | --- |
| Pluggable Database (PDB) configuration | For all Oracle RDBMS releases 12c Release 2 (12.2) to 21c, configure the CDB with local undo mode  See [Undo Modes in 12.2 Multitenant Databases - Local and Shared Modes (Doc ID 2169828.1)](https://support.oracle.com/rs?type=doc&id=2169828.1) | Supported as part of CDB and PDB creation |
| PDB service management | Mandatory MAA best practices for any Oracle databases with Oracle Clusterware (for example, Oracle RAC and single instance databases with Oracle Clusterware installed)  1. Never use PDB default services, nor SAVED STATE (except during relocate operations), nor database triggers to manage role-based services. 2. Use clusterware-managed distinct services per PDB for your application service, and leverage that application service to connect to the database. 3. When defining a clusterware-managed application service, define which PDB and services will be started and in which RAC instance and database role. 4. For Data Guard, always use role-based services by assigning a role to each clusterware-managed service.  If the above practices are applied, you will have predictable service management during PDB open and Data Guard role transitions. This will lead to higher application service availability and avoid application errors.  For single instance databases without MAA-recommended Oracle clusterware setup, follow these practices:  1. Never use PDB default services. 2. Use distinct services per PDB for your application service, and leverage that application service to connect to the database. 3. For non-Data Guard, use only SAVED state to open PDBs and start up explicit application services OR for Data Guard, use only AFTER STARTUP database triggers to programmatically manage which application services should be started depending on primary, READ ONLY, or snapshot standby database role.  See [Best Practices for Pluggable Database End User and Application Connection and Open on Database Startup (Doc ID 2833029.1)](https://support.oracle.com/rs?type=doc&id=2833029.1) | OCI creates non-default services as part of PDB creation. Ensure that they are used. |
| Using Data Guard with Oracle Multitenant | The following My Oracle Support notes provide operational best practice recommendations when using Oracle Multitenant in an Oracle Data Guard configuration.  - [Data Guard Impact on Oracle Multitenant Environments (Doc ID 2049127.1)](https://support.oracle.com/rs?type=doc&id=2049127.1) - [Making Use Deferred PDB Recovery and the STANDBYS=NONE Feature with Oracle Multitenant (Doc ID 1916648.1)](https://support.oracle.com/rs?type=doc&id=1916648.1) during use cases: PDB creation, PDB migration, and PDB cloning - [Reusing the Source Standby Database Files When Plugging a PDB into the Primary Database of a Data Guard Configuration (Doc ID 2273829.1)](https://support.oracle.com/rs?type=doc&id=2273829.1) for PDB migration - [Reusing the Source Standby Database Files When Plugging a non-CDB as a PDB into the Primary Database of a Data Guard Configuration (Doc ID 2273304.1)](https://support.oracle.com/rs?type=doc&id=2273304.1) for PDB migration - [Using standby\_pdb\_source\_file\_dblink and standby\_pdb\_source\_file\_directory to Maintain Standby Databases when Performing PDB Remote Clones or Plugins (Doc ID 2274735.1)](https://support.oracle.com/rs?type=doc&id=2274735.1) for PDB remote clone or PDB plug-in - [Parameter enabled\_pdbs\_on\_standby and STANDBYS Option With Data Guard Subset Standby (Doc ID 2417018.1)](https://support.oracle.com/rs?type=doc&id=2417018.1) to support subset standby | Data Guard Impact on Oracle Multitenant Environments ([Document 2049127.1](https://support.oracle.com/rs?type=doc&id=2049127.1)) provides useful information and should be reviewed. OCI automates PDB instantiation at the standby but does not support the following additional options:  - Making Use of the STANDBYS=NONE Feature with Oracle Multitenant [Document 1916648.1](https://support.oracle.com/rs?type=doc&id=1916648.1) - Reusing the Source Standby Database Files When Plugging a PDB into the Primary Database of a Data Guard Configuration [Document 2273829.1](https://support.oracle.com/rs?type=doc&id=2273829.1) - Reusing the Source Standby Database Files When Plugging a non-CDB as a PDB into the Primary Database of a Data Guard Configuration [Document 2273304.1](https://support.oracle.com/rs?type=doc&id=2273304.1) - Using standby\_pdb\_source\_file\_dblink and standby\_pdb\_source\_file\_directory to Maintain Standby Databases when Performing PDB Remote Clones or Plugins [Document 2274735.1](https://support.oracle.com/rs?type=doc&id=2274735.1) - Parameter enabled\_pdbs\_on\_standby and STANDBYS Option With Data Guard Subset Standby [Document 2417018.1](https://support.oracle.com/rs?type=doc&id=2417018.1) |
| Data Guard: PDB switchover and failover use cases | See [PDB Switchover and Failover in a Multitenant Configuration](pdb-switchover-and-failover-multitenant-configuration.md) | Oracle Cloud automation does not support PDB switchover and failover. |
| PDB migration | The following resources provide operational best practices for different types of PDB migration with minimal downtime:  - Use Zero Downtime Migration if your target is Exadata platform or cloud. See [https://www.oracle.com/database/technologies/rac/zdm.html](https://www.oracle.com/database/technologies/rac/zdm.html) - [Step by Step Process of Migrating non-CDBs and PDBs Using ASM for File Storage (Doc ID 1576755.1)](https://support.oracle.com/rs?type=doc&id=1576755.1) - [Cloning a Pluggable Database from an RMAN Container Database Backup (Doc ID 2042607.1)](https://support.oracle.com/rs?type=doc&id=2042607.1) - [PDB Switchover and Failover in a Multitenant Configuration](pdb-switchover-and-failover-multitenant-configuration.md) | Oracle Cloud Automation supports cloning a PDB from backups using its own automation. |
| PDB relocation | - [Using PDB Relocation to Upgrade an Individual PDB (Doc ID 2771716.1)](https://support.oracle.com/rs?type=doc&id=2771716.1) - [Using PDB Relocation to Move a Single PDB to Another CDB Without Upgrade (Doc ID 2771737.1)](https://support.oracle.com/rs?type=doc&id=2771737.1) | Oracle Cloud Automation supports both processes and automates end to end, including handling instantiation of the PDB at standby databases. |
| PDB resource management | The following My Oracle Support note provides operational use cases for Oracle Multitenant resource management:  [How to Control and Monitor the Memory Usage (Both SGA and PGA) Among the PDBs in Mutitenant Database- 12.2 New Feature (Doc ID 2170772.1)](https://support.oracle.com/rs?type=doc&id=2170772.1) | You can configure or modify resource plans and individual PDB settings for resource management tasks in Oracle cloud |

With Oracle Multitenant MAA solutions, you can achieve administration and system resource savings while still benefiting from various MAA solutions. The following tables highlight zero and near-zero downtime and data loss for various unplanned outages and planned maintenance activities.

Table 42-2 Unplanned Outages

| Unplanned Outages | Key Features for Solution | RTO | RPO |
| --- | --- | --- | --- |
| Recoverable node or instance failures | Real Application Cluster (RAC)  Application Continuity (AC) | Seconds | Zero |
| Database, cluster, and site failures | Active Data Guard fast-start failover | <2 Minutes | Zero or Seconds |
| Data corruptions | Active Data Guard that includes auto block repair of physical corruptions | Zero | Zero |
| PDB unrecoverable failure or "sick" PDB | PDB failover using Data Guard migrate command  Another target CDB on the same cluster is required  See [PDB Failover in a Data Guard environment: Using Data Guard Broker to Unplug a Single Failed PDB from a Standby Database and Plugging into a New Container or Migrate a Single PDB into a New Container (Doc ID 2088201.1)](https://support.oracle.com/rs?type=doc&id=2088201.1) | <2 Minutes | Zero or Seconds |
| PDB failover to active replica | Option 1: Failover entire CDB with Primary and Standby CDB Data Guard architecture  Option 2: Create PDB replica with Oracle GoldenGate. Perform PDB active failover using PDB replica in a different CDB.  Use Global Data Services and practices from [Application Checklist for Continuous Service for MAA Solutions](https://www.oracle.com/a/tech/docs/application-checklist-for-continuous-availability-for-maa.pdf) help with the application failover | Potentially Zero | Zero or Seconds |

Table 42-3 Planned Maintenance

| Planned Downtime | Solution | RTO |
| --- | --- | --- |
| Software and hardware updates | Real Application Cluster (RAC)  [Application Checklist for Continuous Service for MAA Solutions](https://www.oracle.com/a/tech/docs/application-checklist-for-continuous-availability-for-maa.pdf) | Zero |
| Major database upgrade for entire CDB | Active Data Guard DBMS\_ROLLING | Seconds |
| Major database upgrade for single PDB within CDB | PDB Relocate + Upgrade  See [Using PDB Relocation to Upgrade an Individual PDB (Doc ID 2771716.1)](https://support.oracle.com/rs?type=doc&id=2771716.1) | Minutes |
| Migration to remote CDB | PDB Relocate  See [Using PDB Relocation to Move a Single PDB to Another CDB Without Upgrade (Doc ID 2771737.1)](https://support.oracle.com/rs?type=doc&id=2771737.1) | Minutes |
| Migration to remote CDB (logical migration) | Data Pump and Oracle GoldenGate or Zero Downtime Migration | Potentially Zero |