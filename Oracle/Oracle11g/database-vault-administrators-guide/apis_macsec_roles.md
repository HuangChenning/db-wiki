---
title: Using the DBMS_MACSEC_ROLES Package
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/apis_macsec_roles.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 13 Using the DBMS\_MACSEC\_ROLES Package

This chapter contains:

## About the DBMS\_MACSEC\_ROLES Package

You can modify your applications to use the procedures within the `DBMS_MACSEC_ROLES` package to check the authorization for a user or to set an Oracle Database Vault secure application role. The `DBMS_MACSEC_ROLES` package is available to all users.

[Chapter 8, "Configuring Secure Application Roles for Oracle Database Vault,"](cfseappr.md) describes secure application roles in detail. See also [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for a set of general-purpose utility procedures that you can use with the secure application role procedures.

Table 13-1 lists the `DBMS_MACSEC_ROLES` package function and procedure.

Table 13-1 DBMS\_MACSEC\_ROLES Oracle Label Security Configuration Procedures

| Function or Procedure | Description |
| --- | --- |
| CAN\_SET\_ROLE Function | Checks whether the user invoking the method is authorized to use the specified Oracle Database Vault secure application role. Returns a `BOOLEAN` value. |
| SET\_ROLE Procedure | Issues the `SET ROLE` statement for an Oracle Database Vault secure application role. |

## CAN\_SET\_ROLE Function

The `CAN_SET_ROLE` function checks whether the user invoking the method is authorized to use the specified Oracle Database Vault secure application role.

Syntax

```
DBMS_MACSEC_ROLES.CAN_SET_ROLE(
  p_role IN VARCHAR2)
RETURN BOOLEAN;
```

Parameters

Table 13-2 CAN\_SET\_ROLE Parameter

| Parameter | Description |
| --- | --- |
| `p_role` | Role name.  To find existing secure application roles in the current database instance, query the `DVSYS.DBA_DV_ROLE` view, described in ["DVSYS.DBA\_DV\_ROLE View"](views.md). |

Example

```
SET SERVEROUTPUT ON
BEGIN
 IF DBMS_MACSEC_ROLES.CAN_SET_ROLE('SECTOR2_APP_MGR')
  THEN DBMS_OUTPUT.PUT_LINE('''SECTOR2_APP_MGR'' can be enabled.');
 END IF;
END;
/
```

## SET\_ROLE Procedure

The `SET_ROLE` procedure issues the `SET ROLE` PL/SQL statement for specified roles, including both Oracle Database Vault secure application roles and regular Oracle Database roles. This procedure sets an Oracle Database Vault secure application role only if the rule set that is associated with the role evaluates to true.

Syntax

```
DBMS_MACSEC_ROLES.SET_ROLE(
  p_role IN VARCHAR2);
```

Parameters

Table 13-3 SET\_ROLE Parameter

| Parameter | Description |
| --- | --- |
| `p_role` | Role names. You can enter multiple roles, including secure application roles and regular roles.  To find existing secure application roles in the current database instance, query the `DVSYS.DBA_DV_ROLE` view, described in ["DVSYS.DBA\_DV\_ROLE View"](views.md).  To find all of the existing roles in the database, query the `DBA_ROLES` data dictionary view, described in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4220.htm#REFRN23231). |

Example

```
EXEC DBMS_MACSEC_ROLES.SET_ROLE('SECTOR2_APP_MGR, APPS_MGR');
```

You can enter the name of the role in any case (for example, `Sector2_APP_MGR`).