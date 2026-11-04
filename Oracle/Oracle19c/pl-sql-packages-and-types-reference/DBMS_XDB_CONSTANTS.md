---
title: DBMS_XDB_CONSTANTS
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_XDB_CONSTANTS.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_XDB_CONSTANTS` package provides an interface to commonly used constants. Users should use constants instead of dynamic strings to avoid typographical errors.

This chapter contains the following topics:

- Security Model
- Summary of DBMS\_XDB\_CONSTANTS Subprograms

### DBMS\_XDB\_CONSTANTS Security Model

Owned by `XDB`, the `DBMS_XDB_CONSTANTS` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### Summary of DBMS\_XDB\_CONSTANTS Subprograms

This table lists the `DBMS_XDB_CONSTANTS` subprograms and briefly describes them.

Table 1 DBMS\_XDB\_CONSTANTS Package Subprograms

| Subprograms | Description |
| --- | --- |
| ENCODING\_DEFAULT Function | Returns `'AL32UTF8'` |
| ENCODING\_ISOLATIN1 Function | Returns `'WE8ISO8859P1'` |
| ENCODING\_UTF8 Function | Returns `'AL32UTF8'` |
| ENCODING\_WIN1252 Function | Returns `'WE8MSWIN1252'` |
| NAMESPACE\_ACL Function | Returns `'http://xmlns.oracle.com/xdb/acl.xsd'` |
| NAMESPACE\_METADATA Function | Returns `'http://xmlns.oracle.com/xdbuserMetaData'` |
| NAMESPACE\_ORACLE Function | Returns `'http://xmlns.oracle.com'` |
| NAMESPACE\_ORACLE\_XDB Function | Returns `'http://xmlns.oracle.com/xdb'` |
| NAMESPACE\_RESOURCE Function | Returns `'http://xmlns.oracle.com/xdb/XDBResource.xsd'` |
| NAMESPACE\_RESOURCE\_EVENT Function | Returns `'http://xmlns.oracle.com/resourceEvent'` |
| NAMESPACE\_RESOURCE\_CONFIG Function | Returns `'http://xmlns.oracle.com/XDBResConfig.xsd'` |
| NAMESPACE\_XDBSCHEMA Function | Returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd'` |
| NAMESPACE\_XMLDIFF Function | Returns `'http://xmlns.oracle.com/xdb/xdiff.xsd'` |
| NAMESPACE\_XMLINSTANCE Function | Returns `'http://www.w3.org/2001/XMLSchema-instance'` |
| NAMESPACE\_XMLSCHEMA Function | Returns `'http://www.w3.org/2001/XMLSchema'` |
| NSPREFIX\_ACL\_ACL Function | Returns `'xmlns:acl= 'http://xmlns.oracle.com/acs.xsd'` |
| NSPREFIX\_RESCONFIG\_RC Function | Returns `'xmlns:rc="http://xmlns.oracle.com/xdb/XDBResConfig.xsd"'` |
| NSPREFIX\_RESOURCE\_R Function | Returns `'xmlns:r="http://xmlns.oracle.com/XDBResource.xsd'` |
| NSPREFIX\_XDB\_XDB Function | Returns `'http://xmlns.oracle.com/xdb'` |
| NSPREFIX\_XMLINSTANCE\_XSI Function | Returns `'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'` |
| NSPREFIX\_XMLDIFF\_XD Function | Returns `'xmlns:xd="http://xmlns.oracle.com/xdb/xdiff.xsd"'` |
| NSPREFIX\_XMLSCHEMA\_XSD Function | Returns `'xmlns:xsd="http://www.w3.org/2001/XMLSchema"'` |
| SCHEMAURL\_ACL Function | Returns `'http://xmlns.oracle.com/xdb/acl.xsd'` |
| SCHEMAELEM\_RES\_ACL Function | Returns `'http://xmlns.oracle.com/xdb/acl.xsd#acl'` |
| SCHEMAELEM\_RESCONTENT\_BINARY Function | Returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd#binary'` |
| SCHEMAELEM\_RESCONTENT\_TEXT Function | Returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd#text'` |
| SCHEMAURL\_RESOURCE Function | Returns `'http://xmlns.oracle.com/xdb/XDBResource.xsd'` |
| SCHEMAURL\_XDBSCHEMA Function | Returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd'` |
| XDBSCHEMA\_PREFIXES Function | Returns `'xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xdb="http://xmlns.oracle.com/xdb'` |
| XSD\_ATTRIBUTE Function | Returns `'attribute'` |
| XSD\_COMPLEX\_TYPE Function | Returns `'complexType'` |
| XSD\_ELEMENT Function | Returns `'element'` |
| XSD\_GROUP Function | Returns `'group'` |

### ENCODING\_DEFAULT Function

This function returns `'AL32UTF8'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.ENCODING_DEFAULT
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'AL32UTF8'`

### ENCODING\_ISOLATIN1 Function

This function returns `'WE8ISO8859P1'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.ENCODING_ISOLATIN1
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'WE8ISO8859P1'`

### ENCODING\_UTF8 Function

This function returns `'AL32UTF8'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.ENCODING_UTF8
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'AL32UTF8'`

### ENCODING\_WIN1252 Function

This function returns `'WE8MSWIN1252'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.ENCODING_WIN1252
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'WE8MSWIN1252'`

### NAMESPACE\_ACL Function

This function returns `'http://xmlns.oracle.com/xdb/acl.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_ACL
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/acl.xsd'`

### NAMESPACE\_METADATA Function

This function returns `'http://xmlns.oracle.com/xdbuserMetaData'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_METADATA
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdbuserMetaData'`

