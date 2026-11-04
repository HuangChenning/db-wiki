---
title: Using the DBMS_MACADM Package
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/apis_dbms_macadm.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 12 Using the DBMS\_MACADM Package

This chapter contains:

## About the DBMS\_MACADM Package

The procedures and functions within the `DBMS_MACADM` package allow you to write applications that configure the realms, factors, rule sets, command rules, secure application roles, and Oracle Label Security policies normally configured in Oracle Database Vault Administrator.

The `DBMS_MACADM` package is available only for users who have been granted the `DV_ADMIN` or `DV_OWNER` role.

Many of the parameters used in the procedures and functions in the `DBMS_MACADM` package can use the constants available in the `DBMS_MACUTL` package. See ["DBMS\_MACUTL Constants"](apis_dbms_macutl.md) for more information.

Oracle Database Vault also provides a set of PL/SQL interfaces that you can use with the `DBMS_MACADM` package. See [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces,"](plsql_interfaces.md) for more information.

## Realm Procedures Within DBMS\_MACADM

Table 12-1 lists procedures within the `DBMS_MACADM` package that you can use to configure realms. For constants that you can use with these procedures, see [Table 14-1](apis_dbms_macutl.md) for more information.

[Chapter 4, "Configuring Realms,"](cfrealms.md) describes realms in detail. See also [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for a set of general purpose utility procedures that you can use with the realm procedures.

Table 12-1 DBMS\_MACADM Realm Configuration Procedures

| Procedure | Description |
| --- | --- |
| ADD\_AUTH\_TO\_REALM Procedure | Authorizes a user or role to access a realm as an owner or a participant |
| ADD\_OBJECT\_TO\_REALM Procedure | Registers a set of objects for realm protection |
| CREATE\_REALM Procedure | Creates a realm |
| DELETE\_AUTH\_FROM\_REALM Procedure | Removes the authorization of a user or role to access a realm |
| DELETE\_OBJECT\_FROM\_REALM Procedure | Removes a set of objects from realm protection |
| DELETE\_REALM Procedure | Deletes a realm |
| DELETE\_REALM\_CASCADE Procedure | Deletes a realm its related Database Vault configuration information |
| RENAME\_REALM Procedure | Renames a realm. The name change takes effect everywhere the realm is used. |
| UPDATE\_REALM Procedure | Updates a realm. |
| UPDATE\_REALM\_AUTH Procedure | Updates the authorization of a user or role to access a realm |

### ADD\_AUTH\_TO\_REALM Procedure

The `ADD_AUTH_TO_REALM` procedure authorizes a user or role to access a realm as an owner or a participant. For detailed information about realm authorization, see ["Defining Realm Authorization"](cfrealms.md).

Optionally, you can specify a rule set that must be checked before allowing the authorization to proceed.

Syntax

```
DBMS_MACADM.ADD_AUTH_TO_REALM(
  realm_name    IN VARCHAR2, 
  grantee       IN VARCHAR2, 
  rule_set_name IN VARCHAR2, 
  auth_options  IN NUMBER);
```

Parameters

Table 12-2 ADD\_AUTH\_TO\_REALM Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `grantee` | User or role name to authorize as an owner or a participant.  To find the existing users and roles in the current database instance, query the `DBA_USERS` and `DBA_ROLES` views, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm).  To find the authorization of a particular user or role, query the `DVA_DV_REALM_AUTH` view, described in ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md).  To find existing secure application roles used in privilege management, query the `DVSYS.DBA_DV_ROLE` view. Both are described in [Chapter 16, "Oracle Database Vault Data Dictionary Views."](views.md) |
| `rule_set_name` | Optional. Rule set to check before authorizing. If the rule set evaluates to `TRUE`, then the authorization is allowed.  To find the available rule sets, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `auth_options` | Optional. Specify one of the following options to authorize the realm:  - `DBMS_MACUTL.G_REALM_AUTH_PARTICIPANT`: Participant. This account or role provides system or direct privileges to access, manipulate, and create objects protected by the realm, provided these rights have been granted using the standard Oracle Database privilege grant process. - `DBMS_MACUTL.G_REALM_AUTH_OWNER`: Owner. This account or role has the same privileges as the realm participant, plus the authorization to grant or revoke realm-secured database roles. A realm can have multiple owners.  See ["Defining Realm Authorization"](cfrealms.md) for more information on participants and owners. |

Examples

The following example authorizes user `SYSADM` as a participant in the Performance Statistics Realm. Because the default is to authorize the user as a participant, the `auth_options` parameter can be omitted.

```
BEGIN
 DBMS_MACADM.ADD_AUTH_TO_REALM(
  realm_name  => 'Performance Statistics Realm', 
  grantee     => 'SYSADM'); 
END;
/
```

This example sets user `SYSADM` as the owner of the Performance Statistics Realm.

```
BEGIN
 DBMS_MACADM.ADD_AUTH_TO_REALM(
  realm_name   => 'Performance Statistics Realm', 
  grantee      => 'SYSADM', 
  auth_options => DBMS_MACUTL.G_REALM_AUTH_OWNER);
END;
/
```

The next example triggers the Check Conf Access rule set before allowing user `SYSADM` to be made the owner of the Performance Statistics Realm.

```
BEGIN
 DBMS_MACADM.ADD_AUTH_TO_REALM(
  realm_name    => 'Performance Statistics Realm', 
  grantee       => 'SYSADM', 
  rule_set_name => 'Check Conf Access',
  auth_options  => DBMS_MACUTL.G_REALM_AUTH_OWNER);
END;
/
```

### ADD\_OBJECT\_TO\_REALM Procedure

The `ADD_OBJECT_TO_REALM` procedure registers a set of objects for realm protection.

Syntax

```
DBMS_MACADM.ADD_OBJECT_TO_REALM(
  realm_name   IN VARCHAR2, 
  object_owner IN VARCHAR2, 
  object_name  IN VARCHAR2, 
  object_type  IN VARCHAR2);
```

Parameters

Table 12-3 ADD\_OBJECT\_TO\_REALM Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `object_owner` | The owner of the object that is being added to the realm. If you add a role to a realm, the object owner of the role is shown as `%` (for all), because roles do not have owners.  To find the available users, query the `DBA_USERS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5081.htm#REFRN23302).  To find the authorization of a particular user or role, query the `DVA_DV_REALM_AUTH` view, described in ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). |
| `object_name` | Object name. (The wildcard % is allowed. See "Object Name" under ["Creating Realm-Secured Objects"](cfrealms.md) for exceptions to the wildcard %.) You can also use the `DBMS_MACUTL.``G_ALL_OBJECT` constant.  To find the available objects, query the `ALL_OBJECTS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1158.htm#REFRN20146).  To find objects that are secured by existing realms, query the `DVSYS.DBA_DV_REALM_OBJECT` view, described in ["DVSYS.DBA\_DV\_REALM\_OBJECT View"](views.md). |
| `object_type` | Object type, such as `TABLE`, `INDEX`, or `ROLE`. (The wildcard % is allowed. See "Object Types" under ["Creating Realm-Secured Objects"](cfrealms.md) for exceptions to the wildcard %.)  You can also use the `DBMS_MACUTL.``G_ALL_OBJECT` constant. |

Example

```
BEGIN
 DBMS_MACADM.ADD_OBJECT_TO_REALM(
  realm_name   => 'Performance Statistics Realm', 
  object_owner => '%', 
  object_name  => 'GATHER_SYSTEM_STATISTICS', 
  object_type  => 'ROLE'); 
END;
/
```

### CREATE\_REALM Procedure

The `CREATE_REALM` procedure creates a realm. After you create the realm, use the following procedures to complete the realm definition:

- `ADD_OBJECT_TO_REALM` procedure registers one or more objects for the realm.
- `ADD_AUTH_TO_REALM` procedures authorize users or roles for the realm.

Syntax

```
DBMS_MACADM.CREATE_REALM(
  realm_name    IN VARCHAR2, 
  description   IN VARCHAR2, 
  enabled       IN VARCHAR2, 
  audit_options IN NUMBER);
```

Parameters

Table 12-4 CREATE\_REALM Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name, up to 90 characters in mixed-case.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `description` | Description of the purpose of the realm, up to 1024 characters in mixed-case. |
| `enabled` | `DBMS_MACUTL.G_YES` (Yes) enables realm checking; `DBMS_MACUTL.G_NO` (No) disables it. The default is `DBMS_MACUTL.G_YES`. |
| `audit_options` | Specify one of the following options to audit the realm:  - `DBMS_MACUTL.G_REALM_AUDIT_OFF`: Disables auditing for the realm (default) - `DBMS_MACUTL.G_REALM_AUDIT_FAIL`: Creates an audit record when a realm violation occurs (for example, when an unauthorized user tries to modify an object that is protected by the realm) - `DBMS_MACUTL.G_REALM_AUDIT_SUCCESS`: Creates an audit record for authorized activities on objects protected by the realm - `DBMS_MACUTL.G_REALM_AUDIT_FAIL + DBMS_MACUTL.G_REALM_AUDIT_SUCCESS`: Creates an audit record for both authorized and unauthorized activities on objects protected by the realm |

Example

```
BEGIN
 DBMS_MACADM.CREATE_REALM(
  realm_name    => 'Performance Statistics Realm', 
  description   => 'Realm to measure performance', 
  enabled       => DBMS_MACUTL.G_YES, 
  audit_options => DBMS_MACUTL.G_REALM_AUDIT_FAIL + DBMS_MACUTL.G_REALM_AUDIT_SUCCESS);
END; 
/
```

See Also:

[Example 14-1, "Creating a Realm Using DBMS\_MACUTL Constants"](apis_dbms_macutl.md)

### DELETE\_AUTH\_FROM\_REALM Procedure

The `DELETE_AUTH_FROM_REALM` procedure removes the authorization of a user or role to access a realm.

Syntax

```
DBMS_MACADM.DELETE_AUTH_FROM_REALM(
  realm_name IN VARCHAR2,
  grantee    IN VARCHAR2);
```

Parameters

Table 12-5 DELETE\_AUTH\_FROM\_REALM Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `grantee` | User or role name.  To find the authorization of a particular user or role, query the `DVA_DV_REALM_AUTH` view, described in ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.DELETE_AUTH_FROM_REALM(
  realm_name => 'Performance Statistics Realm',
  grantee    => 'SYS');
END;
/
```

### DELETE\_OBJECT\_FROM\_REALM Procedure

The `DELETE_OBJECT_FROM_REALM` procedure removes a set of objects from realm protection.

Syntax

```
DBMS_MACADM.DELETE_OBJECT_FROM_REALM(
  realm_name   IN VARCHAR2, 
  object_owner IN VARCHAR2, 
  object_name  IN VARCHAR2, 
  object_type  IN VARCHAR2);
```

Parameters

Table 12-6 DELETE\_OBJECT\_FROM\_REALM Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `object_owner` | The owner of the object that was added to the realm.  To find the available users, query the `DBA_USERS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). |
| `object_name` | Object name. (The wildcard % is allowed. See "Object Name" under ["Creating Realm-Secured Objects"](cfrealms.md) for exceptions to the wildcard %.) You can also use the `DBMS_MACUTL` `G_ALL_OBJECT` constant.  To find objects that are secured by existing realms, query the `DVSYS.DBA_DV_REALM_OBJECT` view, described in ["DVSYS.DBA\_DV\_REALM\_OBJECT View"](views.md). |
| `object_type` | Object type, such as `TABLE`, `INDEX`, or `ROLE`. (The wildcard % is allowed. See "Object Types" under ["Creating Realm-Secured Objects"](cfrealms.md) for exceptions to the wildcard %.)  You can also use the `DBMS_MACUTL` `G_ALL_OBJECT` constant. |

Example

```
BEGIN
 DBMS_MACADM.DELETE_OBJECT_FROM_REALM(
  realm_name   => 'Performance Statistics Realm', 
  object_owner => 'SYS', 
  object_name  => 'GATHER_SYSTEM_STATISTICS', 
  object_type  => 'ROLE'); 
END;
/
```

### DELETE\_REALM Procedure

The `DELETE_REALM` procedure deletes a realm but does not remove its associated objects and authorizations. Before you delete a realm, you can locate its associated objects by querying the `DVSYS.DBA_DV_REALM_OBJECT` view. To find a listing of the realm-related objects, query the `DVSYS.DBA_DV_REALM` view. To find its authorizations, query `DVSYS.DBA_DV_REALM_AUTH`. These views are described in [Chapter 16, "Oracle Database Vault Data Dictionary Views."](views.md)

If you want to remove the associated objects and authorizations and the realm, see "DELETE\_REALM\_CASCADE Procedure".

Syntax

```
DBMS_MACADM.DELETE_REALM(
  realm_name IN VARCHAR2);
```

Parameters

Table 12-7 DELETE\_REALM Parameter

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_REALM('Performance Statistics Realm');
```

### DELETE\_REALM\_CASCADE Procedure

The `DELETE_REALM_CASCADE` procedure deletes a realm, including its related Database Vault configuration information that specifies who is authorized (`DVSYS.DBA_DV_REALM_AUTH` view) and what objects are protected (`DVSYS.DBA_DV_REALM_OBJECT` view). It does not delete the actual database objects or users. To find a listing of the realm-related objects, query the `DVSYS.DBA_DV_REALM` view. To find its authorizations, query `DVSYS.DBA_DV_REALM_AUTH`. Both are described under [Chapter 16, "Oracle Database Vault Data Dictionary Views."](views.md)

Syntax

```
DBMS_MACADM.DELETE_REALM_CASCADE(
  realm_name IN VARCHAR2);
