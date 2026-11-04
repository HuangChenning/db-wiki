---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XDB_CONFIG.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 203 DBMS\_XDB\_CONFIG

The `DBMS_XDB_CONFIG` package provides an interface for configuring Oracle XML DB and its repository.

This chapter contains the following topics:

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB5449)

### 203.1 DBMS\_XDB\_CONFIG Overview

PL/SQL package `DBMS_XDB_CONFIG` is the Oracle XML DB resource application program interface (API) for PL/SQL for DBAs to configure their system. This API provides functions and procedures to access and manage Oracle XML DB Repository resources using PL/SQL. It includes methods for managing resource security and Oracle XML DB configuration.

Oracle XML DB Repository is modeled on XML, and provides a database file system for any data. The repository maps path names (or URLs) onto database objects of XMLType and provides management facilities for these objects.

PL/SQL package DBMS\_XDB\_CONFIG is an API that you can use to manage all of the following:

- Oracle XML DB resources
- Oracle XML DB security based on access control lists (ACLs). An ACL is a list of access control entries (ACEs) that determines which principals (users and roles) have access to which resources.
- Oracle XML DB configuration

### 203.2 DBMS\_XDB\_CONFIG Security Model

Owned by `XDB`, the `DBMS_XDB_CONFIG` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### 203.3 DBMS\_XDB\_CONFIG Constants

The `DBMS_XDB_CONFIG` package defines several enumerated constants that should be used for specifying parameter values.

These constants are shown in the following table.

Table 203-1 DBMS\_XDB\_CONFIG Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `XDB_ENDPOINT_HTTP` | `NUMBER` | 1 | Defining listener for first HTTP port |
| `XDB_ENDPOINT_HTTP2` | `NUMBER` | 2 | Defining listener for second HTTP port |
| `XDB_ENDPOINT_RHTTP` | `NUMBER` | 3 | Defining listener for a remote HTTP port |
| `XDB_ENDPOINT_RHTTPS` | `NUMBER` | 4 | Defining listener for a remote HTTPS port |
| `XDB_PROTOCOL_TCP` | `NUMBER` | 1 | Defining listener for HTTP protocol |
| `XDB_PROTOCOL_TCPS` | `NUMBER` | 2 | Defining listener for HTTPS protocol |

### 203.4 Summary of DBMS\_XDB\_CONFIG Subprograms

The `DBMS_XDB_CONFIG` package uses subprograms for configuring Oracle XML DB and its repository.

These subprograms are listed in the following table.

