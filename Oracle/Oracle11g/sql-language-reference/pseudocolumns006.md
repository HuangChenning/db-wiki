---
title: OBJECT_VALUE Pseudocolumn
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/pseudocolumns006.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

The `OBJECT_VALUE` pseudocolumn returns system-generated names for the columns of an object table, `XMLType` table, object view, or `XMLType` view. This pseudocolumn is useful for identifying the value of a substitutable row in an object table and for creating object views with the `WITH` `OBJECT` `IDENTIFIER` clause.

Note:

In earlier releases, this pseudocolumn was called `SYS_NC_ROWINFO$`. That name is still supported for backward compatibility. However, Oracle recommends that you use the more intuitive name `OBJECT_VALUE`.

See Also:

- [object\_table](statements_7002.md) and [object\_view\_clause](statements_8004.md) for more information on the use of this pseudocolumn
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11822/adobjbas.htm#ADOBJ7129) for examples of the use of this pseudocolumn