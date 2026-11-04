---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_SCHEMAS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.153 ALL\_XML\_SCHEMAS

`ALL_XML_SCHEMAS` describes the registered XML schemas accessible to the current user.

Related Views

- `DBA_XML_SCHEMAS` describes all registered XML schemas in the database.
- `USER_XML_SCHEMAS` describes the registered XML schemas owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the XML schema |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | Schema URL of the XML schema  Refer to the See Also note below for links to more information about the `schemaurl` attribute for an XML schema. |
| `LOCAL` | `VARCHAR2(3)` |  | Indicates whether the XML schema is local (`YES`) or global (`NO`) |
| `SCHEMA` | `XMLTYPE` |  | XML schema document |
| `INT_OBJNAME` | `VARCHAR2(4000)` |  | Internal database object name for the schema |
| `QUAL_SCHEMA_URL` | `VARCHAR2(865)` |  | Fully qualified schema URL |
| `HIER_TYPE` | `VARCHAR2(11)` |  | Type of hierarchy for which the schema is enabled:  - `NONE` - `RESMETADATA` - `CONTENTS` |
| `BINARY` | `VARCHAR2(3)` |  | Indicates whether the XML Schema is registered for binary encoding usage (`YES`) or not (`NO`) |
| `SCHEMA_ID` | `RAW(16)` |  | Opaque schema identifier (16 bytes) |
| `HIDDEN` | `VARCHAR2(3)` |  | Indicates whether the XML Schema has been deleted in hidden mode (`YES`) or not (`NO`) |

See Also:

- " [DBA\_XML\_SCHEMAS](DBA_XML_SCHEMAS.md) "
- " [USER\_XML\_SCHEMAS](USER_XML_SCHEMAS.md) "
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-2758A6B4-2BE7-4597-94E7-F344FF7C9660) for information about registering an XML schema with Oracle XML DB
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-149CBDAE-C2DA-4D44-A1E4-30F31CD1E4C3) for information about restrictions for an XML schema URL