---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATAGUARD_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.162 V$DATAGUARD\_STATS

`V$DATAGUARD_STATS` displays information about Oracle Data Guard metrics when queried on a target database. No rows are returned when queried on a primary database. In the descriptions in this section, the originating database that is generating the redo is either a primary database or a logical standby database.

| Column | Datatype | Description |
| --- | --- | --- |
| `SOURCE_DBID` | `NUMBER` | Database ID of the originating database |
| `SOURCE_DB_UNIQUE_NAME` | `VARCHAR2(32)` | DB unique name of the originating database |
| `NAME` | `VARCHAR2(32)` | Name of the metric:  - `apply` `finish` `time` - An estimate of the time needed to apply all received, but unapplied redo from the originating database. If there are one or more redo gaps on the target database, an estimate of the time needed to apply all received, but unapplied redo up to the end of the last archived redo log before the beginning of the earliest redo gap. - `apply` `lag` - Apply lag is a measure of the degree to which the data in a target database lags behind the data in the originating database, due to delays in propagating and applying redo to the target database. This value is relevant only to the applying instance. - `estimated` `startup` `time` - An estimate of the time needed to start and open the database. - `transport` `lag` - Transport lag is a measure of the degree to which the transport of redo to the target database lags behind the generation of redo on the originating database. If there are one or more redo gaps on the target database, the transport lag is calculated as if no redo has been received after the beginning of the earliest redo gap. |
| `VALUE` | `VARCHAR2(64)` | Value of the metric |
| `UNIT` | `VARCHAR2(30)` | Unit of measurement |
| `TIME_COMPUTED` | `VARCHAR2(30)` | Local time at the target database when the metric was computed |
| `DATUM_TIME` | `VARCHAR2(30)` | Local time at the target database when the data used to compute the metric was received  The `apply` `lag` and `transport` `lag` metrics are computed based on data that is periodically received from the source database. An unchanging value in this column across multiple queries indicates that the target database is not receiving data from the source database. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |