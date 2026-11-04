---
title: Using the DBMS_MACUTL Package
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/apis_dbms_macutl.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 14 Using the DBMS\_MACUTL Package

This chapter contains:

## About the DBMS\_MACUTL Package

The `DBMS_MACUTL` package provides a set of general purpose utility procedures and functions that you can use throughout the application code you write for Oracle Database Vault. This package is available to all users.

## DBMS\_MACUTL Constants

This section contains:

- DBMS\_MACUTL Listing of Constants
- Examples of Using the DBMS\_MACUTL Constants

### DBMS\_MACUTL Listing of Constants

Table 14-1 summarizes constant (that is, fields) descriptions for the `DBMS_MACUTL` package. You can use these constants with any of the Oracle Database Vault PL/SQL packages. Many of these constants have equivalents in the Oracle Database Vault package. For example, the `enabled` parameter, which is available in several procedures, can accept either `Y` (for Yes) or the constant `G_YES`. Choosing one over the other is a matter of personal preference. They both have the same result.

Table 14-1 DBMS\_MACUTL Listing of Constants

| Constant Name | Data Type | Description |
| --- | --- | --- |
| `G_ALL_OBJECT` | `VARCHAR2(1)` | Used with the realm API `object_name` and `object_type` parameters as a wildcard to indicate all object names or all object types. |
| `G_AUDIT_ALWAYS` | `NUMBER` | Used with the factor API `audit_options` parameter to enable an audit. |
| `G_AUDIT_OFF` | `NUMBER` | Used with the factor API `audit_options` parameter to disable auditing. |
| `G_AUDIT_ON_GET_ERROR` | `NUMBER` | Used with the factor API `audit_options` parameter to audit if the expression specified in the `get_expr` parameter returns an error. |
| `G_AUDIT_ON_GET_NULL` | `NUMBER` | Used with the factor API `audit_options` parameter to audit if the expression in the `get_expr` field is null. |
| `G_AUDIT_ON_TRUST_LEVEL_NEG` | `NUMBER` | Used with the factor API `audit_options` parameter to audit if the trust level is negative. |
| `G_AUDIT_ON_TRUST_LEVEL_NULL` | `NUMBER` | Used with the factor API `audit_options` parameter to audit if no trust level exists. |
| `G_AUDIT_ON_VALIDATE_ERROR` | `NUMBER` | Used with the factor API `audit_options` parameter to audit if the validation function returns an error. |
| `G_AUDIT_ON_VALIDATE_FALSE` | `NUMBER` | Used with the factor API `audit_options` parameter to audit if validation function is false. |
| `G_EVAL_ON_ACCESS` | `NUMBER` | Used with the factor API `eval_options` parameter to reevaluate the factor each time it is accessed. |
| `G_EVAL_ON_SESSION` | `NUMBER` | Used with the factor API `eval_options` parameter to evaluate the factor only once, when the user logs in to the session. |
| `G_FAIL_SILENTLY` | `NUMBER` | Used with the `fail_options` parameter to fail and show no error message. |
| `G_FAIL_WITH_MESSAGE` | `NUMBER` | Used with the `fail_options` parameter to fail and show an error message. |
| `G_IDENTIFY_BY_CONSTANT` | `NUMBER` | Used with the factor API `identify_by` parameter: Fixed value in PL/SQL expression defined in the `get_expr` parameter. |
| `G_IDENTIFY_BY_CONTEXT` | `NUMBER` | Used with the factor API `identify_by` parameter to indicate context. |
| `G_IDENTIFY_BY_FACTOR` | `NUMBER` | Used with the factor API `identify_by` parameter for subfactors through the `factor_link$` table. |
| `G_IDENTIFY_BY_METHOD` | `NUMBER` | Used with the factor API `identify_by` parameter: Expression in `get_expr` field |
| `G_IDENTIFY_BY_RULESET` | `NUMBER` | Used with the factor API `identify_by` parameter: Expression and Rule Set with the `factor_expr$` table |
| `G_LABELED_BY_FACTORS` | `NUMBER` | Used with the factor API `labeled_by` parameter to derive the label from subfactor and merge algorithm. |
| `G_LABELED_BY_SELF` | `NUMBER` | Used with the factor API `labeled_by` parameter to label the factor identities. |
| `G_MAX_SESSION_LABEL` | `VARCHAR2(30)` | This is the highest label a user could set based on the factors. It does not consider the label for a user. |
| `G_MIN_POLICY_LABEL` | `VARCHAR2(30)` | The label to which a factor with a null label defaults. |
| `G_NO` | `VARCHAR2(1)` | Used with the following APIs:  - The factor API `label_indicator` parameter to indicate that a child factor linked to a parent factor does not contribute to the label of the parent factor in an Oracle Label Security integration. - Any API that uses the `enabled` parameter. |
| `G_OLS_SESSION_LABEL` | `VARCHAR2(30)` | The Oracle Label Security session label for a user at the time `init_session` is run. |
| `G_REALM_AUDIT_FAIL` | `NUMBER` | Used with the realm API `audit_options` parameter to audit when the realm is violated. |
| `G_REALM_AUDIT_OFF` | `NUMBER` | Used with the realm API `audit_options` parameter to disable auditing. |
| `G_REALM_AUDIT_SUCCESS` | `NUMBER` | Used with the realm API `audit_options parameter`: Audit on successful realm access |
| `G_REALM_AUTH_OWNER` | `NUMBER` | Used with the realm API `auth_options` parameter to set the realm authorization to Owner. |
| `G_REALM_AUTH_PARTICIPANT` | `NUMBER` | Used with the realm API `auth_options` parameter to set the realm authorization to Participant. |
| `G_RULESET_AUDIT_FAIL` | `NUMBER` | Used with the rule set API `audit_options` parameter to audit on rule set failure. |
| `G_RULESET_AUDIT_OFF` | `NUMBER` | Used with the rule set API `audit_options` parameter to disable auditing. |
| `G_RULESET_AUDIT_SUCCESS` | `NUMBER` | Used with the rule set API `audit_options` parameter to audit on rule set success. |
| `G_RULESET_EVAL_ALL` | `NUMBER` | Used with the rule set API `eval_options` parameter to enable the rule set to succeed if all rules evaluate to true. |
| `G_RULESET_EVAL_ANY` | `NUMBER` | Used with the rule set API `eval_options` parameter to succeed if any of the rules evaluate to true. |
| `G_RULESET_FAIL_SHOW` | `NUMBER` | Used with the rule set API `fail_options` parameter to show an error message if the rule set fails. |
| `G_RULESET_FAIL_SILENT` | `NUMBER` | Used with the rule set API `fail_options` parameter to not show an error message if the rule set fails. |
| `G_RULESET_HANDLER_FAIL` | `NUMBER` | Used with the rule set API `handler_options` parameter to call a handler (specified by the `handler` parameter) if the rule set fails. |
| `G_RULESET_HANDLER_OFF` | `NUMBER` | Used with the rule set API `handler_options` parameter to disable calls to a handler or if no handler is used. |
| `G_RULESET_HANDLER_SUCCESS` | `NUMBER` | Used with the rule set API `handler_options` parameter to call a handler if the rule set succeeds. |
| `G_USER_POLICY_LABEL` | `VARCHAR2(30)` | This is what Oracle Label Security has decided the user's label should be set to after factoring in the preceding values. |
| `G_YES` | `VARCHAR2(1)` | Used with the following APIs:  - The factor API `label_indicator` parameter to indicate that a child factor linked to a parent factor contributes to the label of the parent factor in an Oracle Label Security integration. - Any API that uses the `enabled` parameter. |

