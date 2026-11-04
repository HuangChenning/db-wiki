---
title: Oracle Database Vault Data Dictionary Views
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/views.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 16 Oracle Database Vault Data Dictionary Views

This chapter contains:

## About the Oracle Database Vault Data Dictionary Views

Oracle Database Vault provides a set of `DBA` -style data dictionary views that can be accessed through the `DV_SECANALYST` role or the `DV_ADMIN` role. (Alternatively, you can run reports on Oracle Database Vault. See [Chapter 18, "Oracle Database Vault Reports,"](reports.md) for more information.) These views provide access to the various underlying Oracle Database Vault tables in the `DVSYS` and `LBACSYS` schemas without exposing the primary and foreign key columns that may be present. These views are intended for the database administrative user to report on the state of the Oracle Database Vault configuration without having to perform the joins required to get the labels for codes that are stored in the core tables or from the related tables.

## DVSYS.DBA\_DV\_CODE View

The `DVSYS.DBA_DV_CODE` data dictionary view lists generic lookup codes for the user interface, error messages, constraint checking, and so on. These codes are used for the user interface, views, and for validating input in a translatable fashion.

For example:

```
SELECT CODE, VALUE FROM DVSYS.DBA_DV_CODE WHERE CODE_GROUP = 'BOOLEAN';
```

Output similar to the following appears:

```
CODE    VALUE
------- --------
Y       True
N       False
```

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `CODE_GROUP` | `VARCHAR(30)` | `NOT NULL` | Displays one of the following code groups: - `AUDIT_EVENTS`: Contains the action numbers and action names that are used for the custom event audit trail records - `BOOLEAN`: A simple Yes or No or True or False lookup - `DB_OBJECT_TYPE`: The database object types that can be used for realm objects and command authorizations - `SQL_CMDS`: The DDL commands that can be protected through command rules - `FACTOR_AUDIT`: The auditing options for factor retrieval processing - `FACTOR_EVALUATE`: The evaluation options (by session or by access) for factor retrieval - `FACTOR_FAIL`: The options for propagating errors when a factor retrieval method fails - `FACTOR_IDENTIFY`: The options for determining how a factor identifier is resolved (for example, by method or by factors) - `FACTOR_LABEL`: The options for determining how a factor identifier is labeled in the session establishment phase - `LABEL_ALG`: The algorithms that can be used to determine the maximum session label for a database session for each policy. See [Table 12-57, "Oracle Label Security Merge Algorithm Codes"](apis_dbms_macadm.md) for a listing of the Oracle Label Security merge algorithm codes. - `OPERATORS`: The Boolean operators that can be used for identity maps - `REALM_AUDIT`: The options for auditing realm access or realm violations - `REALM_OPTION`: The options for ownership of a realm - `RULESET_AUDIT`: The options for auditing rule set execution or rule set errors - `RULESET_EVALUATE`: The options for determining the success or failure of a rule set based on all associated rules being true or any associated rule being true - `RULESET_EVENT`: The options to invoke a custom event handler when a rule set evaluates to Succeeds or Fails - `RULESET_FAIL`: The options to determine the run-time visibility of a rule set failing |
| `CODE` | `VARCHAR(30)` | `NOT NULL` | Boolean code used; either `Y` (yes) or `N` (no). |
| `VALUE` | `VARCHAR(4000)` |  | Boolean value used; either `True` if the Boolean code is `Y` or `False` if the Boolean code is `N`. |
| `LANGUAGE` | `VARCHAR(3)` | `NOT NULL` | Language for this installation of Oracle Database Vault.  See [Adding Languages to Oracle Database Vault](dvca.md) for a list of supported languages. |
| `DESCRIPTION` | `VARCHAR(1024)` |  | Brief description of the code group. |

## DVSYS.DBA\_DV\_COMMAND\_RULE View

The `DVSYS.DBA_DV_COMMAND_RULE` data dictionary view lists the SQL statements that are protected by command rules. See [Chapter 6, "Configuring Command Rules,"](cfcmdaut.md) for more information about command rules.

For example:

```
SELECT COMMAND, RULE_SET_NAME FROM DVSYS.DBA_DV_COMMAND_RULE;
```