Table 203-2 DBMS\_XDB\_CONFIG Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADDHTTPEXPIREMAPPING Procedure | Adds to `XDB$CONFIG` a mapping of the URL pattern to an expiration date. This will control the Expire headers for URLs matching the pattern. |
| ADDMIMEMAPPING Procedure | Adds a mime mapping to XDB configuration |
| ADDSCHEMALOCMAPPING Procedure | Adds a schema location mapping to the XDB configuration |
| ADDSERVLET Procedure | Adds a servlet to XDB configuration |
| ADDSERVLETMAPPING Procedure | Adds a servlet mapping to XDB configuration |
| ADDSERVLETSECROLE Procedure | Adds a security role `REF` to a specified servlet in XDB configuration |
| ADDXMLEXTENSION Procedure | Adds adds the following XML extension to the XDB configuration under `<xml-extensions>`: \<extension>extension\</extension> |
| CFG\_GET Function | Retrieves the session's configuration information as an `XMLType` instance |
| CFG\_REFRESH Procedure | Refreshes the session's configuration information to the latest configuration |
| CFG\_UPDATE Procedure | Updates the configuration information and commits the change. |
| DELETEHTTPEXPIREMAPPING Procedure | Deletes from `XDB$CONFIG` all mappings of the URL pattern to an expiration date |
| DELETEMIMEMAPPING Procedure | Deletes the mime mapping for a specified extension from the XDB configuration |
| DELETESCHEMALOCMAPPING Procedure | Deletes the schema location mapping for a specified schema URL from the XDB configuration |
| DELETESERVLET Procedure | Deletes a servlet from the XDB configuration |
| DELETESERVLETMAPPING Procedure | Deletes the servlet mapping for a specified servlet name from the XDB configuration |
| DELETESERVLETSECROLE Procedure | Deletes the specified role from a servlet in the XDB configuration |
| DELETEXMLEXTENSION Procedure | Deletes the specified XML extension from the XDB configuration |
| ENABLEDIGESTAUTHENTICATION Procedure | Enables enables digest authentication |
| GETFTPPORT Function | Gets the value of the current FTP port |
| GETHTTPPORT Function | Gets the value of the current HTTP port |
| GETHTTPCONFIGREALM Function | Gets the realm name |
| GETHTTPSPORT Function | Gets the value of the current HTTPS port |
| GETLISTENERENDPOINT Procedure | Gets the parameters of a listener end point corresponding to the XML DB HTTP server |
| GETREMOTEHTTPPORT Function | Gets the value of a remote HTTP port |
| GETREMOTEHTTPSPORT Function | Gets the value of a remote HTTPS port |
| ISGLOBALPORTENABLED Function | Returns the value of the `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` procedure setting |
| SETGLOBALPORTENABLED Procedure | Enables the use of a global port for Oracle Enterprise Manager Database Express (EM Express) clients |
| SETFTPPORT Procedure | Sets the FTP port to a new value |
| SETHTTPPORT Procedure | Sets the HTTP port to a new value |
| SETHTTPCONFIGREALM Procedure | Sets the realm to a new value |
| SETHTTPSPORT Procedure | Sets the HTTPS port to a new value |
| SETLISTENERENDPOINT Procedure | Sets the parameters of a listener end point corresponding to the XML DB HTTP server |
| SETLISTENERLOCALACCESS Procedure | Restricts all listener end points of the XML DB HTTP server to listen either only on the localhost interface (when `l_access` is set to `TRUE`) or to listen on both localhost and non-localhost interfaces (when `l_access` is set to `FALSE`) |
| SETREMOTEHTTPPORT Procedure | Sets the remote HTTP port to a new value |
| SETREMOTEHTTPSPORT Procedure | Sets the remote HTTPS port to a new value |
| USEDPORT Procedure | Obtains the port numbers used by other pluggable databases in the same consolidation database |

#### 203.4.1 ADDHTTPEXPIREMAPPING Procedure

This procedure adds to `XDB$CONFIG` a mapping of the URL pattern to an expiration date. This will control the Expire headers for URLs matching the pattern.

Syntax

```
DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING (
     pattern    IN    VARCHAR2,
     expire     IN    VARCHAR2);
```

Parameters

Table 203-3 ADDHTTPEXPIREMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pattern` | URL pattern (only \* accepted as wildcards) |
| `expire` | Expiration directive, follows the `ExpireDefault` in Apache's `mod_expires`:  ``` base [plus] (num type)* -- base: now \| modification -- type: year\|years\|month\|months\|week\|weeks\|day\|days\| minute\|minutess\|second\|seconds ``` |

Examples

```
DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING ('/public/test1/*', 'now plus 4 weeks');
DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING (
             '/public/test2/*', 'modification plus 1 day 30 seconds');
```

#### 203.4.2 ADDMIMEMAPPING Procedure

This procedure adds the following mime mapping to XDB configuration:

```
<mime-mapping>
<extension>extension</extension>
<mime-type>mimetype</mime-type>
</mime-mapping>
```

Syntax

```
DBMS_XDB_CONFIG.ADDMIMEMAPPING(
     extension    IN   VARCHAR2,
     mimetype     IN   VARCHAR2);
```

Parameters

Table 203-4 ADDMIMEMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | Extension for which a mime type is being added |
| `mimetype` | Mime type |

#### 203.4.3 ADDSCHEMALOCMAPPING Procedure

This procedure adds the following schema location mapping to the XDB configuration:

```
<schemaLocation-mapping>
     <namespace>namespace</namespace>
     <element>element</element>
      <schemaURL>schemaURL</schemaURL>
</schemaLocation-mapping>
```

Syntax

```
DBMS_XDB_CONFIG.ADDSCHEMALOCMAPPING(
     namespace    IN   VARCHAR2,
     element      IN   VARCHAR2,
     schemaURL    IN   VARCHAR2);