### Examples of Using the DBMS\_MACUTL Constants

Example 14-1 shows how to use the `G_YES` and `G_REALM_AUDIT_FAIL` `DBMS_MACUTL` constants when creating a realm.

Example 14-1 Creating a Realm Using DBMS\_MACUTL Constants

```
BEGIN
 DBMS_MACADM.CREATE_REALM(
  realm_name    => 'Performance Statistics Realm',
  description   => 'Realm to measure performance',
  enabled       =>  DBMS_MACUTL.G_YES,
  audit_options =>  DBMS_MACUTL.G_REALM_AUDIT_FAIL);
END;
/
```

Example 14-2 shows how to use several `DBMS_MACUTL` constants when creating a rule set.

Example 14-2 Creating a Rule Set Using DBMS\_MACUTL Constants

```
BEGIN
 DBMS_MACADM.CREATE_RULE_SET(
  rule_set_name    => 'Limit_DBA_Access', 
  description      => 'DBA access through predefined processes', 
  enabled          => 'Y',
  eval_options     => DBMS_MACUTL.G_RULESET_EVAL_ALL,
  audit_options    => DBMS_MACUTL.G_RULESET_AUDIT_FAIL,
  fail_options     => DBMS_MACUTL.G_RULESET_FAIL_SHOW,
  fail_message     => 'Rule Set Limit_DBA_Access has failed.',
  fail_code        => 20000,
  handler_options  => DBMS_MACUTL.G_RULESET_HANDLER_FAIL, 
  handler          => 'dbavowner.email_alert');
END;
/
```

