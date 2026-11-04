---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/oracle-ai-database-high-availability-overview.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Part I Oracle Database High Availability Overview

- [Overview of High Availability](overview-of-ha.md)
- [High Availability and Data Protection – Getting From Requirements to Architecture](https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/ha-requirements-architecture.html#GUID-7EB6D827-A30E-4E76-BAF8-0AF4DDCAD2C2 "Any effort to design and implement a high availability strategy for Oracle Database begins by performing a thorough business impact analysis to identify the consequences to the enterprise of downtime and data loss, whether caused by unplanned or planned outages.The business impact analysis categorizes the business processes based on the severity of the impact of IT-related outages.A complete business impact analysis provides the insight needed to quantify the cost of unplanned and planned downtime.The business impact analysis determines your tolerance to downtime, also known as the recovery time objective (RTO).The business impact analysis also determines your tolerance to data loss, also known as a recovery point objective (RPO).A manageability goal is more subjective than either the RPO or the RTO. You must make an objective evaluation of the skill sets, management resources, and tools available in an organization, and the degree to which the organization can successfully manage all elements of a high availability architecture.Understanding the total cost of ownership (TCO) and objectives for return on investment (ROI) are essential to selecting a high availability architecture that also achieves the business goals of your organization.The business impact analysis will help you document what is already known. The outcome of the business impact analysis provides the insight you need to group databases having similar RTO and RPO objectives together.Oracle MAA best practices define high availability reference architectures that address the complete range of availability and data protection required by enterprises of all sizes and lines of business.The Bronze tier is appropriate for databases where simple restart of a failed component (e.g. listener, database instance, or database) or restore from backup is \"HA and DR enough.\"The Silver tier provides an additional level of high availability for databases that require minimal or zero downtime in the event of database instance or server failure, as well as most common planned maintenance events, such as hardware and software updates.The Gold tier raises the stakes substantially for business-critical applications that cannot tolerate high RTO and RPO for any disasters such as database, cluster, corruptions, or site failures. Additionally, major database upgrades or site migrations can be done in seconds.The Platinum tier introduces two architecture patterns: Oracle GoldenGate replication with Oracle Database 19c Oracle Active Data Guard and Oracle AI Database 26ai and later releases.The Diamond tier introduces builds on MAA Platinum with Oracle GoldenGate, and is ideal for extremely mission critical systems.Each MAA reference architecture delivers known and tested levels of downtime and data protection.")
- [Features for Maximizing Availability](ha-features.md)
- [Oracle Database High Availability Solutions for Unplanned Downtime](ha-unplanned-downtime.md)
- [Oracle Database High Availability Solutions for Planned Downtime](ha-planned-downtime.md)
- [Enabling Continuous Service for Applications](enabling-continuous-service-applications.md)
- [Operational Prerequisites to Maximizing Availability](operational-prerequisites-maximizing-availability1.md)