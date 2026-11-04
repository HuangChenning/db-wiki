---
title: DBA_HIGH_WATER_MARK_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3200.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIGH_WATER_MARK_STATISTICS` displays information about database high-watermark statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Identifier of the database for which the high-watermark statistics are tracked |
| `NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the high-watermark statistic (see Table 4-1) |
| `VERSION` | `VARCHAR2(17)` | `NOT NULL` | Database version in which the high watermarks were tracked |
| `HIGHWATER` | `NUMBER` |  | Highest value of the statistic seen at sampling time |
| `LAST_VALUE` | `NUMBER` |  | Value of the statistic at the last sample time |
| `DESCRIPTION` | `VARCHAR2(128)` |  | Description of the high-watermark statistics (see Table 4-1) |

Table 4-1 DBA\_HIGH\_WATER\_MARK\_STATISTICS Statistics

| Name | Description |
| --- | --- |
| ACTIVE\_SESSIONS | Maximum Number of Active Sessions seen in the system |
| CPU\_COUNT | Maximum Number of CPUs |
| DATAFILES | Maximum Number of Datafiles |
| DB\_SIZE | Maximum Size of the Database (Bytes) |
| EXADATA\_DISKS | Number of physical disks |
| INSTANCES | Oracle Database instances |
| PART\_INDEXES | Maximum Number of Partitions belonging to an User Index |
| PART\_TABLES | Maximum Number of Partitions belonging to an User Table |
| QUERY\_LENGTH | Maximum Query Length |
| SEGMENT\_SIZE | Size of Largest Segment (Bytes) |
| SESSIONS | Maximum Number of Concurrent Sessions seen in the database |
| SQL\_NCHAR\_COLUMNS | Maximum Number of SQL NCHAR Columns |
| TABLESPACES | Maximum Number of Tablespaces |
| USER\_INDEXES | Number of User Indexes |
| USER\_MV | Maximum Number of Materialized Views (User) |
| USER\_TABLES | Number of User Tables |