---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_SCHEMA_SIMPLE_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.150 ALL\_XML\_SCHEMA\_SIMPLE\_TYPES

`ALL_XML_SCHEMA_SIMPLE_TYPES` describes all simple types accessible to the current user.

Related Views

- `DBA_XML_SCHEMA_SIMPLE_TYPES` describes all simple types.
- `USER_XML_SCHEMA_SIMPLE_TYPES` describes all simple types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | The user who owns the type |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | The URL of the schema within which the type is defined  Refer to the See Also note below for links to more information about the `schemaurl` attribute for an XML schema. |
| `TARGET_NAMESPACE` | `VARCHAR2(2000)` |  | The namespace of the type |
| `SIMPLE_TYPE_NAME` | `VARCHAR2(256)` |  | Name of the simple type |
| `SIMPLE_TYPE` | `XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBSchema.xsd" Element "simpleType")` |  | The actual XMLType of the type |

See Also:

- " [DBA\_XML\_SCHEMA\_SIMPLE\_TYPES](DBA_XML_SCHEMA_SIMPLE_TYPES.md) "
- " [USER\_XML\_SCHEMA\_SIMPLE\_TYPES](USER_XML_SCHEMA_SIMPLE_TYPES.md) "
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-2758A6B4-2BE7-4597-94E7-F344FF7C9660) for information about registering an XML schema with Oracle XML DB
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-149CBDAE-C2DA-4D44-A1E4-30F31CD1E4C3) for information about restrictions for an XML schema URL