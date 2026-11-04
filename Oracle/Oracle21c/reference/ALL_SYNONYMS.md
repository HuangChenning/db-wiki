---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SYNONYMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.103 ALL\_SYNONYMS

`ALL_SYNONYMS` describes the synonyms accessible to the current user.

The following criteria determine the list of synonyms that `ALL_SYNONYMS` shows:

- All private synonyms owned by the logged-in user, even if the base object pointed to is not accessible.
- All public synonyms, even if the base object pointed to is not accessible.
- All private synonyms owned by a different user, where the ultimate base object pointed to by that synonym or by any chain of nested synonyms, is know to be accessible because of a grant to the logged-in user, or a grant to a role in effect for this session.
- If the current session has any of the following privileges, then all synonyms that point directly to local objects are shown because it is assumed that the session can access those objects:
	- `LOCK ANY TABLE`
		- `READ ANY TABLE`
		- `SELECT ANY TABLE`
		- `INSERT ANY TABLE`
		- `UPDATE ANY TABLE`
		- `DELETE ANY TABLE`
	Synonyms that point to remote objects are excluded because the system privileges just listed do not automatically convey access to those remote objects. Also, if the synonyms point to objects other than tables and views (such as sequences, PL/SQL procedures, and so on) then this rule may show synonyms that ultimately resolve to objects that this session cannot access.
- All private synonyms owned by a different user, where the synonym is via a database link, are excluded.

Related Views

- `DBA_SYNONYMS` describes all synonyms in the database.
- `USER_SYNONYMS` describes the synonyms owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the synonym |
| `SYNONYM_NAME` | `VARCHAR2(128)` |  | Name of the synonym |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the object referenced by the synonym, or creator of the referring synonym if the target is a public synonym (that is, the object referred to by `TABLE_NAME`).  Although the column is called `TABLE_OWNER`, the object owned is not necessarily a table. It can be any general object such as a view, sequence, stored procedure, synonym, and so on. |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the object referenced by the synonym. Although the column is called `TABLE_NAME`, the object does not necessarily have to be a table. It can be any general object such as a view, sequence, stored procedure, synonym, and so on. |
| `DB_LINK` | `VARCHAR2(128)` |  | Name of the database link referenced, if any |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

See Also:

- " [DBA\_SYNONYMS](DBA_SYNONYMS.md) "
- " [USER\_SYNONYMS](USER_SYNONYMS.md) "