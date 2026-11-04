---
title: REMOTE_LOGIN_PASSWORDFILE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams212.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REMOTE_LOGIN_PASSWORDFILE = { shared \| exclusive \| none }` |
| Default value | `exclusive` |
| Modifiable | No |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

`REMOTE_LOGIN_PASSWORDFILE` specifies whether Oracle checks for a password file.

Values:

- `shared`
	One or more databases can use the password file. The password file can contain `SYS` as well as non- `SYS` users.
- `exclusive`
	The password file can be used by only one database. The password file can contain `SYS` as well as non- `SYS` users.
- `none`
	Oracle ignores any password file. Therefore, privileged users must be authenticated by the operating system.

Notes:

- When `REMOTE_LOGIN_PASSWORDFILE` is set to either `exclusive` or `shared`, but the password file does not exist, then the behavior is the same as setting `REMOTE_LOGIN_PASSWORDFILE` to `none`.
- If you change `REMOTE_LOGIN_PASSWORDFILE` to `exclusive` or `shared` from `none`, then ensure that the password file is in sync with the dictionary passwords. See [Oracle Database Administrator's Guide f](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN11060) or more information.