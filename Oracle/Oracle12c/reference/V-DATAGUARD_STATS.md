---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-DATAGUARD_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$DATAGUARD_STATS` displays information about Oracle Data Guard metrics when queried on a standby database. No rows are returned when queried on a primary database.

| Column | Datatype | Description |
| --- | --- | --- |
| `SOURCE_DBID` | `NUMBER` | Database ID of the protected source database |
| `SOURCE_DB_UNIQUE_NAME` | `VARCHAR2(32)` | DB unique name of the protected source database |
| `NAME` | `VARCHAR2(32)` | Name of the metric:  - `APPLY FINISH TIME` - An estimate of the time needed to apply all received, but unapplied redo from the primary database. If there are one or more redo gaps on the standby database, an estimate of the time needed to apply all received, but unapplied redo up to the end of the last archived redo log before the beginning of the earliest redo gap. - `APPLY LAG` - Apply lag is a measure of the degree to which the data in a standby database lags behind the data in the primary database, due to delays in propagating and applying redo to the standby database. This value is relevent only to the applying instance. - `TRANSPORT LAG` - Transport lag is a measure of the degree to which the transport of redo to the standby database lags behind the generation of redo on the primary database. If there are one or more redo gaps on the standby database, the transport lag is calculated as if no redo has been received after the beginning of the earliest redo gap. - `ESTIMATED STARTUP TIME` - An estimate of the time needed to start and open the database. |
| `VALUE` | `VARCHAR2(64)` | Value of the metric |
| `UNIT` | `VARCHAR2(30)` | Unit of measurement |
| `TIME_COMPUTED` | `VARCHAR2(30)` | Local time at the standby database when the metric was computed |
| `DATUM_TIME` | `VARCHAR2(30)` | Local time at the standby database when the datum used to compute the metric was received  The `APPLY LAG` and `TRANSPORT LAG` metrics are computed based on data that is periodically received from the primary database. An unchanging value in this column across multiple queries indicates that the standby database is not receiving data from the primary database. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |