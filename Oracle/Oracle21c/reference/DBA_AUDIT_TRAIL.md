---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUDIT_TRAIL.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.177 DBA\_AUDIT\_TRAIL

`DBA_AUDIT_TRAIL` displays all standard audit trail entries.

Note:

This view is relevant when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

Related View

`USER_AUDIT_TRAIL` displays the standard audit trail entries related to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OS_USERNAME` | `VARCHAR2(255)` |  | Operating system login username of the user whose actions were audited |
| `USERNAME` | `VARCHAR2(128)` |  | Name (not ID number) of the user whose actions were audited |
| `USERHOST` | `VARCHAR2(128)` |  | Client host machine name |
| `TERMINAL` | `VARCHAR2(255)` |  | Identifier of the user's terminal |
| `TIMESTAMP ` | `DATE` |  | Date and time of the creation of the audit trail entry (date and time of user login for entries created by `AUDIT SESSION`) in the local database session time zone |
| `OWNER` | `VARCHAR2(128)` |  | Creator of the object affected by the action |
| `OBJ_NAME ` | `VARCHAR2(128)` |  | Name of the object affected by the action |
| `ACTION` | `NUMBER` | `NOT NULL` | Numeric action type code. The corresponding name of the action type is in the `ACTION_NAME` column. |
| `ACTION_NAME ` | `VARCHAR2(28)` |  | Name of the action type corresponding to the numeric code in the `ACTION` column |
| `NEW_OWNER ` | `VARCHAR2(128)` |  | Owner of the object named in the `NEW_NAME` column |
| `NEW_NAME` | `VARCHAR2(128)` |  | New name of the object after a `RENAME` or the name of the underlying object |
| `OBJ_PRIVILEGE ` | `VARCHAR2(32)` |  | Object privileges granted or revoked by a `GRANT` or `REVOKE` statement. The value of this column is a 32-character string of `Y` and dash (`-`) characters. Each character corresponds to a numbered privilege in the following list. The left-most character corresponds to privilege 0, the next character corresponds to privilege 1, and so on. The right-most character corresponds to privilege 31.  - 0 - `ALTER` - 1 - `AUDIT` - 2 - `COMMENT` - 3 - `DELETE` - 4 - `GRANT` - 5 - `INDEX` - 6 - `INSERT` - 7 - `LOCK` - 8 - `CREATE` - 9 - `SELECT` - 10 - `UPDATE` - 11 - `REFERENCES` - 12 - `EXECUTE` - 13 - `VIEW` - 14 - `DROP` - 15 - `ANALYZE` - 16 - `CREATE` - 17 - `READ` - 18 - `WRITE` - 19 - `KEEP` `SEQUENCE` - 20 - `ENQUEUE` - 21 - `DEQUEUE` - 22 - `UNDER` - 23 - `ON` `COMMIT` - 24 - `REWRITE` - 25 - `UPSERT` - 26 - `DEBUG` - 27 - `FLASHBACK` - 28 - `MERGE` - 29 - `USE` - 30 - `FLASHBACK` `ARCHIVE` - 31 - `DIRECTORY` `EXECUTE`  A `Y` indicates that the privilege was granted or revoked by the statement. A dash indicates that the privilege was not affected by the statement. For example, the following value indicates that the `MERGE` privilege was granted or revoked by the statement:  `----------------------------Y---` |
| `SYS_PRIVILEGE ` | `VARCHAR2(40)` |  | System privileges granted or revoked by a `GRANT` or `REVOKE` statement |
| `ADMIN_OPTION` | `VARCHAR2(1)` |  | Indicates whether the role or system privilege was granted with the `ADMIN` option |
| `GRANTEE` | `VARCHAR2(128)` |  | Name of the grantee specified in a `GRANT` or `REVOKE` statement |
| `AUDIT_OPTION` | `VARCHAR2(40)` |  | Auditing option set with the `AUDIT` statement |
| `SES_ACTIONS` | `VARCHAR2(19)` |  | Session summary (a string of 16 characters, one for each action type in the order `ALTER`, `AUDIT`, `COMMENT`, `DELETE`, `GRANT`, `INDEX`, `INSERT`, `LOCK`, `RENAME`, `SELECT`, `UPDATE`, `REFERENCES`, and `EXECUTE`). Positions 14, 15, and 16 are reserved for future use. The characters are:  - `-` - None - `S` - Success - `F` - Failure - `B` - Both |
| `LOGOFF_TIME` | `DATE` |  | Date and time of user log off |
| `LOGOFF_LREAD` | `NUMBER` |  | Logical reads for the session |
| `LOGOFF_PREAD` | `NUMBER` |  | Physical reads for the session |
| `LOGOFF_LWRITE` | `NUMBER` |  | Logical writes for the session |
| `LOGOFF_DLOCK` | `VARCHAR2(40)` |  | Deadlocks detected during the session |
| `COMMENT_TEXT ` | `VARCHAR2(4000)` |  | Text comment on the audit trail entry, providing more information about the statement audited  Also indicates how the user or remote call was authenticated. The method can be one of the following:  - `DATABASE` - Authentication was done by password - `NETWORK` - Authentication was done by Oracle Net Services or strong authentication - `PROXY` - Client was authenticated by another user; the name of the proxy user follows the method type  When an object is accessed remotely over a database link, the `COMMENT_TEXT` column also captures the information about the database link. For example:  ``` DBLINK_INFO: (SOURCE_GLOBAL_NAME=view02.regress.rdbms.dev.us.example.com,  DBLINK_NAME=VIEW05_LINK.REGRESS.RDBMS.DEV.US.EXAMPLE.COM,  SOURCE_AUDIT_SESSIONID=250805) ``` |
| `SESSIONID` | `NUMBER` | `NOT NULL` | Numeric ID for each Oracle session. Each user session gets a unique session ID. |
| `ENTRYID` | `NUMBER` | `NOT NULL` | Numeric ID for each audit trail entry in the session. The entry ID is an index of a session's audit entries that starts at 1 and increases to the number of entries that are written. |
| `STATEMENTID` | `NUMBER` | `NOT NULL` | nth statement in the user session. The first SQL statement gets a value of 1 and the value is incremented for each subsequent SQL statement. Note that one SQL statement can create more than one audit trail entry (for example, when more than one object is audited from the same SQL statement), and in this case the statement ID remains the same for that statement and the entry ID increases for each audit trail entry created by the statement. |
| `RETURNCODE` | `NUMBER` | `NOT NULL` | Oracle error code generated by the action. Some useful values:  - `0` - Action succeeded - `2004` - Security violation |
| `PRIV_USED` | `VARCHAR2(40)` |  | System privilege used to execute the action |
| `CLIENT_ID` | `VARCHAR2(128)` |  | Client identifier in each Oracle session |
| `ECONTEXT_ID` | `VARCHAR2(64)` |  | Application execution context identifier |
| `SESSION_CPU` | `NUMBER` |  | Amount of CPU time used by each Oracle session (in centiseconds) |
| `EXTENDED_TIMESTAMP` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of the creation of the audit trail entry (timestamp of user login for entries created by `AUDIT SESSION`) in UTC (Coordinated Universal Time) time zone |
| `PROXY_SESSIONID` | `NUMBER` |  | Proxy session serial number, if an enterprise user has logged in through the proxy mechanism |
| `GLOBAL_UID` | `VARCHAR2(32)` |  | Global user identifier for the user, if the user has logged in as an enterprise user |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number as specified by the `INSTANCE_NUMBER` initialization parameter |
| `OS_PROCESS` | `VARCHAR2(16)` |  | Operating System process identifier of the Oracle process |
| `TRANSACTIONID` | `RAW(8)` |  | Transaction identifier of the transaction in which the object is accessed or modified |
| `SCN` | `NUMBER` |  | System change number (SCN) of the creation of the audit trail entry |
| `SQL_BIND` | `NVARCHAR2(2000)` |  | Bind variable data of the query |
| `SQL_TEXT` | `NVARCHAR2(2000)` |  | SQL text of the query |
| `OBJ_EDITION_NAME` | `VARCHAR2(128)` |  | Name of the edition containing the audited object |
| `DBID` | `NUMBER` |  | Database identifier of the audited database |
| `RLS_INFO` | `CLOB` |  | Stores virtual private database (VPD) policy names and predicates separated by delimiter.  To format the output into individual rows, use the `DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_STD` function. |
| `CURRENT_USER` | `VARCHAR2(128)` |  | Effective user for the statement execution |

Note:

The `SQL_BIND` and `SQL_TEXT` columns are only populated if the `AUDIT_TRAIL` initialization parameter is set to `db`, `extended`.

See Also:

- " [AUDIT\_TRAIL](AUDIT_TRAIL.md) "
- " [USER\_AUDIT\_TRAIL](USER_AUDIT_TRAIL.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-B71876E3-EE8D-484B-8668-331617F40FEB) for more information about the `DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_XML` function.