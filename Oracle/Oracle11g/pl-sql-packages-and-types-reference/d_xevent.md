---
title: DBMS_XEVENT
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xevent.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 170 DBMS\_XEVENT

The DBMS\_XEVENTpackage provides event-related types and supporting subprograms.

See Also:

Oracle XML DB Developer's Guide for more information about ["Oracle XML DB Repository Events"](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb_repos_events.htm#ADXDB2580)

This chapter contains the following topics:

- Using DBMS\_XEVENT
- Subprogram Groups
- Summary of DBMS\_XEVENT Subprograms

---

## Using DBMS\_XEVENT

- Security Model
- Constants

---

### Security Model

Owned by `XDB`, the `DBMS_XEVENT` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

### Constants

The `DBMS_XEVENT` package uses the constants shown in Table 170-1:

Table 170-1 DBMS\_XEVENT Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `RENDER_EVENT` | `PLS_INTEGER` | `1` |  |
| `PRE_CREATE_EVENT` | `PLS_INTEGER` | 2 |  |
| `POST_CREATE_EVENT` | `PLS_INTEGER` | `3` |  |
| `PRE_DELETE_EVENT` | `PLS_INTEGER` | 4 |  |
| `POST_DELETE_EVENT` | `PLS_INTEGER` | `5` |  |
| `PRE_UPDATE_EVENT` | `PLS_INTEGER` | 6 |  |
| `POST_UPDATE_EVENT` | `PLS_INTEGER` | `7` |  |
| `PRE_LOCK_EVENT` | `PLS_INTEGER` | 8 |  |
| `POST_LOCK_EVENT` | `PLS_INTEGER` | `9` |  |
| `PRE_UNLOCK_EVENT` | `PLS_INTEGER` | 10 |  |
| `POST_UNLOCK_EVENT` | `PLS_INTEGER` | `11` |  |
| `PRE_LINKIN_EVENT` | `PLS_INTEGER` | 12 |  |
| `POST_LINKIN_EVENT` | `PLS_INTEGER` | 13 |  |
| `PRE_LINKTO_EVENT` | `PLS_INTEGER` | 14 |  |
| `POST_LINKTO_EVENT` | `PLS_INTEGER` | `15` |  |
| `PRE_UNLINKIN_EVENT` | `PLS_INTEGER` | 16 |  |
| `POST_UNLINKIN_EVENT` | `PLS_INTEGER` | `17` |  |
| `PRE_UNLINKFROM_EVENT` | `PLS_INTEGER` | `18` |  |
| `POST_UNLINKFROM_EVENT` | `PLS_INTEGER` | 19 |  |
| `PRE_CHECKIN_EVENT` | `PLS_INTEGER` | `20` |  |
| `POST_CHECKIN_EVENT` | `PLS_INTEGER` | 21 |  |
| `PRE_CHECKOUT_EVENT` | `PLS_INTEGER` | 22 |  |
| `POST_CHECKOUT_EVENT` | `PLS_INTEGER` | 23 |  |
| `PRE_UNCHECKOUT_EVENT` | `PLS_INTEGER` | 24 |  |
| `POST_UNCHECKOUT_EVENT` | `PLS_INTEGER` | 25 |  |
| `PRE_VERSIONCONTROL_EVENT` | `PLS_INTEGER` | 26 |  |
| `POST_VERSIONCONTROL_EVENT` | `PLS_INTEGER` | 27 |  |
| `PRE_OPEN_EVENT` | `PLS_INTEGER` | 28 |  |
| `POST_OPEN_EVENT` | `PLS_INTEGER` | 29 |  |
| `PRE_INCONSISTENT_UPDATE_EVENT` | `PLS_INTEGER` | 30 |  |
| `POST_INCONSISTENT_UPDATE_EVENT` | `PLS_INTEGER` | 21 |  |
| `POST_CHECKIN_EVENT` | `PLS_INTEGER` | 21 |  |

---

## Subprogram Groups

---

### XDBEvent Type Subprograms

This subprogram group provides an interface for use in conjunction with the XDBEvent type.

Table 170-2 XDBEvent Subprograms

| Subprogram | Description |
| --- | --- |
| GETCURRENTUSER Function | Returns the name of the user executing the operation that triggers the event |
| GETEVENT Function | Returns a value identifying the triggering event |
| ISNULL Functions | Returns `TRUE` if input argument is `NULL` |

The Summary of DBMS\_XEVENT Subprograms contains a complete listing of all subprograms in the package.

---

### XDBRepositoryEvent Type Subprograms