Example 14-3 shows how to use constants when creating a factor.

Example 14-3 Creating a Factor Using DBMS\_MACUTL Constants

```
BEGIN
 DBMS_MACADM.CREATE_FACTOR(
  factor_name       => 'Sector2_DB', 
  factor_type_name  => 'Instance', 
  description       => ' ', 
  rule_set_name     => 'DB_access', 
  get_expr          => 'UPPER(SYS_CONTEXT(''USERENV'',''DB_NAME''))', 
  validate_expr     => 'dbavowner.check_db_access', 
  identify_by       => DBMS_MACUTL.G_IDENTIFY_BY_FACTOR, 
  labeled_by        => DBMS_MACUTL.G_LABELED_BY_SELF, 
  eval_options      => DBMS_MACUTL.G_EVAL_ON_SESSION, 
  audit_options     => DBMS_MACUTL.G_AUDIT_ALWAYS, 
  fail_options      => DBMS_MACUTL.G_FAIL_SILENTLY); 
END;
/
```

## Procedures and Functions Within the DBMS\_MACUTL Package

Table 14-2 lists the procedures and functions in the `DBMS_MACUTL` package. You can use these procedures or functions as standalone code, or within rule expressions. The examples in this section show a mixture of using both.

Table 14-2 DBMS\_MACUTL Utility Functions

| Procedure or Function | Descriptions |
| --- | --- |
| CHECK\_DVSYS\_DML\_ALLOWED Procedure | Verifies that public-packages are not being bypassed by users updating the Oracle Database Vault configuration |
| GET\_CODE\_VALUE Function | Looks up the value for a code within a code group. |
| GET\_SECOND Function | Returns the seconds in Oracle SS format (00-59). Useful for rule expressions based on time data |
| GET\_MINUTE Function | Returns the minute in Oracle MI format (00–59). Useful for rule expressions based on time data |
| GET\_HOUR Function | Returns the month in Oracle HH24 format (00–23). Useful for rule expressions based on time data |
| GET\_DAY Function | Returns the day in Oracle DD format (01–31). Useful for rule expressions based on time data |
| GET\_MONTH Function | Returns the month in Oracle MM format (01–12). Useful for rule expressions based on time data |
| GET\_YEAR Function | Returns the year in Oracle YYYY format (0001–9999). Useful for rule expressions based on time data |
| IS\_ALPHA Function | Checks whether the character is alphabetic |
| IS\_DIGIT Function | Checks whether the character is numeric |
| IS\_DVSYS\_OWNER Function | Determines whether a user is authorized to manage the Oracle Database Vault configuration |
| IS\_OLS\_INSTALLED Function | Returns an indicator regarding whether Oracle Label Security is installed |
| IS\_OLS\_INSTALLED\_VARCHAR Function | Returns an indicator regarding whether Oracle Label Security is installed |
| USER\_HAS\_ROLE Function | Checks whether a user has a role privilege, directly or indirectly (through another role) |
| USER\_HAS\_ROLE\_VARCHAR Function | Checks whether a user has a role privilege, directly or indirectly (through another role) |
| USER\_HAS\_SYSTEM\_PRIVILEGE Function | Checks whether a user has a system privilege, directly or indirectly (through a role) |

### CHECK\_DVSYS\_DML\_ALLOWED Procedure

The `CHECK_DVSYS_DML_ALLOWED` procedure verifies that public packages are not being bypassed by users updating the Oracle Database Vault configuration.

Syntax

```
DBMS_MACUTL.CHECK_DVSYS_DML_ALLOWED(
  p_user IN VARCHAR2 DEFAULT USER);
```

Parameter

Table 14-3 CHECK\_DVSYS\_DML\_ALLOWED Parameter

