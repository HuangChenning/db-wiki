---
title: "Using the Oracle Database Vault PL/SQL Interfaces"
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/plsql_interfaces.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 15 Using the Oracle Database Vault PL/SQL Interfaces

This chapter contains:

## Oracle Database Vault Run-Time PL/SQL Procedures and Functions

Oracle Database Vault provides a set of procedural interfaces to administer various Database Vault security options and manage Database Vault security enforcements. There are also procedures and functions that expose the logic to validate a DDL command for realm violations and command authorizations. Additional procedures and functions are provided to set the value of a factor (assuming their associated rule sets evaluate to true) (for example, from a Web application), to retrieve the trust level for a session or specific factor identity, and to get the label for a factor identity. These procedures and functions are provided so that a database administrator does not grant the `EXECUTE` privilege on all `DVSYS` package procedures to the general database account population. The procedures and functions expose only the minimum methods that are required. All of these functions and procedures are publicly available for applications that need them.

Table 15-1 lists the default run-time PL/SQL procedures and functions.

Table 15-1 DVSYS Functions

| Procedure or Function | Parameter |
| --- | --- |
| SET\_FACTOR Procedure | Sets a factor |
| GET\_FACTOR Function | Retrieves a factor |
| GET\_TRUST\_LEVEL Function | Retrieves the trust level assigned to a factor |
| GET\_TRUST\_LEVEL\_FOR\_IDENTITY Function | Retrieves the trust level for a specified factor and an identity |
| ROLE\_IS\_ENABLED Function | Checks whether the specified database role is enabled |
| GET\_FACTOR\_LABEL Function | Retrieves the label for the specified factor when the factor has a label assigned to it for the specified Oracle Label Security policy |

### SET\_FACTOR Procedure

The `SET_FACTOR` procedure can be exposed to an application that requires the ability to set factor identities dynamically. It wraps the package procedure `DBMS_MACADM.SET_FACTOR`. When a factor has a rule set associated with it for assignment and if the rule set returns true, then the value is set. Normal rule set handling occurs, and the factor value (identity) validation method is called. This procedure is available (to execute) to the general database account population.

Syntax

```
DVSYS.SET_FACTOR(
  p_factor IN VARCHAR2, 
  p_value  IN VARCHAR2);
```

Parameters

Table 15-2 SET\_FACTOR Parameters

| Parameter | Description |
| --- | --- |
| `p_factor` | Factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` data dictionary view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `p_value` | Identity value, up to 1024 characters in mixed case.  To find the identities for each factor in the current database instance, query the `DVSYS.DBA_DV_IDENTITY` data dictionary view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md). |

Example

```
EXECUTE DVSYS.SET_FACTOR(''Sector2_ClientID'', ''identity'');
```

### GET\_FACTOR Function

The `GET_FACTOR` function is exposed to the `DVF` schema to allow the public factor functions to resolve the identity of a factor. This enables the `F$` functions in the `DVF` schema. This function is available (to execute) to the general database account population.

Syntax

```
DVSYS.GET_FACTOR(
  p_factor IN VARCHAR2)
RETURN VARCHAR2;
```

Parameter

Table 15-3 GET\_FACTOR Parameter

| Parameter | Description |
| --- | --- |
| `p_factor` | Factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` data dictionary view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Get Client ID Factor Identity',
  rule_expr => 'DVSYS.GET_FACTOR(''Sector2_ClientID'')');
END;
/
```

### GET\_TRUST\_LEVEL Function

The `GET_TRUST_LEVEL` function returns the trust level of the current session identity for the factor requested. This function is available (to execute) to the general database account population. See ["Creating and Configuring a Factor Identity"](cfgfact.md) for a listing of the available trust levels.

Syntax

```
DVSYS.GET_TRUST_LEVEL(
  p_factor IN VARCHAR2)
