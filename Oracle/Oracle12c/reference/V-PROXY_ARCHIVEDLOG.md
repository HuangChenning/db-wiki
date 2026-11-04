---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-PROXY_ARCHIVEDLOG.html
tags:
  - oracle
  - 12c
  - reference
---

`V$PROXY_ARCHIVEDLOG` contains descriptions of archived log backups that were taken using the proxy copy functionality.

In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Proxy copy record identifier |
| `STAMP` | `NUMBER` | Proxy copy stamp |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of media device that stores the proxy copy |
| `HANDLE` | `VARCHAR2(513)` | Name or "handle" for the proxy copy |