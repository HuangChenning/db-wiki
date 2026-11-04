---
title: DBA_REGISTERED_MVIEW_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4208.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_REGISTERED_MVIEW_GROUPS` lists all the registered materialized view groups at the master site or master materialized view site.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` |  | Name of the materialized view replication group |
| `MVIEW_SITE` | `VARCHAR2(128)` |  | Site of the materialized view replication group |
| `GROUP_COMMENT` | `VARCHAR2(80)` |  | Description of the materialized view replication group |
| `VERSION` | `VARCHAR2(8)` |  | Oracle release of the materialized view replication group:  Note: Oracle8i and newer materialized view groups show `ORACLE 8`. |
| `FNAME` | `VARCHAR2(30)` |  | Name of the flavor of the materialized view group |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the materialized view replication group |