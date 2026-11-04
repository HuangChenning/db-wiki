---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-oracle-ai-database-cloud-best-practices.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 33 Overview of Oracle Database Cloud Best Practices

Oracle Cloud and MAA collaborate closely to enable customer success using the various Oracle Database Cloud services.

This partnership ensures

- Databases, Grid Infrastructure, Exadata, and infrastructure are deployed and configured with MAA best practices in [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/), including public cloud, [OCI Dedicated Region](https://www.oracle.com/cloud/cloud-at-customer/dedicated-region/), [Oracle Database@Azure](https://www.oracle.com/cloud/azure/oracle-database-at-azure/), [Oracle Database@Google Cloud](https://www.oracle.com/cloud/google/oracle-database-at-google-cloud/), [Oracle Daabase@AWS](https://www.oracle.com/cloud/aws/), and [Exadata Cloud@Customer](https://www.oracle.com/engineered-systems/exadata/cloud-at-customer/).
- Cloud life cycle practices such as patching, backup and restore, disaster recovery, and pluggable database management incorporate MAA optimizations as new features and capabilities are introduced into the Oracle cloud.
- Oracle Cloud owns and manages network, system, and Exadata infrastructure using MAA practices and optimizations.
	The only exception is in Oracle Multicloud where you can choose to use AWS, Azure, or Google's network between application and database tiers, or network between database tiers for Oracle Data Guard and Oracle GoldenGate architectures. Oracle typically recommends using Oracle "OCI" network between Data Guard configurations to reduce additional network hops.
- Oracle high availability and disaster recovery (HA/DR) solutions meet our Enterprise customer standards for Gold and Platinum MAA solutions.

For the latest details, see [Oracle Cloud Maximum Availability Architecture](https://www.oracle.com/a/tech/docs/cloud-maa-overview.pdf).

MAA Cloud Certification Matrix

The following table indicates which MAA Reference Architectures are certified on each Oracle Database cloud service.

| Oracle AI Database Cloud Service | MAA Bronze | MAA Silver | MAA Gold - Cross-AD | MAA Gold - Cross-Region | MAA Platinum | MAA Diamond |
| --- | --- | --- | --- | --- | --- | --- |
| Oracle ExaDB-D | Certified | Certified | Certified | Certified | Certified | Certified |
| Oracle ExaDB-C@C | Certified | Certified | Certified | Certified | Certified | Planned |
| Oracle ExaDB-XS | Certified | Certified | Certified | Certified | Planned | Planned |
| Oracle ADB-S | Certified | Certified | Certified | Planned | Planned | Planned |
| Oracle ADB-D | Certified | Certified | Certified | Certified | Certified with Oracle Active Data Guard on Oracle AI Database 26ai | Planned |
| Oracle BaseDB without Oracle RAC | Reevaluation Planned | Reevaluation Planned | Reevaluation Planned | Reevaluation Planned | N/A | N/A |
| Oracle DB@C-C with Oracle RAC | Certified | Certified | Certified | Planned | N/A | N/A |

For multicloud, see [MAA Multicloud Certification Matrix](multilcoud-certification-matrix.md).

MAA Validated Solutions

The following topics outline MAA validated solutions and guidance for Oracle Database Cloud services.

Oracle Base Database Service (BaseDB)

| MAA Tier | Validated Solution |
| --- | --- |
| Bronze | BaseDB Single Instance  - Use Oracle Database cloud automation to configure the network and create DB Systems and databases - Use Oracle Database cloud automation for system and database life cycle operations, including software updates, upgrades, monitoring, alerting, and database administration and management. - Use a cloud-managed backup service. Recommended: Use (Zero Data Loss) Autonomous Recovery Service and real-time redo to reduce data loss in case of disasters - Customer responsibilities: 	- Create test systems to evaluate application, configuration, or software changes 		- Execute System and database sizing, resource management, and monitoring |
| Silver | Option 1: BaseDB 2-Node Oracle RAC (where available)  Bronze, plus the following:  - Use Oracle Database cloud automation to create multi-node Oracle RAC database systems on Oracle Cloud Infrastructure (OCI) - Customer responsibilities: 	- Maximize application failover and uptime with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)  Option 2: BaseDB Single Instance with Data Guard  Bronze, plus the following:  - Use Oracle Database cloud automation to create single instance database systems on Oracle Cloud Infrastructure (OCI) - Use cloud automation to create and manage a standby database. The location can be in another Availability Domain, Availability Zone, or Region for better fault isolation. - Customer responsibilities:  Bronze, plus the following:  - Customer responsibilities: 	- (Highly Recommended) Set up [Data Guard Fast Start Failover](https://docs.oracle.com/en/database/oracle/oracle-database/19/haovw/configure-and-deploy-oracle-data-guard.html#GUID-FA4AAC8F-EDA8-489F-9168-E83AE23B86F7) (automatic failover) with MAA practices to bound RTO after database, cluster, potentially Availability Domain or regional failure 		- Tune Data Guard if lagging (see [Overview of Oracle Data Guard Tuning and Troubleshooting](overview-oracle-data-guard-tuning.md)) 		- Extend application failover to standby ([Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)) or use [Full Stack Disaster Recovery Service](https://www.oracle.com/cloud/full-stack-disaster-recovery/). 		- Maximize application failover and uptime with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) |
| Gold | Base DB 2-Nodes Oracle RAC (where available) with Oracle Active Data Guard  Silver, plus the following:  - Recommended: primary and standby database systems are symmetric in shape and system resources. - Use cloud automation to create and manage a standby database. The location can be in another Availability Domain, Availability Zone, or Region for better fault isolation. - Customer responsibilities: 	- (Highly Recommended) Set up [Data Guard Fast Start Failover](https://docs.oracle.com/en/database/oracle/oracle-database/19/haovw/configure-and-deploy-oracle-data-guard.html#GUID-FA4AAC8F-EDA8-489F-9168-E83AE23B86F7) (automatic failover) with MAA practices to bound RTO after database, cluster, potentially Availability Domain or regional failure 		- Tune Data Guard if lagging (see [Overview of Oracle Data Guard Tuning and Troubleshooting](overview-oracle-data-guard-tuning.md)) 		- Extend application failover to standby ([Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)) or use [Full Stack Disaster Recovery Service](https://www.oracle.com/cloud/full-stack-disaster-recovery/). |
| Platinum | N/A |
| Diamond | N/A |

Oracle Exadata Database Service on Dedicated Infrastructure (ExaDB-D)

| MAA Tier | Validated Solutions |
| --- | --- |
| Bronze | N/A |
| Silver | ExaDB-D (Default)  - Use Oracle Database cloud automation to create Exadata infrastructure, VM cluster, and Oracle RAC databases. - Use Oracle Database cloud automation for system and database life cycle operations, including software updates, upgrades, monitoring, service events, health alerts, and database administration and management. - Use a cloud-managed backup service. Recommended: Use (Zero Data Loss) Autonomous Recovery Service and real-time redo to reduce data loss in case of disasters - Customer responsibilities: 	- Create test systems to evaluate application, configuration, or software changes. 		- Execute system and database sizing, resource management and monitoring, and reviewing exachk (holistic health) 		- Maximize application failover and uptime with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) |
| Gold | ExaDB-XS with Oracle Active Data Guard  Silver, plus the following:  - Recommended: primary and standby database systems are symmetric in shape and system resources. - Use cloud automation to create and manage a standby database. The location can be in another Availability Domain, Availability Zone, or Region for better fault isolation. - Customer responsibilities: 	- Set up [Data Guard Fast Start Failover](https://docs.oracle.com/en/database/oracle/oracle-database/19/haovw/configure-and-deploy-oracle-data-guard.html#GUID-FA4AAC8F-EDA8-489F-9168-E83AE23B86F7) (automatic failover) with MAA practices to bound RTO after database, cluster, potentially Availability Domain or regional failure 		- Tune Data Guard if lagging (see [Overview of Oracle Data Guard Tuning and Troubleshooting](overview-oracle-data-guard-tuning.md)) 		- Extend application failover to standby ([Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)) or use [Full Stack Disaster Recovery Service](https://www.oracle.com/cloud/full-stack-disaster-recovery/). |
| Platinum | Option 1: Upgrade MAA Gold to Oracle AI Database 26ai  Option 2: ExaDB-D with Oracle Active Data Guard and Oracle GoldenGate  Gold, plus the following customer responsibilities:  - Follow Oracle GoldenGate and MAA Platinum architectural solution for Oracle GoldenGate management and tuning ([MAA Platinum Reference Architecture Overview](maa-platinum-reference-architecture-overview.md)). - Extend application failover to Oracle GoldenGate replica with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) - Optionally use [Global Data Services](https://www.oracle.com/database/technologies/high-availability/global-data-services.html) for smart workload management between GoldenGate replicas and standby databases |
| Diamond | Platinum Option 2 with Oracle GoldenGate, and:  - Upgrade to Oracle AI Database 26ai - Upgrade to Oracle GoldenGate 26ai |

Oracle Exadata Database Service on Exascale Infrastructure (ExaDB-XS)

| MAA Tier | Validated Solution |
| --- | --- |
| Bronze | N/A |
| Silver | ExaDB-XS (Default)  - Use Oracle Database cloud automation to create Exadata infrastructure, VM cluster, and Oracle RAC databases. - Use Oracle Database cloud automation for system and database life cycle operations, including software updates, upgrades, monitoring, service events, and health alerts, and database administration and management. - Use a cloud-managed backup service. Recommended: Use (Zero Data Loss) Autonomous Recovery Service and real-time redo to reduce data loss in case of disasters. - Customer responsibilities: 	- Create test systems to evaluate application, configuration, or software changes. 		- Execute system and database sizing, resource management and monitoring, and reviewing exachk (holistic health) 		- Maximize application failover and uptime with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) |
| Gold | ExaDB-XS with Oracle Active Data Guard  Silver, plus the following:  - Recommended: primary and standby database systems are symmetric in shape and system resources. - Use cloud automation to create and manage a standby database. The location can be in another Availability Domain, Availability Zone, or Region for better fault isolation. - Customer responsibilities: 	- Set up [Data Guard Fast Start Failover](https://docs.oracle.com/en/database/oracle/oracle-database/19/haovw/configure-and-deploy-oracle-data-guard.html#GUID-FA4AAC8F-EDA8-489F-9168-E83AE23B86F7) (automatic failover) with MAA practices to bound RTO after database, cluster, potentially Availability Domain or regional failure 		- Tune Data Guard if lagging (see [Overview of Oracle Data Guard Tuning and Troubleshooting](overview-oracle-data-guard-tuning.md)) 		- Extend application failover to standby ([Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)) or use [Full Stack Disaster Recovery Service](https://www.oracle.com/cloud/full-stack-disaster-recovery/). |
| Platinum | Planned |
| Diamond | Planned |

Oracle Exadata Database Service on Cloud@Customer (ExaDB-C@C)

| MAA Tier | Validated Solutions |
| --- | --- |
| Bronze | N/A |
| Silver | ExaDB-C@C (Default)  - Use Oracle Database cloud automation to create Exadata infrastructure, VM cluster, and Oracle RAC databases. - Use Oracle Database cloud automation for system and database life cycle operations, including software updates, upgrades, monitoring, service events, and health alerts, and database administration and management. - Use a cloud-managed backup service. Recommended: Use Zero Data Loss Recovery Server and real-time redo to reduce data loss in case of disasters. - Customer responsibilities: 	- Create test systems to evaluate application, configuration, or software changes. 		- Execute system and database sizing, resource management and monitoring, and reviewing exachk (holistic health) 		- Maximize application failover and uptime with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) |
| Gold | ExaDB-C@C with Oracle Active Data Guard  Silver, plus the following:  - Recommended: primary and standby database systems are symmetric in shape and system resources. - Use cloud automation to create and manage a standby database. The location can be in another Availability Domain, Availability Zone, or Region for better fault isolation. - Customer responsibilities: 	- Set up [Data Guard Fast Start Failover](https://docs.oracle.com/en/database/oracle/oracle-database/19/haovw/configure-and-deploy-oracle-data-guard.html#GUID-FA4AAC8F-EDA8-489F-9168-E83AE23B86F7) (automatic failover) with MAA practices to bound RTO after database, cluster, potentially Availability Domain or regional failure 		- Tune Data Guard if lagging (see [Overview of Oracle Data Guard Tuning and Troubleshooting](overview-oracle-data-guard-tuning.md)) 		- Extend application failover to standby ([Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)) or use [Full Stack Disaster Recovery Service](https://www.oracle.com/cloud/full-stack-disaster-recovery/). |
| Platinum | Option 1: Upgrade MAA Gold with Oracle AI Database 26ai  Option 2: ExaDB-C@C with Oracle Active Data Guard and Oracle GoldenGate  Gold, plus the following:  - Extend application failover to GoldenGate replica ([Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)) - Optionally use [Global Data Services](https://www.oracle.com/database/technologies/high-availability/global-data-services.html) for smart workload management between GoldenGate replicas and standby databases - Customer's responsibilities: 	- Follow Oracle GoldenGate and MAA Platinum architectural solution for Oracle GoldenGate management and tuning ([MAA Platinum Reference Architecture Overview](maa-platinum-reference-architecture-overview.md)). |
| Diamond | Planned |

Autonomous Database Serverless (ADB-S)

| MAA Tier | Validated Solutions |
| --- | --- |
| Bronze | N/A |
| Silver | ADB-S (Default)  - Use Oracle Database cloud automation life cycle operations including software updates, upgrades, monitoring, and database administration and management. - Auto scaling CPU and storage resizing is possible - Customer Responsibilities: 	- Create test systems to evaluate application changes 		- Maximize application failover and uptime with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) 		- Update compute and storage limits when required ([Update Compute and storage limits](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database/serverless&id=ADBSB-GUID-73BA00C4-5B70-461B-AA8D-C124B4730FED) |
| Gold | ADB-S with Autonomous Data Guard  Silver, plus the following:  - Enable Autonomous Data Guard, choose automatic failover, and data loss tolerance to bound and meet RTO and RPO SLAs. The location can be in another Availability Domain for better fault isolation. Automatic standby failover is only available for a standby within the same region and is required for meeting Gold MAA solution. - Customer responsibilities: 	- Extend application failover to local standby ([Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md)) or use [Full Stack Disaster Recovery Service.](https://www.oracle.com/cloud/full-stack-disaster-recovery/) for cross region standby.  MAA Gold certification includes  - Option 1: Standby database within the same region (preferably in a different Availability Domain) - Option 2: Standby database within the same region with an additional cross-region Autonomous Data Guard standby. |
| Platinum | Planned |
| Diamond | Planned |

Autonomous Database on Dedicated Infrastructure (ADB-D)

| MAA Tier | Validated Solutions |
| --- | --- |
| Bronze | N/A |
| Silver | ADB-D (Default)  - Use Oracle Database cloud automation life cycle operations, including software updates, upgrades, monitoring, and database administration and management. - Customer responsibilities: 	- Create test systems to evaluate application changes 		- Maximize application failover and uptime with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) |
| Gold | ADB-D with Autonomous Data Guard  Silver, plus the following:  - Enable Autonomous Data Guard, choose protection mode, data loss tolerance, and enable automatic failover. The location can be in another Availability Domain or Region for better fault isolation. - Customer responsibilities: 	- Extend application failover to standby with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) or use [Full Stack Disaster Recovery Service](https://www.oracle.com/cloud/full-stack-disaster-recovery/). |
| Platinum | Option 1: Upgrade MAA Gold with Oracle AI Database 26ai  Option 2: ADB-D with Autonomous Data Guard and Oracle GoldenGate  Gold, plus the following customer responsibilities:  - Set up GoldenGate [Cloud Within Region: Configuring Oracle GoldenGate Hub for MAA Platinum](cloud-gghub-region.md). GoldenGate management and tuning. - Extend application failover to Oracle GoldenGate replica with [Achieving Continuous Availability For Your Applications](oracle-maximum-availability-architecture-oracle-exadata-cloud-systems.md) |
| Diamond | Planned |