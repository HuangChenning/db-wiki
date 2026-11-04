---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: F30732-30
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sutil/oracle-external-tables.html
tags:
  - oracle
  - 21c
  - utilities
---

## Part III External Tables

To use external tables successfully, find out about external table concepts, and see examples of what options are available to you to use external tables with Oracle Database.

- [External Tables Concepts](oracle-external-tables-concepts.md)  
	The external tables feature is a complement to existing SQL\*Loader functionality. It enables you to access data in external sources as if it were in a table in the database.
- [The ORACLE\_LOADER Access Driver](oracle_loader-access-driver.md)  
	Learn how to control the way external tables are accessed by using the ORACLE\_LOADER access driver parameters to modify the default behavior of the access driver.
- [The ORACLE\_DATAPUMP Access Driver](oracle_datapump-access-driver.md)  
	The `ORACLE_DATAPUMP` access driver provides a set of access parameters that are unique to external tables of the type `ORACLE_DATAPUMP`.
- [ORACLE\_BIGDATA Access Driver](oracle-bigdata-access-driver.md)  
	With the `ORACLE_BIGDATA` access driver, you can access data stored in object stores as if that data was stored in tables in an Oracle Database.
- [External Tables Examples](using-oracle-external-tables-examples.md)  
	Learn from these examples how to use the `ORACLE_LOADER`, `ORACLE_DATAPUMP``,ORACLE_HDFS`, and `ORACLE_HIVE` access drivers to query data in Oracle Database and Big Data.