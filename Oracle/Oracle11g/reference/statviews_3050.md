---
title: DBA_APPLY_DML_HANDLERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3050.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_APPLY_DML_HANDLERS` displays information about the DML handlers on all tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object on which the DML handler is specified |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object on which the DML handler is specified |
| `OPERATION_NAME` | `VARCHAR2(13)` |  | Name of the DML operation for which the DML handler is used: |
| `USER_PROCEDURE` | `VARCHAR2(98)` |  | Name of the user-specified DML handler, which handles row logical change records that contain the DML operation in the `OPERATION_NAME` column on the object |
| `ERROR_HANDLER` | `VARCHAR2(1)` |  | Indicates whether the DML handler handles only the relevant row logical change records that result in apply errors (`Y`) or all relevant row logical change records (`N`) |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |
| `APPLY_NAME` | `VARCHAR2(30)` |  | Name of the apply process for the given object |
| `ASSEMBLE_LOBS` | `VARCHAR2(1)` |  | Indicates whether LOB assembly is used for LOB columns in logical change records (LCRs) processed by the handler (`Y`) or not (`N`)  LOB assembly combines multiple LCRs for a LOB column resulting from a single row change into one row LCR before passing the LCR to the handler. |
| `HANDLER_NAME` | `VARCHAR2(30)` |  | Name of the apply DML handler; NULL for error and procedural handlers |
| `HANDLER_TYPE` | `VARCHAR2(17)` |  | Type of the apply DML handler: |
| `SET_BY` <sup>Foot 1</sup> | `VARCHAR2(10)` |  | Entity that set up the handler. Possible values include: |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)

See Also:

["ALL\_APPLY\_DML\_HANDLERS"](statviews_1007.md)