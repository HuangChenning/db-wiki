---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STATISTICS_LEVEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.355 STATISTICS\_LEVEL

`STATISTICS_LEVEL` specifies the level of collection for database and operating system statistics. The Oracle Database collects these statistics for a variety of purposes, including making self-management decisions.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STATISTICS_LEVEL = { ALL \| TYPICAL \| BASIC }` |
| Default value | `TYPICAL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

The default setting of `TYPICAL` ensures collection of all major statistics required for database self-management functionality and provides best overall performance. The default value should be adequate for most environments.

When the `STATISTICS_LEVEL` parameter is set to `ALL`, additional statistics are added to the set of statistics collected with the `TYPICAL` setting. The additional statistics are timed operating system statistics and plan execution statistics.

Setting the `STATISTICS_LEVEL` parameter to `BASIC` disables the collection of many of the important statistics required by Oracle Database features and functionality, including:

- All server-generated alerts
- Automatic Database Diagnostic Monitor (ADDM)
- Automatic optimizer statistics collection
- Automatic SGA Memory Management
- Automatic Workload Repository (AWR) Snapshots
- Buffer cache advisory
- Database time distribution statistics (`V$SESS_TIME_MODEL` and `V$SYS_TIME_MODEL`)
- End to End Application Tracing (`V$CLIENT_STATS`)
- Monitoring of statistics
- MTTR advisory
- Object Activity Tracking System (OATS)
- Object level statistics
- PGA Target advisory
- Segment level statistics
- Service level statistics
- Shared pool sizing advisory
- Timed statistics

Note:

Oracle strongly recommends that you do not disable these important features and functionality.

When the `STATISTICS_LEVEL` parameter is modified by `ALTER SYSTEM`, all advisories or statistics are dynamically turned on or off, depending on the new value of `STATISTICS_LEVEL`. When modified by `ALTER SESSION`, the following advisories or statistics are turned on or off in the local session only. Their systemwide state is not changed:

- Timed statistics
- Timed operating system statistics
- Plan execution statistics

The `V$STATISTICS_LEVEL` view displays information about the status of the statistics or advisories controlled by the `STATISTICS_LEVEL` parameter. See " [V$STATISTICS\_LEVEL](V-STATISTICS_LEVEL.md) ".

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA153) for more information about this parameter