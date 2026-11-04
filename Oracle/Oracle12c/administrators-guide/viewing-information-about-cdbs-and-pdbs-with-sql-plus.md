---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/viewing-information-about-cdbs-and-pdbs-with-sql-plus.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

You can view information about CDBs and PDBs with SQL\*Plus.

Note:

You can complete the tasks in this chapter using SQL\*Plus or Oracle SQL Developer.

- About CDB and Container Information in Views  
	In a multitenant container database (CDB), the metadata for data dictionary tables and view definitions is stored only in the root. However, each container, including each pluggable database (PDB), application root, and application PDB, has its own set of data dictionary tables and views for the database objects contained in the container.
- About Viewing Information When the Current Container Is a Not the CDB Root  
	When the current container is a PDB, an application root, or an application PDB, a user can view data dictionary information for the current container only.
- About Viewing Information When the Current Container Is the CDB Root  
	When the current container is the CDB root, a common user can view data dictionary information for the CDB root and for PDBs, application roots, and application PDBs by querying container data objects.
- Views for a CDB  
	You can query a set of views for information about a CDB and its PDBs.
- Determining Whether a Database Is a CDB  
	You can query the `CDB` column in the `V$DATABASE` view to determine whether a database is a CDB or a non-CDB. The `CDB` column returns `YES` if the current database is a CDB or `NO` if the current database is a non-CDB.
- Viewing Information About the Containers in a CDB  
	The `V$CONTAINERS` view provides information about all of the containers in a CDB, including the root and all PDBs.
- Viewing Information About PDBs  
	The `CDB_PDBS` view and `DBA_PDBS` view provide information about the PDBs associated with a CDB, including the status of each PDB.
- Viewing the Open Mode of Each PDB  
	The `V$PDBS` view provides information about the PDBs associated with the current database instance.
- Querying Container Data Objects  
	In the root, container data objects can show information about database objects (such as tables and users) contained in the root and in PDBs. Access to PDB information is controlled by the common user's `CONTAINER_DATA` attribute.
- Querying Across Containers with the CONTAINERS Clause  
	The `CONTAINERS` clause enables you to query tables and views across all containers in a CDB. It also enables you to query application common objects across all containers in an application container.
- Determining the Current Container ID or Name  
	You can determine your current container ID or container name in a CDB.
- Listing the Initialization Parameters That Are Modifiable in PDBs  
	In a CDB, some initialization parameters apply to the root and to all of the PDBs. When such an initialization parameter is changed, it affects the entire CDB. You can set other initialization parameters to different values in each container.
- Viewing the History of PDBs  
	The `CDB_PDB_HISTORY` view shows the history of the PDBs in a CDB. It provides information about when and how each PDB was created and other information about each PDB's history.
- Viewing Information About Applications in Application Containers  
	Several views provide information about the applications in application containers in a CDB.

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 45.1 About CDB and Container Information in Views

In a multitenant container database (CDB), the metadata for data dictionary tables and view definitions is stored only in the root. However, each container, including each pluggable database (PDB), application root, and application PDB, has its own set of data dictionary tables and views for the database objects contained in the container.

Because each container can contain different data and schema objects, containers can display different information in data dictionary views, even when querying the same data dictionary view in each container. For example, the information about tables displayed in the `DBA_TABLES` view can be different in two different containers, because the containers can contain different tables. An internal mechanism called a metadata link enables a container to access the metadata for these views in the root.

If a dictionary table stores information that pertains to the CDB as a whole, instead of for each container, then both the metadata and the data displayed in a data dictionary view are stored in the root. For example, Automatic Workload Repository (AWR) data can be stored in the root, and this data is displayed in some data dictionary views, such as the `DBA_HIST_ACTIVE_SESS_HISTORY` view. An internal mechanism called an data link enables a container to access both the metadata and the data for these types of views in the root.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89255) for more information about dictionary access in containers, metadata links, and data links

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.2 About Viewing Information When the Current Container Is a Not the CDB Root

When the current container is a PDB, an application root, or an application PDB, a user can view data dictionary information for the current container only.

To an application connected to a particular PDB, application root, or application PDB, the data dictionary appears as it would for a non-CDB. The data dictionary only shows information related to the current container. Also, in a container that is not the CDB root, `CDB_` views only show information about database objects visible through the corresponding `DBA_` view.

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.3 About Viewing Information When the Current Container Is the CDB Root

When the current container is the CDB root, a common user can view data dictionary information for the CDB root and for PDBs, application roots, and application PDBs by querying container data objects.

A container data object is a table or view that can contain data pertaining to the following:

- One or more containers
- The CDB as a whole
- One or more containers and the CDB as a whole

Container data objects include `V$`, `GV$`, `CDB_`, and some Automatic Workload Repository `DBA_HIST*` views. A common user's `CONTAINER_DATA` attribute determines which containers are visible in container data objects.

In a CDB, for every `DBA_` view, there is a corresponding `CDB_` view. All `CDB_` views are container data objects, but most `DBA_` views are not.

Each container data object contains a `CON_ID` column that identifies the container for each row returned. Table 45-1 describes the meanings of the values in the `CON_ID` column.

Table 45-1 CON\_ID Column in Container Data Objects

| Value in CON\_ID Column | Description |
| --- | --- |
| 0 | The data pertains to the entire CDB |
| 1 | The data pertains to the CDB root |
| 2 | The data pertains to the CDB seed |
| 3 - 4,098 | The data pertains to a PDB, an application root, or an application PDB  Each container has its own container ID. |

The following views behave differently from other `[G]V$` views:

- `[G]V$SYSSTAT`
- `[G]V$SYS_TIME_MODEL`
- `[G]V$SYSTEM_EVENT`
- `[G]V$SYSTEM_WAIT_CLASS`

When queried from the CDB root, these views return instance-wide data, with `0` in the `CON_ID` column for each row returned. However, you can query equivalent views that behave the same as other container data objects. The following views can return specific data for each container in a CDB: `[G]V$CON_SYSSTAT`, `[G]V$CON_SYS_TIME_MODEL`, `[G]V$CON_SYSTEM_EVENT`, and `[G]V$CON_SYSTEM_WAIT_CLASS`.

Note:

- When querying a container data object, the data returned depends on whether containers are open and on the privileges granted to the user running the query.
- In an Oracle Real Application Clusters (Oracle RAC) environment, the data returned by container data objects might vary based on the instance to which a session is connected.
- In a non-CDB, all `CON_ID` columns in container data objects are 0 (zero).
- When a container is opened in restricted mode, it is ignored in queries on `CDB_` views.

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89349) for a conceptual overview of container data objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) for detailed information about container data objects

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.4 Views for a CDB

