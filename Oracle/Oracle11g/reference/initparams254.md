---
title: STATISTICS_LEVEL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams254.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STATISTICS_LEVEL = { ALL \| TYPICAL \| BASIC }` |
| Default value | `TYPICAL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |

`STATISTICS_LEVEL` specifies the level of collection for database and operating system statistics. The Oracle Database collects these statistics for a variety of purposes, including making self-management decisions.

The default setting of `TYPICAL` ensures collection of all major statistics required for database self-management functionality and provides best overall performance. The default value should be adequate for most environments.

When the `STATISTICS_LEVEL` parameter is set to `ALL`, additional statistics are added to the set of statistics collected with the `TYPICAL` setting. The additional statistics are timed OS statistics and plan execution statistics.

Setting the `STATISTICS_LEVEL` parameter to `BASIC` disables the collection of many of the important statistics required by Oracle Database features and functionality, including:

- Automatic Workload Repository (AWR) Snapshots
- Automatic Database Diagnostic Monitor (ADDM)
- All server-generated alerts
- Automatic SGA Memory Management
- Automatic optimizer statistics collection
- Object level statistics
- End to End Application Tracing (`V$CLIENT_STATS`)
- Database time distribution statistics (`V$SESS_TIME_MODEL` and `V$SYS_TIME_MODEL`)
- Service level statistics
- Buffer cache advisory
- MTTR advisory
- Shared pool sizing advisory
- Segment level statistics
- PGA Target advisory
- Timed statistics
- Monitoring of statistics

Note:

Oracle strongly recommends that you do not disable these important features and functionality.

When the `STATISTICS_LEVEL` parameter is modified by `ALTER SYSTEM`, all advisories or statistics are dynamically turned on or off, depending on the new value of `STATISTICS_LEVEL`. When modified by `ALTER SESSION`, the following advisories or statistics are turned on or off in the local session only. Their system-wide state is not changed:

- Timed statistics
- Timed OS statistics
- Plan execution statistics

The `V$STATISTICS_LEVEL` view displays information about the status of the statistics or advisories controlled by the `STATISTICS_LEVEL` parameter. See ["V$STATISTICS\_LEVEL"](dynviews_3075.md).