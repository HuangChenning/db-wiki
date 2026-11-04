---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_SCHEMA_ATTRIBUTES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.146 ALL\_XML\_SCHEMA\_ATTRIBUTES

`ALL_XML_SCHEMA_ATTRIBUTES` describes all the attributes and their properties accessible to the current user.

Related Views

- `DBA_XML_SCHEMA_ATTRIBUTES` describes all the attributes and their properties accessible to the current user in the database.
- `USER_XML_SCHEMA_ATTRIBUTES` describes all the attributes and their properties owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | The user who owns the attribute |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | The URL of the schema within which the attribute is defined  Refer to the See Also note below for links to more information about the `schemaurl` attribute for an XML schema. |
| `TARGET_NAMESPACE` | `VARCHAR2(2000)` |  | The namespace of the attribute |
| `ATTRIBUTE_NAME` | `VARCHAR2(2000)` |  | Name of the attribute |
| `IS_REF` | `NUMBER` |  | Indicates whether an attribute was defined using a reference in the XML schema (`1`) or not (`0`) |
| `TYPE_NAME` | `VARCHAR2(2000)` |  | Name of the type of the attribute |
| `GLOBAL` | `RAW(1)` |  | Indicates whether the attribute is global (`1`) or not (`0`) |
| `ATTRIBUTE` | `XMLTYPE` |  | Actual XMLType for the attribute |
| `ELEMENT_ID` | `RAW(20)` |  | Element ID of the element to which the attribute belongs |
| `SQL_TYPE` | `VARCHAR2(128)` |  | XDB annotation for sqlType |
| `SQL_NAME` | `VARCHAR2(128)` |  | XDB annotation value for sqlName |

See Also:

- " [DBA\_XML\_SCHEMA\_ATTRIBUTES](DBA_XML_SCHEMA_ATTRIBUTES.md) "
- " [USER\_XML\_SCHEMA\_ATTRIBUTES](USER_XML_SCHEMA_ATTRIBUTES.md) "
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-2758A6B4-2BE7-4597-94E7-F344FF7C9660) for information about registering an XML schema with Oracle XML DB
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-149CBDAE-C2DA-4D44-A1E4-30F31CD1E4C3) for information about restrictions for an XML schema URL