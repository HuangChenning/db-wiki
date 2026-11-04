---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: F30732-30
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sutil/other-oracle-utilities.html
tags:
  - oracle
  - 21c
  - utilities
---

## Part IV Other Utilities

Other Oracle data management utilities include the ADR Command Interpreter, `DBVERIFY`, Oracle LogMiner, the `DBMS_METADATA` API, and the legacy data movement utilities.

- [Cloud Premigration Advisor Tool](premigration-advisor-tool.md)  
	To evaluate the compatibility of the source database before you migrate to an Oracle Cloud database, use the Cloud Premigration Advisor Tool (CPAT).
- [ADRCI: ADR Command Interpreter](oracle-adr-command-interpreter-adrci.md)  
	The Automatic Diagnostic Repository Command Interpreter (ADRCI) utility is a command-line tool that you use to manage Oracle Database diagnostic data.
- [DBVERIFY: Offline Database Verification Utility](oracle-dbverify-utility.md)  
	DBVERIFY is an external command-line utility that performs a physical data structure integrity check.
- [DBNEWID Utility](oracle-dbnewid-utility.md)  
	`DBNEWID` is a database utility that can change the internal database identifier (`DBID`) and the database name (`DBNAME`) for an operational database.
- [Using LogMiner to Analyze Redo Log Files](oracle-logminer-utility.md)  
	LogMiner, which is part of Oracle Database, enables you to query online and archived redo log files through a SQL interface.
- [Using the Metadata APIs](using-oracle-dbms_metadata-api.md)  
	The `DBMS_METADATA` APIs enable you to check and update object metadata.
- [Original Import](oracle-original-import-utility.md)  
	The original Import utility (`imp`) imports dump files that were created using the original Export utility (`exp`).