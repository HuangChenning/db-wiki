---
title: DBA_OUTLINES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4168.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_OUTLINES` describes all stored outlines in the database.

Related View

`USER_OUTLINES` describes the stored outlines owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` |  | User-specified or generated name of the stored outline. The name must be of a form that can be expressed in SQL. |
| `OWNER` | `VARCHAR2(30)` |  | Name of the user who created the outline |
| `CATEGORY` | `VARCHAR2(30)` |  | User-defined name of the category to which the outline belongs |
| `USED` | `VARCHAR2(6)` |  | Indicates whether the outline has ever been used (`USED`) or not (`UNUSED`) |
| `TIMESTAMP` | `DATE` |  | Timestamp of outline creation |
| `VERSION` | `VARCHAR2(64)` |  | Oracle version that created the outline |
| `SQL_TEXT` | `LONG` |  | SQL text of the query, including any hints that were a part of the original statement. If bind variables are included, the variable names are stored as SQL text, not the values that are assigned to the variables. |
|  |  |  | Note: This field may contain sensitive information about your database or application. Therefore, use discretion when granting `SELECT` or `VIEW` object privileges on these views. |
| `SIGNATURE` | `RAW(16)` |  | Signature uniquely identifying the outline SQL text |
| `COMPATIBLE` | `VARCHAR2(12)` |  | Indicates whether the outline hints were compatible across a migration (`COMPATIBLE`) or not (`INCOMPATIBLE`) |
| `ENABLED` | `VARCHAR2(8)` |  | Indicates whether the outline is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `FORMAT` | `VARCHAR2(6)` |  | Hint format: |
| `MIGRATED` | `VARCHAR2(12)` |  | Indicates whether the outline has been migrated to a SQL plan baseline (`MIGRATED`) or not (`NOT-MIGRATED`) |

See Also:

["USER\_OUTLINES"](statviews_5384.md)