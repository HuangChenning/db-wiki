---
title: Creating the Data Dictionary
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/scripts001.htm
tags:
  - oracle
  - 11g
  - reference
---

When you use the Database Configuration Assistant to create a database, Oracle automatically creates the data dictionary. Thereafter, whenever the database is in operation, Oracle updates the data dictionary in response to every DDL statement.

The data dictionary base tables are the first objects created in any Oracle database. They are created in the `SYSTEM` tablespace and must remain there. The data dictionary base tables store information about all user-defined objects in the database.

Table B-1 lists required scripts, which are run automatically when you create a database using the Database Configuration Assistant. They are described here because you might need to run them if you create a database manually. To run these scripts, you must be connected to Oracle as a user with `SYSDBA` privileges.

Table B-1 Creating the Data Dictionary Scripts

| Script Name | Needed For | Description |
| --- | --- | --- |
| `catalog.sql` | All databases | Creates the data dictionary and public synonyms for many of its views  Grants `PUBLIC` access to the synonyms |
| `catproc.sql` | All databases | Runs all scripts required for, or used with, PL/SQL |
| `catclust.sql` | Real Application Clusters | Creates Real Application Clusters data dictionary views |

See Also:

- Your operating system-specific Oracle documentation for the exact names and locations of these scripts on your operating system
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about creating a database
- Your release notes and [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) to learn when it is necessary to run these scripts