```

Parameters

Table 12-8 DELETE\_REALM\_CASCADE Parameter

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_REALM_CASCADE('Performance Statistics Realm');
```

### RENAME\_REALM Procedure

The `RENAME_REALM` procedure renames a realm. The name change takes effect everywhere the realm is used.

Syntax

```
DBMS_MACADM.RENAME_REALM(
  realm_name IN VARCHAR2, 
  new_name   IN VARCHAR2);
```

Parameters

Table 12-9 RENAME\_REALM Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Current realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `new_name` | New realm name, up to 90 characters in mixed-case. |

Example

```
BEGIN
 DBMS_MACADM.RENAME_REALM(
  realm_name => 'Performance Statistics Realm', 
  new_name   => 'Sector 2 Performance Statistics Realm');
END; 
/
```

### UPDATE\_REALM Procedure

The `UPDATE_REALM` procedure updates a realm.

Syntax

```
DBMS_MACADM.UPDATE_REALM(
  realm_name    IN VARCHAR2, 
  description   IN VARCHAR2, 
  enabled       IN VARCHAR2, 
  audit_options IN NUMBER DEFAULT NULL);
```

Parameters

Table 12-10 UPDATE\_REALM Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `description` | Description of the purpose of the realm, up to 1024 characters in mixed-case. |
| `enabled` | `DBMS_MACUTL.G_YES` (Yes) enables realm checking; `DBMS_MACUTL.G_NO` (No) disables it.  The default for `enabled` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_REALM` data dictionary view. |
| `audit_options` | Specify one of the following options to audit the realm:  - `DBMS_MACUTL.G_REALM_AUDIT_OFF`: Disables auditing for the realm - `DBMS_MACUTL.G_REALM_AUDIT_FAIL`: Creates an audit record when a realm violation occurs (for example, when an unauthorized user tries to modify an object that is protected by the realm - `DBMS_MACUTL.G_REALM_AUDIT_SUCCESS`: Creates an audit record for authorized activities on objects protected by the realm. - `DBMS_MACUTL.G_REALM_AUDIT_FAIL + DBMS_MACUTL.G_REALM_AUDIT_SUCCESS`: Creates an audit record for both authorized and unauthorized activities on objects protected by the realm  The default for `audit_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_REALM` data dictionary view. |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_REALM(
  realm_name    => 'Sector 2 Performance Statistics Realm', 
  description   => 'Realm to measure performance for Sector 2 applications', 
  enabled       => DBMS_MACUTL.G_YES, 
  audit_options => DBMS_MACUTL.G_REALM_AUDIT_FAIL + G_REALM_AUDIT_SUCCESS); 
END;
/
```

### UPDATE\_REALM\_AUTH Procedure

The `UPDATE_REALM_AUTH` procedure updates the authorization of a user or role to access a realm.

Syntax

```
DBMS_MACADM.UPDATE_REALM_AUTH(
  realm_name    IN VARCHAR2, 
  grantee       IN VARCHAR2, 
  rule_set_name IN VARCHAR2, 
  auth_options  IN NUMBER);
```

Parameters

Table 12-11 UPDATE\_REALM\_AUTH Parameters

| Parameter | Description |
| --- | --- |
| `realm_name` | Realm name.  To find the existing realms in the current database instance, query the `DVSYS.DBA_DV_REALM` view, described in ["DVSYS.DBA\_DV\_REALM View"](views.md). |
| `grantee` | User or role name.  To find the available users and roles, query the `DBA_USERS` and `DBA_ROLES` views, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm).  To find the authorization of a particular user or role, query the `DVA_DV_REALM_AUTH` view, described in ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md).  To find existing secure application roles used in privilege management, query the `DVSYS.DBA_DV_ROLE` view, described in ["DVSYS.DBA\_DV\_ROLE View"](views.md). |
| `rule_set_name` | Optional Rule set to check before authorizing. If the rule set evaluates to `TRUE`, then the authorization is allowed.  To find the available rule sets, query the `DVSYS.DBA_DV_RULE_SET` view. To find rules that are associated with the rule sets, query the `DBA_DB_RULE_SET_RULE` view. Both are described in [Chapter 16, "Oracle Database Vault Data Dictionary Views."](views.md) |
| `auth_options` | Optional. Specify one of the following options to authorize the realm:  - `DBMS_MACUTL.G_REALM_AUTH_PARTICIPANT`: Participant. This account or role provides system or direct privileges to access, manipulate, and create objects protected by the realm, provided these rights have been granted using the standard Oracle Database privilege grant process. - `DBMS_MACUTL.G_REALM_AUTH_OWNER`: Owner. This account or role has the same privileges as the realm participant, plus the authorization to grant or revoke realm-secured database roles. A realm can have multiple owners.  The default for `auth_options` value is the previously set value, which you can find by querying the `DVSYS.DBA_DV_REALM_AUTH` data dictionary view. |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_REALM_AUTH(
  realm_name    => 'Sector 2 Performance Statistics Realm', 
  grantee       => 'SYSADM', 
  rule_set_name => 'Check Conf Access', 
  auth_options  => DBMS_MACUTL.G_REALM_AUTH_OWNER);
END; 
/
```

## Rule Set Procedures Within DBMS\_MACADM

Table 12-12 lists procedures within the `DBMS_MACADM` package that you can use to configure rule sets.

See Also:

- [Chapter 5, "Configuring Rule Sets,"](cfrulset.md) for detailed information about rule sets
- [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for a set of general-purpose utility procedures that you can use with the rule set procedures
- [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces,"](plsql_interfaces.md) for PL/SQL interfaces that you can use with rules

Table 12-12 DBMS\_MACADM Rule Set Configuration Procedures

| Procedure | Description |
| --- | --- |
| ADD\_RULE\_TO\_RULE\_SET Procedure | Adds a rule to a rule set |
| CREATE\_RULE Procedure | Creates a rule |
| CREATE\_RULE\_SET Procedure | Creates a rule set |
| DELETE\_RULE Procedure | Deletes a rule |
| DELETE\_RULE\_FROM\_RULE\_SET Procedure | Deletes a rule from a rule set |
| DELETE\_RULE\_SET Procedure | Deletes a rule set |
| RENAME\_RULE Procedure | Renames a rule. The name change takes effect everywhere the rule is used. |
| RENAME\_RULE\_SET Procedure | Renames a rule set. The name change takes effect everywhere the rule set is used. |
| SYNC\_RULES Procedure | Synchronizes the rules |
| UPDATE\_RULE Procedure | Updates a rule |
| UPDATE\_RULE\_SET Procedure | Updates a rule set |

### ADD\_RULE\_TO\_RULE\_SET Procedure

The `ADD_RULE_TO_RULE_SET` procedure adds rule to a rule set, and lets you specify whether to have the rule be checked when the rule set is evaluated.

Syntax

```
DBMS_MACADM.ADD_RULE_TO_RULE_SET(
  rule_set_name  IN VARCHAR2, 
  rule_name      IN VARCHAR2, 
  rule_order     IN NUMBER, 
  enabled        IN VARCHAR2);
```

Parameters

Table 12-13 ADD\_RULE\_TO\_RULE\_SET Parameters

| Parameter | Description |
| --- | --- |
| `rule_set_name` | Rule set name.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `rule_name` | Rule to add to the rule set.  To find existing rules, query the `DVSYS.DBA_DV_RULE` view, described in ["DVSYS.DBA\_DV\_RULE View"](views.md).  To find rules that have been associated with rule sets, use `DVSYS.DBA_DV_RULE_SET_RULE`, described in ["DVSYS.DBA\_DV\_RULE\_SET\_RULE View"](views.md). |
| `rule_order` | Does not apply to this release, but you must include a value for the `ADD_RULE_TO_RULE_SET` procedure to work. Enter `1`. |
| `enabled` | Optional. Determines whether the rule should be checked when the rule set is evaluated. Possible values are:  - `Y` (yes; default). Enables the rule to be checked during the rule set evaluation. - `N` (no). Prevents the rule from being checked during the rule set evaluation.  You can also enter the following `DBMS_MACUTL` constants:  - `DBMS_MACUTL.G_YES` (default) - `DBMS_MACUTL.G_NO`  See [Table 14-1](apis_dbms_macutl.md) for more information. |

Examples

The following example adds a rule to a rule set, and by omitting the `enabled` parameter, automatically enables the rule to be checked when the rule set is evaluated.

```
BEGIN
 DBMS_MACADM.ADD_RULE_TO_RULE_SET(
  rule_set_name => 'Limit_DBA_Access', 
  rule_name     => 'Restrict DROP TABLE operations',
  rule_order    => 1);
END;
/
```

This example adds the rule to the rule set but disables rule checking.

```
BEGIN
 DBMS_MACADM.ADD_RULE_TO_RULE_SET(
  rule_set_name => 'Limit_DBA_Access',
  rule_name     => 'Check UPDATE operations',
  rule_order    => 1,
  enabled       => DBMS_MACUTL.G_NO);
END;
/
```

### CREATE\_RULE Procedure

The `CREATE_RULE` procedure creates a rule. After you create a rule, you can add it to a rule set.

Syntax

```
DBMS_MACADM.CREATE_RULE(
  rule_name  IN VARCHAR2, 
  rule_expr  IN VARCHAR2);
```

Parameters

Table 12-14 CREATE\_RULE Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | Rule name, up to 90 characters in mixed-case. Spaces are allowed.  To find existing rules in the current database instance, query the `DVSYS.DBA_DV_RULE` view, described in ["DVSYS.DBA\_DV\_RULE View"](views.md).  To find rules that have been associated with rule sets, query `DVSYS.DBA_DV_RULE_SET_RULE`, described in ["DVSYS.DBA\_DV\_RULE\_SET\_RULE View"](views.md). |
| `rule_expr` | PL/SQL `BOOLEAN` expression.  If the expression contains quotation marks, do not use double quotation marks. Instead, use two single quotation marks. Enclose the entire expression within single quotation marks. For example:  ``` 'TO_CHAR(SYSDATE,''HH24'') = ''12''' ```  See ["Creating a New Rule"](cfrulset.md) for more information on rule expressions. |

Example

```
BEGIN
 DBMS_MACADM.CREATE_RULE(
  rule_name  => 'Check UPDATE operations', 
  rule_expr  =>'SYS_CONTEXT(''USERENV'',''SESSION_USER'') = ''SYSADM''');
