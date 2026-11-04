---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XDB_VERSION.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 206 DBMS\_XDB\_VERSION

Oracle XML DB versioning interfaces are found in the `DBMS_XBD_VERSION` package. Functions and procedures of `DBMS_XDB_VERSION` help to create a VCR and manage the versions in the version history.

This chapter contains the following topic:

- Security Model
- Summary of DBMS\_XDB\_VERSION Subprograms

See Also:

[Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB-GUID-02D41CF0-A074-4B25-89E3-EE815E3CB5DA)

### 206.1 DBMS\_XDB\_VERSION Security Model

Owned by `XDB`, the `DBMS_XDB_VERSION` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### 206.2 Summary of DBMS\_XDB\_VERSION Subprograms

This table lists the `DBMS_XDB_VERSION` subprograms and briefly describes them.

Table 206-1 DBMS\_XDB\_VERSION Package Subprograms

| Method | Description |
| --- | --- |
| CHECKIN Function | Checks in a checked-out VCR and returns the resource id of the newly-created version |
| CHECKOUT Procedure | Checks out a VCR before updating or deleting it |
| GETCONTENTSBLOBBYRESID Function | Obtain contents as a `BLOB` |
| GETCONTENTSCLOBBYRESID Function | Obtain contents as a `CLOB` |
| GETCONTENTSXMLBYRESID Function | Obtain contents as an `XMLType` |
| GETPREDECESSORS Function | Retrieves the list of predecessors by path name |
| GETPREDSBYRESID Function | Retrieves the list of predecessors by resource id |
| GETRESOURCEBYRESID Function | Obtains the resource as an `XMLType`, given the resource object ID |
| GETSUCCESSORS Function | Retrieves the list of successors by path name |
| GETSUCCSBYRESID Function | Retrieves the list of successors by resource id |
| MAKEVERSIONED Function | Turns a regular resource whose path name is given into a version-controlled resource |
| UNCHECKOUT Function | Checks in a checked-out resource, returns the resource id of the version before the resource is checked out |

#### 206.2.1 CHECKIN Function

This function checks in a checked-out VCR and returns the resource id of the newly-created version.

Syntax

```
DBMS_XDB_VERSION.CHECKIN(
   pathname VARCHAR2) 
 RETURN DBMS_XDB.resid_type;
```

Parameters

Table 206-2 CHECKIN Function Parameters

| Parameter | Description |
| --- | --- |
| `pathname` | The path name of the checked-out resource. |

Usage Notes

This is not an auto-commit SQL operation. CHECKIN Function doesn't have to take the same path name that was passed to CHECKOUT Procedure operation. However, the CHECKIN Function path name and the CHECKOUT Procedure path name must be of the same resource for the operations to function correctly. If the resource has been renamed, the new name must be used to CHECKIN Function because the old name is either invalid or is currently bound with a different resource. Exception is raised if the path name does not exist. If the path name has been changed, the new path name must be used to CHECKIN Function the resource.

#### 206.2.2 CHECKOUT Procedure

This procedure checks out a VCR before updating or deleting it.

Syntax

```
DBMS_XDB_VERSION.Checkout(
   pathname    VARCHAR2);
```

Parameters

Table 206-3 CHECKOUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pathname` | The path name of the VCR to be checked out. |

Usage Notes

This is not an auto-commit SQL operation. Two users of the same workspace cannot CHECKOUT Procedure the same VCR at the same time. If this happens, one user must rollback. As a result, it is good practice to commit the CHECKOUT Procedure operation before updating a resource and avoid loss of the update if the transaction is rolled back. An exception is raised if the given resource is not a VCR, if the VCR is already checked out, if the resource doesn't exist.

#### 206.2.3 GETCONTENTSBLOBBYRESID Function

This function obtain contents as a `BLOB`.

Syntax

```
DBMS_XDB_VERSION.GETCONTENTSBLOBYRESID(
   resid      DBMS_XDB.resid_type)
 RETURN BLOB;
```

Parameters

Table 206-4 GETCONTENTSBLOBYRESID Function Parameters

| Parameter | Description |
| --- | --- |
| `resid` | The resource id. |

#### 206.2.4 GETCONTENTSCLOBBYRESID Function

This function obtains contents as a `CLOB`.

Syntax

```
DBMS_XDB_VERSION.GETCONTENTSCLOBYRESID(
   resid     DBMS_XDB.resid_type)
 RETURN CLOB;
```

Parameters

Table 206-5 GETCONTENTSCLOBYRESID Function Parameters

| Parameter | Description |
| --- | --- |
| `resid` | The resource id. |

#### 206.2.5 GETCONTENTSXMLBYRESID Function

This function obtains contents as an `XMLType`.

Syntax

```
DBMS_XDB_VERSION.GETCONTENTSXMLBYRESID(
   resid      DBMS_XDB.resid_type)
 RETURN XMLType;
