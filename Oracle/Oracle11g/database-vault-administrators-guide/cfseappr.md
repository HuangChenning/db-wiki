---
title: "Configuring Secure Application Roles for Oracle Database Vault"
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/cfseappr.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 8 Configuring Secure Application Roles for Oracle Database Vault

This chapter contains:

## What Are Secure Application Roles in Oracle Database Vault?

In Oracle Database Vault, you can create a secure application role that you enable with an Oracle Database Vault rule set. Regular Oracle Database secure application roles are enabled by custom PL/SQL procedures. You use secure application roles to prevent users from accessing data from outside an application. This forces users to work within the framework of the application privileges that have been granted to the role.

The advantage of basing database access for a role on a rule set is that you can store database security policies in one central place, as opposed to storing them in all your applications. Basing the role on a rule set provides a consistent and flexible method to enforce the security policies that the role provides. In this way, if you must update the security policy for the application role, you do it in one place, the rule set. Furthermore, no matter how the user connects to the database, the result is the same, because the rule set is bound to the role. All you need to do is to create the role and then associate it with a rule set. The associated rule set validates the user who is trying to enable the role.

You can run reports on secure application roles that you create in Oracle Database Vault. See "Related Reports and Data Dictionary View" for more information.

This chapter explains how to configure secure application roles by using Oracle Database Vault Administrator. To configure secure application roles by using the PL/SQL interfaces and packages provided by Oracle Database Vault, refer to the following chapters:

- [Chapter 12, "Using the DBMS\_MACADM Package"](apis_dbms_macadm.md)
- [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces"](plsql_interfaces.md)

## Creating and Editing Secure Application Roles

Follow these steps:

1. Create a rule set that contains at least one rule to set the conditions for allowing or disallowing the user to enable the role.
	When you create the underlying rule for the rule set, remember that the rule should validate the user who is trying to enable the role. The rule should validate the user who is trying to log in. See [Chapter 5, "Configuring Rule Sets,"](cfrulset.md) for more information about rule sets.
2. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
3. In the Administration page, under Database Vault Feature Administration, click Secure Application Roles.
4. In the Secure Application Roles page:
	- To create a new secure application role, click Create.
		- To edit an existing secure application role, select it from the list and then click Edit.
		Remember that you can modify an existing secure application role only if it has been created in Oracle Database Vault. You cannot modify secure application roles or database roles that have been created outside of Oracle Database Vault. If you want to modify an existing Oracle Database role so that it can work with Oracle Database Vault, create a new secure application role in Oracle Database Vault and then grant the existing role to the secure application role. For example, in SQL\*Plus:
		```
		GRANT myExistingDBrole TO myDVrole;
		```
		After you create a new secure application role, you must modify your code to use this new role. You can use `DBMS_MACSEC_ROLES.SET_ROLE` in your application code to accomplish this. See ["SET\_ROLE Procedure"](apis_macsec_roles.md) for more information about the `SET_ROLE` function.
5. In the Create (or Edit) Role page, enter the following settings and then click OK.
	- General
		- Rule Set

General

Enter the following settings:

- Role: Enter the name using no more than 30 characters, with no spaces. Preferably, enter the role name in upper case letters, though you are not required to do so. Ensure that this name follows the standard Oracle naming conventions for role creation using the `CREATE ROLE` statement, described in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm). This attribute is mandatory.
- Status: Select either Enabled or Disabled to enable or disable the secure application role during run time. The default is Enabled. This attribute is mandatory.
	- Enabled: Enables the role to be available for use. That is, users are allowed to call the `DBMS_MACSEC_ROLES.SET_ROLE` function to try to enable the role. Note that whether or not the role will be enabled depends on the evaluation result of the associated rule set.
		See ["SET\_ROLE Procedure"](apis_macsec_roles.md) for more information about this function.
		- Disabled: Disables the role from being available for use. The `DBMS_MACSEC_ROLES.SET_ROLE` function will not be able to enable the role.
	See ["Oracle Database Vault PL/SQL Packages"](plsql_interfaces.md) for more information about the `DBMS_MACSEC_ROLES.SET_ROLE` function.

Rule Set

