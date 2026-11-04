---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-maa-best-practices-oracle-data-guard.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 14 Overview of MAA Best Practices for Oracle Data Guard

By adding a physical standby database with Oracle Active Data Guard, a Silver MAA reference architecture is elevated to a Gold MAA reference architecture. Implement Oracle Data Guard best practices to achieve minimal downtime and potentially zero data loss for all unplanned outages.

Oracle Active Data Guard plays an important role in delivering the high availability and comprehensive data protection that you expect of the Gold MAA reference architecture. The Gold reference architecture, consisting of an Oracle RAC primary database and Oracle RAC standby systems with Oracle Active Data Guard, plus MAA configuration and life cycle operations, provides a comprehensive set of services that create, maintain, manage, and monitor one or more standby databases. Oracle Active Data Guard protects your data during all types of planned maintenance activities, such as software updates and major database upgrades, and unplanned outages, including database failures, site outages, natural disasters, and data corruptions.

The goal of Oracle Data Guard best practices is to help you implement tested and proven MAA best practices to ensure a successful and stable Data Guard deployment. The following steps connect you to the Oracle MAA best practices for planning, implementing, and maintaining this type of architecture.

1. Plan your Oracle Data Guard architecture, and take into account various considerations for the application, network, and so on.
2. Configure and Deploy Data Guard using Oracle MAA best practices.
3. Tune and Troubleshoot your Data Guard deployment.

To learn more about the Gold MAA reference architecture, see [High Availability Reference Architectures](https://www.oracle.com/webfolder/technetwork/tutorials/architecture-diagrams/high-availability-overview/high-availability-reference-architectures.html).