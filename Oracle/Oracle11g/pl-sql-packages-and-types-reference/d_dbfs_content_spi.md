---
title: DBMS_DBFS_CONTENT_SPI
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_dbfs_content_spi.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 48 DBMS\_DBFS\_CONTENT\_SPI

The `DBMS_DBFS_CONTENT_SPI` package provides the Application Programming Interface (API) specification for [DBMS\_DBFS\_CONTENT](d_dbfs_content.md) service providers. Application designers can create PL/SQL packages conforming to this API to extend `DBMS_CONTENT` to utilize custom service providers.

See Also:

- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_dbstore.htm#ADLOB0079)

This chapter contains the following topics:

- Using DBMS\_DBFS\_CONTENT\_SPI
- Summary of DBMS\_DBFS\_CONTENT\_SPI Subprograms

---

## Using DBMS\_DBFS\_CONTENT\_SPI

---

### Overview

The `DBMS_DBFS_CONTENT_SPI` package describes an internal contract between the implementation of the [DBMS\_DBFS\_CONTENT](d_dbfs_content.md) interface and individual service providers, and whichever package contains their code.

Since PL/SQL does not allow a compile-time, declarative type-conformation between package signatures, store providers should informally conform to the SPI, which is to say, they should implement the SPI by means of a package that contains all of the methods specified in package `DBMS_DBFS_CONTENT_SPI`, with the same method signatures and semantics.

Obviously, these provider packages can implement other methods and expose other interfaces, however, these interfaces are not to be used by the `DBMS_CONTENT` interface itself.

Since the provider SPI is merely a contract specification, there is no package body for `DBMS_DBFS_CONTENT_SPI`, and it is not possible to actually invoke any methods using this package.

The SPI references various elements (constants, types, exceptions) defined by the `DBMS_CONTENT` interface.

Additionally, there is an almost one-to-one correspondence between the client API exported by the `DBMS_CONTENT` interface and the provider interface that the `DBMS_CONTENT` interface itself expects to work against.

The main distinction in the method naming conventions is that all path name references are always store-qualified. That is, the notion of mount-points and full-absolute path names have been normalized and converted to store-qualified path names by the `DBMS_CONTENT` interface before it invokes any of the provider SPI methods.

Since the interconnection of the `DBMS_DBFS_CONTENT` interface and the provider SPI is a 1-to-many pluggable architecture, and the interface uses dynamic SQL to invoke methods in the provider SPI, this can lead to runtime errors.

---

### Security Model

Implementations of the `DBMS_DBFS_CONTENT_SPI` package should be created as `AUTHID` `CURRENT_USER`.

---

### Operational Notes

- Implementation
- Path Names
- Creation Operations
- Deletion Operations
- Get (Retrieve) and Put (Insert) Operations
- Rename and Move Operations
- Directory Navigation and Search
- Locking Operations
- Access Check Operation

Implementation

Since the interconnection of the [DBMS\_DBFS\_CONTENT](d_dbfs_content.md) interface and the provider SPI is a 1-to-many pluggable architecture, the interface uses dynamic SQL to invoke methods in the provider SPI, this can lead to runtime errors.

There are no explicit `INIT` or `FINI` methods to indicate when the `DBMS_DBFS_CONTENT` interface plugs or unplugs a particular provider SPI. Provider SPIs must be willing to auto-initialize themselves at any SPI entry-point.

All operations performed by a service provider are "stateless" in that they are complete operations unto themselves. If state is necessary to be maintained for some reason, then the state must be maintained in data structures such as auxiliary tables that can be queried as needed.

Path Names

All path names used in the provider SPI are store-qualified in pair form (`store_name`, `pathname`) where the path name is rooted within the store namespace.

Stores and their providers that support contentID-based access (see `FEATURE_CONTENT_ID` in [DBMS\_DBFS\_CONTENT Constants - Store Features](d_dbfs_content.md)) also support a form of addressing that is not based on path names. Content items are identified by an explicit store name, a `NULL` path name, and possibly a contentID specified as a parameter or by way of the `OPT_CONTENT_ID` (see [DBMS\_DBFS\_CONTENT Constants - Optional Properties](d_dbfs_content.md)) property.

Not all operations are supported with contentID-based access, and applications should depend only on the simplest create or delete functionality being available.

Creation Operations

