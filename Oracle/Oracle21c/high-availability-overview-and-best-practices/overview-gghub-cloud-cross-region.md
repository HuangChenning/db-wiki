---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-gghub-cloud-cross-region.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Overview of MAA GoldenGate Hub

To achieve the highest levels of availability, resulting in zero or near-zero downtime for both unplanned outages and planned maintenance activities, you can use the combination of Oracle Real Application Clusters (Oracle RAC), Oracle Active Data Guard, and Oracle GoldenGate.

This architecture, typically referred as MAA Platinum, or Never Down Architecture, delivers near zero Recovery Time Objective (RTO--downtime incurred during outage) and potentially zero or near zero Recovery Point Objective (RPO--data loss potential).

Traditionally, Oracle GoldenGate is installed and run locally on the database server that the GoldenGate processes connect to. When used with Oracle Grid Infrastructure Standalone Agent (XAG), Oracle GoldenGate processes can be configured to seamlessly relocate or failover between Oracle RAC nodes and follow Oracle Active Data Guard switchover and failovers.

Using MAA Oracle GoldenGate Hub (MAA GGHub) moves the GoldenGate software and processes off of the Exadata database servers, reducing complexity and system resource utilization. MAA GGHub centralizes Oracle GoldenGate management and offloads the majority of the Oracle GoldenGate processing and associated CPU and storage resource utilization from Exadata system resources. Connectivity between the GoldenGate processes and the databases they operate against is managed with Oracle Net Services.

To achieve an MAA Platinum solution in the Oracle Cloud, you follow these high level steps:

1. Review [Oracle MAA Platinum Tier for Oracle Exadata](https://www.oracle.com/a/tech/docs/exadata-maa-platinum-focused.pdf) to understand Platinum MAA benefits and use cases.
2. Deploy or migrate your database onto Exadata Cloud Service, Base Database Service, or Autonomous Database on Dedicated Infrastructure Service.
3. Add symmetric standby databases in the Oracle Cloud using Oracle Cloud Control Plan or Cloud automation.
4. Configure and deploy Oracle Data Guard Fast Start Failover using the Oracle MAA best practice recommendations in [Configure Fast Start Failover](configure-and-deploy-oracle-data-guard.md). For Exadata Cloud Service and Base Database Service, this is manual step.
5. Set up MAA GGHub across different OCI regions, which is detailed in the topics that follow. For an MAA GGHub within one OCI region, see [Cloud Within Region: Configuring Oracle GoldenGate Hub for MAA Platinum](cloud-gghub-region.md).
6. Configure Bidirectional Replication and Automatic Conflict Detection and Resolution. See [Oracle Cloud Infrastructure GoldenGate documentation](https://docs.oracle.com/en/cloud/paas/goldengate-service/index.html) for information.
7. Decide on Application Failover Options such as Global Data Services (see [Oracle Global Data Services Best Practices](oracle-global-data-services-best-practices.md)), or use your own customized application failover.