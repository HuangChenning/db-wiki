---
title: "What to Expect After You Install Oracle Database Vault"
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/dv_impact.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 2 What to Expect After You Install Oracle Database Vault

This chapter contains:

See Also:

[Appendix D, "Oracle Database Vault Security Guidelines,"](guidelines.md) for guidelines on managing security in the Oracle Database configuration

## Initialization and Password Parameter Settings That Change

When you install Oracle Database Vault, the installation process modifies several database initialization parameter settings to better secure your database configuration. If these changes adversely affect your organizational processes or database maintenance procedures, then contact Oracle Support for help in resolving the issue.

Table 2-1 describes the initialization parameter settings that Oracle Database Vault modifies. Initialization parameters are stored in the `init.ora` initialization parameter file, located in `$ORACLE_HOME/srvm/admin`. For more information about this file, see [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm).

Table 2-1 Modified Database Initialization Parameter Settings

| Parameter | Default Value in Database | New Value Set by Database Vault | Impact of the Change |
| --- | --- | --- | --- |
| `AUDIT_SYS_OPERATIONS` | `FALSE` | `TRUE` | Enables the auditing of top-level operations directly issued by user `SYS`, and users connecting with `SYSDBA` or `SYSOPER` privilege.  For more information about `AUDIT_SYS_OPERATIONS`, see [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams015.htm#REFRN10005). |
| `OS_ROLES` | Not configured. | `FALSE` | Disables the operating system to completely manage the granting and revoking of roles to users. Any previous grants of roles to users using `GRANT` statements do not change, because they are still listed in the data dictionary. Only the role grants made at the operating system-level to users apply. Users can still grant privileges to roles and users.  For more information about `OS_ROLES`, see [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm). |
| `RECYCLEBIN` | `ON` | `OFF` | Controls whether the Flashback Drop feature is turned on or off. If `RECYCLEBIN` is set to `OFF`, then dropped tables do not go into the recycle bin. If it is set to `ON`, then dropped tables go into the recycle bin, which means that they can be recovered.  See Also:  - ["Security Considerations for the Recycle Bin"](guidelines.md) - [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams208.htm#REFRN10264) for more information about `RECYCLEBIN` |
| `REMOTE_LOGIN_PASSWORDFILE` | `EXCLUSIVE` | `EXCLUSIVE` | Specifies whether Oracle Database checks for a password file. The `EXCLUSIVE` setting enforces the use of the password file, if you installed Oracle Database Vault into a database where `REMOTE_LOGIN_PASSWORDFILE` is not set to `EXCLUSIVE`.  For more information about `REMOTE_LOGIN_PASSWORDFILE`, see [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams212.htm#REFRN10184). |
| `SQL92_SECURITY` | `FALSE` | `TRUE` | Ensures that if a user has been granted the `UPDATE` and `DELETE` object privileges, then the user must also be granted the `SELECT` object privilege before being able to perform `UPDATE` or `DELETE` operations on tables that have `WHERE` or `SET` clauses.  For more information about `SQL92_SECURITY`, see [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm). |

## How Oracle Database Vault Restricts User Authorizations

During installation of Oracle Database Vault, the installer prompts for two additional database account names. In addition, several database roles are created. These accounts are part of the separation of duties provided by Oracle Database Vault. One common audit problem that has affected several large organizations is the unauthorized creation of new database accounts by a database administrator within a production instance. Upon installation, Oracle Database Vault prevents anyone other than the Oracle Database Vault account manager or a user granted the Oracle Database Vault account manager role from creating users in the database.

For guidelines on managing separation of duty, see ["Separation of Duty Guidelines"](guidelines.md).

## New Database Roles to Enforce Separation of Duties

To meet regulatory, privacy and other compliance requirements, Oracle Database Vault implements the concept of separation of duty. Oracle Database Vault makes clear separation between the account management responsibility, data security responsibility, and database resource management responsibility inside the database. This means that the concept of a super-privileged user (for example, `DBA`) is divided among several new database roles to ensure no one user has full control over both the data and configuration of the system. Oracle Database Vault prevents the `SYS` user and other accounts with the `DBA` role and other system privileges from designated protected areas of the database called realms. It also introduces new database roles called the Oracle Database Vault Owner (`DV_OWNER`) and the Oracle Database Vault Account Manager (`DV_ACCTMGR`). These new database roles separate the data security and the account management from the traditional `DBA` role. You should map these roles to distinct security professionals within your organization.

See Also:

- ["Separation of Duty Guidelines"](guidelines.md) for advice on managing separation of duty for your site
- ["Oracle Database Vault Roles"](db_objects.md) for detailed information about the roles created during the Oracle Database Vault installation
- ["Oracle Database Vault Accounts"](db_objects.md) for default accounts that are created and for suggestions of additional accounts that you may want to create

## Privileges That Are Revoked from Existing Users and Roles

When you install Oracle Database Vault, it revokes a set of privileges from several Oracle Database-supplied roles, as part of the separation of duty enhancement.

Table 2-2 lists privileges that Oracle Database Vault revokes from existing users and roles. Be aware that if you disable Oracle Database Vault, these privileges remain revoked. If your applications depend on these privileges, then grant them to application owner directly.

Table 2-2 Privileges Oracle Database Vault Revokes

| User or Role | Privilege That Is Revoked |
| --- | --- |
| `DBA` role | - `BECOME USER` - `SELECT ANY TRANSACTION` - `CREATE ANY JOB` - `CREATE EXTERNAL JOB` - `EXECUTE ANY PROGRAM` - `EXECUTE ANY CLASS` - `MANAGE SCHEDULER` - `DEQUEUE ANY QUEUE` - `ENQUEUE ANY QUEUE` - `MANAGE ANY QUEUE` |
| `IMP_FULL_DATABASE` role <sup>Foot 1</sup> | - `BECOME USER` - `MANAGE ANY QUEUE` |
| `EXECUTE_CATALOG_ROLE` role | - `EXECUTE ON DBMS_LOGMNR` - `EXECUTE ON DBMS_LOGMNR_D` - `EXECUTE ON DBMS_LOGMNR_LOGREP_DICT` - `EXECUTE ON DBMS_LOGMNR_SESSION` - `EXECUTE ON DBMS_FILE_TRANSFER` |
| `PUBLIC` user | - `EXECUTE ON UTL_FILE` |
| `SCHEDULER_ADMIN` role <sup>Foot 2</sup> | - `CREATE ANY JOB` - `CREATE EXTERNAL JOB` - `EXECUTE ANY PROGRAM` - `EXECUTE ANY CLASS` - `MANAGE SCHEDULER` |

<sup>Footnote 1</sup> To authorize users to export and import data using Oracle Data Pump, see ["Using Oracle Data Pump in an Oracle Database Vault Environment"](dba.md).

<sup>Footnote 2</sup> To authorize users to schedule database jobs, see ["Scheduling Database Jobs in an Oracle Database Vault Environment"](dba.md).

Note:

Both the `SYS` and `SYSTEM` users retain the `SELECT` privilege for the `DBA_USERS_WITH_DEFPWD` data dictionary view, which lists user accounts that use default passwords. If you want other users to have access to this view, grant them the `SELECT` privilege on it.

## Privileges That Are Prevented for Existing Users and Roles

The following privileges are prevented for all users and roles who have been granted these privileges, including users `SYS` and `SYSTEM`:

- `ALTER PROFILE`
- `ALTER USER` (but users can still use the `ALTER USER` statement to change their own passwords)
- `CREATE PROFILE`
- `CREATE USER`
- `DROP PROFILE`
- `DROP USER`

For better security and to maintain separation-of-duty standards, do not enable `SYS` or `SYSTEM` users the ability to create or manage user accounts.

## How Oracle Database Vault Affects Oracle Database Auditing

This section contains:

- AUD$ Table Moved from SYS to the SYSTEM Schema
- Modified AUDIT Statement Settings

### AUD$ Table Moved from SYS to the SYSTEM Schema

In an Oracle Database Vault environment, when Oracle Label Security is enabled, the `AUD$` table is moved from the `SYS` schema to the `SYSTEM` schema. The synonym `SYS.AUD$` is created to refer to the `SYSTEM.AUD$` table.

Tip:

For greater security, create a realm around the `SYSTEM.AUD$` and `SYS.FGA_LOG$` tables. See [Chapter 4, "Configuring Realms,"](cfrealms.md) for more information about realms.

### Modified AUDIT Statement Settings

When you install Oracle Database Vault, it configures several `AUDIT` statement settings in the database. See ["Oracle Database Audit Settings Created for Oracle Database Vault"](audplcy.md) for more information.