The provider SPI must allow the DBFS content API to create directory, file, link, and reference elements subject to store feature support.

All of the creation subprograms require a valid path name, but note the special exemption for contentID-based access. Creation subprograms can optionally specify properties to be associated with the path name as it is created. It is also possible for clients to returns item properties after the creation completes so that automatically generated properties, such as `STD_CREATION_TIME` (see [DBMS\_DBFS\_CONTENT Constants - Standard Properties](d_dbfs_content.md)) are immediately available to clients. The exact set of properties fetched back is controlled by the various `PROP_XXX` bitmasks in the `prop_flags` parameter.

Links and references require an additional path name to associate with the primary path name.

File path names can optionally specify a `BLOB` value to use to initially populate the underlying file content (the provided `BLOB` may be any valid LOB). On creation, the underlying LOB is returned to the client, provided that `PROP_DATA` is specified in the `prop_flags` parameter.

Non-directory path names require that their parent directory be created first. Directory path names themselves can be recursively created with the path name hierarchy leading up to a directory created in one call.

Attempts to create paths that already exist is an error; the sole exception is path names that are "soft-deleted" (as discussed in the context of Deletion Operations) In these cases, the soft-deleted item is implicitly purged, and the new item creation is attempted.

Stores and their providers that support contentID-based access accept an explicit store name and a `NULL` path to create a new content element. The contentID generated for this element is available by means of the `OPT_CONTENT_ID` property (see [DBMS\_DBFS\_CONTENT Constants - Optional Properties](d_dbfs_content.md)), contentID-based creation being automatically implied by `PROP_OPT` property in the `prop_flags` parameter).

The newly created element may also have an internally generated path name if `FEATURE_LAZY_PATH` property is not supported (see [DBMS\_DBFS\_CONTENT Constants - Store Features](d_dbfs_content.md)) and this path is available by way of the `STD_CANONICAL_PATH` property (see [DBMS\_DBFS\_CONTENT Constants - Standard Properties](d_dbfs_content.md)).

Only file elements are candidates for contentID-based access.

Deletion Operations

The provider SPI must allow the DBFS content API to delete directory, file, link, and reference elements (subject to store feature support).

By default, the deletions are permanent, removing the successfully deleted items on transaction commit, but stores may also support "soft-delete" features. If requested by the client, soft-deleted items are retained by the store, although they are not typically visible in normal listings or searches.

Soft-deleted items can be restored, or explicitly purged.

Directory path names can be recursively deleted, with the path name hierarchy below a directory deleted in one call. Non-recursive deletions can be performed only on empty directories. Recursive soft-deletions apply the soft-delete to all of the items being deleted.

Individual path names, as well as all soft-deleted path names under a directory, can be restored or purged by means of the various restore and purge subprograms.

Providers that support filtering can use the provider filter to identify subsets of items to delete. This makes most sense for bulk operations such as the DELETEDIRECTORY Procedure, PURGEALL Procedure, and RESTOREALL Procedure, but all of the deletion-related operations accept a `filter` argument.

Stores and their providers that support contentID-based access can also allow file items to be deleted by specifying their contentID.

Get (Retrieve) and Put (Insert) Operations

Existing path items can be accessed (for query or for update) and modified using simple get and put subprograms. All path names allow their metadata (properties) to be read and modified. On completion of the call, the client can request specific properties to be fetched by means of the `prop_flags` parameter.

File path names allow their data (content) to be read and modified. On completion of the call, the client can use the `PROP_DATA` bitmasks in the `prop_flags` parameter to request a new `BLOB` locator to continue data access.

Files can also be read or written without using `BLOB` locators by explicitly specifying logical offsets or buffer-amounts and a suitably sized buffer.

Update accesses must specify the `forUpdate` flag. Access to link path names can be implicitly and internally de-referenced by stores (subject to feature support) if the `deref` flag is specified, however, this may have undetermined outcomes since symbolic links are not always resolvable.

The read methods, such as the GETPATH Procedures where `forUpdate` is specified as 0, also accepts a valid `asof` timestamp in the `ctx` parameter that can be used by stores to implement "as of" style flashback queries. Mutating versions of the GETPATH Procedures and the PUTPATH Procedures methods do not support "as of" modes of operation.