END;
/
```

### CREATE\_RULE\_SET Procedure

The `CREATE_RULE_SET` procedure creates a rule set. After you create a rule set, you can use the `CREATE_RULE` and `ADD_RULE_TO_RULE_SET` procedures to create and add rules to the rule set.

Syntax

```
DBMS_MACADM.CREATE_RULE_SET(
  rule_set_name    IN VARCHAR2, 
  description      IN VARCHAR2, 
  enabled          IN VARCHAR2, 
  eval_options     IN NUMBER, 
  audit_options    IN NUMBER, 
  fail_options     IN NUMBER, 
  fail_message     IN VARCHAR2, 
  fail_code        IN NUMBER, 
  handler_options  IN NUMBER, 
  handler          IN VARCHAR2,
  is_static        IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 12-15 CREATE\_RULE\_SET Parameters

| Parameter | Description |
| --- | --- |
| `rule_set_name` | Rule set name, up to 90 characters in mixed-case. Spaces are allowed.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `description` | Description of the purpose of the rule set, up to 1024 characters in mixed-case. |
| `enabled` | `DBMS_MACUTL.G_YES` (Yes) enables the rule set; `DBMS_MACUTL.G_NO` (No) disables it. The default is `Y`. |
| `eval_options` | If you plan to assign multiple rules to the rule set, enter one of the following settings:  - `DBMS_MACUTL.G_RULESET_EVAL_ALL`: All rules in the rule set must evaluate to true for the rule set itself to evaluate to true (default). - `DBMS_MACUTL.G_RULESET_EVAL_ANY`: At least one rule in the rule set must evaluate to true for the rule set itself to evaluate to true. |
| `audit_options` | Select one of the following settings:  - `DBMS_MACUTL.G_RULESET_AUDIT_OFF`: Disables auditing for the rule set (default) - `DBMS_MACUTL.G_RULESET_AUDIT_FAIL`: Creates an audit record when a rule set violation occurs - `DBMS_MACUTL.G_RULESET_AUDIT_SUCCESS`: Creates an audit record for a successful rule set evaluation - `DBMS_MACUTL.G_RULESET_AUDIT_FAIL + DBMS_MACUTL.G_RULESET_AUDIT_SUCCESS`: Creates an audit record for both successful and failed rule set evaluations  See ["Audit Options"](cfrulset.md) for more information. |
| `fail_options` | Options for reporting factor errors:  - `DBMS_MACUTL.G_RULESET_FAIL_SHOW`: Shows an error message (default) - `DBMS_MACUTL.G_RULESET_FAIL_SILENT`: Does not show an error message  See ["Error Handling Options"](cfrulset.md) for more information. |
| `fail_message` | Enter an error message for failure, up to 80 characters in mixed-case, to associate with the fail code you specify for `fail_code`. |
| `fail_code` | Enter a number in the range of -20000 to -20999 or 20000 to 20999 to associate with the `fail_message` parameter. |
| `handler_options` | Select one of the following settings:  - `DBMS_MACUTL.G_RULESET_HANDLER_OFF`: Disables error handling (default) - `DBMS_MACUTL.G_RULESET_HANDLER_FAIL`: Calls handler on rule set failure - `DBMS_MACUTL.G_RULESET_HANDLER_SUCCESS`: Calls handler on rule set success  See ["Error Handling Options"](cfrulset.md) for more information. |
| `handler` | Name of the PL/SQL function or procedure that defines the custom event handler logic.  See ["Error Handling Options"](cfrulset.md) for more information. |
| `is_static` | Optional. Determines how often a rule set is evaluated when it is accessed. The default is `FALSE`.  - `TRUE`: The rule set is evaluated once during the user session. After that, the value is re-used. - `FALSE`: The rule set evaluated every time. |

Example

```
BEGIN
 DBMS_MACADM.CREATE_RULE_SET(
  rule_set_name    => 'Limit_DBA_Access', 
  description      => 'DBA access through predefined processes', 
  enabled          => DBMS_MACUTL.G_YES,
  eval_options     => 2,
  audit_options    => DBMS_MACUTL.G_RULESET_AUDIT_FAIL + DBMS_MACUTL.G_RULESET_AUDIT_SUCCESS,
  fail_options     => DBMS_MACUTL.G_RULESET_FAIL_SILENT,
  fail_message     => '',
  fail_code        => 20461,
  handler_options  => DBMS_MACUTL.G_RULESET_HANDLER_FAIL, 
  handler          => 'dbavowner.email_alert',
  is_static        => TRUE);
END;
/
```

See Also:

[Example 14-2, "Creating a Rule Set Using DBMS\_MACUTL Constants"](apis_dbms_macutl.md)

### DELETE\_RULE Procedure

The `DELETE_RULE` procedure deletes a rule.

Syntax

```
DBMS_MACADM.DELETE_RULE(
  rule_name IN VARCHAR2);
```

Parameter

Table 12-16 DELETE\_RULE Parameter

| Parameter | Description |
| --- | --- |
| `rule_name` | Rule name.  To find existing rules in the current database instance, query the `DVSYS.DBA_DV_RULE` view, described in ["DVSYS.DBA\_DV\_RULE View"](views.md).  To find rules that have been associated with rule sets, query `DVSYS.DBA_DV_RULE_SET_RULE`, described in ["DVSYS.DBA\_DV\_RULE\_SET\_RULE View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_RULE('Check UPDATE operations');
```

### DELETE\_RULE\_FROM\_RULE\_SET Procedure

The `DELETE_RULE_FROM_RULE_SET` procedure deletes a rule from a rule set.

Syntax

```
DBMS_MACADM.DELETE_RULE_FROM_RULE_SET(
  rule_set_name IN VARCHAR2, 
  rule_name     IN VARCHAR2);
```

Parameters

Table 12-17 DELETE\_RULE\_FROM\_RULE\_SET Parameters

| Parameter | Description |
| --- | --- |
| `rule_set_name` | Rule set name.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `rule_name` | Rule to remove from the rule set.  To find existing rules in the current database instance, query the `DVSYS.DBA_DV_RULE` view, described in ["DVSYS.DBA\_DV\_RULE View"](views.md).  To find rules that have been associated with rule sets, query `DVSYS.DBA_DV_RULE_SET_RULE`, described in ["DVSYS.DBA\_DV\_RULE\_SET\_RULE View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.DELETE_RULE_FROM_RULE_SET(
  rule_set_name => 'Limit_DBA_Access', 
  rule_name     => 'Check UPDATE operations');
END;
/
```

### DELETE\_RULE\_SET Procedure

The `DELETE_RULE_SET` procedure deletes a rule set.

Syntax

```
DBMS_MACADM.DELETE_RULE_SET(
  rule_set_name IN VARCHAR2);
```

Parameters

Table 12-18 DELETE\_RULE\_SET Parameter

| Parameter | Description |
| --- | --- |
| `rule_set_name` | Rule set name.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_RULE_SET('Limit_DBA_Access');
```

### RENAME\_RULE Procedure

The `RENAME_RULE` procedure renames a rule. The name change takes effect everywhere the rule is used.

Syntax

```
DBMS_MACADM.RENAME_RULE(
  rule_name  IN VARCHAR2, 
  new_name   IN VARCHAR2);
```

Parameters

Table 12-19 RENAME\_RULE Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | Current rule name.  To find existing rules in the current database instance, query the `DVSYS.DBA_DV_RULE` view, described in ["DVSYS.DBA\_DV\_RULE View"](views.md).  To find rules that have been associated with rule sets, query `DVSYS.DBA_DV_RULE_SET_RULE`, described in ["DVSYS.DBA\_DV\_RULE\_SET\_RULE View"](views.md). |
| `new_name` | New rule name, up to 90 characters in mixed-case. |

Example

```
BEGIN
 DBMS_MACADM.RENAME_RULE(
  rule_name  => 'Check UPDATE operations', 
  new_name   => 'Check Sector 2 Processes');
END; 
/
```

### RENAME\_RULE\_SET Procedure

The `RENAME_RULE_SET` procedure renames a rule set. The name change takes effect everywhere the rule set is used.

Syntax

```
DBMS_MACADM.RENAME_RULE_SET(
  rule_set_name IN VARCHAR2, 
  new_name      IN VARCHAR2);
```

Parameters

Table 12-20 RENAME\_RULE\_SET Parameters

| Parameter | Description |
| --- | --- |
| `rule_set_name` | Current rule set name.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `new_name` | New rule set name, up to 90 characters in mixed-case. Spaces are allowed. |

Example

```
BEGIN
 DBMS_MACADM.RENAME_RULE_SET(
  rule_set_name => 'Limit_DBA_Access', 
  new_name      => 'Limit Sector 2 Access'); 
END;
/
```

### SYNC\_RULES Procedure

The `SYNC_RULES` procedure synchronizes the rules in Oracle Database Vault and Advanced Queuing Rules engine. You must perform this operation immediately after you roll back an `ADD_RULE_TO_RULESET`, a `DELETE_RULE`, or an `UPDATE_RULE` operation.

Syntax

```
DBMS_MACADM.SYNC_RULES();
```

Parameters

None.

Example

```
EXEC DBMS_MACADM.SYNC_RULES();
```

### UPDATE\_RULE Procedure

The `UPDATE_RULE` procedure updates a rule.

Syntax

```
DBMS_MACADM.UPDATE_RULE(
  rule_name  IN VARCHAR2, 
  rule_expr  IN VARCHAR2);
```

Parameters

Table 12-21 UPDATE\_RULE Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | Rule name.  To find existing rules in the current database instance, query the `DVSYS.DBA_DV_RULE` view, described in ["DVSYS.DBA\_DV\_RULE View"](views.md).  To find rules that have been associated with rule sets, query `DVSYS.DBA_DV_RULE_SET_RULE`, described in ["DVSYS.DBA\_DV\_RULE\_SET\_RULE View"](views.md). |
| `rule_expr` | PL/SQL `BOOLEAN` expression.  If the expression contains quotation marks, do not use double quotation marks. Instead, use two single quotation marks. Enclose the entire expression within single quotation marks. For example:  ``` 'TO_CHAR(SYSDATE,''HH24'') = ''12''' ```  See ["Creating a New Rule"](cfrulset.md) for more information on rule expressions.  To find existing rule expressions, query the `DVSYS.DBA_DV_RULE` view. |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_RULE(
  rule_name  => 'Check UPDATE operations', 
  rule_expr  =>'SYS_CONTEXT(''USERENV'',''SESSION_USER'') = ''SYSADM'' AND
               (
                 UPPER(SYS_CONTEXT(''USERENV'',''MODULE'')) LIKE ''APPSRVR%'' OR
                 UPPER(SYS_CONTEXT(''USERENV'',''MODULE'')) LIKE ''DBAPP%'' )'
               );
END;
/
```

### UPDATE\_RULE\_SET Procedure

The `UPDATE_RULE_SET` procedure updates a rule set.

Syntax

```
DBMS_MACADM.UPDATE_RULE_SET(
  rule_set_name    IN VARCHAR2,
  description      IN VARCHAR2, 
  enabled          IN VARCHAR2, 
  eval_options     IN NUMBER, 
  audit_options    IN NUMBER, 
  fail_options     IN NUMBER, 
  fail_message     IN VARCHAR2, 
  fail_code        IN NUMBER, 
  handler_options  IN NUMBER, 
  handler          IN VARCHAR2,
  is_static        IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 12-22 UPDATE\_RULE\_SET Parameters

| Parameter | Description |
| --- | --- |
| `rule_set_name` | Rule set name.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `description` | Description of the purpose of the rule set, up to 1024 characters in mixed-case. |
| `enabled` | `DBMS_MACUTL.G_YES` (Yes) enables rule set checking; `DBMS_MACUTL.G_NO` (No) disables it.  The default for the `enabled` setting is the previously set value, which you can find by querying the `DVSYS.DBA_DV_RULE_SET` data dictionary view. |
| `eval_options` | If you plan to assign multiple rules to the rule set, enter one of the following settings:  - `DBMS_MACUTL.G_RULESET_EVAL_ALL`: All rules in the rule set must evaluate to true for the rule set itself to evaluate to true. - `DBMS_MACUTL.G_RULESET_EVAL_ANY`: At least one rule in the rule set must evaluate to true for the rule set itself to evaluate to true.  The default for `eval_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_RULE_SET` data dictionary view. |
| `audit_options` | Select one of the following settings:  - `DBMS_MACUTL.G_RULESET_AUDIT_OFF`: Disables auditing for the rule set - `DBMS_MACUTL.G_RULESET_AUDIT_FAIL`: Creates an audit record when a rule set violation occurs - `DBMS_MACUTL.G_RULESET_AUDIT_SUCCESS`: Creates an audit record for a successful rule set evaluation - `DBMS_MACUTL.G_RULESET_AUDIT_FAIL + DBMS_MACUTL.G_RULESET_AUDIT_SUCCESS`: Creates an audit record for both successful and failed rule set evaluations  The default for `audit_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_RULE_SET` data dictionary view.  See ["Audit Options"](cfrulset.md) for more information. |
| `fail_options` | Options for reporting factor errors:  - `DBMS_MACUTL.G_RULESET_FAIL_SHOW`: Shows an error message. - `DBMS_MACUTL.G_RULESET_FAIL_SILENT`: Does not show an error message.  The default for `fail_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_RULE_SET` data dictionary view.  See ["Error Handling Options"](cfrulset.md) for more information. |
| `fail_message` | Error message for failure, up to 80 characters in mixed-case, to associate with the fail code you specify for `fail_code`. |
| `fail_code` | Enter a number in the range of -20000 to -20999 or 20000 to 20999 to associate with the `fail_message` parameter. |
| `handler_options` | Select one of the following settings:  - `DBMS_MACUTL.G_RULESET_HANDLER_OFF`: Disables error handling. - `DBMS_MACUTL.G_RULESET_HANDLER_FAIL`: Call handler on rule set failure. - `DBMS_MACUTL.G_RULESET_HANDLER_SUCCESS`: Call handler on rule set success.  The default for `handler_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_RULE_SET` data dictionary view.  See ["Error Handling Options"](cfrulset.md) for more information. |
| `handler` | Name of the PL/SQL function or procedure that defines the custom event handler logic.  See ["Error Handling Options"](cfrulset.md) for more information. |
| `is_static` | Optional. Determines how often a rule set is evaluated when it is accessed by a SQL statement.  - `TRUE`: The rule set is evaluated once during the user session. After that, the value is re-used. - `FALSE`: The rule set evaluated each time a SQL statement accesses it (default). |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_RULE_SET(
  rule_set_name    => 'Limit_DBA_Access', 
  description      => 'DBA access through predefined processes', 
  enabled          => DBMS_MACUTL.G_YES,
  eval_options     => DBMS_MACUTL.G_RULESET_AUDIT_FAIL,
  audit_options    => DBMS_MACUTL.G_RULESET_AUDIT_FAIL,
  fail_options     => DBMS_MACUTL.G_RULESET_FAIL_SHOW,
  fail_message     => 'Access denied!',
  fail_code        => 20900,
  handler_options  => DBMS_MACUTL.G_RULESET_HANDLER_OFF, 
  handler          => '',
  is_static        =  TRUE);
END;
/
```

## Command Rule Procedures Within DBMS\_MACADM

Table 12-23 lists procedures within the `DBMS_MACADM` package that you can use to configure command rules.

[Chapter 6, "Configuring Command Rules,"](cfcmdaut.md) describes command rules in detail. See also [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for a set of general-purpose utility procedures that you can use with the command rule procedures.

Table 12-23 DBMS\_MACADM Command Rule Configuration Procedures

| Procedure | Description |
| --- | --- |
| CREATE\_COMMAND\_RULE Procedure | Creates a command rule, associates it with a rule set, and lets you enable the command rule for rule checking with a rule set |
| DELETE\_COMMAND\_RULE Procedure | Drops a command rule declaration |
| UPDATE\_COMMAND\_RULE Procedure | Updates a command rule declaration |

### CREATE\_COMMAND\_RULE Procedure

The `CREATE_COMMAND_RULE` procedure creates a command rule, associates it with a rule set, and lets you enable the command rule for rule checking with a rule set.

Syntax

```
DBMS_MACADM.CREATE_COMMAND_RULE(
  command         IN VARCHAR2, 
  rule_set_name   IN VARCHAR2, 
  object_owner    IN VARCHAR2, 
  object_name     IN VARCHAR2, 
  enabled         IN VARCHAR2);
```

Parameters

Table 12-24 CREATE\_COMMAND\_RULE Parameters

| Parameter | Description |
| --- | --- |
| `command` | SQL statement to protect.  See also the following:  - ["DVSYS.DBA\_DV\_COMMAND\_RULE View"](views.md) for a listing of existing command rules - ["SQL Statements That Can Be Protected by Command Rules"](cfcmdaut.md) for a listing of available SQL statements that you can use - [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about SQL statements |
| `rule_set_name` | Name of rule set to associate with this command rule.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `object_owner` | Database schema to which this command rule will apply. The wildcard `%` is allowed, except for the `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `EXECUTE` statements.  To find the available users, query the `DBA_USERS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5081.htm#REFRN23302).  See also "Object Owner" in ["Creating and Editing a Command Rule"](cfcmdaut.md) for more information. |
| `object_name` | Object name. (The wildcard % is allowed. See "Object Name" in ["Creating and Editing a Command Rule"](cfcmdaut.md) for more information about objects protected by command rules.)  To find the available objects, query the `ALL_OBJECTS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1158.htm#REFRN20146). |
| `enabled` | `DBMS_MACUTL.G_YES` (Yes) enables the command rule; `DBMS_MACUTL.G_NO` (No) disables it. The default is `DBMS_MACUTL.G_YES`. |

Example

```
BEGIN
 DBMS_MACADM.CREATE_COMMAND_RULE(
  command         => 'SELECT', 
  rule_set_name   => 'Limit Sector 2 Access', 
  object_owner    => 'SYSADM', 
  object_name     => 'EMP_DATA', 
  enabled         => DBMS_MACUTL.G_YES);
END; 
/
```

### DELETE\_COMMAND\_RULE Procedure

The `DELETE_COMMAND_RULE` procedure drops a command rule declaration.

Syntax

```
DBMS_MACADM.DELETE_COMMAND_RULE(
  command      IN VARCHAR2, 
  object_owner IN VARCHAR2, 
  object_name  IN VARCHAR2);
```

Parameters

Table 12-25 DELETE\_COMMAND\_RULE Parameters

| Parameter | Description |
| --- | --- |
| `command` | SQL statement the command rule protects.  To find available command rules, query the `DVSYS.DBA_DV_COMMAND_RULE` view, described in ["DVSYS.DBA\_DV\_COMMAND\_RULE View"](views.md). |
| `object_owner` | Database schema to which this command rule applies.  To find the available users in the current database instance, query the `DBA_USERS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5081.htm#REFRN23302).  See also "Object Owner" in ["Creating and Editing a Command Rule"](cfcmdaut.md) for more information. |
| `object_name` | Object name. (The wildcard % is allowed. See "Object Name" in ["Creating and Editing a Command Rule"](cfcmdaut.md) for more information about objects protected by command rules.)  To find the available objects, query the `ALL_OBJECTS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1158.htm#REFRN20146). |

Example

```
BEGIN
 DBMS_MACADM.DELETE_COMMAND_RULE(
  command      => 'SELECT', 
  object_owner => 'SYSADM', 
  object_name  => 'EMP_DATA'); 
END;
/
```

### UPDATE\_COMMAND\_RULE Procedure

The `UPDATE_COMMAND_RULE` procedure updates a command rule declaration.

Syntax

```
DBMS_MACADM.UPDATE_COMMAND_RULE(
  command        IN VARCHAR2, 
  rule_set_name  IN VARCHAR2, 
  object_owner   IN VARCHAR2, 
  object_name    IN VARCHAR2, 
  enabled        IN VARCHAR2);
```

Parameters

Table 12-26 UPDATE\_COMMAND\_RULE Parameters

| Parameter | Description |
| --- | --- |
| `command` | SQL statement to protect.  See also the following:  - ["SQL Statements That Can Be Protected by Command Rules"](cfcmdaut.md) for a listing of available SQL statements that you can use - ["DVSYS.DBA\_DV\_COMMAND\_RULE View"](views.md) for a listing of existing command rules - [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about SQL statements |
| `rule_set_name` | Name of rule set to associate with this command rule.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |
| `object_owner` | Database schema to which this command rule applies.  To find the available users, query the `DBA_USERS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5081.htm#REFRN23302). See also "Object Owner" in ["Creating and Editing a Command Rule"](cfcmdaut.md) for more information. |
| `object_name` | Object name. (The wildcard % is allowed. See "Object Name" in ["Creating and Editing a Command Rule"](cfcmdaut.md) for more information about objects protected by command rules.)  To find the available objects, query the `ALL_OBJECTS` view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1158.htm#REFRN20146). |
| `enabled` | `DBMS_MACUTL.G_YES` (Yes) enables the command rule; `DBMS_MACUTL.G_NO` (No) disables it.  The default for `enabled` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_COMMAND_RULE` data dictionary view. |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_COMMAND_RULE(
  command         => 'SELECT', 
  rule_set_name   => 'Limit Sector 2 Access', 
  object_owner    => 'SYSADM', 
  object_name     => '%', 
  enabled         => DBMS_MACUTL.G_NO);
END;
/
```

## Factor Procedures and Functions Within DBMS\_MACADM

Table 12-27 lists procedures and functions within the `DBMS_MACADM` package that you can use to configure factors.

See Also:

- [Chapter 7, "Configuring Factors,"](cfgfact.md) for detailed information about factors
- [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for a set of general-purpose utility procedures that you can use with the factor procedures
- [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces,"](plsql_interfaces.md) for a set of PL/SQL interfaces that you can use with factors

Table 12-27 DBMS\_MACADM Factor Configuration Procedures

| Procedure | Description |
| --- | --- |
| ADD\_FACTOR\_LINK Procedure | Specifies a parent-child relationship for two factors |
| ADD\_POLICY\_FACTOR Procedure | Specifies that the label for a factor contributes to the Oracle Label Security label for a policy. |
| CHANGE\_IDENTITY\_FACTOR Procedure | Associates an identity with a different factor |
| CHANGE\_IDENTITY\_VALUE Procedure | Updates the value of an identity |
| CREATE\_DOMAIN\_IDENTITY Procedure | Adds an Oracle Real Application Clusters (Oracle RAC) database node to the domain factor identities and labels it according to the Oracle Label Security policy. |
| CREATE\_FACTOR Procedure | Creates a factor |
| CREATE\_FACTOR\_TYPE Procedure | Creates a factor type |
| CREATE\_IDENTITY Procedure | Creates an identity |
| CREATE\_IDENTITY\_MAP Procedure | Defines a set of tests that are used to derive the identity of a factor from the value of linked child factors (subfactors) |
| DELETE\_FACTOR Procedure | Deletes a factor |
| DELETE\_FACTOR\_LINK Procedure | Removes a parent-child relationship for two factors |
| DELETE\_FACTOR\_TYPE Procedure | Deletes a factor type |
| DELETE\_IDENTITY Procedure | Removes an identity |
| DELETE\_IDENTITY\_MAP Procedure | Removes an identity map from a factor |
| DROP\_DOMAIN\_IDENTITY Procedure | Removes an Oracle RAC database node from a domain |
| GET\_INSTANCE\_INFO Function | Returns information from the `SYS.V_$INSTANCE` system table about the current database instance; returns a `VARCHAR2` value |
| GET\_SESSION\_INFO Function | Returns information from the `SYS.V_$SESSION` system table for the current session; returns a `VARCHAR2` value |
| RENAME\_FACTOR Procedure | Renames a factor. The name change takes effect everywhere the factor is used. |
| RENAME\_FACTOR\_TYPE Procedure | Renames a factor type. The name change takes effect everywhere the factor type is used. |
| UPDATE\_FACTOR Procedure | Updates a factor |
| UPDATE\_FACTOR\_TYPE Procedure | Updates the description of a factor type |
| UPDATE\_IDENTITY Procedure | Updates the trust level of a factor identity |

### ADD\_FACTOR\_LINK Procedure

The `ADD_FACTOR_LINK` procedure specifies a parent-child relationship for two factors.

Syntax

```
DBMS_MACADM.ADD_FACTOR_LINK(
  parent_factor_name IN VARCHAR2, 
  child_factor_name  IN VARCHAR2, 
  label_indicator    IN VARCHAR2);
```

Parameters

Table 12-28 ADD\_FACTOR\_LINK Parameters

| Parameter | Description |
| --- | --- |
| `parent_factor_name` | Parent factor name.  To find existing parent and child factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR_LINK` view, described in ["DVSYS.DBA\_DV\_FACTOR\_LINK View"](views.md). |
| `child_factor_name` | Child factor name. |
| `label_indicator` | Indicates that the child factor being linked to the parent factor contributes to the label of the parent factor in an Oracle Label Security integration. Specify either `DBMS_MACUTL.G_YES` (for Yes) or `DBMS_MACUTL.G_NO` (for No).  To find the Oracle Label Security policies and labels associated with factors, query the following views, described in [Chapter 16, "Oracle Database Vault Data Dictionary Views"](views.md):  - `DVSYS.DBA_DV_MAC_POLICY`: Lists Oracle Label Security policies defined in the current database instance. - `DVSYS.DBA_DV_MAC_POLICY_FACTOR`: Lists the factors that are associated with Oracle Label Security policies for the current database instance. - `DVSYS.DBA_DV_POLICY_LABEL`: Lists the Oracle Label Security label for each factor identifier in the `DVSYS.DBA_DV_IDENTITY` view for each policy. |

Example

```
BEGIN
 DBMS_MACADM.ADD_FACTOR_LINK(
  parent_factor_name => 'HQ_ClientID', 
  child_factor_name  => 'Div1_ClientID', 
  label_indicator    => DBMS_MACUTL.G_YES);
END;
/
```

### ADD\_POLICY\_FACTOR Procedure

The `ADD_POLICY_FACTOR` procedure specifies that the label for a factor contributes to the Oracle Label Security label for a policy.

Syntax

```
DBMS_MACADM.ADD_POLICY_FACTOR(
  policy_name  IN VARCHAR2, 
  factor_name  IN VARCHAR2);
```

Parameters

Table 12-29 ADD\_POLICY\_FACTOR Parameters

| Parameter | Description |
| --- | --- |
| `policy_name` | Oracle Label Security policy name.  To find the policies defined in the current database instance, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md).  To find factors that are associated with Oracle Label Security policies, query `DVSYS.DBA_DV_MAC_POLICY_FACTOR`, described in ["DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR View"](views.md). |
| `factor_name` | Factor name.  To find existing factors, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.ADD_POLICY_FACTOR(
  policy_name  => 'AccessData', 
  factor_name  => 'Sector2_ClientID'); 
END;
/
```

### CHANGE\_IDENTITY\_FACTOR Procedure

The `CHANGE_IDENTITY_FACTOR` procedure associates an identity with a different factor.

Syntax

```
DBMS_MACADM.CHANGE_IDENTITY_FACTOR(
  factor_name     IN VARCHAR2, 
  value           IN VARCHAR2, 
  new_factor_name IN VARCHAR2);
```

Parameters

Table 12-30 CHANGE\_IDENTITY\_FACTOR Parameters

| Parameter | Description |
| --- | --- |
| `factor_name` | Current factor name.  To find existing factors, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `value` | Value of the identity to update.  To find existing identities for each factor in the current database instance, query the `DVSYS.DBA_DV_IDENTITY` view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md).  To find current identity mappings, query the `DVSYS.DBA_DV_IDENTITY_MAP` view, described in ["DVSYS.DBA\_DV\_IDENTITY\_MAP View"](views.md). |
| `new_factor_name` | Name of the factor to associate with the identity, which you can find by querying the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.CHANGE_IDENTITY_FACTOR(
  factor_name     => 'Sector2_ClientID', 
  value           => 'intranet', 
  new_factor_name => 'Sector4_ClientID'); 
END;
/
```

### CHANGE\_IDENTITY\_VALUE Procedure

The `CHANGE_IDENTITY_FACTOR` procedure updates the value of an identity.

Syntax

```
DBMS_MACADM.CHANGE_IDENTITY_VALUE(
  factor_name  IN VARCHAR2, 
  value        IN VARCHAR2, 
  new_value    IN VARCHAR2);
```

Parameters

Table 12-31 CHANGE\_IDENTITY\_VALUE Parameters

| Parameter | Description |
| --- | --- |
| `factor_name` | Factor name.  To find existing factors, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `value` | Current value associated with the identity.  To find existing identities for each factor in the current database instance, query the `DVSYS.DBA_DV_IDENTITY` view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md).  To find current identity mappings, query the `DVSYS.DBA_DV_IDENTITY_MAP` view, described in ["DVSYS.DBA\_DV\_IDENTITY\_MAP View"](views.md). |
| `new_value` | New identity value, up to 1024 characters in mixed-case. |

Example

```
BEGIN
 DBMS_MACADM.CHANGE_IDENTITY_VALUE(
  factor_name  => 'Sector2_ClientID', 
  value        => 'remote', 
  new_value    => 'intranet');
END; 
/
```

### CREATE\_DOMAIN\_IDENTITY Procedure

The `CREATE_DOMAIN_IDENTITY` procedure adds an Oracle Real Application Clusters (Oracle RAC) database node to the domain factor identities and labels it according to the Oracle Label Security policy.

Syntax

```
DBMS_MACADM.CREATE_DOMAIN_IDENTITY(
  domain_name  IN VARCHAR2, 
  domain_host  IN VARCHAR2, 
  policy_name  IN VARCHAR2 DEFAULT NULL, 
  domain_label IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 12-32 CREATE\_DOMAIN\_IDENTITY Parameters

| Parameter | Description |
| --- | --- |
| `domain_name` | Name of the domain to which to add the host.  To find the logical location of the database within the network structure within a distributed database system, run the `DVF.F$DATABASE_DOMAIN` function, described in ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md). |
| `domain_host` | Oracle Real Application Clusters host name being added to the domain.  To find host name of a database, run the `DVF.F$DATABASE_HOSTNAME` function, described in ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md). |
| `policy_name` | Oracle Label Security policy name. If you omit the policy name, then the domain is not associated with any policy.  To find the available policies, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). |
| `domain_label` | Name of the domain to which to add the Oracle Label Security policy. |

Examples

```
BEGIN
 DBMS_MACADM.CREATE_DOMAIN_IDENTITY(
  domain_name  => 'example', 
  domain_host  => 'mydom_host', 
  policy_name  => 'AccessData', 
  domain_label => 'sensitive'); 
END;
/
```

### CREATE\_FACTOR Procedure

The `CREATE_FACTOR` procedure creates a factor. After you create a factor, you can give it an identity by using the `CREATE_IDENTITY` procedure, described in "CREATE\_IDENTITY Procedure".

Syntax

```
DBMS_MACADM.CREATE_FACTOR(
  factor_name       IN VARCHAR2, 
  factor_type_name  IN VARCHAR2, 
  description       IN VARCHAR2, 
  rule_set_name     IN VARCHAR2, 
  get_expr          IN VARCHAR2, 
  validate_expr     IN VARCHAR2, 
  identify_by       IN NUMBER, 
  labeled_by        IN NUMBER, 
  eval_options      IN NUMBER, 
  audit_options     IN NUMBER, 
  fail_options      IN NUMBER);
```

Parameters

Table 12-33 CREATE\_FACTOR Parameters

| Parameter | Description |
| --- | --- |
| `factor_name` | Factor name, up to 28 characters in mixed-case, without spaces.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `factor_type_name` | Type of the factor, up to 30 characters in mixed-case, without spaces.  To find existing factor types, query the `DBA_DV_FACTOR_TYPE` view, described in ["DVSYS.DBA\_DV\_FACTOR\_TYPE View"](views.md). |
| `description` | Description of the purpose of the factor, up to 1024 characters in mixed-case. |
| `rule_set_name` | Rule set name if you want to use a rule set to control when and how a factor identity is set.  To find existing rule sets, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). See also ["Assignment Rule Set"](cfgfact.md) for more information about assigning rule sets to factors. |
| `get_expr` | Valid PL/SQL expression that retrieves the identity of a factor. It can use up to 255 characters in mixed-case. See ["Retrieval Method"](cfgfact.md) for more information. See also the `audit_options` parameter. |
| `validate_expr` | Name of the procedure to validate the factor. This is a valid PL/SQL expression that returns a Boolean value (`TRUE` or `FALSE`) to validate the identity of the factor. See ["Validation Method"](cfgfact.md) for more information. |
| `identify_by` | Options for determining the identity of a factor, based on the expression set for the `get_expr` parameter:  - `DBMS_MACUTL.G_IDENTIFY_BY_CONSTANT`: By constant - `DBMS_MACUTL.G_IDENTIFY_BY_METHOD`: By method - `DBMS_MACUTL.G_IDENTIFY_BY_FACTOR`: By factor - `DBMS_MACUTL.G_IDENTIFY_BY_CONTEXT`: By context  See ["Factor Identification"](cfgfact.md) for more information. |
| `labeled_by` | Options for labeling the factor:  - `DBMS_MACUTL.G_LABELED_BY_SELF`: Labels the identities for the factor directly from the labels associated with an Oracle Label Security policy (default) - `DBMS_MACUTL.G_LABELED_BY_FACTORS`: Derives the factor identity label from the labels of its child factor identities.  See ["Factor Labeling"](cfgfact.md) for more information. |
| `eval_options` | Options for evaluating the factor when the user logs on:  - `DBMS_MACUTL.G_EVAL_ON_SESSION`: When the database session is created (default) - `DBMS_MACUTL.G_EVAL_ON_ACCESS` Each time the factor is accessed - `DBMS_MACUTL.G_EVAL_ON_STARTUP` On start-up  See ["Evaluation"](cfgfact.md) for more information. |
| `audit_options` | Options for auditing the factor if you want to generate a custom Oracle Database Vault audit record.  - `DBMS_MACUTL.G_AUDIT_OFF`: Disables auditing. - `DBMS_MACUTL.G_AUDIT_ALWAYS`: Always audits. - `DBMS_MACUTL.G_AUDIT_ON_GET_ERROR`: Audits if `get_expr` returns an error. - `DBMS_MACUTL.G_AUDIT_ON_GET_NULL`: Audits if `get_expr` is null. - `DBMS_MACUTL.G_AUDIT_ON_VALIDATE_ERROR`: Audits if the validation procedure returns an error. - `DBMS_MACUTL.G_AUDIT_ON_VALIDATE_FALSE`: Audits if the validation procedure is false. - `DBMS_MACUTL.G_AUDIT_ON_TRUST_LEVEL_NULL`: Audits if there is no trust level set. - `DBMS_MACUTL.G_AUDIT_ON_TRUST_LEVEL_NEG`: Audits if the trust level is negative.  See ["Audit Options"](cfgfact.md) for more information. |
| `fail_options` | Options for reporting factor errors:  - `DBMS_MACUTL.G_FAIL_WITH_MESSAGE`: Shows an error message (default) - `DBMS_MACUTL.G_FAIL_SILENTLY`: Does not show an error message  See ["Error Options"](cfgfact.md) for more information. |

Example

```
BEGIN
 DBMS_MACADM.CREATE_FACTOR(
  factor_name       => 'Sector2_DB', 
  factor_type_name  => 'Instance', 
  description       => ' ', 
  rule_set_name     => 'Limit_DBA_Access', 
  get_expr          => 'UPPER(SYS_CONTEXT(''USERENV'',''DB_NAME''))', 
  validate_expr     => 'dbavowner.check_db_access', 
  identify_by       => DBMS_MACUTL.G_IDENTIFY_BY_METHOD, 
  labeled_by        => DBMS_MACUTL.G_LABELED_BY_SELF, 
  eval_options      => DBMS_MACUTL.G_EVAL_ON_SESSION, 
  audit_options     => DBMS_MACUTL.G_AUDIT_OFF, 
  fail_options      => DBMS_MACUTL.G_FAIL_SILENTLY); 
END;
/
```

### CREATE\_FACTOR\_TYPE Procedure

The `CREATE_FACTOR_TYPE` procedure creates a user-defined factor type.

Syntax

```
DBMS_MACADM.CREATE_FACTOR_TYPE(
  name        IN VARCHAR2, 
  description IN VARCHAR2);
```

Parameters

Table 12-34 CREATE\_FACTOR\_TYPE Parameters

| Parameter | Description |
| --- | --- |
| `name` | Factor type name, up to 30 characters in mixed-case, without spaces.  To find existing factor types, query the `DVSYS.DBA_DV_FACTOR_TYPE` view, described in ["DVSYS.DBA\_DV\_FACTOR\_TYPE View"](views.md). |
| `description` | Description of the purpose of the factor type, up to 1024 characters in mixed-case. |

Example

```
BEGIN
 DBMS_MACADM.CREATE_FACTOR_TYPE(
  name        => 'Sector2Instance', 
  description => 'Checks DB instances used in Sector 2');
END;
/
```

### CREATE\_IDENTITY Procedure

The `CREATE_IDENTITY` procedure assigns an identity and an associated trust level for a given factor. After you create a factor, you must assign it an identity.

Syntax

```
DBMS_MACADM.CREATE_IDENTITY(
  factor_name  IN VARCHAR2, 
  value        IN VARCHAR2, 
  trust_level  IN NUMBER);
```

Parameters

Table 12-35 CREATE\_IDENTITY Parameters

| Parameter | Description |
| --- | --- |
| `factor_name` | Factor name.  To find existing factors, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `value` | The actual value of the factor, up to 1024 characters in mixed-case. For example, the identity of an IP\_Address factor could be the IP address of 192.0.2.12. |
| `trust_level` | Number that indicates the magnitude of trust relative to other identities for the same factor. In general, the higher the trust level number is set, the greater the trust. A trust level of 10 indicates "very trusted." Negative trust levels are not trusted.  See ["Creating and Configuring a Factor Identity"](cfgfact.md) for more information about trust levels and label security. |

Example

```
BEGIN
 DBMS_MACADM.CREATE_IDENTITY(
  factor_name  => 'Sector2_ClientID', 
  value        => 'intranet', 
  trust_level  => 5); 
END;
/
```

### CREATE\_IDENTITY\_MAP Procedure

The `CREATE_IDENTITY_MAP` procedure defines a set of tests that are used to derive the identity of a factor from the value of linked child factors (subfactors).

Syntax

```
DBMS_MACADM.CREATE_IDENTITY_MAP(
  identity_factor_name  IN VARCHAR2,
  identity_factor_value IN VARCHAR2, 
  parent_factor_name    IN VARCHAR2, 
  child_factor_name     IN VARCHAR2, 
  operation             IN VARCHAR2, 
  operand1              IN VARCHAR2, 
  operand2              IN VARCHAR2);
```

Parameters

Table 12-36 CREATE\_IDENTITY\_MAP Parameters

| Parameter | Description |
| --- | --- |
| `identity_factor_name` | Factor the identity map is for.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `identity_factor_value` | Value the factor assumes if the identity map evaluates to `TRUE`.  To find existing factor identities, query the `DVSYS.DBA_DV_IDENTITY` view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md).  To find current factor identity mappings, use `DVSYS.DBA_DV_IDENTITY_MAP`, described in ["DVSYS.DBA\_DV\_IDENTITY\_MAP View"](views.md). |
| `parent_factor_name` | The parent factor link to which the map is related.  To find existing parent-child factor mappings, query the `DVSYS.DBA_DV_IDENTITY_MAP` view, described in ["DVSYS.DBA\_DV\_IDENTITY\_MAP View"](views.md). |
| `child_factor_name` | The child factor link to which the map is related. |
| `operation` | Relational operator for the identity map (for example, <, >, =, and so on). |
| `operand1` | Left operand for the relational operator; refers to the low value you enter. |
| `operand2` | Right operand for the relational operator; refers to the high value you enter. |

Example

```
BEGIN
 DBMS_MACADM.CREATE_IDENTITY_MAP(
  identity_factor_name  => 'Sector2_ClientID',
  identity_factor_value => 'intranet', 
  parent_factor_name    => 'HQ_ClientID', 
  child_factor_name     => 'Div1_ClientID', 
  operation             => '<', 
  operand1              => '192.0.2.50', 
  operand2              => '192.0.2.100');
END;
/
```

### DELETE\_FACTOR Procedure

The `DELETE_FACTOR` procedure deletes a factor.

Syntax

```
DBMS_MACADM.DELETE_FACTOR(
  factor_name IN VARCHAR2);
```

Parameters

Table 12-37 DELETE\_FACTOR Parameter

| Parameter | Description |
| --- | --- |
| `factor_name` | Factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_FACTOR('Sector2_ClientID');
```

### DELETE\_FACTOR\_LINK Procedure

The `DELETE_FACTOR_LINK` procedure removes a parent-child relationship for two factors.

Syntax

```
DBMS_MACADM.DELETE_FACTOR_LINK(
  parent_factor_name IN VARCHAR2, 
  child_factor_name  IN VARCHAR2);
```

Parameters

Table 12-38 DELETE\_FACTOR\_LINK Parameters

| Parameter | Description |
| --- | --- |
| `parent_factor_name` | Factor name.  To find factors that are used in parent-child mappings in the current database instance, query the `DVSYS.DBA_DV_FACTOR_LINK` view, described in ["DVSYS.DBA\_DV\_FACTOR\_LINK View"](views.md). |
| `child_factor_name` | Factor name. |

Example

```
BEGIN
 DBMS_MACADM.DELETE_FACTOR_LINK(
  parent_factor_name => 'HQ_ClientID', 
  child_factor_name  => 'Div1_ClientID'); 
END;
/
```

### DELETE\_FACTOR\_TYPE Procedure

The `DELETE_FACTOR_TYPE` procedure deletes a factor type.

Syntax

```
DBMS_MACADM.DELETE_FACTOR_TYPE(
  name IN VARCHAR2);
```

Parameters

Table 12-39 DELETE\_FACTOR\_TYPE Parameters

| Parameter | Description |
| --- | --- |
| `name` | Factor type name.  To find existing factor types, query the `DVSYS.DBA_DV_FACTOR_TYPE` view, described in ["DVSYS.DBA\_DV\_FACTOR\_TYPE View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_FACTOR_TYPE('Sector2Instance');
```

### DELETE\_IDENTITY Procedure

The `DELETE_IDENTITY` procedure removes an identity from an existing factor.

Syntax

```
DBMS_MACADM.DELETE_IDENTITY(
  factor_name IN VARCHAR2, 
  value       IN VARCHAR2);
```

Parameters

Table 12-40 DELETE\_IDENTITY Parameters

| Parameter | Description |
| --- | --- |
| `factor_name` | Factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `value` | Identity value associated with the factor.  To find the identities for each factor in the current database instance, query the `DVSYS.DBA_DV_IDENTITY` view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.DELETE_IDENTITY(
  factor_name => 'Sector2_ClientID', 
  value       => 'intranet'); 
END;
/
```

### DELETE\_IDENTITY\_MAP Procedure

The `DELETE_IDENTITY_MAP` procedure removes an identity map for a factor.

Syntax

```
DBMS_MACADM.DELETE_IDENTITY_MAP(
  identity_factor_name  IN VARCHAR2, 
  identity_factor_value IN VARCHAR2,
  parent_factor_name    IN VARCHAR2, 
  child_factor_name     IN VARCHAR2, 
  operation             IN VARCHAR2, 
  operand1              IN VARCHAR2, 
  operand2              IN VARCHAR2);
```

Parameters

Table 12-41 DELETE\_IDENTITY\_MAP Parameters

| Parameter | Description |
| --- | --- |
| `identity_factor_name` | Factor the identity map is for.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `identity_factor_value` | Value the factor assumes if the identity map evaluates to `TRUE`.  To find existing factor identities, query the `DVSYS.DBA_DV_IDENTITY` view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md).  To find current factor identity mappings, query `DVSYS.DBA_DV_IDENTITY_MAP`, described in ["DVSYS.DBA\_DV\_IDENTITY\_MAP View"](views.md). |
| `parent_factor_name` | The parent factor link to which the map is related.  To find existing parent-child factors, query the `DVSYS.DBA_DV_FACTOR_link` view, described in ["DVSYS.DBA\_DV\_FACTOR\_LINK View"](views.md). |
| `child_factor_name` | The child factor to which the map is related. |
| `operation` | Relational operator for the identity map (for example, <, >, =, and so on). |
| `operand1` | Left (low value) operand for the relational operator. |
| `operand2` | Right (high value) operand for the relational operator. |

Example

```
BEGIN
 DBMS_MACADM.DELETE_IDENTITY_MAP(
  identity_factor_name  => 'Sector2_ClientID',
  identity_factor_value => 'intranet', 
  parent_factor_name    => 'HQ_ClientID', 
  child_factor_name     => 'Div1_ClientID', 
  operation             => '<', 
  operand1              => '192.0.2.10', 
  operand2              => '192.0.2.15');
END;
/
```

### DROP\_DOMAIN\_IDENTITY Procedure

The `DROP_DOMAIN_IDENTITY` procedure removes an Oracle Real Application Clusters database node from a domain.

Syntax

```
DBMS_MACADM.DROP_DOMAIN_IDENTITY(
  domain_name  IN VARCHAR2, 
  domain_host  IN VARCHAR2);
```

Parameters

Table 12-42 DROP\_DOMAIN\_IDENTITY Parameters

| Parameter | Description |
| --- | --- |
| `domain_name` | Name of the domain to which the host was added.  To find the domain of a database as specified by the `DB_DOMAIN` initialization parameter, run the `DVF.F$DATABASE_DOMAIN` function, described in ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md). |
| `domain_host` | Oracle Real Application Clusters host name being that was added to the domain.  To find the host name for a specified database, run the `DVF.F$DATABASE_HOSTNAME` function, described in ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md). |

Example

```
BEGIN
 DBMS_MACADM.DROP_DOMAIN_IDENTITY(
  domain_name  => 'example', 
  domain_host  => 'mydom_host'); 
END;
/
```

### GET\_INSTANCE\_INFO Function

The `GET_INSTANCE_INFO` function returns information from the `SYS.V_$INSTANCE` system table about the current database instance. The `V$INSTANCE` data dictionary view also contains database instance information from this table. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2002.htm#REFRN30105) for more information.

Syntax

```
DBMS_MACADM.GET_INSTANCE_INFO(
  p_parameter IN VARCHAR2)
RETURN VARCHAR2;
```

Parameters

Table 12-43 GET\_INSTANCE\_INFO Parameter

| Parameter | Description |
| --- | --- |
| `p_parameter` | Column name in the `SYS.V_$INSTANCE` system table |

Example

```
DECLARE
 instance_var varchar2 := null;
BEGIN 
 instance_var = DBMS_MACADM.GET_INSTANCE_INFO('INSTANCE_NAME'); 
END;
/
```

### GET\_SESSION\_INFO Function

The `GET_SESSION_INFO` function returns information from the `SYS.V_$SESSION` system table for the current session. The `V$SESSION` data dictionary view also contains session information from this table. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3016.htm#REFRN30223) for more information.

Syntax

```
DBMS_MACADM.GET_SESSION_INFO(
  p_parameter IN VARCHAR2)
RETURN VARCHAR2;
```

Parameters

Table 12-44 GET\_SESSION\_INFO Parameter

| Parameter | Description |
| --- | --- |
| `p_parameter` | Column name in the `SYS.V_$SESSION` system table. |

Example

```
DECLARE
 session_var varchar2 := null;
BEGIN 
 session_var = DBMS_MACADM.GET_SESSION_INFO('PROCESS'); 
END;
/
```

### RENAME\_FACTOR Procedure

The `RENAME_FACTOR` procedure renames a factor. The name change takes effect everywhere the factor is used.

Syntax

```
DBMS_MACADM.RENAME_FACTOR(
  factor_name     IN VARCHAR2, 
  new_factor_name IN VARCHAR2);
```

Parameters

Table 12-45 RENAME\_FACTOR Parameters

| Parameter | Description |
| --- | --- |
| `factor_name` | Current factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `new_factor_name` | New factor name, up to 28 characters in mixed-case, without spaces. |

Example

```
BEGIN
 DBMS_MACADM.RENAME_FACTOR(
  factor_name     => 'Sector2_ClientID', 
  new_factor_name => 'Sector2_Clients');
END;
/
```

### RENAME\_FACTOR\_TYPE Procedure

The `RENAME_FACTOR` procedure renames a factor type. The name change takes effect everywhere the factor type is used.

Syntax

```
DBMS_MACADM.RENAME_FACTOR_TYPE(
  old_name  IN VARCHAR2, 
  new_name  IN VARCHAR2);
```

Parameters

Table 12-46 RENAME\_FACTOR\_TYPE Parameters

| Parameter | Description |
| --- | --- |
| `old_name` | Current factor type name.  To find existing factor types in the current database instance, query the `DVSYS.DBA_DV_FACTOR_TYPE` view, described in ["DVSYS.DBA\_DV\_FACTOR\_TYPE View"](views.md). |
| `new_name` | New factor type name, up to 30 characters in mixed-case, without spaces. |

Example

```
BEGIN
 DBMS_MACADM.RENAME_FACTOR_TYPE(
  old_name  => 'Sector2Instance', 
  new_name  => 'Sector2DBInstance'); 
END;
/
```

### UPDATE\_FACTOR Procedure

The `UPDATE_FACTOR` procedure updates the description of a factor type.

Syntax

```
DBMS_MACADM.UPDATE_FACTOR(
  factor_name       IN VARCHAR2, 
  factor_type_name  IN VARCHAR2, 
  description       IN VARCHAR2, 
  rule_set_name     IN VARCHAR2, 
  get_expr          IN VARCHAR2, 
  validate_expr     IN VARCHAR2, 
  identify_by       IN NUMBER, 
  labeled_by        IN NUMBER, 
  eval_options      IN NUMBER, 
  audit_options     IN NUMBER, 
  fail_options      IN NUMBER);
```

Parameters

Table 12-47 UPDATE\_FACTOR

| Parameter | Description |
| --- | --- |
| `factor_name` | Factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `factor_type_name` | Factor type name.  To find existing factor types, query the `DVSYS.DBA_DV_FACTOR_TYPE` view, described in ["DVSYS.DBA\_DV\_FACTOR\_TYPE View"](views.md). |
| `description` | Description of the purpose of the factor, up to 1024 characters in mixed-case. |
| `rule_set_name` | Name of the rule set used to control when and how a factor identity is set.  To find existing rule sets, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md).  See also ["Assignment Rule Set"](cfgfact.md) for more information about assigning rule sets to factors. |
| `get_expr` | Valid PL/SQL expression that retrieves the identity of a factor. It can use up to 255 characters in mixed-case. See ["Retrieval Method"](cfgfact.md) for more information. See also the `audit_options` parameter. |
| `validate_expr` | Name of the procedure to validate factor. This is a valid PL/SQL expression that returns a Boolean value (`TRUE` or `FALSE`) to validate the identity of the factor. See ["Validation Method"](cfgfact.md) for more information. |
| `identify_by` | Options for determining the identity of a factor, based on the expression set for the `get_expr` parameter:  - `DBMS_MACUTL.G_IDENTIFY_BY_CONSTANT`: By constant - `DBMS_MACUTL.G_IDENTIFY_BY_METHOD`: By method - `DBMS_MACUTL.G_IDENTIFY_BY_FACTOR`: By factor - `DBMS_MACUTL.G_IDENTIFY_BY_CONTEXT`: By context  See ["Factor Identification"](cfgfact.md) for more information. |
| `labeled_by` | Options for labeling the factor:  - `DBMS_MACUTL.G_LABELED_BY_SELF`: Labels the identities for the factor directly from the labels associated with an Oracle Label Security policy - `DBMS_MACUTL.G_LABELED_BY_FACTORS`: Derives the factor identity label from the labels of its child factor identities.  The default for `labeled_by` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_FACTOR` data dictionary view.  See ["Factor Labeling"](cfgfact.md) for more information. |
| `eval_options` | Options for evaluating the factor when the user logs on:  - `DBMS_MACUTL.G_EVAL_ON_SESSION`: When the database session is created - `DBMS_MACUTL.G_EVAL_ON_ACCESS`: Each time the factor is accessed - `DBMS_MACUTL.G_EVAL_ON_STARTUP`: On start-up  The default for `eval_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_FACTOR` data dictionary view.  See ["Evaluation"](cfgfact.md) for more information. |
| `audit_options` | Options for auditing the factor if you want to generate a custom Oracle Database Vault audit record.  - `DBMS_MACUTL.G_AUDIT_OFF`: Disables auditing. - `DBMS_MACUTL.G_AUDIT_ALWAYS`: Always audits. - `DBMS_MACUTL.G_AUDIT_ON_GET_ERROR`: Audits if `get_expr` returns an error. - `DBMS_MACUTL.G_AUDIT_ON_GET_NULL`: Audits if `get_expr` is null. - `DBMS_MACUTL.G_AUDIT_ON_VALIDATE_ERROR`: Audits if the validation procedure returns an error. - `DBMS_MACUTL.G_AUDIT_ON_VALIDATE_FALSE`: Audits if the validation procedure is false. - `DBMS_MACUTL.G_AUDIT_ON_TRUST_LEVEL_NULL`: Audits if there is no trust level set. - `DBMS_MACUTL.G_AUDIT_ON_TRUST_LEVEL_NEG`: Audits if the trust level is negative.  The default for `audit_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_FACTOR` data dictionary view.  See ["Audit Options"](cfgfact.md) for more information. |
| `fail_options` | Options for reporting factor errors:  - `DBMS_MACUTL.G_FAIL_WITH_MESSAGE`: Shows an error message. - `DBMS_MACUTL.G_FAIL_SILENTLY`: Does not show an error message.  The default for `fail_options` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_FACTOR` data dictionary view.  See ["Error Options"](cfgfact.md) for more information. |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_FACTOR(
  factor_name       => 'Sector2_DB', 
  factor_type_name  => 'Instance', 
  description       => ' ', 
  rule_set_name     => 'Limit_DBA_Access', 
  get_expr          => 'UPPER(SYS_CONTEXT(''USERENV'',''DB_NAME''))', 
  validate_expr     => 'dbavowner.check_db_access', 
  identify_by       => DBMS_MACUTL.G_IDENTIFY_BY_METHOD, 
  labeled_by        => DBMS_MACUTL.G_LABELED_BY_SELF, 
  eval_options      => DBMS_MACUTL.G_EVAL_ON_ACCESS, 
  audit_options     => DBMS_MACUTL.G_AUDIT_ALWAYS, 
  fail_options      => DBMS_MACUTL.G_FAIL_WITH_MESSAGE); 
END;
/
```

### UPDATE\_FACTOR\_TYPE Procedure

The `UPDATE_FACTOR_TYPE` procedure updates a factor type.

Syntax

```
DBMS_MACADM.UPDATE_FACTOR_TYPE(
  name         IN VARCHAR2, 
  description  IN VARCHAR2);
```

Parameters

Table 12-48 UPDATE\_FACTOR\_TYPE Parameters

| Parameter | Description |
| --- | --- |
| `name` | Factor type name.  To find existing factor types in the current database instance, query the `DVSYS.DBA_DV_FACTOR_TYPE` view, described in ["DVSYS.DBA\_DV\_FACTOR\_TYPE View"](views.md). |
| `description` | Description of the purpose of the factor type, up to 1024 characters in mixed case. |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_FACTOR_TYPE(
  name        => 'Sector2DBInstance', 
  description => 'Checks DB instances used in Sector 2');
END;
/
```

### UPDATE\_IDENTITY Procedure

The `UPDATE_IDENTITY` procedure updates the trust level of a factor identity.

Syntax

```
DBMS_MACADM.UPDATE_IDENTITY(
  factor_name  IN VARCHAR2, 
  value        IN VARCHAR2, 
  trust_level  IN NUMBER);
```

Parameters

Table 12-49 UPDATE\_IDENTITY Parameters

| Parameter | Description |
| --- | --- |
| `factor_name` | Factor name.  To find existing factors in the current database instance, query the `DBSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md).  To find factors that have identities, query `DVSYS.DBA_DV_IDENTITY`, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md). |
| `value` | New factor identity, up to 1024 characters in mixed-case. For example, the identity of an IP\_Address factor could be the IP address of 192.0.2.12. |
| `trust_level` | Number that indicates the magnitude of trust relative to other identities for the same factor. In general, the higher the trust level number is set, the greater the trust. A trust level of 10 indicates "very trusted." Negative trust levels are not trusted.  See ["Creating and Configuring a Factor Identity"](cfgfact.md) for more information about trust levels and label security. |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_IDENTITY(
  factor_name  => 'Sector2_ClientID', 
  value        => 'intranet', 
  trust_level  => 10); 