This subprogram group provides an interface for use in conjunction with the XDBRepositoryEvent type.

Table 170-3 XDBRepositoryEvent Subprograms

| Subprogram | Description |
| --- | --- |
| GETAPPLICATIONDATA Function | Returns the `<applicationData>` element extracted from the resource configuration that defines the invoking handler |
| GETHANDLERLIST Function | Returns an `XDBHandlerList` object containing the list of handlers that will be executed after the currently executing handler |
| GETINTERFACE Function | Returns the top-level interface used to initiate the operation that triggered the event |
| GETLINK Function | Returns an `XDBLink` object for the target resource |
| GETLOCK Function | Returns the lock object corresponding to the current operation |
| GETOLDRESOURCE Function | Returns the original `XDBResource` object before the operation was executed |
| GETOPENACCESSMODE Function | Returns the access mode for the open operation |
| GETOPENDENYMODE Function | Returns the deny mode for the open operation |
| GETOUTPUTSTREAM Function | Returns the output BLOB in which the handler can write the rendered data |
| GETPARAMETER Function | Returns the value of a request or session-specific parameter |
| GETPARENT Function | Returns the resource object corresponding to a parent folder of the target resource |
| GETPATH Function | Returns the `XDBPath` object representing the path of the resource for which the event was fired |
| GETRESOURCE Function | Returns an `XDBResource` object that provides methods to access and modify the contents and metadata of the target resource |
| GETUPDATEBYTECOUNT Function | If the current operation is a byte-range write, returns the byte count |
| GETUPDATEBYTEOFFSET Function | If the current operation is a byte-range write, function returns the byte offset at which the range begins |
| GETXDBEVENT Function | Converts an `XDBRepositoryEvent` object to an `XDBEvent` type |
| ISNULL Functions | Returns `TRUE` if input argument is `NULL` |
| SETRENDERPATH Procedure | Specifies the path of the resource that contains the rendered contents |
| SETRENDERSTREAM Procedure | sets the `BLOB` from which the rendered contents can be read |

The Summary of DBMS\_XEVENT Subprograms contains a complete listing of all subprograms in the package.

---

### XDBHandlerList Type Subprograms

This subprogram group provides an interface for use in conjunction with the XDBHandlerList type.

Table 170-4 XDBHandlerList Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAR Procedure | Clears the handler list |
| GETFIRST Function | Returns the first handler in the list |
| GETNAME Function | Returns the next handler in the list |
| ISNULL Functions | Returns `TRUE` if input argument is `NULL` |
| REMOVE Procedure | Removes the specified handler from the handler list |

The Summary of DBMS\_XEVENT Subprograms contains a complete listing of all subprograms in the package.

---

### XDBHandler Type Subprograms

This subprogram group provides an interface for use in conjunction with the XDBHandler type.

Table 170-5 XDBHandler Type Subprograms

| Subprogram | Description |
| --- | --- |
| GETLANGUAGE Function | Returns the implementation language of the handler |
| GETSCHEMA Function | Returns the schema of the handler's source |
| GETSOURCE Function | Returns the name of the Java class, PL/SQL package or object type implementing the handler |
| ISNULL Functions | Returns `TRUE` if input argument is `NULL` |

The Summary of DBMS\_XEVENT Subprograms contains a complete listing of all subprograms in the package.

---

### XDBPath Type Subprograms

This subprogram group provides an interface for use in conjunction with the XDBPath type.

Table 170-6 XDBPath Type Subprograms

| Subprogram | Description |
| --- | --- |
| GETNAME Function | Returns the string representation of the path |
| GETPARENTPATH Function | Returns the parent's path |
| ISNULL Functions | Returns `TRUE` if input argument is `NULL` |

The Summary of DBMS\_XEVENT Subprograms contains a complete listing of all subprograms in the package.

---

### XDBLink Type Subprograms

This subprogram group provides an interface for use in conjunction with the XDBLink type.

Table 170-7 XDBLink Type Subprograms

| Subprogram | Description |
| --- | --- |
| GETCHILDOID Function | Returns the OID of the resource to which the link is pointing |
| GETPARENTNAME Function | Returns the link's parent folder's name |
| GETPARENTOID Function | Returns the link's parent folder's OID |
| ISNULL Functions | Returns `TRUE` if input argument is `NULL` |

The Summary of DBMS\_XEVENT Subprograms contains a complete listing of all subprograms in the package.

---

## Summary of DBMS\_XEVENT Subprograms

