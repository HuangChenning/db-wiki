---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_PDB_ALTER_SHARING.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 131 DBMS\_PDB\_ALTER\_SHARING

In an application container with a pre-installed application, the `DBMS_PDB_ALTER_SHARING` package provides an interface to set database objects as application common objects or to specify that a database object is not an application common object.

Note:

This package provides a subset of the subprograms in the `DBMS_PDB` package. Users who do not have `EXECUTE` privilege on the `DBMS_PDB` package can be granted `EXECUTE` privilege on this package to run these subprograms.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container
- [Oracle XML DB Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB2700) for information about configuring protocol ports and DNS mappings
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF55686) for information about creating PDBs
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG634) regarding how to create audit policies in a multitenant environment

This chapter contains the following topics:

### 131.1 DBMS\_PDB\_ALTER\_SHARING Overview

The subprograms in this package can set a database object to one of the following types of application common objects in an application container: data-linked object, extended data-linked object, or metadata-linked object.

A data-linked application common object stores data in the application root that can be accessed and modified by all of the application PDBs in the application container. For an extended data-linked object, each application PDB can create its own specific data while sharing the common data in the application root. Therefore, with an extended data-linked object, only the data stored in the application root is common for all application PDBs. A metadata-linked application common object stores the metadata for the specific object, such as a table, in the application root, so that the containers in the application container have the same structure for the object but different data. This package also contains a procedure that specifies that a database object is not an application common object.

You can use the subprograms in this package when you

Typically, the subprograms in this package are used in the following cases:

- An application that is installed in a PDB is migrated to an application container. The application can be migrated to the application root or to an application PDB. For example, you can migrate an application installed in a PDB plugged into an Oracle Database 12c Release 1 (12.1) CDB to an application container in an Oracle Database 12c Release 2 (12.2) CDB.
- An application is installed in an application root using an installation program that does not allow setting application common objects.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container

### 131.2 DBMS\_PDB\_ALTER\_SHARING Security Model

This package provides a subset of the subprograms in the `DBMS_PDB` package. User who do not have `EXECUTE` privilege on the `DBMS_PDB` package can be granted `EXECUTE` privilege on this package to run these subprograms.

Security on this package can be controlled in either of the following ways:

- Granting `EXECUTE` on this package to selected users or roles.
- Granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

### 131.3 Summary of DBMS\_PDB\_ALTER\_SHARING Subprograms

This table lists and briefly describes `DBMS_PDB_ALTER_SHARING` package subprograms.

Table 131-1 DBMS\_PDB\_ALTER\_SHARING Subprograms

| Subprogram | Description |
| --- | --- |
| REMOVE\_LINK Procedure | Specifies that a database object is not an application common object |
| SET\_DATA\_LINKED Procedure | Sets a database object to a data-linked application common object |
| SET\_EXT\_DATA\_LINKED Procedure | Sets a database object to an extended data-linked application common object |
| SET\_METADATA\_LINKED Procedure | Sets a database object to a metadata-linked application common object |
| SET\_PROFILE\_EXPLICIT Procedure | Sets a profile as an application common profile in an application container. |
| SET\_ROLE\_EXPLICIT Procedure | Sets a role as an application common role in an application container. |
| SET\_USER\_EXPLICIT Procedure | Sets a local user as an application common user in an application container. |

#### 131.3.1 REMOVE\_LINK Procedure

This procedure specifies that a database object is not an application common object. In an application container, application common objects are shared between multiple containers.

Syntax

```
DBMS_PDB_ALTER_SHARING.REMOVE_LINK (
   schema_name  IN VARCHAR2, 
   object_name  IN VARCHAR2, 
   namespace    IN NUMBER, 
   edition_name IN VARCHAR2  DEFAULT NULL);
```

Parameters

Table 131-2 REMOVE\_LINK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema that owns the database object. |
| `object_name` | The name of the database object. |
| `namespace` | The namespace of the database object.  The `NAMESPACE` column of the `DBA_OBJECTS` view shows the namespace of an object. |
| `edition_name` | The name of the edition for the database object. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container

#### 131.3.2 SET\_DATA\_LINKED Procedure

This procedure sets a database object to a data-linked application common object. In an application container, data-linked application common objects store data in the application root only, and the data can be accessed by all of the application PDBs in the application container. The data in a data-linked application common object can be modified only in the application root.

You can use this procedure to set data-linked application common objects when you migrate an application that is installed in a PDB to an application container. The application can be migrated to the application root or to an application PDB. For example, you can migrate an application installed in a PDB plugged into an Oracle Database 12c Release 1 (12.1) CDB to an application container in an Oracle Database 12c Release 2 (12.2) CDB.

Syntax