RETURN VARCHAR2;
```

Parameter

Table 15-4 GET\_TRUST\_LEVEL Parameter

| Parameter | Description |
| --- | --- |
| `p_factor` | Factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` data dictionary view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Get Client ID Trust Level',
  rule_expr => 'DVSYS.GET_TRUST_LEVEL(''Sector2_ClientID'')');
END;
/
```

### GET\_TRUST\_LEVEL\_FOR\_IDENTITY Function

The `GET_TRUST_LEVEL_FOR_IDENTITY` function returns the trust level for the factor and identity requested. This function is available (to execute) to the general database account population. See ["Creating and Configuring a Factor Identity"](cfgfact.md) for a listing of the available trust levels.

Syntax

```
DVSYS.GET_TRUST_LEVEL_FOR_IDENTITY(
  p_factor   IN VARCHAR2, 
  p_identity IN VARCHAR2)
RETURN VARCHAR2;
```

Parameters

Table 15-5 GET\_TRUST\_LEVEL\_FOR\_IDENTITY Parameters

| Parameter | Description |
| --- | --- |
| `p_factor` | Factor name.  To find existing factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md). |
| `p_identity` | Identity value.  To find the identities for each factor in the current database instance, use the `DVSYS.DBA_DV_IDENTITY` data dictionary view, described in ["DVSYS.DBA\_DV\_IDENTITY View"](views.md). |

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Get Client ID Identity Trust Level',
  rule_expr => 'DVSYS.GET_TRUST_LEVEL_FOR_IDENTITY(''Sector2_ClientID'', ''identity'')');
END;
/
```

### ROLE\_IS\_ENABLED Function

The `ROLE_IS_ENABLED` function returns a boolean value that specifies whether a database role has been enabled. This function is available (to execute) to the general database account population.

Syntax

```
DVSYS.ROLE_IS_ENABLED(
  p_role IN VARCHAR2)
RETURN BOOLEAN;
```

Parameter

Table 15-6 ROLE\_IS\_ENABLED Parameter

| Parameter | Description |
| --- | --- |
| `p_role` | Database role name to check.  To find existing roles, use the following data dictionary views:  - `DBA_ROLES`: Finds available roles in the current database instance. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). - `DVSYS.DBA_DV_REALM_AUTH`: Finds the authorization of a particular role. See ["DVSYS.DBA\_DV\_REALM View"](views.md). - `DVSYS.DBA_DV_ROLE`: Finds existing secure application roles used in privilege management. See ["DVSYS.DBA\_DV\_ROLE View"](views.md). |

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check if SYSADM Role Is Enabled',
  rule_expr => 'DVSYS.ROLE_IS_ENABLED(''SYSADM'')');
END;
/
```

### GET\_FACTOR\_LABEL Function

The `GET_FACTOR_LABEL` function returns the label for the specified factor when the factor has a label assigned to it for the specified Oracle Label Security policy. The function returns a label that is merged with the maximum session label for the policy if the policy is configured with Oracle Label Security. The function is available (to execute) to the general database population. See ["Label Identity"](cfgfact.md) for more information about factor labels.

Syntax

```
DVSYS.GET_FACTOR_LABEL(
  p_factor      IN VARCHAR2, 
  p_policy_name IN VARCHAR2)
RETURN VARCHAR2;
```

Parameters

Table 15-7 GET\_FACTOR\_LABEL Parameters

| Parameter | Description |
| --- | --- |
| `p_factor` | Factor name.  To find the available factors in the current database instance, query the `DVSYS.DBA_DV_FACTOR` data dictionary view. To find factors that are associated with Oracle Label Security policies, use `DVSYS.DBA_DV_MAC_POLICY_FACTOR`.  See ["DVSYS.DBA\_DV\_FACTOR View"](views.md) and ["DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR View"](views.md). |
| `p_policy_name` | Oracle Label Security policy name.  Use the following data dictionary views to find information about policies and factors in the current database instance:  - `DVSYS.DBA_DV_MAC_POLICY`: Lists Oracle Label Security policies defined in the current database instance. See ["DVSYS.DBA\_DV\_MAC\_POLICY View"](views.md). - `DVSYS.DBA_DV_MAC_POLICY_FACTOR`: Lists the factors that are associated with Oracle Label Security policies for the current database instance. See ["DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR View"](views.md). - `DVSYS.DBA_DV_POLICY_LABEL`: Lists the Oracle Label Security label for each factor identifier in the `DVSYS.DBA_DV_IDENTITY` view for each policy. See ["DVSYS.DBA\_DV\_POLICY\_LABEL View"](views.md). |

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Get the ClientID Factor Label',
  rule_expr => 'DVSYS.GET_FACTOR_LABEL(''Sector2_ClientID'', ''Access Locations'')');
END;
/
```

