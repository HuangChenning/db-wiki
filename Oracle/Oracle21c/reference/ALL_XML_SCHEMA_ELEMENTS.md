---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_SCHEMA_ELEMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.148 ALL\_XML\_SCHEMA\_ELEMENTS

`ALL_XML_SCHEMA_ELEMENTS` describes all the elements and their properties accessible to the current user.

Related Views

- `DBA_XML_SCHEMA_ELEMENTS` describes all the elements and their properties.
- `USER_XML_SCHEMA_ELEMENTS` describes all the elements and their properties owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | The user who owns the element |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | The URL of the schema within which the element is defined  Refer to the See Also note below for links to more information about the `schemaurl` attribute for an XML schema. |
| `TARGET_NAMESPACE` | `VARCHAR2(2000)` |  | The namespace of the element |
| `ELEMENT_NAME` | `VARCHAR2(2000)` |  | Name of the element |
| `IS_REF` | `NUMBER` |  | Indicates whether an attribute was defined using a reference in the XML schema (`1`) or not (`0`) |
| `TYPE_NAME` | `VARCHAR2(2000)` |  | Name of the type of the element |
| `GLOBAL` | `RAW(1)` |  | Indicates whether the attribute is global (`1`) or not (`0`) |
| `ELEMENT` | `XMLTYPE` |  | The actual XML fragment of the element |
| `SQL_INLINE` | `RAW(1)` |  | XDB annotation for sqlInline |
| `SQL_TYPE` | `VARCHAR2(128)` |  | XDB annotation value for sqlType |
| `SQL_SCHEMA` | `VARCHAR2(128)` |  | XDB annotation value for sqlSchema |
| `DEFAULT_TABLE` | `VARCHAR2(128)` |  | XDB annotation value for default table |
| `SQL_NAME` | `VARCHAR2(128)` |  | XDB annotation value for sqlName |
| `SQL_COL_TYPE` | `VARCHAR2(128)` |  | XDB annotation value for sqlColType |
| `MAINTAIN_DOM` | `RAW(1)` |  | XDB annotation for maintainDOM |
| `MAINTAIN_ORDER` | `RAW(1)` |  | XDB annotation for maintainOrder |
| `ELEMENT_ID` | `RAW(20)` |  | Unique identifier for the element |
| `PARENT_ELEMENT_ID` | `RAW(20)` |  | Identies the parent of the element |

See Also:

- " [DBA\_XML\_SCHEMA\_ELEMENTS](DBA_XML_SCHEMA_ELEMENTS.md) "
- " [USER\_XML\_SCHEMA\_ELEMENTS](USER_XML_SCHEMA_ELEMENTS.md) "
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-2758A6B4-2BE7-4597-94E7-F344FF7C9660) for information about registering an XML schema with Oracle XML DB
- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-149CBDAE-C2DA-4D44-A1E4-30F31CD1E4C3) for information about restrictions for an XML schema URL