END;
/
```

## Secure Application Role Procedures Within DBMS\_MACADM

Table 12-50 lists procedures within the `DBMS_MACADM` package that you can use to configure Oracle Database Vault secure application roles.

[Chapter 8, "Configuring Secure Application Roles for Oracle Database Vault,"](cfseappr.md) describes secure application roles in detail. See also [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for a set of general-purpose utility procedures that you can use with the secure application role procedures.

Table 12-50 DBMS\_MACADM Secure Application Role Configuration Procedures

| Procedure | Description |
| --- | --- |
| CREATE\_ROLE Procedure | Creates an Oracle Database Vault secure application role |
| DELETE\_ROLE Procedure | Deletes an Oracle Database Vault secure application role |
| RENAME\_ROLE Procedure | Renames an Oracle Database Vault secure application role. The name change takes effect everywhere the role is used. |
| UPDATE\_ROLE Procedure | Updates a Oracle Database Vault secure application role |

### CREATE\_ROLE Procedure

The `CREATE_ROLE` procedure creates an Oracle Database Vault secure application role.

Syntax

```
DBMS_MACADM.CREATE_ROLE(
  role_name      IN VARCHAR2, 
  enabled        IN VARCHAR2,
  rule_set_name  IN VARCHAR2);
```

Parameters

Table 12-51 CREATE\_ROLE Parameters

| Parameter | Description |
| --- | --- |
| `role_name` | Role name, up to 30 characters, with no spaces. Preferably, enter the role name in upper case letters, though you are not required to do so.  To find existing secure application roles in the current database instance, query the `DVSYS.DBA_DV_ROLE` view, described in ["DVSYS.DBA\_DV\_ROLE View"](views.md). |
| `enabled` | `Y` (yes) makes the role available for enabling; `N` (no) prevents the role from being enabled. The default is `Y`.  You can also use the following `DBMS_MACUTL` constants:  - `DBMS_MACUTL.G_YES` - `DBMS_MACUTL.G_NO` |
| `rule_set_name` | Name of rule set to determine whether a user can set this secure application role.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.CREATE_ROLE(
  role_name      => 'Sector2_APP_MGR', 
  enabled        => DBMS_MACUTL.G_YES,
  rule_set_name  => 'Check App2 Access');
END;
/
```