You can query a set of views for information about a CDB and its PDBs.

Table 45-2 describes data dictionary views that are useful for monitoring a CDB and its PDBs.

Table 45-2 Views for a CDB

| View | Description | More Information |
| --- | --- | --- |
| Container data objects, including:  - `V$` views - `GV$` views - `CDB_` views - `DBA_HIST*` views | Container data objects can display information about multiple PDBs. Each container data object includes a `CON_ID` column to identify containers.  There is a `CDB_` view for each corresponding `DBA_` view. | " Querying Container Data Objects "  [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) |
| `{CDB\|DBA}_PDBS` | Displays information about the PDBs associated with the CDB, including the status of each PDB. | " Viewing Information About PDBs "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN23794) |
| `CDB_PROPERTIES` | Displays the permanent properties of each container in a CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN29012) |
| `{CDB\|DBA}_PDB_HISTORY` | Displays the history of each PDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN23865) |
| `{CDB\|DBA}_CONTAINER_DATA` | Displays information about the user-level and object-level `CONTAINER_DATA` attributes specified in the CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN23866) |
| `{CDB\|DBA}_HIST_PDB_INSTANCE` | Displays the PDBs and instances in the Workload Repository. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN23862) |
| `{CDB\|DBA}_PDB_SAVED_STATES` | Displays information about the current saved PDB states in the CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN23959)  " [Preserving or Discarding the Open Mode of PDBs When the CDB Restarts](administering-a-cdb-with-sql-plus.md) " |
| `{CDB\|DBA}_APPLICATIONS` | Describes all of the applications in an application container. | " Viewing Information About Applications " |
| `{CDB\|DBA}_APP_STATEMENTS` | Describes all of the statements from application installation, upgrade, and patch operations in an application container. | " Viewing Information About Application Statements " |
| `{CDB\|DBA}_APP_PATCHES` | Describes all of the application patches in an application container. | " Viewing Information About Application Patches " |
| `{CDB\|DBA}_APP_ERRORS` | Describes all of the application error messages generated in an application container. | " Viewing Information About Application Errors " |
| `{CDB\|DBA}_CDB_RSRC_PLANS` | Displays information about all the CDB resource plans. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN23809)  " [Viewing CDB Resource Plans](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) " |
| `{CDB\|DBA}_CDB_RSRC_PLAN_DIRECTIVES` | Displays information about all the CDB resource plan directives. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN23808)  " [Viewing CDB Resource Plan Directives](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) " |
| `PDB_ALERTS` | Contains descriptions of reasons for PDB alerts. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN29165) |
| `PDB_PLUG_IN_VIOLATIONS` | Displays information about incompatibilities between a PDB and the CDB to which it belongs. This view is also used to display information generated by executing `DBMS_PDB.CHECK_PLUG_COMPATIBILITY`. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN29161)  " [Creating a PDB by Plugging an Unplugged PDB into a CDB](creating-and-removing-pdbs-with-sql-plus.md) " |
| `{USER\|ALL\|DBA\|CDB}_OBJECTS` | Displays information about database objects, and the `SHARING` column shows whether a database object is a metadata-linked object, a data-linked object, an extended data-linked object, or a standalone object that is not linked to another object. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN20146) |
| `{ALL\|DBA\|CDB}_SERVICES` | Displays information about database services, and the `PDB` column shows the name of the PDB associated with each service. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN20465) |
| `{USER\|ALL\|DBA\|CDB}_VIEWS`  `{USER\|ALL\|DBA\|CDB}_TABLES` | The `CONTAINER_DATA` column shows whether the view or table is a container data object. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN) |
| `{USER\|ALL\|DBA\|CDB}_USERS` | The `COMMON` column shows whether a user is a common user or a local user. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN20302) |
| `{USER\|ALL\|DBA\|CDB}_ROLES`  `{USER\|ALL\|DBA\|CDB}_COL_PRIVS`  `{USER\|ALL}_COL_PRIVS_MADE`  `{USER\|ALL}_COL_PRIVS_RECD`  `{USER\|ALL}_TAB_PRIVS_MADE`  `{USER\|ALL}_TAB_PRIVS_RECD`  `{USER\|DBA\|CDB}_SYS_PRIVS`  `{USER\|DBA\|CDB}_ROLE_PRIVS`  `ROLE_TAB_PRIVS`  `ROLE_SYS_PRIVS` | The `COMMON` column shows whether a role or privilege is commonly granted or locally granted. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN) |
| `{USER\|ALL\|DBA\|CDB}_ARGUMENTS`  `{USER\|ALL\|DBA\|CDB}_CLUSTERS`  `{USER\|ALL\|DBA\|CDB}_CONSTRAINTS`  `{ALL\|DBA\|CDB}_DIRECTORIES`  `{USER\|ALL\|DBA\|CDB}_IDENTIFIERS`  `{USER\|ALL\|DBA\|CDB}_LIBRARIES`  `{USER\|ALL\|DBA\|CDB}_PROCEDURES`  `{USER\|ALL\|DBA\|CDB}_SOURCE`  `{USER\|ALL\|DBA\|CDB}_SYNONYMS`  `{USER\|ALL\|DBA\|CDB}_VIEWS` | The `ORIGIN_CON_ID` column shows the ID of the container from which the row originates. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN) |
| `[G]V$DATABASE` | Displays information about the database from the control file. If the database is a CDB, then CDB-related information is included. | " Determining Whether a Database Is a CDB "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN30047) |
| `[G]V$CONTAINERS` | Displays information about the containers associated with the current CDB, including the root and all PDBs. | " Viewing Information About the Containers in a CDB "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN30708) |
| `[G]V$PDBS` | Displays information about the PDBs associated with the current CDB, including the open mode of each PDB. | " Viewing the Open Mode of Each PDB "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN30652) |
| `[G]V$PDB_INCARNATION` | Displays information about all PDB incarnations. Oracle creates a new PDB incarnation whenever a PDB is opened with the `RESETLOGS` option. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN30709) |
| `[G]V$SYSTEM_PARAMETER`  `[G]V$PARAMETER` | Displays information about initialization parameters, and the `ISPDB_MODIFIABLE` column shows whether a parameter can be modified for a PDB. | " Listing the Initialization Parameters That Are Modifiable in PDBs "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN30275) |
| `V$DIAG_ALERT_EXT`  `[G]V$DIAG_APP_TRACE_FILE`  `[G]V$DIAG_OPT_TRACE_RECORDS`  `V$DIAG_SESS_OPT_TRACE_RECORDS`  `V$DIAG_SESS_SQL_TRACE_RECORDS`  `[G]V$DIAG_SQL_TRACE_RECORDS`  `[G]V$DIAG_TRACE_FILE`  `[G]V$DIAG_TRACE_FILE_CONTENTS` | Displays trace file and alert file data for the current container in a CDB. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGSQL-GUID-93ACB9CC-9937-479E-8995-FEABD854C900) |
| `V$DIAG_INCIDENT`  `V$DIAG_PROBLEM` | Displays information about problems and incidents for the current container in a CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN) |

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.5 Determining Whether a Database Is a CDB

