---
title: DBA_XSTREAM_ADMINISTRATOR
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5106.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_XSTREAM_ADMINISTRATOR` displays information about the users who have been granted privileges to be XStream administrators by procedures in the `DBMS_XSTREAM_AUTH` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the user who has been granted privileges to be an XStream administrator |
| `LOCAL_PRIVILEGES` | `VARCHAR2(3)` |  | Indicates whether the user has been granted local XStream administrator privileges (`YES`) or not (`NO`) |
| `ACCESS_FROM_REMOTE` | `VARCHAR2(3)` |  | Indicates whether the user can be used for remote XStream administration through a database link (`YES`) or not (`NO`) |

Note:

The `DBA_XSTREAM_ADMINISTRATOR` view is available starting with Oracle Database 11g Release 2 (11.2.0.2).