Output similar to the following appears:

```
COMMAND         RULE_SET_NAME
--------------- -----------------------------
GRANT           Can Grant VPD Administration
REVOKE          Can Grant VPD Administration
ALTER SYSTEM    Allow System Parameters
ALTER USER      Can Maintain Own Account
CREATE USER     Can Maintain Account/Profiles
DROP USER       Can Maintain Account/Profiles
CREATE PROFILE  Can Maintain Account/Profiles
DROP PROFILE    Can Maintain Account/Profiles
ALTER PROFILE   Can Maintain Account/Profiles
```

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `COMMAND` | `VARCHAR(30)` | `NOT NULL` | Name of the command rule. For a list of default command rules, see [Default Command Rules](cfcmdaut.md). |
| `RULE_SET_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the rule set associated with this command rule. |
| `OBJECT_OWNER` | `VARCHAR(30)` | `NOT NULL` | The owner of the object that the command rule affects. |
| `OBJECT_NAME` | `VARCHAR(128)` | `NOT NULL` | The name of the database object the command rule affects (for example, a database table). |
| `ENABLED` | `VARCHAR(1`) | `NOT NULL` | `Y` indicates the command rule is enabled; `N` indicates it is disabled. |

## DVSYS.DBA\_DV\_DATAPUMP\_AUTH View

The `DVSYS.DBA_DV_DATAPUMP_AUTH` data dictionary view lists the authorizations for using Oracle Data Pump in an Oracle Database Vault environment. See ["Using Oracle Data Pump in an Oracle Database Vault Environment"](dba.md) for more information.

For example:

```
SELECT * FROM DVSYS.DBA_DV_DATAPUMP_AUTH WHERE GRANTEE = 'PRESTON';
```

Output similar to the following appears:

```
GRANTEE SCHEMA OBJECT
------- ------ -------
PRESTON OE     ORDERS
```

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` | `NOT NULL` | Name of the user who has been granted Data Pump authorization |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Name of the schema on which the user `GRANTEE` is authorized to perform Data Pump operations |
| `OBJECT` | `VARCHAR2(128)` | `NOT NULL` | Name of the object within the schema specified by the `SCHEMA` parameter on which the `GRANTEE` user has Data Pump authorization (such as a table) |

## DVSYS.DBA\_DV\_FACTOR View

The `DVSYS.DBA_DV_FACTOR` data dictionary view lists the existing factors in the current database instance.

For example:

```
SELECT NAME, GET_EXPR FROM DVSYS.DBA_DV_FACTOR WHERE NAME = 'Session_User';
```

Output similar to the following appears:

```
NAME          GET_EXPR
------------- ---------------------------------------------
Session_User  UPPER(SYS_CONTEXT('USERENV', 'SESSION_USER'))
```

Related Views

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the factor. See ["Default Factors"](cfgfact.md) for a list of default factors. |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the factor. |
| `FACTOR_TYPE_NAME` | `VARCHAR2(90)` | `NOT NULL` | Category of the factor, which is used to classify the purpose of the factor. |
| `ASSIGN_RULE_SET_NAME` | `VARCHAR2(90)` |  | Rule set used to control the identify of the factor. |
| `GET_EXPR` | `VARCHAR2(1024)` |  | PL/SQL expression that retrieves the identity of a factor. |
| `VALIDATE_EXPR` | `VARCHAR2(1024)` |  | PL/SQL expression used to validate the identify of the factor. It returns a Boolean value. |
| `IDENTIFIED_BY` | `NUMBER` | `NOT NULL` | Determines the identity of a factor, based on the expression listed in the `GET_EXPR` column. Possible values are: - `0`: By constant - `1`: By method - `2`: By factors |
| `IDENTIFIED_BY_MEANING` | `VARCHAR2(4000)` |  | Provides a text description for the corresponding value in the `IDENTIFIED_BY` column. Possible values are: - `By Constant`: If `IDENTIFIED_COLUMN` is `0` - `By Method`: If `IDENTIFIED_COLUMN` is `1` - `By Factors`: If `IDENTIFIED_COLUMN` is `2` |
| `LABELED_BY` | `NUMBER` | `NOT NULL` | Determines the labeling the factor: - `0`: Labels the identities for the factor directly from the labels associated with an Oracle Label Security policy - `1`: Derives the factor identity label from the labels of its child factor identities. |
| `LABELED_BY_MEANING` | `VARCHAR2(4000)` |  | Provides a text description for the corresponding value in the `LABELED_BY` column. Possible values are: - `By Self`: If `LABELED_BY` column is `0` - `By Factors`: If `LABELED_BY` column is `1` |
| `EVAL_OPTIONS` | `NUMBER` | `NOT NULL` | Determines how the factor is evaluated when the user logs on: - `0`: When the database session is created - `1`: Each time the factor is accessed - `2`: On start-up |
| `EVAL_OPTIONS_MEANING` | `VARCHAR2(4000)` |  | Provides a text description for the corresponding value in the `EVAL_OPTIONS` column. Possible values are: - `For Session`: If `EVAL_OPTIONS` is `0` - `By Access`: If `EVAL_OPTIONS` is `1` - `On Startup`: If `EVAL_OPTIONS` is `2` |
| `AUDIT_OPTIONS` | `NUMBER` | `NOT NULL` | Option for auditing the factor if you want to generate a custom Oracle Database Vault audit record. Possible values are: - `0`: No auditing set - `1`: Always audits - `2`: Audits if `get_expr` returns an error - `4`: Audits if `get_expr` is null - `8`: Audits if the validation procedure returns an error - `16`: Audits if the validation procedure is false - `32`: Audits if there is no trust level set - `64`: Audits if the trust level is negative. |
| `FAIL_OPTIONS` | `NUMBER` | `NOT NULL` | Options for reporting factor errors: - `1`: Shows an error message. - `2`: Does not show an error message. |
| `FAIL_OPTIONS_MEANING` | `VARCHAR2(4000)` |  | Provides a text description for the corresponding value in the `FAIL_OPTIONS` column. Possible values are: - `Show Error Message` - `Do Not Show Error Message`: |

## DVSYS.DBA\_DV\_FACTOR\_LINK View

The `DVSYS.DBA_DV_FACTOR_LINK` data dictionary view shows the relationships of each factor whose identity is determined by the association of child factors. The view contains one entry for each parent factor and child factor. You can use this view to resolve the relationships from the factor links to identity maps.

For example:

```
SELECT PARENT_FACTOR_NAME, CHILD_FACTOR_NAME FROM DVSYS.DBA_DV_FACTOR_LINK;
```

Output similar to the following appears:

```
PARENT_FACTOR_NAME             CHILD_FACTOR_NAME
------------------------------ ------------------------------
Domain                         Database_Instance
Domain                         Database_IP
Domain                         Database_Hostname
```

Related Views

- DVSYS.DBA\_DV\_FACTOR View
- DVSYS.DBA\_DV\_FACTOR\_TYPE View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `PARENT_FACTOR_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the parent factor. |
| `CHILD_FACTOR_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the child factor of the parent factor. |
| `LABEL_IND` | `VARCHAR(1)` | `NOT NULL` | Indicates whether the child factor that is linked to the parent factor contributes to the label of the parent factor in an Oracle Label Security integration. Possible values are: - `Y` (for Yes) - `N` (for No) |

## DVSYS.DBA\_DV\_FACTOR\_TYPE View

The `DVSYS.DBA_DV_FACTOR_TYPE` data dictionary view lists the names and descriptions of factor types used in the system.

For example:

```
SELECT * FROM DVSYS.DBA_DV_FACTOR_TYPE WHERE NAME = 'Hostname';
```

Output similar to the following appears:

```
NAME      DESCRIPTION
--------- ----------------------------------------------------------------------
Time      Time-based factor
```

Related Views

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the factor type. |
| `DESCRIPTION` | `VARCHAR(1024)` |  | Description of the factor type. |

## DVSYS.DBA\_DV\_IDENTITY View

The `DVSYS.DBA_DV_IDENTITY` data dictionary view lists the identities for each factor.

For example:

```
SELECT * FROM DVSYS.DBA_DV_IDENTITY WHERE VALUE = 'GLOBAL SHARED';
```

Output similar to the following appears, assuming you have created only one factor identity:

```
FACTOR_NAME          VALUE          TRUST_LEVEL
----------------     -------------- ------------
Identification_Type  GLOBAL SHARED  1
```

Related Views

- DVSYS.DBA\_DV\_FACTOR View
- DVSYS.DBA\_DV\_IDENTITY\_MAP View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `FACTOR_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the factor. |
| `VALUE` | `VARCHAR(1024)` | `NOT NULL` | Value of the factor. |
| `TRUST_LEVEL` | `NUMBER` | `NOT NULL` | Number that indicates the magnitude of trust relative to other identities for the same factor. |

## DVSYS.DBA\_DV\_IDENTITY\_MAP View

The `DVSYS.DBA_DV_IDENTITY_MAP` data dictionary view lists the mappings for each factor identity. The view includes mapping factors that are identified by other factors to combinations of parent-child factor links. For each factor, the maps are joined by the `OR` operation, and for different factors, the maps are joined by the `AND` operation.

You can use this view to resolve the identity for factors that are identified by other factors (for example, a domain) or for factors that have continuous domains (for example, Age or Temperature).

For example:

```
SELECT FACTOR_NAME, IDENTITY_VALUE FROM DVSYS.DBA_DV_IDENTITY_MAP;
```

Output similar to the following appears:

```
FACTOR_NAME      IDENTITY_VALUE
---------------- --------------------
Sector2_Program  Accounting-Sensitive
```

Related Views

- DVSYS.DBA\_DV\_FACTOR View
- DVSYS.DBA\_DV\_IDENTITY View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `FACTOR_NAME` | `VARCHAR(30)` | `NOT NULL` | Factor the identity map is for. |
| `IDENTITY_VALUE` | `VARCHAR(1024)` | `NOT NULL` | Value the factor assumes if the identity map evaluates to `TRUE`. |
| `OPERATION_VALUE` | `VARCHAR(4000)` |  | Relational operator for the identity map (for example, <, >, =, and so on) |
| `OPERAND1` | `VARCHAR(1024)` |  | Left operand for the relational operator; refers to the low value you enter. |
| `OPERAND2` | `VARCHAR(1024)` |  | Right operand for the relational operator; refers to the high value you enter. |
| `PARENT_FACTOR_NAME` | `VARCHAR(30)` |  | The parent factor link to which the map is related. |
| `CHILD_FACTOR_NAME` | `VARCHAR(30)` |  | The child factor link to which the map is related. |
| `LABEL_IND` | `VARCHAR(1)` |  | Indicates whether the child factor being linked to the parent factor contributes to the label of the parent factor in an Oracle Label Security integration. Possible values are: - `Y` (for Yes) - `N` (for No) |

## DVSYS.DBA\_DV\_MAC\_POLICY View

The `DVSYS.DBA_DV_MAC_POLICY` data dictionary view lists the Oracle Label Security policies defined for use with Oracle Database Vault.

For example:

```
SELECT POLICY_NAME, ALGORITHM_CODE, ALGORITHM_MEANING 
 FROM DVSYS.DBA_DV_MAC_POLICY;
```

Output similar to the following appears:

```
POLICY_NAME     ALGORITHM_CODE    ALGORITHM_MEANING
--------------- ----------------- -----------------------
ACCESS_DATA     LUI               Minimum Level/Union/Intersection
```

Related Views

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the policy. |
| `ALGORITHM_CODE` | `VARCHAR(30)` | `NOT NULL` | Merge algorithm code used for the policy. See [Table 12-57](apis_dbms_macadm.md) for a listing of algorithm codes. |
| `ALGORITHM_MEANING` | `VARCHAR(4000)` |  | Provides a text description for the corresponding value in the `ALGORITHM_CODE` column. See [Table 12-57](apis_dbms_macadm.md) for a listing of algorithm code descriptions. |
| `ERROR_LABEL` | `VARCHAR(4000)` |  | Label specified for initialization errors, to be set when a configuration error or run-time error occurs during session initialization. |

## DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR View

The `DVSYS.DBA_DV_MAC_POLICY` data dictionary view lists the factors that are associated with Oracle Label Security policies.

You can use this view to determine what factors contribute to the maximum session label for each policy using the `DVSYS.DBA_DV_MAC_POLICY` view.

For example:

```
SELECT * FROM DVSYS.DBA_DV_MAC_POLICY_FACTOR;
```

Output similar to the following appears:

```
FACTOR_NAME    MAC_POLICY_NAME
-------------- ------------------
App_Host_Name  Access Locations
```

Related Views

- DVSYS.DBA\_DV\_MAC\_POLICY View
- DVSYS.DBA\_DV\_POLICY\_LABEL View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `FACTOR_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the factor. |
| `MAC_POLICY_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the Oracle Label Security policy associated with this factor. |

## DVSYS.DBA\_DV\_POLICY\_LABEL View

The `DVSYS.DBA_DV_POLICY_LABEL` data dictionary view lists the Oracle Label Security label for each factor identifier in the `DVSYS.DBA_DV_IDENTITY` view for each policy.

For example:

```
SELECT * FROM DVSYS.DBA_DV_POLICY_LABEL;
```

Output similar to the following appears:

```
IDENTITY_VALUE   FACTOR_NAME     POLICY_NAME       LABEL
---------------- --------------  ----------------  ---------
App_Host_Name    Sect2_Fin_Apps  Access Locations  Sensitive
```

Related Views

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `IDENTITY_VALUE` | `VARCHAR(1024)` | `NOT NULL` | Name of the factor identifier. |
| `FACTOR_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the factor associated with the factor identifier. |
| `POLICY_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the Oracle Label Security policy associated with this factor. |
| `LABEL` | `VARCHAR(4000)` | `NOT NULL` | Name of the Oracle Label Security label associated with the policy. |

## DVSYS.DBA\_DV\_PUB\_PRIVS View

The `DVSYS.DBA_DV_PUB_PRIVS` data dictionary view lists data reflected in the Oracle Database Vault privilege management reports used in the Oracle Database Vault Administrator (`DV_ADMIN`). See also ["Privilege Management - Summary Reports"](reports.md).

For example:

```
SELECT USERNAME, ACCESS_TYPE FROM DVSYS.DBA_DV_PUB_PRIVS WHERE USERNAME = 'OE';
```

Output similar to the following appears:

```
USERNAME    ACCESS_TYPE
----------- -----------------
OE          PUBLIC
```

Related Views

- DVSYS.DBA\_DV\_USER\_PRIVS View
- DVSYS.DBA\_DV\_USER\_PRIVS\_ALL View
- DVSYS.DBA\_DV\_ROLE View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR(30)` | `NOT NULL` | Database schema in the current database instance.acces |
| `ACCESS_TYPE` | `VARCHAR(30)` |  | Access type granted to the user listed in the `USERNAME` column (for example, `PUBLIC`). |
| `PRIVILEGE` | `VARCHAR(40`) | `NOT NULL` | Privilege granted to the user listed in the `USERNAME` column. |
| `OWNER` | `VARCHAR(30)` | `NOT NULL` | Owner of the database schema to which the `USERNAME` user has been granted privileges. |
| `OBJECT_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the object within the schema listed in the `OWNER` column. |

## DVSYS.DBA\_DV\_REALM View

The `DVSYS.DBA_DV_REALM` data dictionary view lists the realms created in the current database instance.

For example:

For example:

```
SELECT NAME, AUDIT_OPTIONS, ENABLED FROM DVSYS.DBA_DV_REALM 
  WHERE AUDIT_OPTIONS = '1';
