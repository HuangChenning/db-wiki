---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_OUT_OF_LINE_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.145 ALL\_XML\_OUT\_OF\_LINE\_TABLES

`ALL_XML_OUT_OF_LINE_TABLES` descibes all the out of line tables connected to a given root table for the same schema accessible to the current user.

Related Views

- `DBA_XML_OUT_OF_LINE_TABLES` describes all the out of line tables connected to a given root table for the same schema in the database.
- `USER_XML_OUT_OF_LINE_TABLES` describes all the out of line tables connected to a given root table for the same schema owned by the current user. This view does not display the `TABLE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | The URL of the schema within which the out of line table is defined  Refer to the See Also note below for links to more information about the `schemaurl` attribute for an XML schema. |
| `SCHEMA_OWNER` | `VARCHAR2(128)` |  | Owner of the schema |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the out of line table |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the out of line table |

See Also:

- " [DBA\_XML\_OUT\_OF\_LINE\_TABLES](DBA_XML_OUT_OF_LINE_TABLES.md) "
- " [USER\_XML\_OUT\_OF\_LINE\_TABLES](USER_XML_OUT_OF_LINE_TABLES.md) "
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-2758A6B4-2BE7-4597-94E7-F344FF7C9660) for information about registering an XML schema with Oracle XML DB
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-149CBDAE-C2DA-4D44-A1E4-30F31CD1E4C3) for information about restrictions for an XML schema URL