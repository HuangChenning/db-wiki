---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CREDENTIALS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.142 ALL\_CREDENTIALS

`ALL_CREDENTIALS` lists all credentials visible to the user.

Related Views

- `DBA_CREDENTIALS` lists all credentials in the database.
- `USER_CREDENTIALS` lists credentials owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the credential |
| `CREDENTIAL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the credential |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user that will be used to log in to the remote database or the remote or local operating system |
| `WINDOWS_DOMAIN` | `VARCHAR2(30)` |  | For a Windows target, the Windows domain to use when logging in |