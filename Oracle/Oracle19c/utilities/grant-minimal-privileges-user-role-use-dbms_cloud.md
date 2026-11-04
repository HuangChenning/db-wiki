---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/grant-minimal-privileges-user-role-use-dbms_cloud.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.6.1 Grant Minimal Privileges to a User or Role for DBMS\_CLOUD

For a user or role to use DBMS\_CLOUD functionality, you have to grant at least minimal access privileges.

The privileges shown in the examples that follows are required for a user or role to use `DBMS_CLOUD` functionality. To make the management of the necessary privileges easier for multiple users, Oracle recommends that you grant the necessary privileges through a role.

Example 20-2 Granting Privileges Using a Local Role

This example script uses a local role, `CLOUD_USER_ROLE`, and grants privileges to a local user, `SCOTT`. You can modify this script as needed for your PDB or non-CDB environment, and run the script within your pluggable database as a privileged administrator (for example, `SYS` or `SYSTEM`).

```
set verify off
 
-- target example role
define userrole='CLOUD_USER_ROLL'
 
-- target sample user
define username='SCOTT'
 
create role &userrole;
grant &userrole to &username;
 
REM the following are minimal privileges to use DBMS_CLOUD
REM - this script assumes core privileges
REM - CREATE SESSION
REM - Tablespace quota on the default tablespace for a user
 
REM for creation of external tables, e.g. DBMS_CLOUD.CREATE_EXTERNAL_TABLE()
grant CREATE TABLE to &userrole;
 
REM for using COPY_DATA()
REM - Any log and bad file information is written into this directory
grant read, write on directory DATA_PUMP_DIR to &userrole;
 
REM grant as you see fit
grant EXECUTE on dbms_cloud to &userrole;
grant EXECUTE on dbms_cloud_pipeline to &userrole;
grant EXECUTE on dbms_cloud_repo to &userrole;
grant EXECUTE on dbms_cloud_notification to &userrole;
```

Example 20-3 Granting Privileges to an Individual User

You can choose to grant DBMS\_CLOUD privileges to an individual user. In this example script, privileges are granted to local user `SCOTT`. You can modify this script as needed for your PDB or non-CDB environment.

```
set verify off
 
-- target sample user
define username='SCOTT'
 
REM the following are minimal privileges to use DBMS_CLOUD
REM - this script assumes core privileges
REM - CREATE SESSIONREM - Tablespace quota on the default tablespace for a user
 
REM for creation of external tables, e.g. DBMS_CLOUD.CREATE_EXTERNAL_TABLE()
grant CREATE TABLE to &username;
 
REM for using COPY_DATA()
REM - Any log and bad file information is written into this directory
grant read, write on directory DATA_PUMP_DIR to &username;
 
REM grant as you see fit
grant EXECUTE on dbms_cloud to &username;
grant EXECUTE on dbms_cloud_pipeline to &username;
grant EXECUTE on dbms_cloud_repo to &username;
grant EXECUTE on dbms_cloud_notification to &username;
```

**Parent topic:** [Configuring Users or Roles to use DBMS\_CLOUD](configuring-users-roles-use-dbms_cloud.md)