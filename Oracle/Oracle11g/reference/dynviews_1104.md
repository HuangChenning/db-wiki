---
title: "V$DATAGUARD_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1104.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DATAGUARD_STATS` displays information about Data Guard metrics when queried on a standby database. No rows are returned when queried on a primary database.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(32)` | Name of the metric: - `APPLY FINISH TIME` - An estimate of the time needed to apply all received, but unapplied redo from the primary database. If there are one or more redo gaps on the standby database, an estimate of the time needed to apply all received, but unapplied redo up to the end of the last archived redo log before the beginning of the earliest redo gap. - `APPLY LAG` - Apply lag is a measure of the degree to which the data in a standby database lags behind the data in the primary database, due to delays in propagating and applying redo to the standby database. This value is relevent only to the applying instance. - `TRANSPORT LAG` - Transport lag is a measure of the degree to which the transport of redo to the standby database lags behind the generation of redo on the primary database. If there are one or more redo gaps on the standby database, the transport lag is calculated as if no redo has been received after the beginning of the earliest redo gap. - `ESTIMATED STARTUP TIME` - An estimate of the time needed to start and open the database. |
| `VALUE` | `VARCHAR2(64)` | Value of the metric |
| `UNIT` | `VARCHAR2(30)` | Unit of measurement |
| `TIME_COMPUTED` | `VARCHAR2(30)` | Local time at the standby database when the metric was computed |
| `DATUM_TIME` | `VARCHAR2(30)` | Local time at the standby database when the datum used to compute the metric was received  The `APPLY LAG` and `TRANSPORT LAG` metrics are computed based on data that is periodically received from the primary database. An unchanging value in this column across multiple queries indicates that the standby database is not receiving data from the primary database. |