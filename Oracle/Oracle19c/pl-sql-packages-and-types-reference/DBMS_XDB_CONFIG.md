---
title: DBMS_XDB_CONFIG
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_XDB_CONFIG.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_XDB_CONFIG` package provides an interface for configuring Oracle XML DB and its repository.

This chapter contains the following topics:

**See Also:** [*Oracle XML DB Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADXDB5449)

### DBMS\_XDB\_CONFIG Overview

PL/SQL package `DBMS_XDB_CONFIG` is the Oracle XML DB resource application program interface (API) for PL/SQL for DBAs to configure their system. This API provides functions and procedures to access and manage Oracle XML DB Repository resources using PL/SQL. It includes methods for managing resource security and Oracle XML DB configuration.

Oracle XML DB Repository is modeled on XML, and provides a database file system for any data. The repository maps path names (or URLs) onto database objects of XMLType and provides management facilities for these objects.

PL/SQL package DBMS\_XDB\_CONFIG is an API that you can use to manage all of the following:

- Oracle XML DB resources
- Oracle XML DB security based on access control lists (ACLs). An ACL is a list of access control entries (ACEs) that determines which principals (users and roles) have access to which resources.
- Oracle XML DB configuration

### DBMS\_XDB\_CONFIG Security Model

Owned by `XDB`, the `DBMS_XDB_CONFIG` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### DBMS\_XDB\_CONFIG Constants

The `DBMS_XDB_CONFIG` package defines several enumerated constants that should be used for specifying parameter values.

These constants are shown in the following table.

Table 1 DBMS\_XDB\_CONFIG Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `XDB_ENDPOINT_HTTP` | `NUMBER` | 1 | Defining listener for first HTTP port |
| `XDB_ENDPOINT_HTTP2` | `NUMBER` | 2 | Defining listener for second HTTP port |
| `XDB_ENDPOINT_RHTTP` | `NUMBER` | 3 | Defining listener for a remote HTTP port |
| `XDB_ENDPOINT_RHTTPS` | `NUMBER` | 4 | Defining listener for a remote HTTPS port |
| `XDB_PROTOCOL_TCP` | `NUMBER` | 1 | Defining listener for HTTP protocol |
| `XDB_PROTOCOL_TCPS` | `NUMBER` | 2 | Defining listener for HTTPS protocol |

### Summary of DBMS\_XDB\_CONFIG Subprograms

The `DBMS_XDB_CONFIG` package uses subprograms for configuring Oracle XML DB and its repository.

These subprograms are listed in the following table.

Table 2 DBMS\_XDB\_CONFIG Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADDHTTPEXPIREMAPPING Procedure | Adds to `XDB$CONFIG` a mapping of the URL pattern to an expiration date. This will control the Expire headers for URLs matching the pattern. |
| ADDMIMEMAPPING Procedure | Adds a mime mapping to XDB configuration |
| ADDSCHEMALOCMAPPING Procedure | Adds a schema location mapping to the XDB configuration |
| ADDSERVLET Procedure | Adds a servlet to XDB configuration |
| ADDSERVLETMAPPING Procedure | Adds a servlet mapping to XDB configuration |
| ADDSERVLETSECROLE Procedure | Adds a security role `REF` to a specified servlet in XDB configuration |
| ADDXMLEXTENSION Procedure | Adds adds the following XML extension to the XDB configuration under `<xml-extensions>`: extension |
| CFG\_GET Function | Retrieves the session’s configuration information as an `XMLType` instance |
| CFG\_REFRESH Procedure | Refreshes the session’s configuration information to the latest configuration |
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

### ADDHTTPEXPIREMAPPING Procedure

This procedure adds to `XDB$CONFIG` a mapping of the URL pattern to an expiration date. This will control the Expire headers for URLs matching the pattern.

**Syntax**

```md
DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING (
     pattern    IN    VARCHAR2,
     expire     IN    VARCHAR2);
```

**Parameters**

Table 3 *ADDHTTPEXPIREMAPPING Procedure Parameters*

| Parameter | Description |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pattern` | URL pattern (only \* accepted as wildcards) |  |  |  |  |  |  |  |  |  |  |  |  |
| `expire` | {::nomarkdown}\<p>Expiration directive, follows the `ExpireDefault` in Apache’s `mod_expires`: \</p>\<pre class="oac\_no\_warn" dir="ltr">base \[plus\] (num type)\* – base: now | modification – type: year | years | month | months | week | weeks | day | days | minute | minutess | second | seconds\</pre> {:/} |

**Examples**

```md
DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING ('/public/test1/*', 'now plus 4 weeks');
DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING (
             '/public/test2/*', 'modification plus 1 day 30 seconds');
```

### ADDMIMEMAPPING Procedure

This procedure adds the following mime mapping to XDB configuration:

```md
<mime-mapping>
<extension>extension</extension>
<mime-type>mimetype</mime-type>
</mime-mapping>
```

**Syntax**

```md
DBMS_XDB_CONFIG.ADDMIMEMAPPING(
     extension    IN   VARCHAR2,
     mimetype     IN   VARCHAR2);
```

**Parameters**

Table 4 *ADDMIMEMAPPING Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `extension` | Extension for which a mime type is being added |
| `mimetype` | Mime type |

### ADDSCHEMALOCMAPPING Procedure

This procedure adds the following schema location mapping to the XDB configuration:

```md
<schemaLocation-mapping>
     <namespace>namespace</namespace>
     <element>element</element>
      <schemaURL>schemaURL</schemaURL>
</schemaLocation-mapping>
```

**Syntax**

```md
DBMS_XDB_CONFIG.ADDSCHEMALOCMAPPING(
     namespace    IN   VARCHAR2,
     element      IN   VARCHAR2,
     schemaURL    IN   VARCHAR2);
```

**Parameters**

Table 5 *ADDSCHEMALOCMAPPING Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `namespace` | Namespace |
| `element` | Element |
| `schemaURL` | Schema URL |

### ADDSERVLET Procedure

This procedure adds a servlet to XDB configuration.

IT adds the following servlet:

```md
<servlet>
     <servlet-name>name</servlet-name>     <servlet-language>language</servlet-language>
     <display-name>dispname</display-name>
     <description>descript</description>
     <servlet-class>class</servlet-class>
     <servlet-schema>schema</servlet-schema>
</servlet>
```

**Syntax**

```md
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

**Parameters**

Table 6 ADDSERVLET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |
| `language` | Must be one of “C”, “Java”, “PL/SQL” |
| `dispname` | Display name |
| `icon` | Icon |
| `descript` | Description |
| `class` | The `class` / `jspfile` / `plsql` function corresponding to this servlet. The first non- `NULL` argument amongst these three is chosen, and the others are treated as `NULL`. |
| `jspfile` | This parameter is not supported. Always provide `NULL` value for this parameter. System throws an error if the value is not `NULL`. |
| `plsql` | The `class` / `jspfile` / `plsql` function corresponding to this servlet. The first non- `NULL` argument amongst these three is chosen, and the others are treated as `NULL`. |
| `schema` | Schema is used to specify `servlet-schema` xml element name in `xdbconfig.xml`. It indicates the Oracle schema in which the Java class is loaded.  If you do not specify any value, then the schema is searched using the default resolver specification. |

### ADDSERVLETMAPPING Procedure

This procedure adds a servlet mapping to XDB configuration.

It adds the following servlet mapping:

```md
<servlet-mapping>
     <servlet-pattern>pattern</servlet-pattern>
     <servlet-name>name</servlet-name>
</servlet-mapping>
```

**Syntax**

```md
DBMS_XDB_CONFIG.ADDSERVLETMAPPING(
     pattern   IN   VARCHAR2,     name      IN   VARCHAR2);
```

**Parameters**

Table 7 *ADDSERVLETMAPPING Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `pattern` | Sservlet pattern |
| `name` | Servlet name |

### ADDSERVLETSECROLE Procedure

This procedure adds the security role `REF` to a specified servlet in XDB configuration.

It adds the following security role as shown in the following:

```md
<security-role-ref>
     <role-name>rolename</role-name>
     <role-link>rolelink</role-link>
     <description>descript</description>
</security-role-ref>
```

**Syntax**

```md
DBMS_XDB_CONFIG.ADDSERVLETSECROLE(
     servname    IN   VARCHAR2,     rolename    IN   VARCHAR2,     rolelink    IN   VARCHAR2,     descript    IN   VARCHAR2 := NULL);