### DELETE\_ROLE Procedure

The `DELETE_ROLE` procedure deletes an Oracle Database Vault secure application role.

Syntax

```
DBMS_MACADM.DELETE_ROLE(
  role_name IN VARCHAR2);
```

Parameters

Table 12-52 DELETE\_ROLE Parameter

| Parameter | Description |
| --- | --- |
| `role_name` | Role name.  To find existing secure application roles in the current database instance, query the `DVSYS.DBA_DV_ROLE` view, described in ["DVSYS.DBA\_DV\_ROLE View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_ROLE('SECT2_APP_MGR');
```

### RENAME\_ROLE Procedure

The `RENAME_ROLE` procedure renames an Oracle Database Vault secure application role. The name change takes effect everywhere the role is used.

Syntax

```
DBMS_MACADM.RENAME_ROLE(
  role_name      IN VARCHAR2, 
  new_role_name  IN VARCHAR2);
```

Parameters

Table 12-53 RENAME\_ROLE Parameters

| Parameter | Description |
| --- | --- |
| `role_name` | Current role name. Preferably, enter the role name in upper case letters, though you are not required to do so.  To find existing secure application roles in the current database instance, query the `DVSYS.DBA_DV_ROLE` view, described in ["DVSYS.DBA\_DV\_ROLE View"](views.md). |
| `new_role_name` | Role name, up to 30 characters, in uppercase, with no spaces. Ensure that this name follows the standard Oracle naming conventions for role creation described in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm). |

Example

```
BEGIN
 DBMS_MACADM.RENAME_ROLE(
  role_name      => 'SECT2_APP_MGR', 
  new_role_name  => 'SECT2_SYSADMIN');
END;
/
```

### UPDATE\_ROLE Procedure

The `UPDATE_ROLE` procedure updates a Oracle Database Vault secure application role.

Syntax

```
DBMS_MACADM.UPDATE_ROLE(
  role_name      IN VARCHAR2, 
  enabled        IN VARCHAR2, 
  rule_set_name  IN VARCHAR2);
```

Parameters

Table 12-54 UPDATE\_ROLE Parameters

| Parameter | Description |
| --- | --- |
| `role_name` | Role name.  To find existing secure application roles in the current database instance, query the `DVSYS.DBA_DV_ROLE` view, described in ["DVSYS.DBA\_DV\_ROLE View"](views.md). |
| `enabled` | `DBMS_MACUTL.G_YES` (Yes) makes the role available for enabling; `DBMS_MACUTL.G_NO` (No) prevents the role from being enabled.  The default for `enabled` is the previously set value, which you can find by querying the `DVSYS.DBA_DV_ROLE` data dictionary view. |
| `rule_set_name` | Name of rule set to determine whether a user can set this secure application role.  To find existing rule sets in the current database instance, query the `DVSYS.DBA_DV_RULE_SET` view, described in ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_ROLE(
  role_name      => 'SECT2_SYSADMIN', 
  enabled        => DBMS_MACUTL.G_YES, 
  rule_set_name  => 'System Access Controls');
END;
/
```

## Oracle Label Security Policy Procedures Within DBMS\_MACADM

Table 12-55 lists procedures within the `DBMS_MACADM` package that you can use to configure Oracle Label Security policies for Oracle Database Vault.

[Chapter 9, "Integrating Oracle Database Vault with Other Oracle Products,"](dv_ols.md) describes Oracle Label Security policies in detail. See also [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for a set of general-purpose utility procedures that you can use with the Oracle Label Security policy procedures.

Table 12-55 DBMS\_MACADM Oracle Label Security Configuration Procedures

| Procedure | Description |
| --- | --- |
| CREATE\_MAC\_POLICY Procedure | Specifies the algorithm that is used to merge labels when computing the label for a factor, or the Oracle Label Security Session label |
| CREATE\_POLICY\_LABEL Procedure | Labels an identity within an Oracle Label Security policy |
| DELETE\_MAC\_POLICY\_CASCADE Procedure | Deletes all Oracle Database Vault objects related to an Oracle Label Security policy. |
| DELETE\_POLICY\_FACTOR Procedure | Removes the factor from contributing to the Oracle Label Security label |
| DELETE\_POLICY\_LABEL Procedure | Removes the label from an identity within an Oracle Label Security policy |
| UPDATE\_MAC\_POLICY Procedure | Specifies the algorithm that is used to merge labels when computing the label for a factor, or the Oracle Label Security Session label |

### CREATE\_MAC\_POLICY Procedure

The `CREATE_MAC_POLICY` procedure specifies the algorithm that is used to merge labels when computing the label for a factor, or the Oracle Label Security Session label.

Syntax

```
DBMS_MACADM.CREATE_MAC_POLICY(
  policy_name  IN VARCHAR2,
  algorithm    IN VARCHAR2);
```

Parameters

Table 12-56 CREATE\_MAC\_POLICY Parameters

| Parameter | Description |
| --- | --- |
| `policy_name` | Name of an existing policy.  To find existing policies in the current database instance, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). |
| `algorithm` | Merge algorithm for cases when Oracle Label Security has merged two labels. Enter the code listed in Table 12-57 that corresponds to the merge algorithm you want. For example, enter `HUU` to if you want to select the Maximum Level/Union/Union merge algorithm.  For more information on label-merging algorithms, see [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/toc.htm). |

Table 12-57 Oracle Label Security Merge Algorithm Codes

| Code | Value |
| --- | --- |
| `HUU` | Maximum Level/Union/Union |
| `HIU` | Maximum Level/Intersection/Union |
| `HMU` | Maximum Level/Minus/Union |
| `HNU` | Maximum Level/Null/Union |
| `HUI` | Maximum Level/Union/Intersection |
| `HII` | Maximum Level/Intersection/Intersection |
| `HMI` | Maximum Level/Minus/Intersection |
| `HNI` | Maximum Level/Null/Intersection |
| `HUM` | Maximum Level/Union/Minus |
| `HIM` | Maximum Level/Intersection/Minus |
| `HMM` | Maximum Level/Minus/Minus |
| `HNM` | Maximum Level/Null/Minus |
| `HUN` | Maximum Level/Union/Null |
| `HIN` | Maximum Level/Intersection/Null |
| `HMN` | Maximum Level/Minus/Null |
| `HNN` | Maximum Level/Null/Null |
| `LUU` | Minimum Level/Union/Union |
| `LIU` | Minimum Level/Intersection/Union |
| `LMU` | Minimum Level/Minus/Union |
| `LNU` | Minimum Level/Null/Union |
| `LUI` | Minimum Level/Union/Intersection |
| `LII` | Minimum Level/Intersection/Intersection |
| `LMI` | Minimum Level/Minus/Intersection |
| `LNI` | Minimum Level/Null/Intersection |
| `LUM` | Minimum Level/Union/Minus |
| `LIM` | Minimum Level/Intersection/Minus |
| `LMM` | Minimum Level/Minus/Minus |
| `LNM` | Minimum Level/Null/Minus |
| `LUN` | Minimum Level/Union/Null |
| `LIN` | Minimum Level/Intersection/Null |
| `LMN` | Minimum Level/Minus/Null |
| `LNN` | Minimum Level/Null/Null |

Example

```
BEGIN
 DBMS_MACADM.CREATE_MAC_POLICY(
  policy_name  => 'Access Locations',
  algorithm    => 'HUU');
END;
/
```

### CREATE\_POLICY\_LABEL Procedure

The `CREATE_POLICY_LABEL` procedure labels an identity within an Oracle Label Security policy.

Syntax

```
DBMS_MACADM.CREATE_POLICY_LABEL(
  identity_factor_name   IN VARCHAR2, 
  identity_factor_value  IN VARCHAR2, 
  policy_name            IN VARCHAR2, 
  label                  IN VARCHAR2);
```

Parameters

Table 12-58 CREATE\_POLICY\_LABEL Parameters

| Parameter | Description |
| --- | --- |
| `identity_factor_name` | Name of the factor being labeled.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md).  To find factors that are associated with Oracle Label Security policies, use `DVSYS.DBA_DV_MAC_POLICY_FACTOR`, described in ["DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR View"](views.md).  See also ["Label Security Policy Factors"](dv_ols.md) for more information. |
| `identity_factor_value` | Value of identity for the factor being labeled.  To find the identities of existing factors in the current database instance, query the `DVSYS.DBA_DV_IDENTITY` view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md). |
| `policy_name` | Name of an existing policy.  To find existing policies in the current database instance, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). |
| `label` | Oracle Label Security label name.  To find existing policy labels for factor identifiers, query the `DVSYS.DBA_DV_POLICY_LABEL` view, described in ["DVSYS.DBA\_DV\_POLICY\_LABEL View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.CREATE_POLICY_LABEL(
  identity_factor_name   => 'App_Host_Name', 
  identity_factor_value  => 'Sect2_Fin_Apps', 
  policy_name            => 'Access Locations', 
  label                  => 'Sensitive'); 