You can query the `CDB` column in the `V$DATABASE` view to determine whether a database is a CDB or a non-CDB. The `CDB` column returns `YES` if the current database is a CDB or `NO` if the current database is a non-CDB.

To determine whether a database is a CDB:

1. In SQL\*Plus, connect to the database as an administrative user.
2. Query the `V$DATABASE` view.

Example 45-1 Determining Whether a Database is a CDB

```
SELECT CDB FROM V$DATABASE;
```

Sample output:

```
CDB
---
YES
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN30047)

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.6 Viewing Information About the Containers in a CDB

The `V$CONTAINERS` view provides information about all of the containers in a CDB, including the root and all PDBs.

To view this information, the query must be run by a common user whose current container is the root. When the current container is a PDB, this view only shows information about the current PDB.

To view information about the containers in a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `V$CONTAINERS` view.

Example 45-2 Viewing Identifying Information About Each Container in a CDB

```
COLUMN NAME FORMAT A8

SELECT NAME, CON_ID, DBID, CON_UID, GUID FROM V$CONTAINERS ORDER BY CON_ID;
```

Sample output:

```
NAME         CON_ID       DBID    CON_UID GUID
-------- ---------- ---------- ---------- --------------------------------
CDB$ROOT          1  659189539          1 C091A6F89C7572A1E0436797E40AC78D
PDB$SEED          2 4026479912 4026479912 C091AE9C00377591E0436797E40AC138
HRPDB             3 3718888687 3718888687 C091B6B3B53E7834E0436797E40A9040
SALESPDB          4 2228741407 2228741407 C091FA64EF8F0577E0436797E40ABE9F
```

### 45.7 Viewing Information About PDBs

The `CDB_PDBS` view and `DBA_PDBS` view provide information about the PDBs associated with a CDB, including the status of each PDB.

To view this information, the query must be run by a common user whose current container is the root. When the current container is a PDB, all queries on these views return no results.

To view information about PDBs:

1. In SQL\*Plus, ensure that the current container is the root.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `CDB_PDBS` or `DBA_PDBS` view.

Example 45-3 Viewing Container ID, Name, and Status of Each PDB

```
COLUMN PDB_NAME FORMAT A15
 
SELECT PDB_ID, PDB_NAME, STATUS FROM DBA_PDBS ORDER BY PDB_ID;
```

Sample output:

```
PDB_ID PDB_NAME        STATUS
---------- --------------- -------------
         2 PDB$SEED        NORMAL
         3 HRPDB           NORMAL
         4 SALESPDB        NORMAL
```

See Also:

" [About the Current Container](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.8 Viewing the Open Mode of Each PDB

The `V$PDBS` view provides information about the PDBs associated with the current database instance.

You can query this view to determine the open mode of each PDB. For each PDB that is open, this view can also show when the PDB was last opened. A common user can query this view when the current container is the root or a PDB. When the current container is a PDB, this view only shows information about the current PDB.

To view the open status of each PDB:

1. In SQL\*Plus, access a container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `V$PDBS` view.

Example 45-4 Viewing the Name and Open Mode of Each PDB

```
COLUMN NAME FORMAT A15
COLUMN RESTRICTED FORMAT A10
COLUMN OPEN_TIME FORMAT A30
 
SELECT NAME, OPEN_MODE, RESTRICTED, OPEN_TIME FROM V$PDBS;
```

Sample output:

```
NAME            OPEN_MODE  RESTRICTED OPEN_TIME
--------------- ---------- ---------- ------------------------------
PDB$SEED        READ ONLY  NO         21-MAY-12 12.19.54.465 PM
HRPDB           READ WRITE NO         21-MAY-12 12.34.05.078 PM
SALESPDB        MOUNTED    NO         22-MAY-12 10.37.20.534 AM
```

See Also:

- " [Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE](administering-a-cdb-with-sql-plus.md) "
- " [Modifying the Open Mode of PDBs](administering-a-cdb-with-sql-plus.md) "
- " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) "
- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.9 Querying Container Data Objects

In the root, container data objects can show information about database objects (such as tables and users) contained in the root and in PDBs. Access to PDB information is controlled by the common user's `CONTAINER_DATA` attribute.

For example, `CDB_` views are container data objects. See " About Viewing Information When the Current Container Is the Root " and [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) for more information about container data objects.

Each container data object contains a `CON_ID` column that shows the container ID of each PDB in the query results. You can view the PDB name for a container ID by querying the `DBA_PDBS` view.

To use container data objects to show information about multiple PDBs:

1. In SQL\*Plus, ensure that the current container is the root.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the container data object to show the desired information.

Note:

When a query contains a join of a container data object and a non-container data object, and the current container is the root, the query returns data for the entire CDB only (`CON_ID` = `0`).

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89349) for a conceptual overview of container data objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) for detailed information about container data objects

Example 45-5 Showing the Tables Owned by Specific Schemas in Multiple PDBs

This example queries the `DBA_PDBS` view and the `CDB_TABLES` view from the root to show the tables owned by `hr` user and `oe` user in the PDBs associated with the CDB. This query returns only rows where the PDB has an ID greater than 2 (`p.PDB_ID > 2`) to avoid showing the users in the CDB root and CDB seed.

```
COLUMN PDB_NAME FORMAT A15
COLUMN OWNER FORMAT A15
COLUMN TABLE_NAME FORMAT A30
 
SELECT p.PDB_ID, p.PDB_NAME, t.OWNER, t.TABLE_NAME 
  FROM DBA_PDBS p, CDB_TABLES t 
  WHERE p.PDB_ID > 2 AND
        t.OWNER IN('HR','OE') AND
        p.PDB_ID = t.CON_ID
  ORDER BY p.PDB_ID;
