---
title: DBMS_XDB
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xdb.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 164 DBMS\_XDB

The `DBMS_XDB` package supports the following features:

- Resource Management subprograms which complement Resource Views
- The Access Control List (ACL)-based Security Mechanism
- Configuration Session Management
- Creation of the XDB username
	See Also:
	- [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)
	- [Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm)

This chapter contains the following topics:

- Using DBMS\_XDB
- Summary of DBMS\_XDB Subprograms

---

## Using DBMS\_XDB

This section contains topics which relate to using the `DBMS_XDB` package.

---

### Overview

The `DBMS_XDB` package supports the following features:

- The Resource Management functionality provides LINK Procedures, EXISTSRESOURCE Function, LOCKRESOURCE Function, GETLOCKTOKEN Procedure, UNLOCKRESOURCE Function, CREATERESOURCE Functions, RENAMERESOURCE Procedure, DELETERESOURCE Procedure, GETRESOID Function, CREATEOIDPATH Function, REBUILDHIERARCHICALINDEX Procedure and CREATEFOLDER Function subprograms which complement Resource Views.
- The Access Control List (ACL)-based Security Mechanism can be used with in-hierarchy ACLs stored by the database or in-memory ACLs that may be stored outside the database. Some of these methods can be used for both Oracle resources and arbitrary database objects. Use CHECKPRIVILEGES Function, GETACLDOCUMENT Function, CHANGEPRIVILEGES Function and GETCHILDRESPATHS Function for Oracle Resources. ACLCHECKPRIVILEGES Function provides access to Oracle's ACL-based Security mechanism without storing objects in the Hierarchy.
- Configuration Session Management is supported by CFG\_REFRESH Procedure, CFG\_GET Function and CFG\_UPDATE Procedure. methods.
- The XDB username is created during XDB installation. This user owns a set of default tables and packages. GETXDB\_TABLESPACE Function and MOVEXDB\_TABLESPACE Procedure enable movement of schemas to a specified tablespace, and support the default `SYSAUX` tablespace introduction

---

### Deprecated Subprograms

Note:

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only and may be terminated in future releases.

The following subprograms are deprecated with Oracle Database 11g:

- MOVEXDB\_TABLESPACE Procedure
- REBUILDHIERARCHICALINDEX Procedure

This functionality is replaced by the subprograms of the same name in the [DBMS\_XDB\_ADMIN](d_xdb_admin.md) package:

- [MOVEXDB\_TABLESPACE Procedure](d_xdb_admin.md)
- [REBUILDHIERARCHICALINDEX Procedure](d_xdb_admin.md)

---

### Security Model

Owned by `XDB`, the `DBMS_XDB` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user. Subprograms that operate on the XDB Configuration will succeed only if the current user is `SYS` or `XDB`, or the current user has the `XDBADMIN` or `DBA` role.

---

### Constants

Table 164-1 Defined Constants for DBMS\_XDB

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `DELETE_RESOURCE` | `NUMBER` | 1 | Deletes a resource; fails if the resource has children. |
| `DELETE_RECURSIVE` | `NUMBER` | 2 | Deletes a resource and its children, if any. |
| `DELETE_FORCE` | `NUMBER` | 3 | Deletes the resource, even if the object it contains is invalid. |
| `DELETE_RECURSIVE_FORCE` | `NUMBER` | 4 | Deletes a resource and its children, if any, even if the object it contains is invalid. |

---

## Summary of DBMS\_XDB Subprograms

Table 164-2 DBMS\_XDB Package Subprograms

