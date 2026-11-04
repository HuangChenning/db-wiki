---
title: "V$RECOVERY_FILE_STATUS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2126.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RECOVERY_FILE_STATUS` contains one row for each datafile for each `RECOVER` statement. This view contains useful information only for the Oracle process doing the recovery. When Recovery Manager directs a server process to perform recovery, only Recovery Manager is able to view the relevant information in this view. `V$RECOVERY_FILE_STATUS` will be empty to all other Oracle users.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILENUM` | `NUMBER` | Number of the file being recovered |
| `FILENAME` | `VARCHAR2(513)` | Filename of the datafile being recovered |
| `STATUS` | `VARCHAR2(13)` | Status of the recovery: |