```

Sample output:

```
PDB_ID PDB_NAME        OWNER           TABLE_NAME
---------- --------------- --------------- ------------------------------
         3 HRPDB           HR              COUNTRIES
         3 HRPDB           HR              JOB_HISTORY
         3 HRPDB           HR              EMPLOYEES
         3 HRPDB           HR              JOBS
         3 HRPDB           HR              DEPARTMENTS
         3 HRPDB           HR              LOCATIONS
         3 HRPDB           HR              REGIONS
         4 SALESPDB        OE              PRODUCT_INFORMATION
         4 SALESPDB        OE              INVENTORIES
         4 SALESPDB        OE              ORDERS
         4 SALESPDB        OE              ORDER_ITEMS
         4 SALESPDB        OE              WAREHOUSES
         4 SALESPDB        OE              CUSTOMERS
         4 SALESPDB        OE              SUBCATEGORY_REF_LIST_NESTEDTAB
         4 SALESPDB        OE              PRODUCT_REF_LIST_NESTEDTAB
         4 SALESPDB        OE              PROMOTIONS
         4 SALESPDB        OE              PRODUCT_DESCRIPTIONS
```

This sample output shows the PDB `hrpdb` has tables in the `hr` schema and the PDB `salespdb` has tables in the `oe` schema.

Example 45-6 Showing the Users in Multiple PDBs

This example queries the `DBA_PDBS` view and the `CDB_USERS` view from the root to show the users in each PDB. The query uses `p.PDB_ID > 2` to avoid showing the users in the CDB root and the CDB seed.

```
COLUMN PDB_NAME FORMAT A15
COLUMN USERNAME FORMAT A30
 
SELECT p.PDB_ID, p.PDB_NAME, u.USERNAME 
  FROM DBA_PDBS p, CDB_USERS u
  WHERE p.PDB_ID > 2 AND
        p.PDB_ID = u.CON_ID
  ORDER BY p.PDB_ID;
```

Sample output:

```
PDB_ID PDB_NAME        USERNAME
---------- --------------- ------------------------------
         .
         .
         .
         3 HRPDB           HR
         3 HRPDB           OLAPSYS
         3 HRPDB           MDSYS
         3 HRPDB           ORDSYS
         .
         .
         .
         4 SALESPDB        OE
         4 SALESPDB        CTXSYS
         4 SALESPDB        MDSYS
         4 SALESPDB        EXFSYS
         4 SALESPDB        OLAPSYS
         .
         .
         .
```

Example 45-7 Showing the Data Files for Each PDB in a CDB

This example queries the `DBA_PDBS` and `CDB_DATA_FILES` views to show the name and location of each data file for all of the PDBs in a CDB, including the CDB seed.

```
COLUMN PDB_ID FORMAT 999
COLUMN PDB_NAME FORMAT A8
COLUMN FILE_ID FORMAT 9999
COLUMN TABLESPACE_NAME FORMAT A10
COLUMN FILE_NAME FORMAT A45

SELECT p.PDB_ID, p.PDB_NAME, d.FILE_ID, d.TABLESPACE_NAME, d.FILE_NAME
  FROM DBA_PDBS p, CDB_DATA_FILES d
  WHERE p.PDB_ID = d.CON_ID
  ORDER BY p.PDB_ID;
```

Sample output:

```
PDB_ID PDB_NAME FILE_ID TABLESPACE FILE_NAME
------ -------- ------- ---------- ---------------------------------------------
     2 PDB$SEED       6 SYSAUX     /disk1/oracle/dbs/pdbseed/cdb1_ax.f
     2 PDB$SEED       5 SYSTEM     /disk1/oracle/dbs/pdbseed/cdb1_db.f
     3 HRPDB          9 SYSAUX     /disk1/oracle/dbs/hrpdb/hrpdb_ax.f
     3 HRPDB          8 SYSTEM     /disk1/oracle/dbs/hrpdb/hrpdb_db.f
     3 HRPDB         13 USER       /disk1/oracle/dbs/hrpdb/hrpdb_usr.dbf
     4 SALESPDB      15 SYSTEM     /disk1/oracle/dbs/salespdb/salespdb_db.f
     4 SALESPDB      16 SYSAUX     /disk1/oracle/dbs/salespdb/salespdb_ax.f
     4 SALESPDB      18 USER       /disk1/oracle/dbs/salespdb/salespdb_usr.dbf
```

Example 45-8 Showing the Temp Files in a CDB

This example queries the `CDB_TEMP_FILES` view to show the name and location of each temp file in a CDB, as well as the tablespace that uses the temp file.

```
COLUMN CON_ID FORMAT 999
COLUMN FILE_ID FORMAT 9999
COLUMN TABLESPACE_NAME FORMAT A15
COLUMN FILE_NAME FORMAT A45

SELECT CON_ID, FILE_ID, TABLESPACE_NAME, FILE_NAME
  FROM CDB_TEMP_FILES
  ORDER BY CON_ID;
```

Sample output:

```
CON_ID FILE_ID TABLESPACE_NAME FILE_NAME
------ ------- --------------- ---------------------------------------------
     1       1 TEMP            /disk1/oracle/dbs/t_tmp1.f
     2       2 TEMP            /disk1/oracle/dbs/pdbseed/t_tmp1.f
     3       3 TEMP            /disk1/oracle/dbs/hrpdb/t_hrpdb_tmp1.f
     4       4 TEMP            /disk1/oracle/dbs/salespdb/t_salespdb_tmp1.f
```

Example 45-9 Showing the Services Associated with PDBs

This example queries the `CDB_SERVICES` view to show the PDB name, network name, and container ID of each service associated with a PDB.

```
COLUMN NETWORK_NAME FORMAT A30
COLUMN PDB FORMAT A15
COLUMN CON_ID FORMAT 999

SELECT PDB, NETWORK_NAME, CON_ID FROM CDB_SERVICES
  WHERE PDB IS NOT NULL AND
        CON_ID > 2
  ORDER BY PDB;
```

Sample output:

```
PDB             NETWORK_NAME                   CON_ID
--------------- ------------------------------ ------
HRPDB           hrpdb.example.com                   3
SALESPDB        salespdb.example.com                4
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN20465)

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.10 Querying Across Containers with the CONTAINERS Clause

The `CONTAINERS` clause enables you to query tables and views across all containers in a CDB. It also enables you to query application common objects across all containers in an application container.

- About Querying Across Containers with the CONTAINERS Clause  
	The `CONTAINERS` clause enables you to query across containers in a CDB.
- Querying User-Created Tables and Views Across All Containers  
	The `CONTAINERS` clause enables you to query user-created tables and views across all containers in a CDB. This clause enables queries from the CDB root to display data in tables or views that exist in all of the open PDBs in a CDB.