| Parameter | Description |
| --- | --- |
| `p_user` | User performing the operation.  To find existing users in the current database instance, query the following views:  - `DBA_USERS`: Finds available users for the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular user or role. See ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). - `DVSYS.DBA_DV_ROLE`: Finds existing secure application roles used in privilege management. See ["DVSYS.DBA\_DV\_ROLE View"](views.md). |

Example

User `SYSTEM` fails the check:

```
EXEC DBMS_MACUTL.CHECK_DVSYS_DML_ALLOWED('system'); 

ERROR at line 1:
ORA-47920: Authorization failed for user system to perform this operation
ORA-06512: at "DBMS_MACUTL", line 23
ORA-06512: at "DBMS_MACUTL", line 372
ORA-06512: at "DBMS_MACUTL", line 508
ORA-06512: at "DBMS_MACUTL", line 572
ORA-06512: at line 1
```

User `lbrown_dvowner`, who has the `DV_OWNER` role, passes the check:

```
EXEC DBMS_MACUTL.CHECK_DVSYS_DML_ALLOWED('lbrown_dvowner');

PL/SQL procedure successfully completed.
```

### GET\_CODE\_VALUE Function

The `GET_CODE_VALUE` function finds the value for a code within a code group, and then returns a `VARCHAR2` value.

Syntax

```
DBMS_MACUTL.GET_CODE_VALUE(
  p_code_group IN VARCHAR2, 
  p_code       IN VARCHAR2)
RETURN VARCHAR2;
```

Parameters

Table 14-4 GET\_CODE\_VALUE Parameters

| Parameter | Description |
| --- | --- |
| `p_code_group` | Code group (for example, `AUDIT_EVENTS` or `BOOLEAN`).  To find available code groups in the current database instance, query the `DVSYS.DBA_DV_CODE` view, described in ["DVSYS.DBA\_DV\_CODE View"](views.md). |
| `p_code` | ID of the code.  This ID is listed when you run the `DVSYS.DBA_DV_CODE` view. |

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Get Label Algorithm for Maximum Level/Union/Null',
  rule_expr => 'DBMS_MACUTL.GET_CODE_VALUE(''LABEL_ALG'', ''HUN'') = ''Union''');
END;
/
```

### GET\_SECOND Function

The `GET_SECOND` function returns the seconds in Oracle SS (seconds) format (00–59), and then returns a `NUMBER` value. It is useful for rule expressions based on time data.

Syntax

```
DBMS_MACUTL.GET_SECOND(
  p_date IN DATE DEFAULT SYSDATE)
RETURN NUMBER;
```

Parameter

Table 14-5 GET\_SECOND Parameter

| Parameter | Description |
| --- | --- |
| `p_date` | Date in SS format (for example, `59`).  If you do not specify a date, then Oracle Database Vault uses the Oracle Database `SYSDATE` function to retrieve the current date and time set for the operating system on which the database resides. |

Example

```
SET SERVEROUTPUT ON
DECLARE 
  seconds number; 
BEGIN 
  seconds := DBMS_MACUTL.GET_SECOND(TO_DATE('03-APR-2009 6:56 PM', 
  'dd-mon-yyyy hh:mi PM')); 
  DBMS_OUTPUT.PUT_LINE('Seconds: '||seconds); 
END; 
/
```

This example, which uses a fixed date and time, returns the following:

```
Seconds: 56
```

### GET\_MINUTE Function

The `GET_MINUTE` function returns the minute in Oracle MI (minute) format (00–59), in a `NUMBER` value. It is useful for rule expressions based on time data.

Syntax

```
DBMS_MACUTL.GET_MINUTE(
  p_date IN DATE DEFAULT SYSDATE)
RETURN NUMBER;
```

Parameter

Table 14-6 GET\_MINUTE Parameter

| Parameter | Description |
| --- | --- |
| `p_date` | Date in MI format (for example, `30`, as in 2:30).  If you do not specify a date, then Oracle Database Vault uses the Oracle Database `SYSDATE` function to retrieve the current date and time set for the operating system on which the database resides. |

Example

```
SET SERVEROUTPUT ON
DECLARE 
  minute number; 
BEGIN 
  minute := DBMS_MACUTL.GET_MINUTE(SYSDATE); 
  DBMS_OUTPUT.PUT_LINE('Minute: '||minute); 
