---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/cdb_-views.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.4 CDB\_\* Views

For every DBA\_\* view, a CDB\_\* view is defined. In the root of a multitenant container database (CDB), CDB\_\* views can be used to obtain information about tables, tablespaces, users, privileges, parameters, and so on contained in the root and in pluggable databases (PDBs).

The CDB\_\* views can be queried only by users with the `SYSDBA` system privilege or `SELECT ANY DICTIONARY` privilege, or `SELECT_CATALOG_ROLE` role, or by users with direct privileges granted to them.

CDB\_\* views are container data objects. When a user connected to the root queries a CDB\_\* view, the query results will depend on the `CONTAINER_DATA` attribute for users for the view. The `CONTAINER_DATA` clause of the SQL `ALTER USER` statement is used to set and modify users' `CONTAINER_DATA` attribute.

The CDB\_\* views are owned by `SYS`, regardless of who owns the underlying DBA\_\* view.

By default, a user connected to the root will only see data pertaining to the root.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG803) for more information about container data objects
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF55681) for more information about the `CONTAINER_DATA` clause for the SQL `ALTER USER` statement

CDB\_\* views include these hidden columns:

- `CON$NAME`: This column includes the name of the container whose data a given CDB\_\* row represents
- `CDB$NAME`: This column displays the name of the CDB whose data a given CDB\_\* row represents

In a PDB, the CDB\_\* views only show objects visible through a corresponding DBA\_\* view.

In addition to all the columns found in a given DBA\_\* view, the corresponding CDB\_\* view also contains the `CON_ID` column, which identifies a container whose data a given CDB\_\* row represents. In a non-CDB, the value of a `CON_ID` column will be `0`.

CDB views can return data from different containers in a CDB when queried from the root container. These objects will implicitly convert data to the character set of the root container (AL32UTF8) and then return the result to the user. Some character sets may have character expansion (more bytes needed to represent a character) when converted to AL32UTF8, so there may be data truncation if the view column width is not able to accommodate data from a given PDB.

Data is returned by these views from all open PDBs at the time the query is issued, except for PDBs that are open in RESTRICTED mode. In an Oracle RAC environment, data returned by these views may vary according to the instance to which a session is connected.