```

**Parameters**

Table 8 *ADDSERVLETSECROLE Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `servname` | Sservlet name |
| `rolename` | Role name |
| `rolelink` | Role link |
| `descript` | Description |

### ADDXMLEXTENSION Procedure

This procedure adds an XML extension to the XDB configuration under `<xml-extensions>`.

It adds the following XML extension to the XDB configuration, under `<xml-extensions>`:

```md
<extension>extension</extension>
```

**Syntax**

```md
DBMS_XDB_CONFIG.ADDXMLEXTENSION(
     extension    IN   VARCHAR2);
```

**Parameters**

Table 9 *ADDXMLEXTENSION Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `extension` | XML extension to be added |

### CFG\_GET Function

This function retrieves the session’s configuration information as an `XMLType` instance.

**Syntax**

```md
DBMS_XDB_CONFIG.CFG_GET
 RETURN SYS.XMLType;
```

### CFG\_REFRESH Procedure

This procedure refreshes the session’s configuration information to the latest configuration.

**Syntax**

```md
DBMS_XDB_CONFIG.CFG_REFRESH;
```

### CFG\_UPDATE Procedure

This procedure updates the configuration information and commits the change.

**Syntax**

```md
DBMS_XDB_CONFIG.CFG_UPDATE(
   xdbconfig   IN  SYS.XMLTYPE);
```

**Parameters**

Table 10 CFG\_UPDATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xdbconfig` | The new configuration data |

### DELETEHTTPEXPIREMAPPING Procedure

This procedure deletes from `XDB$CONFIG` all mappings of the URL pattern to an expiration date.

**Syntax**

```md
DBMS_XDB_REPOS.DELETEHTTPEXPIREMAPPING(
     pattern  IN   VARCHAR2);
```

**Parameters**

Table 11 DELETEHTTPEXPIREMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pattern` | URL pattern (only \* accepted as wildcards) |

### DELETEMIMEMAPPING Procedure

This procedure deletes the mime mapping for a specified extension from the XDB configuration.

**Syntax**

```md
DBMS_XDB_CONFIG.DELETEMIMEMAPPING(
     extension    IN   VARCHAR2);
```

**Parameters**

Table 12 *DELETEMIMEMAPPING Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `extension` | Extension for which a mime type is to be deleted |

### DELETESCHEMALOCMAPPING Procedure

This procedure deletes the schema location mapping for a specified schema URL from the XDB configuration.

**Syntax**

```md
DBMS_XDB_CONFIG.DELETESCHEMALOCMAPPING(
     schemaURL    IN   VARCHAR2);
```

**Parameters**

Table 13 *DELETESCHEMALOCMAPPING Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `schemaURL` | Schema URL |

### DELETESERVLET Procedure

This procedure deletes a servlet from the XDB configuration.

**Syntax**

```md
DBMS_XDB_CONFIG.DELETESERVLET(
     name        IN   VARCHAR2);
```

**Parameters**

Table 14 *DELETESERVLET Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |

### DELETESERVLETMAPPING Procedure

This procedure deletes the servlet mapping for a specified servlet name from the XDB configuration.

**Syntax**

```md
DBMS_XDB_CONFIG.DELETESERVLETMAPPING(
     name      IN   VARCHAR2);
```

**Parameters**

Table 15 *DELETESERVLETMAPPING Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |

### DELETESERVLETSECROLE Procedure

This procedure deletes the specified role from a servlet in the XDB configuration.

**Syntax**

```md
DBMS_XDB_CONFIG.DELETESERVLETSECROLE(
     servname    IN   VARCHAR2,     rolename    IN   VARCHAR2);
```

**Parameters**

Table 16 *DELETESERVLETSECROLE Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `servname` | Servlet name |
| `rolename` | Name of the role to be deleted |

### DELETEXMLEXTENSION Procedure

This procedure deletes the specified XML extension from the XDB configuration.

**Syntax**

```md
DBMS_XDB_CONFIG.DELETEXMLEXTENSION(
     extension    IN   VARCHAR2);
```

**Parameters**

Table 17 *DELETEXMLEXTENSION Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `extension` | XML extension to be deleted |

### ENABLEDIGESTAUTHENTICATION Procedure

This procedure enables digest authentication. It will list digest as the first authentication mechanism to be used by the XML DB HTTP server.

**Syntax**

```md
DBMS_XDB_CONFIG.ENABLEDIGESTAUTHENTICATION;
```

### GETFTPPORT Function

This procedure gets the value of the current FTP port.

**Syntax**

```md
DBMS_XDB_CONFIG.GETFTPPORT
 RETURN NUMBER;