- Querying Application Common Objects Across Application PDBs  
	The `CONTAINERS` clause enables you to query application common objects, such as tables and views, across all application PDBs in an application container. This clause enables queries from the application root to display data in tables or views that exist in all of the open application PDBs in the application container.

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

#### 45.10.1 About Querying Across Containers with the CONTAINERS Clause

The `CONTAINERS` clause enables you to query across containers in a CDB.

The `CONTAINERS` clause enables you to query user-created tables and views across all containers in a CDB. This clause enables queries from the CDB root to display data in tables or views that exist in all of the open containers in a CDB.

The `CONTAINERS` clause also enables you to query application common objects, such as tables and views, across all application PDBs in an application container. This clause enables queries from the application root to display data in tables or views that exist in all of the open application PDBs in the application container.

The `CONTAINERS_PARALLEL_DEGREE` initialization parameter can control the degree of parallelism of a query involving the `CONTAINERS` clause. If the value of `CONTAINERS_PARALLEL_DEGREE` is lower than `65535` (the default), then the specified value is used.

When the `CONTAINERS_PARALLEL_DEGREE` initialization parameter is set to the default value (`65535`), queries that use the `CONTAINERS` clause are parallel by default. The default degree of parallelism is calculated with the following formula:
```
max(min(cpu_count,number_of_open_containers),#instances)
```

In addition, you can pass a `DEFAULT_PDB_HINT` hint in the `CONTAINERS` clause. The hint is passed in the query that is run in each container.

You can force the recursive SQL that results from a query that includes the `CONTAINERS` clause to be parallel by using the `DEFAULT_PDB_HINT` clause of a `CONTAINERS` hint or by using automatic degree of parallelism. However, parallel statement queuing is not possible for recursive SQL that results from a query that includes the `CONTAINERS` clause.

Columns of the following types are removed if they exist in a table specified in a `CONTAINERS` clause:

- The following user-defined types: object types, varrays, REFs, and nested tables
- The following Oracle-supplied types: `ANYTYPE`, `ANYDATASET`, URI types, `SDO_TOPO_GEOMETRY`, `SDO_GEORASTER`, and `Expression`

Note:

- When a container is opened in restricted mode, it is ignored by the `CONTAINERS` clause.
- When the `CONTAINERS` clause is used and an error is returned by a container, the query does not return results from the container that raised the error, and the error is not returned. For example, you cannot select a `BFILE` column from a remote table into a local variable. If a query that does this uses the `CONTAINERS` clause and includes local and remote containers, then the query returns results for the local containers, but not the remote containers, and no error is returned.

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF56898) for more information about the `CONTAINERS` clause and the `CONTAINERS` hint
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) for detailed information about container data objects
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN-GUID-17F470E8-4C0D-43C8-AD2F-376B1503BCF6) for more information about the `CONTAINERS_PARALLEL_DEGREE` initialization parameter
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DWHSG9066) for more information about automatic degree of parallelism and parallel statement queuing

**Parent topic:** Querying Across Containers with the CONTAINERS Clause

#### 45.10.2 Querying User-Created Tables and Views Across All Containers

The `CONTAINERS` clause enables you to query user-created tables and views across all containers in a CDB. This clause enables queries from the CDB root to display data in tables or views that exist in all of the open PDBs in a CDB.

Note:

This feature is available starting with Oracle Database 12c Release 1 (12.1.0.2).

Prerequisites

The tables and views, or synonyms of them, specified in the `CONTAINERS` clause must exist in the CDB root and in all other containers.

To use the `CONTAINERS` clause to query tables and views across all containers:

1. In SQL\*Plus, access a container.
	To view data in multiple containers, ensure that the current container is the CDB root.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Run a query that includes the `CONTAINERS` clause.

Example 45-10 Querying a Table Owned by a Common User Across All Containers

This example makes the following assumptions:

- An organization has several PDBs, and each PDB is for a different department in the organization.
- Each PDB has an `employees` table that tracks the employees in the department, but the table in each PDB contains different employees.
- The CDB root also has an empty `employees` table.
- The employees table in each container is owned by the same common user.

With the CDB root as the current container and the common user that owns the table as the current user, run the following query with the `CONTAINERS` clause to return all of the employees in the `employees` table in all PDBs:

```
SELECT * FROM CONTAINERS(employees);
```

Example 45-11 Querying a Table Owned by Local Users Across All Containers

This example makes the following assumptions:

- An organization has several PDBs, and each PDB is for a different department in the organization.
- Each PDB has an `hr.employees` table that tracks the employees in the department, but the table in each PDB contains different employees.
- The CDB root also has an empty `employees` table owned by a common user.

To run a query that returns all of the employees in all of the PDBs, first connect to each PDB as a common user, and create a view with the following statement:

```
CREATE OR REPLACE VIEW employees AS SELECT * FROM hr.employees;
```

The common user that owns the view must be the same common user that owns the `employees` table in the CDB root. After you run this statement in each PDB, the common user has a view named `employees` in each PDB.

With the CDB root as the current container and the common user as the current user, run the following query with the `CONTAINERS` clause to return all of the employees in the `hr.employees` table in all PDBs:

```
SELECT * FROM CONTAINERS(employees);
```

You can also query the view in specific containers. For example, the following SQL statement queries the view in the containers with a `CON_ID` of `3` and `4`:

```
SELECT * FROM CONTAINERS(employees) WHERE CON_ID IN(3,4);
```

Note:

You can also use the `CONTAINERS` clause to query Oracle-supplied tables and views. When running the query, ensure that the current user is the owner of the table or view, or create a view using the `CONTAINERS` clause and grant `SELECT` privilege on the view to the appropriate users.

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF56898) for more information about the `CONTAINERS` clause
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89349) for a conceptual overview of container data objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) for detailed information about container data objects

**Parent topic:** Querying Across Containers with the CONTAINERS Clause

#### 45.10.3 Querying Application Common Objects Across Application PDBs

The `CONTAINERS` clause enables you to query application common objects, such as tables and views, across all application PDBs in an application container. This clause enables queries from the application root to display data in tables or views that exist in all of the open application PDBs in the application container.

The `CONTAINERS` clause is most useful for metadata-linked application common objects. With metadata-linked application common objects, the structure is the same in all of the containers in an application container, but the data is different. You can use the `CONTAINERS` clause to view the data in a metadata-linked application common object in multiple application PDBs. The benefits are similar for extended data-linked objects. The `CONTAINERS` clause uses parallel execution to execute the query across the distinct application PDBs hosted in the application root.

To use the `CONTAINERS` clause to query tables and views across all application PDBs:

1. In SQL\*Plus, access the application root.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Run a query that includes the `CONTAINERS` clause.

Note:

You can enable the `CONTAINERS_DEFAULT` attribute for a table or view in an application root. When this attribute is enabled, the `CONTAINERS` clause is used for queries and DML statements on the database object by default, and the `CONTAINERS` clause is not required in the SQL statements. To enable the `CONTAINERS_DEFAULT` attribute for a table or view in an application root, run the `ALTER TABLE` or `CREATE OR REPLACE VIEW` statement with the `ENABLE CONTAINERS_DEFAULT` clause.

Example 45-12 Querying an Application Common Object Across All Application PDBs

This example makes the following assumptions:

- An organization has several application PDBs, and each application PDB is for a different department in the organization.
- Each application PDB has an `employees` table that tracks the employees in the department, but the table in each application PDB contains different employees.
- The application root also has an empty `employees` table.
- The employees table in each container is owned by the same common user.
- A company has multiple tenants that use an application in an application container, and each tenant has its own application PDB.
- The company uses metadata-linked application common objects to keep the structure of the data the same in all of the application PDBs, but the data is different in each application PDB.
- Each application PDB has a metadata-linked `sales.customers` table that stores information about each tenant’s customers.

With the application root as the current container and the application common user that owns the table as the current user, run the following query with the `CONTAINERS` clause to return all of the customers in the `sales.customers` table in all application PDBs:

```
SELECT * FROM CONTAINERS(sales.customers);
```

See Also:

- " [About Application Common Objects](administering-application-containers-with-sql-plus.md) "
- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF56898) for more information about the `CONTAINERS` clause
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) for detailed information about container data objects

**Parent topic:** Querying Across Containers with the CONTAINERS Clause

### 45.11 Determining the Current Container ID or Name

You can determine your current container ID or container name in a CDB.

To determine the current container ID:

- Run the following SQL\*Plus command:
	```
	SHOW CON_ID
	```

To determine the current container name:

- Run the following SQL\*Plus command:
	```
	SHOW CON_NAME
	```

In addition, you can use the functions listed in Table 45-3 to determine the container ID of a container.

Table 45-3 Functions That Return the Container ID of a Container

| Function | Description |
| --- | --- |
| `CON_NAME_TO_ID` ('container\_name') | Returns the container ID based on the container's name. |
| `CON_DBID_TO_ID` (container\_dbid) | Returns the container ID based on the container's DBID. |
| `CON_UID_TO_ID` (container\_uid) | Returns the container ID based on the container's unique identifier (UID). |
| `CON_GUID_TO_ID` (container\_guid) | Returns the container ID based on the container's globally unique identifier (GUID). |

The `V$CONTAINERS` view shows the name, DBID, UID, and GUID for each container in a CDB.

Example 45-13 Returning the Container ID Based on the Container Name

```
SELECT CON_NAME_TO_ID('HRPDB') FROM DUAL;
```

Example 45-14 Returning the Container ID Based on the Container DBID

```
SELECT CON_DBID_TO_ID(2226957846) FROM DUAL;
```

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.12 Listing the Initialization Parameters That Are Modifiable in PDBs

In a CDB, some initialization parameters apply to the root and to all of the PDBs. When such an initialization parameter is changed, it affects the entire CDB. You can set other initialization parameters to different values in each container.

For example, you might have a parameter set to one value in the root, set to another value in one PDB, and set to yet another value in a second PDB.

The query in this section lists the initialization parameters that you can set independently in each PDB.

To list the initialization parameters that are modifiable in each container:

1. In SQL\*Plus, access a container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Run the following query:
	```
	SELECT NAME FROM V$SYSTEM_PARAMETER
	  WHERE ISPDB_MODIFIABLE = 'TRUE'
	  ORDER BY NAME;
	```

If an initialization parameter listed by this query is not set independently for a PDB, then the PDB inherits the parameter value of the root.

See Also:

- " [Using the ALTER SYSTEM SET Statement in a CDB](administering-a-cdb-with-sql-plus.md) "
- " [Using the ALTER SYSTEM Statement to Modify a PDB](administering-pdbs-with-sql-plus.md) "

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.13 Viewing the History of PDBs

The `CDB_PDB_HISTORY` view shows the history of the PDBs in a CDB. It provides information about when and how each PDB was created and other information about each PDB's history.

To view the history of each PDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query `CDB_PDB_HISTORY` view.

Example 45-15 Viewing the History of PDBs

This example shows the following information about each PDB's history:

- The `DB_NAME` field shows the CDB that contained the PDB.
- The `CON_ID` field shows the container ID of the PDB.
- The `PDB_NAME` field shows the name of the PDB in one of its incarnations.
- The `OPERATION` field shows the operation performed in the PDB's history.
- The `OP_TIMESTAMP` field shows the date on which the operation was performed.
- If the PDB was cloned in an operation, then the `CLONED_FROM_PDB` field shows the PDB from which the PDB was cloned.
```
COLUMN DB_NAME FORMAT A10
COLUMN CON_ID FORMAT 999
COLUMN PDB_NAME FORMAT A15
COLUMN OPERATION FORMAT A16
COLUMN OP_TIMESTAMP FORMAT A10
COLUMN CLONED_FROM_PDB_NAME FORMAT A15
 
SELECT DB_NAME, CON_ID, PDB_NAME, OPERATION, OP_TIMESTAMP, CLONED_FROM_PDB_NAME
  FROM CDB_PDB_HISTORY
  WHERE CON_ID > 2
  ORDER BY CON_ID;
```

Sample output:

```
DB_NAME    CON_ID PDB_NAME        OPERATION        OP_TIMESTA CLONED_FROM_PDB
---------- ------ --------------- ---------------- ---------- ---------------
NEWCDB          3 HRPDB           CREATE           10-APR-12  PDB$SEED
NEWCDB          4 SALESPDB        CREATE           17-APR-12  PDB$SEED
NEWCDB          5 TESTPDB         CLONE            30-APR-12  SALESPDB
```

Note:

When the current container is a PDB, the `CDB_PDB_HISTORY` view shows the history of the current PDB only. A local user whose current container is a PDB can query the `DBA_PDB_HISTORY` view and exclude the `CON_ID` column from the query to view the history of the current PDB.

See Also:

" [About the Current Container](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

### 45.14 Viewing Information About Applications in Application Containers

Several views provide information about the applications in application containers in a CDB.

- Viewing Information About Applications  
	The `DBA_APPLICATIONS` view provides information about the applications in an application container.
