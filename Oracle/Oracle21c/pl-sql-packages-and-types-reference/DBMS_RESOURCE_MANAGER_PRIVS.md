---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_RESOURCE_MANAGER_PRIVS.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 149 DBMS\_RESOURCE\_MANAGER\_PRIVS

The `DBMS_RESOURCE_MANAGER_PRIVS` package maintains privileges associated with the Resource Manager.

This chapter contains the following topics:

- Summary of DBMS\_RESOURCE\_MANAGER\_PRIVS Subprograms

See Also:

For more information on using the Database Resource Manager, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-EA8CC987-EF18-4434-B962-01312CD3A8AC)

### 149.1 Summary of DBMS\_RESOURCE\_MANAGER\_PRIVS Subprograms

This table lists the `DBMS_RESOURCE_MANAGER_PRIVS` subprograms and briefly describes them.

Table 149-1 DBMS\_RESOURCE\_MANAGER\_PRIVS Package Subprograms

| Subprogram | Description |
| --- | --- |
| GRANT\_SWITCH\_CONSUMER\_GROUP Procedure | Grants the privilege to switch to resource consumer groups |
| GRANT\_SYSTEM\_PRIVILEGE Procedure | Performs a grant of a system privilege |
| REVOKE\_SWITCH\_CONSUMER\_GROUP Procedure | Revokes the privilege to switch to resource consumer groups. |
| REVOKE\_SYSTEM\_PRIVILEGE Procedure | Performs a revoke of a system privilege |

#### 149.1.1 GRANT\_SWITCH\_CONSUMER\_GROUP Procedure

This procedure grants the privilege to switch to a resource consumer group.

Syntax

```
DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP (
   grantee_name   IN VARCHAR2, 
   consumer_group IN VARCHAR2, 
   grant_option   IN BOOLEAN);
```

Parameters

Table 149-2 GRANT\_SWITCH\_CONSUMER\_GROUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `grantee_name` | Name of the user or role to whom privilege is to be granted. |
| `consumer_group` | Name of consumer group. |
| `grant_option` | `TRUE` if grantee should be allowed to grant access, `FALSE` otherwise. |

Usage Notes

If you grant permission to switch to a particular consumer group to a user, then that user can immediately switch their current consumer group to the new consumer group.

If you grant permission to switch to a particular consumer group to a role, then any users who have been granted that role and have enabled that role can immediately switch their current consumer group to the new consumer group.

If you grant permission to switch to a particular consumer group to `PUBLIC`, then any user can switch to that consumer group.

If the `grant_option` parameter is `TRUE`, then users granted switch privilege for the consumer group may also grant switch privileges for that consumer group to others.

In order to set the initial consumer group of a user, you must grant the switch privilege for that group to the user.

See Also:

[DBMS\_RESOURCE\_MANAGER](DBMS_RESOURCE_MANAGER.md)

Examples

```
BEGIN 
DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP ( 
 'scott', 'mail_maintenance_group', true); 
DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA(); 
DBMS_RESOURCE_MANAGER.set_consumer_group_mapping( 
  dbms_resource_manager.oracle_user, 'scott','mail_maintenance_group'); 
DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA(); 
END; 
/
```

#### 149.1.2 GRANT\_SYSTEM\_PRIVILEGE Procedure

This procedure performs a grant of a system privilege to a user or role.

Syntax

```
DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE (
   grantee_name    IN VARCHAR2, 
   privilege_name  IN VARCHAR2 DEFAULT 'ADMINISTER_RESOURCE_MANAGER',             
   admin_option    IN BOOLEAN);
```

Parameters

Table 149-3 GRANT\_SYSTEM\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `grantee_name` | Name of the user or role to whom privilege is to be granted. |
| `privilege_name` | Name of the privilege to be granted. |
| `admin_option` | `TRUE` if the grant is with `admin_option`, `FALSE` otherwise. |

Usage Notes

Currently, Oracle provides only one system privilege for the Resource Manager: `ADMINISTER_RESOURCE_MANAGER`. Database administrators have this system privilege with the `ADMIN` option. The grantee and the revokee can either be a user or a role. Users that have been granted the system privilege with the `ADMIN` option can also grant this privilege to others.

Examples

The following call grants this privilege to a user called `scott` without the `ADMIN` option:

```
BEGIN
DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE (
 grantee_name => 'scott',
 privilege_name => 'ADMINISTER_RESOURCE_MANAGER',
 admin_option => FALSE);
END;
/
```

#### 149.1.3 REVOKE\_SWITCH\_CONSUMER\_GROUP Procedure

This procedure revokes the privilege to switch to a resource consumer group.

Syntax

```
DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP (
   revokee_name   IN VARCHAR2, 
   consumer_group IN VARCHAR2);
```

Parameters

Table 149-4 REVOKE\_SWITCH\_CONSUMER\_GROUP Procedure Parameter

| Parameter | Description |
| --- | --- |
| `revokee_name` | Name of user/role from which to revoke access. |
| `consumer_group` | Name of consumer group. |

Usage Notes

If you revoke a user's switch privilege for a particular consumer group, then any subsequent attempts by that user to switch to that consumer group will fail.

If you revoke the initial consumer group from a user, then that user will automatically be part of the `DEFAULT_CONSUMER_GROUP` consumer group when logging in.

If you revoke the switch privilege for a consumer group from a role, then any users who only had switch privilege for the consumer group through that role will not be able to switch to that consumer group.

If you revoke the switch privilege for a consumer group from `PUBLIC`, then any users who could previously only use the consumer group through `PUBLIC` will not be able to switch to that consumer group.

Examples

The following example revokes the privileges to switch to `mail_maintenance_group` from Scott:

```
BEGIN
DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP (
 'scott', 'mail_maintenance_group');
END;
/
```

#### 149.1.4 REVOKE\_SYSTEM\_PRIVILEGE Procedure

This procedure performs a revoke of a system privilege from a user or role.

Syntax

```
DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE (
   revokee_name   IN VARCHAR2, 
   privilege_name IN VARCHAR2 DEFAULT 'ADMINISTER_RESOURCE_MANAGER');
```

Parameters

Table 149-5 REVOKE\_SYSTEM\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `revokee_name` | Name of the user or role from whom privilege is to be revoked. |
| `privilege_name` | Name of the privilege to be revoked. |

Examples

The following call revokes the `ADMINISTER_RESOURCE_MANAGER` from user scott:

```
BEGIN
DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SYSTEM_PRIVILEGE ('scott');
END;
/
```