END; 
/
```

Output similar to the following appears:

```
Minute: 17
```

### GET\_HOUR Function

The `GET_HOUR` function returns the hour in Oracle HH24 (hour) format (00–23), in a `NUMBER` value. It is useful for rule expressions based on time data.

Syntax

```
DBMS_MACUTL.GET_HOUR(
  p_date IN DATE DEFAULT SYSDATE)
RETURN NUMBER;
```

Parameter

Table 14-7 GET\_HOUR Parameter

| Parameter | Description |
| --- | --- |
| `p_date` | Date in HH24 format (for example, `14` for 2:00 p.m.)  If you do not specify a date, then Oracle Database Vault uses the Oracle Database `SYSDATE` function to retrieve the current date and time set for the operating system on which the database resides. |

Example

```
SET SERVEROUTPUT ON
DECLARE 
  hours number; 
BEGIN 
  hours := DBMS_MACUTL.GET_HOUR(SYSDATE); 
  DBMS_OUTPUT.PUT_LINE('Hour: '||hours); 
END; 
/
```

Output similar to the following appears:

```
Hour: 12
```

### GET\_DAY Function

The `GET_DAY` function returns the day in Oracle DD (day) format (01–31), in a `NUMBER` value. It is useful for rule expressions based on time data.

Syntax

```
DBMS_MACUTL.GET_DAY(
  p_date IN DATE DEFAULT SYSDATE)
RETURN NUMBER;
```

Parameter

Table 14-8 GET\_DAY Parameter

| Parameter | Description |
| --- | --- |
| `p_date` | Date in DD format (for example, `01` for the first day of the month).  If you do not specify a date, then Oracle Database Vault uses the Oracle Database `SYSDATE` function to retrieve the current date and time set for the operating system on which the database resides. |

Example

```
SET SERVEROUTPUT ON
DECLARE 
  day number; 
BEGIN 
  day := DBMS_MACUTL.GET_DAY(SYSDATE); 
  DBMS_OUTPUT.PUT_LINE('Day: '||day); 
END; 
/
```

Output similar to the following appears:

```
Day: 3
```

### GET\_MONTH Function

The `GET_MONTH` function returns the month in Oracle MM (month) format (01–12), in a `NUMBER` value. It is useful for rule expressions based on time data.

Syntax

```
DBMS_MACUTL.GET_MONTH(
  p_date IN DATE DEFAULT SYSDATE)
RETURN NUMBER;
```

Parameter

Table 14-9 GET\_MONTH Parameter

| Parameter | Description |
| --- | --- |
| `p_date` | Date in MM format (for example, `08` for the month of August).  If you do not specify a date, then Oracle Database Vault uses the Oracle Database `SYSDATE` function to retrieve the current date and time set for the operating system on which the database resides. |

Example

```
SET SERVEROUTPUT ON
DECLARE 
  month number; 
BEGIN 
  month := DBMS_MACUTL.GET_MONTH(SYSDATE); 
  DBMS_OUTPUT.PUT_LINE('Month: '||month); 
END; 
/
```

Output similar to the following appears:

```
Month: 4
```

### GET\_YEAR Function

The `GET_YEAR` function returns the year in Oracle YYYY (year) format (0001–9999), in a `NUMBER` value. It is useful for rule expressions based on time data.

Syntax

```
DBMS_MACUTL.GET_YEAR(
  p_date IN DATE DEFAULT SYSDATE)
RETURN NUMBER;
```

Parameter

Table 14-10 GET\_YEAR Parameter

| Parameter | Description |
| --- | --- |
| `p_date` | Date in YYYY format (for example, `1984`).  If you do not specify a date, then Oracle Database Vault uses the `SYSDATE` function to retrieve the current date and time set for the operating system on which the database resides. |

Example

```
SET SERVEROUTPUT ON
DECLARE 
  year number; 
BEGIN 
  year := DBMS_MACUTL.GET_YEAR(SYSDATE); 
  DBMS_OUTPUT.PUT_LINE('Year: '||year); 
END; 
/
```

### IS\_ALPHA Function

The `IS_ALPHA` function checks whether the character is alphabetic, and then returns a `BOOLEAN` value. `IS_ALPHA` returns `TRUE` if the character is alphabetic.

Syntax

```
DBMS_MACUTL.IS_ALPHA(
  c IN VARCHAR2)
