---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_EXPRESSIONS_USAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.153 INMEMORY\_EXPRESSIONS\_USAGE

`INMEMORY_EXPRESSIONS_USAGE` controls which In-Memory Expressions (IM expressions) are populated into the In-Memory Column Store (IM column store) and are available for queries.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INMEMORY_EXPRESSIONS_USAGE = { STATIC_ONLY \| DYNAMIC_ONLY \| ENABLE \| DISABLE }` |
| Default value | `ENABLE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

The four values for this parameter are:

- `STATIC_ONLY`: Tables enabled for in-memory and containing certain data types such as Oracle numbers or JSON will have these columns populated in the IM column store using a more efficient representation. Note that this setting will increase the in-memory footprint for some tables. A static configuration enables the IM column store to cache OSON (binary JSON) columns, which are marked with an IS\_JSON check constraint. Internally, an OSON column is a hidden virtual column named `SYS_IME_OSON`. In contrast, a dynamic configuration automatically creates and populates frequently used expressions.
- `DYNAMIC_ONLY`: IM expressions will be automatically created and populated into the IM column store, if used in conjunction with PL/SQL procedure `DBMS_INMEMORY.IME_CAPTURE_EXPRESSIONS`. Note that setting this value will increase the in-memory footprint for some tables.
- `ENABLE`: Both static and dynamic IM expressions will be populated into the IM column store and available to be used by queries. Note that setting this value will increase the in-memory footprint for some tables. This is the default value.
- `DISABLE`: No IM expressions of any kind will be populated into the IM column store.

Changing the mode of a parameter does not have an immediate effect on existing in-memory data. For example, if the `inmemory_expressions_usage` clause is changed from `DYNAMIC_ONLY` to `DISABLE`, the stored IM expressions are not immediately removed. The next repopulation will not bring back the expressions in memory, thereby effectively removing the expressions.

See Also:

- " [INMEMORY\_VIRTUAL\_COLUMNS](INMEMORY_VIRTUAL_COLUMNS.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-5F82168D-A024-4F96-B3AF-7DA4C52908B8) for more information about IM expressions
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-2333DC40-794B-434B-9B1F-9A0AF8356515) for more information about the `DBMS_INMEMORY` PL/SQL package