---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_SCHEMA_NAMESPACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.149 ALL\_XML\_SCHEMA\_NAMESPACES

`ALL_XML_SCHEMA_NAMESPACES` describes all the available namespaces accessible to the current user.

Related Views

- `DBA_XML_SCHEMA_NAMESPACES` describes all the available namespaces.
- `USER_XML_SCHEMA_NAMESPACES` describes all the available namespaces owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | User who owns the namespace |
| `TARGET_NAMESPACE` | `VARCHAR2(2000)` |  | The target namespace |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | The URL of the schema  Refer to the See Also note below for links to more information about the `schemaurl` attribute for an XML schema. |

See Also:

- " [DBA\_XML\_SCHEMA\_NAMESPACES](DBA_XML_SCHEMA_NAMESPACES.md) "
- " [USER\_XML\_SCHEMA\_NAMESPACES](USER_XML_SCHEMA_NAMESPACES.md) "
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-2758A6B4-2BE7-4597-94E7-F344FF7C9660) for information about registering an XML schema with Oracle XML DB
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-149CBDAE-C2DA-4D44-A1E4-30F31CD1E4C3) for information about restrictions for an XML schema URL