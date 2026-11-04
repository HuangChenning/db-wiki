---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DOCUMENT_LINKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.186 DOCUMENT\_LINKS

`DOCUMENT_LINKS` provides system information about Oracle XML DB document links in Oracle XML DB Repository documents.

When an XML document that includes XLink or XInclude links is added to the repository, these links can be mapped to document links, which are tracked using view `DOCUMENT_LINKS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_ID` | `RAW(16)` |  | The source resource OID |
| `TARGET_ID` | `RAW(16)` |  | The target resource OID |
| `TARGET_PATH` | `VARCHAR2(4000)` |  | This column is always NULL. It is reserved for future use. |
| `LINK_TYPE` | `VARCHAR2(8)` |  | The document link type: Hard or Weak |
| `LINK_FORM` | `VARCHAR2(8)` |  | Whether the original link was of form XLink or XInclude |
| `SOURCE_TYPE` | `VARCHAR2(17)` |  | Whether the link is contained in Resource Content or Resource Metadata |

See Also:

[Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-B9EAFB57-6F16-4BD0-B664-957359B4263E) for information about using this view