## Oracle Database Vault PL/SQL Factor Functions

In addition to the functions and procedures made available from the `DVSYS` schema, the `DVF` schema contains a single function for each factor defined in the system. Oracle Database Vault maintains these functions when you use the `DBMS_MACADM` PL/SQL package to manage the various factors. The functions are then available to the general database account population through PL/SQL functions and standard SQL. This enables factors to be used in Oracle Label Security, Oracle Virtual Private Database (VPD), and so on.

Typically, you can incorporate these functions into rule expressions. For example:

```
BEGIN
 DBMS_MACADM.CREATE_RULE(
 rule_name => 'Not Internal DBA',
 rule_expr => 'DVF.F$SESSION_USER NOT IN (''JSMTIH'', ''TBROWN'')');
END;
/
```

To find the value of a factor function, select from the `DUAL` system table. For example:

```
SELECT DVF.F$SESSION_USER FROM DUAL;

F$SESSION_USER
------------------------------------------------
LBROWN_DVOWNER
```

The name of the factor itself is case-insensitive. For example, the following statements return the same result

```
select dvf.f$session_user from dual;

SELECT DVF.F$SESSION_USER FROM DUAL;
```

Table 15-8 lists the default factor functions.

Table 15-8 Installed Oracle Database Vault Factor Functions

| DVF Factor Function | Description |
| --- | --- |
| F$AUTHENTICATION\_METHOD Function | Returns the method of authentication in `VARCHAR2` data type. In the list that follows, the type of user is followed by the method returned |
| F$CLIENT\_IP Function | Returns the IP address of the computer from which the client is connected |
| F$DATABASE\_DOMAIN Function | Returns the domain of the database as specified in the `DB_DOMAIN` initialization parameter |
| F$DATABASE\_HOSTNAME Function | Returns the host name of the computer on which the database instance is running |
| F$DATABASE\_INSTANCE Function | Returns the database instance identification number of the current database instance |
| F$DATABASE\_IP Function | Returns the IP address of the computer on which the database instance is running |
| F$DATABASE\_NAME Function | Returns the name of the database as specified in the `DB_NAME` initialization parameter |
| F$DOMAIN Function | Returns a named collection of physical, configuration, or implementation-specific factors in the run-time environment (for example, a networked IT environment or subset of it) that operates at a specific sensitivity level |
| F$ENTERPRISE\_IDENTITY Function | Returns the enterprise-wide identity for a user |
| F$IDENTIFICATION\_TYPE Function | Returns the way the schema of a user was created in the database. Specifically, it reflects the `IDENTIFIED` clause in the `CREATE USER` or `ALTER USER` syntax. |
| F$LANG Function | Returns the ISO abbreviation for the language name, a shorter form than the existing `LANGUAGE` parameter |
| F$LANGUAGE Function | Returns the language and territory currently used by your session, in `VARCHAR2` data type, along with the database character set |
| F$MACHINE Function | Returns the computer (host) name for the database client that established the database session. |
| F$NETWORK\_PROTOCOL Function | Returns the network protocol being used for communication, as specified in the `PROTOCOL` = `protocol` portion of the connect string |
| F$PROXY\_ENTERPRISE\_IDENTITY Function | Returns the Oracle Internet Directory distinguished name (DN) when the proxy user is an enterprise user |
| F$SESSION\_USER Function | Returns the database user name by which the current user is authenticated |

