---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/ogg-active-active-guidance-dev-and-admin1.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 30 Oracle GoldenGate Active-Active Guidance for Developers and Administrators

Oracle MAA provides guidance for developers and administrators when designing an active-active distributed database architecture using Oracle GoldenGate architecture, where data conflicts may occur between GoldenGate replicas.

For these Oracle GoldenGate or MAA Platinum architectures, active-active replication requires conflict detection and resolution, which includes Automatic Conflict Detection and Resolution (Auto-CDR), or the manual method of conflict detection and resolution using the GoldenGate parameters `COMPARECOLS` and `RESOLVECONFLICT` (referred to as the `COMPARECOLS` / `RESOLVECONFLICTS` method in this topic). Also see [Automatic Conflict Detection and Resolution](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-automatic-cdr.html) and [Manual Conflict Detection and Resolution](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-configure-conflict-detection-and-resolution.html) in Oracle GoldenGate documentation.

For more information about GoldenGate in general, refer to [Oracle GoldenGate documentation](https://docs.oracle.com/en/database/goldengate/core/index.html). These instructions are specific for Oracle-to-Oracle replication. For non-Oracle/heterogeneous active-active refer to `COMPARECOLS` and `RESOLVECONFLICT` parameters in the [Oracle GoldenGate Parameters and Functions Reference Guide](https://docs.oracle.com/en/database/goldengate/core/26/reference/index.html).

### Preparing for Conflict Resolution

Active-active replication requires tighter integration between Oracle Database and Oracle GoldenGate, and there are some additional requirements that must be met from an application and database structure perspective to ensure a smooth experience.

These requirements only pertain to tables that could have a conflict. If there are tables in the application that will be updated on one server only (for example, a lookup table that contains zip codes to city relationships that is updated once a year as part of a batch process) then those tables do not need to meet these requirements.

To understand why these requirements exist, here's a quick refresher on how a conflict is detected and how it’s resolved:

To detect a conflict, Oracle GoldenGate constructs an `UPDATE` or `DELETE` DML statement with a `WHERE` clause that includes the before image of every column that the GoldenGate Replicat can use in a `WHERE` clause. If that DML operation returns a “row not found” exception, that means that there is a conflict, and additional steps are then taken by the Replicat to determine if some other value in that row was changed, or if the row was deleted. This determination is done by querying the target table to see if the row with that primary key exists or not. The resolution portion will provide eventual consistency so that the two rows are the same between two distinct databases. This resolution typically involves ignoring the current DML operation the Replicat is applying, or overwriting the existing data in the target row.

The Oracle GoldenGate documentation covers the different ways to resolve conflicts for both Auto-CDR and `COMPARECOLS` / `RESOLVECONFLICTS` methods as well as examples on how each of them work. See [Automatic Conflict Detection and Resolution](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-automatic-cdr.html) and [Manual Conflict Detection and Resolution](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/administer-configure-conflict-detection-and-resolution.html) for details.

Requirements

- Primary key requirements
	- The table must have a primary key that is made up of one or more columns.
		- The uniqueness of a primary key must be generated so that they are unique across all databases. In two-way active-active, you could have sequences assigned to the primary key that are odd (1,3,5,…) in one database and even (2,4,6,…) in the other. This could guarantee that two databases don’t have the same primary key for different rows and you’ll never have an insert conflict.
- Table structure requirements
	- If you are using manual conflict detection and resolution and defining your own `COMPARECOLS` / `RESOLVECONFLICTS`, which is time-stamp-based resolution, the table must have a time stamp column that uses the same time zone across all databases. Auto-CDR does not require a time stamp column on the existing table.
	- Conflicts within Large Objects (JSON, BLOB, CLOB, for example) and user-defined objects (Abstract data types, collections, arrays) cannot be detected by Oracle GoldenGate, because these columns are not used in the `WHERE` clause by Oracle GoldenGate.
	- If there is a requirement for uniqueness in non-primary key columns this must be enforced using a trigger on the table or through the application.
	- Supplemental logging of all columns is required for tables that you are replicating, and will result in higher redo log generation for those targeted table changes.
- Required GoldenGate settings
	- For Auto-CDR you must include `MAPINVISIBLECOLUMNS` and `LOGALLSUPCOLS` in the Extract. The Replicat must be integrated Replicat or parallel Replicat in integrated mode.
		- For `COMPARECOLS` / `RESOLVECONFLICTS`, you must use `LOGALLSUPCOLS` in the Extract.

### Best Practices for Active-Active Oracle GoldenGate Architecture

To ensure that your active-active configuration runs smoothly these are some best-practice recommendations to consider.

Application Recommendations

- If conflicts can be avoided, do so. This could include splitting users by geographical region, like routing users East of the Mississippi to use the server in Ashburn, VA, and routing users West of the Mississippi to use the server located in Phoenix, AZ. This geographical split can often avoid conflicts where two users would be modifying the same row. Users could also be split by account numbers (even on one server, odd on another), or names (A-M or N-Z).
- Connection stickiness or geographical affinity is also important. If you are using a load balancer to route traffic to the databases, it should include some type of connection persistence, so that if a user’s connection is lost and they reconnect very quickly they are sent to the same server as before. This prevents situations where a user makes changes on server A, disconnects, and then reconnects. If the user is connected to server B before the data is replicated to it, that could cause a poor user experience.
- While Auto-CDR does support the conflict detection and resolution of primary key updates (which it does through the use of the tombstone table), the `COMPARECOLS` / `RESOLVECONFLICTS` method does not. So if you are using the `COMPARECOLS` / `RESOLVECONFLICTS` method, ensure that primary key updates are performed in a manner that would prevent conflicts from occurring.
- In some cases, it may be necessary to communicate back to a user that something they did in the database was reversed or overwritten due to the conflict resolution policies in place. Auto-CDR has a view (`DBA_APPLY_ERROR_MESSAGES`) that can be used to track when a conflict has occurred and what resolution was performed. Monitor this table on all databases.

Database Recommendations

- Edition Based Redefinition can be used to help ensure zero downtime for schema changes, and in Oracle Database 23ai, DDL operations on tables with supplemental logging no longer require an exclusive lock on the table. In Oracle Database 19c, Edition Based Redefinition was not leveraged with active GoldenGate replication because of this exclusive lock requirement.
- DDL should only be performed on one node at a time, and only replicated uni-directionally. GoldenGate doesn’t provide support for conflicts within DDL operations.

Oracle GoldenGate Recommendations

- Procedural replication should be enabled, so that when you use the `DBMS_GOLDENGATE_ADM` calls to enable or disable Auto-CDR on a table, that command is replicated to the target database automatically.
	`TRANLOGOPTIONS INTEGRATEDPARAMS                             (ENABLE_PROCEDURAL_REPLICATION Y)`
- Oracle recommends using Integrated Parallel Replicat. Auto-CDR is not supported with Parallel non-integrated Replicat, Classic Replicat, or Coordinated Replicat.
- DDL replication should be enabled for all tables in replication (syntax `DDL INCLUDE ALL`) in both the Extract and Replicat parameter files.