- Viewing Information About Application Status  
	The `DBA_APP_PDB_STATUS` view provides information about the status of the applications in an application container. It can show the status of each application in each application PDB.
- Viewing Information About Application Statements  
	The `DBA_APP_STATEMENTS` view provides information about SQL statements issued during application installation, upgrade, and patch operations
- Viewing Information About Application Versions  
	The `DBA_APP_VERSIONS` view provides information about the versions for applications in an application container.
- Viewing Information About Application Patches  
	The `DBA_APP_PATCHES` view provides information about the patches for applications in an application container.
- Viewing Information About Application Errors  
	The `DBA_APP_ERRORS` view provides information errors raised when an application PDB synchronizes with an application in the application root. An application PDB issues the `ALTER PLUGGABLE DATABASE APPLICATION` statement with the `SYNC` clause.
- Listing the Shared Database Objects in an Application Container  
	The `DBA_OBJECTS` view can list the shared database objects in an application container. Shared database objects are metadata-linked application common objects, data-linked application common objects, and extended data-linked application common objects.
- Listing the Extended Data-Linked Objects in an Application Container  
	The `DBA_TABLES` and `DBA_VIEWS` views can list the extended data-linked objects in an application container.

**Parent topic:** Viewing Information About CDBs and PDBs with SQL\*Plus

#### 45.14.1 Viewing Information About Applications

The `DBA_APPLICATIONS` view provides information about the applications in an application container.

Note:

The `DBA_APPLICATIONS` view provides information about the application in the current container only. To view information about applications in all of the application PDBs in the current application container, query the `DBA_APP_PDB_STATUS` with the application root as the current container.

To view information about the applications in an application container:

1. In SQL\*Plus, access the application root of the application container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_APPLICATIONS` view.

Example 45-16 Viewing Details About the Applications in an Application Container

This query shows the name, the latest version, and the status of each user-created application in the application container.

```
COLUMN APP_NAME FORMAT A15
COLUMN APP_VERSOIN FORMAT A15
COLUMN APP_STATUS FORMAT A15
 
SELECT APP_NAME, APP_VERSION, APP_STATUS
  FROM DBA_APPLICATIONS
  WHERE APP_IMPLICIT='N';
```

Your output is similar to the following:

```
APP_NAME        APP_VERSION                    APP_STATUS
--------------- ------------------------------ ---------------
SALESAPP        1.2                            NORMAL
```

Note:

Oracle Database creates some applications implicitly when an application common user operation is issued with a `CONTAINER=ALL` clause outside of `ALTER PLUGGABLE DATABASE APPLICATION BEGIN/END` statements. The sample query excludes implicitly-created applications by specifying `APP_IMPLICIT='N'` in the `WHERE` clause.

#### 45.14.2 Viewing Information About Application Status

The `DBA_APP_PDB_STATUS` view provides information about the status of the applications in an application container. It can show the status of each application in each application PDB.

The view can show the status of an application in an application PDB even if the application PDB is closed.

Note:

When queried from the application root, the `DBA_APP_PDB_STATUS` view provides information about the applications in all of the application PDBs in the current application container. To view information about the application in the current container only, query the `DBA_APPLICATIONS` view.

To view information about the application status in an application container:

1. In SQL\*Plus, access the application root of the application container.
	See " [About Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_APP_PDB_STATUS` view.

Example 45-17 Viewing Information About Application Status

This query shows the name of the application PDB, the name of the application, the version number of the application, and the status of the application.

```
COLUMN PDB_NAME FORMAT A15
COLUMN APP_NAME FORMAT A15
COLUMN APP_VERSION FORMAT A20
COLUMN APP_STATUS FORMAT A12
 
SELECT p.PDB_NAME, s.APP_NAME, s.APP_VERSION, s.APP_STATUS
  FROM DBA_PDBS p, DBA_APP_PDB_STATUS s
  WHERE p.CON_UID = s.CON_UID;
```

Your output is similar to the following:

```
PDB_NAME        APP_NAME        APP_VERSION          APP_STATUS
--------------- --------------- -------------------- ------------
SALES1          SALESAPP        4.2                  NORMAL
```

Note:

The status of an application can be `NORMAL` in an application PDB even when the application has not been synchronized to the latest version. Other statuses might indicate that an operation is in progress or that an operation encountered a problem. For example, the status `UPGRADING` might indicate that an upgrade of the application is in progress in the application PDB, or it might indicate that an error was encountered when the application PDB tried to upgrade an application.

#### 45.14.3 Viewing Information About Application Statements

The `DBA_APP_STATEMENTS` view provides information about SQL statements issued during application installation, upgrade, and patch operations

Oracle Database records all of the SQL statements issued during application installation, upgrade, and patch operations, and you can view the history of these statements by querying the `DBA_APP_STATEMENTS` view.

To view information about the SQL statements issued during application operations:

1. In SQL\*Plus, access the application root of the application container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_APP_STATEMENTS` view.

Example 45-18 Viewing Information About Application Statements

This query shows the statement ID, capture time, SQL statement, and application name for the SQL statements for applications in the application container.

```
SET LONG  8000
SET PAGES 8000
COLUMN STATEMENT_ID FORMAT NNNNN
COLUMN CAPTURE_TIME FORMAT A12
COLUMN APP_STATEMENT FORMAT A36
COLUMN APP_NAME FORMAT A15
 
SELECT STATEMENT_ID, CAPTURE_TIME, APP_STATEMENT, APP_NAME
  FROM DBA_APP_STATEMENTS
  ORDER BY STATEMENT_ID;
