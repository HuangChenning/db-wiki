---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_CREDENTIAL.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 46 DBMS\_CREDENTIAL

The `DBMS_CREDENTIAL` package provides an interface for authenticating and impersonating `EXTPROC` callout functions, as well as external jobs, remote jobs and file watchers from the `SCHEDULER`.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN13373) regarding Specifying Job Credentials
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG656) regarding Guidelines for Securing External Processes

This chapter contains the following topics:

### 46.1 DBMS\_CREDENTIAL Overview

Credentials are database objects that hold a username/password pair for authenticating and impersonating `EXTPROC` callout functions, as well as remote jobs, external jobs and file watchers from the `SCHEDULER`.

They are created using the CREATE\_CREDENTIAL Procedure. The procedure also allows you to specify the Windows domain for remote external jobs executed against a Windows server.

### 46.2 DBMS\_CREDENTIAL Security Model

Every Oracle credential has a unique credential name and you can associate a credential through its unique credential name with `EXTPROC` by means of a PL/SQL alias library.

In order to associate a credential with a PL/SQL alias library and external procedure, you must have the `CREATE` `AND` `/` `OR` `REPLACE` `LIBRARY` privilege or `CREATE` `AND/OR` `REPLACE` `FUNCTION` `/` `PROCEDURE` privilege and read permission of the DLL or shared object that the alias library to be associated with so that you can create and/or replace function or procedure to make use of the alias library.

Once authenticated, `EXTPROC` must act on behalf of the client based on client's identity defined in the supplied user credential. If not authenticated, `EXTPROC` must return an error message.

In order to create or alter a credential, you must have the `CREATE` `CREDENTIAL` privilege. If you are attempting to create or alter a credential in a schema other than your own, you must have the `CREATE` `ANY` `CREDENTIAL` privilege.

### 46.3 DBMS\_CREDENTIAL Operational Notes

As the existing `CREATE OR REPLACE LIBRARY` statement and `CREATE OR REPLACE FUNCTION/PROCEDURE` do not support a `CREDENTIAL` clause, this model requires syntax and semantic changes in `CREATE OR REPLACE LIBRARY` and `CREATE OR REPLACE FUNCTION/PROCEDURE` statement.

For example:

```
CREATE OR REPLACE LIBRARY test 
  AS '$ORACLE_HOME/bin/test.so' CREDENTIAL ricky_cred;
CREATE OR REPLACE FUNCTION ftest1
  (x VARCHAR2, y BINARY_INTEGER)
RETURN BINARY_INTEGER
AS LANGUAGE C
LIBRARY test
NAME "negative"
PARAMETERS(x STRING, y INT);
```

The credential name defined in the `CREDENTIAL` clause is a name of a database object. Therefore, do not enclose the credential name with single or double quotes.

An example of a credential being used on an external job:

```
BEGIN
   DBMS_SCHEDULER.CREATE_JOB(
   job_name            => 'example_job',
   job_type            => 'EXECUTABLE',
   job_action          => '/bin/ls',
   credential_name     => 'ricky_cred');
END;
/
```

### 46.4 Summary of DBMS\_CREDENTIAL Subprograms

This table lists the `DBMS_CREDENTIAL` subprograms and briefly describes them.

Table 46-1 DBMS\_CREDENTIAL Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATE\_CREDENTIAL Procedure | Creates a stored username/password pair in a database object called an Oracle credential |
| DISABLE\_CREDENTIAL Procedure | Disables an Oracle credential |
| DROP\_CREDENTIAL Procedure | Drops an Oracle credential |
| ENABLE\_CREDENTIAL Procedure | Enables an Oracle credential |
| UPDATE\_CREDENTIAL Procedure | Updates an existing Oracle credential |

#### 46.4.1 CREATE\_CREDENTIAL Procedure

This procedure creates a stored username/password pair in a database object called an Oracle credential. You can also use this procedure to manage the credentials used for accessing files stored in cloud object storage.

Syntax

```
DBMS_CREDENTIAL.CREATE_CREDENTIAL (
   credential_name   IN  VARCHAR2,
   username          IN  VARCHAR2,
   password          IN  VARCHAR2,
   database_role     IN  VARCHAR2 DEFAULT NULL
   windows_domain    IN  VARCHAR2 DEFAULT NULL,
   comments          IN  VARCHAR2 DEFAULT NULL,
   enabled           IN  BOOLEAN DEFAULT TRUE);
```

Parameters

Table 46-2 CREATE\_CREDENTIAL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `credential_name` | Name of the credential. It can optionally be prefixed with a schema. This cannot be set to `NULL`. It is converted to upper case unless enclosed in double quotes. |
| `username` | User name to login to the operating system or remote database to run a job if this credential is chosen. This cannot be set to `NULL`. |
| `password` | Password to login to the remote operating system to run a job if this credential is chosen. It is case sensitive. |
| `database_role` | Whether a database job using this credential should attempt to log in with administrative privileges. Values: `SYSDBA`, `SYSDG`, `SYSADMIN` or `SYSBACKUP`. |
| `windows_domain` | For a Windows remote executable target, this is the domain that the specified user belongs to. The domain will be converted to uppercase automatically. |