The GETPATHNOWAIT Procedure implies that the operation is for an update, and, if implemented (see `FEATURE_NOWAIT` in [DBMS\_DBFS\_CONTENT Constants - Store Features](d_dbfs_content.md)), this allows providers to return an exception (ORA-00054) rather than wait for row locks.

Rename and Move Operations

Path names can be renamed or moved, possibly across directory hierarchies and mount-points, but within the same store.

Non-directory path names previously accessible by way of specifying the `oldPath` parameter are renamed as a single item subsequently accessible by specifying `newPath`, assuming that `newPath` does not already exist.

If `newPath` exists and is not a directory, the action of renaming implicitly deletes the existing item before renaming `oldPath`. If the `newPath` exists and is a directory, `oldPath` is moved into the target directory.

Directory path names previously accessible by way of `oldPath` are renamed by moving the directory and all of its children to `newPath` (if it does not already exist) or as children of `newPath` (if it exists and is a directory).

Stores and their providers that support contentID-based access and lazy path name binding also support the SETPATH Procedure that associates an existing contentID with a new "path".

Directory Navigation and Search

The `DBMS_CONTENT` interface can list or search the contents of directory path names, with the option of doing so recursively into sub-directories, optionally seeing soft-deleted items, optionally using flashback "as of" a provided timestamp, and optionally filtering items in or out within the store based on list or search predicates.

Locking Operations

Clients of the `DBMS_CONTENT` interface can apply user-level locks to any valid path name (subject to store feature support), associate the lock with user-data, and subsequently unlock these path names.

The status of locked items is available using various optional properties (note the previous discussion regarding `opt_lock`).

It is the responsibility of the store (assuming it supports user-defined lock checking) to ensure that lock and unlock operations are performed in a consistent manner.

Access Check Operation

This operation ascertains if a given path name (`store_name`, `path`, `pathtype`) can be manipulated by operation (see the various `DBMS_CONTENT.OP_XXX` opcodes in [DBMS\_DBFS\_CONTENT Constants - Optional Properties](d_dbfs_content.md)) by the user acting on the store utilizing the `principal` parameter. This is a convenience function for the `DBMS_CONTENT` interface; a store that supports access control still internally performs these checks to guarantee security.

---

## Summary of DBMS\_DBFS\_CONTENT\_SPI Subprograms

Table 48-1 DBMS\_DBFS\_CONTENT\_SPI Package Subprograms

| Subprogram | Description |
| --- | --- |
| CHECKACCESS Function | Reports if the user (`principal`) can perform the specified operation on the given path |
| CREATEDIRECTORY Procedure | Creates a directory |
| CREATEFILE Procedure | Creates a file |
| CREATELINK Procedure | Creates a physical link to an already existing file system element |
| CREATEREFERENCE Procedure | Creates a new reference to the source file system element |
| DELETECONTENT Procedure | Deletes the file specified by the given contentID |
| DELETEDIRECTORY Procedure | Deletes a directory |
| DELETEFILE Procedure | Deletes a file |
| GETFEATURES Function | Returns the features of a store |
| GETPATH Procedures | Returns existing path items (such as files and directories) |
| GETPATHBYSTOREID Function | If the underlying GUID is found in the underlying store, returns the store-qualified path name |
| GETPATHNOWAIT Procedure | Implies that the operation is for an update, and, if implemented, allows providers to return an exception (`ORA-00054`) rather than wait for row locks. |
| GETSTOREID Function | Returns the ID of a store |
| GETVERSION Function | Returns the version associated with a store |
| LIST Function | Lists the contents of a directory path name |
| LOCKPATH Procedure | Applies user-level locks to the given valid path name |
| PURGEALL Procedure | Purges all soft-deleted entries matching the path and optional filter criteria |
| PURGEPATH Procedure | Purges any soft-deleted versions of the given path item |
| PUTPATH Procedures | Creates a new path item |
| RENAMEPATH Procedure | Renames or moves a path |
| RESTOREALL Procedure | Restores all soft-deleted path items meeting the path and filter criteria |
| RESTOREPATH Procedure | Restores all soft-deleted path items that match the given path and filter criteria |
| SEARCH Function | Searches for path items matching the given path and filter criteria |
| SETPATH Procedure | Assigns a path name to a path item represented by contentID |
| SPACEUSAGE Procedure | Queries file system space usage statistics |
| UNLOCKPATH Procedure | Unlocks path items that were previously locked with the LOCKPATH Procedure |

