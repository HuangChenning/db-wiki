---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XSTREAM_AUTH.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 222 DBMS\_XSTREAM\_AUTH

The `DBMS_XSTREAM_AUTH` package provides subprograms for granting privileges to and revoking privileges from XStream administrators.

This chapter contains the following topic:

See Also:

GRANT\_ADMIN\_PRIVILEGE Procedure

### 222.1 DBMS\_XSTREAM\_AUTH Overview

This package provides subprograms for granting privileges to XStream administrators and revoking privileges from XStream administrators.

### 222.2 DBMS\_XSTREAM\_AUTH Security Model

Security on this package can be controlled by either granting `EXECUTE` on this package to selected users or roles, or by granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

The user executing the subprograms in the `DBMS_XSTREAM_AUTH` package must have `SYSDBA` administrative privilege, and the user must exercise the privilege using `AS SYSDBA` at connect time.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

To ensure that the user who runs the subprograms in this package has the necessary privileges, connect as an administrative user who can create users, grant privileges, and create tablespaces when using this package.

### 222.3 Summary of DBMS\_XSTREAM\_AUTH Subprograms

This table lists the `DBMS_XSTREAM_AUTH` subprograms and briefly describes them.

Table 222-1 DBMS\_XSTREAM\_AUTH Package Subprograms

| Subprogram | Description |
| --- | --- |
| GRANT\_ADMIN\_PRIVILEGE Procedure | Either grants the privileges needed by a user to be an XStream administrator directly, or generates a script that grants these privileges |
| GRANT\_REMOTE\_ADMIN\_ACCESS Procedure | Enables a remote XStream administrator to perform administrative actions at the local database by connecting to the grantee using a database link |
| REVOKE\_ADMIN\_PRIVILEGE Procedure | Either revokes XStream administrator privileges from a user directly, or generates a script that revokes these privileges |
| REVOKE\_REMOTE\_ADMIN\_ACCESS Procedure | Disables a remote XStream administrator from performing administrative actions by connecting to the grantee using a database link |

Note:

All subprograms commit unless specified otherwise.

#### 222.3.1 GRANT\_ADMIN\_PRIVILEGE Procedure

This procedure either grants the privileges needed by a user to be an XStream administrator directly, or generates a script that grants these privileges.

See Also:

" GRANT\_ADMIN\_PRIVILEGE Procedure "

Syntax

```
DBMS_XSTREAM_AUTH.GRANT_ADMIN_PRIVILEGE(
   grantee                    IN  VARCHAR2,
   privilege_type             IN  VARCHAR2  DEFAULT '*',
   grant_select_privileges    IN  BOOLEAN   DEFAULT FALSE,
   do_grants                  IN  BOOLEAN   DEFAULT TRUE,
   file_name                  IN  VARCHAR2  DEFAULT NULL,
   directory_name             IN  VARCHAR2  DEFAULT NULL
   grant_optional_privileges  IN  VARCHAR2  DEFAULT NULL,
   container                  IN  VARCHAR2  DEFAULT 'CURRENT');
```

Parameters

Table 222-2 GRANT\_ADMIN\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `grantee` | The user to whom privileges are granted |
| `privilege_type` | Specify one of the following values:  - `CAPTURE` 	Specifying `CAPTURE` grants the minimum privileges required by the user to administer capture processes. - `APPLY` 	Specifying `APPLY` grants the minimum privileges required by the user to administer outbound servers, inbound servers, and apply processes. - `*` 	Specifying `*` grants the minimum privileges required by the user to administer capture processes, outbound servers, inbound servers, and apply processes. |
| `grant_select_privileges` | If `TRUE`, then the procedure grants a set of privileges, including `SELECT_CATALOG_ROLE`, to the user.  If `FALSE`, then the procedure does not grant the set of privileges to the user.  `SELECT_CATALOG_ROLE` enables the user to select from the data dictionary. Set this parameter to `TRUE` for the XStream trusted user model. Set this parameter to `FALSE` for the XStream untrusted user model. |
| `do_grants` | If `TRUE`, then the procedure grants the privileges to the specified grantee directly, and adds the grantee to the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view with `YES` for both the `LOCAL_PRIVILEGES` column and the `ACCESS_FROM_REMOTE` column. If the user already has an entry in this data dictionary view, then the procedure does not make another entry, and no error is raised. If `TRUE` and any of the grant statements fails, then the procedure raises an error.  If `FALSE`, then the procedure does not grant the privileges to the specified grantee directly, and does not add the grantee to the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view.  You specify `FALSE` when the procedure is generating a file that you will run later. If you specify `FALSE` and either the `file_name` or `directory_name` parameter is `NULL`, then the procedure raises an error. |
| `file_name` | The name of the file generated by the procedure. The file contains all of the statements that grant the privileges. If a file with the specified file name exists in the specified directory name, then the grant statements are appended to the existing file.  If `NULL`, then the procedure does not generate a file. |
| `directory_name` | The directory into which the generated file is placed. The specified directory must be a directory object created using the SQL statement `CREATE` `DIRECTORY`. If you specify a directory, then the user who invokes the procedure must have the `WRITE` privilege on the directory object.  If `t` he `file_name` parameter is `NULL`, then this parameter is ignored, and the procedure does not generate a file.  If `NULL` and the `file_name` parameter is non- `NULL`, then the procedure raises an error. |
| `grant_optional_privileges` | A comma-separated list of optional privileges to grant to the grantee, such as the `DV_XSTREAM_ADMIN` and `DV_GOLDENGATE_ADMIN` privileges |
| `container` | If `CURRENT`, then grants privileges to the grantee only in the container where the procedure is invoked. `CURRENT` can be specified while connected to the root or to a PDB.  If `ALL`, then grants privileges to the grantee in all containers in the CDB and all PDBs created after the procedure is invoked. To specify `ALL`, the procedure must be invoked in the root.  If a container name, then grants privileges to the grantee only in the specified container. To specify root, use `CDB$ROOT` while connected to the root. To specify a PDB, the procedure must be invoked in the root.  Note: This parameter only applies to CDBs. |

