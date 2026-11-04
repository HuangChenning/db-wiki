---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/migration-oracle-cloud-best-practices1.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 38 Migration to Oracle Cloud Best Practices

The following is a summary of cloud migration best practices, and provides links to resources where details can be found.

Use Zero Downtime Migration (ZDM)

Oracle MAA's simple, automated, one-button approach solution for moving your Oracle Databases into the Oracle Cloud

Use the latest ZDM version. See [Zero Downtime Migration](https://www.oracle.com/database/zero-downtime-migration/) for detailed product information and software kit download.

For cross-platform migration cases, such as migrating from AIX, Sparc, or Windows-based platforms to Linux platforms, ZDM uses data pump, RMAN, Transportable Tablespace (XTTS), and Oracle GoldenGate instantiation and migration options. ZDM supports online migration with Data Pump and Oracle GoldenGate, or offline migration with RMAN XTTS for data and Data Pump for metadata migration.

For cross-platform migration cases using Transportable Tablespace and RMAN Incremental Backups, see [KB144840](https://support.oracle.com/support/?documentId=KB144840). ZDM does not support Full Transportable Data Pump with RMAN Incremental Backup migrations.

Evaluate network and use high-bandwidth network

- See [Network Evaluation](maa-evaluations-multicloud-solutions.md)
- See [Assessing and Optimizing Network Performance](plan-oracle-data-guard-deployment.md)
- Network bandwidth impacts migration time. Migration downtime is impacted by switchover timings.

Plan and take the opportunity to refresh and optimize

Planning:

- Understand your HA and DR Service Level Agreements, and make sure you pick the correct cloud MAA reference architecture to meet those needs (see [Oracle Cloud Maximum Availability Architecture](https://www.oracle.com/a/tech/docs/cloud-maa-overview.pdf)). Also, see [Overview of Oracle Database Cloud Best Practices](overview-oracle-ai-database-cloud-best-practices.md).
- Understand and document your application performance Key Performance Indicators (KPIs).
- Understand if the target cluster will have one or many databases, and size it accordingly as described below.
- Plan to take advantage of new benefits when using Exadata, Exascale, other Oracle Database Cloud services or Autonomous Database.
- Understand what the maximum tolerated downtime for data migration is for your application. Note that migration options are significantly simpler when you can tolerate some downtime. The options depend on if you can tolerate hours (for example, using Backup/Restore, RMAN XTTS or Data Pump), seconds to low minutes (using Data Guard, for example) or near zero (using Oracle GoldenGate). Also, if possible, physical migration is a simpler solution requiring less operational and application investment.

Refresh and optimize:

- With logical database migration, you have an opportunity to optimize by reducing the number of data files by using BigFiles, restructure tables and indexes, or even drop indexes and make any schema redesigns. Any logical migration or optimization will add to migration planning and testing investments.
- Use Oracle cloud-supplied system configuration, server parameter file (SPFILE), and automation. Only change database initialization parameters that are relevant for resource performance sizing. MAA works with various database cloud services to ensure MAA best practice compliance to achieve the highest stability and availability.
- Do NOT migrate your undocumented parameters.
- Use cloud automation such as Cloud Control Plan or Oracle-supplied cloud automation instead of your on-premises custom scripts.

Size for success

Assess current workload and resource utilization

- Collect usage metrics: Use tools like Oracle Automatic Workload Repository (AWR), PerfHub, or Enterprise Manager to collect at least 7-30 days of actual workload data (CPU, Memory, Storage, IOPS, Throughput).
- Peak workload analysis: Identify peak periods to size for your maximum required capacity—not just the average.

Inventory and profile applications

- Database characteristics: List database count, size, growth rate, redundancy, high availability, and disaster recovery requirements.
- Workload type: OLTP, OLAP, mixed workloads, and any special database features or options in use (such as partitioning or compression).

Calculate core requirements

- CPU: Size based on peak CPU usage, considering future growth (typically add 20-30% headroom).
- Memory: Assess SGA and PGA memory usage, plus OS requirements.
- Consolidation: Factor additional resources if you are consolidating multiple databases or instances.

Storage sizing

- Capacity: Calculate size needed for data, indexes, online redo logs, and possibly standby redo logs, temp tablespace, undo, system, and sysaux space for DATA disk group RECO disk group contains archive logs (typically 24 hours), flashback logs (typically 24 hours, or same as archive log space), and in some cases database backups.
	For simplicity use Cloud Defaults of DATA 80% and RECO 20% when database backups are offloaded to Oracle cloud managed services, or DATA 40% and RECO 60% when database backups are local to the VM cluster.
- Performance: Consider flash IOPS for low latency, disk IOPS, storage throughput, and latency needs. Exadata storage provides high performance, so try to model storage needs for both capacity and speed. Incorporate ASM redundancy level in your calculations. Oracle Cloud uses ASM High Redundancy as a default for all database services using Exadata because of its superior data protection.

High availability and disaster recovery

- Redundancy: Choose correct Exadata or database shapes to meet your high availability SLAs.
- Data Guard needs: If you are using Oracle Data Guard, consider sizing your standby environments symmetrically so that performance KPIs are preserved after Data Guard role transitions.

Choose the right Exadata shape

- Match your computed requirements to the available Exadata Database Service shapes (for example, number of database/compute servers, storage servers, vCPU allocations).

Helpful Oracle tools and documentation

- [Oracle Cloud Capacity Analytics (OCCA):](https://occa.us.oracle.com/) Internal and partner-accessible tools for detailed sizing (reach out to your Oracle account team)
- Oracle Exadata Cloud Service Documentation: [Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/index.html), [Exadata Database Service on Exascale Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-database-exascale/index.html), [Exadata Database Service on Cloud@Customer](https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/index.html), or [Oracle Base Database Service](https://docs.oracle.com/en/cloud/paas/base-database/index.html)
- Oracle Database Performance Tuning Guide: [Measuring Database Performance](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=TGDBA-GUID-811E9E65-C64A-4028-A90E-102BBFF6E68F) and [Gathering Database Statistics](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=TGDBA-GUID-CBB1716F-2B20-4575-ADCE-94E33BEA53EF)

Prepare for high availability and disaster recovery

- Plan for application high availability (HA) and the best way to take most advantage of Oracle Real Application Clusters (RAC) benefits. See [Continuous Availability for Applications](continuous-availability-applications.md) and [Design and Deployment Techniques](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=RACAD-GUID-DD273C7C-7F74-4A95-B8E5-E007D36119D2) to enable applications and database consolidation in an Oracle RAC environment.
- Plan for disaster recovery (DR).
	- If DR is important, then add a Cloud standby to the target before migration.
		- Use Cloud automation and MAA best practices to create the standby database.
		- Understand how best to failover or switchover the application. Evaluate [Oracle Cloud Infrastructure Full Stack Disaster Recovery](https://docs.oracle.com/en/cloud/iaas/disaster-recovery/index.html) service.

Test and ensure you meet your performance and requirements

- Use ZDM `-eval` mode to create a test environment
- Evaluate application performance to ensure Key Performance Indicators (KPIs) and performance Service Level Agreements (SLAs) are met
- Evaluate simple outages to ensure application and HA SLAs are met
- Practice migration multiple times to ensure readiness

Cut over during low workload

- Pick a non-peak application window to do the migration.
- Establish a game plan to stay behind if issues arise.
- When possible, establish a fallback plan. For logical migration using Oracle GoldenGate, you will need to set up bi-directional replication. For physical migration using Data Guard, you need to use the ZDM parameter `ZDM_SKIP_DG_CONFIG_CLEANUP` so Data Guard transport can continue after migration.