### F$AUTHENTICATION\_METHOD Function

The `F$AUTHENTICATION_METHOD` function returns the method of authentication in `VARCHAR2` data type. In the list that follows, the type of user is followed by the method returned:

- Password-authenticated enterprise user, local database user, or `SYSDBA` / `SYSOPER` using Password File; proxy with user name using password: `PASSWORD`
- Kerberos-authenticated enterprise or external user: `KERBEROS`
- SSL-authenticated enterprise or external user: `SSL`
- Radius-authenticated external user: `RADIUS`
- Operating system-authenticated external user or `SYSDBA` / `SYSOPER`: `OS`
- DCE-authenticated external user: `DCE`
- Proxy with certificate, distinguished name (DN), or user name without using password: `NONE`

You can use `IDENTIFICATION_TYPE` to distinguish between external and enterprise users when the authentication method is Password, Kerberos, or SSL.

Syntax

```
DVF.F$AUTHENTICATION_METHOD () 
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check SSL Authentication Method',
  rule_expr => 'DVF.F$AUTHENTICATION_METHOD = ''SSL''');
END;
/
```

### F$CLIENT\_IP Function

The `F$CLIENT_IP` function returns the IP address of the computer from which the client is connected, in `VARCHAR2` data type.

Syntax

```
DVF.F$CLIENT_IP ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Client IP Address',
  rule_expr => 'DVF.F$CLIENT_IP BETWEEN ''192.0.2.10'' AND ''192.0.2.20''');
END;
/
```

### F$DATABASE\_DOMAIN Function

The `F$DATABASE_DOMAIN` function returns the domain of the database as specified in the `DB_DOMAIN` initialization parameter, in `VARCHAR2` data type.

Syntax

```
DVF.F$DATABASE_DOMAIN ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Client Database Domain',
  rule_expr => 'DVF.F$DATABASE_DOMAIN NOT IN (''EXAMPLE'', ''YOURDOMAIN'')');
END;
/
```

### F$DATABASE\_HOSTNAME Function

The `F$DATABASE_HOSTNAME` function returns the host name of the computer on which the instance is running, in `VARCHAR2` data type.

Syntax

```
DVF.F$DATABASE_HOSTNAME ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Host Name',
  rule_expr => 'DVF.F$DATABASE_HOSTNAME IN (''SHOBEEN'', ''MAU'')');
END;
/
```

### F$DATABASE\_INSTANCE Function

The `F$DATABASE_INSTANCE` function returns the instance identification number of the current database instance, in `VARCHAR2` data type.

Syntax

```
DVF.F$DATABASE_INSTANCE ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Database Instance ID',
  rule_expr => 'DVF.F$DATABASE_INSTANCE = ''SALES_DB''');
END;
/
```

### F$DATABASE\_IP Function

The `F$DATABASE_IP` function returns the IP address of the computer on which the database instance is running, in `VARCHAR2` data type.

Syntax

```
DVF.F$DATABASE_IP ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Database IP address',
  rule_expr => 'DVF.F$DATABASE_IP = ''192.0.2.5''');
END;
/
```

### F$DATABASE\_NAME Function

The `F$DATABASE_NAME` function returns the name of the database as specified in the `DB_NAME` initialization parameter, in `VARCHAR2` data type.

Syntax

```
DVF.F$DATABASE_NAME ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Database DB_NAME Name',
  rule_expr => 'DVF.F$DATABASE_NAME = ''ORCL''');
END;
/
```

### F$DOMAIN Function

The `F$DOMAIN` function returns a named collection of physical, configuration, or implementation-specific factors in the run-time environment (for example, a networked IT environment or subset of it) that operates at a specific sensitivity level. The return type is `VARCHAR2`.

