---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/apply-software-update.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Apply Software Updates

Well-planned, tested, and properly executed software updates are crucial to maximizing uptime and minimizing business disruption. Wherever possible, Oracle recommends out-of-place, gold image-based patching—especially for clustered systems—to ensure safe rollbacks and rapid issue resolution.

Key Practices

- Before updating software run Exachk/Orachk and correct configuration that does not follow recommended best practices.
- Follow client failover best practices to reduce application-level impact during rolling updates that disrupt database instance connectivity. See [Continuous Availability for Applications](continuous-availability-applications.md) for details.
- Test the update and rollback process in a non-production environment with production-like workload and configuration.
- Use Data Guard Standby-First Patch Apply approach to minimize risk and primary database impact when updating mission critical systems. See [Oracle Patch Assurance - Data Guard Standby-First Patch Apply (KB137118)](https://support.oracle.com/support/?documentId=KB137118) for details.
- Take system and database backups immediately before software changes.
- Always validate, backup, and have a proven rollback plan before making software changes.
- Use repeatable, automated, image-based workflows provided by Oracle software maintenance tools to ensure consistency and reduce manual errors.
- Use DBCA/DBCACTL or AutoUpgrade for out-of-place, gold image-based Database updates on standalone/non-clustered systems.
- Use FPP or EM for coordinated, out-of-place, rolling, gold image-based Database and Grid Infrastructure updates on clustered environments such as RAC and Exadata.
- Apply online/in-place updates only for specific patch types or situations where minimal disruption is required. See MOS note [RDBMS Online Patching Aka Hot Patching (KB140524)](https://support.oracle.com/support/?documentId=KB140524) for details.

### Software Update Method Selection: Benefits and Tradeoffs

Table 45-1 Database Software on Non-Clustered Systems (Standalone Hosts)

| Method | Benefits/Tradeoffs |
| --- | --- |
| Out-of-place (gold image) with DBCA/DBCACTL or AutoUpgrade  (Recommended) | - Fast, simple, easy rollback - Requires extra disk space ``` $ dbca -moveDatabase -sourceDB <dbname> -silent ``` |
| Online hot patch with OPatch | - No database downtime or database connection disruption - Patching is done in-place in the existing database home - Limited to supported patches (MRP/interim) |

Table 45-2 Database Software on Clustered Systems (Oracle RAC/Exadata)

| Method | Benefits/Tradeoffs |
| --- | --- |
| Out-of-place (gold image), RAC rolling with FPP or EM  (Recommended) | - Fast, simple, full cluster orchestration, easy rollback - Requires extra disk space ``` $ rhpctl move database –sourcewc <src> –patchedwc <dest> ``` |
| Online hot patch with FPP | - No database downtime or database connection disruption - Patching is done in-place in the existing database home - Limited to supported patches (MRP/interim) |
| Non-rolling with FPP | - All updates applied at once, reduced planned maintenance time - Full database downtime |

Table 45-3 Grid Infrastructure Software on Clustered Systems (Oracle RAC/Exadata)

| Method | Benefits/Tradeoffs |
| --- | --- |
| Out-of-place (gold image), Oracle RAC rolling with FPP  (Recommended) | - Fast, simple, full cluster orchestration, easy rollback - Requires extra disk space ``` $ rhpctl move gihome –sourcewc <src> –destwc <dest> ``` |
| Zero-downtime out-of-place (gold image), Oracle RAC rolling with FPP | - No database connection disruption - Requires extra disk space ``` $ rhpctl move gihome –sourcewc <src> –destwc <dest> -tgip ``` |

Table 45-4 Exadata System Software

| Method | Benefits/Tradeoffs |
| --- | --- |
| Rolling update with patchmgr or FPP  (Recommended)  - Storage servers - Database servers - Network fabric switches | - No database downtime, simple, full system orchestration ``` $ patchmgr --dbnodes <group_file> --repo <repo>  --upgrade --target_version <version> --rolling ``` |
| Live update with patchmgr or FPP  - Database servers | - No database connection disruption, supports partial updates to address security issues - Outstanding work update items cannot be completed online and require a system reboot ``` $ patchmgr --dbnodes <group_file> --repo <repo>  --upgrade --target_version <version> --rolling --live-update-target full ``` |
| Non-rolling with patchmgr or FPP  - Storage servers - Database servers - Network fabric switches | - All updates applied at once, reduced planned maintenance time - Full system downtime |