---
title: DOCUMENT_LINKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5122.htm
tags:
  - oracle
  - 11g
  - reference
---

`DOCUMENT_LINKS` provides system information about Oracle XML DB document links in Oracle XML DB Repository documents. When an XML document that includes XLink or XInclude links is added to the repository, these links can be mapped to document links, which are tracked using view `DOCUMENT_LINKS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_ID` | `RAW(16)` |  | The source resource OID |
| `TARGET_ID` | `RAW(16)` |  | The target resource OID |
| `TARGET_PATH` | `VARCHAR2(4000)` |  | This column is always NULL. It is reserved for future use. |
| `LINK_TYPE` | `VARCHAR2(8)` |  | The document link type: Hard or Weak |
| `LINK_FORM` | `VARCHAR2(8)` |  | Whether the original link was of form XLink or XInclude |
| `SOURCE_TYPE` | `VARCHAR2(17)` |  | Whether the link is contained in Resource Content or Resource Metadata |

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for information about using this view