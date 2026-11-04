---
title: DBA_REGISTRY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4210.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_REGISTRY` displays information about all components in the database that are loaded into the component registry. The component registry tracks components that can be separately loaded into the Oracle Database. When a SQL script loads the PL/SQL packages and other database objects for a component into the database, the script uses the `DBMS_REGISTRY` package to record the component name, status, and version. If scripts are used to upgrade/downgrade the dictionary elements for the component, then those scripts also use the `DBMS_REGISTRY` package to provide status and version information.

Related View

`USER_REGISTRY` displays information about the components owned by the current user that are loaded into the component registry.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMP_ID` | `VARCHAR2(30)` | `NOT NULL` | Component identifier |
| `COMP_NAME` | `VARCHAR2(255)` |  | Component name |
| `VERSION` | `VARCHAR2(30)` |  | Component version loaded |
| `STATUS` | `VARCHAR2(11)` |  | Component status: - `INVALID` - `VALID` - `LOADING` - `LOADED` - `UPGRADING` - `UPGRADED` - `DOWNGRADING` - `DOWNGRADED` - `REMOVING` - `REMOVED` |
| `MODIFIED` | `VARCHAR2(20)` |  | Time when the component was last modified |
| `NAMESPACE` | `VARCHAR2(30)` | `NOT NULL` | Component namespace |
| `CONTROL` | `VARCHAR2(30)` | `NOT NULL` | User that created the component entry |
| `SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | User that contains the objects for the component |
| `PROCEDURE` | `VARCHAR2(61)` |  | Validation procedure |
| `STARTUP` | `VARCHAR2(8)` |  | Indicates whether the component requires a startup after the upgrade (`REQUIRED`) or not |
| `PARENT_ID` | `VARCHAR2(30)` |  | Parent component identifier |

See Also:

["USER\_REGISTRY"](statviews_5412.md)