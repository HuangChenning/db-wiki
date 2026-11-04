---
title: AUDIT_SYS_OPERATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams015.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |
| Basic | No |

`AUDIT_SYS_OPERATIONS` enables or disables the auditing of top-level operations, which are SQL statements directly issued by users when connecting with `SYSDBA` or `SYSOPER` privileges. (SQL statements run from within PL/SQL procedures or functions are not considered top-level.) The audit records are written to the operating system's audit trail. The audit records will be written in XML format if the `AUDIT_TRAIL` initialization parameter is set to `xml` or `xml, extended`.

On UNIX platforms, if the `AUDIT_SYSLOG_LEVEL` parameter has also been set, then it overrides the `AUDIT_TRAIL` parameter and SYS audit records are written to the system audit log using the `SYSLOG` utility.