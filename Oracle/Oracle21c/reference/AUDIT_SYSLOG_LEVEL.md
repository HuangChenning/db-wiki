---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDIT_SYSLOG_LEVEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.25 AUDIT\_SYSLOG\_LEVEL

`AUDIT_SYSLOG_LEVEL` allows `SYS` and standard `OS` audit records to be written to the system audit log using the `SYSLOG` utility.

Note:

This parameter is effective when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `AUDIT_SYSLOG_LEVEL = '` `facility_clause``.``priority_clause` `'` |
| Syntax | facility\_clause::=  ` { USER \| LOCAL[0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7] \| SYSLOG \| DAEMON \| KERN \| MAIL \| AUTH \| LPR \| NEWS \| UUCP \| CRON }` |
| Syntax | priority\_clause::=  ` { NOTICE \| INFO \| DEBUG \| WARNING \| ERR \| CRIT \| ALERT \| EMERG }` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Examples | ``` AUDIT_SYSLOG_LEVEL = 'KERN.EMERG'; AUDIT_SYSLOG_LEVEL = 'LOCAL1.WARNING'; ``` |

If you use this parameter, it is best to assign a file corresponding to every combination of facility and priority (especially `KERN.EMERG`) in `syslog.conf`. Sometimes these are assigned to print to the console in the default `syslog.conf` file. This can become annoying and will be useless as audit logs. Also, if you use this parameter, it is best to set the maximum length of syslog messages in the system to 512 bytes.

Note:

Audit records written to the system audit log could get truncated to 512 bytes, and different parts of the same audit record may not be joined to get the original complete audit record.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-D352B575-2EA9-451D-9170-FD9298993DEF) for information about configuring syslog auditing

If `AUDIT_SYSLOG_LEVEL` is set and `SYS` auditing is enabled (`AUDIT_SYS_OPERATIONS` = `TRUE`), then `SYS` audit records are written to the system audit log. If `AUDIT_SYSLOG_LEVEL` is set and standard audit records are being sent to the operating system (`AUDIT_TRAIL` = `os`), then standard audit records are written to the system audit log.

In a CDB, the scope of the settings for this initialization parameter is the CDB. Although the audit trail is provided per PDB in a CDB, this initialization parameter cannot be configured for individual PDBs.