```

Parameters

Table 206-6 GETCONTENTSXMLBYRESID Function Parameters

| Parameter | Description |
| --- | --- |
| `resid` | The resource id. |

Return Values

If the contents are not valid XML, returns `NULL`.

#### 206.2.6 GETPREDECESSORS Function

This function retrieves the list of predecessors by the path name.

Syntax

```
DBMS_XDB_VERSION.GETPREDECESSORS(
   pathname       VARCHAR2) 
 RETURN resid_list_type;
```

Parameters

Table 206-7 GETPREDECESSORS Function Parameters

| Parameter | Description |
| --- | --- |
| `pathname` | The path name of the resource. |

Return Values

An exception is raised if `pathname` is illegal.

#### 206.2.7 GETPREDSBYRESID Function

This function retrieves the list of predecessors by resource id.

Syntax

```
DBMS_XDB_VERSION.GETPREDSBYRESID(
   resid      resid_type) 
 RETURN resid_list_type;
```

Parameters

Table 206-8 GETPREDSBYRESID Function Parameters

| Parameter | Description |
| --- | --- |
| `resid` | The resource id. |

Usage Notes

Getting predecessors by `RESID` is more efficient than by `pathname`.

Exceptions

An exception is raised if the `RESID` is illegal.

#### 206.2.8 GETRESOURCEBYRESID Function

This function obtains the resource as an `XMLType`, given the resource object ID. Because the system does not create a path name for versions, this function is useful for retrieving the resource using its resource id.

Syntax

```
DBMS_XDB_VERSION.GETRESOURCEBYRESID(
   resid      resid_type) 
 RETURN XMLType;
```

Parameters

Table 206-9 GETRESOURCEBYRESID Function Parameters

| Parameter | Description |
| --- | --- |
| `resid` | The resource id. |

#### 206.2.9 GETSUCCESSORS Function

Given a version resource or a VCR, this function retrieves the list of the successors of the resource by the path name.

Syntax

```
DBMS_XDB_VERSION.GETSUCCESSORS( 
   pathname VARCHAR2) 
 RETURN resid_list_type;
```

Parameters

Table 206-10 GETSUCCESSORS Function Parameters

| Parameter | Description |
| --- | --- |
| `pathname` | The path name of the resource. |

Usage Notes

Getting successors by `RESID` is more efficient than by `pathname`.

Exceptions

An exception is raised if the `pathname` is illegal.

#### 206.2.10 GETSUCCSBYRESID Function

This function retrieves the list of the successors of the resource by resource id using version resource or VCR.

Syntax

```
DBMS_XDB_VERSION.GETSUCCSBYRESID(
   resid    resid_type) 
  RETURN resid_list_type;
```

Parameters

Table 206-11 GETSUCCSBYRESID Function Parameters

| Parameter | Description |
| --- | --- |
| `resid` | The resource id. |

Usage Notes

Getting successors by `RESID` is more efficient than by `pathname`.

Exceptions

An exception is raised if the `pathname` is illegal.

#### 206.2.11 MAKEVERSIONED Function

This function turns a regular resource whose path name is given into a version-controlled resource. This new resource is then put under version control. All other path names continue to refer to the original resource.

Syntax

```
DBMS_XDB_VERSION.MAKEVERSIONED(
   pathname   VARCHAR2) 
 RETURN DBMS_XDB.resid_type;
```

Parameters

Table 206-12 MAKEVERSIONED Function Parameters

| Parameter | Description |
| --- | --- |
| `pathname` | The path name of the resource to be put under version control. |

Return Values

This function returns the resource ID of the first version, or root, of the VCR.

Usage Notes

If two or more path names are bound with the same resource, a copy of the resource is created, and the given path name is bound with the newly-created copy.

This is not an auto-commit SQL operation. An exception is raised if the resource doesn't exist.

- This call is legal for VCR, and neither exception nor warning is raised.
- This call is illegal for folder, version history, version resource, and ACL.
- No support for Schema-based resources is provided.

#### 206.2.12 UNCHECKOUT Function

This function checks-in a checked-out resource and returns the resource id of the version before the resource is checked out.

Syntax

```
DBMS_XDB_VERSION.UNCHECKOUT(
   pathname    VARCHAR2) 
 RETURN DBMS_XDB.resid_type;
```

Parameters

Table 206-13 UNCHECKOUT Function Parameters

| Parameter | Description |
| --- | --- |
| `pathname` | The path name of the checked-out resource. |

Usage Notes

This is not an auto-commit SQL operation. The UNCHECKOUT Function does not have to take the same path name that was passed to the operation by the CHECKOUT Procedure. However, the UNCHECKOUT Function path name and the CHECKOUT Procedure path name must be of the same resource for the operations to function correctly. If the resource has been renamed, the new name must be used to UNCHECKOUT Function, because the old name is either invalid or is currently bound with a different resource. If the path name has been changed, the new path name must be used to UNCHECKOUT Function the resource.

Exceptions

An exception is raised if the path name doesn't exist.