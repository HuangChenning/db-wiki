---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/admin-oracle-asm-audit-trail.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This document explains how to manage the audit trail records in Oracle ASM instances.

### Oracle ASM audit records with Syslog

- Oracle ASM audit trail records are redirected to the Syslog facility.
- With this facility, the Oracle ASM audit trail records are written to /var/log/oraasmaudit.log file.
- Log rotation is configured for Oracle ASM audit trail records in /etc/logrotate.d/oraasmaudit configuration file. Audit logs are rotated once every four weeks and will be compressed after they are rotated.

### Managing Oracle ASM audit records in Operating system audit trail

#### Operating system audit trail

Enabling Operating system audit trail

To disable syslog auditing and enable Operating system audit trail, set `AUDIT_SYSLOG_LEVEL` initialization parameter to `NULL` and `AUDIT_TRAIL` initialization parameter to ‘OS’.

See Also:

- [AUDIT\_FILE\_DEST initialization parameter](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=refrn-GUID-82C7E258-EEF7-48D2-B06B-7F949686E54B)
- [AUDIT\_TRAIL initialization parameter](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=refrn-GUID-BD86F593-B606-4367-9FB6-8DAB2E47E7FA)

Purging Operating system audit trail files

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=dbseg-GUID-9F298B8A-6196-4206-A889-A7CEB0924CF1) for more information on purging audit trail files.
- [ASMCMD Audit Files Management Commands](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-95231568-96AE-47F4-9E61-A46D47E7E634) provides detailed information about ASMCMD commands to manage Oracle ASM audit trail files.
	See Also:
	- [audcreatejob ASMCMD command](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-B8ADA15C-2A32-4A56-8AB3-5297339F9061)
	- [audsettimestamp ASMCMD command](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-EF7A7759-98CC-47B3-87F4-E54F0D482FA5)
	- [audcleanaudittrail ASMCMD command](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-B0BF59C0-D8E6-417C-99FD-294BC2E309FE)

### Managing Oracle ASM audit records in Unified audit trail

Unified audit trail

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=dbseg-GUID-16E8E421-CFCE-4584-B09B-88F01D51B152) for more information about unified auditing.
- Unified audit trail records are available through
	- `GV$UNIFIED_AUDIT_TRAIL` view for Oracle ASM RAC instances.

Enabling Unified audit trail

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=dbseg-GUID-AE3A5133-D90F-4447-822C-CF186247EDDC) for more details on enabling unified audit trail.

Purging Unified audit trail files

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=dbseg-GUID-9B891A44-3DF4-4B52-98D4-A931DBFAEC1D) for more information on purging audit trail files.
- [ASMCMD Audit Files Management Commands](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-95231568-96AE-47F4-9E61-A46D47E7E634) provides detailed information about ASMCMD commands to manage Oracle ASM audit trail files.

### Audit Trail Properties in Operating System and Unified Audit Trail

Table 3-3 Audit Trail Size and Age Properties

| Property Name | Description |
| --- | --- |
| Audit file max size | - Audit file max size can have a minimum value of 1 KB and maximum value of 2000000 KB. The default value is 10000 KB. - Oracle ASM instance will stop writing audit records to the audit files upon reaching the file max size limit. The files are renamed and a new file will be created for subsequent audit records. - See [ASMCMD Audit Files Management Commands](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-06F84E5F-7A56-43BA-83FC-90F639FA3BBA) to set the audit file max property. |
| Audit file max age | - Audit file max age can have a minimum value of 1 day and maximum value of 497 days. The default value is 5 days. - Oracle ASM instance will stop writing audit records to the audit files upon reaching the file max age limit. The files are renamed and a new file will be created for subsequent audit records. - See [ASMCMD Audit Files Management Commands](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-06F84E5F-7A56-43BA-83FC-90F639FA3BBA) to set the audit file max age. |
| Audit purge job interval | - Audit purge job interval can have a minimum value of 1 hour and maximum value of 999 hours. - See [ASMCMD Audit Files Management Commands](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-A053693F-A4C0-4A0F-BC2C-8B3B2A2F3F20) to set the audit purge job interval. |

See Also:

- [audclearproperty ASMCMD command](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ostmg-GUID-B9B0FFB9-C3DF-43A6-ACDD-4DC39A812F8B)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=arpls-GUID-835445FD-845E-48C2-B2C0-F8CC2249E9F2) for more details about audit trail properties.