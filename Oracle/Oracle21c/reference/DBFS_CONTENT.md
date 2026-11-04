---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBFS_CONTENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.173 DBFS\_CONTENT

`DBFS_CONTENT` displays all the path items from all available content stores in the system.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STORE` | `VARCHAR2(256)` |  | Name of store |
| `MOUNT` | `VARCHAR2(256)` |  | Location at which instance of store is mounted |
| `PATHNAME` | `VARCHAR2(1024)` |  | Name of path to item |
| `PATHTYPE` | `VARCHAR2(32)` |  | Type of path item (see `DBMS_DBFS_CONTENT` Constants - Path Name Types) |
| `FILEDATA` | `BLOB` |  | BLOB locator that can be used to access data in the path item |
| `STD_ACCESS_TIME` | `TIMESTAMP(6)` |  | Time of last access of a path name's contents |
| `STD_ACL` | `VARCHAR2(1024)` |  | Access Control List (in standard ACL syntax) |
| `STD_CHANGE_TIME` | `TIMESTAMP(6)` |  | Time of last change to the path name |
| `STD_CHILDREN` | `NUMBER` |  | Number of child directories/folders a directory/folder path has (this property should be available in providers that support the `FEATURE_FOLDERS` feature) |
| `STD_CONTENT_TYPE` | `VARCHAR2(1024)` |  | One or more client-supplied mime-types (in standard RFC syntax) describing the path name which is typically of `TYPE_FILE`. The content type is not necessarily interpreted by the store. |
| `STD_CREATION_TIME` | `TIMESTAMP(6)` |  | Time at which the item was created. Once set, this value remains the same for the lifetime of the path name. |
| `STD_DELETED` | `NUMBER` |  | Set to a nonzero number if the path name has been soft-deleted but not yet purged (see `DBMS_DBFS_CONTENT` Constants - Store Features) |
| `STD_GUID` | `NUMBER` |  | Store-specific unique identifier for a path name. Clients must not depend on the GUID being unique across different stores, but a given (store-name, store-specific-path name) has a stable and unique GUID for its lifetime. |
| `STD_MODIFICATION_TIME` | `TIMESTAMP(6)` |  | Time of last change to the data associated with a path name. Changes to the content of a `TYPE_FILE` or `TYPE_REFERENCE` path, the referent of the `TYPE_LINK` path, and addition or deletion of immediate children in a `TYPE_DIRECTORY` path, all constitute data changes. |
| `STD_OWNER` | `VARCHAR2(32)` |  | Client-supplied (or implicit) owner name for the path name |
| `STD_PARENT_GUID` | `NUMBER` |  | Store-specific unique identifier for the parent of a path name. Clients must not depend on the GUID being unique across different stores, but a given (store-name, store-specific-path name) has a stable and unique GUID for its lifetime.  The GUID of the parent of this path name (that is that std\_parent\_guid(pathname) == std\_guid(parent(pathname))). |
| `STD_REFERENT` | `VARCHAR2(1024)` |  | Content of the symbolic link of a `TYPE_LINK` path, otherwise NULL. The `STD_REFERENT` can be an arbitrary string and must not necessarily be interpreted as path name by clients (or such interpretation should be done with great care). |
| `OPT_HASH_TYPE` | `VARCHAR2(32)` |  | Type of hash provided in the `OPT_HASH_VALUE` property (see `DBMS_CRYPTO` for possible options) |
| `OPT_HASH_VALUE` | `VARCHAR2(128)` |  | Hash value of type `OPT_HASH_TYPE` describing the content of the path name |
| `OPT_LOCK_COUNT` | `NUMBER` |  | Number of compatible locks placed on a path name. If different principals are allowed to place compatible (read) locks on a path, the `OPT_LOCKER` must specify all lockers with repeats so that lock counts can be correctly maintained. |
| `OPT_LOCK_DATA` | `VARCHAR2(128)` |  | Client-supplied user-data associated with a user-lock, uninterpreted by the store |
| `OPT_LOCKER` | `VARCHAR2(128)` |  | One or more implicit or client-specified principals that applied a user-lock on a path name |
| `OPT_LOCK_STATUS` | `NUMBER` |  | One of the (`LOCK_READ_ONLY`, `LOCK_WRITE_ONLY`, `LOCK_READ_WRITE`) values describing the type of lock currently applied on a path name |
| `OPT_VERSION` | `NUMBER` |  | Sequence number for linear versioning of a path name |
| `OPT_VERSION_PATH` | `VARCHAR2(1024)` |  | Version path name for hierarchical versioning of a path name |
| `OPT_CONTENT_ID` | `RAW(128)` |  | A provider-generated store-specific unique contentID in the form of a string for a file element (that may optionally not be associated with a path (see `FEATURE_CONTENT_ID` and `FEATURE_LAZY_PATH` in `DBMS_DBFS_CONTENT` Constants - Store Features) |

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS72478) for more information about DBMS\_DBFS\_CONTENT Constants - Path Name Types and DBMS\_DBFS\_CONTENT Constants - Store Features
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS664) for more information about the DBMS\_CRYPTO package