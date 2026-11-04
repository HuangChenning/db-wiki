---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SQLJ_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.80 ALL\_SQLJ\_TYPES

`ALL_SQLJ_TYPES` describes the SQLJ object types accessible to the current user.

Related Views

- `DBA_SQLJ_TYPES` describes all SQLJ object types in the database.
- `USER_SQLJ_TYPES` describes the SQLJ object types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the type |
| `TYPE_OID` | `RAW(16)` | `NOT NULL` | Object identifier (OID) of the type |
| `EXTERNAL_NAME` | `VARCHAR2(4000)` |  | External class name of the type |
| `USING` | `VARCHAR2(21)` |  | Representation of the type:  - `SQLData` - `CustomDatum` - `Serializable` - `Serializable Internal` - `ORAData` |
| `TYPECODE` | `VARCHAR2(128)` |  | Typecode of the type |
| `ATTRIBUTES` | `NUMBER` |  | Number of attributes (if any) in the type |
| `METHODS` | `NUMBER` |  | Number of methods (if any) in the type |
| `PREDEFINED` | `VARCHAR2(3)` |  | Indicates whether the type is a predefined type (`YES`) or not (`NO`) |
| `INCOMPLETE` | `VARCHAR2(3)` |  | Indicates whether the type is an incomplete type (`YES`) or not (`NO`) |
| `FINAL` | `VARCHAR2(3)` |  | Indicates whether the type is a final type (`YES`) or not (`NO`) |
| `INSTANTIABLE` | `VARCHAR2(3)` |  | Indicates whether the type is an instantiable type (`YES`) or not (`NO`) |
| `SUPERTYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the supertype (NULL if type is not a subtype) |
| `SUPERTYPE_NAME` | `VARCHAR2(128)` |  | Name of the supertype (NULL if type is not a subtype) |
| `LOCAL_ATTRIBUTES` | `NUMBER` |  | Number of local (not inherited) attributes (if any) in the subtype |
| `LOCAL_METHODS` | `NUMBER` |  | Number of local (not inherited) methods (if any) in the subtype |

See Also:

- " [DBA\_SQLJ\_TYPES](DBA_SQLJ_TYPES.md) "
- " [USER\_SQLJ\_TYPES](USER_SQLJ_TYPES.md) "