You can identify a domain using factors such as host name, IP address, and database instance names of the Oracle Database Vault nodes in a secure access path to the database. Each domain can be uniquely determined using a combination of the factor identifiers that identify the domain. You can use these identifying factors and possibly additional factors to define the Maximum Security Label within the domain. This restricts data access and commands, depending on the physical factors about the Oracle Database Vault session. Example domains of interest may be Corporate Sensitive, Internal Public, Partners, and Customers.

Syntax

```
DVF.F$DOMAIN ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Domain',
  rule_expr => 'DVF.F$DOMAIN = ''EXAMPLE.COM''');
END;
/
```

### F$ENTERPRISE\_IDENTITY Function

The `F$ENTERPRISE_IDENTITY` function returns the enterprise-wide identity for a user, in `VARCHAR2` data type:

- For enterprise users: the Oracle Internet Directory DN.
- For external users: the external identity (Kerberos principal name, Radius and DCE schema names, operating system user name, certificate DN).
- For local users and `SYSDBA` / `SYSOPER` logins: NULL.

The value of the attribute differs by proxy method:

- For a proxy with DN: the Oracle Internet Directory DN of the client.
- For a proxy with certificate: the certificate DN of the client for external users; the Oracle Internet Directory DN for global users.
- For a proxy with user name: the Oracle Internet Directory DN if the client is an enterprise user; NULL if the client is a local database user.

Syntax

```
DVF.F$ENTERPRISE_IDENTITY ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check User Enterprise Identity',
  rule_expr => 'DVF.F$ENTERPRISE_IDENTITY NOT IN (''JSMITH'', ''TSMITH'')');
END;
/
```

### F$IDENTIFICATION\_TYPE Function

The `F$IDENTIFICATION_TYPE` function returns the way the schema of a user was created in the database. Specifically, it reflects the `IDENTIFIED` clause in the `CREATE` / `ALTER USER` syntax. The return type is `VARCHAR2`. In the list that follows, the syntax used during schema creation is followed by the identification type returned:

- `IDENTIFIED BY` `password``:` `LOCAL`
- `IDENTIFIED EXTERNALLY``:` `EXTERNAL`
- `IDENTIFIED GLOBALLY``:` `GLOBAL SHARED`
- `IDENTIFIED GLOBALLY` `AS DN: GLOBAL PRIVATE`

Syntax

```
DVF.F$IDENTIFICATION_TYPE ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check User Schema Creation Type',
  rule_expr => 'DVF.F$IDENTIFICATION_TYPE = ''GLOBAL SHARED''');
END;
/
```

### F$LANG Function

The `F$LANG` function returns the ISO abbreviation for the language name, a shorter form than the existing `LANGUAGE` parameter, for the session of the user. The return type is `VARCHAR2`.

See [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for a listing of supported languages for Oracle Database.

Syntax

```
DVF.F$LANG ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check ISO Abbreviated Language Name',
  rule_expr => 'DVF.F$LANG IN (''EN'', ''DE'', ''FR'')');
END;
/
```

### F$LANGUAGE Function

The `F$LANGUAGE` function returns the language and territory currently used by a user session, in `VARCHAR2` data type, along with the database character set, in the following form:

`language_territory.characterset`

See [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for a listing of supported languages and territories for Oracle Database.

Syntax

```
DVF.F$LANGUAGE ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Session Language and Territory',
  rule_expr => 'DVF.F$LANGUAGE = ''AMERICAN_AMERICA.WE8ISO8859P1''');
END;
/
```

### F$MACHINE Function

The `F$MACHINE` function returns the computer (host) name for the database client that established the database session. The return type is `VARCHAR2`.

Syntax

```
DVF.F$MACHINE ()
RETURN VARCHAR2;
```

Parameter

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Client Computer Host Name',
  rule_expr => 'DVF.F$MACHINE NOT IN (''SHOBEEN'', ''SEBASTIAN'')');
END;
/
```

### F$NETWORK\_PROTOCOL Function

The `F$NETWORK_PROTOCOL` function returns the network protocol being used for communication, as specified in the `PROTOCOL` = `protocol` portion of the connect string. The return type is `VARCHAR2`.

Syntax

```
DVF.F$NETWORK_PROTOCOL ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Network Protocol',
  rule_expr => 'DVF.F$NETWORK_PROTOCOL = ''TCP''');