Usage Notes

The user who runs the procedure must be an administrative user who can grant privileges to other users.

Specifically, the procedure grants the following privileges to the specified user:

- The `RESTRICTED` `SESSION` system privilege
- `EXECUTE` on the following packages:
	- `DBMS_APPLY_ADM`
		- `DBMS_AQ`
		- `DBMS_AQADM`
		- `DBMS_AQIN`
		- `DBMS_AQELM`
		- `DBMS_CAPTURE_ADM`
		- `DBMS_FLASHBACK`
		- `DBMS_LOCK`
		- `DBMS_PROPAGATION_ADM`
		- `DBMS_RULE_ADM`
		- `DBMS_TRANSFORM`
		- `DBMS_XSTREAM_ADM`
- Privileges to enqueue messages into and dequeue messages from any queue
- Privileges to manage any queue
- Privileges to create, alter, and execute any of the following types of objects in the user's own schema and in other schemas:
	- Evaluation contexts
		- Rule sets
		- Rules
	In addition, the grantee can grant these privileges to other users.
- `SELECT_CATALOG_ROLE`
- `SELECT` or `READ` privilege on data dictionary views related to XStream and Oracle Replication
- The ability to allow a remote XStream administrator to perform administrative actions through a database link by connecting to the grantee
	This ability is enabled by running the `GRANT_REMOTE_ADMIN_ACCESS` procedure in this package.
	Note:
	- To view all of the statements run by the procedure in detail, you can use the procedure to generate a script and then view the script in a text editor.
	- This procedure grants only the privileges necessary to configure and administer an XStream environment. You can grant additional privileges to the grantee if necessary.
	See Also:
	- " GRANT\_REMOTE\_ADMIN\_ACCESS Procedure "
	- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF01207) for information about the `CREATE` `DIRECTORY` SQL statement

#### 222.3.2 GRANT\_REMOTE\_ADMIN\_ACCESS Procedure

This procedure enables a remote XStream administrator to perform administrative actions at the local database by connecting to the grantee using a database link.

Syntax

```
DBMS_XSTREAM_AUTH.GRANT_REMOTE_ADMIN_ACCESS(
   grantee  IN  VARCHAR2);
```

Parameters

Table 222-3 GRANT\_REMOTE\_ADMIN\_ACCESS Procedure Parameter

| Parameter | Description |
| --- | --- |
| `grantee` | The user who allows remote access. The procedure adds the grantee to the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view with `YES` for the `ACCESS_FROM_REMOTE` column. If the user already has an entry in this data dictionary view, then the procedure does not make another entry. Instead, it updates the `ACCESS_FROM_REMOTE` column to `YES`. |

Usage Notes

Typically, you run the procedure and specify a grantee at a local source database if a downstream capture process captures changes originating at the local source database. The XStream administrator at a downstream capture database administers the source database using this connection.

Note:

The `GRANT_ADMIN_PRIVILEGE` procedure in this package runs this procedure.

See Also:

" GRANT\_ADMIN\_PRIVILEGE Procedure "

#### 222.3.3 REVOKE\_ADMIN\_PRIVILEGE Procedure

This procedure either revokes XStream administrator privileges from a user directly, or generates a script that revokes these privileges.

Syntax

```
DBMS_XSTREAM_AUTH.REVOKE_ADMIN_PRIVILEGE(
   grantee                     IN  VARCHAR2,  
   privilege_type              IN  VARCHAR2  DEFAULT '*',
   revoke_select_privileges    IN  BOOLEAN   DEFAULT FALSE,
   do_revokes                  IN  BOOLEAN   DEFAULT TRUE,
   file_name                   IN  VARCHAR2  DEFAULT NULL,
   directory_name              IN  VARCHAR2  DEFAULT NULL
   revoke_optional_privileges  IN  VARCHAR2  DEFAULT NULL,
   container                   IN  VARCHAR2  DEFAULT 'CURRENT');
```

