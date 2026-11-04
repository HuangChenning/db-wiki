---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_RESCONFIG.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 147 DBMS\_RESCONFIG

The `DBMS_RESCONFIG` package provides an interface to operate on the resource configuration list, and to retrieve listener information for a resource.

This chapter contains the following topics:

- Overview
- Summary of DBMS\_RESCONFIG Subprograms

See Also:

Oracle XML DB Developer's Guide for more information about ["Resource Configuration"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB2050).

### 147.1 DBMS\_RESCONFIG Overview

The `DBMS_RESCONFIG` package contains functions and procedures to manage the resource configuration lists of individual resources and the repository.

### 147.2 Summary of DBMS\_RESCONFIG Subprograms

This table lists and briefly describes the `DBMS_RESCONFIG` package subprograms.

Table 147-1 DBMS\_RESCONFIG Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADDREPOSITORYRESCONFIG Procedure | Inserts the resource configuration specified by absolute path at the given position of the repository's configuration list |
| ADDRESCONFIG Procedure | Inserts the resource configuration specified by the absolute path at the given position in the target resource's configuration list |
| APPENDRESCONFIG Procedure | Appends the resource configuration specified by rcpath to the target resource's configuration list if it is not already included in the list |
| DELETEREPOSITORYRESCONFIG Procedure | Removes the configuration at the given position in the repository's configuration list. |
| DELETERESCONFIG Procedures | Removes the configuration at the given position in the target resource's configuration list. I |
| GETLISTENERS Function | Returns the list of listeners applicable for a given resource |
| GETREPOSITORYRESCONFIG Function | Returns the resource configuration at the specified position of the repository's configuration list |
| GETREPOSITORYRESCONFIGPATHS Function | Returns a list of resource configuration paths defined for the repository |
| GETRESCONFIG Function | Returns the resource configuration at the specified position of the target resource's configuration list |
| GETRESCONFIGPATHS Function | Returns a list of resource configuration paths defined in the target resource's configuration list |
| PATCHREPOSITORYRESCONFIGLIST Procedure | Removes invalid references from the repository resource configuration list, and makes the repository available |

#### 147.2.1 ADDREPOSITORYRESCONFIG Procedure

This procedure inserts the resource configuration specified by absolute path of the resource configuration at the specified position of the repository's configuration list. It shifts the element currently at that position (if any) and any subsequent elements to the right.

Syntax

```
DBMS_RESCONFIG.ADDREPOSITORYRESCONFIG(
   rcpath     IN   VARCHAR2, 
   pos        IN   PLS_INTEGER := NULL);
```

Parameters

Table 147-2 ADDREPOSITORYRESCONFIG Function Parameters