```

Parameters

Table 203-5 ADDSCHEMALOCMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `namespace` | Namespace |
| `element` | Element |
| `schemaURL` | Schema URL |

#### 203.4.4 ADDSERVLET Procedure

This procedure adds a servlet to XDB configuration.

IT adds the following servlet:

```
<servlet>
     <servlet-name>name</servlet-name>     <servlet-language>language</servlet-language>
     <display-name>dispname</display-name>
     <description>descript</description>
     <servlet-class>class</servlet-class>
     <servlet-schema>schema</servlet-schema>
</servlet>
```

Syntax

```
DBMS_XDB_CONFIG.ADDSERVLET(
    name        IN   VARCHAR2,
    language    IN   VARCHAR2,
    dispname    IN   VARCHAR2,
    icon        IN   VARCHAR2 := NULL,
    descript    IN   VARCHAR2 := NULL,
    class       IN   VARCHAR2 := NULL,
    jspfile     IN   VARCHAR2 := NULL,
    plsql       IN   VARCHAR2 := NULL,
    schema      IN   VARCHAR2 := NULL);
```

Parameters

Table 203-6 ADDSERVLET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |
| `language` | Must be one of "C", "Java", "PL/SQL" |
| `dispname` | Display name |
| `icon` | Icon |
| `descript` | Description |
| `class` | The `class` / `jspfile` / `plsql` function corresponding to this servlet. The first non- `NULL` argument amongst these three is chosen, and the others are treated as `NULL`. |
| `jspfile` | This parameter is not supported. Always provide `NULL` value for this parameter. System throws an error if the value is not `NULL`. |
| `plsql` | The `class` / `jspfile` / `plsql` function corresponding to this servlet. The first non- `NULL` argument amongst these three is chosen, and the others are treated as `NULL`. |
| `schema` | Schema is used to specify `servlet-schema` xml element name in `xdbconfig.xml`. It indicates the Oracle schema in which the Java class is loaded.  If you do not specify any value, then the schema is searched using the default resolver specification. |

#### 203.4.5 ADDSERVLETMAPPING Procedure

This procedure adds a servlet mapping to XDB configuration.

It adds the following servlet mapping:

```
<servlet-mapping>
     <servlet-pattern>pattern</servlet-pattern>
     <servlet-name>name</servlet-name>
</servlet-mapping>
```

Syntax

```
DBMS_XDB_CONFIG.ADDSERVLETMAPPING(
     pattern   IN   VARCHAR2,     name      IN   VARCHAR2);
```

Parameters

Table 203-7 ADDSERVLETMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pattern` | Sservlet pattern |
| `name` | Servlet name |

#### 203.4.6 ADDSERVLETSECROLE Procedure

This procedure adds the security role `REF` to a specified servlet in XDB configuration.

It adds the following security role as shown in the following:

```
<security-role-ref>
     <role-name>rolename</role-name>
     <role-link>rolelink</role-link>
     <description>descript</description>
</security-role-ref>
```

Syntax

```
DBMS_XDB_CONFIG.ADDSERVLETSECROLE(
     servname    IN   VARCHAR2,     rolename    IN   VARCHAR2,     rolelink    IN   VARCHAR2,     descript    IN   VARCHAR2 := NULL);
```

Parameters

Table 203-8 ADDSERVLETSECROLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `servname` | Sservlet name |
| `rolename` | Role name |
| `rolelink` | Role link |
| `descript` | Description |

#### 203.4.7 ADDXMLEXTENSION Procedure

This procedure adds an XML extension to the XDB configuration under `<xml-extensions>`.

It adds the following XML extension to the XDB configuration, under `<xml-extensions>`:

```
<extension>extension</extension>
```

Syntax

```
DBMS_XDB_CONFIG.ADDXMLEXTENSION(
     extension    IN   VARCHAR2);
```

Parameters

Table 203-9 ADDXMLEXTENSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | XML extension to be added |

#### 203.4.8 CFG\_GET Function

This function retrieves the session's configuration information as an `XMLType` instance.

Syntax

```
DBMS_XDB_CONFIG.CFG_GET 
 RETURN SYS.XMLType;
```

