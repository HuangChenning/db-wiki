---
title: Configuring Factors
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/cfgfact.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 7 Configuring Factors

This chapter contains:

## What Are Factors?

A factor is a named variable or attribute, such as a user location, database IP address, or session user, that Oracle Database Vault can recognize. You can use factors for activities such as authorizing database accounts to connect to the database or creating filtering logic to restrict the visibility and manageability of data.

Oracle Database Vault provides a selection of factors that lets you set controls on such components as the domain for your site, IP addresses, databases, and so on. "Default Factors" describes the default factors in detail. You also can create custom factors, using your own PL/SQL retrieval methods.

You can use factors in combination with rules in rule sets. The `DVF` factor functions described in ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md) are factor-specific functions that you can use in rule expressions.

Factors have values (identities) and are further categorized by their factor types. "Factor Identification" explains more about factor identities. See "Factor Type" under "General" for information about factor types.

You also can integrate factors with Oracle Label Security labels. ["Integrating Oracle Database Vault with Oracle Label Security"](dv_ols.md) explains how. See ["Tutorial: Integrating Oracle Database Vault with Oracle Label Security"](dv_ols.md) for more information.

You can run reports on the factors that you create in Oracle Database Vault. See "Related Reports and Data Dictionary Views" for more information.

This chapter explains how to configure factors by using Oracle Database Vault Administrator. To configure factors by using the PL/SQL packages and interfaces provided by Oracle Database Vault, refer to the following chapters:

- [Chapter 12, "Using the DBMS\_MACADM Package"](apis_dbms_macadm.md)
- [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces"](plsql_interfaces.md)

## Default Factors

Oracle Database Vault provides a set of default factors. For each of these factors, there is an associated function that retrieves the value of the factor. See ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md) for a listing of these functions.

You can create custom factors by using your own PL/SQL retrieval methods. A useful PL/SQL function you can use (which is used for many of the default factors) is the `SYS_CONTEXT` SQL function, which retrieves data about the user session. After you create the custom factor, you can query its values similar to the functions used to query the default factors. "Tutorial: Preventing Ad Hoc Tool Access to the Database" shows an example of how to create and query a custom factor.

See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions184.htm#SQLRF06117) for more information about the `SYS_CONTEXT` function.

You can use the default factors in your own security configurations. If you do not need them, you can remove them. (That is, they are not needed for internal use by Oracle Database Vault.)

The default factors are as follows:

- Authentication\_Method: Is the method of authentication. In the list that follows, the type of user is followed by the method returned:
	- Password-authenticated enterprise user, local database user, or `SYSDBA` / `SYSOPER` using Password File; proxy with user name using password: `PASSWORD`
		- Kerberos-authenticated enterprise or external user: `KERBEROS`
		- SSL-authenticated enterprise or external user: `SSL`
		- Radius-authenticated external user: `RADIUS`
		- Operating system-authenticated external user or `SYSDBA` / `SYSOPER`: `OS`
		- DCE-authenticated external user: `DCE`
		- Proxy with certificate, distinguished name (DN), or user name without using password: `NONE`
	You can use `IDENTIFICATION_TYPE` to distinguish between external and enterprise users when the authentication method is Password, Kerberos, or SSL.
- Client\_IP: Is the IP address of the machine from which the client is connected.
- Database\_Domain: Is the domain of the database as specified in the `DB_DOMAIN` initialization parameter.
- Database\_Hostname: Is the host name of the computer on which the instance is running.
- Database\_Instance: Is the instance identification number of the current instance.
- Database\_IP: Is the IP address of the computer on which the instance is running.
- Database\_Name: Is the name of the database as specified in the `DB_NAME` initialization parameter.
- Domain: Is a named collection of physical, configuration, or implementation-specific factors in the run-time environment (for example, a networked IT environment or subset of it) that operates at a specific sensitivity level. You can identify a domain using factors such as host name, IP address, and database instance names of the Database Vault nodes in a secure access path to the database. Each domain can be uniquely determined using a combination of the factor identifiers that identify the domain. You can use these identifying factors and possibly additional factors to define the Maximum Security Label within the domain. This restricts data access and commands, depending on the physical factors about the Database Vault session. Example domains of interest may be Corporate Sensitive, Internal Public, Partners, and Customers.
- Enterprise\_Identity: Is the enterprise-wide identity for the user:
	- For enterprise users: the Oracle Internet Directory-distinguished name (DN).
		- For external users: the external identity (Kerberos principal name, Radius and DCE schema names, operating system user name, certificate DN).
		- For local users and `SYSDBA` and `SYSOPER` logins: NULL.
	The value of the attribute differs by proxy method:
	- For a proxy with DN: the Oracle Internet Directory DN of the client.
		- For a proxy with certificate: the certificate DN of the client for external users; the Oracle Internet Directory DN for global users.
		- For a proxy with user names: the Oracle Internet Directory DN if the client is an enterprise user; NULL if the client is a local database user.
- Identification\_Type: Is the way the user schema was created in the database. Specifically, it reflects the `IDENTIFIED` clause in the `CREATE` / `ALTER USER` syntax. In the list that follows, the syntax used during schema creation is followed by the identification type returned:
	- `IDENTIFIED BY` `password`: `LOCAL`
		- `IDENTIFIED EXTERNALLY`: `EXTERNAL`
		- `IDENTIFIED GLOBALLY`: `GLOBAL SHARED`
		- `IDENTIFIED GLOBALLY` `AS DN`: `GLOBAL PRIVATE`