END;
/
```

### DELETE\_MAC\_POLICY\_CASCADE Procedure

The `DELETE_MAC_POLICY_CASCADE` procedure deletes all Oracle Database Vault objects related to an Oracle Label Security policy.

Syntax

```
DBMS_MACADM.DELETE_MAC_POLICY_CASCADE(
  policy_name  IN VARCHAR2);
```

Parameters

Table 12-59 DELETE\_MAC\_POLICY\_CASCADE Parameter

| Parameter | Description |
| --- | --- |
| `policy_name` | Name of an existing policy.  To find existing policies in the current database instance, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). |

Example

```
EXEC DBMS_MACADM.DELETE_MAC_POLICY_CASCADE('Access Locations');
```

### DELETE\_POLICY\_FACTOR Procedure

The `DELETE_POLICY_FACTOR` procedure removes the factor from contributing to the Oracle Label Security label.

Syntax

```
DBMS_MACADM.DELETE_POLICY_FACTOR(
  policy_name  IN VARCHAR2, 
  factor_name  IN VARCHAR2);
```

Parameters

Table 12-60 DELETE\_POLICY\_FACTOR Parameters

| Parameter | Description |
| --- | --- |
| `policy_name` | Name of an existing policy.  To find existing policies in the current database instance, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). |
| `factor_name` | Name of factor associated with the Oracle Label Security label.  To find factors that are associated with Oracle Label Security policies, query `DVSYS.DBA_DV_MAC_POLICY_FACTOR`, described in ["DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.DELETE_POLICY_FACTOR(
  policy_name  => 'Access Locations', 
  factor_name  => 'App_Host_Name'); 
END;
/
```

