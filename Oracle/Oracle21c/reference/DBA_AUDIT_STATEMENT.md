---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUDIT_STATEMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.176 DBA\_AUDIT\_STATEMENT

`DBA_AUDIT_STATEMENT` displays audit trail records for all `GRANT`, `REVOKE`, `AUDIT`, `NOAUDIT`, and `ALTER SYSTEM` statements in the database.

Note:

This view is relevant when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

Related View

`USER_AUDIT_STATEMENT` displays audit trail records for the `GRANT`, `REVOKE`, `AUDIT`, `NOAUDIT`, and `ALTER SYSTEM` statements issued by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OS_USERNAME` | `VARCHAR2(255)` |  | Operating system login username of the user whose actions were audited |
| `USERNAME ` | `VARCHAR2(128)` |  | Name (not ID number) of the user whose actions were audited |
| `USERHOST ` | `VARCHAR2(128)` |  | Client host machine name |
| `TERMINAL ` | `VARCHAR2(255)` |  | Identifier of the user's terminal |
| `TIMESTAMP ` | `DATE` |  | Date and time of the creation of the audit trail entry (date and time of user login for entries created by `AUDIT SESSION`) in the local database session time zone |
| `OWNER` | `VARCHAR2(128)` |  | Creator of the object affected by the action |
| `OBJ_NAME ` | `VARCHAR2(128)` |  | Name of the object affected by the action |
| `ACTION_NAME ` | `VARCHAR2(28)` |  | Name of the action type corresponding to the numeric code in the `ACTION` column in `DBA_AUDIT_TRAIL` |
| `NEW_NAME` | `VARCHAR2(128)` |  | New name of an object after a `RENAME` or the name of the underlying object |
| `OBJ_PRIVILEGE ` | `VARCHAR2(32)` |  | Object privileges granted or revoked by a `GRANT` or `REVOKE` statement. The value of this column is a 32-character string of `Y` and dash (`-`) characters. Each character corresponds to a numbered privilege in the following list. The left-most character corresponds to privilege 0, the next character corresponds to privilege 1, and so on. The right-most character corresponds to privilege 31.  - 0 - `ALTER` - 1 - `AUDIT` - 2 - `COMMENT` - 3 - `DELETE` - 4 - `GRANT` - 5 - `INDEX` - 6 - `INSERT` - 7 - `LOCK` - 8 - `CREATE` - 9 - `SELECT` - 10 - `UPDATE` - 11 - `REFERENCES` - 12 - `EXECUTE` - 13 - `VIEW` - 14 - `DROP` - 15 - `ANALYZE` - 16 - `CREATE` - 17 - `READ` - 18 - `WRITE` - 19 - `KEEP` `SEQUENCE` - 20 - `ENQUEUE` - 21 - `DEQUEUE` - 22 - `UNDER` - 23 - `ON` `COMMIT` - 24 - `REWRITE` - 25 - `UPSERT` - 26 - `DEBUG` - 27 - `FLASHBACK` - 28 - `MERGE` - 29 - `USE` - 30 - `FLASHBACK` `ARCHIVE` - 31 - `DIRECTORY` `EXECUTE`  A `Y` indicates that the privilege was granted or revoked by the statement. A dash indicates that the privilege was not affected by the statement. For example, the following value indicates that the `MERGE` privilege was granted or revoked by the statement:  `----------------------------Y---` |
| `SYS_PRIVILEGE ` | `VARCHAR2(40)` |  | System privileges granted or revoked by a `GRANT` or `REVOKE` statement |
| `ADMIN_OPTION` | `VARCHAR2(1)` |  | Signifies the role or system privilege was granted with the `ADMIN` option |
| `GRANTEE` | `VARCHAR2(128)` |  | Name of the grantee specified in a `GRANT` or `REVOKE` statement |
| `AUDIT_OPTION` | `VARCHAR2(40)` |  | Auditing option set with the `AUDIT` statement |
| `SES_ACTIONS ` | `VARCHAR2(19)` |  | Session summary (a string of 16 characters, one for each action type in the order `ALTER`, `AUDIT`, `COMMENT`, `DELETE`, `GRANT`, `INDEX`, `INSERT`, `LOCK`, `RENAME`, `SELECT`, `UPDATE`, `REFERENCES`, and `EXECUTE`). Positions 14, 15, and 16 are reserved for future use. The characters are:  - `-` - None - `S` - Success - `F` - Failure - `B` - Both |
| `COMMENT_TEXT ` | `VARCHAR2(4000)` |  | Text comment on the audit trail, inserted by the application |
| `SESSIONID` | `NUMBER` | `NOT NULL` | Numeric ID for each Oracle session |
| `ENTRYID` | `NUMBER` | `NOT NULL` | Numeric ID for each audit trail entry in the session |
| `STATEMENTID` | `NUMBER` | `NOT NULL` | Numeric ID for each statement run |
| `RETURNCODE` | `NUMBER` | `NOT NULL` | Oracle error code generated by the action. Some useful values:  - `0` - Action succeeded - `2004` - Security violation |
| `PRIV_USED` | ` VARCHAR2(40)` |  | System privilege used to execute the action |
| `CLIENT_ID` | `VARCHAR2(128)` |  | Client identifier in each Oracle session |
| `ECONTEXT_ID` | `VARCHAR2(64)` |  | Application execution context identifier |
| `SESSION_CPU` | `NUMBER` |  | Amount of CPU time used by each Oracle session |
| `EXTENDED_TIMESTAMP` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of the creation of the audit trail entry (timestamp of user login for entries created by `AUDIT SESSION`) in UTC (Coordinated Universal Time) time zone |
| `PROXY_SESSIONID` | `NUMBER` |  | Proxy session serial number, if an enterprise user has logged in through the proxy mechanism |
| `GLOBAL_UID` | `VARCHAR2(32)` |  | Global user identifier for the user, if the user has logged in as an enterprise user |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number as specified by the `INSTANCE_NUMBER` initialization parameter |
| `OS_PROCESS` | `VARCHAR2(16)` |  | Operating System process identifier of the Oracle process |
| `TRANSACTIONID` | `RAW(8)` |  | Transaction identifier of the transaction in which the object is accessed or modified |
| `SCN` | `NUMBER` |  | System change number (SCN) of the query |
| `SQL_BIND` | `NVARCHAR2(2000)` |  | Bind variable data of the query |
| `SQL_TEXT` | `NVARCHAR2(2000)` |  | SQL text of the query |
| `OBJ_EDITION_NAME` | `VARCHAR2(128)` |  | Name of the edition containing the audited object |

Note:

The `SQL_BIND` and `SQL_TEXT` columns are only populated if the `AUDIT_TRAIL` initialization parameter is set to `db`, `extended`.

See Also:

- " [AUDIT\_TRAIL](AUDIT_TRAIL.md) "
- " [USER\_AUDIT\_STATEMENT](USER_AUDIT_STATEMENT.md) "