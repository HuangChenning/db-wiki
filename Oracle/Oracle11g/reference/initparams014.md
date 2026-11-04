---
title: AUDIT_FILE_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams014.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `AUDIT_FILE_DEST = '` `directory` `'` |
| Default value | The first default value is:  `ORACLE_BASE` / `admin/` `ORACLE_SID/adump`  The second default value, which is used if the first default value does not exist or is unusable, is:  `ORACLE_HOME` `/rdbms/audit`  Both of these default values are for Unix systems. Other platforms may have different defaults. |
| Modifiable | `ALTER SYSTEM ... DEFERRED` |
| Basic | No |

`AUDIT_FILE_DEST` specifies the operating system directory into which the audit trail is written when the `AUDIT_TRAIL` initialization parameter is set to os, xml, or xml,extended. The audit records will be written in XML format if the `AUDIT_TRAIL` initialization parameter is set to xml or xml, extended. It is also the location to which mandatory auditing information is written and, if so specified by the `AUDIT_SYS_OPERATIONS` initialization parameter, audit records for user `SYS`.