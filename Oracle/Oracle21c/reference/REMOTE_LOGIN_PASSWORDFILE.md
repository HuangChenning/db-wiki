---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/REMOTE_LOGIN_PASSWORDFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.305 REMOTE\_LOGIN\_PASSWORDFILE

`REMOTE_LOGIN_PASSWORDFILE` specifies whether Oracle checks for a password file.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REMOTE_LOGIN_PASSWORDFILE = { SHARED \| EXCLUSIVE \| NONE }` |
| Default value | `EXCLUSIVE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

Values

- `SHARED`
	One or more databases can use the password file. The password file can contain `SYS` and non- `SYS` users.
	When `REMOTE_LOGIN_PASSWORDFILE` is set to `SHARED`:
	- The database disables modification of the password file by an ASM or RDBMS instance.
		- If you attempt to change the password of a user that is in the password file, the operation fails with "ORA-01999: password file cannot be updated in SHARED mode.
		- If you attempt to change the password of an administrative user (except SYS) that is not in the password file, the password change operation will succeed, but the new password will not go into effect. This is because the password is updated only in the data dictionary and not in the password file.
		- Grants and revokes of administrative privileges (`SYSDBA`, `SYSOPER`, `SYSASM`, `SYSBACKUP`, `SYSDG`, `SYSKM`) to or from individual users are not allowed. For example, `GRANT` `SYSDBA` `TO` `SCOTT` fails with "ORA-01999: password file cannot be updated in SHARED mode."
		- If the password file does not exist, then the behavior is the same as setting `REMOTE_LOGIN_PASSWORDFILE` to `NONE`.
- `EXCLUSIVE`
	The password file is intended for use by ASM instances in the same cluster or by one or more instances of the same Oracle database.
	The password file can contain `SYS` and non- `SYS` users.
	If the password file does not exist, then the behavior is the same as setting `REMOTE_LOGIN_PASSWORDFILE` to `NONE`.
- `NONE`
	ASM and RDBMS instances ignore the password file. Therefore, privileged users must be authenticated by the operating system.

Note:

If you change `REMOTE_LOGIN_PASSWORDFILE` to `EXCLUSIVE` or `SHARED` from `NONE`, then ensure that the password file is synchronized with the dictionary passwords.