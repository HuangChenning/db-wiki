---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_VIEWS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_VIEWS` describes the views accessible to the current user.

Related Views

- `DBA_VIEWS` describes all views in the database.
- `USER_VIEWS` describes the views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the view |
| `VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the view |
| `TEXT_LENGTH` | `NUMBER` |  | Length of the view text |
| `TEXT` | `LONG` |  | View text. This column returns the correct value only when the row originates from the current container. The `BEQUEATH` clause will not appear as part of the `TEXT` column in this view. |
| `TEXT_VC` | `VARCHAR2(4000)` |  | View text. This column may truncate the view text. The `BEQUEATH` clause will not appear as part of the `TEXT_VC` column in this view. |
| `TYPE_TEXT_LENGTH` | `NUMBER` |  | Length of the type clause of the typed view |
| `TYPE_TEXT` | `VARCHAR2(4000)` |  | Type clause of the typed view |
| `OID_TEXT_LENGTH` | `NUMBER` |  | Length of the `WITH OID` clause of the typed view |
| `OID_TEXT` | `VARCHAR2(4000)` |  | `WITH OID` clause of the typed view |
| `VIEW_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of the view if the view is a typed view |
| `VIEW_TYPE` | `VARCHAR2(128)` |  | Type of the view if the view is a typed view |
| `SUPERVIEW_NAME` | `VARCHAR2(128)` |  | Name of the superview |
| `EDITIONING_VIEW` | `VARCHAR2(1)` |  | Reserved for future use |
| `READ_ONLY` | `VARCHAR2(1)` |  | Indicates whether the view is read-only (`Y`) or not (`N`) |
| `CONTAINER_DATA` | `VARCHAR2(1)` |  | Indicates whether the view contains container-specific data. Possible values:  - `Y` if the view was created with the `CONTAINER_DATA` clause - `N` otherwise |
| `BEQUEATH` | `VARCHAR2(12)` |  | Possible values:  - `CURRENT_USER`: When the view is a `BEQUEATH CURRENT_USER` view - `DEFINER`: When the view is a `BEQUEATH DEFINER` view  For more information about the syntax and semantics of the `BEQUEATH` clause in the SQL `CREATE VIEW` statement, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF01504). |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |
| `DEFAULT_COLLATION` | `VARCHAR2(100)` |  | Default collation for the view  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CONTAINERS_DEFAULT` | `VARCHAR2(3)` |  | Indicates whether the view is enabled for `CONTAINERS()` by default (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CONTAINER_MAP` | `VARCHAR2(3)` |  | Indicates whether the view is enabled for use with the `container_map` database property (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `EXTENDED_DATA_LINK` | `VARCHAR2(3)` |  | Indicates whether the view is enabled for fetching an extended data link from the root (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `EXTENDED_DATA_LINK_MAP` | `VARCHAR2(3)` |  | For internal use only  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_VIEWS](DBA_VIEWS.md) "
- " [USER\_VIEWS](USER_VIEWS.md) "