```

### GETHTTPCONFIGREALM Function

This function gets the realm name. Definition of a realm is referenced in IETF’s RFC2617.

**Syntax**

```md
DBMS_XDB_CONFIG.GETHTTPCONFIGREALM
 RETURN VARCHAR2;
```

### GETHTTPPORT Function

This function gets the value of the current HTTP port.

**Syntax**

```md
DBMS_XDB_CONFIG.GETHTTPPORT
 RETURN NUMBER;
```

### GETHTTPSPORT Function

This procedure gets the value of the current HTTPS port.

**Syntax**

```md
DBMS_XDB_CONFIG.GETHTTPSPORT
 RETURN NUMBER;
```

**Usage Notes**

Returns `NULL` if no port has been configured

### GETLISTENERENDPOINT Procedure

This procedure retrieves the parameters of a listener end point corresponding to the XML DB HTTP server. The parameters of both HTTP and HTTP2 end points can be retrieved by invoking this procedure.

**Syntax**

```md
DBMS_XDB_CONFIG.GETLISTENERENDPOINT (
   endpoint  IN   NUMBER,
   host      OUT  VARCHAR2,    port      OUT  NUMBER,
   protocol  OUT  NUMBER);
```

**Parameters**

Table 18 GETLISTENERENDPOINT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `endpoint` | End point to be retrieved. Its value can be `XDB_ENDPOINT_HTTP` or `XDB_ENDPOINT_HTTP2`. |
| `host` | Interface on which the listener end point listens |
| `port` | Port on which the listener end point listens |
| `protocol` | Transport protocol accepted by the listener end point |

### GETREMOTEHTTPPORT Function

This function gets the value of a remote HTTP port.

**Syntax**

```md
DBMS_XDB_CONFIG.GETREMOTEHTTPPORT
 RETURN NUMBER;
```

### GETREMOTEHTTPSPORT Function

This function gets the value of a remote HTTPS port.

**Syntax**

```md
DBMS_XDB_CONFIG.GETREMOTEHTTPSPORT
 RETURN NUMBER;
```

### ISGLOBALPORTENABLED Function

This procedure returns the value of the `GlobalPortEnabled` setting.

**Syntax**

```md
DBMS_XDB_CONFIG.ISGLOBALPORTENABLED RETURN BOOLEAN;
```

**Usage Notes**

- This procedure returns `TRUE` if `GlobalPortEnabled` has been set to `TRUE`; otherwise it returns `FALSE`.
- In a multitenant environment, you can execute this function in both the CDB root and PDBs.

### SETFTPPORT Procedure

This procedure sets the FTP port to a new value.

**Syntax**

```md
DBMS_XDB_CONFIG.SETFTPPORT(
   new_port  IN  NUMBER);
```

**Parameters**

Table 19 SETFTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the FTP port is set |

### SETGLOBALPORTENABLED Procedure

This procedure enables Oracle Enterprise Manager Database Express (EM Express) clients to use a single port (called a global port), for the session rather than using a port dedicated to the PDB.

**Syntax**

```md
DBMS_XDB_CONFIG.SETGLOBALPORTENABLED (
   isenabled  IN  BOOLEAN);
```

**Parameters**

Table 20 SETGLOBALPORTENABLED Procedure Parameters

| Parameter | Description |
| --- | --- |
| `isenabled` | `TRUE` enables the EM Express client to use a global port for the session rather than using the PDB that allocated the port.  `FALSE` enables the port ID to determine the PDB to use.  The default is `TRUE` for PDBs but `FALSE` for the CDB root. |

**Usage Notes**

- Use the `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` procedure if you use EM Express to manage database ports in a multitenant environment.
- To use a global port, you must enable it in both the CDB and the PDB. PDBs have it enabled by default. For CDBs, you must run the `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` procedure in the CDB root.
- After you set `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` to `TRUE`, then you must specify a PDB to use for the global port. You can do so by specifying the PDB name in the **Container Name** field of the EM Express login page. For example, if you enter `hr_pdb`, then the EM Express URL becomes `http://server_name:5500/hr_pdb/em`. This example uses the port `5500` in the CDB root, which in turn routes messages to the EM Express in the PDB `hr_pdb`. The port can be an HTTP or HTTPS port.
- The PDB that you specify in the EM Express login page must be open in read/write mode before you can run `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED`. You can check the read/write mode status of a PDB by connecting to the PDB and then querying the `OPEN_MODE` column of the `V$PDBS` dynamic view.
- The `DBMS_XDB_CONFIG.ISGLOBALPORTENABLED` function returns the value of the `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` setting.
- You can use the `XDB_PROTOCOLS` lockdown profile to control the security for the global port.