```
DBMS_PDB_ALTER_SHARING.SET_DATA_LINKED (
   schema_name  IN VARCHAR2, 
   object_name  IN VARCHAR2, 
   namespace    IN NUMBER, 
   edition_name IN VARCHAR2  DEFAULT NULL);
```

Parameters

Table 131-3 SET\_DATA\_LINKED Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema that owns the database object. |
| `object_name` | The name of the database object. |
| `namespace` | The namespace of the database object.  The `NAMESPACE` column of the `DBA_OBJECTS` view shows the namespace of an object. |
| `edition_name` | The name of the edition for the database object. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container

#### 131.3.3 SET\_EXT\_DATA\_LINKED Procedure

This procedure sets a database object to an extended data-linked application common object. In an application container, for an extended data-linked object, each application PDB can create its own specific data while sharing the common data in the application root. Therefore, only the data stored in the application root is common for all application PDBs.

You can use this procedure to set extended data-linked application common objects when you migrate an application that is installed in a PDB to an application container. The application can be migrated to the application root or to an application PDB. For example, you can migrate an application installed in a PDB plugged into an Oracle Database 12c Release 1 (12.1) CDB to an application container in an Oracle Database 12c Release 2 (12.2) CDB.

Syntax

```
DBMS_PDB_ALTER_SHARING.SET_EXT_DATA_LINKED (
   schema_name  IN VARCHAR2, 
   object_name  IN VARCHAR2, 
   namespace    IN NUMBER, 
   edition_name IN VARCHAR2  DEFAULT NULL);
```

Parameters

Table 131-4 SET\_EXT\_DATA\_LINKED Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema that owns the database object. |
| `object_name` | The name of the database object. |
| `namespace` | The namespace of the database object.  The `NAMESPACE` column of the `DBA_OBJECTS` view shows the namespace of an object. |
| `edition_name` | The name of the edition for the database object. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container

#### 131.3.4 SET\_METADATA\_LINKED Procedure

This procedure sets a database object to a metadata-linked application common object. In an application container, metadata-linked application common objects store the metadata for specific objects, such as tables, so that the containers that share the application common object have the same structure but different data.

You can use this procedure to set metadata-linked application common objects when you migrate an application that is installed in a PDB to an application container. The application can be migrated to the application root or to an application PDB. For example, you can migrate an application installed in a PDB plugged into an Oracle Database 12c Release 1 (12.1) CDB to an application container in an Oracle Database 12c Release 2 (12.2) CDB.

Syntax

```
DBMS_PDB_ALTER_SHARING.SET_METADATA_LINKED (
   schema_name  IN VARCHAR2, 
   object_name  IN VARCHAR2, 
   namespace    IN NUMBER, 
   edition_name IN VARCHAR2  DEFAULT NULL);
```

Parameters

Table 131-5 SET\_METADATA\_LINKED Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema that owns the database object. |
| `object_name` | The name of the database object. |
| `namespace` | The namespace of the database object.  The `NAMESPACE` column of the `DBA_OBJECTS` view shows the namespace of an object. |
| `edition_name` | The name of the edition for the database object. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container

#### 131.3.5 SET\_PROFILE\_EXPLICIT Procedure

This procedure sets a profile as an application common profile in an application container. This procedure is intended for migrating a profile from a previous release to an application container in the current release.

This procedure must be invoked in an application install, patch, upgrade, or uninstall operation in an application root.

Syntax

```
DBMS_PDB_ALTER_SHARING.SET_PROFILE_EXPLICIT (
   profile_name IN VARCHAR2);
```

Parameters

Table 131-6 SET\_PROFILE\_EXPLICIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `profile_name` | The name of the profile. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container.

#### 131.3.6 SET\_ROLE\_EXPLICIT Procedure

This procedure sets a role as an application common role in an application container. This procedure is intended for migrating a role from a previous release to an application container in the current release.

This procedure must be invoked in an application install, patch, upgrade, or uninstall operation in an application root.

Syntax

```
DBMS_PDB_ALTER_SHARING.SET_ROLE_EXPLICIT (
   role_name IN VARCHAR2);
```

Parameters

Table 131-7 SET\_ROLE\_EXPLICIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `role_name` | The name of the role. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container.

#### 131.3.7 SET\_USER\_EXPLICIT Procedure

This procedure sets a local user as an application common user in an application container.

This procedure must be invoked in an application install, patch, upgrade, or uninstall operation in an application root.

Syntax

```
DBMS_PDB_ALTER_SHARING.SET_USER_EXPLICIT (
   user_name IN VARCHAR2);
```

Parameters

Table 131-8 SET\_USER\_EXPLICIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `user_name` | The name of the user. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-D2F30723-9E70-469C-8048-CB06DE00173E) for information about migrating an application to an application container.