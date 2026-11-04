---
title: Database Limits
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/appg_db_lmts.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## F Database Limits

This appendix describes database limits.

## F.1 Database Limits

Table F-1 lists the default and maximum values for parameters in a `CREATE DATABASE` or `CREATE CONTROLFILE` statement.

Note:

Interdependencies between these parameters may affect permissible values.

Table F-1 CREATE CONTROLFILE and CREATE DATABASE Parameters

| Parameter | Default | Maximum Value |
| --- | --- | --- |
| `MAXLOGFILES` | 16 | 255 |
| `MAXLOGMEMBERS` | 2 | 5 |
| `MAXLOGHISTORY` | 100 | 65534 |
| `MAXDATAFILES` | 30 | 65534 |
| `MAXINSTANCES` | 1 | 1055 |

Table F-2 lists the Oracle Database file size limits in bytes.

Table F-2 File Size Limits

| File Type | Platform | File size limit |
| --- | --- | --- |
| Data files | Any | 4,194,303 multiplied by the value of the `DB_BLOCK_SIZE` parameter |
| Import/Export files and SQL\*Loader files | AIX, HP-UX, Linux, and Solaris: 32-bit with 32-bit files | 2,147,483,647 bytes |
|  | AIX, HP-UX, Linux, and Solaris: 64-bit files | Unlimited  Note: File size is limited by limits allowed by the operating system on different file systems. |
| Control files | HP-UX, Linux, AIX, and Solaris | 25000 control file blocks with a block size of 4096 bytes. |