**See Also:**

[*Oracle Database 2 Day DBA*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADMQS-GUID-06C767B0-B435-4C6B-9123-C39C030DF457) for information about using `DBMS_XDB_CONFIG.SETGLOBALPORTENABLED` to start EM Express for a PDB

[*Oracle Database Security Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DBSEG-GUID-AB5E62DB-7E2A-4B5A-BA96-A2BD2DF15275)

for information about lockdown profiles

### SETHTTPPORT Procedure

This procedure sets the HTTP port to a new value.

**Syntax**

```md
DBMS_XDB_CONFIG.SETHTTPPORT(
   new_port  IN  NUMBER);
```

**Parameters**

Table 21 SETHTTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the HTTP port is set |

### SETHTTPCONFIGREALM Procedure

This procedure modifies the realm value.

**Syntax**

```md
DBMS_XDB_CONFIG.SETHTTPCONFIGREALM(
   realm IN VARCHAR2);
```

**Parameters**

Table 22 SETHTTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `realm` | Realm as defined in IETF’s RFC2617 |

### SETHTTPSPORT Procedure

This procedure sets the HTTPS port to a new value.

**Syntax**

```md
DBMS_XDB_CONFIG.SETHTTPSPORT(
   new_port  IN  NUMBER);
```

**Parameters**

Table 23 SETHTTPSPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the HTTPS port is set |

### SETLISTENERENDPOINT Procedure

This procedure sets the parameters of a listener end point corresponding to the XML DB HTTP server.

Both HTTP and HTTP2 end points can be set by invoking this procedure.

**Syntax**

```md
DBMS_XDB_CONFIG.SETLISTENERENDPOINT (
   endpoint  IN  NUMBER,
   host      IN  VARCHAR2,    port      IN  NUMBER,
   protocol  IN  NUMBER);
```

**Parameters**

Table 24 SETLISTENERENDPOINT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `endpoint` | End point to be set. Its value can be `XDB_ENDPOINT_HTTP` or `XDB_ENDPOINT_HTTP2`. |
| `host` | Interface on which the listener end point is to listen. Its value can be ‘ `LOCALHOST`,’ `NULL`, or a hostname. If its value is ‘ `LOCALHOST` ’ the listener end point is permitted to only listen on the localhost interface. If its value is `NULL` or hostname, the listener end point is permitted to listen on both localhost and non-localhost interfaces. |
| `port` | Port on which the listener end point is to listen |
| `protocol` | Transport protocol that the listener end point is to accept. Its value can be `XDB_PROTOCOL_TCP` or `XDB_PROTOCOL_TCPS` |

### SETLISTENERLOCALACCESS Procedure

This procedure restricts all listener end points of the XML DB HTTP server to listen either only on the localhost interface (when `l_access` is set to `TRUE`) or to listen on both localhost and non-localhost interfaces (when `l_access` is set to `FALSE`).

**Syntax**

```md
DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS (
   l_access   BOOLEAN);
```

**Parameters**

Table 25 SETLISTENERLOCALACCESS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `l_access`. | `TRUE` or `FALSE`. |

### SETREMOTEHTTPPORT Procedure

This procedure sets a remote HTTP port to a new value.

**Syntax**

```md
DBMS_XDB_CONFIG.SETREMOTEHTTPPORT(
   new_port  IN  NUMBER);
```

**Parameters**

Table 26 SETREMOTEHTTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the remote HTTP port is set |

### SETREMOTEHTTPSPORT Procedure

This procedure sets a remote HTTPS port to a new value.

**Syntax**

```md
DBMS_XDB_CONFIG.SETREMOTEHTTPSPORT (
   new_port  IN  NUMBER);
```

**Parameters**

Table 27 SETREMOTEHTTPSPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the remote HTTPS port is set |

### USEDPORT Function

This function obtains the port numbers used by other pluggable databases in the same consolidation database.

**Syntax**

```md
DBMS_XDB_CONFIG.USEDPORT RETURN XMLTYPE;
```