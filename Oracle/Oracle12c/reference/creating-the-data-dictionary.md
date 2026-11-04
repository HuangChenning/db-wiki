---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/creating-the-data-dictionary.html
tags:
  - oracle
  - 12c
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
| `catclust.sql` | Oracle Real Application Clusters | Creates Oracle Real Application Clusters data dictionary views |

See Also:

- Your operating system-specific Oracle documentation for the exact names and locations of these scripts on your operating system
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN002) for more information about creating a database
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=RACAD7401) for more information about creating Oracle Real Application Cluster views