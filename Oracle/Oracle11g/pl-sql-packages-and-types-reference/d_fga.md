---
title: DBMS_FGA
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_fga.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 66 DBMS\_FGA

The `DBMS_FGA` package provides fine-grained security functions.

This chapter contains the following topics:

- Using DBMS\_FGA
- Summary of DBMS\_FGA Subprograms

---

## Using DBMS\_FGA

- Security Model
- Operational Notes

---

### Security Model

Execute privilege on `DBMS_FGA` is needed for administering audit policies. Because the audit function can potentially capture all user environment and application context values, policy administration should be executable by privileged users only. The policy event handler module will be executed with the module owner's privilege.

---

### Operational Notes

This package is available for only cost-based optimization. The rule-based optimizer may generate unnecessary audit records since audit monitoring can occur before row filtering. For both the rule-based optimizer and the cost-based optimizer, you can refer to `DBA_FGA_AUDIT_TRAIL` to analyze the SQL text and corresponding bind variables that are issued.

---

## Summary of DBMS\_FGA Subprograms

Table 66-1 DBMS\_FGA Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_POLICY Procedure | Creates an audit policy using the supplied predicate as the audit condition |
| DISABLE\_POLICY Procedure | Disables an audit policy |
| DROP\_POLICY Procedure | Drops an audit policy |
| ENABLE\_POLICY Procedure | Enables an audit policy |

---

### ADD\_POLICY Procedure

This procedure creates an audit policy using the supplied predicate as the audit condition. The maximum number of FGA policies on any table or view object is 256.

Syntax

```
DBMS_FGA.ADD_POLICY(
   object_schema      VARCHAR2, 
   object_name        VARCHAR2, 
   policy_name        VARCHAR2, 
   audit_condition    VARCHAR2, 
   audit_column       VARCHAR2, 
   handler_schema     VARCHAR2, 
   handler_module     VARCHAR2, 
   enable             BOOLEAN, 
   statement_types    VARCHAR2,
   audit_trail        BINARY_INTEGER IN DEFAULT,
   audit_column_opts  BINARY_INTEGER IN DEFAULT);
```

Parameters

Table 66-2 ADD\_POLICY Procedure Parameters

| Parameter | Description | Default Value |
| --- | --- | --- |
| `object_schema` | The schema of the object to be audited. `(``If NULL, the current log-on user schema is assumed.)` | `NULL` |
| `object_name` | The name of the object to be audited. | \- |
| `policy_name` | The unique name of the policy. | \- |
| `audit_condition` | A condition in a row that indicates a monitoring condition. `NULL` is allowed and acts as `TRUE`. | `NULL` |
| `audit_column` | The columns to be checked for access. These can include OLS hidden columns or object type columns. The default, `NULL`, causes audit if any column is accessed or affected. | `NULL` |
| `handler_schema` | The schema that contains the event handler. The default, `NULL`, causes the current schema to be used. | `NULL` |
| `handler_module` | The function name of the event handler; includes the package name if necessary. This function is invoked only after the first row that matches the audit condition in the query is processed. If the procedure fails with an exception, the user SQL statement will fail as well. | `NULL` |
| `enable` | Enables the policy if TRUE, which is the default. | `TRUE` |
| `statement_types` | The SQL statement types to which this policy is applicable: `INSERT`, `UPDATE`, `DELETE`, or `SELECT` only. | `SELECT` |
| `audit_trail` | Destination (DB or XML) of fine grained audit records. Also specifies whether to populate `LSQLTEXT` and `LSQLBIND` in `fga_log$`. | `DB+` `EXTENDED` |
| `audit_column_opts` | Establishes whether a statement is audited when the query references any column specified in the audit\_column parameter or only when all such columns are referenced. | `ANY_COLUMNS` |

Usage Notes