| Subprogram | Description |
| --- | --- |
| ACLCHECKPRIVILEGES Function | Checks access privileges granted to the current user by specified ACL document on a resource whose owner is specified by the 'owner' parameter. |
| ADDHTTPEXPIREMAPPING Procedure | Adds to `xdb$config` a mapping of the URL pattern to an expiration date. This will control the Expire headers for URLs matching the pattern. |
| ADDMIMEMAPPING Procedure | Adds a mime mapping to the XDB configuration |
| ADDSCHEMALOCMAPPING Procedure | Adds a schema location mapping to the XDB configuration |
| ADDSERVLET Procedure | Adds a servlet to XDB configuration |
| ADDSERVLETMAPPING Procedure | Adds a servlet mapping to XDB configuration |
| ADDSERVLETSECROLE Procedure | Adds a security role `REF` to a specified servlet in the XDB configuration |
| ADDXMLEXTENSION Procedure | Adds adds an XML extension to the XDB configuration |
| APPENDPATH Procedure | Appends a childpath to a parentpath |
| APPENDPATH Procedure | Takes in user-defined metadata either as a `REF` to `XMLTYPE` or an `XMLTYPE` and adds it to the desired resource |
| CFG\_GET Function | Retrieves the session's configuration information |
| CFG\_REFRESH Procedure | Refreshes the session's configuration information to the latest configuration |
| CFG\_UPDATE Procedure | Updates the configuration information |
| CHANGEOWNER Procedure | Changes the owner of the resource/s to the specified owner. |
| CHANGEPRIVILEGES Function | Adds a specified ACE to a specified resource's ACL |
| CHECKPRIVILEGES Function | Checks access privileges granted to the current user on the specified resource |
| CREATEFOLDER Function | Creates a new folder resource in the hierarchy |
| CREATEOIDPATH Function | Creates a virtual path to the resource based on object ID |
| CREATERESOURCE Functions | Creates a new resource |
| DELETEHTTPEXPIREMAPPING Procedure | Deletes from `xdb$config` all mappings of the URL pattern to an expiration date |
| DELETEMIMEMAPPING Procedure | Deletes the mime mapping from the XDB configuration |
| DELETERESOURCE Procedure | Deletes a resource from the hierarchy |
| DELETERESOURCEMETADATA Procedures | Deletes metadata from a resource (can be used for schema-based or nonschema-based metadata) |
| DELETESCHEMALOCMAPPING Procedure | Deletes the schema location mapping for the specified schema URL from the XDB configuration. |
| DELETESERVLET Procedure | Deletes a servlet from XDB configuration |
| DELETESERVLETMAPPING Procedure | Deletes the servlet mapping for the specified servlet name from the XDB configuration |
| DELETESERVLETSECROLE Procedure | Deletes the specified role from a servlet in the XDB configuration |
| DELETEXMLEXTENSION Procedure | Deletes the specified XML extension from the XDB configuration |
| EXISTSRESOURCE Function | Determines if a resource is the hierarchy, based on its absolute path |
| GETACLDOCUMENT Function | Retrieves ACL document that protects resource given its path name |
| GETCHILDRESPATHS Function | Returns a cursor over the absolute paths of all the child resources |
| GETCONTENTBLOB Function | Retrieves the contents of a resource returned as a BLOB |
| GETCONTENTCLOB Function | Retrieves the contents of a resource returned as a CLOB |
| GETCONTENTVARCHAR2 Function | Retrieves the contents of a resource returned as a string |
| GETCONTENTXMLREF Function | Retrieves the contents of a resource returned as a a `REF` to an `XMLTYPE` |
| GETCONTENTXMLTYPE Function | Retrieves the contents of a resource returned as an `XMLTYPE` |
| GETFTPPORT Function | Gets the value of the current FTP port |
| GETHTTPPORT Function | Gets the value of the current HTTP port |
| GETLOCKTOKEN Procedure | Returns that resource's lock token for the current user given a path to a resource |
| GETLISTENERENDPOINT Procedure | Retrieves the parameters of a listener end point corresponding to the XML DB HTTP server |
| GETRESOID Function | Returns the object ID of the resource from its absolute path |
| GETXDB\_TABLESPACE Function | Returns the current tablespace of the XDB (user) |
| HASBLOBCONTENT Function | Returns `TRUE` if the resource has BLOB content |
| HASCHARCONTENT Function | Returns `TRUE` if the resource has character content |
| HASXMLCONTENT Function | Returns `TRUE` if the resource has XML content |
| HASXMLREFERENCE Function | Returns `TRUE` if the resource has `REF` to XML content |
| ISFOLDER Function | Returns `TRUE` if the resource is a folder or container |
| LINK Procedures | Creates a link to an existing resource |
| LOCKRESOURCE Function | Gets a WebDAV-style lock on that resource given a path to that resource |
| MOVEXDB\_TABLESPACE Procedure | \[Deprecated\] Moves the XDB (user) to the specified tablespace |
| PROCESSLINKS Procedure | Processes document links in the specified resource |
| PURGERESOURCEMETADATA Procedure | Deletes all user metadata from a resource |
| REBUILDHIERARCHICALINDEX Procedure | \[Deprecated\] Rebuilds the hierarchical index after import or export operations |
| RENAMERESOURCE Procedure | Renames the XDB resource |
| SETACL Procedure | Sets the ACL on a specified resource |
| SETCONTENT Procedures | Replaces the contents of a specified resource with specified datatype |
| SETFTPPORT Procedure | Sets the FTP port to a new value |
| SETHTTPPORT Procedure | Sets the HTTP port to a new value |
| SETLISTENERENDPOINT Procedure | Sets the parameters of a listener end point corresponding to the XML DB HTTP server |
| SETLISTENERLOCALACCESS Procedure | Restricts all listener end points of the XML DB HTTP server to listen either only on the localhost interface or on both localhost and non-localhost interfaces |
| SPLITPATH Procedure | Splits the path into a parentpath and childpath |
| TOUCHRESOURCE Procedure | Changes the modification time of the resource to the current time |
| UPDATERESOURCEMETADATA Procedures | Updates metadata for a resource |
| UNLOCKRESOURCE Function | Unlocks the resource given a lock token and resource path |

---

### ACLCHECKPRIVILEGES Function

This function checks access privileges granted to the current user by specified ACL document by the `OWNER` of the resource. Returns positive integer if all privileges are granted.

Syntax

```
DBMS_XDB.ACLCHECKPRIVILEGES(
   acl_path  IN  VARCHAR2,
   owner     IN  VARCHAR2,
   privs     IN  xmltype)
 RETURN PLS_INTEGER;
```

Parameters

Table 164-3 ACLCHECKPRIVILEGES Function Parameters

| Parameter | Description |
| --- | --- |
| `acl_path` | Absolute path in the Hierarchy for ACL document |
| `owner` | Resource owner name; the pseudo user "DAV:owner" is replaced by this user during ACL privilege resolution |
| `privs` | An `XMLType` instance of the privilege element specifying the requested set of access privileges. See description for CHECKPRIVILEGES Function. |

---

### ADDHTTPEXPIREMAPPING Procedure

This procedure adds to `xdb$config` a mapping of the URL pattern to an expiration date. This will control the Expire headers for URLs matching the pattern.

Syntax

```
DBMS_XDB.ADDHTTPEXPIREMAPPING (
     pattern    IN    VARCHAR2,
     expire     IN    VARCHAR2);
```

Parameters

Table 164-4 ADDHTTPEXPIREMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pattern` | URL pattern (only \* accepted as wildcards) |
| `expire` | Expiration directive, follows the `ExpireDefault` in Apache's `mod_expires`:  ``` base [plus] (num type)* -- base: now \| modification -- type: year\|years\|month\|months\|week\|weeks\|day\|days\| minute\|minutess\|second\|seconds ``` |

Examples

```
DBMS_XDB.ADDHTTPEXPIREMAPPING ('/public/test1/*', 'now plus 4 weeks');
DBMS_XDB.ADDHTTPEXPIREMAPPING (
             '/public/test2/*', 'modification plus 1 day 30 seconds');
```

---

### ADDMIMEMAPPING Procedure

This procedure adds the following mime mapping to XDB configuration:

```
<mime-mapping>
<extension>extension</extension>
<mime-type>mimetype</mime-type>
</mime-mapping>
```

Syntax

```
DBMS_XDB.ADDMIMEMAPPING(
     extension    IN   VARCHAR2,
     mimetype     IN   VARCHAR2);
```

Parameters

Table 164-5 ADDMIMEMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | Extension for which a mime type is being added |
| `mimetype` | Mime type |

---

### ADDSCHEMALOCMAPPING Procedure

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
DBMS_XDB.ADDSCHEMALOCMAPPING(
     namespace    IN   VARCHAR2,
     element      IN   VARCHAR2,
     schemaURL    IN   VARCHAR2);
```

Parameters

