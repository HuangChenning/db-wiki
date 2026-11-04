---
title: "V$PWFILE_USERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2111.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PWFILE_USERS` lists all users in the password file, and indicates whether the user has been granted the `SYSDBA`, `SYSOPER`, and `SYSASM` privileges.

| Column | Datatype | Description |
| --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` | Name of the user that is contained in the password file |
| `SYSDBA` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSDBA` privileges (`TRUE`) or not (`FALSE`) |
| `SYSOPER` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSOPER` privileges (`TRUE`) or not (`FALSE`) |
| `SYSASM` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSASM` privileges (`TRUE`) or not (`FALSE`) |