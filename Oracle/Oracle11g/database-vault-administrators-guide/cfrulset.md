---
title: Configuring Rule Sets
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/cfrulset.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 5 Configuring Rule Sets

This chapter contains:

## What Are Rule Sets?

A rule set is a collection of one or more rules that you can associate with a realm authorization, factor assignment, command rule, or secure application role. The rule set evaluates to true or false based on the evaluation of each rule it contains and the evaluation type (All True or Any True). A rule within a rule set is a PL/SQL expression that evaluates to true or false. You can create a rule and add the rule to multiple rule sets.

You can use rule sets to accomplish the following activities:

- As a further restriction to realm authorization, to define the conditions under which realm authorization is active
- To define when to allow a command rule
- To enable a secure application role
- To define when to assign the identity of a factor

When you create a rule set, Oracle Database Vault makes it available for selection when you configure the authorization for a realm, command rule, factor, or secure application role.

You can run reports on the rule sets that you create in Oracle Database Vault. See "Related Reports and Data Dictionary Views" for more information.

This chapter explains how to configure rule sets by using Oracle Database Vault Administrator. To configure rule sets by using the PL/SQL interfaces and packages provided by Oracle Database Vault, refer to the following chapters:

- [Chapter 12, "Using the DBMS\_MACADM Package"](apis_dbms_macadm.md)
- [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces"](plsql_interfaces.md)

## Default Rule Sets

Oracle Database Vault provides a set of default rules sets that you can customize for your needs. The default rule sets are as follows:

- Allow Sessions: Controls the ability to create a session in the database. This rule set enables you to add rules to control database logins using the CONNECT command rule. The CONNECT command rule is useful to control or limit `SYSDBA` access to programs that require its use. This rule set is not populated.
- Allow System Parameters: Controls the ability to set system initialization parameters. For Oracle Database 11g Release 2 (11.2), the Allow Fine Grained Control of System Parameters rule set replaces this rule set, but it is still supported for backward compatibility. The Allow System Parameters rule set is not associated with any commands, but its rules are still available and can be used with any custom rule set. Oracle recommends that you use the Allow Fine Grained Control of System Parameters rule set.
- Allow Fine Grained Control of System Parameters: Provides a very flexible, fine-grained control over initialization parameters that manage system security, dump or destination location, backup and restore settings, optimizer settings, PL/SQL debugging, and security parameters. It affects the following initialization parameters, based on the associated rules of this rule set:
	- Are System Security Parameters Allowed rule: Cannot set `O7_DICTIONARY_ACCESSIBILITY`
		- Are Dump or Dest Parameters Allowed rule: Cannot set the following parameters:
		|  | `BACKGROUND_DUMP_DEST` | `LOG_ARCHIVE_DEST_STATE_` `n` |
		| --- | --- | --- |
		|  | `CORE_DUMP_DEST` | `LOG_ARCHIVE_DUPLEX_DEST` |
		|  | `DB_CREATE_ONLINE_LOG_DEST` | `LOG_ARCHIVE_FORMAT` |
		|  | `DB_RECOVERY_FILE_DEST` | `LOG_ARCHIVE_LOCAL_FIRST` |
		|  | `DB_RECOVERY_FILE_DEST_SIZE` | `LOG_ARCHIVE_MAX_PROCESSES` |
		|  | `DIAGNOSTIC_DEST` | `LOG_ARCHIVE_MIN_SUCCEED_DEST` |
		|  | `DUMP_DATAFILE` | `LOG_ARCHIVE_TRACE` |
		|  | `LOG_ARCHIVE_CONFIG` | `MAX_DUMP_FILE_SIZE` |
		|  | `LOG_ARCHIVE_DEST` | `STANDBY_ARCHIVE_DEST` |
		|  | `LOG_ARCHIVE_DEST_` `n` | `USER_DUMP_DEST` |
		- Are Backup Restore Parameters Allowed rule: Cannot set `RECYCLEBIN` (but does not prevent disabling the recycle bin)
		- Are Database File Parameters Allowed rule: Can set `CONTROL_FILE_RECORD_KEEP_TIME`, `CONTROL_FILES`
		- Are Optimizer Parameters Allowed rule: Cannot set `OPTIMIZER_SECURE_VIEW_MERGING`
		- Are PL-SQL Parameters Allowed rule: Cannot set `UTL_FILE_DIR`, `PLSQL_DEBUG`
		- Are Security Parameters Allowed rule: Cannot set the following:
		|  | `AUDIT_SYS_OPERATIONS = FALSE` | `OS_ROLES` |
		| --- | --- | --- |
		|  | `AUDIT_TRAIL = NONE` or `FALSE` | `REMOTE_OS_ROLES` |
		|  | `AUDIT_SYSLOG_LEVEL` | `SQL92_SECURITY` |
	See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams_part.htm#REFRN001) for detailed information about initialization parameters.
- Can Grant VPD Administration: Controls the ability to grant the `GRANT EXECUTE` or `REVOKE EXECUTE` privileges on the Oracle Virtual Private Database `DBMS_RLS` package, with the `GRANT` and `REVOKE` statements.
- Allow Oracle Data Pump Operation: Contains rules that describe each user authorization that was created by the `DBMS_MACADM.AUTHORIZE_DATAPUMP_USER` procedure. The rule includes the user login account and the level of access the user is allowed: the entire database, a schema within the database, or a table within this schema. When a user attempts to perform an Oracle Data Pump export or import operation, Oracle Database Vault checks the authorizations defined in this rule set. If the user's authorizations are not defined here, then he or she is not permitted to perform the export or import operation.
	See ["Using Oracle Data Pump in an Oracle Database Vault Environment"](dba.md) for more information.
- Allow Scheduler Job: Contains rules that describe each user authorization that was created by the `DBMS_MACADM.AUTHORIZE_SCHEDULER_USER` procedure. If you do not define the user's authorizations here, then he or she still can create a job. But if the user runs a job under another schema, the job will fail when this job accesses Oracle Database Vault-protected objects. The rule includes the user login account and the level of access the user is allowed: the entire database or a schema within the database. When a user attempts to schedule a database job, Oracle Database Vault checks the authorizations defined in this rule set. If the user's authorizations are not defined here, then he or she is not permitted to create the job.
	See ["Scheduling Database Jobs in an Oracle Database Vault Environment"](dba.md) for more information.
- Can Maintain Accounts/Profiles: Controls the roles that manage user accounts and profiles, through the `CREATE USER`, `DROP USER`, `CREATE PROFILE`, `ALTER PROFILE`, or `DROP PROFILE` statements.
- Can Maintain Own Account: Allows the accounts with the `DV_ACCTMGR` role to manage user accounts and profiles with the `ALTER USER` statement. Also allows individual accounts to change their own password using the `ALTER USER` statement. See ["DV\_ACCTMGR Database Vault Account Manager Role"](db_objects.md) for more information about the `DV_ACCTMGR` role.
- Disabled: Convenience rule set to quickly disable security configurations like realms, command rules, factors, and secure application roles.
- Enabled: Convenience rule set to quickly enable system features.

## Creating a Rule Set

In general, to create a rule set, you first create the rule set itself, and then you edit the rule set to associate it with one or more rules. You can associate a new rule with the rule set, add existing rules to the rule set, or delete a rule association from the rule set.

See also the following sections:

- "Guidelines for Designing Rule Sets" for advice on designing rule sets
- ["Oracle Database Vault PL/SQL Rule Functions"](plsql_interfaces.md) for a set of functions that you can use in rule expressions
- ["Rule Set Configuration Issues Report"](reports.md) to check the configuration of the rule sets for your database

To create a rule set:

1. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. In the Administration page, under Database Vault Feature Administration, click Rule Sets.
3. In the Rule Sets page, click Create.
4. In the Create Rule Set page, enter the following settings, and then click OK:
	- General
		- Audit Options
		- Error Handling Options

General

Enter the following settings:

- Name: Enter a name for the rule set. It can contain up to 90 characters in mixed-case. Spaces are allowed. This attribute is mandatory.
	Oracle suggests that you start the name with a verb and complete it with the realm or command rule name to which the rule set is attached. For example:
	```
	Limit SQL*Plus access
	```
- Description: Enter a description of the functionality for the rule set. It can have up to 1024 characters in mixed-case. This attribute is optional.
	You may want to document the business requirement of the rule set. For example:
	```
	Rule to limit access to SQL*Plus
	```
- Status: Select either Enabled or Disabled to enable or disable the rule set during run time. Rule sets are enabled by default. This attribute is mandatory.
- Evaluation Options: If you plan to assign multiple rules to a rule set, select one of the following settings:
	- All True: Default. All rules in the rule set must evaluate to true for the rule set itself to evaluate to true.
		- Any True: At least one rule in the rule set must evaluate to true for the rule set itself to evaluate to true.
	If you want to determine how often a rule set is evaluated when it is accessed by a command rule, then you can use the `is_static` parameter of the `DBMS_MACADM.CREATE_RULE_SET` procedure. See ["CREATE\_RULE\_SET Procedure"](apis_dbms_macadm.md) for more information.

Audit Options

Select from the following options to generate an audit record for the rule set. Oracle Database Vault writes the audit trail to the `DVSYS.AUDIT_TRAIL$` system file, described in [Appendix A, "Auditing Oracle Database Vault."](audplcy.md)

This attribute is mandatory. The settings are:

- Audit Disabled: Does not create an audit record under any circumstances.
- Audit On Failure: Default. Creates an audit record when the rule set evaluates to false or one of the associated rules contains an invalid PL/SQL expression.
- Audit On Success or Failure: Creates an audit record whenever a rule set is evaluated.

For additional audit options, see ["CREATE\_RULE\_SET Procedure"](apis_dbms_macadm.md).

The Oracle Database Vault audit trail, written to the `DVSYS.AUDIT_TRAIL$` system table, contains the fields `RULE_SET_NAME` and `RULE_SET_ID`. These fields are populated when a rule set is associated with a realm authorization and a command authorization, and the rule set is configured to audit under some circumstances. See [Appendix A, "Auditing Oracle Database Vault,"](audplcy.md) for more information.

Error Handling Options

Enter the following settings to control the messaging to the database session when the rule set evaluates to false or one of the associated rules contains an invalid PL/SQL expression:

- Fail Options: Select either Show Error Message (the default) or Do Not Show Error Message.
	An advantage of selecting Do Not Show Error Message and then enabling auditing is that you can track the activities of a potential intruder. The audit report reveals the activities of the intruder, yet the intruder is unaware that you are doing this because he or she does not see any error messages.
- Fail Code: Enter a number in the ranges of -20000 to -20999 or 20000 to 20999. The error code is displayed with the Fail Message (created next) when the rule set evaluates to false or one of the associated rules contains an invalid PL/SQL expression. If you omit this setting, then Oracle Database Vault displays the following error code:
	```
	ORA-01031: Insufficient privileges
	```
- Fail Message: Enter a message, up to 80 characters in mixed-case, to associate with the fail code you specified under Fail Code. The error message is displayed when the rule set evaluates to false or one of the associated rules contains an invalid PL/SQL expression. If you do not specify an error message, then Oracle Database Vault displays a generic error message.
- Custom Event Handler Option: Select one of the following options to determine when to run the Custom Event Handler Logic (created next).
	- Handler Disabled: Default. Does not run any custom event method.
		- Execute On Failure: Runs the custom event method when the rule set evaluates to false or one of the associated rules contains an invalid PL/SQL expression.
		- Execute On Success: Runs the custom event method when the rule set evaluates to true.
	You can create a custom event method to provide special processing outside the standard Oracle Database Vault rule set auditing features. For example, you can use an event handler to initiate a workflow process or send event information to an external system.
- Custom Event Handler Logic: Enter a PL/SQL expression up to 255 characters in mixed-case. An expression may include any package procedure or standalone procedure. You can create your own expression or use the PL/SQL interfaces described in [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces."](plsql_interfaces.md)
	Write the expression as a fully qualified procedure (such as `schema`.`procedure_name`). Do not include complete SQL statements. If you are using application package procedures or standalone procedures, you must provide `DVSYS` with the `EXECUTE` privilege on the object. The procedure signature can be in one of the following two forms:
	- `PROCEDURE` `my_ruleset_handler(``p_ruleset_name` `IN VARCHAR2,` `p_ruleset_rules` `IN BOOLEAN)`: Use this form when the name of the rule set and its return value are required in the handler processing.
		- `PROCEDURE` `my_ruleset_handler`: Use this form when the name of the rule set and its return value are not required in the handler processing.
	When you define the expression in the user interface that uses one of these two formats, put the expression in the following form:
	```
	myschema.my_ruleset_handler
	```

After you create a rule set, you are ready to create rules to attach to the rule set. To do so, you edit the new rule set, and then define its rules.

## Configuring or Editing a Rule Set

To configure or edit a rule set:

1. In the Oracle Database Vault Administration page, select Rule Sets.
2. In the Rule Set page, select the rule set that you want to edit.
3. Click Edit.
4. Modify the rule set as necessary, and then click OK.

See Also:

- "Creating a Rule Set" to modify the settings created for a new rule set
- Creating a Rule to Add to a Rule Set to add or modify rule for the rule set

## Creating a Rule to Add to a Rule Set

After you create a new rule set, you can associate it with one or more rules. When you create a new rule, it is automatically added to the current rule set. You also can add existing rules to the rule set. Alternatively, you can omit adding rules to the rule set and use it as a template for rule sets you may want to create in the future.

The rule set evaluation depends on the evaluation of its rules using the Evaluation Options (All True or Any True). If a rule set is disabled, Oracle Database Vault evaluates the rule set to true without evaluating its rules.

See "How Rule Sets Work" for information on how rules are evaluated, how to nest rules, and how to create rules that exclude a particular user, such as a privileged user.

### Creating a New Rule

To create and add a rule to a rule set:

1. In the Oracle Database Vault Administration page, select Rule Sets.
2. In the Rule Sets page, select the rule set to which you want to create and add a rule, and then select Edit.
3. In the Edit Rule Set Page, scroll down to Rules Associated To The Rule Set and select Create.
4. In the Create Rule page, enter the following settings:
	- Name: Enter a name for the rule. Use up to 90 characters in mixed-case.
		Oracle suggests that you start the name with a verb and complete the name with the purpose of the rule. For example:
		```
		Prevent non-admin access to SQL*Plus
		```
		Because rules do not have a Description field, make the name explicit but be sure to not exceed over 90 characters.
		- Rule Expression: Enter a PL/SQL expression that fits the following requirements:
		- It is valid in a SQL `WHERE` clause.
				- It can be a freestanding and valid PL/SQL Boolean expression such as the following:
			```
			TO_CHAR(SYSDATE,'HH24') = '12'
			```
				- It must evaluate to a Boolean (`TRUE` or `FALSE`) value.
				- It must be no more than 255 characters long.
				- It can contain existing and compiled PL/SQL functions from the current database instance. Ensure that these are fully qualified functions (such as `schema`. `function_name`). Do not include complete SQL statements.
			If you want to use application package functions or standalone functions, you must grant the `DVSYS` account the `EXECUTE` privilege on the function. Doing so reduces the chances of errors when you add new rules.
				- Ensure that the rule works. You can test the syntax by running the following statement in SQL\*Plus:
			```
			SELECT rule_expression FROM DUAL;
			```
			For example, suppose you have created the following the rule expression:
			```
			SYS_CONTEXT('USERENV','SESSION_USER') != 'TSMITH'
			```
			You could test this expression as follows:
			```
			SELECT SYS_CONTEXT('USERENV','SESSION_USER') FROM DUAL;
			```
		See the following sections for functions that you can use in the rule set expression:
		- ["Oracle Database Vault PL/SQL Rule Functions"](plsql_interfaces.md)
				- [Chapter 12, "Using the DBMS\_MACADM Package"](apis_dbms_macadm.md)
				- [Chapter 14, "Using the DBMS\_MACUTL Package"](apis_dbms_macutl.md)
		For additional examples of expressions, see the rule defined in the rule sets provided with Oracle Database Vault. "Default Rule Sets" lists these rule sets.
5. Click OK.
	The Edit Rule Set page appears. By default, the new rule is added to the rule set.

Editing a Rule

The changes you make to a rule apply to all rule sets that include the rule.

To edit a rule:

1. In the Edit Rule Set page, scroll to Rules Associated To The Rule Set.
2. Select the rule you want to edit and click Edit.
3. In the Edit Rule page, modify the rule as necessary.
4. Click OK.

Removing a Rule from a Rule Set

Before you remove a rule from a rule set, you can locate the various references to it by querying the rules-related Oracle Database Vault views. See [Chapter 16, "Oracle Database Vault Data Dictionary Views,"](views.md) for more information.

To remove a rule from a rule set:

1. In the Edit Rule Set page, scroll to Rules Associated To The Rule Set.
2. Select the rule you want to delete and click Remove.
3. In the Confirmation page, click Yes.

After you remove the rule from the rule set, it still exists. If you want, you can associate it with other rule sets. If you want to delete the rule, use the `DBMS_MACADM.DELETE_RULE` function, described in ["Rule Set Procedures Within DBMS\_MACADM"](apis_dbms_macadm.md). For example, to delete the rule Night Shift, log in to SQL\*Plus as the Database Vault Owner and enter the following statement:

```
EXEC DBMS_MACADM.DELETE_RULE('Night Shift');
```

### Adding Existing Rules to a Rule Set

To add existing rules to a rule set:

1. In the Rule Sets page, select the rule set that you want to add rules to, and then select Edit.
2. Under Rules Associated To The Rule Set, select Add Existing Rules.
3. In the Add Existing Rules page, select the rules you want, and then click Move (or Move All, if you want all of them) to move them to the Selected Rules list.
	You can select multiple rules by holding down the Ctrl key as you click each rule.
4. Click OK.

## Deleting a Rule Set

Before you delete a rule set, you can locate the various references to it by querying the rules-related Oracle Database Vault views. See [Chapter 16, "Oracle Database Vault Data Dictionary Views,"](views.md) for more information.

To delete a rule set:

1. If other Database Vault objects, such as command rules, reference the rule set, then remove the reference.
	You can delete a rule set only if no other Database Vault objects are referencing it.
2. In the Oracle Database Vault Administration page, select Rule Sets.
3. In the Rule Set page, select the rule set that you want to remove.
4. Click Remove.
5. In the Confirmation page, click Yes.
	The rule set is deleted. However, the rules associated with the rule set are not deleted.

## How Rule Sets Work

This section describes how rule sets work in the following ways:

- How Oracle Database Vault Evaluates Rules
- Nesting Rules Within a Rule Set
- Creating Rules to Apply to Everyone Except One User

### How Oracle Database Vault Evaluates Rules

Oracle Database Vault evaluates the rules within a rule set as a collection of expressions. If you have set Evaluation Options to All True and if a rule fails the evaluation, then the evaluation stops at that point, instead of attempting to evaluate the rest of the rules in the rule set. Similarly, if Evaluation Options is set to Any True and if a rule evaluates to true, the evaluation stops at that point. If a rule set is disabled, Oracle Database Vault evaluates it to true without evaluating its rules.

### Nesting Rules Within a Rule Set

You can nest one or more rules within the rule set. For example, suppose you want to create a nested rule, Is Corporate Network During Maintenance, that performs the following two tasks:

- It limits table modifications only when the database session originates within the corporate network.
- It restricts table modifications during the system maintenance window scheduled between 10:00 p.m. and 10:59 p.m.

The rule definition would be as follows:

```
DVF.F$NETWORK = 'Corporate' AND TO_CHAR(SYSDATE,'HH24') between '22' AND '23'
```

You can create it using a factor function. See ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md) for more information. [Chapter 7](cfgfact.md) explains how to create factors.

### Creating Rules to Apply to Everyone Except One User

You can also create rules to apply to everyone except one user (for example, a privileged user). The rule definition for this type of rule can be as follows:

```
SYS_CONTEXT('USERENV','SESSION_USER') = 'SUPERADMIN_USER' OR additional_rule
```

If the current user is a privileged user, then the system evaluates the rule to true without evaluating `additional_rule`. If the current user is not a privileged user, then the evaluation of the rule depends on the evaluation of `additional_rule`.

## Tutorial: Creating an Email Alert for Security Violations

This section contains:

- About This Tutorial
- Step 1: Install and Configure the UTL\_MAIL PL/SQL Package
- Step 2: Create an Email Security Alert PL/SQL Procedure
- Step 3: Configure an Access Control List File for Network Services
- Step 4: Create a Rule Set and a Command Rule to Use the Email Security Alert
- Step 5: Test the Email Security Alert
- Step 6: Remove the Components for This Tutorial

### About This Tutorial

In the following tutorial, you create an email alert that is sent when a user attempts to alter a table outside a maintenance period. To do this, you must create a rule to set the maintenance period hours, attach this rule to a rule set, and then create a command rule to allow the user to alter the table. You then associate the rule set with this command rule, which then sends the email alert when the user attempts to use the `ALTER TABLE` SQL statement outside the maintenance period.

### Step 1: Install and Configure the UTL\_MAIL PL/SQL Package

1. Log in to SQL\*Plus as `SYS` using the `SYSDBA` privilege, and then install the `UTL_MAIL` package.
	```
	sqlplus sys as sysdba
	Enter password: password
	@$ORACLE_HOME/rdbms/admin/utlmail.sql
	@$ORACLE_HOME/rdbms/admin/prvtmail.plb
	```
	The `UTL_MAIL` package enables you to manage email. See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/u_mail.htm#ARPLS384) for more information about `UTL_MAIL`. However, be aware that currently, the `UTL_MAIL` PL/SQL package do not support SSL servers.
2. Check the current value of the `SMTP_OUT_SERVER` parameter, and make a note of this value so that you can restore it when you complete this tutorial.
	For example:
	```
	SHOW PARAMETER SMTP_OUT_SERVER
	```
	Output similar to the following appears:
	```
	NAME                    TYPE              VALUE
	----------------------- ----------------- ----------------------------------
	SMTP_OUT_SERVER         string            some_value.example.com
	```
3. Issue the following `ALTER SYSTEM` statement:
	```
	ALTER SYSTEM SET SMTP_OUT_SERVER="imap_mail_server.example.com";
	```
	Replace `imap_mail_server.example.com` with the name of your SMTP server, which you can find in the account settings in your email tool. Enclose these settings in quotation marks. For example:
	```
	ALTER SYSTEM SET SMTP_OUT_SERVER="my_imap_mail_server.example.com"
	```
4. Connect as `SYS` using the `SYSOPER` privilege and then restart the database.
	```
	CONNECT SYS/AS SYSOPER
	Enter password: password
	SHUTDOWN IMMEDIATE
	STARTUP
	```
5. Ensure that the `SMTP_OUT_SERVER` parameter setting is correct.
	```
	CONNECT SYS AS SYSDBA
	Enter password: password
	SHOW PARAMETER SMTP_OUT_SERVER
	```
	Output similar to the following appears:
	```
	NAME                    TYPE              VALUE
	----------------------- ----------------- ----------------------------------
	SMTP_OUT_SERVER         string            my_imap_mail_server.example.com
	```

### Step 2: Create an Email Security Alert PL/SQL Procedure

1. Ensure that you are connected as `SYS` using the `SYSDBA` privilege, and then grant the following privileges to a user who has been granted the `DV_OWNER` role.
	(Alternatively, you can select a user who has been granted the `DV_ADMIN` role, but for this tutorial, you will select a user who has the `DV_OWNER` role.)
	For example:
	```
	CONNECT SYS AS SYSDBA
	Enter password: password
	GRANT CREATE PROCEDURE, DROP ANY PROCEDURE TO lbrown_dvowner;
	GRANT EXECUTE ON UTL_TCP TO lbrown_dvowner;
	GRANT EXECUTE ON UTL_SMTP TO lbrown_dvowner;
	GRANT EXECUTE ON UTL_MAIL TO lbrown_dvowner;
	GRANT EXECUTE ON DBMS_NETWORK_ACL_ADMIN TO lbrown_dvowner;
	```
	The `UTL_TCP`, `UTL_SMTP`, `UTL_MAIL`, and `DBMS_NETWORK_ACL_ADMIN` PL/SQL packages will be used by the email security alert that you create.
2. Connect to SQL\*Plus as the `DV_OWNER` user.
	For example:
	```
	CONNECT lbrown_dvowner
	Enter password: password
	```
3. Create the following procedure:
	```
	CREATE OR REPLACE PROCEDURE email_alert AS
	msg varchar2(20000) := 'Realm violation occurred for the ALTER TABLE Command Security Policy rule set. The time is: '; 
	BEGIN
	  msg := msg||to_char(SYSDATE, 'Day DD MON, YYYY HH24:MI:SS'); 
	UTL_MAIL.SEND (
	    sender      => 'youremail@example.com',
	    recipients  => 'recipientemail@example.com',
	    subject     => 'Table modification attempted outside maintenance!',
	    message     => msg); 
	END email_alert;
	/
	```
	Replace `youremail@example.com` with your email address, and `recipientemail@example.com` with the email address of the person you want to receive the notification.
4. Grant the `EXECUTE` permission on this procedure to `DVSYS`.
	```
	GRANT EXECUTE ON email_alert TO DVSYS;
	```

### Step 3: Configure an Access Control List File for Network Services

Before you can use PL/SQL network utility packages such as `UTL_MAIL`, you must configure an access control list (ACL) file that enables fine-grained access to external network services. For detailed information about this topic, see [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG40012).

To configure an access control list for the email alert:

1. As the `DV_OWNER` user, in SQL\*Plus, create the following access control list and its privilege definitions.
	```
	BEGIN
	 DBMS_NETWORK_ACL_ADMIN.CREATE_ACL (
	  acl          => 'mail_server_permissions.xml', 
	  description  => 'Enables network permissions for the mail server',
	  principal    => 'LBROWN_DVOWNER',
	  is_grant     => TRUE, 
	  privilege    => 'connect');
	END;
	/
	```
	Ensure that you enter your exact user name for the principal setting, in upper-case letters. For this tutorial, enter the name of the Database Vault Owner account (for example, `LBROWN_DVOWNER`).
2. Assign the access control list to the outgoing SMTP network host for your email server.
	```
	BEGIN
	 DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL (
	  acl         => 'mail_server_permissions.xml',
	  host        => 'SMTP_OUT_SERVER_setting', 
	  lower_port  => port); 
	END;
	/
	```
	In this example:
	- `SMTP_OUT_SERVER_setting`: Enter the `SMTP_OUT_SERVER` setting that you set for the `SMTP_OUT_SERVER` parameter in "Step 1: Install and Configure the UTL\_MAIL PL/SQL Package". This setting should match exactly the setting that your email tool specifies for its outgoing server.
		- `port`: Enter the port number that your email tool specifies for its outgoing server. Typically, this setting is 25. Enter this value for both the `lower_port` and `upper_port` settings. (Currently, the `UTL_MAIL` package does not support SSL. If your mail server is an SSL server, then enter 25 for the port number, even if the mail server uses a different port number.)
3. Commit your changes to the database.
	```
	COMMIT;
	```
4. Test the settings that you have created so far.
	```
	EXEC EMAIL_ALERT;
	COMMIT;
	```
	SQL\*Plus should display a `PL/SQL procedure successfully completed` message, and in a moment, depending on the speed of your email server, you should receive the email alert.
	If you receive an `ORA-24247: network access denied by access control list (ACL)` error followed by `ORA-06512: at` `string` `line` `string` errors, then check the settings in the access control list file.

### Step 4: Create a Rule Set and a Command Rule to Use the Email Security Alert

1. As the `DV_OWNER` user, create the following rule set:
	```
	BEGIN
	 DBMS_MACADM.CREATE_RULE_SET(
	  rule_set_name    => 'ALTER TABLE Command Security Policy', 
	  description      => 'This rule set allows ALTER TABLE only during the 
	                       maintenance period.', 
	  enabled          => DBMS_MACUTL.G_YES,
	  eval_options     => DBMS_MACUTL.G_RULESET_EVAL_ALL ,
	  audit_options    => DBMS_MACUTL.G_RULESET_AUDIT_FAIL,,
	  fail_options     => DBMS_MACUTL.G_RULESET_FAIL_SILENT,
	  fail_message     => '',
	  fail_code        => NULL,
	  handler_options  => DBMS_MACUTL.G_RULESET_HANDLER_FAIL,
	  handler          => 'dbavowner.email_alert');
	END;
	/
	```
2. Create a rule similar to the following.
	For now, set the rule expression to be during the time you test it. For example, if you want to test it between 2 p.m. and 3 p.m., create the rule as follows:
	```
	BEGIN
	 DBMS_MACADM.CREATE_RULE(
	  rule_name  => 'Restrict Access to Maintenance Period', 
	  rule_expr  => 'TO_CHAR(SYSDATE,''HH24'') BETWEEN ''14'' AND ''15''');
	END;
	/
	```
	Ensure that you use two single quotation marks instead of double quotation marks for `HH24`, `14`, and `15`.
	You can check the system time on your computer by issuing the following SQL statement:
	```
	SELECT TO_CHAR(SYSDATE,'HH24') FROM DUAL;
	```
	Output similar to the following appears:
	```
	TO
	--
	14
	```
	Later on, when you are satisfied that the rule works, you can update it to a time when your site typically performs maintenance work (for example, between 7 p.m. and 10 p.m), as follows:
	```
	BEGIN
	 DBMS_MACADM.UPDATE_RULE(
	  rule_name  => 'Restrict Access to Maintenance Period', 
	  rule_expr  => 'TO_CHAR(SYSDATE,''HH24'') BETWEEN ''19'' AND ''22''');
	END;
	/
	```
3. Add the Restrict Access to Maintenance Period rule to the ALTER TABLE Command Security Policy rule set.
	```
	BEGIN
	 DBMS_MACADM.ADD_RULE_TO_RULE_SET(
	  rule_set_name => 'ALTER TABLE Command Security Policy', 
	  rule_name     => 'Restrict Access to Maintenance Period'); 
	END;
	/
	```
4. Create the following command rule:
	```
	BEGIN
	 DBMS_MACADM.CREATE_COMMAND_RULE(
	  command         => 'ALTER TABLE', 
	  rule_set_name   => 'ALTER TABLE Command Security Policy', 
	  object_owner    => 'SCOTT', 
	  object_name     => '%', 
	  enabled         => DBMS_MACUTL.G_YES);
	END; 
	/
	```
5. Commit these updates to the database.
	```
	COMMIT;
	```

### Step 5: Test the Email Security Alert

1. Connect to SQL\*Plus as user `SCOTT`.
	For example:
	```
	CONNECT SCOTT
	Enter password: password
	```
	If the `SCOTT` account is locked and expired, then a user with the `DV_ACCTMGR` role can unlock this account and create a new password as follows:
	```
	ALTER USER SCOTT ACCOUNT UNLOCK IDENTIFIED BY password;
	```
	Replace `password` with a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for the minimum requirements for creating passwords.
2. As the user `SCOTT`, create a test table.
	```
	CREATE TABLE mytest (col1 number);
	```
3. Change the system time on your computer to a time when the ALTER TABLE Command Security Policy rule set takes place (for example, between 2 p.m. and 3 p.m).
	UNIX: Log in as root and use the `date` command to set the time. For example, assuming the date today is December 14, 2011, you would enter the following:
	```
	su root
	Password: password
	date --set="14 DEC 2011 14:00:00"
	```
	Windows: Double-click the clock icon, which is typically at the lower right corner of the screen. In the Date and Time Properties window, set the time to 2 p.m., and then click OK.
4. Try altering the `my_test` table.
	```
	ALTER TABLE mytest ADD (col2 number);
	Table altered.
	```
	`SCOTT` should be able to alter the `mytest` table during this time.
5. Reset the system time to a time outside the Restrict Access to Maintenance Period time.
6. Log in as `SCOTT` and try altering the `my_test` table again.
	```
	CONNECT SCOTT
	Enter password: password
	ALTER TABLE mytest ADD (col3 number);
	```
	The following output should appear:
	```
	ORA-47400: Command Rule violation for ALTER TABLE on SCOTT.MYTEST
	```
	`SCOTT` cannot alter the `mytest` table. In a moment, you should receive an email with the subject header `Table modification attempted outside maintenance!` and with a message similar to the following:
	```
	Realm violation occurred for the ALTER TABLE Command Security Policy rule set. The time is: Wednesday 06 MAY, 2009 14:24:25
	```
7. Reset the system time to the correct time.

### Step 6: Remove the Components for This Tutorial

1. Connect to SQL\*Plus as the `DV_OWNER` user, and then in the order shown, drop the Oracle Database Vault rule components.
	```
	EXEC DBMS_MACADM.DELETE_RULE_FROM_RULE_SET('ALTER TABLE Command Security Policy', 'Restrict Access to Maintenance Period');
	EXEC DBMS_MACADM.DELETE_RULE('Restrict Access to Maintenance Period');
	EXEC DBMS_MACADM.DELETE_COMMAND_RULE('ALTER TABLE', 'SCOTT', '%');
	EXEC DBMS_MACADM.DELETE_RULE_SET('ALTER TABLE Command Security Policy');
	```
2. Drop the `email_alert` PL/SQL procedure.
	```
	DROP PROCEDURE email_alert;
	```
3. Remove the access control list.
	```
	EXEC DBMS_NETWORK_ACL_ADMIN.DROP_ACL ('email_alert_permissions.xml');
	```
4. Connect as user `SCOTT` and remove the `mytest` table.
	```
	CONNECT SCOTT
	Enter password: password
	DROP TABLE mytest;
	```
5. Connect as `SYS` using the `SYSDBA` privilege and then revoke the `EXECUTE` privilege on the `UTL_TCP`, `UTL_SMTP`, and `UTL_MAIL` PL/SQL packages from the `DV_OWNER` user.
	For example:
	```
	REVOKE EXECUTE ON UTL_TCP FROM lbrown_dvowner;
	REVOKE EXECUTE ON UTL_SMTP FROM lbrown_dvowner;
	REVOKE EXECUTE ON UTL_MAIL FROM lbrown_dvowner;
	REVOKE EXECUTE ON DBMS_NETWORK_ACL_ADMIN from lbrown_dvowner;
	```
6. Set the `SMTP_OUT_SERVER` parameter to its original value.
	For example:
	```
	ALTER SYSTEM SET SMTP_OUT_SERVER="some_value.example.com";
	```
7. Connect as `SYS` using the `SYSOPER` privilege and then restart the database.
	```
	CONNECT SYS/AS SYSOPER
	Enter password: password
	SHUTDOWN IMMEDIATE
	STARTUP
	```

## Tutorial: Configuring Two-Person Integrity, or Dual Key Security

This section contains:

- About This Tutorial
- Step 1: Create Users for This Tutorial
- Step 2: Create a Function to Check if User patch\_boss Is Logged In
- Step 3: Create Rules, a Rule Set, and a Command Rule to Control the Users' Access
- Step 4: Test the Users' Access
- Step 5: Remove the Components for This Tutorial

### About This Tutorial

In this tutorial, you configure a rule set that defines two-person integrity (TPI), also called dual key security, dual key connection, and two-man rule security. In this type of security, two users are required to authorize an action instead of one user. The idea is that one user provides a safety check for the other user before that user can proceed with a task. Two-person integrity provides an additional layer of security for actions that potentially can be dangerous. This type of scenario is often used for tasks such as database patch updates, which is what this tutorial will demonstrate. One user, `patch_user` must log in to perform a database patch upgrade, but the only way that he can do this is if his manager, `patch_boss` is already logged in. You will create a function, rules, a rule set, and a command rule to control `patch_user` 's ability to log in.

### Step 1: Create Users for This Tutorial

You must create the following two users for this tutorial:

- `patch_boss` acts in a supervisory role: If `patch_boss` is not logged in, then the `patch_user` user cannot log in.
- `patch_user` is the user who is assigned to perform the patch upgrade. However, for this tutorial, user `patch_user` does not actually perform a patch upgrade. He only attempts to log in.

To create the users:

1. Connect to SQL\*Plus as a user who has been granted the `DV_ACCTMGR` role.
	For example:
	```
	CONNECT amalcolm_dvacctmgr
	Enter password: password
	```
2. Create the following users.
	```
	CREATE USER patch_boss IDENTIFIED BY password;
	CREATE USER patch_user IDENTIFIED BY password;
	```
	Replace `password` with a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for the minimum requirements for creating passwords.
3. Connect as user `SYS` with the `SYSDBA` privilege and grant privileges to the `patch_boss` and `patch_user` users.
	```
	CONNECT SYS AS SYSDBA
	Enter password: password
	GRANT CREATE SESSION TO patch_boss, patch_user;
	```
4. Grant the following privileges to the `DV_OWNER` or `DV_ADMIN` user.
	For example:
	```
	GRANT CREATE PROCEDURE TO lbrown_dvowner;
	GRANT SELECT ON V_$SESSION TO lbrown_dvowner;
	```
	The `V_$SESSION` table is the underlying table for the `V$SESSION` dynamic view.

In a real-world scenario, you also would log in as the `DV_OWNER` user and grant the `DV_PATCH_ADMIN` role to user `patch_user` (but not to `patch_boss`). But because you are not really going to perform a database patch upgrade in this tutorial, you do not need to grant this role to user `patch_user`.

### Step 2: Create a Function to Check if User patch\_boss Is Logged In

The function that you must create, `check_boss_logged_in`, does just that: When user `patch_user` tries to log in to SQL\*Plus, it checks if user `patch_boss` is already logged in by querying the `V$SESSION` data dictionary view.

To create the `check_boss_logged_in` function:

1. As the `DV_OWNER` or `DV_ADMIN` user, create the `check_boss_logged_in` function as follows:
	```
	CREATE OR REPLACE FUNCTION check_boss_logged_in
	return varchar2
	authid definer as 
	 
	v_session_number number := 0;
	v_allow varchar2(10)    := 'TRUE';
	v_deny varchar2(10)     := 'FALSE';
	 
	BEGIN
	  SELECT COUNT(*) INTO v_session_number
	  FROM SYS.V_$SESSION
	  WHERE USERNAME = 'PATCH_BOSS'; -- Enter the user name in capital letters.
	 
	 IF v_session_number > 0
	  THEN RETURN v_allow;
	 ELSE
	  RETURN v_deny;
	 END IF;
	END check_boss_logged_in;
	/
	```
2. Grant the `EXECUTE` privilege on the `check_boss_logged_in` function to the `DVSYS` schema.
	```
	GRANT EXECUTE ON check_boss_logged_in to DVSYS;
	```

### Step 3: Create Rules, a Rule Set, and a Command Rule to Control the Users' Access

Next, you must create two rules, a rule set to which you will add them, and a command rule. The rule set triggers the `check_boss_logged_in` function when user `patch_user` tries to logs in to the database.

To create the rules and rule set:

1. Connect as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	For example:
	```
	CONNECT lbrown_dvowner
	Enter password: password
	```
2. Create the Check if Boss Is Logged In rule, which checks that the `patch_user` user is logged in to the database. In the definition, replace `lbrown_dvowner` with the name of the `DVOWNER` or `DV_ADMIN` user who created the `check_boss_logged_in` function.
	If the `check_boss_logged_in` function returns `TRUE` (that is, `patch_boss` is logged in to another session), then `patch_user` can log in.
	```
	BEGIN
	  DBMS_MACADM.CREATE_RULE(
	  rule_name => 'Check if Boss Is Logged In',
	  rule_expr => 'SYS_CONTEXT(''USERENV'',''SESSION_USER'') = ''PATCH_USER'' and lbrown_dvowner.check_boss_logged_in =  ''TRUE'' ');
	END;
	/
	```
	Enter the user name, `PATCH_USER`, in upper-case letters, which is how the `SESSION_USER` parameter stores it.
3. Create the Allow Connect for Other Database Users rule, which ensures that the user logged in (`patch_user`) is not user `patch_boss`. It also enables all other valid users to log in.
	```
	BEGIN
	 DBMS_MACADM.CREATE_RULE(
	  rule_name => 'Allow Connect for Other Database Users',
	  rule_expr => 'SYS_CONTEXT(''USERENV'',''SESSION_USER'') != ''PATCH_USER''');
	END;
	/
	COMMIT;
	```
4. Create the Dual Connect for Boss and Patch rule set, and then add the two rules to it.
	```
	BEGIN
	     DBMS_MACADM.CREATE_RULE_SET(
	     rule_set_name => 'Dual Connect for Boss and Patch',
	     description => 'Checks if both boss and patch users are logged in.',
	     enabled           => DBMS_MACUTL.G_YES,
	     eval_options      => DBMS_MACUTL.G_RULESET_EVAL_ANY,
	     audit_options     => DBMS_MACUTL.G_RULESET_AUDIT_FAIL,
	     fail_options      => DBMS_MACUTL.G_RULESET_FAIL_SILENT,
	     fail_message      =>'',
	     fail_code         => NULL,
	     handler_options   => DBMS_MACUTL.G_RULESET_HANDLER_OFF,
	     handler           => ''
	     );
	END;
	/
	BEGIN
	     DBMS_MACADM.ADD_RULE_TO_RULE_SET(
	     rule_set_name     => 'Dual Connect for Boss and Patch',
	     rule_name         => 'Check if Boss Is Logged In'
	   );
	END;
	/
	BEGIN
	     DBMS_MACADM.ADD_RULE_TO_RULE_SET(
	     rule_set_name     => 'Dual Connect for Boss and Patch',
	     rule_name         => 'Allow Connect for Other Database Users'
	   );
	END;
	/
	```
5. Create the following CONNECT command rule, which permits user `patch_user` to connect to the database only if `patch_boss` is already logged in.
	```
	BEGIN
	   DBMS_MACADM.CREATE_COMMAND_RULE(
	   command             => 'CONNECT',
	    rule_set_name      => 'Dual Connect for Boss and Patch',
	    object_owner       => '%',
	    object_name        => '%',
	    enabled            => DBMS_MACUTL.G_YES);
	END;
	/
	COMMIT;
	```

### Step 4: Test the Users' Access

1. Exit SQL\*Plus.
	```
	EXIT
	```
2. Create a second shell, for example:
	```
	xterm &
	```
3. In the first shell, try to log in as user `patch_user`.
	```
	sqlplus patch_user
	Enter password: password
	ERROR:
	ORA-47400: Command Rule violation for CONNECT on LOGON
	Enter user-name:
	```
	User `patch_user` cannot log in until user `patch_boss` is already logged in. (Do not try the `Enter user-name` prompt yet.)
4. In the second shell, log in as user `patch_boss`.
	```
	sqlplus patch_boss
	Enter password: password
	Connected.
	```
	User `patch_boss` can log in.
5. Go back to the first shell, and then try logging in as user `patch_user` again.
	```
	Enter user_name: patch_user
	Enter password: password
	```
	This time, user `patch_user` is deemed a valid user, so now he can log in.

### Step 5: Remove the Components for This Tutorial

1. In the session for the user `patch_boss`, exit SQL\*Plus and then close the shell.
	```
	EXIT
	```
2. In the first shell, connect the `DV_ACCTMGR` user and remove the users you created.
	```
	CONNECT amalcolm_dvacctmgr
	Enter password: password
	DROP USER patch_boss;
	DROP USER patch_user;
	```
3. Connect as user `SYS` with the `SYSDBA` privilege and revoke the privileges that you had granted to the `DV_OWNER` or `DV_ADMIN` user.
	```
	CONNECT SYS AS SYSDBA
	Enter password: password
	REVOKE CREATE PROCEDURE FROM lbrown_dvowner;
	REVOKE SELECT ON V_$SESSION FROM lbrown_dvowner;
	```
4. Connect as the `DV_OWNER` or `DV_ADMIN` user and drop the rules, rule set, and command rule, in the order shown.
	```
	CONNECT lbrown_dvowner
	Enter password: password
	DROP FUNCTION check_boss_logged_in;
	EXEC DBMS_MACADM.DELETE_COMMAND_RULE('CONNECT', '%', '%');
	EXEC DBMS_MACADM.DELETE_RULE_FROM_RULE_SET('Dual Connect for Boss and Patch', 'Check if Boss Is Logged In');
	EXEC DBMS_MACADM.DELETE_RULE_FROM_RULE_SET('Dual Connect for Boss and Patch', 'Allow Connect for Other Database Users');
	EXEC DBMS_MACADM.DELETE_RULE('Check if Boss Is Logged In');
	EXEC DBMS_MACADM.DELETE_RULE('Allow Connect for Other Database Users');
	EXEC DBMS_MACADM.DELETE_RULE_SET('Dual Connect for Boss and Patch');
	COMMIT;
	```

## Guidelines for Designing Rule Sets

Follow these guidelines for designing rule sets:

- You can share rules among multiple rule sets. This lets you develop a library of reusable rule expressions. Oracle recommends that you design such rules to be discrete, single-purpose expressions.
- You can design a rule set so that its evaluation is static, that is, it is evaluated only once during a user session. Alternatively, it can be evaluated each time the associated command rule accesses the rule set. If the rule set is evaluated only once, then the evaluated value is reused throughout the user session each time the command rule accesses the rule set. Using static evaluation is useful in cases where the rule set must be accessed multiple times but the conditions on which the rule set depend do not change during that session. An example would be a SELECT command rule associated with a rule set when the same `SELECT` statement occurs multiple times and if the evaluated value is acceptable to use again, rather than evaluating the rule set each time the `SELECT` occurs.
	To control the static evaluation of the rule set, set the `is_static` parameter of the `CREATE_RULE_SET` or `UPDATE_RULE_SET` procedures of the `DBMS_MACADM` PL/SQL package. See ["Rule Set Procedures Within DBMS\_MACADM"](apis_dbms_macadm.md) for more information.
- Use Oracle Database Vault factors in your rule expressions to provide reusability and trust in the values used by your rule expressions. Factors can provide contextual information to use in your rules expressions.
- You can use custom event handlers to extend Oracle Database Vault security policies to integrate external systems for error handling or alerting. Using Oracle utility packages such as `UTL_TCP`, `UTL_HTTP`, `UTL_MAIL`, `UTL_SMTP`, or `DBMS_AQ` can help you to achieve this type of integration.
- Test rule sets thoroughly for various accounts and scenarios either on a test database or on a test realm or command rule for nonsensitive data before you apply them to realms and command rules that protect sensitive data. You can test rule expressions directly with the following SQL statement:
	```
	SQL> SELECT SYSDATE from DUAL where rule expression
	```
- You can nest rule expressions inside a single rule. This helps to achieve more complex situations where you would need a logical `AND` for a subset of rules and a logical `OR` with the rest of the rules. See the definition for the Is Corporate Network During Maintenance rule set under "Tutorial: Creating an Email Alert for Security Violations" for an example.
- You cannot use invoker's rights procedures with rule expressions. Only use definer's rights procedures with rule expressions.

## How Rule Sets Affect Performance

In general, the more rules and more complex the rules, the more performance overhead the performance for execution of certain operations governed by these rule sets. For example, if you have a very large number of rules in a rule set governing a `SELECT` statement, performance could degrade significantly.

If you have rule sets that require many rules, performance improves if you move all the rules to logic defined in a single PL/SQL standalone or package function. However, if a rule is used by other rule sets, there is little performance effect on your system.

If possible, consider setting the rule set to use static evaluation, assuming this is compatible with the associated command rule's usage. See "Guidelines for Designing Rule Sets" for more information.

You can check system performance by running tools such as Oracle Enterprise Manager (including Oracle Enterprise Manager Database Control, which is installed by default with Oracle Database), `Statspack`, and `TKPROF`. For more information about Oracle Enterprise Manager, see the Oracle Enterprise Manager documentation set. For information about Database Control, refer to its online Help. [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) describes the `Statspack` and `TKPROF` utilities.

## Related Reports and Data Dictionary Views

Table 5-1 lists Oracle Database Vault reports that are useful for analyzing rule sets and the rules within them. See [Chapter 18, "Oracle Database Vault Reports,"](reports.md) for information about how to run these reports.

Table 5-1 Reports Related to Rule Sets

| Report | Description |
| --- | --- |
| ["Rule Set Configuration Issues Report"](reports.md) | Lists rule sets that have no rules defined or enabled |
| ["Secure Application Configuration Issues Report"](reports.md) | Lists secure application roles that have incomplete or disabled rule sets |
| ["Command Rule Configuration Issues Report"](reports.md) | Lists rule sets that are incomplete or disabled |

Table 5-2 lists data dictionary views that provide information about existing rules and rule sets.

Table 5-2 Data Dictionary Views Used for Rules and Rule Sets

| Data Dictionary View | Description |
| --- | --- |
| ["DVSYS.DBA\_DV\_RULE View"](views.md) | Lists the rules that have been defined |
| ["DVSYS.DBA\_DV\_RULE\_SET View"](views.md) | Lists the rules sets that have been created |
| ["DVSYS.DBA\_DV\_RULE\_SET\_RULE View"](views.md) | Lists rules that are associated with existing rule sets |