From the list, select the rule set that you want to associate with the secure application role. This attribute is mandatory.

When calling `DBMS_MACSEC_ROLES.SET_ROLE`, if the rule set evaluates to true, then Oracle Database Vault sets the role for the database session. If the rule set evaluates to false, then the role is not set.

See [Chapter 5, "Configuring Rule Sets,"](cfrulset.md) for more information about rule sets.

See Also:

["Propagating Oracle Database Vault Policies to Other Databases"](dba.md)

## Securing a Secure Application Role

Users who have database administrative privileges may try to use the `DROP ROLE` SQL statement to delete secure application roles that were created using Oracle Database Vault.

Whenever an Oracle Database Vault secure application role has been created, Database Vault adds the secure application role to the Database Vault realm. This prevents the database administrator from deleting the secure application role.

## Deleting a Secure Application Role

Before you delete a secure application role, you can locate the various references to it by querying the role-related Oracle Database Vault views. See [Chapter 16, "Oracle Database Vault Data Dictionary Views,"](views.md) for more information.

To delete a secure application role:

1. Check and modify any applications that may be using the secure application role that you want to delete.
2. In the Oracle Database Vault Administration page, select Secure Application Roles.
3. In the Secure Application Roles page, select the role that you want to remove.
4. Click Remove.
5. In the Confirmation page, click Yes.

## How Secure Application Roles Work

The process flow for a secure application role that is managed by Oracle Database Vault is as follows:

1. Create or update the role either in Oracle Database Vault Administrator or by using the secure application role-specific functions in the `DBMS_MACADM` package.
	See ["Secure Application Role Procedures Within DBMS\_MACADM"](apis_dbms_macadm.md) for more information.
2. Modify your application to call the role, by using the `DBMS_MACSEC_ROLES.SET_ROLE` function.
	See ["SET\_ROLE Procedure"](apis_macsec_roles.md) for more information.
3. Oracle Database Vault then evaluates the rule set associated with the secure application role.
	If the rule set evaluates to true, then Oracle Database Vault enables the role for the current session. If the rule set evaluates to false, the role is not enabled. In either case, Oracle Database Vault processes the associated auditing and custom event handlers for the rule set associated with the secure application role.

## Tutorial: Granting Access with Database Vault Secure Application Roles

This section contains:

- About This Tutorial
- Step 1: Create Users for This Tutorial
- Step 2: Enable the OE User Account
- Step 3: Create the Rule Set and Its Rules
- Step 4: Create the Database Vault Secure Application Role
- Step 5: Grant the SELECT Privilege to the Secure Application Role
- Step 6: Test the Database Vault Secure Application Role
- Step 7: Remove the Components for This Tutorial

### About This Tutorial

In this tutorial, you restrict the `SELECT` SQL statement on the `ORDERS` table in the `OE` schema to a specific set of users. Furthermore, these users can only perform these statements on the `OE.ORDERS` table from within the office, not from a remote connection. To accomplish this, you create an Oracle Database Vault secure application role that is enabled for the user only if the user passes the checks enforced by the rule set that you associate with the secure application role.

### Step 1: Create Users for This Tutorial

1. Log in to SQL\*Plus as a user who has been granted the `DV_ACCTMGR` role.
	For example:
	```
	sqlplus amalcolm_dvacctmgr
	Enter password: password
	```
2. Create the following user accounts:
	```
	CREATE USER eabel IDENTIFIED BY password;
	CREATE USER ahutton IDENTIFIED BY password;
	CREATE USER ldoran IDENTIFIED BY password;
	```
	Replace `password` with a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for the minimum requirements for creating passwords.
3. Connect as `SYS` using the `SYSDBA` privilege, and then grant these users the `CREATE SESSION` privilege.
	```
	CONNECT SYS AS SYSDBA
	Enter password: password
	GRANT CREATE SESSION TO eabel, ahutton, ldoran;
	```

### Step 2: Enable the OE User Account

1. In SQL\*Plus, connect as the `DV_ACCTMGR` user.
	For example:
	```
	CONNECT amalcolm_dvacctmgr
	Enter password: password
	```
2. Check the account status of the `OE` account.
	```
	SELECT USERNAME, ACCOUNT_STATUS FROM DBA_USERS WHERE USERNAME = 'OE';
	```