Table 170-8 DBMS\_XEVENT Package Subprograms

| Subprogram | Description | Group |
| --- | --- | --- |
| CLEAR Procedure | Clears the handler list | XDBHandlerList Type Subprograms |
| GETAPPLICATIONDATA Function | Returns the `<applicationData>` element extracted from the resource configuration that defines the invoking handler | XDBRepositoryEvent Type Subprograms |
| GETCHILDOID Function | Returns the OID of the resource to which the link is pointing | XDBLink Type Subprograms |
| GETCURRENTUSER Function | Returns the name of the user executing the operation that triggers the event | XDBEvent Type Subprograms |
| GETEVENT Function | Returns a value identifying the triggering event | XDBEvent Type Subprograms |
| GETFIRST Function | Returns the first handler in the list | XDBHandlerList Type Subprograms |
| GETHANDLERLIST Function | Returns an `XDBHandlerList` object containing the list of handlers that will be executed after the currently executing handler | XDBRepositoryEvent Type Subprograms |
| GETINTERFACE Function | Returns the top-level interface used to initiate the operation that triggered the event | XDBRepositoryEvent Type Subprograms |
| GETLANGUAGE Function | Returns the implementation language of the handler | XDBHandler Type Subprograms |
| GETLINK Function | Returns an `XDBLink` object for the target resource | XDBRepositoryEvent Type Subprograms |
| GETLOCK Function | Returns the lock object corresponding to the current operation | XDBRepositoryEvent Type Subprograms |
| GETNAME Function | Returns the string representation of the path | XDBPath Type Subprograms |
| GETNAME Function | Returns the next handler in the list | XDBHandlerList Type Subprograms |
| GETOLDRESOURCE Function | Returns the original `XDBResource` object before the operation was executed | XDBRepositoryEvent Type Subprograms |
| GETOPENACCESSMODE Function | Returns the access mode for the open operation | XDBRepositoryEvent Type Subprograms |
| GETOPENDENYMODE Function | Returns the deny mode for the open operation | XDBRepositoryEvent Type Subprograms |
| GETOUTPUTSTREAM Function | Returns the output BLOB in which the handler can write the rendered data | XDBRepositoryEvent Type Subprograms |
| GETPARAMETER Function | Returns the value of a request or session-specific parameter | XDBRepositoryEvent Type Subprograms |
| GETPARENT Function | Returns the resource object corresponding to a parent folder of the target resource | XDBRepositoryEvent Type Subprograms |
| GETPARENTNAME Function | Returns the link's parent folder's name | XDBLink Type Subprograms |
| GETPARENTOID Function | Returns the link's parent folder's OID | XDBLink Type Subprograms |
| GETPARENTNAME Function | Returns the parent's path | XDBPath Type Subprograms |
| GETPATH Function | Returns the `XDBPath` object representing the path of the resource for which the event was fired | XDBRepositoryEvent Type Subprograms |
| GETRESOURCE Function | Returns an `XDBResource` object that provides methods to access and modify the contents and metadata of the target resource | XDBRepositoryEvent Type Subprograms |
| GETSCHEMA Function | Returns the schema of the handler's source | XDBHandler Type Subprograms |
| GETSOURCE Function | Returns the name of the Java class, PL/SQL package or object type implementing the handler | XDBHandler Type Subprograms |
| GETUPDATEBYTECOUNT Function | If the current operation is a byte-range write, returns the byte count | XDBRepositoryEvent Type Subprograms |
| GETUPDATEBYTEOFFSET Function | If the current operation is a byte-range write, function returns the byte offset at which the range begins | XDBRepositoryEvent Type Subprograms |
| GETXDBEVENT Function | Converts an `XDBRepositoryEvent` object to an `XDBEvent` type | XDBRepositoryEvent Type Subprograms |
| ISNULL Functions | Returns `TRUE` if input argument is `NULL` | XDBEvent Type Subprograms  XDBRepositoryEvent Type Subprograms  XDBHandlerList Type Subprograms  XDBHandler Type Subprograms  XDBPath Type Subprograms |
| REMOVE Procedure | Removes the specified handler from the handler list | XDBHandlerList Type Subprograms |
| SETRENDERPATH Procedure | Specifies the path of the resource that contains the rendered contents | XDBRepositoryEvent Type Subprograms |
| SETRENDERSTREAM Procedure | sets the `BLOB` from which the rendered contents can be read | XDBRepositoryEvent Type Subprograms |

---

### CLEAR Procedure

this procedure clears the handler list.

See Also:

XDBHandlerList Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.CLEAR (
    hl       IN OUT   XDBHandlerList);
```

Parameters

Table 170-9 CLEAR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `hl` | Handler list |

---

### GETAPPLICATIONDATA Function

This function returns the `<applicationData>` element extracted from the resource configuration that defines the invoking handler.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETAPPLICATIONDATA (
    ev   IN   XDBRepositoryEvent) 
  RETURN XMLType;
```

Parameters

Table 170-10 GETAPPLICATIONDATA Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETCHILDOID Function

This function returns the OID of the resource to which the link is pointing.

See Also:

XDBLink Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETCHILDOID (
    link   IN   XDBLink) 
  RETURN RAW;
```

Parameters

Table 170-11 GETCHILDOID Function Parameters

| Parameter | Description |
| --- | --- |
| `link` | Link |

---

### GETCURRENTUSER Function

This function returns the name of the user executing the operation that triggers the event.

See Also:

XDBEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETCURRENTUSER (
    ev   IN   XDBEvent) 
  RETURN VARCHAR2;
```

Parameters

Table 170-12 GETCURRENTUSER Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBEvent type |

---

### GETEVENT Function

This function returns the name of the user executing the operation that triggers the event.

See Also:

XDBEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETEVENT (
    ev   IN   XDBEvent) 
  RETURN XDBEventID;
```

Parameters

Table 170-13 GETEVENT Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBEvent type |

---

### GETFIRST Function

This function returns the first handler in the list.

See Also:

XDBHandlerList Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETFIRST (
    hl   IN   XDBHandlerList) 
  RETURN XDBHandler;
```

Parameters

Table 170-14 GETFIRST Function Parameters

| Parameter | Description |
| --- | --- |
| `hl` | Handler list |

---

### GETHANDLERLIST Function