#### 203.4.9 CFG\_REFRESH Procedure

This procedure refreshes the session's configuration information to the latest configuration.

Syntax

```
DBMS_XDB_CONFIG.CFG_REFRESH;
```

#### 203.4.10 CFG\_UPDATE Procedure

This procedure updates the configuration information and commits the change.

Syntax

```
DBMS_XDB_CONFIG.CFG_UPDATE(
   xdbconfig   IN  SYS.XMLTYPE);
```

Parameters

Table 203-10 CFG\_UPDATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xdbconfig` | The new configuration data |

#### 203.4.11 DELETEHTTPEXPIREMAPPING Procedure

This procedure deletes from `XDB$CONFIG` all mappings of the URL pattern to an expiration date.

Syntax

```
DBMS_XDB_REPOS.DELETEHTTPEXPIREMAPPING(
     pattern  IN   VARCHAR2);
```

Parameters

Table 203-11 DELETEHTTPEXPIREMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pattern` | URL pattern (only \* accepted as wildcards) |

#### 203.4.12 DELETEMIMEMAPPING Procedure

This procedure deletes the mime mapping for a specified extension from the XDB configuration.

Syntax

```
DBMS_XDB_CONFIG.DELETEMIMEMAPPING(
     extension    IN   VARCHAR2);
```

Parameters

Table 203-12 DELETEMIMEMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | Extension for which a mime type is to be deleted |

#### 203.4.13 DELETESCHEMALOCMAPPING Procedure

This procedure deletes the schema location mapping for a specified schema URL from the XDB configuration.

Syntax

```
DBMS_XDB_CONFIG.DELETESCHEMALOCMAPPING(
     schemaURL    IN   VARCHAR2);
```

Parameters

Table 203-13 DELETESCHEMALOCMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schemaURL` | Schema URL |

#### 203.4.14 DELETESERVLET Procedure

This procedure deletes a servlet from the XDB configuration.

Syntax

```
DBMS_XDB_CONFIG.DELETESERVLET(
     name        IN   VARCHAR2);
```

Parameters

Table 203-14 DELETESERVLET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |

#### 203.4.15 DELETESERVLETMAPPING Procedure

This procedure deletes the servlet mapping for a specified servlet name from the XDB configuration.

Syntax

```
DBMS_XDB_CONFIG.DELETESERVLETMAPPING(
     name      IN   VARCHAR2);
```

Parameters

Table 203-15 DELETESERVLETMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |

#### 203.4.16 DELETESERVLETSECROLE Procedure

This procedure deletes the specified role from a servlet in the XDB configuration.

Syntax

```
DBMS_XDB_CONFIG.DELETESERVLETSECROLE(
     servname    IN   VARCHAR2,     rolename    IN   VARCHAR2);
```

Parameters

Table 203-16 DELETESERVLETSECROLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `servname` | Servlet name |
| `rolename` | Name of the role to be deleted |

#### 203.4.17 DELETEXMLEXTENSION Procedure

This procedure deletes the specified XML extension from the XDB configuration.

Syntax

```
DBMS_XDB_CONFIG.DELETEXMLEXTENSION(
     extension    IN   VARCHAR2);
```

Parameters

Table 203-17 DELETEXMLEXTENSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | XML extension to be deleted |

#### 203.4.18 ENABLEDIGESTAUTHENTICATION Procedure

This procedure enables digest authentication. It will list digest as the first authentication mechanism to be used by the XML DB HTTP server.

Syntax

```
DBMS_XDB_CONFIG.ENABLEDIGESTAUTHENTICATION;
```

#### 203.4.19 GETFTPPORT Function

This procedure gets the value of the current FTP port.

Syntax

```
DBMS_XDB_CONFIG.GETFTPPORT
 RETURN NUMBER;
```

#### 203.4.20 GETHTTPCONFIGREALM Function

This function gets the realm name. Definition of a realm is referenced in IETF's RFC2617.

Syntax

```
DBMS_XDB_CONFIG.GETHTTPCONFIGREALM
 RETURN VARCHAR2;
```

#### 203.4.21 GETHTTPPORT Function

This function gets the value of the current HTTP port.

Syntax

```
DBMS_XDB_CONFIG.GETHTTPPORT
 RETURN NUMBER;