RETURN BOOLEAN;
```

Parameter

Table 14-11 IS\_ALPHA Parameter

| Parameter | Description |
| --- | --- |
| `c` | String with one character |

Example

```
SET SERVEROUTPUT ON
BEGIN 
 IF DBMS_MACUTL.IS_ALPHA('z')  
  THEN DBMS_OUTPUT.PUT_LINE('The alphabetic character was found');
 ELSE 
  DBMS_OUTPUT.PUT_LINE('No alphabetic characters today.'); 
 END IF; 
END;
/
```

### IS\_DIGIT Function

The `IS_DIGIT` function checks whether the character is numeric, and then returns a `BOOLEAN` value. `IS_DIGIT` returns `TRUE` if the character is a digit.

Syntax

```
DBMS_MACUTL.IS_DIGIT(
  c IN VARCHAR2)
RETURN BOOLEAN;
```

Parameter

Table 14-12 IS\_DIGIT Parameter

| Parameter | Description |
| --- | --- |
| `c` | String with one character |

Example

```
SET SERVEROUTPUT ON
BEGIN 
 IF DBMS_MACUTL.IS_DIGIT('7')  
  THEN DBMS_OUTPUT.PUT_LINE('The numeric character was found');
 ELSE 
  DBMS_OUTPUT.PUT_LINE('No numeric characters today.'); 
 END IF; 
END;
/
```

### IS\_DVSYS\_OWNER Function

The `IS_DVSYS_OWNER` function determines whether a user is authorized to manage the Oracle Database Vault configuration, and then returns a `BOOLEAN` value. `IS_DVSYS_OWNER` returns `TRUE` if the user is authorized.

Syntax

```
DBMS_MACUTL.IS_DVSYS_OWNER(
  p_user IN VARCHAR2 DEFAULT USER)
RETURN BOOLEAN;
```

Parameter

Table 14-13 IS\_DVSYS\_OWNER Parameter

| Parameter | Description |
| --- | --- |
| `p_user` | User to check.  To find existing users, query the following views:  - `DBA_USERS`: Finds available users for the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular user or role. See ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). - `DVSYS.DBA_DV_ROLE`: Finds existing secure application roles used in privilege management. See ["DVSYS.DBA\_DV\_ROLE View"](views.md). |

Example

```
SET SERVEROUTPUT ON
BEGIN 
 IF DBMS_MACUTL.IS_DVSYS_OWNER('PSMITH')
  THEN DBMS_OUTPUT.PUT_LINE('PSMITH is authorized to manage Database Vault.');
 ELSE 
  DBMS_OUTPUT.PUT_LINE('PSMITH is not authorized to manage Database Vault.'); 
 END IF; 
END;
/
```

### IS\_OLS\_INSTALLED Function

The `IS_OLS_INSTALLED` function returns an indicator regarding whether Oracle Label Security is installed, and then returns a `TRUE` or `FALSE` `BOOLEAN` value. If Oracle Label Security is installed, `IS_OLS_INSTALLED` returns `TRUE`.

Syntax

```
DBMS_MACUTL.IS_OLS_INSTALLED()
RETURN BOOLEAN;
```

Parameters

None.

Example

```
SET SERVEROUTPUT ON
BEGIN 
 IF DBMS_MACUTL.IS_OLS_INSTALLED()  
  THEN DBMS_OUTPUT.PUT_LINE('OLS is installed');
 ELSE 
  DBMS_OUTPUT.PUT_LINE('OLS is not installed'); 
 END IF; 
END;
/
```

### IS\_OLS\_INSTALLED\_VARCHAR Function

The `IS_OLS_INSTALLED_VARCHAR` function returns an indicator regarding whether Oracle Label Security is installed, and then returns a `Y` or `N` `VARCHAR2` value. If Oracle Label Security is installed, then `IS_OLS_INSTALLED_VARCHAR` returns `Y`.

Syntax

```
DBMS_MACUTL.IS_OLS_INSTALLED_VARCHAR()
RETURN VARCHAR2;
```

Parameters

None.

Example

See "IS\_OLS\_INSTALLED Function" for an example.

### USER\_HAS\_ROLE Function

The `USER_HAS_ROLE` function checks whether a user has a role privilege, directly or indirectly (through another role), and then returns a `BOOLEAN` value. If the user has a role privilege, then `USER_HAS_ROLE` returns `TRUE`.

Syntax

```
DBMS_MACUTL.USER_HAS_ROLE(
  p_role IN VARCHAR2, 
  p_user IN VARCHAR2 DEFAULT USER)
