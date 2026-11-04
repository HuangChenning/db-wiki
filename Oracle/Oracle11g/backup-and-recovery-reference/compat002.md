---
title: Determining the Recovery Catalog Schema Version
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat002.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

To determine the current release of the catalog schema, you must run a SQL query.

1. Use SQL\*Plus to connect to the recovery catalog database as the catalog owner. For example, enter:
	```
	% sqlplus rman@catdb
	```
2. Query the `rcver` catalog table. For example, run this query:
	```
	SQL> SELECT * FROM rcver; 
	     VERSION 
	     ------------ 
	     09.00.01.00
	     10.02.01.00
	     11.01.00.03
	```
	If multiple versions are listed, then the last row is the current version, and the rows before it are prior versions. In the preceding example, the current recovery catalog schema version is 11.1 and the previous version was 10.2.
	For releases 10.2 and later, the last two digits in the `rcver` output indicate patch level. For earlier releases, they are always zeros.