```

#### 203.4.22 GETHTTPSPORT Function

This procedure gets the value of the current HTTPS port.

Syntax

```
DBMS_XDB_CONFIG.GETHTTPSPORT
 RETURN NUMBER;
```

Usage Notes

Returns `NULL` if no port has been configured

#### 203.4.23 GETLISTENERENDPOINT Procedure

This procedure retrieves the parameters of a listener end point corresponding to the XML DB HTTP server. The parameters of both HTTP and HTTP2 end points can be retrieved by invoking this procedure.

Syntax

```
DBMS_XDB_CONFIG.GETLISTENERENDPOINT (
   endpoint  IN   NUMBER, 
   host      OUT  VARCHAR2,    port      OUT  NUMBER, 
   protocol  OUT  NUMBER);
```

Parameters

Table 203-18 GETLISTENERENDPOINT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `endpoint` | End point to be retrieved. Its value can be `XDB_ENDPOINT_HTTP` or `XDB_ENDPOINT_HTTP2`. |
| `host` | Interface on which the listener end point listens |
| `port` | Port on which the listener end point listens |
| `protocol` | Transport protocol accepted by the listener end point |

#### 203.4.24 GETREMOTEHTTPPORT Function

This function gets the value of a remote HTTP port.

Syntax

```
DBMS_XDB_CONFIG.GETREMOTEHTTPPORT
 RETURN NUMBER;
```

#### 203.4.25 GETREMOTEHTTPSPORT Function

This function gets the value of a remote HTTPS port.

Syntax

```
DBMS_XDB_CONFIG.GETREMOTEHTTPSPORT
 RETURN NUMBER;
```

#### 203.4.26 ISGLOBALPORTENABLED Function

This procedure returns the value of the `GlobalPortEnabled` setting.

Syntax

```
DBMS_XDB_CONFIG.ISGLOBALPORTENABLED RETURN BOOLEAN;
```

Usage Notes

- This procedure returns `TRUE` if `` `GlobalPortEnabled` `` has been set to `TRUE`; otherwise it returns `FALSE`.
- In a multitenant environment, you can execute this function in both the CDB root and PDBs.

#### 203.4.27 SETFTPPORT Procedure

This procedure sets the FTP port to a new value.

Syntax

```
DBMS_XDB_CONFIG.SETFTPPORT(
   new_port  IN  NUMBER);
```

Parameters

Table 203-19 SETFTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the FTP port is set |

#### 203.4.28 SETGLOBALPORTENABLED Procedure

This procedure enables Oracle Enterprise Manager Database Express (EM Express) clients to use a single port (called a global port), for the session rather than using a port dedicated to the PDB.

Syntax

Note:

Starting from Oracle Database 21c Release, Oracle Enterprise Manager Database Express (EM Express) is deprecated. Oracle recommends that you do not use deprecated values in new applications. Support for deprecated features is for backward compatibility only.
```
DBMS_XDB_CONFIG.SETGLOBALPORTENABLED (
   isenabled  IN  BOOLEAN);
```

Parameters

Table 203-20 SETGLOBALPORTENABLED Procedure Parameters

| Parameter | Description |
| --- | --- |
| `isenabled` | `TRUE` enables the EM Express client to use a global port for the session rather than using the PDB that allocated the port.  `FALSE` enables the port ID to determine the PDB to use.  The default is `TRUE` for PDBs but `FALSE` for the CDB root. |

Usage Notes

- Use the `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` procedure if you use EM Express to manage database ports in a multitenant environment.
- To use a global port, you must enable it in both the CDB and the PDB. PDBs have it enabled by default. For CDBs, you must run the `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` procedure in the CDB root.
- After you set `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` to `TRUE`, then you must specify a PDB to use for the global port. You can do so by specifying the PDB name in the Container Name field of the EM Express login page. For example, if you enter `hr_pdb`, then the EM Express URL becomes `http://server_name:5500/hr_pdb/em`. This example uses the port `5500` in the CDB root, which in turn routes messages to the EM Express in the PDB `hr_pdb`. The port can be an HTTP or HTTPS port.
- The PDB that you specify in the EM Express login page must be open in read/write mode before you can run `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED`. You can check the read/write mode status of a PDB by connecting to the PDB and then querying the `OPEN_MODE` column of the `V$PDBS` dynamic view.
- The `DBMS_XDB_CONFIG.ISGLOBALPORTENABLED` function returns the value of the `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` setting.
- You can use the `XDB_PROTOCOLS` lockdown profile to control the security for the global port.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG-GUID-AB5E62DB-7E2A-4B5A-BA96-A2BD2DF15275) for information about lockdown profiles

