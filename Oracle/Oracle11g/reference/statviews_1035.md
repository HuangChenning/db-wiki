---
title: ALL_CHANGE_SOURCES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1035.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CHANGE_SOURCES` displays information about Change Data Capture change sources.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the change source |
| `DBID` | `NUMBER` |  | Database identifier |
| `LOG_DIRECTORY` | `VARCHAR2(2000)` |  | Log file directory location |
| `LOGFILE_PATTERN` | `VARCHAR2(30)` |  | Wildcard pattern for log file names |
| `SOURCE_DESCRIPTION` | `VARCHAR2(255)` |  | Description of the change source |
| `CREATED` | `DATE` | `NOT NULL` | Creation date of the change source |
| `SOURCE_TYPE` | `VARCHAR2(18)` |  | Capture mode of the change source: - `AUTOLOG` - `HOTLOG` - `SYNCHRONOUS` - `DISTRIBUTED HOTLOG` - `AUTOLOG ONLINE` |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Global name of the source database |
| `FIRST_SCN` | `NUMBER` |  | SCN of a LogMiner dictionary at which capture can begin |
| `PUBLISHER` | `VARCHAR2(30)` |  | Publisher of the change source |
| `CAPTURE_NAME` | `VARCHAR2(30)` |  | Name of the Streams capture process |
| `CAPTURE_QUEUE_NAME` | `VARCHAR2(30)` |  | Name of the Streams capture queue name |
| `CAPTURE_QUEUE_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the Streams capture table |
| `SOURCE_ENABLED` | `VARCHAR2(1)` |  | Indicates whether the change source is enabled (`Y`) or not (`N`) |