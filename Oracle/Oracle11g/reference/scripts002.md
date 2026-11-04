---
title: Creating Additional Data Dictionary Structures
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/scripts002.htm
tags:
  - oracle
  - 11g
  - reference
---

Oracle supplies other scripts that create additional structures you can use in managing your database and creating database applications. These scripts are listed in Table B-2.

See Also:

Your operating system-specific Oracle documentation for the exact names and locations of these scripts on your operating system

Table B-2 Creating Additional Data Dictionary Structures

| Script Name | Needed For | Run By | Description |
| --- | --- | --- | --- |
| `catblock.sql` | Performance management | `SYS` | Creates views that can dynamically display lock dependency graphs |
| `catexp7.sql` | Exporting data to Oracle7 | `SYS` | Creates the dictionary views needed for the Oracle7 Export utility to export data from the Oracle Database in Oracle7 Export file format |
| `caths.sql` | Heterogeneous Services | `SYS` | Installs packages for administering heterogeneous services |
| `catio.sql` | Performance management | `SYS` | Allows I/O to be traced on a table-by-table basis |
| `catoctk.sql` | Security | `SYS` | Creates the Oracle Cryptographic Toolkit package |
| `catqueue.sql` | Advanced Queuing |  | Creates the dictionary objects required for Advanced Queuing |
| `catrep.sql` | Oracle Replication | `SYS` | Runs all SQL scripts for enabling database replication |
| `dbmsiotc.sql` | Storage management | Any user | Analyzes chained rows in index-organized tables |
| `dbmspool.sql` | Performance management | `SYS` or `SYSDBA` | Enables DBA to lock PL/SQL packages, SQL statements, and triggers into the shared pool |
| `userlock.sql` | Concurrency control | `SYS` or `SYSDBA` | Provides a facility for user-named locks that can be used in a local or clustered environment to aid in sequencing application actions |
| `utlbstat.sql` and `utlestat.sql` | Performance monitoring | `SYS` | Respectively start and stop collecting performance tuning statistics |
| `utlchn1.sql` | Storage management | Any user | For use with the Oracle Database. Creates tables for storing the output of the `ANALYZE` command with the `CHAINED ROWS` option. Can handle both physical and logical rowids. |
| `utlconst.sql` | Year 2000 compliance | Any user | Provides functions to validate that `CHECK` constraints on date columns are year 2000 compliant |
| `utldtree.sql` | Metadata management | Any user | Creates tables and views that show dependencies between objects |
| `utlexpt1.sql` | Constraints | Any user | For use with the Oracle Database. Creates the default table (`EXCEPTIONS`) for storing exceptions from enabling constraints. Can handle both physical and logical rowids. |
| `utlip.sql` | PL/SQL | `SYS` | Used primarily for upgrade and downgrade operations. It invalidates all existing PL/SQL modules by altering certain dictionary tables so that subsequent recompilations will occur in the format required by the database. It also reloads the packages `STANDARD` and `DBMS_STANDARD`, which are necessary for any PL/SQL compilations. |
| `utlirp.sql` | PL/SQL | `SYS` | Used to change from 32-bit to 64-bit word size or vice versa. This script recompiles existing PL/SQL modules in the format required by the new database. It first alters some data dictionary tables. Then it reloads the packages `STANDARD` and `DBMS_STANDARD`, which are necessary for using PL/SQL. Finally, it triggers a recompilation of all PL/SQL modules, such as packages, procedures, and types. |
| `utllockt.sql` | Performance monitoring | `SYS` or `SYSDBA` | Displays a lock wait-for graph, in tree structure format |
| `utlpwdmg.sql` | Security | `SYS` or `SYSDBA` | Creates PL/SQL functions for default password complexity verification. Sets the default password profile parameters and enables password management features. |
| `utlrp.sql` | PL/SQL | `SYS` | Recompiles all existing PL/SQL modules that were previously in an `INVALID` state, such as packages, procedures, and types. |
| `utlsampl.sql` | Examples | `SYS` or any user with DBA role | Creates sample tables, such as `emp` and `dept`, and users, such as `scott` |
| `utlscln.sql` | Oracle Replication | Any user | Copies a snapshot schema from another snapshot site |
| `utltkprf.sql` | Performance management | `SYS` | Creates the TKPROFER role to allow the TKPROF profiling utility to be run by non-DBA users |
| `utlvalid.sql` | Partitioned tables | Any user | Creates tables required for storing output of `ANALYZE TABLE ...VALIDATE STRUCTURE` of a partitioned table |
| `utlxplan.sql` | Performance management | Any user | Creates the table `PLAN_TABLE`, which holds output from the `EXPLAIN PLAN` statement |