END;
/
```

### F$PROXY\_ENTERPRISE\_IDENTITY Function

The `F$PROXY_ENTERPRISE_IDENTITY` function returns the Oracle Internet Directory distinguished name (DN) when the proxy user is an enterprise user. The return type is `VARCHAR2`.

Syntax

```
DVF.F$PROXY_ENTERPRISE_IDENTITY ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Get OID DN of Enterprise User',
  rule_expr => 'DVF.F$PROXY_ENTERPRISE_IDENTITY = ''cn=Provisioning Admins''');
END;
/
```

### F$SESSION\_USER Function

The `F$SESSION_USER` function returns the database user name by which the current user is authenticated. This value remains the same throughout the session. The return type is `VARCHAR2`.

Syntax

```
DVF.F$SESSION_USER ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Database User Name',
  rule_expr => 'DVF.F$SESSION_USER IN (''JSMITH'', ''TSMITH'')');
END;
/
```

## Oracle Database Vault PL/SQL Rule Functions

Oracle Database Vault provides a set of functions that you can use in rule sets to inspect the SQL statement that you want the rule set to protect. For example, if a rule set protects `SELECT ON HR.EMPLOYEES` under a command rule, then you could use these functions to make more informed decisions in the rule expression.

Table 15-9 lists the default rule functions.

Table 15-9 Installed Oracle Database Vault PL/SQL Rule Set Functions

| Rule Set Function | Description |
| --- | --- |
| DV\_SYSEVENT Function | Returns the system event firing the rule set |
| DV\_LOGIN\_USER Function | Returns the login user name |
| DV\_INSTANCE\_NUM Function | Returns the database instance number |
| DV\_DATABASE\_NAME Function | Returns the database name |
| DV\_DICT\_OBJ\_TYPE Function | Returns the type of the dictionary object on which the database operation occurred (for example, table, procedure, view) |
| DV\_DICT\_OBJ\_OWNER Function | Returns the owner of the dictionary object on which the database operation occurred |
| DV\_DICT\_OBJ\_NAME Function | Returns the name of the dictionary object on which the database operation occurred |
| DV\_SQL\_TEXT Function | Returns the first 4000 characters of SQL text of the database statement used in the operation |

### DV\_SYSEVENT Function

The `DV_SYSEVENT` function returns the system event firing the rule set, in `VARCHAR2` data type. The event name is the same as that in the syntax of the SQL statement (for example, `INSERT`, `CREATE`.)

Syntax

```
DVSYS.DV_SYSEVENT ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Get System Event Firing the Maintenance Rule Set',
  rule_expr => 'DVSYS.DV_SYSEVENT = ''CREATE''');
END;
/
```

### DV\_LOGIN\_USER Function

The `DV_LOGIN_USER` function returns the login user name, in `VARCHAR2` data type.

Syntax

```
DVSYS.DV_LOGIN_USER ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check System Login User Name',
  rule_expr => 'DVSYS.DV_LOGIN_USER = ''SEBASTIAN''');
END;
/
```

### DV\_INSTANCE\_NUM Function

The `DV_INSTANCE_NUM` function returns the database instance number, in `NUMBER` data type.

Syntax

```
DVSYS.DV_INSTANCE_NUM ()
RETURN NUMBER;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Database Instance Number',
  rule_expr => 'DVSYS.DV_INSTANCE_NUM BETWEEN 6 AND 9');
END;
/
```

### DV\_DATABASE\_NAME Function

The `DV_DATABASE_NAME` function returns the database name, in `VARCHAR2` data type.

Syntax

```
DVSYS.DV_DATABASE_NAME ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Database Name',
  rule_expr => 'DVSYS.DV_DATABASE_NAME = ''ORCL''');