Table 164-6 ADDSCHEMALOCMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `namespace` | Namespace |
| `element` | Element |
| `schemaURL` | Schema URL |

---

### ADDSERVLET Procedure

This procedure adds the following servlet to XDB configuration:

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
DBMS_XDB.ADDSERVLET(
     name       IN   VARCHAR2,
    language    IN   VARCHAR2,
    dispname    IN   VARCHAR2,
    icon        IN   VARCHAR2 := NULL,
    descript    IN   VARCHAR2 := NULL,
    class       IN   VARCHAR2 := NULL,
    jspfile     IN   VARCHAR2 := NULL,
    plsql       IN   VARCHAR2 := NULL);
```

Parameters

Table 164-7 ADDSERVLET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |
| `language` | Must be one of "C", "Java", "PL/SQL" |
| `dispname` | Display name |
| `icon` | Icon |
| `descript` | Description |
| `class` | The `class` / `jspfile` / `plsql` function corresponding to this servlet. The first non- `NULL` argument amongst these three is chosen, and the others are treated as `NULL`. |
| `jspfile` | The `class` / `jspfile` / `plsql` function corresponding to this servlet. The first non- `NULL` argument amongst these three is chosen, and the others are treated as `NULL`. |
| `plsql` | The `class` / `jspfile` / `plsql` function corresponding to this servlet. The first non- `NULL` argument amongst these three is chosen, and the others are treated as `NULL`. |
| `schema` | Schema |

---

### ADDSERVLETMAPPING Procedure

This procedure adds the following servlet mapping to XDB configuration:

```
<servlet-mapping>     <servlet-pattern>pattern</servlet-pattern>     <servlet-name>name</servlet-name></servlet-mapping>
```

Syntax

```
DBMS_XDB.ADDSERVLETMAPPING(
     pattern   IN   VARCHAR2,     name      IN   VARCHAR2);
```

Parameters

Table 164-8 ADDSERVLETMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pattern` | Sservlet pattern |
| `name` | Servlet name |

---

### ADDSERVLETSECROLE Procedure

This procedure adds the following security role `REF` to a specified servlet in XDB configuration:

```
<security-role-ref>
     <role-name>rolename</role-name>
     <role-link>rolelink</role-link>
     <description>descript</description>
</security-role-ref>
```

Syntax

```
DBMS_XDB.ADDSERVLETSECROLE(
     servname    IN   VARCHAR2,     rolename    IN   VARCHAR2,     rolelink    IN   VARCHAR2,     descript    IN   VARCHAR2 := NULL);
```

Parameters

Table 164-9 ADDSERVLETSECROLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `servname` | Sservlet name |
| `rolename` | Role name |
| `rolelink` | Role link |
| `descript` | Description |

---

### ADDXMLEXTENSION Procedure

This procedure adds the following XML extension to the XDB configuration under `<xml-extensions>`:

```
<extension>extension</extension>
```

Syntax

```
DBMS_XDB.ADDXMLEXTENSION(
     extension    IN   VARCHAR2);
```

Parameters

Table 164-10 ADDXMLEXTENSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | XML extension to be added |

---

### APPENDPATH Procedure

This procedure appends a childpath to a parentpath.

Syntax

```
DBMS_XDB.APPENDPATH (
     abspath       OUT   VARCHAR2,     parentpath    IN    VARCHAR2,    childpath      IN    VARCHAR2);
```

Parameters

Table 164-11 APPENDPATH Procedure

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |
| `parentpath` | Parentpath |
| `childpath` | Childpath |

---

### APPENDRESOURCEMETADATA Procedure

This procedure takes in user-defined metadata either as a `REF` to `XMLTYPE` or an `XMLTYPE` and adds it to the desired resource.

Syntax

```
DBMS_XDB.APPENDRESOURCEMETADATA (
 abspath   IN  VARCHAR2, 
 metadata  IN  XMLTYPE);

DBMS_XDB.APPENDRESOURCEMETADATA (
 abspath   IN  VARCHAR2, 
 metadata  IN  REF SYS.XMLTYPE);
```

Parameters

Table 164-12 APPENDRESOURCEMETADATA Procedure

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |
| `metadata` | Metadata can be schema based or nonschema-based. Schema-based metadata is stored in its own table. |

Usage Notes

- In the case in which a `REF` is passed in, the procedure stores the `REF` in the resource, and the metadata is stored in a separate table. In this case you are responsible for populating the `RESID` column for the metadata table. Note that the `REF` passed in must be unique. In other words, there must not be a `REF` with the same value in the resource metadata, as this would violate uniqueness of properties. An error is thrown if users attempt to add a `REF` that already exists.
- In the case where the XMLTYPE is passed in, the data is parsed to determine if it is schema-based or not and stored accordingly.

---

### CFG\_GET Function

This function retrieves the session's configuration information as an `XMLType` instance.

Syntax

```
DBMS_XDB.CFG_GET 
 RETURN SYS.XMLType;
```

---

### CFG\_REFRESH Procedure

This procedure refreshes the session's configuration information to the latest configuration.

Syntax

```
DBMS_XDB.CFG_REFRESH;
```

---

### CFG\_UPDATE Procedure

This procedure updates the configuration information and commits the change.

Syntax

```
DBMS_XDB.CFG_UPDATE(
   xdbconfig   IN  SYS.XMLTYPE);
```

Parameters

Table 164-13 CFG\_UPDATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xdbconfig` | The new configuration data |

---

### CHANGEOWNER Procedure

This procedure changes the owner of the resource/s to the specified owner.

Syntax

```
DBMS_XDB.CHANGEOWNER(
     abspath    IN   VARCHAR2,
     owner      IN   VARCHAR2,
     recurse    IN   BOOLEAN := FALSE);
```

Parameters

Table 164-14 CHANGEOWNER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |
| `owner` | New owner for the resource |
| `recurse` | If `TRUE`, recursively change owner of all resources in the folder tree |

---

### CHANGEPRIVILEGES Function

This function adds a specified ACE to a specified resource's ACL.

Syntax

```
DBMS_XDB.CHANGEPRIVILEGES(
   res_path   IN    VARCHAR2,
   ace        IN    xmltype)
 RETURN PLS_INTEGER;