#### 203.4.29 SETHTTPPORT Procedure

This procedure sets the HTTP port to a new value.

Syntax

```
DBMS_XDB_CONFIG.SETHTTPPORT(
   new_port  IN  NUMBER);
```

Parameters

Table 203-21 SETHTTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the HTTP port is set |

#### 203.4.30 SETHTTPCONFIGREALM Procedure

This procedure modifies the realm value.

Syntax

```
DBMS_XDB_CONFIG.SETHTTPCONFIGREALM(
   realm IN VARCHAR2);
```

Parameters

Table 203-22 SETHTTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `realm` | Realm as defined in IETF's RFC2617 |

#### 203.4.31 SETHTTPSPORT Procedure

This procedure sets the HTTPS port to a new value.

Syntax

```
DBMS_XDB_CONFIG.SETHTTPSPORT(
   new_port  IN  NUMBER);
```

Parameters

Table 203-23 SETHTTPSPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the HTTPS port is set |

#### 203.4.32 SETLISTENERENDPOINT Procedure

This procedure sets the parameters of a listener end point corresponding to the XML DB HTTP server.

Both HTTP and HTTP2 end points can be set by invoking this procedure.

Syntax

```
DBMS_XDB_CONFIG.SETLISTENERENDPOINT (
   endpoint  IN  NUMBER, 
   host      IN  VARCHAR2,    port      IN  NUMBER, 
   protocol  IN  NUMBER);
```

Parameters

Table 203-24 SETLISTENERENDPOINT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `endpoint` | End point to be set. Its value can be `XDB_ENDPOINT_HTTP` or `XDB_ENDPOINT_HTTP2`. |
| `host` | Interface on which the listener end point is to listen. Its value can be ' `LOCALHOST`,' `NULL`, or a hostname. If its value is ' `LOCALHOST` ' the listener end point is permitted to only listen on the localhost interface. If its value is `NULL` or hostname, the listener end point is permitted to listen on both localhost and non-localhost interfaces. |
| `port` | Port on which the listener end point is to listen |
| `protocol` | Transport protocol that the listener end point is to accept. Its value can be `XDB_PROTOCOL_TCP` or `XDB_PROTOCOL_TCPS` |

#### 203.4.33 SETLISTENERLOCALACCESS Procedure

This procedure restricts all listener end points of the XML DB HTTP server to listen either only on the localhost interface (when `l_access` is set to `TRUE`) or to listen on both localhost and non-localhost interfaces (when `l_access` is set to `FALSE`).

Syntax

```
DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS (
   l_access   BOOLEAN);
```

Parameters

Table 203-25 SETLISTENERLOCALACCESS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `l_access`. | `TRUE` or `FALSE`. |

#### 203.4.34 SETREMOTEHTTPPORT Procedure

This procedure sets a remote HTTP port to a new value.

Syntax

```
DBMS_XDB_CONFIG.SETREMOTEHTTPPORT(
   new_port  IN  NUMBER);
```

Parameters

Table 203-26 SETREMOTEHTTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the remote HTTP port is set |

#### 203.4.35 SETREMOTEHTTPSPORT Procedure

This procedure sets a remote HTTPS port to a new value.

Syntax

```
DBMS_XDB_CONFIG.SETREMOTEHTTPSPORT (
   new_port  IN  NUMBER);
```

Parameters

Table 203-27 SETREMOTEHTTPSPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the remote HTTPS port is set |

#### 203.4.36 USEDPORT Function

This function obtains the port numbers used by other pluggable databases in the same consolidation database.

Syntax

```
DBMS_XDB_CONFIG.USEDPORT RETURN XMLTYPE;
```