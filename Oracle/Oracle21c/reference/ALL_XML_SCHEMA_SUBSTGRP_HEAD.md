---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_SCHEMA_SUBSTGRP_HEAD.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.151 ALL\_XML\_SCHEMA\_SUBSTGRP\_HEAD

`ALL_XML_SCHEMA_SUBSTGRP_HEAD` describes the heads of substitution groups accessible to the current user.

Related Views

- `DBA_XML_SCHEMA_SUBSTGRP_HEAD` describes the heads of substitution groups.
- `USER_XML_SCHEMA_SUBSTGRP_HEAD` describes the heads of substitution groups owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | The user who owns the element |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | The URL of the schema within which the element is defined  Refer to the See Also note below for links to more information about the `schemaurl` attribute for an XML schema. |
| `TARGET_NAMESPACE` | `VARCHAR2(2000)` |  | The namespace of the element |
| `ELEMENT_NAME` | `VARCHAR2(256)` |  | Name of the element |
| `ELEMENT` | `XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBSchema.xsd" Element "element")` |  | The actual XML fragment of the element |

See Also:

- " [DBA\_XML\_SCHEMA\_SUBSTGRP\_HEAD](DBA_XML_SCHEMA_SUBSTGRP_HEAD.md) "
- " [USER\_XML\_SCHEMA\_SUBSTGRP\_HEAD](USER_XML_SCHEMA_SUBSTGRP_HEAD.md) "
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-2758A6B4-2BE7-4597-94E7-F344FF7C9660) for information about registering an XML schema with Oracle XML DB
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-149CBDAE-C2DA-4D44-A1E4-30F31CD1E4C3) for information about restrictions for an XML schema URL