### DELETE\_POLICY\_LABEL Procedure

The `DELETE_POLICY_LABEL` procedure removes the label from an identity within an Oracle Label Security policy.

Syntax

```
DBMS_MACADM.DELETE_POLICY_LABEL(
  identity_factor_name   IN VARCHAR2, 
  identity_factor_value  IN VARCHAR2, 
  policy_name            IN VARCHAR2, 
  label                  IN VARCHAR2);
```

Parameters

Table 12-61 DELETE\_POLICY\_LABEL Parameters

| Parameter | Description |
| --- | --- |
| `identity_factor_name` | Name of the factor that was labeled.  To find existing factors in the current database instance that are associated with Oracle Label Security policies, query `DVSYS.DBA_DV_MAC_POLICY_FACTOR`, described in ["DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR View"](views.md).  See also ["Label Security Policy Factors"](dv_ols.md) for more information. |
| `identity_factor_value` | Value of identity for the factor that was labeled.  To find the identities of existing factors in the current database instance, query the `DVSYS.DBA_DV_IDENTITY` view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md). |
| `policy_name` | Name of an existing policy.  To find existing policies in the current database instance, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). |
| `label` | Oracle Label Security label name.  To find existing policy labels for factor identifiers, query the `DVSYS.DBA_DV_POLICY_LABEL` view, described in ["DVSYS.DBA\_DV\_POLICY\_LABEL View"](views.md). |