```

Your output is similar to the following:

```
STATEMENT_ID CAPTURE_TIME APP_STATEMENT                        APP_NAME
------------ ------------ ------------------------------------ ---------------
           1 30-AUG-15    SYS                                  APP$1E87C094764
                                                               1142FE0534018F8
                                                               0AA6C5
           2 30-AUG-15    ALTER PLUGGABLE DATABASE APPLICATION APP$1E87C094764
                           APP$CON BEGIN INSTALL '1.0'         1142FE0534018F8
                                                               0AA6C5
           3 30-AUG-15    ALTER PLUGGABLE DATABASE APPLICATION APP$1E87C094764
                           APP$CON END INSTALL '1.0'           1142FE0534018F8
                                                               0AA6C5
           4 30-AUG-15    SYS                                  SALESAPP
           5 30-AUG-15    ALTER PLUGGABLE DATABASE APPLICATION SALESAPP
                           salesapp BEGIN INSTALL '1.0'
           6 30-AUG-15    CREATE TABLE oe.cmtb SHARING=METADAT SALESAPP
                          A (
                             value   VARCHAR2(30),
                             country VARCHAR2(30))
           7 30-AUG-15    CREATE TABLE conmap (                SALESAPP
                              country VARCHAR2(30) NOT NULL)
                          PARTITION BY LIST (country) (
                          PARTITION AMER VALUES ('US','MEXICO'
                          ,'CANADA'),
                          PARTITION EURO VALUES ('UK','FRANCE'
                          ,'GERMANY'),
                          PARTITION ASIA VALUES ('INDIA','CHIN
                          A','JAPAN'))
           8 30-AUG-15    ALTER TABLE oe.cmtb ENABLE CONTAINER SALESAPP
                          _MAP
           9 30-AUG-15    ALTER PLUGGABLE DATABASE APPLICATION SALESAPP
                           salesapp END INSTALL '1.0'
.
.
.
```

Note:

Oracle Database creates some applications implicitly when an application common user operation is issued with a `CONTAINER=ALL` clause outside of `ALTER PLUGGABLE DATABASE APPLICATION BEGIN/END` statements. The names of these applications begin with `APP$`, and the sample output shows these applications.

#### 45.14.4 Viewing Information About Application Versions

The `DBA_APP_VERSIONS` view provides information about the versions for applications in an application container.

Oracle Database records the versions for each application in an application container.

To view information about the application versions in an application container:

1. In SQL\*Plus, access the application root of the application container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_APP_VERSIONS` view.

Example 45-19 Viewing Information About Application Versions

This query shows the name of the application that was versioned, the version number, and the comment for the version.

```
COLUMN APP_NAME FORMAT A15
COLUMN APP_VERSION FORMAT A20
COLUMN APP_VERSION_COMMENT FORMAT A25
 
SELECT APP_NAME, APP_VERSION, APP_VERSION_COMMENT
  FROM DBA_APP_VERSIONS;
```

Your output is similar to the following:

```
APP_NAME        APP_VERSION          APP_VERSION_COMMENT
--------------- -------------------- -------------------------
SALESAPP        1.0                  Sales Application
```

#### 45.14.5 Viewing Information About Application Patches

The `DBA_APP_PATCHES` view provides information about the patches for applications in an application container.

Oracle Database records the patches for each application in an application container.

To view information about the application patches in an application container:

1. In SQL\*Plus, access the application root of the application container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_APP_PATCHES` view.

Example 45-20 Viewing Information About Application Patches

This query shows the name of the application that was patched, the patch number, the minimum application version for the patch, and the status of the patch for each patch in the application container.

```
COLUMN APP_NAME FORMAT A15
COLUMN PATCH_NUMBER FORMAT NNNNNNNN
COLUMN PATCH_MIN_VERSION FORMAT A10
COLUMN PATCH_STATUS FORMAT A15
 
SELECT APP_NAME, PATCH_NUMBER, PATCH_MIN_VERSION, PATCH_STATUS
  FROM DBA_APP_PATCHES;
```

Your output is similar to the following:

```
APP_NAME        PATCH_NUMBER PATCH_MIN_ PATCH_STATUS
--------------- ------------ ---------- ---------------
SALESAPP                   1 1.2        INSTALLED
```

#### 45.14.6 Viewing Information About Application Errors

The `DBA_APP_ERRORS` view provides information errors raised when an application PDB synchronizes with an application in the application root. An application PDB issues the `ALTER PLUGGABLE DATABASE APPLICATION` statement with the `SYNC` clause.

You can view the history of application errors during application synchronization by querying the `DBA_APP_ERRORS` view.

To view information about errors raised during application synchronization:

1. In SQL\*Plus, access the application root of the application container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_APP_ERRORS` view.

Example 45-21 Viewing Details About Errors Raised During Application Synchronization

This query shows the application name, the SQL statement that raised the error, the error number, and the error message for errors raised during application synchronization.

```
SET LONG  8000
SET PAGES 8000
COLUMN APP_NAME FORMAT A15
COLUMN APP_STATEMENT FORMAT A36
COLUMN ERRORNUM FORMAT NNNNNNNN
COLUMN ERRORMSG FORMAT A20

SELECT APP_NAME, APP_STATEMENT, ERRORNUM, ERRORMSG
  FROM DBA_APP_ERRORS;
```

#### 45.14.7 Listing the Shared Database Objects in an Application Container

The `DBA_OBJECTS` view can list the shared database objects in an application container. Shared database objects are metadata-linked application common objects, data-linked application common objects, and extended data-linked application common objects.

To list the shared database objects in an application container:

1. In SQL\*Plus, access the application root of the application container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_OBJECTS` view and specify the `SHARING` column.

Example 45-22 Listing the User-Created Shared Database Objects in an Application Container

This query shows the owner and name of the user-created shared database objects in the application container. It also shows whether each shared database object is a metadata-linked application common object or a data-linked application common object. The query excludes Oracle-supplied shared database objects.

```
COLUMN OWNER FORMAT A15
COLUMN OBJECT_NAME FORMAT A25
COLUMN SHARING FORMAT A13 

SELECT OWNER, OBJECT_NAME, SHARING 
   FROM DBA_OBJECTS WHERE SHARING != 'NONE' 
   AND ORACLE_MAINTAINED = 'N';
```

Your output is similar to the following:

```
OWNER           OBJECT_NAME               SHARING
--------------- ------------------------- -------------
SALESADM        CONMAP                    METADATA LINK
OE              PRODUCT_DESCRIPTIONS_OB   DATA LINK
OE              CMTB                      METADATA LINK
```

#### 45.14.8 Listing the Extended Data-Linked Objects in an Application Container

The `DBA_TABLES` and `DBA_VIEWS` views can list the extended data-linked objects in an application container.

An extended data-linked object is a special type of data-linked object for which each application PDB can create its own specific data while sharing the common data in the application root. Only the data stored in the application root is common for all application PDBs

To list the extended data-linked objects in an application container:

1. In SQL\*Plus, access the application root of the application container.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Query the `DBA_TABLES` or `DBA_VIEWS` view and specify the `EXTENDED_DATA_LINK='YES'` in the `WHERE` clause.

Example 45-23 Listing the Extended Data-Linked Tables in an Application Container

This query shows the owner and name of the extended data-linked tables in the application container.

```
COLUMN OWNER FORMAT A20
COLUMN TABLE_NAME FORMAT A30
 
SELECT OWNER, TABLE_NAME FROM DBA_TABLES WHERE EXTENDED_DATA_LINK='YES';
```

Your output is similar to the following:

```
OWNER                TABLE_NAME
-------------------- ------------------------------
SALESADM             ZIPCODES
```