RETURN BOOLEAN;
```

Parameters

Table 14-14 USER\_HAS\_ROLE Parameters

| Parameter | Description |
| --- | --- |
| `p_role` | Role privilege to check.  To find existing roles, query the following views:  - `DBA_ROLES`: Finds available roles in the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular user or role. See ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). - `DVSYS.DBA_DV_ROLE`: Finds existing secure application roles used in privilege management. See ["DVSYS.DBA\_DV\_ROLE View"](views.md). |
| `p_user` | User to check.  To find existing users, query the following views:  - `DBA_USERS`: Finds available users for the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular user or role. See ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). |

Example

```
SET SERVEROUTPUT ON
BEGIN
 IF DBMS_MACUTL.USER_HAS_ROLE('SECTOR2_APP_MGR', 'PSMITH')
  THEN DBMS_OUTPUT.PUT_LINE('User PSMITH has the SECTOR2_APP_MGR role');
   ELSE 
  DBMS_OUTPUT.PUT_LINE('User PSMITH does not have the SECTOR2_APP_MGR role.'); 
 END IF;
END;
/
```

### USER\_HAS\_ROLE\_VARCHAR Function

The `USER_HAS_ROLE_VARCHAR` function checks whether a user has a role privilege, directly or indirectly (through another role), and then returns a `VARCHAR2` value. If the user has the role privilege specified, then `USER_HAS_ROLE_VARCHAR` returns `Y`.

Syntax

```
DBMS_MACUTL.USER_HAS_ROLE_VARCHAR(
  p_role IN VARCHAR2, 
  p_user IN VARCHAR2 DEFAULT USER)
RETURN VARCHAR2;
```

Parameters

Table 14-15 USER\_HAS\_ROLE\_VARCHAR Parameters

| Parameter | Description |
| --- | --- |
| `p_role` | Role to check.  To find existing roles, query the following views:  - `DBA_ROLES`: Finds available roles in the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular user or role. See ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). - `DVSYS.DBA_DV_ROLE`: Finds existing secure application roles used in privilege management. See ["DVSYS.DBA\_DV\_ROLE View"](views.md). |
| `p_user` | User to check.  To find existing users, query the following views:  - `DBA_USERS`: Finds available users for the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular user or role. See ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). |

### USER\_HAS\_SYSTEM\_PRIVILEGE Function

The `USER_HAS_SYSTEM_PRIVILEGE` function checks whether a user has a system privilege, directly or indirectly (through a role), and then returns a `BOOLEAN` value. If the user has the system privilege specified, then `USER_HAS_SYSTEM_PRIVILEGE` returns `TRUE`.

Syntax

```
DBMS_MACUTL.USER_HAS_SYSTEM_PRIVILEGE(
  p_privilege  IN VARCHAR2, 
  p_user       IN VARCHAR2 DEFAULT USER)
RETURN BOOLEAN;
```

Parameters

Table 14-16 USER\_HAS\_SYSTEM\_PRIVILEGE Parameters

| Parameter | Description |
| --- | --- |
| `p_privilege` | System privilege to check for.  To find privileges for a database account excluding `PUBLIC` privileges, query the `DVSYS.DBA_DV_USER_PRIVS` view, described in ["DVSYS.DBA\_DV\_USER\_PRIVS View"](views.md).  To find all privileges for a database account, use `DVSYS.DBA_DV_USER_PRIVS_ALL`, described in ["DVSYS.DBA\_DV\_USER\_PRIVS\_ALL View"](views.md). |
| `p_user` | User to check.  To find existing users, query the following views:  - `DBA_USERS`: Finds available users for the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular user or role. See ["DVSYS.DBA\_DV\_REALM\_AUTH View"](views.md). |

Example

```
SET SERVEROUTPUT ON
BEGIN
 IF DBMS_MACUTL.USER_HAS_SYSTEM_PRIVILEGE('EXECUTE', 'PSMITH')
  THEN DBMS_OUTPUT.PUT_LINE('User PSMITH has the EXECUTE ANY PRIVILEGE privilege.');
   ELSE 
  DBMS_OUTPUT.PUT_LINE('User PSMITH does not have the EXECUTE ANY PRIVILEGE privilege.'); 
 END IF;
END;
/
```