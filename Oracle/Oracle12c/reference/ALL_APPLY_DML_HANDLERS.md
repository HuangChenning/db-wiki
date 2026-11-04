---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_APPLY_DML_HANDLERS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_APPLY_DML_HANDLERS` displays information about the DML handlers on the tables accessible to the current user.

Related View

`DBA_APPLY_DML_HANDLERS` displays information about the DML handlers on all tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object on which the DML handler is specified |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object on which the DML handler is specified |
| `OPERATION_NAME` | `VARCHAR2(13)` |  | Name of the DML operation for which the DML handler is used:  - `DEFAULT` - `INSERT` - `UPDATE` - `DELETE` - `LOB_UPDATE` - `ASSEMBLE_LOBS` |
| `USER_PROCEDURE` | `VARCHAR2(98)` |  | Name of the user-specified DML handler, which handles row logical change records that contain the DML operation in the `OPERATION_NAME` column on the object |
| `ERROR_HANDLER` | `VARCHAR2(1)` |  | Indicates whether the DML handler handles only the relevant row logical change records that result in apply errors (`Y`) or all relevant row logical change records (`N`) |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |
| `APPLY_NAME` | `VARCHAR2(128)` |  | Name of the apply process for the given object |
| `ASSEMBLE_LOBS` | `VARCHAR2(1)` |  | Indicates whether LOB assembly is used for LOB columns in logical change records (LCRs) processed by the handler (`Y`) or not (`N`)  LOB assembly combines multiple LCRs for a LOB column resulting from a single row change into one row LCR before passing the LCR to the handler. |
| `SET_BY` | `VARCHAR2(10)` |  | Entity that set up the handler. Possible values include:  - `GOLDENGATE` - `USER` |

See Also:

- " [DBA\_APPLY\_DML\_HANDLERS](DBA_APPLY_DML_HANDLERS.md) "
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=STRMS379) for more information about DML handlers in an Oracle Streams environment
- [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=XSTRM72700) for more information about DML handlers in an Oracle XStream environment