END;
/
```

### DV\_DICT\_OBJ\_TYPE Function

The `DV_DICT_OBJ_TYPE` function returns the type of the dictionary object on which the database operation occurred (for example, table, procedure, or view). The return type is `VARCHAR2`.

Syntax

```
DVSYS.DV_DICT_OBJ_TYPE ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Dictionary Object Type',
  rule_expr => 'DVSYS.DV_DICT_OBJ_TYPE IN (''TABLE'', ''VIEW'')');
END;
/
```

### DV\_DICT\_OBJ\_OWNER Function

The `DV_DICT_OBJ_OWNER` function returns the name of the owner of the dictionary object on which the database operation occurred. The return type is `VARCHAR2`.

Syntax

```
DVSYS.DV_DICT_OBJ_OWNER ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Dictionary Object Owner',
  rule_expr => 'DVSYS.DV_DICT_OBJ_OWNER = ''JSMITH''');
END;
/
```

### DV\_DICT\_OBJ\_NAME Function

The `DV_DICT_OBJ_NAME` function returns the name of the dictionary object on which the database operation occurred. The return type is `VARCHAR2`.

Syntax

```
DVSYS.DV_DICT_OBJ_NAME ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check Dictionary Object Name',
  rule_expr => 'DVSYS.DV_DICT_OBJ_NAME = ''SALES''');
END;
/
```

### DV\_SQL\_TEXT Function

The `DV_SQL_TEXT` function returns the first 4000 characters of SQL text of the database statement used in the operation The return type is `VARCHAR2`.

Syntax

```
DVSYS.DV_SQL_TEXT ()
RETURN VARCHAR2;
```

Parameters

None.

Example

```
BEGIN 
 DBMS_MACADM.CREATE_RULE(
  rule_name => 'Check SQL Text',
  rule_expr => 'DVSYS.DV_SQL_TEXT = ''SELECT SALARY FROM HR.EMPLOYEES''');
END;
/
```

## Oracle Database Vault PL/SQL Packages

Oracle Database Vault provides a collection of PL/SQL package APIs to support the maintenance and run-time behavior of Oracle Database Vault. Table 15-10 lists these packages. [Chapter 12, "Using the DBMS\_MACADM Package,"](apis_dbms_macadm.md) describes these packages in detail.

Table 15-10 Oracle Database Vault Administrator and Run-Time PL/SQL Packages

| Package | Description |
| --- | --- |
| `DBMS_MACADM` | Provides for the administration of all aspects of the secure and access control configuration data. The realm owner of the Oracle Database Vault realm can grant the ability to run this package.  See [Chapter 12, "Using the DBMS\_MACADM Package,"](apis_dbms_macadm.md) for more information. |
| `DBMS_MACSEC_ROLES` | Provides the `CAN_SET_ROLE` method to check whether the user invoking the method is authorized to use the specified Oracle Database Vault secure application role. The authorization is determined by checking the rule set associated with the role.  The API also provides a method to issue the `SET ROLE` statement for a Oracle Database Vault Secure Application Role. Before `SET ROLE` is issued, the `CAN_SET_ROLE` method is called to check the rule set associated with the role. Run-time rule set behavior such as auditing, failure processing, and event handling occur during this process. The package is available to the general database account population.  See [Chapter 13, "Using the DBMS\_MACSEC\_ROLES Package,"](apis_macsec_roles.md) for more information. |
| `DBMS_MACUTL` | Defines several constants and utility methods that are commonly used by other Oracle Database Vault packages, such as code/message lookup, error handling, data conversion, and privilege checks. This package can be run by the general database account population. This allows for security developers to leverage the constants in scripted configuration files. Utility methods such as `USER_HAS_ROLE` can also be used in Oracle Database Vault rules.  See [Chapter 14, "Using the DBMS\_MACUTL Package,"](apis_dbms_macutl.md) for more information. |

Note:

There are several procedures in the `DBMS_MACADM` package that are not exposed in the Oracle Database Vault Administration Web application. The procedures that are not exposed include: