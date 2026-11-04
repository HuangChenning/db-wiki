---
title: "V$IO_CALIBRATION_STATUS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2005.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$IO_CALIBRATION_STATUS` displays the status of I/O calibration in the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATUS` | `VARCHAR2(13)` | Calibration status: - `IN PROGRESS` - Calibration in Progress (Results from a previous calibration run are displayed, if available) - `READY` Results are ready and available from an earlier run - `NOT AVAILABLE` Calibration results are not available |
| `CALIBRATION_TIME` | `TIMESTAMP(3)` | End time of the last calibration run |