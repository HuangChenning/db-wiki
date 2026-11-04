---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/UNDO_RETENTION.html
tags:
  - oracle
  - 12c
  - reference
---

`UNDO_RETENTION` specifies (in seconds) the low threshold value of undo retention.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `900` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to 2 <sup>31</sup> - 1 |
| Basic | No |
| Oracle RAC | Oracle recommends that multiple instances have the same value. |

For `AUTOEXTEND` undo tablespaces, the system retains undo for at least the time specified in this parameter, and automatically tunes the undo retention period to satisfy the undo requirements of the queries. For fixed-size undo tablespaces, the system automatically tunes for the maximum possible undo retention period, based on undo tablespace size and usage history, and ignores `UNDO_RETENTION` unless retention guarantee is enabled for the tablespace.

Automatic tuning of undo retention is not supported for LOBs. The `RETENTION` value for LOB columns is set to the value of the `UNDO_RETENTION` parameter.

The `UNDO_RETENTION` parameter is honored only if the current undo tablespace has enough space. If an active transaction requires undo space and the undo tablespace does not have available space, then the system starts reusing unexpired undo space. This action can potentially cause some queries to fail with a "snapshot too old" message.

The amount of time for which undo is retained for the Oracle Database for the current undo tablespace can be obtained by querying the `TUNED_UNDORETENTION` column of the `V$UNDOSTAT` dynamic performance view.

You can modify this parameter in a PDB only if the PDB is in local undo mode; you cannot modify this parameter if the PDB is in shared undo mode.

Recommendations for Modifying UNDO\_RETENTION

Oracle generally recommends that you leave `UNDO_RETENTION` set to its default value. Modifying this parameter is recommended only in the following situations:

- You may want to increase the value of `UNDO_RETENTION` when using flashback features, such as Oracle Flashback Query, which require undo to be retained for longer than the longest running query in the system.
- In Oracle Active Data Guard environments, you may want to increase the value of `UNDO_RETENTION` on the primary instance in order to accommodate undo retention requirements on the standby instances. This allows the primary instance to retain undo for a longer period of time to serve queries on the standby instances. For more information, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-C1272948-3E08-45D9-BD5A-D6461E249EFB) and [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB-GUID-9D1B7A68-EAC0-47CA-97AB-91156894F35E).

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF01403) for information about creating undo tablespaces
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN013) for information about managing undo data