### NAMESPACE\_ORACLE Function

This function returns `'http://xmlns.oracle.com'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_ORACLE
  RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com'`

### NAMESPACE\_ORACLE\_XDB Function

This function returns `'http://xmlns.oracle.com/xdb'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_ORACLE_XDB
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb'`

### NAMESPACE\_RESOURCE Function

This function returns `'/XDBResource.xsd'`

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_RESOURCE
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/XDBResource.xsd`

### NAMESPACE\_RESOURCE\_EVENT Function

This function returns `'http://xmlns.oracle.com/resourceEvent'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_RESOURCE_EVENT
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/resourceEvent'`

### NAMESPACE\_RESOURCE\_CONFIG Function

This function returns `'http://xmlns.oracle.com/XDBResConfig.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_RESOURCE_CONFIG
  RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/XDBResConfig.xsd'`

### NAMESPACE\_XDBSCHEMA Function

This function returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_XDBSCHEMA
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/XDBSchema.xsd'`

### NAMESPACE\_XMLDIFF Function

This function returns `'http://xmlns.oracle.com/xdb/xdiff.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_XMLDIFF
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/xdiff.xsd'`

### NAMESPACE\_XMLINSTANCE Function

This function returns `'http://www.w3.org/2001/XMLSchema-instance'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NAMESPACE_XMLINSTANCE
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://www.w3.org/2001/XMLSchema-instance'`

### NAMESPACE\_XMLSCHEMA Function

This function returns `'http://www.w3.org/2001/XMLSchema'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS. NAMESPACE_XMLSCHEMA
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://www.w3.org/2001/XMLSchema'`

### NSPREFIX\_ACL\_ACL Function

This function returns `'xmlns:acl= 'http://xmlns.oracle.com/acs.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NSPREFIX_ACL_ACL
  RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'xmlns:acl= 'http://xmlns.oracle.com/acs.xsd'`

### NSPREFIX\_RESCONFIG\_RC Function

This function returns `''xmlns:rc="http://xmlns.oracle.com/xdb/XDBResConfig.xsd"'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NSPREFIX_RESCONFIG_RC
  RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`Returns ''xmlns:rc="http://xmlns.oracle.com/xdb/XDBResConfig.xsd"'`

### NSPREFIX\_RESOURCE\_R Function

This function returns `'xmlns:r="http://xmlns.oracle.com/XDBResource.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NSPREFIX_RESOURCE_R
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'xmlns:r="http://xmlns.oracle.com/XDBResource.xsd'`

### NSPREFIX\_XDB\_XDB Function

This function returns `'http://xmlns.oracle.com/xdb'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NSPREFIX_XDB_XDB
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb'`

### NSPREFIX\_XMLINSTANCE\_XSI Function

This function returns `'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NSPREFIX_XMLINSTANCE_XSI
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` ’

### NSPREFIX\_XMLDIFF\_XD Function

This function returns `'xmlns:xd="http://xmlns.oracle.com/xdb/xdiff.xsd"'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NSPREFIX_XMLDIFF_XD
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'xmlns:xd="http://xmlns.oracle.com/xdb/xdiff.xsd"'`

### NSPREFIX\_XMLSCHEMA\_XSD Function

This function returns `'xmlns:xsd="http://www.w3.org/2001/XMLSchema"'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.NSPREFIX_XMLSCHEMA_XSD
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'xmlns:xsd="http://www.w3.org/2001/XMLSchema"'`

### SCHEMAURL\_ACL Function

This function returns `'http://xmlns.oracle.com/xdb/acl.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.SCHEMAURL_ACL
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/acl.xsd'`

### SCHEMAELEM\_RES\_ACL Function

This function returns `'http://xmlns.oracle.com/xdb/acl.xsd#acl'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.SCHEMAELEM_RES_ACL
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/acl.xsd#acl'`

### SCHEMAELEM\_RESCONTENT\_BINARY Function

This function returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd#binary'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.SCHEMAELEM_RESCONTENT_BINARY
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/XDBSchema.xsd#binary'`

### SCHEMAELEM\_RESCONTENT\_TEXT Function

This function returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd#text'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.SCHEMAELEM_RESCONTENT_TEXT
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/XDBSchema.xsd#text'`

### SCHEMAURL\_RESOURCE Function

This function returns `'http://xmlns.oracle.com/xdb/XDBResource.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.SCHEMAURL_RESOURCE
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/XDBResource.xsd'`

### SCHEMAURL\_XDBSCHEMA Function

This function returns `'http://xmlns.oracle.com/xdb/XDBSchema.xsd'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.SCHEMAURL_XDBSCHEMA
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'http://xmlns.oracle.com/xdb/XDBSchema.xsd'`

### XDBSCHEMA\_PREFIXES Function

This function returns `'xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xdb="http://xmlns.oracle.com/xdb'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.XDBSCHEMA_PREFIXES
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xdb="http://xmlns.oracle.com/xdb'`

### XSD\_ATTRIBUTE Function

This function returns `'attribute'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.XSD_ATTRIBUTE
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'attribute'`

### XSD\_COMPLEX\_TYPE Function

This function returns `'complexType'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS.XSD_COMPLEX_TYPE
  RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'complexType'`

### XSD\_ELEMENT Function

This function returns `'element'`.

**Syntax**

```md
DBMS_XDB_CONSTANTS. XSD_ELEMENT
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'element'`

### XSD\_GROUP Function

This function returns `'group'`

**Syntax**

```md
DBMS_XDB_CONSTANTS.XSD_GROUP
 RETURN VARCHAR2 DETERMINISTIC;
```

**Return Value**

`'group'`