```

Parameters

Table 164-15 CHANGEPRIVILEGES Function Parameters

| Parameter | Description |
| --- | --- |
| `res_path` | Path name of the resource for which privileges need to be changed |
| `ace` | An `XMLType` instance of the `<ace>` element which specifies the `<principal>`, the operation `<grant>` and the list of privileges |

Return Values

A positive integer if the ACL was successfully modified.

Usage Notes

If no ACE with the same principal and the same operation (`grant` / `deny`) already exists in the ACL, the new ACE is added at the end of the ACL.

---

### CHECKPRIVILEGES Function

This function checks access privileges granted to the current user on the specified resource.

Syntax

```
DBMS_XDB.CHECKPRIVILEGES(
   res_path   IN  VARCHAR2,
   privs      IN  xmltype)
 RETURN PLS_INTEGER;
```

Parameters

Table 164-16 CHECKPRIVILEGES Function Parameters

| Parameter | Description |
| --- | --- |
| `res_path` | Absolute path in the Hierarchy for resource |
| `privs` | An `XMLType` instance of the privilege element specifying the requested set of access privileges |

Return Values

A positive integer if all requested privileges granted.

---

### CREATEFOLDER Function

This function creates a new folder resource in the hierarchy.

Syntax

```
DBMS_XDB.CREATEFOLDER(
   path   IN  VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-17 CREATEFOLDER Function Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path name for the new folder |

Return Values

`TRUE` if operation successful; `FALSE`, otherwise.

Usage Notes

The given path name's parent folder must already exist in the hierarchy: if `'/folder1/folder2'` is passed as the path parameter, then `'/folder1'` must already exist.

---

### CREATEOIDPATH Function

This function creates a virtual path to the resource based on object ID.

Syntax

```
DBMS_XDB.CREATEOIDPATH(
   oid    IN   RAW)
 RETURN VARCHAR2;
```

Parameters

Table 164-18 CREATEOIDPATH Function Parameters

| Parameter | Description |
| --- | --- |
| `oid` | Object ID of the resource |

---

### CREATERESOURCE Functions

The functions create a new resource. The description of the overload options precede each version of the syntax

Syntax

Creates a new resource with a specified string as its contents:

```
DBMS_XDB.CREATERESOURCE( 
     abspath        IN  VARCHAR2,
     data           IN  VARCHAR2,
     createfolders  IN  BOOLEAN := FALSE)
 RETURN BOOLEAN;
```

Creates a new resource with a specified `XMLType` data as its contents:

```
DBMS_XDB.CREATERESOURCE(
     abspath        IN  VARCHAR2,
     data           IN  SYS.XMLTYPE,
     createfolders  IN  BOOLEAN := FALSE)
 RETURN BOOLEAN;
```

Given a `REF` to an existing `XMLType` row, creates a resource whose contents point to that row. That row should not already exist inside another resource:

```
DBMS_XDB.CREATERESOURCE(
     abspath        IN  VARCHAR2,
     datarow        IN  REF SYS.XMLTYPE,
     createfolders  IN  BOOLEAN := FALSE)
 RETURN BOOLEAN;
```

Creates a resource with a specified `BLOB` as its contents, and specifies character set of the source `BLOB`:

```
DBMS_XDB.CREATERESOURCE(
     abspath        IN  VARCHAR2,
     data           IN  BLOB,
     csid           IN  NUMBER :=0,
     createfolders  IN  BOOLEAN := FALSE)
 RETURN BOOLEAN;
```

Creates a resource with a specified `BFILE` as its contents, and specifies character set of the source `BFILE`:

```
DBMS_XDB.CREATERESOURCE ( 
     abspath        IN  VARCHAR2,
     data           IN  BFILE,
     csid           IN  NUMBER :=0,
     createfolders  IN  BOOLEAN := FALSE)
 RETURN BOOLEAN;
```

Creates a resource with a specified `CLOB` as its contents:

```
DBMS_XDB.CREATERESOURCE (
     abspath        IN  VARCHAR2,
     data           IN  CLOB,
     createfolders  IN  BOOLEAN := FALSE)
 RETURN BOOLEAN;
```

Given a string, inserts a new resource into the hierarchy with the string as the contents:

```
DBMS_XDB.CREATERESOURCE (
   abspath        IN  VARCHAR2, 
   data           IN  VARCHAR2,
   schemaurl      IN  VARCHAR2 := NULL,
   elem           IN  VARCHAR2 := NULL)
 RETURN BOOLEAN;
```

Given an `XMLTYPE` and a schema URL, inserts a new resource into the hierarchy with the `XMLTYPE` as the contents:

```
DBMS_XDB.CREATERESOURCE (
   abspath        IN  VARCHAR2, 
   data           IN  SYS.XMLTYPE,
   schemaurl      IN  VARCHAR2 := NULL,
   elem           IN  VARCHAR2 := NULL)
 RETURN BOOLEAN;
```

Parameters

Table 164-19 CREATERESOURCE Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource to create. The path name's parent folder must already exist in the hierarchy. In other words, if `/foo/bar.txt` is passed in, then folder `/foo` must already exist. |
| `data` | String buffer containing new resource's contents. The data is parsed to check if it contains a schema-based XML document, and the contents are stored as schema-based in the schema's default table. Otherwise, it is saved as binary data. |
| `datarow` | `REF` to an `XMLType` row to be used as the contents |
| `csid` | Character set id of the document. Must be a valid Oracle ID; otherwise returns an error.  If CSID is not specified, or if a zero CSID is specified, then the character set id of the document is determined as follows:  - From the abspath extension, determine the resource's MIME type. - If the MIME type is \*/xml, then the encoding is detected based on Appendix F of the W3C XML 1.0 Reference at `http://www.w3.org/TR/2000/REC-xml-20001006`; - Otherwise, it is defaulted to the database character set. |
| `createfolders` | If `TRUE`, create the parent folders if they do not exist |
| `schemaurl` | For XML data, schema URL data conforms to (default `NULL`) |
| `elem` | Element name (default `NULL`) |

Return Values

`TRUE` if operation successful; `FALSE`, otherwise.

---

### DELETEHTTPEXPIREMAPPING Procedure

This procedure deletes from `xdb$config` all mappings of the URL pattern to an expiration date.

Syntax

```
DBMS_XDB.DELETEHTTPEXPIREMAPPING(
     pattern  IN   VARCHAR2);
```

Parameters

Table 164-20 DELETEHTTPEXPIREMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pattern` | URL pattern (only \* accepted as wildcards) |

---

### DELETEMIMEMAPPING Procedure

This procedure deletes the mime mapping for a specified extension from the XDB configuration.

Syntax

```
DBMS_XDB.DELETEMIMEMAPPING(
     extension    IN   VARCHAR2);
```

Parameters

Table 164-21 DELETEMIMEMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | Extension for which a mime type is to be deleted |

---

### DELETERESOURCE Procedure

This procedure deletes a resource from the hierarchy.

Syntax

```
DBMS_XDB.DELETERESOURCE(
   path          IN      VARCHAR2,
   delete_option IN      PLS_INTEGER);
```

Parameters

Table 164-22 DELETERESOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path name of the resource to delete |
| `delete_option` | The option that controls how a a resource is deleted; defined in Table 164-1:  - `DELETE_RESOURCE` - `DELETE_RECURSIVE` - `DELETE_FORCE` - `DELETE_RECURSIVE_FORCE` |

---

### DELETERESOURCEMETADATA Procedures

This procedure takes in a resource by absolute path and removes either the schema-based metadata identified by the REF, or the metadata identified by the namespace and name combination, which can be either schema-based or non-schema based. It also takes an additional (optional) parameter that specifies how to delete it. This parameter is only relevant for schema-based resource metadata that needs to be deleted. For non-schema based metadata, this parameter is ignored.

Syntax

Can be used only for schema-based metadata:

```
DBMS_XDB.DELETERESOURCEMETADATA (
   abspath        IN  VARCHAR2, 
   metadata       IN  REF SYS.XMLTYPE,
   delete_option  IN  pls_integer := dbms_xdb.DELETE_RESOURCE_METADATA_CASCADE);
```

Can be used for schema-based or nonschema-based metadata:

```
DBMS_XDB.DELETERESOURCEMETADATA (
   abspath        IN VARCHAR2,
   metadatans     IN VARCHAR2,
   metadataname   IN VARCHAR2,
   delete_option  IN pls_integer := dbms_xdb.DELETE_RESOURCE_METADATA_CASCADE);
```

Parameters

Table 164-23 DELETERESOURCEMETADATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |
| `metadata` | `REF` to the piece of metadata (schema based) to be deleted |
| `mettadatans` | Namespace of the metadata fragment to be removed |
| `mettadataname` | Local name of the metadata fragment to be removed |
| `delete_option` | Only applicable for schema-based metadata, this can be one of the following:  - `DELETE_RES_METADATA_CASCADE` - deletes the corresponding row in the metadata table - `DELETE_RES_METADATA_NOCASCADE` - does not delete the row in the metadata table |

---

### DELETESCHEMALOCMAPPING Procedure

This procedure deletes the schema location mapping for a specified schema URL from the XDB configuration.

Syntax

```
DBMS_XDB.DELETESCHEMALOCMAPPING(
     schemaURL    IN   VARCHAR2);
```

Parameters

Table 164-24 DELETESCHEMALOCMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schemaURL` | Schema URL |

---

### DELETESERVLET Procedure

This procedure deletes a servlet from the XDB configuration.

Syntax

```
DBMS_XDB.DELETESERVLET(
     name        IN   VARCHAR2);
```

Parameters

Table 164-25 DELETESERVLET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |

---

### DELETESERVLETMAPPING Procedure

This procedure deletes the servlet mapping for a specified servlet name from the XDB configuration.

Syntax

```
DBMS_XDB.DELETESERVLETMAPPING(
     name      IN   VARCHAR2);
```

Parameters

Table 164-26 DELETESERVLETMAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Servlet name |

---

### DELETESERVLETSECROLE Procedure

This procedure deletes the specified role from a servlet in the XDB configuration.

Syntax

```
DBMS_XDB.DELETESERVLETSECROLE(
     servname    IN   VARCHAR2,     rolename    IN   VARCHAR2);
```

Parameters

Table 164-27 DELETESERVLETSECROLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `servname` | Servlet name |
| `rolename` | Name of the role to be deleted |

---

### DELETEXMLEXTENSION Procedure

This procedure deletes the specified XML extension from the XDB configuration.

Syntax

```
DBMS_XDB.DELETEXMLEXTENSION(
     extension    IN   VARCHAR2);
```

Parameters

Table 164-28 DELETEXMLEXTENSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `extension` | XML extension to be deleted |

---

### EXISTSRESOURCE Function

This function indicates if a resource is in the hierarchy. Matches resource by a string that represents its absolute path.

Syntax

```
DBMS_XDB.EXISTSRESOURCE(
   abspath    IN    VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-29 EXISTSRESOURCE Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Path name of the resource whose ACL document is required |

Return Values

`TRUE` if the resource is found.

---

### GETACLDOCUMENT Function

This function retrieves ACL document that protects resource given its path name.

Syntax

```
DBMS_XDB.GETACLDOCUMENT(
   abspath  IN  VARCHAR2)
  RETURN sys.xmltype;
```

Parameters

Table 164-30 GETACLDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Path name of the resource whose ACL document is required |

Return Values

The `XMLType` for ACL document.

---

### GETCHILDRESPATHS Function

This function returns a cursor over the absolute paths of all the child resources.

Syntax

```
DBMS_XDB.GETCHILDRESPATHS(
     abspath    IN     VARCHAR2);
  RETURN SYS_REFCURSOR;
```

Parameters

Table 164-31 GETCHILDRESPATHS Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |

Return Values

A cursor over the absolute paths of all the child resources.

---

### GETCONTENTBLOB Function

This function retrieves the contents of a resource returned as a `BLOB`.

Syntax

```
DBMS_XDB.GETCONTENTBLOB(
     abspath    IN     VARCHAR2, 
     csid       OUT    PLS_INTEGER,
     locksrc    IN     BOOLEAN := FALSE) 
  RETURN BLOB;
```

Parameters

Table 164-32 GETCONTENTBLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |
| `csid` | If `TRUE`, lock and return the source LOB. If `FALSE`, return a temp LOB copy. |
| locksrc | Contents of the resource as a BLOB |

Return Values

The contents of the resource as a BLOB.

---

### GETCONTENTCLOB Function

This function gets the contents of a resource returned as a `CLOB`.

Syntax

```
DBMS_XDB.GETCONTENTCLOB(
     abspath    IN     VARCHAR2,
  RETURN CLOB;
```

Parameters

Table 164-33 GETCONTENTCLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |

Return Values

The contents of the resource as a CLOB.

---

### GETCONTENTVARCHAR2 Function

This function gets the contents of a resource returned as a string.

Syntax

```
DBMS_XDB.GETCONTENTVARCHAR2(
     abspath    IN     VARCHAR2,
  RETURN BLOB;
```

Parameters

Table 164-34 GETCONTENTVARCHAR2 Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |

Return Values

The contents of the resource as a string.

---

### GETCONTENTXMLREF Function

This function retrieves the contents of a resource returned as a a `REF` to an `XMLTYPE`.

Syntax

```
DBMS_XDB.GETCONTENTXMLREF(
     abspath    IN     VARCHAR2,
  RETURN SYS.XMLTYPE;
```

Parameters

Table 164-35 GETCONTENTXMLREF Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |

Return Values

The contents of the resource as a `REF` to an `XMLTYPE`.

---

### GETCONTENTXMLTYPE Function

This function retrieves the contents of a resource returned as an `XMLTYPE`.

Syntax

```
DBMS_XDB.GETCONTENTXMLTYPE(
     abspath    IN     VARCHAR2,
  RETURN SYS.XMLTYPE;
```

Parameters

Table 164-36 GETCONTENTXMLTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |

Return Values

The contents of the resource as an XMLTYPE.

---

### GETFTPPORT Function

This procedure gets the value of the current FTP port.

Syntax

```
DBMS_XDB.GETFTPPORT
 RETURN NUMBER;
```

---

### GETHTTPPORT Function

This procedure gets the value of the current HTTP port.

Syntax

```
DBMS_XDB.GETHTTPPORT
 RETURN NUMBER;
```

---

### GETLISTENERENDPOINT Procedure

This procedure retrieves the parameters of a listener end point corresponding to the XML DB HTTP server. The parameters of both HTTP and HTTP2 end points can be retrieved by invoking this procedure.

Syntax

```
DBMS_XDB.GETLISTENERENDPOINT (
   endpoint  IN   NUMBER, 
   host      OUT  VARCHAR2,    port      OUT  NUMBER, 
   protocol  OUT  NUMBER);
```

Parameters

Table 164-37 GETLISTENERENDPOINT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `endpoint` | End point to be retrieved. Its value can be `XDB_ENDPOINT_HTTP` or `XDB_ENDPOINT_HTTP2`. |
| `host` | Interface on which the listener end point listens |
| `port` | Port on which the listener end point listens |
| `protocol` | Transport protocol accepted by the listener end point |

---

### GETLOCKTOKEN Procedure

Given a path to a resource, this procedure returns that resource's lock token for the current user.

Syntax

```
DBMS_XDB.GETLOCKTOKEN(
   path         IN      VARCHAR2,
   locktoken    OUT     VARCHAR2);
```

Parameters

Table 164-38 GETLOCKTOKEN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path name to the resource |
| `locktoken` | Logged-in user's lock token for the resource |

Usage Notes

The user must have `READPROPERTIES` privilege on the resource.

---

### GETPRIVILEGES Function

This function gets all privileges granted to the current user on a specified resource.

Syntax

```
DBMS_XDB.GETPRIVILEGES(
   res_path    IN     VARCHAR2)
 RETURN sys.xmltype;
```

Parameters

Table 164-39 GETPRIVILEGES Function Parameters

| Parameter | Description |
| --- | --- |
| `res_path` | Absolute path in the hierarchy of the resource |

Return Values

An `XMLType` instance of `<privilege>` element, which contains the list of all leaf privileges granted on this resource to the current user.

---

### GETRESOID Function

Returns the object ID of the resource from its absolute path.

Syntax

```
DBMS_XDB.GETRESOID(
   abspath IN VARCHAR2)
RETURN RAW;
```

Parameters

Table 164-40 GETRESOID Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath_path` | Absolute path of the resource |

Return Values

`NULL` if the resource is not present.

---

### GETXDB\_TABLESPACE Function

This function returns the current tablespace of the XDB (user).

Syntax

```
DBMS_XDB.GETXDB_TABLESPACE
 RETURN VARCHAR2;
```

---

### HASBLOBCONTENT Function

This function returns `TRUE` if the resource has BLOB content.

Syntax

```
DBMS_XDB.DBMS_XDB.HASBLOBCONTENT 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-41 HASBLOBCONTENT Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath_path` | Absolute path of the resource |

Return Values

`TRUE` if the resource has BOB content.

---

### HASCHARCONTENT Function

This function returns `TRUE` if the resource has character content.

Syntax

```
DBMS_XDB.DBMS_XDB.HASCHARCONTENT 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-42 HASCHARCONTENT Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath_path` | Absolute path of the resource |

Return Values

`TRUE` if the resource has character content.

---

### HASXMLCONTENT Function

This function returns `TRUE` if the resource has XML content.

Syntax

```
DBMS_XDB.DBMS_XDB.HASXMLCONTENT 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-43 HASXMLCONTENT Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath_path` | Absolute path of the resource |

Return Values

`TRUE` if the resource has XML content.

---

### HASXMLREFERENCE Function

This function returns `TRUE` if the resource has a `REF` to XML content.

Syntax

```
DBMS_XDB.DBMS_XDB.HASXMLREFERENCE 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-44 HASXMLREFERENCE Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath_path` | Absolute path of the resource |

Return Values

`TRUE` resource has a `REF` to XML content.

---

### ISFOLDER Function

This function returns `TRUE` if the resource is a folder or container.

Syntax

```
DBMS_XDB.DBMS_XDB.ISFOLDER 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-45 DBMS\_XDB.ISFOLDER Function Parameters

| Parameter | Description |
| --- | --- |
| `abspath_path` | Absolute path of the resource |

Return Values

`TRUE` if the resource is a folder or container.

---

### LINK Procedures

This procedure creates from a specified folder to a specified resource.

Syntax

```
DBMS_XDB.LINK(
   srcpath      IN   VARCHAR2,
   linkfolder   IN   VARCHAR2,
   linkname     IN   VARCHAR2);
```
```
DBMS_XDB.LINK(
   srcpath      IN   VARCHAR2,
   linkfolder   IN   VARCHAR2,
   linkname     IN   VARCHAR2,
   linktype     IN   PLS_INTEGER := DBMS_XDB.LINK_TYPE_HARD);
```

Parameters

Table 164-46 LINK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `srcpath` | Path name of the resource to which a link is created |
| `linkfolder` | Folder in which the new link is placed |
| `linkname` | Name of the new link |
| `linktype` | Type of link to be created:  - `DBMS_XDB`.`LINK_TYPE_HARD` (default) - `DBMS_XDB`.`LINK_TYPE_WEAK` - `DBMS_XDB`.`LINK_TYPE_SYMBOLIC` |

---

### LOCKRESOURCE Function

Given a path to a resource, this function gets a WebDAV-style lock on that resource.

Syntax

```
DBMS_XDB.LOCKRESOURCE(
   path      IN  VARCHAR2,
   depthzero IN  BOOLEAN,
   shared    IN  boolean)
RETURN BOOLEAN;
```

Parameters

Table 164-47 LOCKRESOURCE Function Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path name of the resource to lock. |
| `depthzero` | Currently not supported |
| `shared` | Passing `TRUE` obtains a shared write lock |

Return Values

`TRUE` if successful.

Usage Notes

The user must have `UPDATE` privileges on the resource.

---

### MOVEXDB\_TABLESPACE Procedure

Note:

This procedure is deprecated in Release 11g. This functionality is replaced by a subprogram of the same name in the [DBMS\_XDB\_ADMIN](d_xdb_admin.md) package - the [MOVEXDB\_TABLESPACE Procedure](d_xdb_admin.md).

This procedure moves the XDB (user) to the specified tablespace.

Syntax

```
DBMS_XDB.MOVEXDB_TABLESPACE(
   new_tablespace   IN  VARCHAR2);
```

Parameters

Table 164-48 MOVEXDB\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_tablespace` | Name of the tablespace to where the XDB is moved |

Usage Notes

- This operation waits for all concurrent XDB sessions to exit.
- If `MOVEXDB_TABLESPACE` fails, the user should restart the database before issuing any further command. Failure to do so willproduce indeterminable results.

---

### PROCESSLINKS Procedure

This procedure processes document links in the specified resource.

Syntax

```
DBMS_XDB.PURGERESOURCEMETADATA( 
 abspath  IN  VARCHAR2,
 recurse  IN  BOOLEAN := FALSE);
```

Parameters

Table 164-49 PROCESSLINKS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource. If the path is a folder, use the `recurse` flag. |
| `recurse` | Used only if `abspath` specifies a folder. If `TRUE`, process links of all resources in the folder hierarchy rooted at the specified resource. If `FALSE`, process links of all documents in this folder only. |

---

### PURGERESOURCEMETADATA Procedure

This procedure deletes all user metadata from a resource. Schema-based metadata is removed in cascade mode, rows being deleted from the corresponding metadata tables.

Syntax

```
DBMS_XDB.PURGERESOURCEMETADATA(  
 abspath  IN  VARCHAR2);
```

Parameters

Table 164-50 PURGERESOURCEMETADATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |

---

### REBUILDHIERARCHICALINDEX Procedure

Note:

This procedure is deprecated in Release 11g. This functionality is replaced by a subprogram of the same name in the [DBMS\_XDB\_ADMIN](d_xdb_admin.md) package - the [REBUILDHIERARCHICALINDEX Procedure](d_xdb_admin.md).

This procedure rebuilds the hierarchical index after import or export operations. This is necessary because data cannot be exported from index tables.

Syntax

```
DBMS_XDB.REBUILDHIERARCHICALINDEX;
```

---

### RENAMERESOURCE Procedure

This procedure renames the XDB resource.

Syntax

```
DBMS_XDB.RENAMERESOURCE(
   srcpath    IN  VARCHAR2,
   destfolder IN  CARCHAR2,
   newname    IN  VARCHAR2);
```

Parameters

Table 164-51 RENAMERESOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `srcpath` | Absolute path in the Hierarchy for the source resource destination folder |
| `destfolder` | Absolute path in the Hierarchy for the destination folder |
| `newname` | Name of the child in the destination folder |

---

### SETACL Procedure

This procedure sets the ACL on a specified resource to be the ACL specified by path.

Syntax

```
DBMS_XDB.SETACL(
   res_path   IN  VARCHAR2,
   acl_path   IN  VARCHAR2);
```

Parameters

Table 164-52 SETACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res_path` | Absolute path in the Hierarchy for resource |
| `acl_path` | Absolute path in the Hierarchy for ACL |

Usage Notes

The user must have `<write-acl>` privileges on the resource.

---

### SETCONTENT Procedures

This procedure replaces the contents of a resource with a specified datatype.

Syntax

Replaces the contents of the a resource with a specified CLOB:

```
DBMS_XDB.SETCONTENT(
     abspath    IN   VARCHAR2,
     data       IN   CLOB);
```

Replaces the contents of a resource with a specified BLOB:

```
DBMS_XDB.SETCONTENT(
     abspath    IN   VARCHAR2,
     data       IN   BLOB,
     csid    IN PLS_INTEGER);
```

Replaces the contents of a resource with a specified `XMLTYPE`:

```
DBMS_XDB.SETCONTENT(
     abspath    IN   VARCHAR2,
     data       IN   SYS.XMLTYPE);
```

Replaces the contents of a resource with a specified string:

```
DBMS_XDB.SETCONTENT(
     abspath    IN   VARCHAR2,
     data       IN   VARCHAR2);
```

Replaces the contents of a resource with a specified `REF` to an `XMLTYPE`

```
DBMS_XDB.SETCONTENT(
     abspath    IN   VARCHAR2,
     data       IN   CLOB,
     sticky     IN   BOOLEAN := TRUE);
```

Replaces the contents of a resource with a specified BFILE:

```
DBMS_XDB.SETCONTENT(
     abspath    IN   VARCHAR2,
     data       IN   CLOB,
     csid       IN   PLS_INTEGER);
```

Parameters

Table 164-53 SETCONTENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path in the Hierarchy for resource |
| `data` | Input varying with overload:  - CLOB data - BLOB data - `XMLTYPE` data - string data - `REF` to `XMLTYPE` data - a BFILE |
| `csid` | Character set id of the BLOB or BFILE |
| `sticky` | Whether or not the `REF` is sticky |

---

### SETFTPPORT Procedure

This procedure sets the FTP port to a new value.

Syntax

```
DBMS_XDB.SETFTPPORT(
   new_port  IN  NUMBER);
```

Parameters

Table 164-54 SETFTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the FTP port is set |

---

### SETHTTPPORT Procedure

This procedure sets the HTTP port to a new value.

Syntax

```
DBMS_XDB.SETHTTPPORT(
   new_port  IN  NUMBER);
```

Parameters

Table 164-55 SETHTTPPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_port` | Value to which the HTTP port is set |

---

### SETLISTENERENDPOINT Procedure

This procedure sets the parameters of a listener end point corresponding to the XML DB HTTP server. Both HTTP and HTTP2 end points can be set by invoking this procedure.

Syntax

```
DBMS_XDB.SETLISTENERENDPOINT (
   endpoint  IN  NUMBER, 
   host      IN  VARCHAR2,    port      IN  NUMBER, 
   protocol  IN  NUMBER);
```

Parameters

Table 164-56 SETLISTENERENDPOINT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `endpoint` | End point to be set. Its value can be `XDB_ENDPOINT_HTTP` or `XDB_ENDPOINT_HTTP2`. |
| `host` | Interface on which the listener end point is to listen. Its value can be ' `LOCALHOST`,' `NULL`, or a hostname. If its value is ' `LOCALHOST` ' the listener end point is permitted to only listen on the localhost interface. If its value is `NULL` or hostname, the listener end point is permitted to listen on both localhost and non-localhost interfaces. |
| `port` | Port on which the listener end point is to listen |
| `protocol` | Transport protocol that the listener end point is to accept. Its value can be `XDB_PROTOCOL_TCP` or `XDB_PROTOCOL_TCPS` |

---

### SETLISTENERLOCALACCESS Procedure

This procedure restricts all listener end points of the XML DB HTTP server to listen either only on the localhost interface (when `l_access` is set to `TRUE`) or to listen on both localhost and non-localhost interfaces (when `l_access` is set to `FALSE`).

Syntax

```
DBMS_XDB.SETLISTENERLOCALACCESS (
   l_access   BOOLEAN);
```

Parameters

Table 164-57 SETLISTENERLOCALACCESS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `l_access`. | `TRUE` or `FALSE`. |

---

### SPLITPATH Procedure

This procedure splits the path into a parentpath and childpath.

Syntax

```
DBMS_XDB.SPLITPATH(
      abspath     IN  VARCHAR2,
      parentpath  OUT VARCHAR2,
     childpath    OUT VARCHAR2);
```

Parameters

Table 164-58 SPLITPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path to be split |
| `parentpath` | Parentpath |
| `childpath` | Childpath |

---

### TOUCHRESOURCE Procedure

This procedure changes the modification time of the resource to the current time.

Syntax

```
DBMS_XDB.DBMS_XDB.TOUCHRESOURCE 
     abspath    IN     VARCHAR2);
```

Parameters

Table 164-59 DBMS\_XDB.TOUCHRESOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath_path` | Absolute path of the resource |

---

### UPDATERESOURCEMETADATA Procedures

This procedure updates metadata for a resource. The procedure takes in a resource identified by absolute path and the metadata in it to replace identified by its `REF`. It replaces that piece of metadata with user-defined metadata which is either in the form of a `REF` to `XMLTYPE` or an `XMLTYPE`.

Syntax

Can be used to update schema-based metadata only. The new metadata must be schema-based:

```
DBMS_XDB.UPDATERESOURCEMETADATA(
   abspath  IN VARCHAR2,
   oldmetadata    IN   REF SYS.XMLTYPE,
   newmetadata    IN   REF SYS.XMLTYPE)
```

Can be used to update schema-based metadata only. The new metadata must be schema-based or nonschema-based:

```
DBMS_XDB.UPDATERESOURCEMETADATA(
   abspath        IN   VARCHAR2,
   oldmetadata    IN   REF SYS.XMLTYPE,
   newmetadata    IN   XMLTYPE);
```

Can be used for both schema-based and nonschema-based metadata:

```
DBMS_XDB.UPDATERESOURCEMETADATA(
   abspath        IN   VARCHAR2,
   oldns          IN   VARCHAR2,
   oldname IN VARCHAR,
   newmetadata IN XMLTYPE);
```

Can be used for both schema-based or nonschema-based metadata. New metadata must be schema-based:

```
DBMS_XDB.UPDATERESOURCEMETADATA(
   abspath       IN   VARCHAR2,
   oldns         IN   VARCHAR2,
   oldname       IN   VARCHAR,
   newmetadata   IN   REF SYS.XMLTYPE);
```

Parameters

Table 164-60 UPDATERESOURCEMETADATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `abspath` | Absolute path of the resource |
| `oldmetadata` | `REF` to the old of metadata |
| `newmetadata` | `REF` to the new, replacement metadata (can be either schema-based or nonschema-based depending on the overload) |
| `oldns` | Namespace identifying old metadata |
| `oldname` | Local name identifying old metadata |

Usage Notes

In the case of `REF`, it stores the `REF` in the resource and the metadata is stored in a separate table. Uniqueness of `REFs` is enforced. In the case where the `XMLTYPE` is passed in, data is parsed to determine if it is schema-based or not and is stored accordingly.

---

### UNLOCKRESOURCE Function

This function unlocks the resource given a lock token and a path to the resource.

Syntax

```
DBMS_XDB.UNLOCKRESOURCE(
   path     IN  VARCHAR2,
   deltoken IN  VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 164-61 UNLOCKRESOURCE Function Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path name to the resource |
| `deltoken` | Lock token to be removed |

Return Values

`TRUE` if operation successful.

Usage Notes

The user must have `UPDATE` privileges on the resource.