---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_GOLDENGATE_AUTH.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 83 DBMS\_GOLDENGATE\_AUTH

The `DBMS_GOLDENGATE_AUTH` package provides subprograms for granting privileges to and revoking privileges from GoldenGate administrators.

This chapter contains the following topics:

See Also:

[GRANT\_ADMIN\_PRIVILEGE Procedure](DBMS_XSTREAM_AUTH.md) in the [DBMS\_XSTREAM\_AUTH](DBMS_XSTREAM_AUTH.md) package

### 83.1 DBMS\_GOLDENGATE\_AUTH Overview

This package provides subprograms for granting privileges to GoldenGate administrators and revoking privileges from GoldenGate administrators. A GoldenGate administrator manages an integrated GoldenGate and XStream Out configuration.

GoldenGate administrators can be used in a multitenant container database (CDB). A CDB is an Oracle database that includes zero, one, or many user-created pluggable databases (PDBs).

### 83.2 DBMS\_GOLDENGATE\_AUTH Security Model

Security on this package can be controlled by granting `EXECUTE` on this package to selected users or roles, or by granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

The user executing the subprograms in the `DBMS_GOLDENGATE_AUTH` package must have `SYSDBA` administrative privilege, and the user must exercise the privilege using `AS SYSDBA` at connect time.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

To ensure that the user who runs the subprograms in this package has the necessary privileges, connect as an administrative user who can create users, grant privileges, and create tablespaces when using this package.

### 83.3 Summary of DBMS\_GOLDENGATE\_AUTH Subprograms

The DBMS\_XSTREAM\_AUTH package includes the GRANT\_ADMIN\_PRIVILEGE procedure and REVOKE\_ADMIN\_PRIVILEGE procedure subprograms.

Table 83-1 DBMS\_GOLDENGATE\_AUTH Package Subprograms

| Subprogram | Description |
| --- | --- |
| GRANT\_ADMIN\_PRIVILEGE Procedure | Either grants the privileges needed by a user to be a GoldenGate administrator directly, or generates a script that grants these privileges |
| REVOKE\_ADMIN\_PRIVILEGE Procedure | Either revokes GoldenGate administrator privileges from a user directly, or generates a script that revokes these privileges |

Note:

All subprograms commit unless specified otherwise.

#### 83.3.1 GRANT\_ADMIN\_PRIVILEGE Procedure

This procedure grants the privileges needed by a user to be a GoldenGate administrator.

See Also:

[GRANT\_ADMIN\_PRIVILEGE Procedure](DBMS_XSTREAM_AUTH.md) in the [DBMS\_XSTREAM\_AUTH](DBMS_XSTREAM_AUTH.md) package

Syntax

```
DBMS_GOLDENGATE_AUTH.GRANT_ADMIN_PRIVILEGE(
   grantee                    IN  VARCHAR2,
   privilege_type             IN  VARCHAR2  DEFAULT '*',
   grant_select_privileges    IN  BOOLEAN   DEFAULT TRUE,
   do_grants                  IN  BOOLEAN   DEFAULT TRUE,
   file_name                  IN  VARCHAR2  DEFAULT NULL,
   directory_name             IN  VARCHAR2  DEFAULT NULL
   grant_optional_privileges  IN  VARCHAR2  DEFAULT NULL,
   container                  IN  VARCHAR2  DEFAULT 'CURRENT');
```

Parameters

Table 83-2 GRANT\_ADMIN\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `grantee` | The user to whom privileges are granted |
| `privilege_type` | Specify one of the following values:  - `CAPTURE` 	Specifying `CAPTURE` grants the minimum privileges required by the user to administer Oracle GoldenGate integrated extract. - `APPLY` 	Specifying `APPLY` grants the minimum privileges required by the user to administer Oracle GoldenGate integrated replicat. - `*` 	Specifying `*` grants the minimum privileges required by the user to administer Oracle GoldenGate integrated extract and Oracle GoldenGate integrated replicat. |
| `grant_select_privileges` | If `TRUE`, then the procedure grants a set of privileges, including `SELECT_CATALOG_ROLE`, to the user. This setting is recommended for GoldenGate administrators.  If `FALSE`, then the procedure does not grant the set of privileges to the user.  `SELECT_CATALOG_ROLE` enables the user to select from the data dictionary. |
| `do_grants` | If `TRUE`, then the procedure grants the privileges to the specified grantee directly, and adds the grantee to the `DBA_GOLDENGATE_PRIVILEGES` data dictionary view. If the user already has an entry in this data dictionary view, then the procedure does not make another entry, and no error is raised. If `TRUE` and any of the grant statements fails, then the procedure raises an error.  If `FALSE`, then the procedure does not grant the privileges to the specified grantee directly, and does not add the grantee to the `DBA_GOLDENGATE_PRIVILEGES` data dictionary view. You specify `FALSE` when the procedure is generating a file that you will run later. If you specify `FALSE` and either the `file_name` or `directory_name` parameter is `NULL`, then the procedure raises an error.  Note: It is recommended that `do_grants` be set to `TRUE` because many APIs check for the presence of a user in the `DBA_GOLDENGATE_PRIVILEGES` view, which will not be populated if `do_grants` is set to `FALSE`. |
| `file_name` | The name of the file generated by the procedure. The file contains all of the statements that grant the privileges. If a file with the specified file name exists in the specified directory name, then the grant statements are appended to the existing file.  If `NULL`, then the procedure does not generate a file. |
| `directory_name` | The directory into which the generated file is placed. The specified directory must be a directory object created using the SQL statement `CREATE` `DIRECTORY`. If you specify a directory, then the user who invokes the procedure must have the `WRITE` privilege on the directory object.  If `t` he `file_name` parameter is `NULL`, then this parameter is ignored, and the procedure does not generate a file.  If `NULL` and the `file_name` parameter is non- `NULL`, then the procedure raises an error. |
| `grant_optional_privileges` | A comma-separated list of optional privileges to grant to the grantee. You can specify the following roles and privileges:  - `XDBADMIN` - `DV_XSTREAM_ADMIN` - `DV_GOLDENGATE_ADMIN` - `EXEMPT_ACCESS_POLICY` - `EXEMPT_REDACTION_POLICY` |
| `container` | If `CURRENT`, then grants privileges to the grantee only in the container where the procedure is invoked. `CURRENT` can be specified while connected to the root or to a PDB.  If `ALL`, then grants privileges to the grantee in all containers in the CDB and all PDBs created after the procedure is invoked. To specify `ALL`, the procedure must be invoked in the root by a common user.  If a container name, then grants privileges to the grantee only in the specified container. To specify root, use `CDB$ROOT` while connected to the root. To specify a PDB, the procedure must be invoked in the root.  Note: This parameter only applies to CDBs. |

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
- `SELECT` or `READ` privilege on data dictionary views related to GoldenGate and Oracle Replication
- The ability to allow a remote GoldenGate administrator to perform administrative actions through a database link by connecting to the grantee
	This ability is enabled by running the `GRANT_REMOTE_ADMIN_ACCESS` procedure in this package.
	Note:
	This procedure grants only the privileges necessary to configure and administer a GoldenGate environment. You can grant additional privileges to the grantee if necessary.
	See Also:
	[GRANT\_ADMIN\_PRIVILEGE Procedure](DBMS_XSTREAM_AUTH.md) in the [DBMS\_XSTREAM\_AUTH](DBMS_XSTREAM_AUTH.md) package

