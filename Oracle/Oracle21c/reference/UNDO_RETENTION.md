---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/UNDO_RETENTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.372 UNDO\_RETENTION

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

For both `AUTOEXTEND` undo tablespaces and fixed-size undo tablespaces, the system retains undo for at least the time specified in this parameter, and automatically tunes the undo retention period to satisfy the undo requirements of the queries.

Automatic tuning of undo retention is not supported for LOBs. The `RETENTION` value for LOB columns is set to the value of the `UNDO_RETENTION` parameter.

The `UNDO_RETENTION` parameter is honored only if the current undo tablespace has enough space. If an active transaction requires undo space and the undo tablespace does not have available space, then the system starts reusing unexpired undo space. This action can potentially cause some queries to fail with a "snapshot too old" message.

The amount of time for which undo is retained for the Oracle Database for the current undo tablespace can be obtained by querying the `TUNED_UNDORETENTION` column of the `V$UNDOSTAT` dynamic performance view.

Recommendations for Modifying UNDO\_RETENTION

Oracle generally recommends that you leave `UNDO_RETENTION` set to its default value. Modifying this parameter is recommended only in the following situations:

- You may want to increase the value of `UNDO_RETENTION` when using flashback features, such as Oracle Flashback Query, which require undo to be retained for longer than the longest running query in the system.
- In Oracle Active Data Guard environments, you may want to increase the value of `UNDO_RETENTION` on the primary instance in order to accommodate undo retention requirements on the standby instances. This allows the primary instance to retain undo for a longer period of time to serve queries on the standby instances. For more information, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-C1272948-3E08-45D9-BD5A-D6461E249EFB) and [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB-GUID-9D1B7A68-EAC0-47CA-97AB-91156894F35E).

Modifying UNDO\_RETENTION in a CDB

You can set the value of `UNDO_RETENTION` in the CDB root (`CDB$ROOT`) and in individual PDBs. The CDB root and PDBs can have the same value or different values. Note that you can modify this parameter in a PDB only if the PDB is in local undo mode; you cannot modify this parameter if the PDB is in shared undo mode.

Starting with Oracle Database release 19c, version 19.9, the value of `UNDO_RETENTION` is not inherited in a CDB. Therefore, if you change the value for `UNDO_RETENTION` in the CDB root, the PDBs do not inherit the new value. If you want to change the value for `UNDO_RETENTION` at the PDB level, you must explicitly do so. For example, if your CDB contains two PDBs (PDB1 and PDB2), you can set `UNDO_RETENTION` to 2000 in the CDB root and both PDBs as follows:

```
ALTER SESSION SET CONTAINER = CDB$ROOT;
ALTER SYSTEM SET UNDO_RETENTION=2000 SCOPE=BOTH;

ALTER SESSION SET CONTAINER = PDB1;
ALTER SYSTEM SET UNDO_RETENTION=2000 SCOPE=BOTH;

ALTER SESSION SET CONTAINER = PDB2;
ALTER SYSTEM SET UNDO_RETENTION=2000 SCOPE=BOTH;
```

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01403) for information about creating undo tablespaces
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN013) for information about managing undo data