- If `object_schema` is not specified, the current log-on user schema is assumed.
- An FGA policy should not be applied to out-of-line columns such as LOB columns.
- Each audit policy is applied to the query individually. However, at most one audit record may be generated for each policy, no matter how many rows being returned satisfy that policy's `audit_condition`. In other words, whenever any number of rows being returned satisfy an audit condition defined on the table, a single audit record will be generated for each such policy.
- If a table with an FGA policy defined on it receives a Fast Path insert or a vectored update, the hint is automatically disabled before any such operations. Disabling the hint allows auditing to occur according to the policy's terms. (One example of a Fast Path insert is the statement `INSERT-WITH-APPEND-hint`.)
- The `audit_condition` must be a boolean expression that can be evaluated using the values in the row being inserted, updated, or deleted. The expression can also use functions, such as the `USER` or `SYS_CONTEXT` functions.
	The expression must not combine conditions using operators such as `AND` and `OR`. `audit_condition` can be `NULL` (or omitted), which is interpreted as `TRUE`, but it cannot contain the following elements:
	- Subqueries or sequences
		- The following attributes of the `USERENV` namespace when accessed using the `SYS_CONTEXT` function:
		- `CURRENT_SQL`
				- `CURRENT_SQL_LENGTH`
				- `CURRENT_BIND`
		- Any use of the pseudo columns `LEVEL, PRIOR, or ROWNUM`.
	Specifying an audit condition of "1=1" to force auditing of all specified statements (" `statement_types` ") affecting the specified column (" `audit_column` ") is no longer needed to achieve this purpose. A `NULL` value for `audit_condition` causes audit to happen even if no rows are processed, so that all actions on a table with this policy are audited.
- The `audit_condition` is evaluated using the privileges of the user who creates the policy.
- The audit function (`handler_module`) is an alerting mechanism for the administrator. The required interface for such a function is as follows:
	```
	PROCEDURE fname ( object_schema VARCHAR2, object_name VARCHAR2, policy_name VARCHAR2 )  AS ...
	```
	where `fname` is the name of the procedure, `object_schema` is the name of the schema of the table audited, `object_name` is the name of the table to be audited, and `policy_name` is the name of the policy being enforced. The audit function will be executed with the function owner's privilege.
	See Also:
	["Tutorial: Adding an E-Mail Alert to a Fine-Grained Audit Policy"](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG90057) in Oracle Database Security Guide for an example of creating an e-mail alert handler for a fine-grained audit policy
- The `audit_trail` parameter specifies both where the fine-grained audit trail will be written and whether it is to include the query's SQL Text and SQL Bind variable information (typically in columns named `LSQLTEXT` and `LSQLBIND`):
	- If audit\_trail includes XML, then fine-grained audit records are written to XML-format operating system files stored in the directory specified by an `AUDIT_FILE_DEST` statement in SQL. (The default `AUDIT_FILE_DEST` is `$ORACLE_BASE/admin/$DB_UNIQUE_NAME/adump` on Unix-based systems, and $ `ORACLE_BASE\admin\$DB_UNIQUE_NAME\adump` on Windows systems.)
		- If `audit_trail` includes `DB` instead, then the audit records are written to the `SYS.FGA_LOG$` table in the database. However, for read-only databases, Oracle Database writes the fine-grained audit records to XML files, regardless of the `audit_trail` settings.
		- If audit\_trail includes `EXTENDED`, then the query's SQL Text and SQL Bind variable information are included in the audit trail.
		Note that the SQL Text information could include sensitive data, such as credit card numbers, in the audit trail. See ["Auditing Sensitive Information"](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG10101) in Oracle Database Security Guide for ways in which you can handle this.
		- For example:
		- Setting `audit_trail` to `DBMS_FGA.DB` sends the audit trail to the `SYS.FGA_LOG$` table in the database and omits SQL Text and SQL Bind.
				- Setting `audit_trail` to `DBMS_FGA.DB + DBMS_FGA.EXTENDED` sends the audit trail to the `SYS.FGA_LOG$` table in the database and includes SQL Text and SQL Bind.
				- Setting `audit_trail` to `DBMS_FGA.XML` writes the audit trail in XML files sent to the operating system and omits SQL Text and SQL Bind.
				- Setting `audit_trail` to `DBMS_FGA.XML + DBMS_FGA.EXTENDED` writes the audit trail in XML files sent to the operating system and includes SQL Text and SQL Bind.
	The `audit_trail` parameter appears in the `ALL_AUDIT_POLICIES` view.
- You can change the operating system destination using the following command:
	`ALTER SYSTEM SET AUDIT_FILE_DEST = '<New Directory>' DEFERRED`
