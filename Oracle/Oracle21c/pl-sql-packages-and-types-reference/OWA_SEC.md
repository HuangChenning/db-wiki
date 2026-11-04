---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/OWA_SEC.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 232 OWA\_SEC

The `OWA_SEC` package provides an interface for custom authentication.

See Also:

For more information about implementation of this package:

- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](https://docs.oracle.com/cd/E23943_01/portal.1111/e12041/toc.htm)

The chapter contains the following topics:

- Operational Notes
- Summary of OWA\_SEC Subprograms

### 232.1 OWA\_SEC Operational Notes

Parameters that have default values are optional.

### 232.2 Summary of OWA\_SEC Subprograms

This table lists the OWA\_SEC subprograms in alphabetical order and briefly describes them.

Table 232-1 OWA\_SEC Package Subprograms

| Subprogram | Description |
| --- | --- |
| GET\_CLIENT\_HOSTNAME Function | Returns the client's hostname |
| GET\_CLIENT\_IP Function | Returns the client's IP address |
| GET\_PASSWORD Function | Returns the password that the user entered |
| GET\_USER\_ID Function | Returns the username that the user entered |
| SET\_AUTHORIZATION Procedure | Enables the PL/SQL application to use custom authentication |
| SET\_PROTECTION\_REALM Procedure | Defines the realm that the page is in |

#### 232.2.1 GET\_CLIENT\_HOSTNAME Function

This function returns the hostname of the client.

Syntax

```
OWA_SEC.GET_CLIENT_HOSTNAME
 RETURN VARCHAR2;
```

Return Values

The hostname.

#### 232.2.2 GET\_CLIENT\_IP Function

This function returns the IP address of the client.

Syntax

```
OWA_SEC.GET_CLIENT_IP 
  RETURN OWA_UTIL.IP_ADDRESS;
```

Return Values

The IP address. The `owa_util.ip_address datatype` is a PL/SQL table where the first four elements contain the four numbers of the IP address. For example, if the IP address is `123.45.67.89` and the variable `ipaddr` is of the owa\_util.ip\_address datatype, the variable would contain the following values:

```
ipaddr(1) = 123
ipaddr(2) = 45
ipaddr(3) = 67
ipaddr(4) = 89
```

#### 232.2.3 GET\_PASSWORD Function

This function returns the password that the user used to log in.

Syntax

```
OWA_SEC.GET_PASSWORD 
  RETURN VARCHAR2;
```

Return Values

The password.

Usage Notes

For security reasons, this function returns a true value only when custom authentication is used. If you call this function when you are not using custom authentication, the function returns an undefined value. Thus, the database passwords are not exposed.

#### 232.2.4 GET\_USER\_ID Function

This function returns the username that the user used to log in.

Syntax

```
OWA_SEC.GET_USER_ID 
  RETURN VARCHAR2;
```

Return Values

The username.

#### 232.2.5 SET\_AUTHORIZATION Procedure

This procedure, called in the initialization portion of the OWA\_CUSTOM package, sets the authorization scheme for the PL/SQL Gateway.

This implements your `authorize` function, which authorizes the user before his requested procedure is run. The placement of the `authorize` function depends on the scheme you select.

Syntax

```
OWA_SEC.SET_AUTHORIZATION(
    scheme         IN       INTEGER);
```

Parameters

Table 232-2 SET\_AUTHORIZATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `scheme` | The authorization scheme. It is one of the following schemes for `SET_AUTHORIZATION`:  - `OWA_SEC.NO_CHECK` - Specifies that the PL/SQL application is not to do any custom authentication. This is the default. - `OWA_SEC.GLOBAL` - Defines an authorize function that is called for all users and all procedures. This is the `OWA_CUSTOM`.[AUTHORIZE Function](OWA_CUSTOM.md) in the " `sys` " schema. - `OWA_SEC.PER_PACKAGE ` - Define an `authorize` function that is called when procedures in a package or anonymous procedures are called. If the procedures are in a package, the package.`AUTHORIZE` function in the user's schema is called to authorize the user. If the procedures are not in a package, then the anonymous `authorize` function in the user's schema is called. - `OWA_SEC.CUSTOM` - Implements different authorize functions for each user. The function `OWA_CUSTOM`.[AUTHORIZE Function](OWA_CUSTOM.md) in the user's schema is called to authorize the user. If the user's schema does not contain an `OWA_CUSTOM`.AUTHORIZE Function, the PL/SQL Gateway looks for it in the "sys" schema. 	The custom `authorize` function has the following signature: 	``` 	FUNCTION AUTHORIZE  	  RETURN BOOLEAN; 	```  If the function returns `TRUE`, authentication succeeded. If it returns `FALSE`, authentication failed. If the `authorize` function is not defined, the Gateway returns an error and fails. |

#### 232.2.6 SET\_PROTECTION\_REALM Procedure

This procedure sets the realm of the page that is returned to the user. The user enters a username and login that already exist in the realm.

Syntax

```
OWA_SEC.SET_PROTECTION_REALM(
   realm      IN      VARCHAR2);
```

Parameters

Table 232-3 SET\_PROTECTION\_REALM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `realm` | The realm where the page belongs. This string is displayed to the user. |