#### 83.3.2 REVOKE\_ADMIN\_PRIVILEGE Procedure

This procedure revokes GoldenGate administrator privileges from a user.

Syntax

```
DBMS_GOLDENGATE_AUTH.REVOKE_ADMIN_PRIVILEGE(
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

Table 83-3 REVOKE\_ADMIN\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `grantee` | The user from whom privileges are revoked |
| `privilege_type` | Specify one of the following values:  - `CAPTURE` 	Specifying `CAPTURE` revokes the minimum privileges required by the user to administer Oracle GoldenGate integrated extract. - `APPLY` 	Specifying `APPLY` revokes the minimum privileges required by the user to administer Oracle GoldenGate integrated replicat. - `*` 	Specifying `*` revokes the minimum privileges required by the user to administer Oracle GoldenGate integrated extract and Oracle GoldenGate integrated replicat. |
| `revoke_select_privileges` | If `TRUE`, then the procedure revokes `SELECT_CATALOG_ROLE` from the user.  If `FALSE`, then the procedure does not revoke `SELECT_CATALOG_ROLE` to the user.  `SELECT_CATALOG_ROLE` enables the user to select from the data dictionary. |
| `do_revokes` | If `TRUE`, then the procedure revokes the privileges from the specified user directly, and removes the user from the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view. If the user does not have a record in this data dictionary view, then the procedure does not remove a record from the view, and no error is raised. If `TRUE` and any of the revoke statements fails, then the procedure raises an error. A revoke statement fails if the user is not granted the privilege that is being revoked.  If `FALSE`, then the procedure does not revoke the privileges from the specified user directly, and does not remove the user from the `DBA_XSTREAM_ADMINISTRATOR` data dictionary view.  You specify `FALSE` when the procedure is generating a file that you will run later. If you specify `FALSE` and either the `file_name` or `directory_name` parameter is `NULL`, then the procedure does not raise an error. |
| `file_name` | The name of the file generated by this procedure. The file contains all of the statements that revoke the privileges. If a file with the specified file name exists in the specified directory name, then the revoke statements are appended to the existing file.  If `NULL`, then the procedure does not generate a file. |
| `directory_name` | The directory into which the generated file is placed. The specified directory must be a directory object created using the SQL statement `CREATE` `DIRECTORY`. If you specify a directory, then the user who invokes the procedure must have the `WRITE` privilege on the directory object.  If the `file_name` parameter is `NULL`, then this parameter is ignored, and the procedure does not generate a file.  If `NULL` and the `file_name` parameter is non- `NULL`, then the procedure raises an error. |
| `revoke_optional_privileges` | A comma-separated list of optional privileges to revoke from the grantee, such as the `DV_XSTREAM_ADMIN` and `DV_GOLDENGATE_ADMIN` privileges |
| `container` | If `CURRENT`, then revokes privileges from the grantee only in the container where the procedure is invoked. `CURRENT` can be specified while connected to the root or to a PDB.  If `ALL`, then revokes privileges from the grantee in all containers in the CDB. To specify `ALL`, the procedure must be invoked in the root.  If a container name, then revokes privileges from the grantee only in the specified container. To specify root, use `CDB$ROOT` while connected to the root. To specify a PDB, the procedure must be invoked in the root.  Note: This parameter only applies to CDBs. |

Usage Notes

The user who runs this procedure must be an administrative user who can revoke privileges from other users. Specifically, this procedure revokes the privileges granted by running the `GRANT_ADMIN_PRIVILEGE` procedure in this package.

See Also:

" GRANT\_ADMIN\_PRIVILEGE Procedure "