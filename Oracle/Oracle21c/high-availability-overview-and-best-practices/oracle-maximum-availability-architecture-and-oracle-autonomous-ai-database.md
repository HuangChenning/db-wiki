---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/oracle-maximum-availability-architecture-and-oracle-autonomous-ai-database.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 34 Oracle Maximum Availability Architecture and Oracle Autonomous Database

Oracle Maximum Availability Architecture (MAA) represents Oracle's comprehensive framework of best practices, reference blueprints, and technologies for ensuring the highest levels of Oracle Database availability, data protection, and disaster recovery.

For users of Oracle Autonomous Database, whether leveraging the elastic, self-service Autonomous Database Serverless or the powerful, dedicated resources of Autonomous Database on Exadata Dedicated Infrastructure, the principles and capabilities of MAA are not a separate set of components to configure; they are the fundamental architecture upon which the service is built and automatically managed.

This fully automated, standardized Autonomous Database infrastructure means that achieving robust availability and disaster recovery for your mission-critical data is dramatically simplified and automated with Autonomous Database. The complexities typically associated with designing, implementing, and maintaining MAA configurations, such as setting up Real Application Clusters and infrastructure redundancy for fast failover for local failures, and setting up Autonomous Data Guard for additional high availability within a region or cross-region disaster recovery, are primarily handled by the Autonomous Database service.

Autonomous Database follows MAA best practices, using integrated technologies to provide built-in resilience, automated failover, and streamlined data protection. This self-managing approach reduces operational overhead and ensures your database benefits from Oracle's highest availability standards with minimal manual intervention. This includes built-in managed services that handle software updates and hardware maintenance, database backup and recovery, system and database monitoring and alerting, and zero downtime for elastic system changes such as increasing CPU and storage requirements.

The following topics provide the latest MAA certifications and observations for each of Oracle Autonomous Database Cloud services.

- [Oracle MAA for Oracle Autonomous Database on Dedicated Exadata Infrastructure](autonomous-database-dedicated-exadata-infrastructure.md)
- [Oracle MAA for Oracle Autonomous Database Serverless](autonomous-database-serverless.md)