---

### CHECKACCESS Function

This function reports if the user (`principal`) can perform the specified operation on the given path. This enables verifying the validity of an operation without attempting to perform the operation. If `CHECKACCESS` returns 0, then the subprogram invoked to implement that operation should fail with an error.

Syntax

```
DBMS_DBFS_CONTENT_SPI.CHECKACCESS (
   store_name     IN     VARCHAR2  DEFAULT NULL,
   path           IN     VARCHAR2,
   pathtype       IN     INTEGER,
   operation      IN     VARCHAR2,
   principal      IN     VARCHAR2)
  RETURN  INTEGER;
```

Parameters

Table 48-2 CHECKACCESS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to check for access |
| `pathtype` | Type of object `path` represents (see [DBMS\_DBFS\_CONTENT Constants - Path Name Types](d_dbfs_content.md)) |
| `operation` | Operation to be checked (see [DBMS\_DBFS\_CONTENT Constants - Optional Properties](d_dbfs_content.md)) |
| `principal` | File system user for whom the access check is made |

Usage Notes

Whether or not the user invokes this function, a store that supports access control internally performs these checks to guarantee security.

---

### CREATEDIRECTORY Procedure

This procedure creates a directory.

Syntax

```
DBMS_DBFS_CONTENT_SPI.CREATEDIRECTORY (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   prop_flags  IN              INTEGER,
   recurse     IN              INTEGER,
   ctx         IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-3 CREATEDIRECTORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to the directory |
| `properties` | One or more properties and their values to be set, returned, or both, depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `prop_flags` | Determines which properties are set, returned, or both. Default is `PROP_STD`. Specify properties to be returned by setting `PROP_SPC` (see [DBMS\_DBFS\_CONTENT Constants - Property Access Flags](d_dbfs_content.md)), and providing an instance of the [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md) with properties whose values are of interest. |
| `recurse` | If 0, do not execute recursively; otherwise, recursively create the directories above the given directory |
| `ctx` | Context with which to create the directory (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### CREATEFILE Procedure

This procedure creates a file.

Syntax

```
DBMS_DBFS_CONTENT_SPI.CREATEFILE (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   content       IN OUT NOCOPY   BLOB,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-4 CREATEFILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to the file |
| `properties` | One or more properties and their values to be set, returned or both depending, or both on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `content` | `BLOB` holding data with which to populate the file (optional) |
| `prop_flags` | Determines which properties are set, returned, or both. Default is `PROP_STD`. Specify properties to be returned by setting `prop_spec`, and providing an instance of the [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md) with properties whose values are of interest. |
| `ctx` | Context with which to create the file (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### CREATELINK Procedure

This procedure creates a physical link to an already existing file system element (such as file or directory). The resulting entry shares the same metadata structures as the value of the `srcPath` parameter, and so is similar to incrementing a reference count on the file system element. This is analogous to a UNIX file system hard link.

Syntax

```
DBMS_DBFS_CONTENT_SPI.CREATELINK (
   store_name    IN              VARCHAR2,
   srcPath       IN              VARCHAR2,
   dstPath       IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-5 CREATELINK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `srcPath` | File system entry with which to link |
| `dstPath` | Path of the new link element to be created |
| `properties` | One or more properties and their values to be set, returned, or both, depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `prop_flags` | Determines which properties are set, returned, or both. Default is `PROP_STD`. Specify properties to be returned by setting `prop_spec`, and providing an instance of the [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md) with properties whose values are of interest. |
| `ctx` | Context with which to create the link (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### CREATEREFERENCE Procedure

This procedure creates a new reference to the source file system element (such as a file, or directory). The resulting reference points to the source element but does not directly share metadata with the source element. This is analogous to a UNIX file system symbolic link.

Syntax

```
DBMS_DBFS_CONTENT_SPI.CREATEREFERENCE (
   srcPath       IN              VARCHAR2,
   dstPath       IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   prop_flags    IN              INTEGER,
   store_name    IN              VARCHAR2,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-6 CREATEREFERENCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `srcPath` | File system entry with which to link |
| `dstPath` | Path of the new link element to be created |
| `properties` | One or more properties and their values to be set, returned, or both, depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `prop_flags` | Determines which properties are set, returned, or both. Default is `PROP_STD`. Specify properties to be returned by setting `prop_spec`, and providing an instance of the [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md) with properties whose values are of interest. |
| `ctx` | Context with which to create the reference (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### DELETECONTENT Procedure

This procedure deletes the file specified by the given contentID.

Syntax

```
DBMS_DBFS_CONTENT_SPI.DELETECONTENT (
   store_name     IN     VARCHAR2,
   contentID      IN     RAW,
   filter         IN     VARCHAR2,
   soft_delete    IN     INTEGER,
   ctx            IN     DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-7 DELETECONTENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `contentID` | Unique identifier for the file to be deleted |
| `filter` | A filter, if any, to be applied |
| `soft_delete` | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete (see "Deletion Operations"). |
| `ctx` | Context with which to delete the file (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### DELETEDIRECTORY Procedure

This procedure deletes a directory. If `recurse` is nonzero, it recursively deletes all elements of the directory. A filter, if supplied, determines which elements of the directory are deleted.

Syntax

```
DBMS_DBFS_CONTENT_SPI.DELETEDIRECTORY (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   filter         IN     VARCHAR2,
   soft_delete    IN     INTEGER,
   recurse        IN     INTEGER,
   ctx            IN     DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-8 DELETEDIRECTORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to the directory |
| `filter` | A filter, if any, to be applied |
| `soft_delete` | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete (see "Deletion Operations"). |
| `recurse` | If 0, do not execute recursively. Otherwise, recursively delete the directories and files below the given directory. |
| `ctx` | Context with which to delete the directory (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### DELETEFILE Procedure

This procedure deletes the specified file.

Syntax

```
DBMS_DBFS_CONTENT_SPI.DELETEFILE (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   filter         IN     VARCHAR2,
   soft_delete    IN     BOOLEAN,
   ctx            IN     DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-9 DELETEFILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to the file |
| `filter` | A filter, if any, to be applied |
| `soft_delete` | If 0, execute a hard (permanent) delete. For any value other than 0, perform a soft delete (see "Deletion Operations"). |
| `ctx` | Context with which to delete the file (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### GETFEATURES Function

This function returns the features of a store.

Syntax

```
DBMS_DBFS_CONTENT_SPI.GETFEATURES (
   store_name          IN      VARCHAR2)
  RETURN  INTEGER;
```

Parameters

Table 48-10 GETFEATURES Function Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |

Return Values

`DBMS_CONTENT.FEATURE_*` features supported by the Service Provider

---

### GETPATH Procedures

This procedure returns existing path items (such as files and directories). This includes both data and metadata (properties).

The client can request (using `prop_flags`) that specific properties be returned. File path names can be read either by specifying a `BLOB` locator using the `prop_data` bitmask in `prop_flags` (see [DBMS\_DBFS\_CONTENT Constants - Property Access Flags](d_dbfs_content.md)) or by passing one or more `RAW` buffers.

When `forUpdate` is 0, this procedure also accepts a valid "as of" timestamp parameter as part of `ctx` that can be used by stores to implement "as of" style flashback queries. Mutating versions of the `GETPATH` Procedures do not support these modes of operation.

Syntax

```
DBMS_DBFS_CONTENT_SPI.GETPATH (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   content     OUT    NOCOPY   BLOB,
   item_type   OUT             INTEGER,
   prop_flags  IN              INTEGER,
   forUpdate   IN              INTEGER,
   deref       IN              INTEGER,
   ctx         IN              DBMS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.GETPATH (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   amount      IN OUT          NUMBER,
   offset      IN              NUMBER,
   buffer      OUT    NOCOPY   RAW,
   prop_flags  IN              INTEGER,
   ctx         IN              DBMS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.GETPATH (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   amount      IN OUT          NUMBER,
   offset      IN              NUMBER,
   buffers     OUT    NOCOPY   DBMS_CONTENT_RAW_T,
   prop_flags  IN              INTEGER,
   ctx         IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-11 GETPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to path items |
| `properties` | One or more properties and their values to be returned depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `content` | `BLOB` holding data which populates the file (optional) |
| `item_type` | Type of the path item specified (see [DBMS\_DBFS\_CONTENT Constants - Path Name Types](d_dbfs_content.md)) |
| `amount` | On input, number of bytes to be read. On output, number of bytes read |
| `offset` | Byte offset from which to begin reading |
| `buffer` | Buffer to which to write |
| `buffers` | Buffers to which to write |
| `prop_flags` | Determines which properties are set, returned, or both. Default is `PROP_STD`. Specify properties to be returned by setting `prop_spec`, and providing an instance of the [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md) with properties whose values are of interest. |
| `forUpdate` | Specifies that a lock should be taken to signify exclusive write access to the path item |
| `deref` | If nonzero, attempts to resolve the given path item to actual data provided it is a reference (symbolic link) |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### GETPATHBYSTOREID Function

If the underlying GUID is found in the underlying store, this function returns the store-qualified path name.

Syntax

```
DBMS_DBFS_CONTENT_SPI.GETPATHBYSTOREID (
   store_name          IN      VARCHAR2,
   guid                IN      INTEGER)
  RETURN VARCHAR2;
```

Parameters

Table 48-12 GETPATHBYSTOREID Function Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `guid` | Unique ID representing the desired path item |

Return Values

Store-qualified path name represented by the GUID

Usage Notes

If the `STD_GUID` is unknown, a `NULL` value is returned. Clients are expected to handle this as appropriate.

---

### GETPATHNOWAIT Procedure

This procedure implies that the operation is for an update, and, if implemented (see `FEATURE_NOWAIT` in [DBMS\_DBFS\_CONTENT Constants - Store Features](d_dbfs_content.md)), allows providers to return an exception (`ORA-00054`) rather than wait for row locks.

Syntax

```
DBMS_DBFS_CONTENT_SPI.GETPATHNOWAIT (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   content     OUT    NOCOPY   BLOB,
   item_type   OUT             INTEGER,
   prop_flags  IN              INTEGER,
   deref       IN              INTEGER,
   ctx         IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-13 GETPATHNOWAIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to path items |
| `properties` | One or more properties and their values to be returned depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `content` | `BLOB` holding data which populates the file (optional) |
| `item_type` | Type of the path item specified (see [DBMS\_DBFS\_CONTENT Constants - Path Name Types](d_dbfs_content.md)) |
| `prop_flags` | Determines which properties are returned. Default is `PROP_STD`. Specify properties to be returned by setting `prop_spec`, and providing an instance of the [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md) with properties whose values are of interest. |
| `deref` | If nonzero, attempts to resolve the given path item to actual data provided it is a reference (symbolic link) |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### GETSTOREID Function

This function returns the ID of a store.

Syntax

```
DBMS_DBFS_CONTENT_SPI.GETSTOREID (
   store_name          IN      VARCHAR2)
  RETURN  NUMBER;
```

Parameters

Table 48-14 GETSTOREID Function Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |

Return Values

ID of the Store

Usage Notes

A store ID identifies a provider-specific store, across registrations and mounts, but independent of changes to the store contents. For this reason, changes to the store table or tables should be reflected in the store ID, but re-initialization of the same store table or tables should preserve the store ID.

---

### GETVERSION Function

This function returns the version associated with a store.

Syntax

```
DBMS_DBFS_CONTENT_SPI.GETVERSION (
   store_name          IN      VARCHAR2)
  RETURN  VARCHAR2;
```

Parameters

Table 48-15 GETVERSION Function Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |

Return Values

A "version" (either specific to a provider package, or to an individual store) based on a standard a.b.c naming convention (for major, minor, and patch components)

---

### LIST Function

This function lists the contents of a directory path name.

The invoker of the subprogram has the option to investigate recursively into sub-directories, to make soft-deleted items visible, to use a flashback "as of" a specified timestamp, and to filter items within the store based on list predicates.

Syntax

```
DBMS_DBFS_CONTENT_SPI.LIST (
   store_name    IN     VARCHAR2,
   path          IN     VARCHAR2,
   filter        IN     VARCHAR2,
   recurse       IN     INTEGER,
   ctx           IN     DBMS_CONTENT_CONTEXT_T)
  RETURN  DBMS_CONTENT_LIST_ITEMS_T PIPELINED;
```

Parameters

Table 48-16 LIST Function Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of respository |
| `path` | Name of path to directories |
| `filter` | A filter, if any, to be applied |
| `recurse` | If 0, do not execute recursively. Otherwise, recursively list the contents of directories and files below the given directory. |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

Return Values

Path items found that match the path, filter and criteria for executing recursively (see [DBMS\_DBFS\_CONTENT\_LIST\_ITEMS\_T Table Type](t_content.md))

Usage Notes

This function returns only list items; the client is expected to explicitly use one of the GETPATH Procedures to access the properties or content associated with an item.

---

### LOCKPATH Procedure

This procedure applies user-level locks to the given valid path name (subject to store feature support), and optionally associates user-data with the lock.

Syntax

```
DBMS_DBFS_CONTENT_SPI.LOCKPATH (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   lock_type      IN     INTEGER,
   lock_data      IN     VARCHAR2,
   ctx            IN     DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-17 LOCKPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Path name of items to be locked |
| `lock_type` | One of the available lock types (see [DBMS\_DBFS\_CONTENT Constants - Lock Types](d_dbfs_content.md)) |
| `lock_data` | Optional user data to be associated with the lock |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

Usage Notes

- It is the responsibility of the store and its providers (assuming it supports user-defined lock checking) to ensure that lock and unlock operations are performed in a consistent manner.
- The status of locked items is available by means of various optional properties (see `OPT_LOCK` \* in [DBMS\_DBFS\_CONTENT Constants - Optional Properties](d_dbfs_content.md)).

---

### PURGEALL Procedure

This procedure purges all soft-deleted entries matching the path and optional filter criteria.

Syntax

```
DBMS_DBFS_CONTENT_SPI.PURGEALL (
   store_name     IN      VARCHAR2,
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   ctx            IN      DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-18 PURGEALL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to file items |
| `filter` | A filter, if any, to be applied based on specified criteria |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### PURGEPATH Procedure

This procedure purges any soft-deleted versions of the given path item.

Syntax

```
DBMS_DBFS_CONTENT_SPI.PURGEPATH (
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   store_name     IN      VARCHAR2,
   ctx            IN      DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-19 PURGEPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to file items |
| `filter` | A filter, if any, to be applied |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### PUTPATH Procedures

This procedure creates a new path item.

Syntax

```
DBMS_DBFS_CONTENT_SPI.PUTPATH (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   content       IN OUT NOCOPY   BLOB,
   item_type     OUT             INTEGER,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.PUTPATH (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   amount        IN              NUMBER,
   offset        IN              NUMBER,
   buffer        IN              RAW,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.PUTPATH (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   written       OUT             NUMBER,
   offset        IN              NUMBER,
   buffers       IN              DBMS_CONTENT_RAW_T,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-20 PUTPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Path name of item to be put |
| `properties` | One or more properties and their values to be set depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `content` | `BLOB` holding data which populates the file (optional) |
| `item_type` | Type of the path item specified (see [DBMS\_DBFS\_CONTENT Constants - Path Name Types](d_dbfs_content.md)) |
| `amount` | Number of bytes to be read |
| `written` | Number of bytes written |
| `offset` | Byte offset from which to begin reading |
| `buffer` | Buffer to which to write |
| `buffers` | Buffers to which to write |
| `prop_flags` | Determines which properties are set. Default is `PROP_STD`. Specify properties to be returned by setting `prop_spec`, and providing an instance of the [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md) with properties whose values are of interest. |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

Usage Notes

- All path names allow their metadata (properties) to be read and modified. On completion of the call, the client can access specific properties using `prop_flags` (see [DBMS\_DBFS\_CONTENT Constants - Property Access Flags](d_dbfs_content.md)).
- On completion of the call, the client can request a new `BLOB` locator that can be used to continue data access using the `prop_data` bitmask in `prop_flags` (see [DBMS\_DBFS\_CONTENT Constants - Property Access Flags](d_dbfs_content.md)).
- Files can also be written without using `BLOB` locators, by explicitly specifying logical offsets or buffer-amounts, and a suitably sized buffer.

---

### RENAMEPATH Procedure

This procedure renames or moves a path. This operation can be performed across directory hierarchies and mount-points as long as it is within the same store.

Note:

See "Rename and Move Operations"

Syntax

```
DBMS_DBFS_CONTENT_SPI.RENAMEPATH (
   store_name    IN              VARCHAR2,
   oldPath       IN              VARCHAR2,
   newPath       IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-21 RENAMEPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store, must be unique |
| `oldPath` | Name of path prior to renaming |
| `newPath` | Name of path after renaming |
| `properties` | One or more properties and their values to be set depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### RESTOREALL Procedure

This procedure restores all soft-deleted path items meeting the path and optional filter criteria.

Syntax

```
DBMS_DBFS_CONTENT_SPI.RESTOREALL (
   store_name     IN      VARCHAR2,
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   ctx            IN      DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-22 RESTOREALL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to path items |
| `filter` | A filter, if any, to be applied |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### RESTOREPATH Procedure

This procedure restores all soft-deleted path items that match the given path and optional filter criteria.

Syntax

```
DBMS_DBFS_CONTENT_SPI.RESTOREPATH (
   store_name     IN      VARCHAR2,
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   ctx            IN      DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-23 RESTOREPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to path items |
| `filter` | A filter, if any, to be applied |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### SEARCH Function

This function searches for path items matching the given path and filter criteria.

Syntax

```
DBMS_DBFS_CONTENT_SPI.SEARCH (
   store_name     IN      VARCHAR2,
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   recurse        IN      INTEGER,
   ctx            IN      DBMS_CONTENT_CONTEXT_T)
 RETURN  DBMS_CONTENT_LIST_ITEMS_T PIPELINED;
```

Parameters

Table 48-24 LIST Function Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to the path items |
| `filter` | A filter, if any, to be applied |
| `recurse` | If 0, do not execute recursively. Otherwise, recursively search the contents of directories and files below the given directory. |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

Return Values

Path items matching the given path and filter criteria (see [DBMS\_DBFS\_CONTENT\_LIST\_ITEMS\_T Table Type](t_content.md))

---

### SETPATH Procedure

This procedure assigns a path name to a path item represented by contentID.

Stores and their providers that support contentID-based access and lazy path name binding also support the `SETPATH Procedure` that associates an existing `contentID` with a new path.

Note:

See "Rename and Move Operations"

Syntax

```
DBMS_DBFS_CONTENT_SPI.SETPATH (
   store_name    IN              VARCHAR2,
   contentID     IN              RAW,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_CONTENT_PROPERTIES_T,
   ctx           IN              DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-25 SETPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of the store |
| `contentID` | Unique identifier for the item to be associated |
| `path` | Name of path to path item |
| `properties` | One or more properties and their values to be set depending on `prop_flags` (see [DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type](t_content.md)) |
| `ctx` | Context with which to access the path items (seE [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |

---

### SPACEUSAGE Procedure

This procedure queries file system space usage statistics. Providers are expected to support this subprogram for their stores and to make a best effort determination of space usage, especially if the store consists of multiple tables, indexes, LOBs, and so on.

Syntax

```
DBMS_DBFS_CONTENT_SPI.SPACEUSAGE (
   store_name    IN        VARCHAR2,
   blksize       OUT       INTEGER,
   tbytes        OUT       INTEGER,
   fbytes        OUT       INTEGER,
   nfile         OUT       INTEGER,
   ndir          OUT       INTEGER,
   nlink         OUT       INTEGER,
   nref          OUT       INTEGER);
```

Parameters

Table 48-26 SPACEUSAGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `blksize` | Natural tablespace blocksize that holds the store. If multiple tablespaces with different blocksizes are used, any valid blocksize is acceptable. |
| `tbytes` | Total size of the store in bytes computed over all segments that comprise the store |
| `fbytes` | Free or unused size of the store in bytes computed over all segments that comprise the store |
| `nfile` | Number of currently available files in the store |
| `ndir` | Number of currently available directories in the store |
| `nlink` | Number of currently available links in the store |
| `nref` | Number of currently available references in the store |

Usage Notes

- A space usage query on the top-level root directory returns a combined summary of the space usage of all available distinct stores under it (if the same store is mounted multiple times, it is still counted only once).
- Since database objects are dynamically expandable, it is not easy to estimate the division between "free" space and "used" space.

---

### UNLOCKPATH Procedure

This procedure unlocks path items that were previously locked with the LOCKPATH Procedure.

Syntax

```
DBMS_DBFS_CONTENT_SPI.UNLOCKPATH (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   ctx            IN     DBMS_CONTENT_CONTEXT_T);
```

Parameters

Table 48-27 UNLOCKPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `store_name` | Name of store |
| `path` | Name of path to the path items |
| `ctx` | Context with which to access the path items (see [DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type](t_content.md)) |