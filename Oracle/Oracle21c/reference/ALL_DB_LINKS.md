---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_DB_LINKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.163 ALL\_DB\_LINKS

`ALL_DB_LINKS` describes the database links accessible to the current user.

Related Views

- `DBA_DB_LINKS` describes all database links in the database.
- `USER_DB_LINKS` describes the database links owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the database link |
| `DB_LINK` | `VARCHAR2(128)` | `NOT NULL` | Name of the database link |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user to be used when connecting to a remote database |
| `CREDENTIAL_NAME` | `VARCHAR2(128)` |  | Name of the credential to be used when connecting to a remote database |
| `CREDENTIAL_OWNER` | `VARCHAR2(128)` |  | Owner of the credential to be used when connecting to a remote database |
| `HOST` | `VARCHAR2(2000)` |  | Oracle Net connect string |
| `CREATED` | `DATE` | `NOT NULL` | Creation time of the database link |
| `HIDDEN` | `VARCHAR2(3)` |  | For internal use only |
| `SHARD_INTERNAL` | `VARCHAR2(3)` |  | Indicates whether the database link is used to support operations across sharded databases. Possible values:  - `YES`: The database link is used and managed for to support sharded databases - `NO`: The database link is not used and managed to support sharded databases  Users should not alter or delete database links that are used and managed to support sharded databases. |
| `VALID` | `VARCHAR2(3)` |  | Indicates whether the database link is valid and usable. Possible values:  - `` `YES` ``: The database link is valid and usable. - `` `NO` ``: The database link is invalid and unusable. |
| `INTRA_CDB` | `VARCHAR2(3)` |  | For internal use only |