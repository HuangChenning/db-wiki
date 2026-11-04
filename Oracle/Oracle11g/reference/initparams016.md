---
title: AUDIT_SYSLOG_LEVEL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams016.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `AUDIT_SYSLOG_LEVEL = '` `facility_clause``.``priority_clause` `'` |
|  | facility\_clause::=  `{ USER \| LOCAL[0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7] \| SYSLOG \| DAEMON \| KERN \| MAIL \| AUTH \| LPR \| NEWS \| UUCP \| CRON }` |
|  | priority\_clause::=  `{ NOTICE \| INFO \| DEBUG \| WARNING \| ERR \| CRIT \| ALERT \| EMERG }` |
| Default value | There is no default value. |
| Modifiable | No |
| Basic | No |
| Examples | ``` AUDIT_SYSLOG_LEVEL = 'KERN.EMERG'; AUDIT_SYSLOG_LEVEL = 'LOCAL1.WARNING'; ``` |

`AUDIT_SYSLOG_LEVEL` allows `SYS` and standard `OS` audit records to be written to the system audit log using the `SYSLOG` utility.

If you use this parameter, it is best to assign a file corresponding to every combination of facility and priority (especially `KERN.EMERG`) in `syslog.conf`. Sometimes these are assigned to print to the console in the default `syslog.conf` file. This can become annoying and will be useless as audit logs. Also, if you use this parameter, it is best to set the maximum length of syslog messages in the system to 512 bytes.

If `AUDIT_SYSLOG_LEVEL` is set and `SYS` auditing is enabled (`AUDIT_SYS_OPERATIONS` = `TRUE`), then `SYS` audit records are written to the system audit log.If `AUDIT_SYSLOG_LEVEL` is set and standard audit records are being sent to the operating system (`AUDIT_TRAIL` = `os`), then standard audit records are written to the system audit log.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG66112) for more information about configuring the syslog audit trail by using the `AUDIT_SYSLOG_LEVEL` parameter