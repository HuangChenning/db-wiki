---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/configure-aces-user-role-use-dbms_cloud.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.6.2 Configure ACEs for a User or Role to Use DBMS\_CLOUD

To provide all the functionality of `DBMS_CLOUD` to a user or role, you must enable the appropriate Access Control Entries (ACEs).

The `DBMS_CLOUD` family of packages have the `INVOKER` right privilege. For that reason, it is necessary to enable the appropriate access control entries (ACEs) to enable a user or role to obtain all the functionality of the `DBMS_CLOUD` family of packages. These ACEs are similar to the ones for `DBMS_CLOUD`.

To facilitate the management of these privileges for multiple users, Oracle recommends that you grant the necessary privileges through a role.

Example 20-4 Granting Access Privileges Using a Role

This example script shows the commands necessary to enable DBMS\_CLOUD functionality. Wrap these commands into a SQL script and run the script either in the CDB, PDB or non-CDB as `SYS` where you want to provide DBMS\_CLOUD functionality to your user or role.

The example script uses a local role, `CLOUD_USER`, and grants privileges to a local user, `SCOTT`. You can modify this script as needed for your PDB or non-CDB environment. Run the script as a privileged administrator within your database (for example, `SYS` or `SYSTEM`)

```
@$ORACLE_HOME/rdbms/admin/sqlsessstart.sql
 
-- target sample roledefine cloudrole=CLOUD_USER
 
-- CUSTOMER SPECIFIC SETUP, NEEDS TO BE PROVIDED BY THE CUSTOMER
-- - SSL Wallet directory
define sslwalletdir=<Set SSL Wallet Directory>
 
---- UNCOMMENT AND SET THE PROXY SETTINGS VARIABLES IF YOUR ENVIRONMENT NEEDS PROXYS
--
-- define proxy_uri=<your proxy URI address>
-- define proxy_host=<your proxy DNS name>
-- define proxy_low_port=<your_proxy_low_port>
-- define proxy_high_port=<your_proxy_high_port>
 
-- Create New ACL / ACEs
begin
-- Allow all hosts for HTTP/HTTP_PROXY
    dbms_network_acl_admin.append_host_ace(
        host =>'*',
        lower_port => 443,
        upper_port => 443,
        ace => xs$ace_type(
            privilege_list => xs$name_list('http', 'http_proxy'),
            principal_name => upper('&cloudrole'),
            principal_type => xs_acl.ptype_db));
 
--
-- UNCOMMENT THE PROXY SETTINGS SECTION IF YOUR ENVIRONMENT NEEDS PROXYS
--
-- Allow Proxy for HTTP/HTTP_PROXY
-- dbms_network_acl_admin.append_host_ace(
-- host =>'&proxy_host',
-- lower_port => &proxy_low_port,
-- upper_port => &proxy_high_port,
-- ace => xs$ace_type(
-- privilege_list => xs$name_list('http', 'http_proxy'),
-- principal_name => upper('&cloudrole'),
-- principal_type => xs_acl.ptype_db));
--
-- END PROXY SECTION
--
 
-- Allow wallet access
    dbms_network_acl_admin.append_wallet_ace(
        wallet_path => 'file:&sslwalletdir',
        ace => xs$ace_type(
            privilege_list =>xs$name_list('use_client_certificates', 'use_passwords'),
            principal_name => upper('&cloudrole'),
            principal_type => xs_acl.ptype_db));
end;
/
 
@$ORACLE_HOME/rdbms/admin/sqlsessend.sql
```

Example 20-5 Granting Access Privileges to an Individual User

In this example script, we assume local user `SCOTT` has been created with `DBMS_CLOUD` privileges, as shown previously, and you are now granting access privileges to that user. You can modify this script as needed for your PDB or non-CDB environment.

```
@$ORACLE_HOME/rdbms/admin/sqlsessstart.sql
 
-- target sample user
define clouduser=SCOTT
 
-- CUSTOMER SPECIFIC SETUP, NEEDS TO BE PROVIDED BY THE CUSTOMER
-- - SSL Wallet directory
define sslwalletdir=<Set SSL Wallet Directory>
 
-- Proxy definition
-- define proxy_uri=<your proxy URI address>
-- define proxy_host=<your proxy DNS name>
-- define proxy_low_port=<your_proxy_low_port>
-- define proxy_high_port=<your_proxy_high_port>
 
-- Create New ACL / ACEs
begin
-- Allow all hosts for HTTP/HTTP_PROXY
    dbms_network_acl_admin.append_host_ace(
        host =>'*',
        lower_port => 443,
        upper_port => 443,
        ace => xs$ace_type(
            privilege_list => xs$name_list('http', 'http_proxy'),
            principal_name => upper('&clouduser'),
            principal_type => xs_acl.ptype_db));
 
--
-- UNCOMMENT THE PROXY SETTINGS SECTION IF YOUR ENVIRONMENT NEEDS PROXYS
--
-- Allow Proxy for HTTP/HTTP_PROXY
-- dbms_network_acl_admin.append_host_ace(
-- host =>'&proxy_host',
-- lower_port => &proxy_low_port,
-- upper_port => &proxy_high_port,
-- ace => xs$ace_type(
-- privilege_list => xs$name_list('http', 'http_proxy'),
-- principal_name => upper('&clouduser'),
-- principal_type => xs_acl.ptype_db));
--
-- END PROXY SECTION
--
 
-- Allow wallet access
    dbms_network_acl_admin.append_wallet_ace(
        wallet_path => 'file:&sslwalletdir',
        ace => xs$ace_type(
            privilege_list =>xs$name_list('use_client_certificates', 'use_passwords'),
            principal_name => upper('&clouduser'),
            principal_type => xs_acl.ptype_db));
end;
/
 
@$ORACLE_HOME/rdbms/admin/sqlsessend.sql
```

After you run the access privileges scripts, your user or role previously granted minimal `DBMS_CLOUD` privileges is now properly configured and enabled to use the `DBMS_CLOUD` family packages.

**Parent topic:** [Configuring Users or Roles to use DBMS\_CLOUD](configuring-users-roles-use-dbms_cloud.md)