This function returns an `XDBHandlerList` object containing the list of handlers that will be executed after the currently executing handler. The current handler can then filter out some of the subsequent handlers if necessary, subject to security checks. An insufficient privilege exception is raised if the executing user does not have the required access privilege to any of the resource configuration associating with a handler in the list.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETHANDLERLIST (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBHandlerList;
```

Parameters

Table 170-15 GETHANDLERLIST Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETINTERFACE Function

This function returns the top-level interface used to initiate the operation that triggered the event. This could be HTTP, FTP or SQL.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETINTERFACE (
    ev   IN   XDBRepositoryEvent) 
  RETURN VARCHAR2;
```

Parameters

Table 170-16 GETINTERFACE Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETLANGUAGE Function

This function returns the implementation language of the handler.

See Also:

XDBHandler Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETLANGUAGE (
    handler   IN   XDBHandler) 
  RETURN VARCHAR2;
```

Parameters

Table 170-17 GETLANGUAGE Function Parameters

| Parameter | Description |
| --- | --- |
| handler | Handler |

---

### GETLINK Function

This function returns an `XDBLink` object for the target resource. For a link\* or unlink\* event, this will be the link involved in the operation. For other events, an error is returned. Using this object the handler can access link properties, such as, `ParentName`, `ParentOID`, `ChildOID` and `LinkName`.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETLINK (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBLink;
```

Parameters

Table 170-18 GETLINK Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETLINKNAME Function

This function returns the name of the link.

See Also:

XDBLink Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETLINKNAME (
    link   IN   XDBLink) 
  RETURN VARCHAR2;
```

Parameters

Table 170-19 GETLINKNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `link` | Link |

---

### GETLOCK Function

This function returns the lock object corresponding to the current operation.I t is only valid for lock and unlock events.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETLOCK  (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBLock;
```

Parameters

Table 170-20 GETLOCK Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETLANGUAGE Function

This function returns the implementation language of the handler.

See Also:

XDBHandler Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETLANGUAGE (
    handler   IN   XDBHandler) 
  RETURN VARCHAR2;
```

Parameters

Table 170-21 GETLANGUAGE Function Parameters

| Parameter | Description |
| --- | --- |
| handler | Handler |

---

### GETNAME Function

This function returns the string representation of the path.

See Also:

XDBPath Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETNAME (
    path   IN   XDBPath) 
  RETURN VARCHAR2;
```

Parameters

Table 170-22 GETNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path |

---

### GETNEXT Function

This function returns the next handler in the list.

See Also:

XDBHandlerList Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETNEXT (
    hl   IN   XDBHandlerList) 
  RETURN XDBHandler;
```

Parameters

Table 170-23 GETNEXT Function Parameters

| Parameter | Description |
| --- | --- |
| `hl` | Handler list |

---

### GETOLDRESOURCE Function

This function returns the original `XDBResource` object before the operation was executed. This method applies only to update event. For other events, an error is returned. This is a read-only object, and consequently none of the modifier methods will work on this object.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETOLDRESOURCE (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBResource;
```

Parameters

Table 170-24 GETOLDRESOURCE Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETOPENACCESSMODE Function

This function returns the access mode for the open operation.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETOPENACCESSMODE (
    ev   IN   XDBRepositoryEvent) 
  RETURN PLS_INTEGER;
```

Parameters

Table 170-25 GETOPENACCESSMODE Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

Return Values

- `XDBRepositoryEvent`.`OPEN_ACCESS_READ` (value 1)
- `XDBRepositoryEvent`.`OPEN_ACCESS_WRITE` (value 2)
- `XDBRepositoryEvent`.`OPEN_ACCESS_READ_WRITE` (value 3)

---

### GETOPENDENYMODE Function

This function returns the deny mode for the open operation. It is only valid for the open event.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETOPENDENYMODE (
    ev   IN   XDBRepositoryEvent) 
  RETURN PLS_INTEGER;
```

Parameters

Table 170-26 GETOPENDENYMODE Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

Return Values

- `XDBRepositoryEvent`.`OPEN_DENY_NONE` (value 0)
- `XDBRepositoryEvent`.`OPEN_DENY_READ` (value 1)
- `XDBRepositoryEvent`.`OPEN_DENY_READ_WRITE` (value 2)

---

### GETOUTPUTSTREAM Function

This function returns the output BLOB in which the handler can write the rendered data. It is only valid for the render event.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETOUTPUTSTREAM (
    ev   IN   XDBRepositoryEvent) 
  RETURN BLOB;
```

Parameters

Table 170-27 GETOUTPUTSTREAM Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETPARAMETER Function

This function returns the value of a request or session-specific parameter. The definition of the `key` parameter can be found in RFC 2616 (HTTP/1.1). They will be mapped to equivalent SQL session parameters (if any).

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETPARAMETER (
    ev   IN   XDBRepositoryEvent,
    key  IN   VARCHAR2) 
  RETURN VARCHAR2;
```

Parameters

Table 170-28 GETPARAMETER Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |
| key | Supported parameters:  - `ACCEPT` - `ACCEPT-LANGUAGE` - `ACCEPT-CHARSET` - `ACCEPT_ENCODING` |

---

### GETPARENT Function

This function returns the resource object corresponding to a parent folder of the target resource. Note that this could be any folder that contains a link to the target resource. This is a read-only object, and consequently none of the modifier methods will work on this object. For a link\* or unlink\* event, this method returns the link's parent folder.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETPARENT (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBResource;
```

Parameters

Table 170-29 GETPARENT Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETPARENTNAME Function

This function returns the link's parent folder's name.

See Also:

XDBLink Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETPARENTNAME (
    link   IN   XDBLink) 
  RETURN VARCHAR2;
```

Parameters

Table 170-30 GETPARENTNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `link` | Link |

---

### GETPARENTOID Function

This function returns the link's parent folder's OID.

See Also:

XDBLink Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETPARENTOID (
    link   IN   XDBLink) 
  RETURN RAW;
```

Parameters

Table 170-31 GETPARENTOID Function Parameters

| Parameter | Description |
| --- | --- |
| `link` | Link |

---

### GETPARENTPATH Function

This function returns the parent's path. The level indicates the number of levels up the hierarchy. This value must be greater than zero. Level 1 means the immediate parent. If level exceeds the height of the tree then a `NULL` is returned.

See Also:

XDBPath Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETPARENTPATH (
    path   IN   XDBPath,
   level   IN   INTEGER) 
  RETURN XDBPath;
```

Parameters

Table 170-32 GETPARENTPATH Function Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path |
| `level` | Number of levels up the hierarchy |

---

### GETPATH Function

This function returns the `XDBPath` object representing the path of the resource for which the event was fired. From this object, functions are provided to get the different path segments.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETPATH (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBPath;
```

Parameters

Table 170-33 GETPATH Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETRESOURCE Function

This function returns an `XDBResource` object that provides methods to access and modify the contents and metadata of the target resource. This object reflects any changes made by previous handlers to the resource.

The modifier methods will work only in the pre-create and pre-update event handlers. For a link\* or unlink\* event, this method returns the resource that the link is pointing to. For a create event, this method returns the resource that is being created.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETRESOURCE (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBResource;
```

Parameters

Table 170-34 GETRESOURCE Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETSCHEMA Function

This function returns the schema of the handler's source.

See Also:

XDBHandler Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETSCHEMA (
    handler   IN   XDBHandler) 
  RETURN VARCHAR2;
```

Parameters

Table 170-35 GETSCHEMA Function Parameters

| Parameter | Description |
| --- | --- |
| handler | Handler |

---

### GETSOURCE Function

This function returns the name of the Java class, PL/SQL package or object type implementing the handler.

See Also:

XDBHandler Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETSOURCE (
    handler   IN   XDBHandler) 
  RETURN VARCHAR2;
```

Parameters

Table 170-36 GETSOURCE Function Parameters

| Parameter | Description |
| --- | --- |
| handler | Handler |

---

### GETUPDATEBYTECOUNT Function

If the current operation is a byte-range write, the function returns the byte count. It is only valid for the inconsistent-update event.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETUPDATEBYTECOUNT (
    ev   IN   XDBRepositoryEvent) 
  RETURN NUMBER;
```

Parameters

Table 170-37 GETUPDATEBYTECOUNT Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETUPDATEBYTEOFFSET Function

If the current operation is a byte-range write, function returns the byte offset at which the range begins. It is only valid for the inconsistent-update event.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETUPDATEBYTEOFFSET (
    ev   IN   XDBRepositoryEvent) 
  RETURN NUMBER;
```

Parameters

Table 170-38 GETUPDATEBYTEOFFSET Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### GETXDBEVENT Function

This function converts an `XDBRepositoryEvent` object to an `XDBEvent` type.

See Also:

XDBRepositoryEvent Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.GETXDBETEVENT (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBEvent;
```

Parameters

Table 170-39 GETXDBEVENT Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of XDBRepositoryEvent type |

---

### ISNULL Functions

This function returns `TRUE` if input argument is `NULL`.

See Also:

- XDBEvent Type Subprograms for other subprograms in this group
- XDBRepositoryEvent Type Subprograms for other subprograms in this group
- XDBHandlerList Type Subprograms for other subprograms in this group
- XDBHandler Type Subprograms for other subprograms in this group
- XDBPath Type Subprograms for other subprograms in this group
- XDBLink Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.ISNULL (
    ev         IN   XDBEvent) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    ev         IN   XDBRepositoryEvent) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    hl         IN   XDBHandlerList) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    handler    IN   XDBHandler) 
  RETURN BOOLEAN;
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    path       IN   XDBPath) 
  RETURN BOOLEAN;

DBMS_XEVENT.ISNULL (
    link       IN   XDBLink) 
  RETURN BOOLEAN;
```

Parameters

Table 170-40 ISNULL Function Parameters

| Parameter | Description |
| --- | --- |
| `ev` | Event of specified type |
| `hl` | Handler list |
| `handler` | Handler |
| `path` | Path |

---

### REMOVE Procedure

This procedure removes the specified handler from the handler list.

See Also:

XDBHandlerList Type Subprograms for other subprograms in this group

Syntax

```
DBMS_XEVENT.REMOVE (
    hl       IN OUT   XDBHandlerList, 
    handler  IN       XDBHandler);
```

Parameters

Table 170-41 REMOVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `hl` | Handler list |
| `handler` | Handler |

---

### SETRENDERPATH Procedure

This procedure specifies the path of the resource that contains the rendered contents. This should not be called after the stream returned by GETOUTPUTSTREAM Function is written to or after the SETRENDERSTREAM Procedure is called; doing so will result in an error. This is only valid for the render event.

Syntax

```
DBMS_XEVENT.SETRENDERPATH (
    ev     IN   XDBRepositoryEvent, 
    path   IN   VARCHAR2);
```

Parameters

Table 170-42 SETRENDERPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ev` | XDB Repository Event object |
| `path` | Path of the resource containing the rendered contents |

---

### SETRENDERSTREAM Procedure

This procedure sets the `BLOB` from which the rendered contents can be read. This should not be called after the stream returned by GETOUTPUTSTREAM is written to or after SETRENDERPATH is called; doing so will result in an error. This is only valid for the render event.

Syntax

```
DBMS_XEVENT.SETRENDERSTREAM (
    ev    IN   XDBRepositoryEvent, 
    istr  IN   BLOB);
```

Parameters

Table 170-43 SETRENDERSTREAM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ev` | XDBRepositoryEvent object |
| `istr` | Input stream from which to get the rendered contents |