3. If the `OE` account is locked and expired, unlock it and assign it a new password.
	```
	ALTER USER OE ACCOUNT UNLOCK IDENTIFIED BY password;
	```

### Step 3: Create the Rule Set and Its Rules

1. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. In the Administration page, select Rule Sets.
	The Rule Sets page appears.
3. Click Create.
	The Create Rule Set page appears.
4. Enter the following information:
	- Name: `Can Modify Orders`
		- Description: `Rule set to control who can modify orders in the OE.ORDERS table`
5. Leave the remaining settings and their defaults, and then click OK.
6. In the Rule Sets page, select the Can Modify Orders rule set, and then click Edit.
	The Edit Rule Set: Can Modify Orders page appears.
7. Scroll to the bottom of the page and under Rules Associated To The Rule Set, click Create.
8. Create the following two rules:
	|  | Rule Name | Rule Expression |
	| --- | --- | --- |
	|  | `Check IP Address` | `DVF.F$CLIENT_IP = '192.0.2.12'` |
	|  | `Check Session User` | `DVF.F$SESSION_USER IN ('EABEL', 'AHUTTON')` |
	For the Check IP Address rule, replace 123.45.67.89 with the IP address for your own computer. In a real-world scenario, you would create an expression that includes all the IP addresses for the users who should be allowed access.
	Both of these rules use the default factors Client\_IP and Session\_User. See ["Default Factors"](cfgfact.md) for more information about these factors. If these factors have been removed or modified, you can use the following rule expressions instead:
	- Check IP Address: `UPPER(SYS_CONTEXT('USERENV','IP_ADDRESS')) = '192.0.2.12'`
		- Check Session User: `UPPER(SYS_CONTEXT('USERENV','SESSION_USER')) IN ('EABEL', 'AHUTTON')`
9. Ensure that the Status setting for the Can Modify Orders table is set to Enabled and Evaluation Options is set to All True.
10. Click OK.

### Step 4: Create the Database Vault Secure Application Role

1. In Oracle Database Vault, return to the Administration page.
2. Under Administration, select Secure Application Roles.
	The Secure Application Roles page appears.
3. Click Create.
	The Create Role page appears.
4. In the Role box, enter `ORDERS_MGMT` to name the role.
5. Under Rule Set, select Can Modify Orders.
6. Click OK.

At this stage, the Database Vault secure application role and its associated rule set are created, though the role does not yet have any privileges.

### Step 5: Grant the SELECT Privilege to the Secure Application Role

1. In SQL\*Plus, connect as user `OE`.
	```
	CONNECT OE
	Enter password: password
	```
2. Grant the `SELECT` privilege to the `ORDERS_MGMT` Database Vault Secure application role.
	```
	GRANT SELECT ON ORDERS TO ORDERS_MGMT;
	```

### Step 6: Test the Database Vault Secure Application Role

1. In SQL\*Plus, connect directly to the database as user `eabel`.
	```
	CONNECT eabel@orcl
	Enter password: password
	```
	Replace `orcl` with the name of your database instance.
2. Set the `ORDERS_MGMT` role.
	```
	EXEC DBMS_MACSEC_ROLES.SET_ROLE('ORDERS_MGMT');
	```
	Typically, you would embed this call in the application that the user logs in to.
3. Select from the `OE.ORDERS` table.
	```
	SELECT COUNT(*) FROM OE.ORDERS;
	```
	The following output should appear:
	```
	COUNT(*)
	----------
	       105
	```
	Because user `eabel` is logging directly into the database from the correct IP address and is listed as a valid session user, she can select from the `OE.ORDERS` table. If user `ahutton` logs in to SQL\*Plus in the same manner, she also can select from the `OE.ORDERS` table.