- Lang: Is the ISO abbreviation for the language name, a shorter form than the existing `LANGUAGE` parameter.
- Language: Is the language and territory your session currently uses, along with the database character set, in the following form:
	```
	language_territory.characterset
	```
	For example:
	```
	AMERICAN_AMERICA.WE8MSWIN1252
	```
	Refer to [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information about languages, territories, and character sets.
- Machine: Is the host name for the database client that established the current session. If you must find out whether the computer was used for a client or server session, then you can compare this setting with the Database\_Hostname factor to make the determination.
- Network\_Protocol: Is the network protocol being used for communication, as specified in the `PROTOCOL=protocol` portion of the connect string.
- Proxy\_Enterprise\_Identity: Is the Oracle Internet Directory DN when the proxy user is an enterprise user.
- Proxy\_User: Is the name of the database user who opened the current session on behalf of `SESSION_USER`.
- Session\_User: Is the database user name by which the current user is authenticated. This value remains the same throughout the session.

## Creating a Factor

In general, to create a factor, you first create the factor itself, and then you edit the factor to include its identity. "Guidelines for Designing Factors" provides advice on designing factors.

To create a factor:

1. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. In the Administration page, under Database Vault Feature Administration, click Factors.
3. In the Factors page, click Create.
4. In the Create Factor page, enter the following settings, and then click OK:
	- General
		- Factor Identification
		- Evaluation
		- Factor Labeling
		- Retrieval Method
		- Validation Method
		- Assignment Rule Set
		- Audit Options
		- Error Options

General

In the General area, enter the following information:

- Name: Enter a name up to 28 characters in mixed-case, without spaces. Oracle Database Vault creates a valid Oracle identifier for the factor function to be created in the `DVF` schema based on the name of the factor chosen. For example, if you create a factor named `GetNetworkIP`, Oracle Database Vault creates the `DVF.F$GETNETWORKIP` function. This attribute is mandatory.
	Oracle suggests that you start the name with a noun and complete the name with a brief description of the derived value.
	["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md) describes the `DVF` factor functions.
- Description: Enter a text description of the factor. It can have up to 1024 characters in mixed-case. This attribute is optional.
- Factor Type: From the list, select the type or category of the factor. This attribute is mandatory.
	Factor types have a name and description and are used only to help classify factors. A factor type is the category name used to classify the factor. The default physical factor types include authentication method, host name, host IP address, instance identifiers, database account information, and others. You can create user-defined factor types, such as application name, certificate information, and so on in addition to the installed factor types, such as time and authentication method.
	You can find the factors that are associated with a particular factor type by querying the `DVSYS.DBA_DV_FACTOR` data dictionary view. For example:
	```
	SELECT NAME 
	FROM DVSYS.DBA_DV_FACTOR 
	WHERE FACTOR_TYPE_NAME='Authentication Method';
	```
	The output is:
	```
	NAME
	------------------------------
	Network_Protocol
	Authentication_Method
	Identification_Type
	```
	Note:
	To create user-defined factor types by using the Oracle Database Vault `DBMS_MACADM` package, use the `CREATE_FACTOR_TYPE` procedure, described in ["CREATE\_FACTOR\_TYPE Procedure"](apis_dbms_macadm.md).

Factor Identification

Under Factor Identification, select how to resolve the identity of a factor. This attribute is mandatory. The values are as follows:

- By Method: Default. Sets the factor identity by executing the PL/SQL expression specified in the Retrieval Method field.
	For example, suppose the expression retrieves the system date:
	```
	to_char(sysdate,'yyyy-mm-dd')
	```
	On December 6, 2009, the By Method option would return the following value:
	```
	2009-12-06
	```
- By Constant: Resolves the factor identity by retrieving the constant value found in the Retrieval Method field.
- By Factors: Determines the factor identity by mapping the identities of the child factor to its parent factor. A parent factor is a factor whose values are resolved based on a second factor, called a child factor. To establish their relationship, you map their identities. (You do not need to specify a Retrieval Method expression for this option.)
	See "Using Identity Mapping to Configure an Identity to Use Other Factors" for more information about mapping identities.

A factor identity is the actual value of a factor (for example, the IP address for a factor that uses the IP\_Address type). A factor can have several identities depending on its retrieval method or its identity mapping logic. For example, a factor such as Database\_Hostname could have multiple identities in an Oracle Real Application Clusters environment; a factor such as Client\_IP can have multiple identities in any RDBMS environment. The retrieval method for these types of factors may return different values because the retrieval method is based on the database session.

Several reports allow you to track the factor identity configuration. See "Related Reports and Data Dictionary Views" for more information.

You can configure the assignment of a factor in the following ways:

- Assign the factor at the time a database session is established.
- Configure individual requests to retrieve the identity of the factor.

With the Oracle Label Security integration, you can label identities with an Oracle Label Security label. You can also assign an identity trust levels, which are numbers that indicate the magnitude of trust relative to other identities for the same factor. In general, the higher the trust level number is set, the greater the trust. Negative trust levels are not trusted.

See Also:

"Adding an Identity to a Factor" for more information about factor identities

Within a database session, a factor assigned identity is available to Oracle Database Vault and any application with a publicly accessible PL/SQL function that exists in the `DVF` schema (which contains functions that retrieve factor values) as follows:

`dvf.f$` `factor_name`

This allows the identifier for a factor to be accessed globally from within the Oracle database (using PL/SQL, SQL, Oracle Virtual Private Database, triggers, and so on). For example, in SQL\*Plus:

```
CONNECT lbrown_dvowner
Enter password: password    

SELECT DVF.F$DATABASE_IP FROM DUAL;
```

Output similar to the following appears:

```
SELECT DVF.F$DATABASE_IP FROM DUAL;

F$DATABASE_IP
-------------------------------------------------------------
192.0.2.1
```

You can also use the `DVSYS.GET_FACTOR` function to find the identity of a factor that is made available for public access. For example:

```
SELECT GET_FACTOR('DATABASE_IP') FROM DUAL;
```

The following output appears:

```
GET_FACTOR('DATABASE_IP')
-------------------------------------------------------------
192.0.2.1
```

Evaluation

Under Evaluation, select how you want the factor to be evaluated and assigned an identity. See "How Factors Affect Performance" for the performance effect of session factors. This attribute is mandatory.

The values are as follows:

- By Session: Default. Evaluates the factor when a database session is created.
- By Access: Evaluates the factor each time it is accessed (for example, referenced by an application) and when the database session is first created.

Factor Labeling

Under Factor Labeling, select how you want the factor identity to retrieve an Oracle Label Security (OLS) label. This setting applies if you plan to use the Oracle Label Security integration. This attribute is mandatory if you want to use an OLS label. (See also ["Integrating Oracle Database Vault with Oracle Label Security"](dv_ols.md) for information on integrating OLS labels with a factors.

The values are as follows:

- By Self: Default. Labels the identities for the factor directly from the labels associated with an Oracle Label Security policy.
- By Factors: If there are multiple child factor labels, then Oracle Database Vault merges the labels by using the Oracle Label Security algorithm that is associated with the applicable Oracle Label Security policy. For each applicable Oracle Label Security policy, a factor identity can have an assigned label.

Retrieval Method

Under Retrieval Method, enter a PL/SQL expression that retrieves the identity of a factor or a constant. It can use up to 255 characters in mixed-case. The Retrieval Method identifies factors where the factor identification is by method or constant. If the factor identification is by factors, Oracle Database Vault identifies it by its identity mappings.

You can create your own PL/SQL retrieval methods, or use the functions supplied with Oracle Database Vault. See the following sections for factor-specific and general utility functions that you can use to build the retrieval method:

- ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md)
- ["Factor Procedures and Functions Within DBMS\_MACADM"](apis_dbms_macadm.md)
- [Chapter 14, "Using the DBMS\_MACUTL Package"](apis_dbms_macutl.md)

The following retrieval method sets a value of the DB\_NAME factor by retrieving the database name (DB\_NAME) from the `USERENV` namespace in a user's session.

```
UPPER(SYS_CONTEXT('USERENV','DB_NAME'))
```

See also the default factors provided with Oracle Database Vault for examples of retrieval methods. "Default Factors" describes these factors.

The Retrieval Method field is mandatory if you have selected the following settings under Factor Identification:

- By Method: Enter a method in the Retrieval Method field.
- By Constant: Enter a constant in the Retrieval Method field.

The value returned as the factor identity must be a `VARCHAR2` string or otherwise convertible to one.

You can include any package function or standalone function in the expression. Ensure that the expression is a fully qualified function, such as `schema`.`function_name`. Do not include complete SQL statements. If you are using application packages or functions, you must provide `DVSYS` with the `GRANT EXECUTE` privilege on the object.

Write the function signature using the following format:

```
FUNCTION GET_FACTOR RETURN VARCHAR2
```

Validation Method

Under Validation Method, enter a PL/SQL expression that returns a Boolean value (`TRUE` or `FALSE`) to validate the identity of a factor being retrieved (with the `DVSYS.GET_FACTOR` function) or the value to be assigned to a factor (with the `DVSYS.SET_FACTOR` function). If the method is evaluated to false for the value being retrieved or to be assigned, then the factor identity is set to null. This optional feature provides an additional level of assurance that the factor is properly retrieved and set. This field can have up to 255 characters in mixed-case.

You can include any package function or standalone function in the expression. Ensure that the expression is a fully qualified function, such as `schema`.`function_name`. Do not include complete SQL statements. If you are using application packages or functions, you must provide `DVSYS` with the `GRANT EXECUTE` privilege on the object.

Write the function using one of the following formats:

- `FUNCTION` `IS_VALID` `RETURN BOOLEAN`
	In this form, you can use the `DVF.F$` `factor_name` function inside the function logic. This is more appropriate for factors that are evaluated by session.
- `FUNCTION` `IS_VALID` `(``p_factor_value` `VARCHAR2``)` `RETURN BOOLEAN`
	In this form, the factor value is passed to the validation function directly. This is more appropriate for factors that are evaluated by access. It is also valid for factors evaluated by session.

See the following sections for factor-specific and general utility functions that you can use to build the validation method:

- ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md)
- ["Factor Procedures and Functions Within DBMS\_MACADM"](apis_dbms_macadm.md)
- [Chapter 14, "Using the DBMS\_MACUTL Package"](apis_dbms_macutl.md)

Assignment Rule Set

Under Assignment Rule Set, select a rule set from the list if you want to use a rule set to control when and how a factor identity is set. For example, you can use a rule set to determine when a database session originates from a known application server or program. [Chapter 5, "Configuring Rule Sets,"](cfrulset.md) explains how to create rule sets.

This attribute is particularly useful for situations where database applications, such as a Web application using a JDBC connection pool, must dynamically set a factor identity for the current database session. For example, a Web application may want to assign the geographic location for a database account logging in to the Web application. To do so, the Web application can use the JDBC Callable Statement, or Oracle Data Provider for.NET (ODP.NET) to execute the PL/SQL function `DVSYS.SET_FACTOR`, for example:

```
BEGIN 
 DVSYS.SET_FACTOR('GEO_STATE','VIRGINIA');
END;
```

Then you can create an assignment rule for the GEO\_STATE factor to allow or disallow the setting of the GEO\_STATE factor based on other factors or rule expressions. See "How Factors Are Set" for more information.

Audit Options

Under Audit Options, select from the settings to generate an audit trail. Oracle Database Vault writes the audit trail to the `DVSYS.AUDIT_TRAIL$` system file, described in [Appendix A, "Auditing Oracle Database Vault."](audplcy.md)

You can use the Factor Audit Report to display the generated audit records. (See "Related Reports and Data Dictionary Views" for more information.) In addition, you can select multiple audit options at a time. Each option is converted to a bit mask and added to determine the aggregate behavior. Note that there is little performance impact in auditing, unless the factor has errors. This attribute is mandatory. The values are as follows:

- Never: Does not audit.
- Always: Always creates an audit record when a factor is evaluated. You can select from the conditions, described next.
- Sometimes: Creates an audit record based on one or more conditions. When you select Sometimes, by default the Retrieval Error and Retrieval NULL options are selected.
	You can select from the following conditions listed next.

Conditions that you can select for the Always and Sometimes options are as follows:

- Retrieval Error: Creates an audit record when the identity of a factor cannot be resolved and assigned, due to an error (such as `No data found` or `Too many rows`).
- Retrieval NULL: Creates an audit record when the identity of a factor is resolved to `NULL`.
- Validation Error: Creates an audit record when the validation method (if provided) returns an error.
- Validation False: Creates an audit record when the validation method (if provided) returns `FALSE`.
- Trust Level NULL: Creates an audit record when the resolved identity of a factor has an assigned trust level of `NULL`.
	See "Creating and Configuring a Factor Identity" for more information about trust levels.
- Trust Level Less Than Zero: Creates an audit record when the resolved identity of a factor has an assigned trust level less than zero.

Error Options

Under Error Options, select from the following to specify the processing that occurs when a factory identity cannot be resolved. This attribute is mandatory.

The values are as follows:

- Show Error Message: Default. Displays an error message to the database session.
- Do Not Show Error Message: Does not display the error message.
	An advantage of selecting Do Not Show Error Message and then enabling auditing is that you can track the activities of a potential intruder. The audit report reveals the activities of the intruder, yet the intruder is unaware that you are doing this because he or she does not see any error messages.

After you have created a new factor, you are ready to configure its identity. To do so, edit the factor and then add its identity.

## Editing a Factor

To edit a factor:

1. In the Oracle Database Vault Administration page, select Factors.
2. In the Factors page, select the factor that you want to edit.
3. Click Edit.
4. Modify the factor as necessary, and then click OK.

See Also:

- "Creating a Factor" to modify the settings created for a new factor
- "Adding an Identity to a Factor" to add or modify an identity for the factor

## Adding an Identity to a Factor

After you create a new factor, you optionally can add an identity to it. An identity is the actual value of the factor. For example, the identity of an IP\_Address factor could be the IP address of 192.0.2.4.

This section contains:

- About Factor Identities
- Creating and Configuring a Factor Identity
- Using Identity Mapping to Configure an Identity to Use Other Factors

### About Factor Identities

A factor identity for a given database session is assigned at run time using the Factor Identification and Retrieval Method fields described in "Creating a Factor". You can further configure the identity for the following reasons:

- To define the known identities for a factor
- To add a trust level to a factor identity
- To add an Oracle Label Security label to a factor identity
- To resolve a factor identity through its child factors, by using Identity Mapping

See Also:

- "How Factors Work" for more information about how a factor behaves during a database session
- "Tutorial: Restricting User Activities Based on Session Data" for an example of how to create and use factor identities

### Creating and Configuring a Factor Identity

To create and configure an identity:

1. In the Oracle Database Vault Administration page, select Factors.
2. In the Factors page, select the factor to which you want to add the identity.
3. Click Edit.
4. In the Edit Factor page, scroll down to Identities and click Create.
5. In the Create Identity page, enter the following settings and then click OK:
	- General
		- Label Identity

General

Enter the following values:

- Value: Enter the value of the identity, up to 1024 characters in mixed-case. This attribute is mandatory.
- Trust Level: Select one of the following trust levels:
	- Very Trusted: Assigns a trust level value of 10
		- Trusted: Assigns a trust level value of 5
		- Somewhat Trusted: Assigns a trust level value of 1
		- Untrusted: Assigns a trust level value of -1
		- Trust Level Not Defined: Assigns a trust level value of `NULL` (default)

Trust levels enable you to assign a numeric value to indicate the measure of trust allowed. A trust value of 1 signifies some trust. A higher value indicates a higher level of trust. A negative value or zero indicates distrust. When the factor identity returned from a factor retrieval method is not defined in the identity, Oracle Database Vault automatically assigns the identity a negative trust level.

To determine the trust level of a factor identity at run time, you can use the `GET_TRUST_LEVEL` and `GET_TRUST_LEVEL_FOR_IDENTITY` functions in the `DVSYS` schema.

For example, suppose you have created a factor named Network. You can create the following identities for the Network factor:

- Intranet, with a trust level of 10
- VPN (virtual private network), with a trust level of 5
- Public, with a trust level of 1

You then can create rule expressions (or custom application code) that base policy decisions on the trust level. For example, you can use `DVSYS.GET_TRUST_LEVEL` to find trust levels greater than 5:

```
DVSYS.GET_TRUST_LEVEL('Network') > 5
```

Or, you can use a `SELECT` statement on the `DVSYS.DBA_DV_IDENTITY` data dictionary view to find trust levels for the Network factor greater than or equal to 5:

```
SELECT VALUE, TRUST_LEVEL FROM DVSYS.DBA_DV_IDENTITY 
   WHERE TRUST_LEVEL >= 5 
   AND FACTOR_NAME='Network'
```

Output similar to the following appears:

```
F$NETWORK GET_TRUST_LEVEL('NETWORK')
------------------------------------
VPN                                5
INTRANET                          10
```

In the preceding example, Network factor identity for VPN is trusted (value equals 5), and the identity for the INTRANET domain is 10, which implies a greater trust.

See [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces,"](plsql_interfaces.md) for more information about the Oracle Database Vault functions.

Label Identity

You can assign Oracle Label Security (OLS) labels to factor identities. (In brief, a label acts as an identifier for a database table row to assign privileges to the row. For more information about labels, see [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/toc.htm).) The Factor Labeling attribute for a factor determines whether a factor is labeled By Self or By Factors. If you set the Factor Labeling attribute to By Self, then you can associate OLS labels with the factor identities. If you set the Factor Labeling attribute to By Factors, then Oracle Database Vault derives the factor identity labels from the labeling of child factor identities. When there are multiple child factor identities with labels, Oracle Database Vault merges the labels using the OLS algorithm associated with the applicable factor Oracle Label Security policy.

To label an identity:

1. In the Create Identity page, under Label Identity, select the OLS label from the Available OLS Labels list.
	The list shows data labels from the Oracle Label Security installation for your site. For more information, refer to [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/toc.htm).
	Note:
	You can select multiple labels by holding down the Ctrl key as you click each label that is to be selected.
2. Click Move to move the OLS label to the Selected OLS Labels list.
3. Repeat Step [^1] and Step [^2] to select more OLS labels.
	You can select only one label for each OLS policy.
4. Click OK to finish labeling the identity.

Editing a Factor Identity

To edit a factor identity:

1. In the Edit Factor page, scroll down to Identities and select the identity you want to edit.
2. Click Edit.
3. In the Edit Identity page, modify the identity as necessary.
4. Click OK.

Deleting a Factor Identity

Before you delete a factor identity, you can locate the various references to it by querying the factor-related Oracle Database Vault views. See [Chapter 16, "Oracle Database Vault Data Dictionary Views,"](views.md) for more information.

To delete a factor identity:

1. In the Edit Factor page, scroll down to Identities and select the identity you want to remove.
2. Click Remove.
3. In the Confirmation page, click Yes.

### Using Identity Mapping to Configure an Identity to Use Other Factors

After you create, edit, and save the factor identity, you can map it. Identity mapping is the process of identifying a factor by using other (child) factors. This is a way to transform combinations of factors into logical identities for a factor or to transform continuous identity values (for example, temperature) or large discrete identity values (for example, IP address ranges) into logical sets. To check configuration issues in the mapping for an identity, see ["Identity Configuration Issues Report"](reports.md). See also "Tutorial: Restricting User Activities Based on Session Data" for an example of how to use identity mapping.

To map an identity to a factor:

1. Create a parent factor and set the attribute Factor Identification to By Factors.
	"Creating a Factor" describes how to create factors.
2. For the parent factor, create a new factor identity.
	"Creating and Configuring a Factor Identity" describes how to create an identity.
3. Map the factor-identity pair of the parent to the factor-identity pairs of its children. Use the following process:
	1. In the Factors page, select the parent factor from the Factors page and then click Edit.
		2. In the Edit Factor page, under Identities, select the parent factor identity and then click Edit.
		3. In the Edit Identity page, click Create under Map Identity.
		4. In the Create Identity Map page, select a factor name from the Contributing Factor list.
		This is the child factor to which you want to map the parent factor.
		5. Select a Map Condition.
		This setting lets you select an operator to compare the contributing (child) factor values.
		6. Enter a value for the Low Value and High Value (optional) fields.
		For example, consider a scenario where the Contributing Factor to the Factor Network is set to Client\_IP, the Map Condition is set to `Between`, the Low Value is set to 192.0.2.1 and the High Value is set to 192.0.2.24. This means that whenever the client IP address lies in the specified address range of 192.0.2.1 to 192.0.2.24, the parent factor evaluates to a predefined identity (for example, INTRANET).
		7. Click OK to map the parent factor-identity to the child factor-identity.
		You can map different identities of a parent factor to different identities of the contributing factor. For example, the INTRANET identity maps to an IP address range of 192.0.2.1 to 192.0.2.24. The REMOTE identity can map to an IP address range that excludes the address range 192.0.2.1 to 192.0.2.24.
		Based on identity mapping, you can create a security policy. For example, you can define a reduced set of privileges for an employee connecting over VPN (with REMOTE), as opposed to an employee connecting from within the corporate network (with INTRANET).
		8. Repeat Step c to Step g to add more contributing factors for a parent factor identity.
		For example, you can configure the Network factor to resolve to a value ACCOUNTING-SENSITIVE, when the Program factor resolves to "Oracle General Ledger" and the Client\_IP is in between 192.0.2.1 and 192.0.2.24. So, if an authorized accounting financial application program, running on a client with IP address 192.0.2.12 accesses the database, then the Network factor is resolved to ACCOUNTING-SENSITIVE. A database session with the ACCOUNTING-SENSITIVE Network value would have more access privileges than one with the INTRANET Network value.

## Deleting a Factor

Before you delete a factor, you can locate the various references to the factor and its identities by querying the factor-related Oracle Database Vault views. See [Chapter 16, "Oracle Database Vault Data Dictionary Views,"](views.md) for more information.

To delete a factor:

1. Delete any references to the factor, such as factor identities, and Oracle Label Security policy associations.
	You cannot delete a factor that has references.
2. In the Oracle Database Vault Administration page, select Factors.
3. In the Factors page, select the factor that you want to remove.
4. Click Remove.
5. In the Confirmation page, click Yes.

## How Factors Work

The following topics in this section explain how Oracle Database Vault processes factors:

- How Factors Are Processed When a Session Is Established
- How Factors Are Retrieved
- How Factors Are Set

### How Factors Are Processed When a Session Is Established

When a database session is established, the following actions occur:

1. At the start of each database session, Oracle Database Vault begins to evaluate all default and user-created factors in the database instance.
	This evaluation occurs after the normal database authentication of the session and the initialization of the Oracle Label Security session information, if applicable.
2. In the factor evaluation stage, the factor initialization process executes the retrieval method for all factors that are identified by methods or constants, to resolve the factor identity for the session.
	The factor error options setting has no effect on the factor initialization process.
3. If a factor has a validation method defined, Oracle Database Vault validates the identity (value) of the factor by executing this validation method. If the validation method fails or returns false, the identity of the factor is undefined (`NULL`).
4. If a factor has any identities defined for it, Oracle Database Vault resolves the trust level of the factor based on the identities defined. If an identity of the factor is defined in this list of defined identities, then Oracle Database Vault assigns the trust level as configured; otherwise it sets it to -1. If there are no identities defined for the factor, the trust level is undefined (`NULL`).
5. Depending on the outcome of this factor evaluation, factor validation, and trust level resolution, Database Vault audits the details of the evaluation as dictated by the factor audit configuration.
6. When the evaluation of all factors that are identified by method or constant completes, Oracle Database Vault resolves the factors that are identified by other factors by using the identity maps that are defined for the factor configured identities.
	The evaluation order of the factor-configured identities is by ASCII sort on the identity values: Oracle Database Vault uses the first alphabetically sorted identity mapping that it evaluates. For example, suppose factor TEST has identities X and Y. Furthermore, identities X and Y have identity maps that are dependent on identities for factors A, B, and C. The following mapping occurs:
	- X is mapped when A=1 and B=1
		- Y is mapped when A=1, B=1, and C=2
	In this case, the first one evaluated is X. Y is not evaluated, but what if its C mapping meets the criteria that is needed for the TEST factor's success? You would need to reverse the mapping, that is, map Y before X so that A, B, and C can be evaluated first. To reverse the mapping, rename Y to V (or some alphabetic value that sorts before X) so that it can be correctly resolved.
	This algorithm works if the ASCII sort ordering is correct and the identities map the same number factors at some level.
7. When the factor initialization completes, the Oracle Database Vault integration with Oracle Label Security occurs.

After this process completes, Oracle Database Vault checks to see if a command rule is associated with the `CONNECT` event. If a rule set associated with the `CONNECT` event, then Oracle Database Vault evaluates the rule set. If the rule set evaluates to false or results in an error, then the session is terminated. Oracle Database Vault executes any auditing or call handlers associated with the rule set before the session is terminated.

Note:

Be careful about associating command rules with the `CONNECT` event, because you can inadvertently lock out other users from of the database. In general, if you create a command rule for `CONNECT`, set its evaluation option of the associated rule set to `Any True`.

If you do inadvertently lock out users, then you should temporarily disable Oracle Database Vault, disable the CONNECT command rule, reenable Oracle Database Vault, and then fix the factor code that is causing the problem. "If the Test Fails" provides an example of how to accomplish this.

### How Factors Are Retrieved

You can retrieve a factor in a database session at any time by using the `DVF` factor function or the `DVSYS.GET_FACTOR` function. To find a listing of available factors, query the `DVS.DBA_DV_FACTOR` data dictionary view, described in ["DVSYS.DBA\_DV\_FACTOR View"](views.md).

Example 7-1 shows an example of using the `DVSYS.GET_FACTOR` function.

Example 7-1 Using DVSYS.GET\_FACTOR to Retrieve a Factor

```
SELECT GET_FACTOR('client_ip') FROM DUAL;
```

You can use the factor values retrieved from the `DVF` factor function or the `DVSYS.GET_FACTOR` in the following ways:

- Oracle Database Vault rule expressions
- Custom application code that is available to all database sessions in an Oracle Database Vault environment

["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md) describes `DVF` factor functions in detail.

If you had set the factor evaluation to By Session, then Oracle Database Vault retrieves the value from the session context established, as described under "How Factors Are Processed When a Session Is Established".

If you had set the factor evaluation to By Access, then Oracle Database Vault performs Step [^3] through Step [^4] (or Step [^5]), as described under "How Factors Are Processed When a Session Is Established", whenever the factor is retrieved.

If you had defined error options for the factor and if an error occurs, then Oracle Database Vault displays the error message.

### How Factors Are Set

You can have a factor identity assigned at any time during a database session, but only if you have defined a factor assignment rule set and that rule set evaluates to true. You can do this in the application code by using the `DVSYS.SET_FACTOR` function. In Java code, you can use the JDBC class `java.sql.CallableStatement` to set this value. For example:

```
java.sql.Connection connection ; 
...
java.sql.CallableStatement statement = 
   connection.prepareCall("{call DVSYS.SET_FACTOR('FACTOR_X', ?)}");
statement.setString(1, "MyValue");
boolean result = statement.execute();
...
```

Applications that can execute Oracle PL/SQL functions can use this procedure (for example, applications written using Oracle Data Provider for.NET (ODP.NET)).

This concept is similar to the standard Oracle `DBMS_SESSION.SET_IDENTIFIER` procedure with an added feature that a rule set controls when a factor value can be set. If the rule set evaluates to true, Steps [^3] through [^4] under "How Factors Are Processed When a Session Is Established" occur.

If you have not associated a assignment rule set for the factor or if the rule set returns false (or returns errors), then Oracle Database Vault sends an error message if you attempt to set the factor using the `DVSYS.SET_FACTOR` function.

## Tutorial: Preventing Ad Hoc Tool Access to the Database

In this section:

- About This Tutorial
- Step 1: Enable the SCOTT User Account
- Step 2: Create the Module Factor
- Step 3: Create the Limit SQL\*Plus Access Rule and Rule Set
- Step 4: Create the CONNECT Command Rule
- Step 5: Test the Ad Hoc Tool Access Restriction
- Step 6: Remove the Components for This Tutorial

See Also:

- "Tutorial: Restricting User Activities Based on Session Data" for an example of using factor identity mapping
- ["Tutorial: Integrating Oracle Database Vault with Oracle Label Security"](dv_ols.md) for an example of integrating an Oracle Database Vault factor with an Oracle Label Security label

### About This Tutorial

Many database applications contain features to explicitly control the actions of a user. However, an ad hoc query tool, such as SQL\*Plus, may not have these controls. As a result, a user could use an ad hoc tool to perform actions in the database that he or she would normally be prevented from performing in a regular database application. You can use a combination of Oracle Database Vault factors, rule sets, and command rules to prevent unauthorized access to the database by ad hoc query tools.

In the following tutorial, you limit the use of SQL\*Plus to only four users: the Database Vault Owner, the Database Vault Account Manager, `SYSTEM`, and `SYS`. To accomplish this, you must create a factor to find the applications on your system and a rule and rule set to limit SQL\*Plus to these four users. Then you create a command rule for the `CONNECT` SQL statement, which is associated with the rule set. When you successfully complete this tutorial, then only the administrative users you specify should be able to connect to the database using SQL\*Plus.

### Step 1: Enable the SCOTT User Account

You must use the `SCOTT` account later on when you test the Oracle Database Vault components for this tutorial, so ensure that this account is active.

1. Log in to SQL\*Plus as a user who has been granted the `DV_ACCTMGR` role.
	For example:
	```
	sqlplus amalcolm_dvacctmgr
	Enter password: password
	```
2. Check the status of the `SCOTT` account.
	```
	SELECT USERNAME, ACCOUNT_STATUS FROM DBA_USERS WHERE USERNAME = 'SCOTT';
	```
3. If the `SCOTT` account is expired and locked, then enter the following statement to make it active:
	```
	ALTER USER SCOTT ACCOUNT UNLOCK IDENTIFIED BY password;
	```
	Replace `password` with a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for the minimum requirements for creating passwords.

### Step 2: Create the Module Factor

The Module factor uses the `SYS_CONTEXT` SQL function to find the names of the applications that are used to access the current instance of Oracle Database. As described previously, the `SYS_CONTEXT` SQL function provides many useful methods for finding the state of a user session. `SYS_CONTEXT` is a valuable tool for creating custom factors. See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions184.htm#SQLRF06117) for more information about the `SYS_CONTEXT` function.

Note:

This type of factor is highly dependent on the security of the client session to ensure that it cannot be faked. See My Oracle Support (formerly OracleMetaLink) Note 281229.1 for more information. You can access My Oracle Support from the following Web site:

[`https://support.oracle.com">>https://support.oracle.com`](https://support.oracle.com/)

1. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. In the Administration page, select Factors.
	The Factors page appears.
3. Click Create to display the Create Factor page.
4. Enter the following information:
	- Name: Enter `Module`.
		- Description: Enter `Factor to find applications that can access Oracle Database`.
		- Factor Type: From the list, select Application.
		- Factor Identification: Select By Method.
		- Evaluation: Select By Access.
		- Factor Labeling: Select By Self.
		- Retrieval Method: Enter the following retrieval method:
		```
		UPPER(SYS_CONTEXT('USERENV', 'MODULE'))
		```
		- Validation Method: Leave blank.
		- Assignment Rule Set: From the list, select \<Non Selected>.
		- Audit Options: Select Never.
		- Error Options: Select Show Error Message.
5. Click OK.
	Oracle Database Vault creates the factor. You now can query for the factor using the same syntax you would use to query the default factors, described ["Oracle Database Vault PL/SQL Factor Functions"](plsql_interfaces.md).
6. In SQL\*Plus, perform a quick test of the Module factor.
	For example:
	```
	sqlplus lbrown_dvowner
	Enter password: password
	SELECT DVF.F$MODULE FROM DUAL;
	```
	The following output should appear:
	```
	F$MODULE
	-----------------------------
	SQLPLUS.EXE
	```
	Do not exit SQL\*Plus. You must use it later on when you test the factor components.

### Step 3: Create the Limit SQL\*Plus Access Rule and Rule Set

1. In Oracle Database Vault Administrator, return to the Administration page.
2. Under Administration, select Rule Sets.
	The Rule Sets page appears.
3. Click Create to display the Create Rule Set page.
4. Enter the following settings:
	- Name: Enter `Limit SQL*Plus Access`.
		- Description: Enter `Rule set to limit access to SQL*Plus`.
		- Status: Select Enabled.
		- Evaluation Options: Select All True.
		- Audit Options: Select Audit Disabled.
		- Error Handling Options: Select Show Error Message.
		- Fail Code, Fail Message: Leave blank.
		- Custom Event Handler Option: Select Handler Disabled.
		- Custom Event Handler Logic: Leave blank.
5. Click OK.
	The Rule Sets page appears.
6. Select the Limit SQL\*Plus rule set and then click Edit.
	The Edit Rule Set page appears.
7. Under Rules Associated To The Rule Set, click Create.
	The Create Rule page appears.
8. Enter the following settings:
	- Name: Enter `Prevent non-admin access to SQL*Plus`.
		- Rule Expression: Enter the following rule expression:
		```
		DVF.F$MODULE = 'SQL*PLUS.EXE' AND DVF.F$SESSION_USER IN ('LBROWN_DVOWNER', 'AMALCOLM_DVACCTMGR', 'SYS', 'SYSTEM')
		```
		Replace `LBROWN_DVOWNER` and `AMALCOLM_DVACCTMGR` with the user account names that you use for the Database Vault Owner and Database Vault Account Manager accounts. You must enter the user account names in upper case letters, because that is how the database stores user account names.
		This expression tells Oracle Database Vault only to allow these four users to use SQL\*Plus. Another way to write the expression is to tell Database Vault to simply exclude certain users from using SQL\*Plus. That way, everyone else has access to SQL\*Plus. For example, to exclude users `JSMITH` and `TSMITH` from using SQL\*Plus, you would create this expression:
		```
		DVF.F$MODULE != 'SQL*PLUS.EXE' AND DVF.F$SESSION_USER NOT IN ('JSMITH', 'TSMITH')
		```
		However, for this tutorial, use the first expression, in which only the four administrative users are allowed to use SQL\*Plus.
9. Ensure that you have entered this rule expression exactly as shown in Step [^6]. If you enter it incorrectly, you cannot log in to SQL\*Plus.
10. Click OK.

### Step 4: Create the CONNECT Command Rule

The CONNECT command rule controls the `CONNECT` SQL statement. It also applies to logging into SQL\*Plus from the command line or other tools your site may use to access SQL\*Plus.

1. In Oracle Database Vault, return to the Administration page.
2. Select Command Rules.
	The Command Rules page appears.
3. Click Create to display the Create Command Rule page.
4. Enter the following settings:
	- Command: Select CONNECT from the list.
		- Status: Select Enabled.
		- Object Owner, Object Name: Set to % so that the command rule applies to anyone who logs in.
		- Rule Set: Select Limit SQL\*Plus Access from the list.
5. Click OK.

### Step 5: Test the Ad Hoc Tool Access Restriction

You have been logged in to SQL\*Plus all along, but note that you do not need to restart your SQL\*Plus session in order for the Oracle Database Vault changes to take effect. They take effect right away.

1. In SQL\*Plus, try to connect as user `SCOTT`:
	```
	CONNECT SCOTT
	Enter password: password
	```
	The following output should appear:
	```
	ERROR:
	ORA-47400: Command Rule violation for CONNECT on LOGON
	Warning: You are no longer connected to ORACLE.
	```
	User `SCOTT` should be prevented from using SQL\*Plus.
2. Now try to connect as user `SYSTEM`:
	```
	CONNECT SYSTEM
	Enter password: password
	Connected.
	```
	User `SYSTEM` should be able to log in to SQL\*Plus. So should `SYS`, the Database Vault Owner account, and the Database Vault Account Manager account.

If the Test Fails

If you cannot log in to SQL\*Plus as `SYSTEM` (or as any of the other administrative users listed in your rule expression), then you are prevented from using both SQL\*Plus and Oracle Database Vault Administrator. But do not fear, you can remedy the problem as follows:

1. Temporarily disable Oracle Database Vault.
	See [Appendix B, "Disabling and Enabling Oracle Database Vault,"](dvdisabl.md) for instructions on disabling Oracle Database Vault. After you disable Oracle Database Vault, you can log in to SQL\*Plus.
2. Log in to SQL\*Plus as a user who has been granted the `DV_OWNE` R or `DV_ADMIN` role.
	For example:
	```
	CONNECT lbrown_dvowner
	Enter password: password
	```
3. Enter the following statement to drop the CONNECT command rule.
	```
	EXEC DBMS_MACADM.DELETE_COMMAND_RULE ('CONNECT', '%', '%');
	```
	Even though you have disabled Oracle Database Vault, you still can use its PL/SQL Packages and Database Vault Administrator.
4. Exit SQL\*Plus.
5. Reenable Oracle Database Vault.
	See [Appendix B, "Disabling and Enabling Oracle Database Vault,"](dvdisabl.md) for instructions on enabling Oracle Database Vault.
6. In Oracle Database Vault Administrator, check the rule expression for any errors and then correct them. Recreate the CONNECT command rule, and then test it.

### Step 6: Remove the Components for This Tutorial

1. In Database Vault Administrator, return to the Administrator page.
2. Select Command Rules.
3. In the Command Rules page, select the CONNECT command rule, and then click Remove. Select Yes in the Confirmation page.
4. In the Administrator page, select Rule Sets.
5. In the Rule Sets page, select the Limit SQL\*Plus Access rule set and click Remove. Select Yes in the Confirmation page.
6. In the Administration page, select Factors.
7. In the Factors page, select the Module factor, and then click Remove. Select Yes in the Confirmation page.
8. As the Database Vault Owner, log in to SQL\*Plus and then remove the Prevent Non-admin access to SQL\*Plus rule.
	For example:
	```
	CONNECT lbrown_dvowner
	Enter password: password
	EXEC DBMS_MACADM.DELETE_RULE('Prevent non-admin access to SQL*Plus');
	```
9. If necessary, connect as the Oracle Database Vault Account Manager and then lock and expire the `SCOTT` account.
	For example:
	```
	CONNECT amalcolm_dvacctmgr
	Enter password: password
	ALTER USER SCOTT ACCOUNT LOCK PASSWORD EXPIRE;
	```

## Tutorial: Restricting User Activities Based on Session Data

This section contains:

- About This Tutorial
- Step 1: Create an Administrative User
- Step 2: Add Identities to the Domain Factor
- Step 3: Map the Domain Factor Identities to the Client\_IP Factor
- Step 4: Create a Rule Set to Set the Hours and Select the Factor Identity
- Step 5: Create a Command Rule That Uses the Rule Set
- Step 6: Test the Factor Identity Settings
- Step 7: Remove the Components for This Tutorial

### About This Tutorial

You can use factor identity mapping to set session-based user restrictions for database activities. For example, suppose you wanted to restrict administrative access to a database using the following criteria:

- Ensure that the administrator is accessing the database from the correct IP address.
- Limit the database access to the standard business hours of the administrator.

This type of configuration is useful for restricting different types of administrators: not only local, internal administrators, but offshore and contract administrators as well.

In this tutorial, you modify the Domain factor to include identities for a secure and non-secure network access, which are based on the IP address of the computer the administrator is using. If the administrator tries to perform an action outside the standard working hours or from a different IP address, then Oracle Database Vault prevents him from doing so.

### Step 1: Create an Administrative User

1. In SQL\*Plus, log in as a user who has been granted the `DV_ACCTMGR` role, and then create the user account `mwaldron`.
	For example:
	```
	sqlplus amalcolm_dvacctmgr
	Enter password: password
	CREATE USER mwaldron IDENTIFIED BY password;
	```
	Replace `password` with a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for the minimum requirements for creating passwords.
2. Connect as `SYS` using the `SYSDBA` privilege, and then grant user `mwaldron` DBA privileges.
	```
	CONNECT SYS AS SYSDBA
	Enter password: password
	GRANT CREATE SESSION, DBA TO mwaldron;
	```

### Step 2: Add Identities to the Domain Factor

1. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. In the Administration page, select Factors.
	The Factors page appears.
3. Select the Domain factor and then select Edit.
	The Domain factor is the parent factor.
4. Under Identities, select Create.
5. In the Create Identity page, enter the following information:
	- Value: Enter `HIGHLY SECURE INTERNAL NETWORK`
		- Trust Level: Select Very Trusted
6. Click OK.
7. In the Edit Factor:Domain page, create a second identity called NOT SECURE, and then set its trust level to Untrusted.

### Step 3: Map the Domain Factor Identities to the Client\_IP Factor

1. In Oracle Database Vault Administrator, in the Edit Factor: Domain page, select the HIGHLY SECURE INTERNAL NETWORK identity and then select Edit.
2. Under Map Identity, select Create.
3. In the Create Identity Map page, enter the following information:
	- Contributing Factor: Select Client\_IP to be the child factor.
		- Map Condition: Select Equal, and then in the Low Value box, enter the IP address for the Virtual Machine (for example, `192.0.2.12`). (This is the computer that user `mwaldron` uses. For this tutorial, you can enter the IP address of your own computer. If you are using Microsoft Windows, use the IP address assigned to the Loopback Adapter.)
4. Click OK, and then click OK again to return to the Edit Factor: Domain page.
5. Create the following two identity maps for the NOT SECURE identity:
	|  | Child Factor Name | Operation Value | Operand 1 | Operand 2 |
	| --- | --- | --- | --- | --- |
	|  | `Client_IP` | `Less` | `192.0.2.5` | (Leave blank) |
	|  | `Client_IP` | `Greater` | `192.0.2.20` | (Leave blank) |
	The identity maps in the NOT SECURE identity are in a range of IP addresses outside the IP address that user `mwaldron` uses (192.0.2.12). The IP addresses here must be in any range outside `mwaldron` 's IP address.
	This identity mapping creates the following condition: If the user logs in from the correct IP address, then Oracle Database Vault decides that the connection is secure, through the HIGHLY SECURE INTERNAL NETWORK identity. However, if the user logs in from an IP address that is less than 192.0.2.5 or greater than 192.0.2.20, then the connection is deemed not secure, through the NO SECURE identity.
6. Click OK to return to the Edit Factor: Domain page, then click OK again to return to the Factors page.
7. Test the factor identities.
	First, in SQL\*Plus, connect as user `mwaldron` but do not specify a database instance.
	```
	CONNECT mwaldron
	Enter password: password
	SELECT DVF.F$CLIENT_IP FROM DUAL;
	```
	The following output should appear:
	```
	F$CLIENT_IP
	-------------------------------------
	```
	Next:
	```
	SELECT DVF.F$DOMAIN FROM DUAL;
	```
	The following output should appear:
	```
	F$DOMAIN
	-------------------------------------
	NOT SECURE
	```
	Because user `mwaldron` is not connecting directly to the database instance, Oracle Database Vault does not recognize the IP address from which he is connecting. In this case, Oracle Database uses the IPC protocol to perform the connection, which sets the IP value to null. Therefore, the identity for this connection is set to NOT SECURE.
	Now connect to SQL\*Plus by specifying the database instance (for example, `orcl`), and then check the factor identities again:
	```
	CONNECT mwaldron@orcl
	Enter password: password
	SELECT DVF.F$CLIENT_IP FROM DUAL;
	```
	The following output should appear:
	```
	F$CLIENT_IP
	-------------------------------------
	192.0.2.12
	```
	Next:
	```
	SELECT DVF.F$DOMAIN FROM DUAL;
	```
	The following output should appear:
	```
	F$DOMAIN
	-------------------------------------
	HIGHLY SECURE INTERNAL NETWORK
	```
	Now that user `mwaldron` is connecting to the `orcl` database instance, his IP address is recognized. This is because the database uses the TCP protocol, so now the host IP value can be populated appropriately. Because the IP address is within the correct range, the factor identity is set to HIGHLY SECURE INTERNAL NETWORK.

### Step 4: Create a Rule Set to Set the Hours and Select the Factor Identity

1. In Oracle Database Vault, return to the Administration page.
2. Select Rule Sets.
3. In the Rule Sets page, select Create.
4. In the Create Rule Set page, enter the following settings:
	- Name: Enter `Internal DBA Standard Working Hours`.
		- Status: Select Enabled.
		- Evaluation Options: Select All True.
	Leave the remaining settings at their defaults.
5. Click OK.
6. In the Rule Sets page, select the Internal DBA Standard Working Hours rule set, and then select Edit.
7. In the Edit Rule Set: Internal DBA Standard Working Hours page, under Rules Associated To The Rule Set, select Create.
8. In the Create Rule page, create the following rules:
	- Name: `Internal DBA`
		Rule Expression: `DVF.F$SESSION_USER='MWALDRON'`
		(When you create an expression with a user name, enter the user name in upper case letters, because that is how the database stores user names.)
		- Name: `Internal Network Only`
		Rule Expression: `DVF.F$DOMAIN='HIGHLY SECURE INTERNAL NETWORK'`
		- Name: `Week Day`
		Rule Expression: `TO_CHAR(SYSDATE, 'D') BETWEEN '2' AND '6'`
		- Name: `Week Working Day Hours`
		Rule Expression: `TO_CHAR(SYSDATE, 'HH24') BETWEEN '08' AND '19'`
9. Click OK to return to the Rule Sets page.

### Step 5: Create a Command Rule That Uses the Rule Set

1. In Oracle Database Vault Administrator, return to the Administration page.
2. Select Command Rules, and in the Command Rules page, select Create.
3. In the Create Command Rule page, enter the following settings:
	- Command: Select CREATE TABLE from the list.
		- Rule Set: Select Internal DBA Standard Working Hours from the list.
	Leave the remaining settings at their defaults.
4. Click OK.

### Step 6: Test the Factor Identity Settings

Test the settings by resetting the system clock, logging in as the `mwaldron` administrative user, and then trying to create a table.

1. Set the system time to 9 p.m.
	UNIX: Log in as root and use the date command to set the time. For example, assuming the date today is December 14 2011, you would enter the following:
	```
	su root
	Password: password
	date --set="14 DEC 2011 21:00:00"
	```
	Windows: Double-click the clock icon, which is typically at the lower right corner of the screen. In the Date and Time Properties window, set the time to 9 p.m., and then click OK.
2. In SQL\*Plus, connect as user `mwaldron` and try to create a table. In the following, replace `orcl` with the name of your database instance.
	```
	CONNECT mwaldron@orcl
	Enter password: password
	CREATE TABLE TEST (num number);
	```
	The following output should appear:
	```
	ORA-47400: Command Rule violation for create table on MWALDRON.TEST
	```
	Because user `mwaldron` is create a table outside working hours, Database Vault prevents him.
3. Reset the system time back to the local time.
4. In SQL\*Plus, as user `mwaldron`, try to create the table again.
	```
	CREATE TABLE TEST (num number);
	Table created.
	DROP TABLE TEST;
	Table dropped.
	```
	Now that user `mwaldron` is working during his local hours and from the IP address associated with the HIGHLY SECURE INTERNAL NETWORK identity, he can create tables.
5. Reconnect as user `mwaldron` but without adding the database instance name to the connection command, and then try to create the table again.
	```
	CONNECT mwaldron
	Enter password: password
	CREATE TABLE TEST (num number);
	```
	The following output should appear:
	```
	ORA-47400: Command Rule violation for create table on MWALDRON.TEST
	```
	Even though user `mwaldron` is trying to create a table during the correct time, he cannot because is not directly logged in to the `orcl` database instance. Oracle Database Vault deems him to be using the NOT SECURE identity, and then denies him access.

### Step 7: Remove the Components for This Tutorial

1. Log in to SQL\*Plus as the `DV_ACCTMGR` user and drop user `mwaldron`.
	```
	sqlplus amalcolm_dvacctmgr
	Enter password: password
	DROP USER mwaldron CASCADE;
	```
2. Remove the CREATE TABLE command rule.
	Return the Administration page and select Command Rules. Select the CREATE TABLE command rule and then select Remove. In the Confirmation page, select Yes.
3. Remove the Internal DBA Standard Working Hours rule set.
	In Oracle Database Vault Administrator, select Rule Sets in the Administration page. In the Rule Sets page, select the Internal DBA Standard Working Hours rule set, and then select Remove. In the Confirmation page, select Yes.
4. In SQL\*Plus, delete the rules associated with the Internal DBA Standard Working Hours rule set.
	```
	CONNECT lbrown_dvowner
	Enter password: password
	EXEC DBMS_MACADM.DELETE_RULE('Internal DBA');
	EXEC DBMS_MACADM.DELETE_RULE('Internal Network Only');
	EXEC DBMS_MACADM.DELETE_RULE('Week Day');
	EXEC DBMS_MACADM.DELETE_RULE('Week Day Working Hours'); 
	COMMIT;
	```
5. Remove the HIGHLY SECURE INTERNAL NETWORK and NOT SECURE factor identities from the Domain factor.
	Return to the Administration page and select Factors. Select the Domain factor, select Edit, and under Identities, remove the HIGHLY SECURE INTERNAL NETWORK and NOT SECURE factor identities. In the Confirmation page, select Yes.

## Guidelines for Designing Factors

Follow these guidelines for designing factors:

- You can use the Oracle utility packages such as `UTL_TCP`, `UTL_HTTP`, `DBMS_LDAP`, and `DBMS_PIPE` to integrate security or other contextual information about the session from external systems.
- Do not specify a retrieval method if the factor identification is set to Identified By Factors. Retrieval methods are only needed if you set the factor to By Method or By Constant.
- Consider using a validation method if a factor has an assignment rule set. Doing so helps to verify that invalid identities are not submitted.
- Use the client-supplied factors such as Program, OS User, and others with caution, because the values that are supplied can only be trusted when the client software is trusted and the communications channel from the client software is known to be secure.
- Only specify an evaluation option of By Access if the value returned by the retrieval method could change from one invocation to the next in the same session (for example, time-based factors).
- Optimize the internal logic of a function used for the factor retrieval method using traditional SQL and PL/SQL optimization techniques. For more information about performance and optimization, see [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm).
- If the discrete values returned by the retrieval method are known, be sure to define identities for each value so that you can assign trust levels for them. Trust levels add value to factors as you also can use the trust level in application logic based on factors.
- A security policy based on more factors is generally considered stronger than one based on fewer factors. You can create a new factor that is identified by other factors to store combinations of factors into logical grouping using identity maps. This also makes it easier to label the parent factor when you integrate the factors with the Oracle Label Security labels. (See ["Integrating Oracle Database Vault with Oracle Label Security"](dv_ols.md) for more information.)
- It is generally easier to configure and debug a factor that is labeled By Self than one labeled By Factors when integrating the Oracle Label Security.
- You can design a database client application to pass one or more security, end-user, or environmental attributes so that they are available to an associated database session. To do this, create a single factor for each attribute and then use an assignment rule set to control when these attributes can be assigned (for example only when using a specific Web application on specified named application server computers). Oracle Database Vault factors used in this fashion are very much like the Oracle procedure `DBMS_SESSION.SET_IDENTIFIER` but also include a capability to control when they can be set. For more information about the `DBMS_SESSION` package, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm).

## How Factors Affect Performance

Each factor has elements that are processed, such as its validation method, trust level, and so on. For factors that are evaluated by the session, such as Database\_Hostname and `Proxy_User`, Oracle Database Vault performs this processing during session initialization, and then caches the results for subsequent requests for that value.

The 17 default factors listed in "Default Factors" are cached because they are likely candidates for a typical security policy. However, if you only use five factors (for example, in rule sets or other components), then the other factors consume resources that could otherwise be used elsewhere. In this case, you should remove the unnecessary factors by deleting them. (Oracle Database Vault does not use any of these factors internally, so you can remove them if you do not need them.)

If you have a large number of users or if your application server frequently must create and destroy connections, the resources used can affect system performance. You can delete the unnecessary factors.

You can check system performance by running tools such as Oracle Enterprise Manager (including Oracle Enterprise Manager Database Control, which is installed by default with Oracle Database), `Statspack`, and `TKPROF`. For more information about Oracle Enterprise Manager, see the Oracle Enterprise Manager documentation set. For information about Database Control, refer to its online Help. [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) describes the `Statspack` and `TKPROF` utilities.

## Related Reports and Data Dictionary Views

Table 7-1 lists Oracle Database Vault reports that are useful for analyzing factors and their identities. See [Chapter 18, "Oracle Database Vault Reports,"](reports.md) for information about how to run these reports.

Table 7-1 Reports Related to Factors and Their Identities

| Report | Description |
| --- | --- |
| ["Factor Audit Report"](reports.md) | Audits factors (for example, to find factors that failed to be evaluated) |
| ["Factor Configuration Issues Report"](reports.md) | Lists configuration issues, such as disabled or incomplete rule sets, or to audit issues that may affect the factor |
| ["Factor Without Identities Report"](reports.md) | Lists factors that have had no identities assigned yet |
| ["Identity Configuration Issues Report"](reports.md) | Lists factors that have invalid label identities or no map for the identity |
| ["Rule Set Configuration Issues Report"](reports.md) | Lists rule sets that have no rules defined or enabled, which may affect the factors that use them |

Table 7-2 lists data dictionary views that provide information about existing factors and factor identities.

Table 7-2 Data Dictionary Views Used for Factors and Factor Identities

| Data Dictionary View | Description |
| --- | --- |
| ["DVSYS.DBA\_DV\_FACTOR View"](views.md) | Lists the existing factors in the current database instance |
| ["DVSYS.DBA\_DV\_FACTOR\_LINK View"](views.md) | Shows the relationships of each factor whose identity is determined by the association of child factors |
| ["DVSYS.DBA\_DV\_FACTOR\_TYPE View"](views.md) | Lists the names and descriptions of factor types used in the system |
| ["DVSYS.DBA\_DV\_IDENTITY View"](views.md) | Lists the identities for each factor |
| ["DVSYS.DBA\_DV\_IDENTITY\_MAP View"](views.md) | Lists the mappings for each factor identity |

[^1]: In the Create Identity page, under Label Identity, select the OLS label from the Available OLS Labels list.

The list shows data labels from the Oracle Label Security installation for your site. For more information, refer to [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/toc.htm).

Note:

You can select multiple labels by holding down the Ctrl key as you click each label that is to be selected.

[^2]: Click Move to move the OLS label to the Selected OLS Labels list.

[^undefined]: Repeat Step 1 and Step 2 to select more OLS labels.

You can select only one label for each OLS policy.

[^undefined]: Click OK to finish labeling the identity.

[^3]: In the factor evaluation stage, the factor initialization process executes the retrieval method for all factors that are identified by methods or constants, to resolve the factor identity for the session.

The factor error options setting has no effect on the factor initialization process.

[^undefined]: If a factor has a validation method defined, Oracle Database Vault validates the identity (value) of the factor by executing this validation method. If the validation method fails or returns false, the identity of the factor is undefined (`NULL`).

[^undefined]: If a factor has any identities defined for it, Oracle Database Vault resolves the trust level of the factor based on the identities defined. If an identity of the factor is defined in this list of defined identities, then Oracle Database Vault assigns the trust level as configured; otherwise it sets it to -1. If there are no identities defined for the factor, the trust level is undefined (`NULL`).

[^4]: Depending on the outcome of this factor evaluation, factor validation, and trust level resolution, Database Vault audits the details of the evaluation as dictated by the factor audit configuration.

[^5]: When the evaluation of all factors that are identified by method or constant completes, Oracle Database Vault resolves the factors that are identified by other factors by using the identity maps that are defined for the factor configured identities.

The evaluation order of the factor-configured identities is by ASCII sort on the identity values: Oracle Database Vault uses the first alphabetically sorted identity mapping that it evaluates. For example, suppose factor TEST has identities X and Y. Furthermore, identities X and Y have identity maps that are dependent on identities for factors A, B, and C. The following mapping occurs:

- X is mapped when A=1 and B=1
- Y is mapped when A=1, B=1, and C=2

In this case, the first one evaluated is X. Y is not evaluated, but what if its C mapping meets the criteria that is needed for the TEST factor's success? You would need to reverse the mapping, that is, map Y before X so that A, B, and C can be evaluated first. To reverse the mapping, rename Y to V (or some alphabetic value that sorts before X) so that it can be correctly resolved.

This algorithm works if the ASCII sort ordering is correct and the identities map the same number factors at some level.

[^undefined]: When the factor initialization completes, the Oracle Database Vault integration with Oracle Label Security occurs.

[^6]: Enter the following settings:

- Name: Enter `Prevent non-admin access to SQL*Plus`.
- Rule Expression: Enter the following rule expression:
	```
	DVF.F$MODULE = 'SQL*PLUS.EXE' AND DVF.F$SESSION_USER IN ('LBROWN_DVOWNER', 'AMALCOLM_DVACCTMGR', 'SYS', 'SYSTEM')
	```
	Replace `LBROWN_DVOWNER` and `AMALCOLM_DVACCTMGR` with the user account names that you use for the Database Vault Owner and Database Vault Account Manager accounts. You must enter the user account names in upper case letters, because that is how the database stores user account names.
	This expression tells Oracle Database Vault only to allow these four users to use SQL\*Plus. Another way to write the expression is to tell Database Vault to simply exclude certain users from using SQL\*Plus. That way, everyone else has access to SQL\*Plus. For example, to exclude users `JSMITH` and `TSMITH` from using SQL\*Plus, you would create this expression:
	```
	DVF.F$MODULE != 'SQL*PLUS.EXE' AND DVF.F$SESSION_USER NOT IN ('JSMITH', 'TSMITH')
	```
	However, for this tutorial, use the first expression, in which only the four administrative users are allowed to use SQL\*Plus.

[^undefined]: Ensure that you have entered this rule expression exactly as shown in Step 8. If you enter it incorrectly, you cannot log in to SQL\*Plus.

[^undefined]: Click OK.