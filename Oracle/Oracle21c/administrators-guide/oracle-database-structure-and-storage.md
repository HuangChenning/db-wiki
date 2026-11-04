---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: F31835-17
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/admin/oracle-database-structure-and-storage.html
tags:
  - oracle
  - 21c
  - administrators-guide
---

## Part II Oracle Database Structure and Storage

You can create and manage database structures and storage components.

- [Managing Control Files](managing-control-files.md)  
	You can create, back up, and drop control files.
- [Managing the Redo Log](managing-the-redo-log.md)  
	You manage the redo log by completing tasks such as creating redo log groups and members, relocating and renaming redo log members, dropping redo log groups and members, and forcing log switches.
- [Managing Archived Redo Log Files](managing-archived-redo-log-files.md)  
	You manage the archived redo log files by completing tasks such as choosing between `NOARCHIVELOG` or `ARCHIVELOG` mode and specifying archive destinations.
- [Managing Tablespaces](managing-tablespaces.md)  
	A tablespace is a database storage unit that groups related logical structures together. The database data files are stored in tablespaces.
- [Managing Data Files and Temp Files](managing-data-files-and-temp-files.md)  
	You can manage data files and temp files by performing tasks such as creating them, altering them, and dropping them.
- [Transporting Data](transporting-data.md)  
	Transporting data moves the data from one database to another.
- [Managing Undo](managing-undo.md)  
	For a default installation, Oracle Database automatically manages undo. There is typically no need for DBA intervention. However, if your installation uses Oracle Flashback operations, you may need to perform some undo management tasks to ensure the success of these operations.
- [Using Oracle Managed Files](using-oracle-managed-files.md)  
	Oracle Database can manage the files that comprise the database.
- [Using Persistent Memory Database](using-PMEM-db-support.md)  
	Mapping the database directly into persistent memory (PMEM) provides significant performance enhancements.