- On many platforms, XML audit files are named `<process_name>_<processId>.xml`, for example, `ora_2111.xml`, or `s002_11.xml`. On Windows, the XML audit files are named <process\_name>\_\<ThreadId>.xml (or <process\_name>\_ProcessId>.xml if the process is not running as a thread).
- The `audit_column_opts` parameter establishes whether a statement is audited
	- when the query references any column specified in the audit\_column parameter (`audit_column_opts` = `DBMS_FGA.ANY_COLUMNS`), or
		- only when all such columns are referenced (`audit_column_opts` = `DBMS_FGA.ALL_COLUMNS`).
	The default is `DBMS_FGA.ANY_COLUMNS`.
	The `ALL_AUDIT_POLICIES` view also shows `audit_column_opts`.
- When `audit_column_opts` is set to `DBMS_FGA.ALL_COLUMNS`, a SQL statement is audited only when all the columns mentioned in `audit_column` have been explicitly referenced in the statement. And these columns must be referenced in the same SQL-statement or in the sub-select.
	Also, all these columns must refer to a single table/view or alias.
	Thus, if a SQL statement selects the columns from different table aliases, the statement will not be audited.

V$XML\_AUDIT\_TRAIL View

The new values for the audit\_trail parameter (`XML` and `XML+EXTENDED`) cause fine-grained auditing records to be written to operating system files in XML format.

Audit records stored in operating system files can be more secure than database-stored audit records because access can require file permissions that DBAs do not have. Operating system storage for audit records also offers higher availability, since such records remain available even if the database is temporarily inaccessible.

A new dynamic view, `V$` `XML_AUDIT_TRAIL`, makes such audit records from XML files available to DBAs through SQL query, providing enhanced usability. Querying this view causes all XML files (all files with an`.xml` extension) in the `AUDIT_FILE_DEST` directory to be parsed and presented in relational table format.

The `DBA_COMMON_AUDIT_TRAIL` view includes the contents of the `V$` `XML_AUDIT_TRAIL` dynamic view for standard and fine-grained audit records.

Since the audit XML files are stored in files with extension`.xml` on all platforms, the dynamic view presents audit information similarly on all platforms, using the following schema:

Table 66-3 Elements in the V$XML\_AUDIT\_TRAIL Dynamic View

| Element | Type |
| --- | --- |
| `AUDIT_TYPE` | `VARCHAR2` `(18)` |
| `SESSION_ID` | `NUMBER` |
| `PROXY_SESSIONID` | `NUMBER` |
| `STATEMENTID` | `NUMBER` |
| `ENTRYID` | `NUMBER` |
| `EXTENDED_TIMESTAMP` | `TIMESTAMP(6) WITH TIME ZONE` |
| `GLOBAL_UID` | `VARCHAR2` `(32)` |
| `DB_USER` | `VARCHAR2(30)` |
| `CLIENT_ID` | `VARCHAR2(64)` |
| `EXT_NAME` | `VARCHAR2(4000)` |
| `OS_USER` | `VARCHAR2(255)` |
| `USERHOST` | `VARCHAR2(128`) |
| `OS_PROCESS` | `VARCHAR2(16)` |
| `TERMINAL` | `VARCHAR2(255)` |
| `INSTANCE_NUMBER` | `NUMBER` |
| `OBJECT_SCHEMA` | `VARCHAR2(30)` |
| `OBJECT_NAME` | `VARCHAR2(128)` |
| `POLICY_NAME` | `VARCHAR2(30)` |
| `STATEMENT_TYPE` | `VARCHAR2(28)` |
| `TRANSACTIONID` | `RAW(8)` |
| `SCN` | `NUMBER` |
| `COMMENT_TEXT` | `VARCHAR2(4000)` |
| `SQL_BIND` | `VARCHAR2(4000)` |
| `SQL_TEXT` | `VARCHAR2(4000)` |

Usage Notes

