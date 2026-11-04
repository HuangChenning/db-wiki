---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: F30732-30
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sutil/oracle-data-pump.html
tags:
  - oracle
  - 21c
  - utilities
---

## Part I Oracle Data Pump

Learn about data movement options using Oracle Data Pump Export, Oracle Data Pump Import, legacy mode, performance, and the Oracle Data Pump API `DBMS_DATAPUMP`.

- [Overview of Oracle Data Pump](oracle-data-pump-overview.md)  
	Oracle Data Pump technology enables very high-speed movement of data and metadata from one database to another.
- [Oracle Data Pump Export](oracle-data-pump-export-utility.md)  
	The Oracle Data Pump Export utility is used to unload data and metadata into a set of operating system files, which are called a dump file set.
- [Oracle Data Pump Import](oracle-datapump-import-utility.md)  
	With Oracle Data Pump Import, you can load an export dump file set into a target database, or load a target database directly from a source database with no intervening files.
- [Oracle Data Pump Legacy Mode](oracle-data-pump-legacy-mode.md)  
	With Oracle Data Pump legacy mode, you can use original Export and Import parameters on the Oracle Data Pump Export and Data Pump Import command lines.
- [Oracle Data Pump Performance](oracle-data-pump-performance-tips.md)  
	Learn how Oracle Data Pump Export and Import is better than that of original Export and Import, and how to enhance performance of export and import operations.
- [Using the Oracle Data Pump API](using-oracle-data-pump-api.md)  
	You can automate data movement operations by using the Oracle Data Pump PL/SQL API `DBMS_DATAPUMP`.