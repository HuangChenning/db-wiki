---
title: DBMS_XDBZ
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xdbz.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 169 DBMS\_XDBZ

The DBMS\_XDBZ package controls the Oracle XML DB repository security, which is based on Access Control Lists (ACLs).

This chapter contains the following topics:

- Using DBMS\_XDBZ
- Summary of DBMS\_XDBZ Subprograms
	See Also:
	[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

---

## Using DBMS\_XDBZ

This section contains topics which relate to using the `DBMS_XDBZ` package.

---

### Security Model

Owned by `XDB`, the `DBMS_XDBZ` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

### Constants

The `DBMS_XDBZ` package uses the constants shown in following tables.

Table 169-1 DBMS\_XDBZ Constants - Name Format

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| NAME\_FORMAT\_SHORT | `PLS_INTEGER` | `1` | DB user name or LDAP nickname |
| NAME\_FORMAT\_DISTINGUISHED | `PLS_INTEGER` | `2` | LDAP distinguished name |

Table 169-2 DBMS\_XDBZ Constants - Enable Option

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| ENABLE\_CONTENTS | `PLS_INTEGER` | `1` | Enables hierarchy for contents and is used by users when calling the ENABLE\_HIERARCHY Procedure |
| `ENABLE_RESMETADATA` | `PLS_INTEGER` | `2` | Enables hierarchy for resource metadata, that is, this table will store schema based custom metadata for resources |

Table 169-3 DBMS\_XDBZ Constants - Enable Option Exercised

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `IS_ENABLED_CONTENTS` | `PLS_INTEGER` | `1` | If hierarchy was enabled for contents, that is, the ENABLE\_HIERARCHY Procedure was called with `hierarchy_type` as `ENABLE_CONTENTS` |
| `IS_ENABLED_RESMETADATA` | `PLS_INTEGER` | `2` | If hierarchy was enabled for resource metadata, that is, the ENABLE\_HIERARCHY Procedure was called with `hierarchy_type` as `ENABLE_RESMETADATA` |

---

## Summary of DBMS\_XDBZ Subprograms

Table 169-4 DBMS\_XDBZ Package Subprograms

| Method | Description |
| --- | --- |
| DISABLE\_HIERARCHY Procedure | Disables repository support for the specified `XMLTYPE` table or view |
| ENABLE\_HIERARCHY Procedure | Enables repository support for the specified `XMLType` table or view |
| GET\_ACLOID Function | Retrieves the ACL Object ID for the specified resource |
| GET\_USERID Function | Retrieves the user ID for the specified user |
| IS\_HIERARCHY\_ENABLED Function | Determines if repository support for the specified `XMLType` table or view is enabled |
| PURGELDAPCACHE Function | Purges the LDAP nickname cache |

---

### DISABLE\_HIERARCHY Procedure

This procedure disables repository support for a particular `XMLType` table or view.

Syntax

```
DBMS_XDBZ.DISABLE_HIERARCHY(
   object_schema IN VARCHAR2,
   object_name   IN VARCHAR2);
```

Parameters

Table 169-5 DISABLE\_HIERARCHY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `object_schema` | The schema name of the `XMLType` table or view |
| `object_name` | The name of the `XMLType` table or view |

---

### ENABLE\_HIERARCHY Procedure

This procedure enables repository support for a particular `XMLType` table or view. This allows the use of a uniform ACL-based security model across all documents in the repository.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb21sec.htm#ADXDB2400) for more information about

Syntax

```
DBMS_XDBZ.ENABLE_HIERARCHY(
   object_schema   IN   VARCHAR2,
   object_name     IN   VARCHAR2,
   hierarchy_type  IN   PLS_INTEGER := DBMS_XDBZ.ENABLE_CONTENTS);
```

Parameters

Table 169-6 ENABLE\_HIERARCHY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `object_schema` | The schema name of the `XMLType` table or view |
| `object_name` | The name of the `XMLType` table or view |
| `hierarchy_type` | How to enable the hierarchy.  - `ENABLE_CONTENTS` - enable hierarchy for contents, that is, this table will store contents of resources in the repository - `ENABLE_RESMETADATA` - enable hierarchy for resource metadata, that is, this table will store schema based custom metadata for resources  If this subprogram is called on a table, another call will have no effect. Note that you cannot enable hierarchy for both contents and resource metadata. |

---

### GET\_ACLOID Function

This function retrieves the ACL Object ID for the specified resource, if the repository path is known.

Syntax

```
DBMS_XDBZ.GET_ACLOID(
   aclpath   IN   VARCHAR2,
   acloid    OUT  RAW)
 RETURN BOOLEAN;
```

Parameters

Table 169-7 GET\_ACLOID Function Parameters

| Parameter | Description |
| --- | --- |
| `aclpath` | ACL resource path for the repository |
| `acloid` | The returned Object ID |

Return Values

Returns `TRUE` if successful.

---

### GET\_USERID Function

This function retrieves the user ID for the specified user name. The local database is searched first, and if found, the `USERID` is returned in 4-byte database format. Otherwise, the LDAP directory is searched, if available, and if found, the `USERID` is returned in 4-byte database format.

Syntax

```
DBMS_XDBZ.GET_USERID(
   username IN  VARCHAR2,
   userid   OUT RAW,
   format   IN  BINARY_INTEGER := NAME_FORMAT_SHORT)
 RETURN BOOLEAN;
```

Parameters

Table 169-8 GET\_USERID Function Parameters

| Parameter | Description |
| --- | --- |
| `username` | Name of the database or LDAP user. |
| `userid` | Return parameter for the matching user id. |
| `format` | Format of the specified user name; valid options are:  - `DBMS_XDBZ.NAME_FORMAT_SHORT` (default) -- DB user name or LDAP nickname - `DBMS_XDBZ.NAME_FORMAT_DISTINGUISHIED` -- LDAP distinguished name. |

Return Values

Returns `TRUE` if successful.

---

### IS\_HIERARCHY\_ENABLED Function

This function determines if repository support for the specified `XMLType` table or view is enabled.

Syntax

```
DBMS_XDBZ.IS_HIERARCHY_ENABLED(
   object_schema   IN  VARCHAR2,
   object_name     IN  VARCHAR2,
   hierarchy_type  IN  PLS_INTEGER := IS_ENABLED_CONTENTS)
 RETURN BOOLEAN;
```

Parameters

Table 169-9 IS\_HIERARCHY\_ENABLED Function Parameters

| Parameter | Description |
| --- | --- |
| `object_schema` | The schema name of the `XMLType` table or view |
| `object_name` | The name of the `XMLType` table or view |
| `hierarchy_type` | The type of hierarchy to check for.  - `IS_ENABLED_CONTENTS` - if hierarchy was enabled for contents, that is, the ENABLE\_HIERARCHY Procedure was called with `hierarchy_type` as `ENABLE_CONTENTS` - `IS_ENABLED_RESMETADATA` - if hierarchy was enabled for resource metadata, that is, the ENABLE\_HIERARCHY Procedure was called with `hierarchy_type` as `ENABLE_RESMETADATA` |

Return Values

Returns `TRUE` if the given XMLTYPE table or view has the XDB Hierarchy enabled with the specified type.

---

### PURGELDAPCACHE Function

This function purges the LDAP nickname cache. Returns `TRUE` if successful.

Syntax

```
DBMS_XDBZ.PURGELDAPCACHE
 RETURN BOOLEAN;
```