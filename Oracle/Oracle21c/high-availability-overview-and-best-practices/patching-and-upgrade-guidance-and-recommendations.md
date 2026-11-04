---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/patching-and-upgrade-guidance-and-recommendations.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Patching and Upgrade Guidance and Recommendations

For patching lifecycle automation or Oracle-assisted patching services, Oracle recommends the following approaches.

Oracle Cloud Database Patching and Lifecycle Maintenance

- Oracle Autonomous Database is fully managed by Oracle.
- For co-managed Oracle Database services in Oracle Cloud Infrastructure or supported multicloud environments, Oracle manages the underlying infrastructure, and customers manage the VM guest and customer-controlled software with the automation provided by the service. Exadata Fleet Update provides fleet-level orchestration for Exadata Database Service updates.

Oracle Platinum Services

Oracle Platinum Services provides patching assistance for eligible on-premises engineered systems. It supports Exadata, Zero Data Loss Recovery Appliance, Oracle Grid Infrastructure, and Oracle Database software for certified configurations under applicable support terms. See [Oracle Platinum Services](https://www.oracle.com/assets/oracle-platinum-services-ds-1653256.pdf)

Oracle Customer Success Services

Oracle Customer Success Services can help customers manage and maintain Oracle databases, applications, and cloud environments through services for patching, upgrades, monitoring, lifecycle management, and operational execution. See [Oracle Customer Success Services](https://www.oracle.com/customer-success/)

Customer-Managed Patching with Oracle Tools

For customer-managed patching with Oracle tools, Oracle recommends:

- Single-instance database deployments: Use out-of-place, gold image-based updates with DBCA, AutoUpgrade patching, or Enterprise Manager Fleet Maintenance.
- Advanced Oracle Database deployments: Use FPP or Enterprise Manager Fleet Maintenance with out-of-place, gold image-based updates for Oracle RAC, Oracle Data Guard, Exadata, and large database fleets.
- Database online hot patching: Use OPatch, or OPatch integrated with FPP, only for supported online patch types and scenarios.
- Database upgrades: Use Oracle AutoUpgrade for database upgrade.

In all cases, prefer repeatable, automated, image-based workflows over manual, one-off procedures. This aligns with MAA principles by reducing configuration drift, enabling consistent validation, and preserving a clear fallback path.