---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/OBJECT_VALUE-Pseudocolumn.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## OBJECT\_VALUE Pseudocolumn

The `OBJECT_VALUE` pseudocolumn returns system-generated names for the columns of an object table, `XMLType` table, object view, or `XMLType` view. This pseudocolumn is useful for identifying the value of a substitutable row in an object table and for creating object views with the `WITH` `OBJECT` `IDENTIFIER` clause.

Note:

In earlier releases, this pseudocolumn was called `SYS_NC_ROWINFO$`. That name is still supported for backward compatibility. However, Oracle recommends that you use the more intuitive name `OBJECT_VALUE`.

See Also:

- [object\_table](CREATE-TABLE.md) and [object\_view\_clause](CREATE-VIEW.md) for more information on the use of this pseudocolumn
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADOBJ7129) for examples of the use of this pseudocolumn