| Parameter | Description |
| --- | --- |
| `rcpath` | Absolute path of the resource configuration to be inserted. An exception is raised if `rcpath` already exists in the target's configuration list. |
| `pos` | Index at which the new configuration is to be inserted. If this parameter is not specified then the new configuration is appended to the end of the list. An exception is raised if the index is out of range (`pos` < 0 or `pos` > the size of the target resource's configuration list). |

Usage Notes

- An error is raised if the document referenced by `rcpath` is not based on `XDBResConfig`.`xsd` schema.
- Users must have `XDBADMIN` role and `READ` privilege on the resource configuration to be inserted; otherwise, an error is returned.

#### 147.2.2 ADDRESCONFIG Procedure

This procedure inserts the resource configuration specified by the absolute path of the resource configuration at the given position in the target resource's configuration list. It shifts the element currently at that position (if any) and any subsequent elements to the right.

Syntax

```
DBMS_RESCONFIG.ADDRESCONFIG(
   respath    IN   VARCHAR2, 
   rcpath     IN   VARCHAR2, 
   pos        IN   PLS_INTEGER := NULL);
```

Parameters

Table 147-3 ADDRESCONFIG Function Parameters

| Parameter | Description |
| --- | --- |
| `respath` | Absolute path of the target resource |
| `rcpath` | Absolute path of the resource configuration to be inserted. An exception is raised if rcpath already exists in the target's configuration list. |
| `pos` | Index at which the new configuration is to be inserted. If this parameter is not specified then the new configuration is appended to the end of the list. An exception is raised if the index is out of range (`pos` < 0 or `pos` > the size of the target resource's configuration list). |

Usage Notes

- An error is raised if the document referenced by `rcpath` is not based on `XDBResConfig`.`xsd` schema.
- Users must have `WRITE` `-CONFIG` privilege on the target resource and read privilege on the resource configuration to be inserted; otherwise, an error is returned.

#### 147.2.3 APPENDRESCONFIG Procedure

This procedure appends the resource configuration specified by rcpath to the target resource's configuration list if it is not already included in the list.

Syntax

```
DBMS_RESCONFIG.ADDRESCONFIG(
   respath       IN   VARCHAR2, 
   rcpath        IN   VARCHAR2, 
   appendOption  IN   PLS_INTEGER);
```

Parameters

Table 147-4 ADDRESCONFIG Function Parameters

| Parameter | Description |
| --- | --- |
| respath | Absolute path of the target resource |
| `rcpath` | Absolute path of the resource configuration to be appended at the end of the target's configuration list. If `rcpath` already exists in the list then nothing is appended. |
| `appendOption` | Either `APPEND_RESOURCE` or `APPEND_RECURSIVE`. If `APPEND_RESOURCE` is specified then only the target resource is affected. If `APPEND_RECURSIVE` is specified then the target resource and all its descendents will be affected. |

Usage Notes

- An error is raised if the document referenced by `rcpath` is not based on `XDBResConfig`.xsd schema.
- Users must have `WRITE` `-CONFIG` privilege on all affected resources and required read privilege on the resource configuration to be inserted; otherwise, an error is returned.

#### 147.2.4 DELETEREPOSITORYRESCONFIG Procedure

This procedure removes the configuration at the given position in the repository's configuration list. It shifts any subsequent elements to the left.

Syntax

```
DBMS_RESCONFIG.DELETEREPOSITORYRESCONFIG(
   pos           IN   PLS_INTEGER);
```

Parameters

Table 147-5 DELETEREPOSITORYRESCONFIG Function Parameters

| Parameter | Description |
| --- | --- |
| `pos` | The index of the configuration to be removed. An exception is raised if the index is out of range (`pos` < 0 or `pos` >= the size of the target resource's configuration list). |

Usage Notes

- Users must have `XDBADMIN` role to execute this.
- This statement is treated as if it is a DDL statement. This means the system will implicitly commit before and after this statement.

#### 147.2.5 DELETERESCONFIG Procedures

This procedure removes the configuration at the given position in the target resource's configuration list. It shifts any subsequent elements to the left. Users can use the overloaded for recursive deletion.

Syntax

```
DBMS_RESCONFIG.DELETERESCONFIG(
   respath       IN   VARCHAR2, 
   pos           IN   PLS_INTEGER);
```
```
DBMS_RESCONFIG.DELETERESCONFIG(
   respath        IN  VARCHAR2,
   rcpath         IN  VARCHAR2, 
   deleteOption   IN  PLS_INTEGER);
```

Parameters

Table 147-6 DELETERESCONFIG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `respath` | Absolute path of the target resource |
| `pos` | The index of the configuration to be removed. An exception is raised if the index is out of range (`pos` < 0 or `pos` >= the size of the target resource's configuration list). |
| `rcpath` | Absolute path of the resource configuration to be deleted if found in list. |
| `deleteOption` | Either `DELETE_RESOURCE` or `DELETE_RECURSIVE`. If `DELETE_RESOURCE` is specified then only the configuration list of the target resource is affected. If `DELETE_RECURSIVE` is specified then the configuration list of the target resource and all its descendents will be affected. |

Usage Notes

Users must have `WRITE-CONFIG` privilege on the target resource to execute this.

#### 147.2.6 GETLISTENERS Function

This function returns the list of listeners applicable for a given resource.

The value returned by this function is an XML document containing the `<event-listeners>` element of the `XDBResconfig`.`xsd` schema. It contains all the listeners applicable to the target resource, including repository-level listeners. From the returned XML document users can use the `EXTRACT` operator to retrieve the listeners defined for a specific event.

Syntax

```
DBMS_RESCONFIG.GETLISTENERS(
   path    IN   VARCHAR2)
 RETURN XMLTYPE;
```

Parameters

Table 147-7 GETLISTENERS Function Parameters

| Parameter | Description |
| --- | --- |
| `path` | Absolute path of the target resource |

Usage Notes

Users must have the required access privilege on all resource configurations referenced by the repository and the target resource; otherwise, an error is returned.

#### 147.2.7 GETREPOSITORYRESCONFIG Function

This function returns the resource configuration at the specified position of the repository's configuration list.

Syntax

```
DBMS_RESCONFIG.GETREPOSITORYRESCONFIG(
   pos    IN   PLS_INTEGER)
 RETURN XMLTYPE;
```

Parameters

Table 147-8 GETREPOSITORYRESCONFIG Function Parameters

| Parameter | Description |
| --- | --- |
| `pos` | Index of element to return. An exception is raised if the index is out of range (`pos` < 0 or `pos` >= the size of the repository's configuration list). |

Usage Notes

Users must have the required read privilege on the requested resource configuration; otherwise, an error is returned.

#### 147.2.8 GETREPOSITORYRESCONFIGPATHS Function

This function returns a list of resource configuration paths defined for the repository.

Syntax

```
DBMS_RESCONFIG.GETREPOSITORYRESCONFIGPATHS
 RETURN XDB$STRING_LIST_T;
```

Usage Notes

Users must be able to access all the referenced resource configurations; otherwise, an error is returned.

#### 147.2.9 GETRESCONFIG Function

This function returns the resource configuration at the specified position of the target resource's configuration list.

Syntax

```
DBMS_RESCONFIG.GETRESCONFIG(
   respath IN VARCHAR2,  
   pos IN PLS_INTEGER)
 RETURN XMLTYPE;
```

Parameters

Table 147-9 GETRESCONFIG Function Parameters

| Parameter | Description |
| --- | --- |
| `respath` | Absolute path of the target resource |
| `pos` | Index of element to return. An exception is raised if the index is out of range (`pos` < 0 or `pos` >= the size of the target resource's configuration list). |

Usage Notes

Users must have the required read privilege on the requested resource configuration; otherwise, an error is returned.

#### 147.2.10 GETRESCONFIGPATHS Function

This function returns a list of resource configuration paths defined in the target resource's configuration list.

Syntax

```
DBMS_RESCONFIG.GETRESCONFIGPATHS(
   respath IN VARCHAR2)  
 RETURN XDB$STRING_LIST_T;
```

Parameters

Table 147-10 GETRESCONFIGPATHS Function Parameters

| Parameter | Description |
| --- | --- |
| `respath` | Absolute path of the target resource |

Usage Notes

Users must be able to access all the referenced resource configurations; otherwise, an error is returned.

#### 147.2.11 PATCHREPOSITORYRESCONFIGLIST Procedure

This procedure removes invalid references from the repository resource configuration list, and makes the repository available.

Under normal circumstances, deletion of a resource configuration resource cannot be performed if it is part of the repository resource configuration list. If, for some reason, the deletion of a resource configuration resource that is part of the repository resource configuration list succeeds, then any repository operation results in a 'dangling reference' error. This procedure removes those invalid references.

This procedure must be run as `SYS`.

Syntax

```
DBMS_RESCONFIG.PATCHREPOSITORYRESCONFIGLIST;
```