```

Output similar to the following appears:

```
NAME                          AUDIT_OPTIONS    ENABLED
----------------------------- ---------------- --------
Performance Statistics Realm  1                Y
```

Related Views

- DVSYS.DBA\_DV\_REALM\_AUTH View
- DVSYS.DBA\_DV\_REALM\_OBJECT View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR(90)` | `NOT NULL` | Names of the realms created. See ["Default Realms"](cfrealms.md) for a listing of default realms. |
| `DESCRIPTION` | `VARCHAR(1024`) | `NOT NULL` | Description of the realm created. |
| `AUDIT_OPTIONS` | `NUMBER` | `NOT NULL` | Specifies whether auditing is enabled. Possible values are: - `0`: No auditing for the realm. - `1`: Creates an audit record when a realm violation occurs (for example, when an unauthorized user tries to modify an object that is protected by the realm). - `2`: Creates an audit record for authorized activities on objects protected by the realm. - `3`: Creates an audit record for both authorized and unauthorized activities on objects protected by the realm. |
| `ENABLED` | `VARCHAR(1)` | `NOT NULL` | Specifies whether realm checking is enabled. `Y` (yes) indicates it is enabled; `N` (no) indicates it is not. |

## DVSYS.DBA\_DV\_REALM\_AUTH View

