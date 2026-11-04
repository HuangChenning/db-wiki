---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/REMOTE_LOGIN_PASSWORDFILE.html
tags:
  - oracle
  - 12c
  - reference
---

`REMOTE_LOGIN_PASSWORDFILE` specifies whether Oracle checks for a password file.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REMOTE_LOGIN_PASSWORDFILE = { shared \| exclusive \| none }` |
| Default value | `exclusive` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

Values

- `shared`
	One or more databases can use the password file. The password file can contain `SYS` and non- `SYS` users.
	When `REMOTE_LOGIN_PASSWORDFILE` is set to `shared`:
	- The `SYS` password cannot be changed. If you try, the password change operation fails with "ORA-28046: Password change for SYS disallowed."
		- The password of any user who has `SYS*` admin privileges (`SYSDBA`, `SYSOPER`, `SYSASM`, `SYSBACKUP`, `SYSDG`, `SYSKM`) cannot be changed. If you try, the password change operation fails with "ORA-01999: password file cannot be updated in SHARED mode."
		- Grants of `SYS*` admin privileges (`SYSDBA`, `SYSOPER`, `SYSASM`, `SYSBACKUP`, `SYSDG`, `SYSKM`) to individual users are not allowed. For example, `grant sysdba to scott` fails with "ORA-01999: password file cannot be updated in SHARED mode." Similarly, revoke of `SYS*` admin privileges fails.
		- If the password file does not exist, then the behavior is the same as setting `REMOTE_LOGIN_PASSWORDFILE` to `none`.
- `exclusive`
	The password file can be used by only one database. The password file can contain `SYS` and non- `SYS` users.
	When `REMOTE_LOGIN_PASSWORDFILE` is set to `exclusive`, if the password file does not exist, then the behavior is the same as setting `REMOTE_LOGIN_PASSWORDFILE` to `none`.
- `none`
	Oracle ignores any password file. Therefore, privileged users must be authenticated by the operating system.

Note:

If you change `REMOTE_LOGIN_PASSWORDFILE` to `exclusive` or `shared` from `none`, then ensure that the password file is synchronized with the dictionary passwords.