4. Reconnect as user `eabel` without specifying the database instance, and then try to select from the `OE.ORDERS` table again.
	```
	CONNECT eabel
	Enter password: password
	EXEC DBMS_MACSEC_ROLES.SET_ROLE('ORDERS_MGMT');
	```
	The following output should appear:
	```
	Error at line 1: 
	ORA-47305: Rule Set Violation on SET ROLE (Can Modfiy Orders)
	...
	```
	Next:
	```
	SELECT COUNT(*) FROM OE.ORDERS;
	```
	The following output should appear:
	```
	ERROR at line 1:
	ORA-00942: table or view does not exist
	```
	Even though user `eabel` is a valid user, she has violated the Check IP Address rule in the rule set, so she is not granted the `ORDERS_MGMT` role. The only way for the IP address to be recognized is to connect by specifying the database instance, as user `eabel` did in Step 1. (For an explanation about how this works, see Step [7](cfgfact.md) in ["Step 3: Map the Domain Factor Identities to the Client\_IP Factor"](cfgfact.md), in [Chapter 7](cfgfact.md).)
5. Connect as user `ldoran` and then enter the following statements:
	```
	EXEC DBMS_MACSEC_ROLES.SET_ROLE('ORDERS_MGMT');
	SELECT COUNT(*) FROM OE.ORDERS;
	```
	Because user `ldoran` is not a valid user, she is not granted the `ORDERS_MGMT` role. Therefore, she cannot select from the `OE.ORDERS` table.

### Step 7: Remove the Components for This Tutorial

1. Log into SQL\*Plus as the `DV_OWNER` or `DV_ADMIN` user.
	For example:
	```
	CONNECT lbrown_dvowner
	Enter password: password
	```
2. Delete the `ORDERS_MGMT` secure application role.
	```
	EXEC DBMS_MACADM.DELETE_ROLE('ORDERS_MGMT');
	```
3. Enter the following commands in the order shown to remove the Can Modify Orders rule set.
	```
	EXEC DBMS_MACADM.DELETE_RULE_FROM_RULE_SET('Can Modify Orders', 'Check IP Address');
	EXEC DBMS_MACADM.DELETE_RULE_FROM_RULE_SET('Can Modify Orders', 'Check Session User');
	EXEC DBMS_MACADM.DELETE_RULE('Check IP Address');
	EXEC DBMS_MACADM.DELETE_RULE('Check Session User');
	EXEC DBMS_MACADM.DELETE_RULE_SET('Can Modify Orders');
	COMMIT;
	```
4. Connect as the Database Vault Account Manager and drop the users.
	For example:
	```
	CONNECT amalcolm_dvacctmgr
	Enter password: password
	DROP USER eabel;
	DROP USER ahutton;
	DROP USER ldoran;
	```
5. If uneccessary, lock and expire the `OE` user account.
	```
	ALTER USER OE ACCOUNT LOCK PASSWORD EXPIRE;
	```

## How Secure Application Roles Affect Performance

You can check system performance by running tools such as Oracle Enterprise Manager (including Oracle Enterprise Manager Database Control, which is installed by default with Oracle Database), `Statspack`, and `TKPROF`. For more information about Oracle Enterprise Manager, see the Oracle Enterprise Manager documentation set. For information about Database Control, refer to its online Help. [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) describes the `Statspack` and `TKPROF` utilities.

## Related Reports and Data Dictionary View

Table 8-1 lists Oracle Database Vault reports that are useful for analyzing Oracle Database Vault secure application roles. See [Chapter 18, "Oracle Database Vault Reports,"](reports.md) for information about how to run these reports.

Table 8-1 Reports Related to Secure Application Roles

| Report | Description |
| --- | --- |
| ["Secure Application Role Audit Report"](reports.md) | Lists audit records generated by the Oracle Database Vault secure application role-enabling operation.  To generate this type of audit record, enable auditing for the rule set associated with the role. |
| ["Secure Application Configuration Issues Report"](reports.md) | Lists secure application roles that have nonexistent database roles, or incomplete or disabled rule sets |
| ["Rule Set Configuration Issues Report"](reports.md) | Lists rule sets that have no rules defined or enabled, which may affect the secure application roles that use them |
| ["Powerful Database Accounts and Roles Reports"](reports.md) | Provides information about powerful database accounts and roles |

You can use the `DVSYS.DBA_DV_ROLE` data dictionary view to find the Oracle Database Vault secure application roles used in privilege management. See ["DVSYS.DBA\_DV\_ROLE View"](views.md) for more information.