The `DVSYS.DBA_DV_REALM_AUTH` data dictionary view lists the authorization of a named database user account or database role (`GRANTEE`) to access realm objects in a particular realm. See [Defining Realm Authorization](cfrealms.md) for more information.

For example:

```
SELECT REALM_NAME, GRANTEE, AUTH_RULE_SET_NAME FROM DVSYS.DBA_DV_REALM_AUTH;
```

Output similar to the following appears:

```
REALM_NAME                    GRANTEE  AUTH_RULE_SET_NAME
---------------------------- --------- ---------------------
Performance Statistics Realm  SYSADM   Check Conf Access
```

Related Views

- DVSYS.DBA\_DV\_REALM View
- DVSYS.DBA\_DV\_REALM\_OBJECT View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `REALM_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the realm. |
| `GRANTEE` | `VARCHAR(30)` | `NOT NULL` | User or role name to authorize as owner or participant. |
| `AUTH_RULE_SET_NAME` | `VARCHAR(90`) |  | Rule set to check before authorizing. If the rule set evaluates to `TRUE`, then the authorization is allowed. |
| `AUTH_OPTIONS` | `VARCHAR(4000)` |  | Type of realm authorization: either `Participant` or `Owner`. |

## DVSYS.DBA\_DV\_REALM\_OBJECT View

The `DVSYS.DBA_DV_REALM_OBJECT` data dictionary view lists the database schemas, or subsets of schemas with specific database objects contained therein, that are secured by the realms. See ["Creating Realm-Secured Objects"](cfrealms.md) for more information.

For example:

```
SELECT REALM_NAME, OWNER, OBJECT_NAME FROM DVSYS.DBA_DV_REALM_OBJECT;
```

Output similar to the following appears:

```
REALM_NAME                   OWNER    OBJECT_NAME
---------------------------- -------- -----------
Performance Statistics Realm OE       ORDERS
```

Related Views

- DVSYS.DBA\_DV\_REALM View
- DVSYS.DBA\_DV\_REALM\_AUTH View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `REALM_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the realm. |
| `OWNER` | `VARCHAR(90)` | `NOT NULL` | Database schema owner who owns the realm. |
| `OBJECT_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the object the realm protects. |
| `OBJECT_TYPE` | `VARCHAR(90)` | `NOT NULL` | Type of object the realm protects, such as a database table, view, index, or role. |

## DVSYS.DBA\_DV\_ROLE View

The `DVSYS.DBA_DV_ROLE` data dictionary view lists the Oracle Database Vault secure application roles used in privilege management.

For example:

```
SELECT ROLE, RULE_NAME FROM DVSYS.DBA_DV_ROLE;
```

Output similar to the following appears:

```
ROLE               RULE_NAME
------------------ --------------------
Sector2_APP_MGR    Check App2 Access
Sector2_APP_DBA    Check App2 Access
```

Related Views

- DVSYS.DBA\_DV\_PUB\_PRIVS View
- DVSYS.DBA\_DV\_USER\_PRIVS View
- DVSYS.DBA\_DV\_USER\_PRIVS\_ALL View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR(30)` | `NOT NULL` | Name of the secure application role. |
| `RULE_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the rule set associated with the secure application role. |
| `ENABLED` | `VARCHAR(1)` | `NOT NULL` | Indicates whether the secure application role is enabled. `Y` (yes) enables the role; `N` (no) disables it. |

## DVSYS.DBA\_DV\_RULE View

The `DVSYS.DBA_DV_RULE` data dictionary view lists the rules that have been defined.

For example:

```
SELECT * FROM DVSYS.DBA_DV_RULE WHERE NAME = 'Maintenance Window';
```

Output similar to the following appears:

```
NAME                RULE_EXP
------------------- ----------------------------------------------
Maintenance Window  TO_CHAR(SYSDATE,'HH24') BETWEEN '10' AND '12'
```

To find the rule sets that use specific rules, query the `DVSYS.DBA_DV_RULE_SET_RULE` view.

Related Views

- DVSYS.DBA\_DV\_RULE\_SET View
- DVSYS.DBA\_DV\_RULE\_SET\_RULE View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the rule. |
| `RULE_EXPR` | `VARCHAR(1024)` | `NOT NULL` | PL/SQL expression for the rule. |

## DVSYS.DBA\_DV\_RULE\_SET View

The `DVSYS.DBA_DV_RULE_SET` data dictionary view lists the rules sets that have been created.

For example:

```
SELECT RULE_SET_NAME, HANDLER_OPTIONS, HANDLER FROM DVSYS.DBA_DV_RULE_SET
 WHERE RULE_SET_NAME = 'Maintenance Period';
```

Output similar to the following appears:

```
RULE_SET_NAME       HANDLER_OPTIONS  HANDLER
------------------- ---------------- ----------------------
Maintenance Period                   1 dbavowner.email_alert
```

Related Views

- DVSYS.DBA\_DV\_RULE View
- DVSYS.DBA\_DV\_RULE\_SET\_RULE View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `RULE_SET_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the rule set. |
| `DESCRIPTION` | `VARCHAR(1024)` |  | Description of the rule set. |
| `ENABLED` | `VARCHAR(1)` | `NOT NULL` | Indicates whether the rule set has been enabled. `Y` (yes) enables the rule set; `N` (no) disables it. |
| `EVAL_OPTIONS_MEANING` | `VARCHAR(4000)` |  | For rules sets that contain multiple rules, determines how many rules are evaluated. Possible values are: - `All True`: All rules in the rule set must evaluate to true for the rule set itself to evaluate to `TRUE`. - `Any True`: At least one rule in the rule set must evaluate to true for the rule set itself to evaluate to `TRUE`. |
| `AUDIT_OPTIONS` | `NUMBER` | `NOT NULL` | Indicates when auditing is used. Possible values are: - `0`: No auditing - `1`: Audit on failure - `2`: Audit on success - `3`: Audit on both failure and success |
| `FAIL_OPTIONS_MEANING` | `VARCHAR(4000)` |  | Determines when an audit record is created for the rule set. Possible values are: - `Do Not Show Error Message`. - `Show Error Message` |
| `FAIL_MESSAGE` | `VARCHAR(80)` |  | Error message for failure that is associated with the fail code listed in the `FAIL_CODE` column. |
| `FAIL_CODE` | `VARCHAR(10)` |  | The error message number associated with the message listed in the `FAIL_MESSAGE` column. Possible values are in the ranges of -20000 to -20999 or 20000 to 20999. |
| `HANDLER_OPTIONS` | `NUMBER` | `NOT NULL` | Determines how error handling is used. Possible values are: - `0`: Disables error handling. - `1`: Call handler on rule set failure. - `2`: Call handler on rule set success. |
| `HANDLER` | `VARCHAR(1024)` |  | Name of the PL/SQL function or procedure that defines the custom event handler logic. |
| `IS_STATIC` | `VARCHAR2(5)` |  | Indicates how often the rule set is evaluated during a user session. Possible values are: - `TRUE`: The rule set is evaluated once, and result of the rule set is reused throughout the user session. - `FALSE` (default): The rule set is evaluated each time it is accessed during the user session. |

## DVSYS.DBA\_DV\_RULE\_SET\_RULE View

The `DVSYS.DBA_DV_RULE_SET_RULE` data dictionary view lists rules that are associated with existing rule sets.

For example:

```
SELECT RULE_SET_NAME, RULE_NAME, RULE_EXPR FROM DVSYS.DBA_DV_RULE_SET_RULE
 WHERE RULE_NAME = 'Is Security Officer';
```

Output similar to the following appears:

```
RULE_SET_NAME                RULE_NAME          RULE_EXP
---------------------------- ------------------ ---------------------------------
Can Grant VPD Administration Is Security Owner  DBMS_MACUTL.USER_HAS_ROLE_
                                                VARCHAR('DV_OWNER',dvsys.dv_
                                                login_user) = 'Y'
```

Related Views

- DVSYS.DBA\_DV\_RULE View
- DVSYS.DBA\_DV\_RULE\_SET View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `RULE_SET_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the rule set that contains the rule. |
| `RULE_NAME` | `VARCHAR(90)` | `NOT NULL` | Name of the rule. |
| `RULE_EXPR` | `VARCHAR(1024)` | `NOT NULL` | PL/SQL expression that defines the rule listed in the `RULE_NAME` column. |
| `ENABLED` | `VARCHAR(1)` |  | Indicates whether the rule is enabled or disabled. `Y` (yes) enables the rule set; `N` (no) disables it. |
| `RULE_ORDER` | `NUMBER` | `NOT NULL` | The order in which rules are used within the rule set. Does not apply to this release. |

## DVSYS.DBA\_DV\_USER\_PRIVS View

The `DVSYS.DBA_DV_USER_PRIVS` data dictionary view lists the privileges for a database user account excluding privileges granted through the `PUBLIC` role.

For example:

```
SELECT USERNAME, ACCESS_TYPE, PRIVILEGE FROM DVSYS.DBA_DV_USER_PRIVS;
```

Output similar to the following appears:

```
USERNAME  ACCESS_TYPE          PRIVILEGE
--------- -------------------- ------------
DVSYS     DV_PUBLIC            EXECUTE
DVOWNER   DV_ADMIN             SELECT
SYS       SELECT_CATALOG_ROLE  SELECT
...
```

Related Views

- DVSYS.DBA\_DV\_PUB\_PRIVS View
- DVSYS.DBA\_DV\_ROLE View
- DVSYS.DBA\_DV\_USER\_PRIVS\_ALL View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR(30)` | `NOT NULL` | Name of the database schema account in which privileges have been defined. |
| `ACCESS_TYPE` | `VARCHAR(30)` |  | Role the database user account listed in the `USERNAME` column uses to access the database. Oracle Database Vault accounts have direct access. |
| `PRIVILEGE` | `VARCHAR(40)` | `NOT NULL` | Privilege granted to the user listed in the `USERNAME` column. |
| `OWNER` | `VARCHAR(30)` | `NOT NULL` | Name of the database user account. |
| `OBJECT_NAME` | `VARCHAR(30)` | `NOT NULL` | Name of the PL/SQL function or procedure used to define privileges. |

## DVSYS.DBA\_DV\_USER\_PRIVS\_ALL View

The `DVSYS.DBA_DV_USER_PRIVS_ALL` data dictionary view lists the privileges for a database account including privileges granted through `PUBLIC`.

For example:

```
SELECT USERNAME, ACCESS_TYPE, PRIVILEGE FROM DVSYS.DBA_DV_USER_PRIVS;
```

Output similar to the following appears:

```
USERNAME            ACCESS_TYPE  PRIVILEGE
------------------- ------------ -----------------
AMALCOLM_DVACCTMGR  CONNECT      CREATE_SESSION
LBROWN_DVOWNER      DIRECT       CREATE PROCEDURE
...
```

Related Views

- DVSYS.DBA\_DV\_PUB\_PRIVS View
- DVSYS.DBA\_DV\_ROLE View
- DVSYS.DBA\_DV\_USER\_PRIVS View

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR(30)` |  | Name of the database schema account in which privileges have been defined. |
| `ACCESS_TYPE` | `VARCHAR(30)` |  | Role the database user account listed in the `USERNAME` column uses to access the database. Oracle Database Vault accounts have direct access. |
| `PRIVILEGE` | `VARCHAR(40)` |  | Privilege granted to the user listed in the `USERNAME` column. |
| `OWNER` | `VARCHAR(30)` |  | Name of the database user account. |
| `OBJECT_NAME` | `VARCHAR(30)` |  | Name of the PL/SQL function or procedure used to define privileges. |