- Every XML audit record contains the elements `AUDIT_TYPE` and `EXTENDED_TIMESTAMP`, with the latter printed in UTC zone (with no timezone information). Values retrieved using `V$XML_AUDIT_TRAIL` view are converted to session timezone and printed.
- For `SQL_TEXT` and `SQL_BIND` element values (`CLOB` type columns), the dynamic view shows only the first 4000 characters. The underlying XML file may have more than 4000 characters for such `SQL_TEXT` and `SQL_BIND` values.
- For large numbers of XML audit files, querying `V$XML_AUDIT_TRAIL` is faster when they are loaded into a database table using SQL\*Loader or a similar tool. XML audit files are larger than the equivalent written to OS files when `AUDIT_TRAIL` =OS.
- Error handling is the same as when `AUDIT_TRAIL` =OS. If any error occurs in writing an audit record to disk, including the directory identified by `AUDIT_FILE_DEST` being full, the auditing operation fails. An alert message is logged.
- The policy event handler module will be executed with the module owner's privilege.
- Do not create recursive fine-grained audit handlers. For example, suppose you create a handler that executes an `INSERT` statement on the `HR.EMPLOYEES` table. The policy that is associated with this handler is for `INSERT` statements (as set by the statement\_types parameter). When the policy is used, the handler executes recursively until the system has run out of memory. This can raise the error `ORA-1000: maximum open cursors exceeded` or `ORA-00036: maximum number of recursive SQL levels (50) exceeded`. See also [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/vpd.htm#DBSEG248)

Examples

```
DBMS_FGA.ADD_POLICY (
   object_schema      =>  'scott', 
   object_name        =>  'emp', 
   policy_name        =>  'mypolicy1', 
   audit_condition    =>  'sal < 100', 
   audit_column       =>  'comm,sal', 
   handler_schema     =>   NULL, 
   handler_module     =>   NULL, 
   enable             =>   TRUE, 
   statement_types    =>  'INSERT, UPDATE', 
   audit_trail        =>   DBMS_FGA.XML + DBMS_FGA.EXTENDED, 
   audit_column_opts  =>   DBMS_FGA.ANY_COLUMNS);
```

---

### DISABLE\_POLICY Procedure

This procedure disables an audit policy.

Syntax

```
DBMS_FGA.DISABLE_POLICY(
   object_schema  VARCHAR2, 
   object_name    VARCHAR2, 
   policy_name    VARCHAR2 );
```

Parameters

Table 66-4 DISABLE\_POLICY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `object_schema` | The schema of the object to be audited. (If `NULL`, the current log-on user schema is assumed.) |
| `object_name` | The name of the object to be audited. |
| `policy_name` | The unique name of the policy. |

The default value for `object_schema` is `NULL`. (If `NULL`, the current log-on user schema is assumed.)

Examples

```
DBMS_FGA.DISABLE_POLICY (
object_schema   =>  'scott',
object_name     =>  'emp',
policy_name     =>  'mypolicy1');
```

---

### DROP\_POLICY Procedure

This procedure drops an audit policy.

Syntax

```
DBMS_FGA.DROP_POLICY(
   object_schema  VARCHAR2, 
   object_name    VARCHAR2, 
   policy_name    VARCHAR2 );
```

Parameters

Table 66-5 DROP\_POLICY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `object_schema` | The schema of the object to be audited. (If `NULL`, the current log-on user schema is assumed.) |
| `object_name` | The name of the object to be audited. |
| `policy_name` | The unique name of the policy. |

Usage Notes

The `DBMS_FGA` procedures cause current DML transactions, if any, to commit before the operation unless they are inside a DDL event trigger. With DDL transactions, the `DBMS_FGA` procedures are part of the DDL transaction. The default value for object\_schema is `NULL`. (If `NULL`, the current log-on user schema is assumed.`)`

Note:

Oracle Database automatically drops the audit policy if you remove the object specified in the `object_name` parameter of the `DBMS_FGA.ADD_POLICY` procedure, or if you drop the user who created the audit policy.

Examples

```
DBMS_FGA.DROP_POLICY (
object_schema   =>  'scott',
object_name     =>  'emp',
policy_name     =>  'mypolicy1');
```

---

### ENABLE\_POLICY Procedure

This procedure enables an audit policy.

Syntax

```
DBMS_FGA.ENABLE_POLICY(
   object_schema  VARCHAR2,
   object_name    VARCHAR2,
   policy_name    VARCHAR2,
   enable         BOOLEAN);
```

Parameters

Table 66-6 ENABLE\_POLICY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `object_schema` | The schema of the object to be audited. (If `NULL`, the current log-on user schema is assumed.) |
| `object_name` | The name of the object to be audited. |
| `policy_name` | The unique name of the policy. |
| `enable` | Defaults to `TRUE` to enable the policy. |

Examples

```
DBMS_FGA.ENABLE_POLICY (
object_schema    =>  'scott',
object_name      =>  'emp',
policy_name      =>  'mypolicy1',
enable           =>   TRUE);
```