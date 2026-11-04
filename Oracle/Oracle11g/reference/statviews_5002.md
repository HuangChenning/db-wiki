---
title: DBA_STREAMS_ADMINISTRATOR
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5002.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_ADMINISTRATOR` displays information about the users who have been granted privileges to be a Streams administrator by procedures in the `DBMS_STREAMS_AUTH` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the user who has been granted privileges to be a Streams administrator |
| `LOCAL_PRIVILEGES` | `VARCHAR2(3)` |  | Indicates whether the user has been granted local Streams administrator privileges (`YES`) or not (`NO`) |
| `ACCESS_FROM_REMOTE` | `VARCHAR2(3)` |  | Indicates whether the user can be used for remote Streams administration through a database link (`YES`) or not (`NO`) |