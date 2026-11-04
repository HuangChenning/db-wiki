---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LDAP_DIRECTORY_SYSAUTH.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.174 LDAP\_DIRECTORY\_SYSAUTH

`LDAP_DIRECTORY_SYSAUTH` allows or disallows directory-based authorization for users granted administrative privileges, such as `SYSDBA`, `SYSOPER`, `SYSBACKUP`, `SYSDG`, and `SYSKM`.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LDAP_DIRECTORY_SYSAUTH = { yes \| no }` |
| Default value | `no` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Basic | Yes |

When `LDAP_DIRECTORY_SYSAUTH` is set to `yes`, directory users are allowed to connect to the database as `SYSDBA`, `SYSOPER`, `SYSBACKUP`, `SYSDG`, or `SYSKM`, if they have mapped database global users that are granted corresponding administrative privileges such as `SYSDBA`, `SYSOPER`, `SYSBACKUP`, `SYSDG`, and `SYSKM`.

When `LDAP_DIRECTORY_SYSAUTH` is set to no, directory users are not allowed to connect to the database as `SYSDBA`, `SYSOPER`, `SYSBACKUP`, `SYSDG`, or `SYSKM`, even if they have mapped database global users that are granted corresponding administrative privileges such as `SYSDBA`, `SYSOPER`, `SYSBACKUP`, `SYSDG`, and `SYSKM`.

When modifying this parameter in a PDB, use the `ALTER` `SYSTEM` command with `SCOPE=SPFILE`.