Parameters

Table 222-4 REVOKE\_ADMIN\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `grantee` | The user from whom privileges are revoked |
| `privilege_type` | Specify one of the following values:  - `CAPTURE` 	Specifying `CAPTURE` revokes the minimum privileges required by the user to administer capture processes. - `APPLY` 	Specifying `APPLY` revokes the minimum privileges required by the user to administer outbound servers, inbound servers, and apply processes. - `*` 	Specifying `*` revokes the minimum privileges required by the user to administer capture processes, outbound servers, inbound servers, and apply processes. |
| `revoke_select_privileges` | If `TRUE`, then the procedure revokes a set of privileges, including `SELECT_CATALOG_ROLE`, to the user.  If `FALSE`, then the procedure does not revoke the set of privileges to the user.  `SELECT_CATALOG_ROLE` enables the user to select from the data dictionary. |
| `do_revokes` | If `TRUE`, then the procedure revokes the privileges from the specified user directly, and removes the user from the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view. If the user does not have a record in this data dictionary view, then the procedure does not remove a record from the view, and no error is raised. If `TRUE` and any of the revoke statements fails, then the procedure raises an error. A revoke statement fails if the user is not granted the privilege that is being revoked.  If `FALSE`, then the procedure does not revoke the privileges from the specified user directly, and does not remove the user from the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view.  You specify `FALSE` when the procedure is generating a file that you will run later. If you specify `FALSE` and either the `file_name` or `directory_name` parameter is `NULL`, then the procedure does not raise an error. |
| `file_name` | The name of the file generated by this procedure. The file contains all of the statements that revoke the privileges. If a file with the specified file name exists in the specified directory name, then the revoke statements are appended to the existing file.  If `NULL`, then the procedure does not generate a file. |
| `directory_name` | The directory into which the generated file is placed. The specified directory must be a directory object created using the SQL statement `CREATE` `DIRECTORY`. If you specify a directory, then the user who invokes the procedure must have the `WRITE` privilege on the directory object.  If the `file_name` parameter is `NULL`, then this parameter is ignored, and the procedure does not generate a file.  If `NULL` and the `file_name` parameter is non- `NULL`, then the procedure raises an error. |
| `revoke_optional_privileges` | A comma-separated list of optional privileges to revoke from the grantee, such as the `DV_XSTREAM_ADMIN` and `DV_GOLDENGATE_ADMIN` privileges |
| `container` | If `CURRENT`, then revokes privileges from the grantee only in the container where the procedure is invoked. `CURRENT` can be specified while connected to the root or to a PDB.  If `ALL`, then revokes privileges from the grantee in all containers in the CDB. To specify `ALL`, the procedure must be invoked in the root.  If a container name, then revokes privileges from the grantee only in the specified container. To specify root, use `CDB$ROOT` while connected to the root. To specify a PDB, the procedure must be invoked in the root.  Note: This parameter only applies to CDBs. |

Usage Notes

The user who runs this procedure must be an administrative user who can revoke privileges from other users. Specifically, this procedure revokes the privileges granted by running the `GRANT_ADMIN_PRIVILEGE` procedure in this package.

Note:

To view all of the statements run by this procedure in detail, you can use the procedure to generate a script and then view the script in a text editor.

See Also:

- " GRANT\_ADMIN\_PRIVILEGE Procedure "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF01207) for information about the `CREATE` `DIRECTORY` SQL statement

#### 222.3.4 REVOKE\_REMOTE\_ADMIN\_ACCESS Procedure

This procedure disables a remote XStream administrator from performing administrative actions by connecting to the grantee using a database link.

Note:

The `REVOKE_ADMIN_PRIVILEGE` procedure in this package runs this procedure.

See Also:

" REVOKE\_ADMIN\_PRIVILEGE Procedure "

Syntax

```
DBMS_XSTREAM_AUTH.REVOKE_REMOTE_ADMIN_ACCESS(
   grantee  IN  VARCHAR2);
```

Parameters

Table 222-5 REVOKE\_REMOTE\_ADMIN\_ACCESS Procedure Parameter

| Parameter | Description |
| --- | --- |
| `grantee` | The user for whom access from a remote XStream administrator is disabled.  If a row for the grantee exists in the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view, then the procedure updates the `ACCESS_FROM_REMOTE` column for the grantee to `NO`. If, after this update, both the `LOCAL_PRIVILEGES` column and the `ACCESS_FROM_REMOTE` column are `NO` for the grantee, then the procedure removes the grantee from the view.  If no row for the grantee exists in the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view, then the procedure does not update the view and does not raise an error. |