Example

```
BEGIN
 DBMS_MACADM.DELETE_POLICY_LABEL(
  identity_factor_name   => 'App_Host_Name', 
  identity_factor_value  => 'Sect2_Fin_Apps', 
  policy_name            => 'Access Locations', 
  label                  => 'Sensitive'); 
END;
/
```

### UPDATE\_MAC\_POLICY Procedure

The `UPDATE_MAC_POLICY` procedure specifies the algorithm that is used to merge labels when computing the label for a factor, or the Oracle Label Security Session label.

Syntax

```
DBMS_MACADM.UPDATE_MAC_POLICY(
  policy_name  IN VARCHAR2, 
  algorithm    IN VARCHAR2);
```

Parameters

Table 12-62 UPDATE\_MAC\_POLICY

| Parameter | Description |
| --- | --- |
| `policy_name` | Name of an existing policy.  To find existing policies in the current database instance, query the `DVSYS.DBA_DV_MAC_POLICY` view, described in ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). |
| `algorithm` | Merge algorithm for cases when Oracle Label Security has merged two labels. See Table 12-57 for listing of the available algorithms.  For more information on label-merging algorithms, see [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/toc.htm). |

Example

```
BEGIN
 DBMS_MACADM.UPDATE_MAC_POLICY(
  policy_name  => 'Access Locations',
  algorithm    => 'LUI');
END;
/
```

## General System Maintenance Procedures Within DBMS\_MACADM

Table 12-63 lists the procedures within the `DBMS_MACADM` PL/SQL package that you can use to perform general maintenance activities that require the protection of the `DV_OWNER` or `DV_ADMIN` role.

Table 12-63 DBMS\_MACADM Disable/Enable Procedures

| Procedure | Description |
| --- | --- |
| ADD\_NLS\_DATA Procedure | Adds a new language to Oracle Database Vault |
| AUTHORIZE\_DATAPUMP\_USER Procedure | Authorizes a user to perform Oracle Data Pump operations when Oracle Database Vault is enabled |
| AUTHORIZE\_SCHEDULER\_USER Procedure | Authorizes a user to schedule database jobs when Oracle Database Vault is enabled |
| UNAUTHORIZE\_DATAPUMP\_USER Procedure | Revokes the authorization that was granted by the `DBMS_MACADM.AUTHORIZE_DATAPUMP_USER` procedure |
| UNAUTHORIZE\_SCHEDULER\_USER Procedure | Revokes authorization that was granted by the `DBMS_MACADM.AUTHORIZE_SCHEDULER_USER` procedure |

### ADD\_NLS\_DATA Procedure

The `ADD_NLS_DATA` procedure adds a new language to Oracle Database Vault.

Syntax

```
DBMS_MACADM.ADD_NLS_DATA(
  language      IN VARCHAR );
```

Parameters

Table 12-64 ADD\_NLS\_DATA

| Parameter | Description |
| --- | --- |
| `language` | Enter one of the following settings. (This parameter is case insensitive.)  - `ENGLISH` - `GERMAN` - `SPANISH` - `FRENCH` - `ITALIAN` - `JAPANESE` - `KOREAN` - `BRAZILIAN PORTUGUESE` - `SIMPLIFIED CHINESE` - `TRADITIONAL CHINESE` |

Examples

```
EXEC DBMS_MACADM.ADD_NLS_DATA('french');
```

### AUTHORIZE\_DATAPUMP\_USER Procedure

The `AUTHORIZE_DATAPUMP_USER` procedure authorizes a user to perform Oracle Data Pump operations when Oracle Database Vault is enabled. It applies to both the `expdp` and `impdp` utilities. See ["Granting a Database Administrator Authorization to Use Oracle Data Pump"](dba.md) for full usage information, including the levels of additional authorization the user must have to use Oracle Data Pump in an Oracle Database Vault environment.

Syntax

```
DBMS_MACADM.AUTHORIZE_DATAPUMP_USER(
  user_name      IN VARCHAR2,
  schema_name    IN VARCHAR2 DEFAULT NULL,
  table_name     IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 12-65 AUTHORIZE\_DATAPUMP\_USER

| Parameter | Description |
| --- | --- |
| `user_name` | Name of the Oracle Data Pump user to whom you want to grant authorization.  To find a list of users who have privileges to use Oracle Data Pump (that is, the `EXP_FULL_DATABASE` and `IMP_FULL_DATABASE` roles), query the `DBA_ROLE_PRIVS` data dictionary view as follows:  ``` SELECT GRANTEE, GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE LIKE '%FULL%' ``` |
| `schema_name` | Name of the database schema that the Oracle Data Pump user must export or import. If you omit this parameter, then the user is granted global authorization to export and import any schema in the database. In this case, ensure the user has been granted the `DV_OWNER` or `DV_ADMIN` role. |
| `table_name` | Name of the table within the schema specified by the `schema_name` parameter. If you omit this parameter, then the user you specified can export and import all tables within the schema specified by the `schema_name` parameter. |

Examples

```
EXEC DBMS_MACADM.AUTHORIZE_DATAPUMP_USER('DP_MGR');

EXEC DBMS_MACADM.AUTHORIZE_DATAPUMP_USER('DP_MGR', 'HR');

EXEC DBMS_MACADM.AUTHORIZE_DATAPUMP_USER('DP_MGR', 'HR', 'EMPLOYEES');
```

### AUTHORIZE\_SCHEDULER\_USER Procedure

The `AUTHORIZE_SCHEDULER_USER` procedure grants a user authorization to schedule database jobs when Oracle Database Vault is enabled. This authorization applies to anyone who has privileges to schedule database jobs. These privileges include any of the following: `CREATE JOB`, `CREATE ANY JOB`, `CREATE EXTERNAL JOB`, `EXECUTE ANY PROGRAM`, `EXECUTE ANY CLASS`, `MANAGE SCHEDULER`. See ["Scheduling Database Jobs in an Oracle Database Vault Environment"](dba.md) full usage information, including the levels of authorization the user must have to schedule database jobs in an Oracle Database Vault environment.

Syntax

```
DBMS_MACADM.AUTHORIZE_SCHEDULER_USER(
  user_name      IN VARCHAR2,
  schema_name    IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 12-66 AUTHORIZE\_SCHEDULER\_USER

| Parameter | Description |
| --- | --- |
| `user_name` | Name of the user to whom you want to grant authorization.  To find a list of users who have privileges to schedule jobs, query the `DBA_SYS_PRIVS` data dictionary view for users who have privileges to schedule database jobs. See Step [2](dba.md) in ["Granting a Database Administrator Authorization to Use Oracle Data Pump"](dba.md). |
| `schema_name` | Name of the database schema for which a job will be scheduled. If you omit this parameter, then the user is granted global authorization to schedule a job for any schema in the database. |

Examples

The following example authorizes the user `JOB_MGR` to run a job under any schema.

```
EXEC DBMS_MACADM.AUTHORIZE_SCHEDULER_USER('JOB_MGR');
```

This example authorizes user `JOB_MGR` to run a job under the `HR` schema only.

```
EXEC DBMS_MACADM.AUTHORIZE_SCHEDULER_USER('JOB_MGR', 'HR');
```

### UNAUTHORIZE\_DATAPUMP\_USER Procedure

The `UNAUTHORIZE_DATAPUMP_USER` procedure revokes the authorization that was granted by the `AUTHORIZE_DATAPUMP_USER` procedure. When you run this procedure, ensure that its settings correspond exactly to the equivalent `AUTHORIZE_DATAPUMP_USER` procedure.

For example, the following two procedures will work because the parameters are consistent:

```
EXEC DBMS_MACADM.AUTHORIZE_DATAPUMP_USER('DP_MGR');

EXEC DBMS_MACADM.UNAUTHORIZE_DATAPUMP_USER('DP_MGR');
```

However, because the parameters in the following procedures are not consistent, the `UNAUTHORIZE_DATAPUMP_USER` procedure will not work:

```
EXEC DBMS_MACADM.AUTHORIZE_DATAPUMP_USER('JSMITH');

EXEC DBMS_MACADM.UNAUTHORIZE_DATAPUMP_USER('JSMITH', 'HR');
```

Syntax

```
DBMS_MACADM.UNAUTHORIZE_DATAPUMP_USER(
  user_name      IN VARCHAR2,
  schema_name    IN VARCHAR2 DEFAULT NULL,
  table_name     IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 12-67 UNAUTHORIZE\_DATAPUMP\_USER

| Parameter | Description |
| --- | --- |
| `user_name` | Name of the Oracle Data Pump user from whom you want to revoke authorization.  To find a list of users and authorizations from the `AUTHORIZE_DATAPUMP_USER` procedure, query the `DVSYS.DBA_DV_RULE_SET` data dictionary view as follows:  ``` SELECT RULE_EXPR FROM DVSYS.DBA_DV_RULE_SET WHERE RULE_SET_NAME = 'Allow Oracle Data Pump Operation'; ``` |
| `schema_name` | Name of the database schema that the Oracle Data Pump user is authorized to export or import. |
| `table_name` | Name of the table within the schema specified by the `schema name` parameter. |

Examples

```
EXEC DBMS_MACADM.UNAUTHORIZE_DATAPUMP_USER('JSMITH');

EXEC DBMS_MACADM.UNAUTHORIZE_DATAPUMP_USER('JSMITH', 'HR');

EXEC DBMS_MACADM.UNAUTHORIZE_DATAPUMP_USER('JSMITH', 'HR', 'SALARY');
```

### UNAUTHORIZE\_SCHEDULER\_USER Procedure

The `UNAUTHORIZE_SCHEDULER_USER` procedure revokes the authorization that was granted by the `AUTHORIZE_SCHEDULER_USER` procedure. When you run this procedure, ensure that its settings correspond exactly to the equivalent `AUTHORIZE_SCHEDULER_USER` procedure.

For example, the following two procedures will work because the parameters are consistent:

```
EXEC DBMS_MACADM.AUTHORIZE_SCHEDULER_USER('JOB_MGR');

EXEC DBMS_MACADM.UNAUTHORIZE_SCHEDULER_USER('JOB_MGR');
```

However, because the parameters in the following procedures are not consistent, the `UNAUTHORIZE_SCHEDULER_USER` procedure will not work:

```
EXEC DBMS_MACADM.AUTHORIZE_SCHEDULER_USER('JOB_MGR');

EXEC DBMS_MACADM.UNAUTHORIZE_SCHEDULER_USER('JOB_MGR', 'HR');
```

Syntax

```
DBMS_MACADM.UNAUTHORIZE_SCHEDULER_USER
  user_name      IN VARCHAR2,
  schema_name    IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 12-68 UNAUTHORIZE\_SCHEDULER\_USER

| Parameter | Description |
| --- | --- |
| `user_name` | Name of the job scheduling user from whom you want to revoke authorization.  To find a list of users and authorizations from the `AUTHORIZE_SCHEDULER_USER` procedure, query the `DVSYS.DBA_DV_RULE_SET` data dictionary view as follows:  ``` SELECT RULE_EXPR FROM DVSYS.DBA_DV_RULE_SET WHERE RULE_SET_NAME = 'Allow Scheduler Job'; ``` |
| `schema_name` | Name of the database schema for which the user is authorized to schedule jobs. |

Examples

```
EXEC DBMS_MACADM.UNAUTHORIZE_SCHEDULER_USER('JOB_MGR');

EXEC DBMS_MACADM.UNAUTHORIZE_SCHEDULER_USER('JOB_MGR', 'HR');
```