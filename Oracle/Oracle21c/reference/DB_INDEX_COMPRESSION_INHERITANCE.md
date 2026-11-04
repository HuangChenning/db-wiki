---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_INDEX_COMPRESSION_INHERITANCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.87 DB\_INDEX\_COMPRESSION\_INHERITANCE

`DB_INDEX_COMPRESSION_INHERITANCE` dictates how index creation inherits compression attributes.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_INDEX_COMPRESSION_INHERITANCE = { TABLESPACE \| TABLE \| ALL \| NONE }` |
| Default value | `NONE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

Values:

- `TABLESPACE`
	Index inheritance is based on tablespace attributes.
- `TABLE`
	Index inheritance is based on table attributes.
- `ALL`
	Index inheritance is based on table settings. However, if the table does not have default compression attributes, then index inheritance is based on tablespace attributes.
- `NONE`
	There is no index inheritance from the table or tablespace.

If the `CREATE INDEX` statement specifies compression attributes, then the value of `DB_INDEX_COMPRESSION_INHERITANCE` is ignored, and there is no inheritance from the table or tablespace. When there is table inheritance or tablespace inheritance (and the tablespace does not have an explicit index compression clause), then the following matrix is used:

| Table/Tablespace Level Compression | Inherited Compression for Index |
| --- | --- |
| `OLTP` | `ADVANCED` `LOW` |
| `QUERY` `LOW`, `QUERY` `HIGH` | `ADVANCED` `HIGH` |
| `ARCHIVE` `LOW`, `ARCHIVE` `HIGH` | `ADVANCED` `HIGH` |

Note:

The value of `DB_INDEX_COMPRESSION_INHERITANCE` is ignored when creating an index owned by `SYS`. Such indexes do not inherit index compression attributes from tables or tablespaces. If you want to compress an index owned by `SYS`, you must explicitly specify the index compression attributes in the `CREATE` `INDEX` or `ALTER` `INDEX` statement.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN14308) for more information about index compression