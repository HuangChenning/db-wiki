---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_SORT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.227 NLS\_SORT

`NLS_SORT` specifies the collating sequence for character value comparison in various SQL operators and clauses.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_SORT = { BINARY \| ` `linguistic_definition` ` }` |
| Default value | Derived from `NLS_LANGUAGE` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | `BINARY` or any valid linguistic definition name |
| Basic | No |

For example, `NLS_SORT` specifies the collating sequence for character value comparison in these SQL operators and clauses: `ORDER BY`, `GROUP BY`, comparison conditions (`=`, `<>`, `<=`, `>=`), `IN`, `BETWEEN`, `LIKE`, `MIN/MAX`, `GREATEST/LEAST`, and `INSTR`.

- If the value is `BINARY`, then comparison is based directly on byte values in the binary encoding of the character values being compared. The ordering depends on the character set of the compared values, which is either the database character set (for `VARCHAR2`, `CHAR`, `LONG`, and `CLOB`) or the national character set (for `NVARCHAR2`, `NCHAR`, and `NCLOB`).
- If the value is a named linguistic sort, then comparison is defined by this sort. A linguistic sort uses various rules to achieve ordering expected by speakers of one or more natural languages. This is usually the same ordering that is used in dictionaries and telephone directories in those languages.

The exact operators and query clauses that obey the `NLS_SORT` parameter depend on the value of the `NLS_COMP` parameter. If an operator or clause does not obey the `NLS_SORT` value, as determined by `NLS_COMP`, the collation used is `BINARY`.

The `BINARY` comparison is faster and uses less resources than any linguistic comparison but for text in a natural language, it does not provide ordering expected by users.

The value of `NLS_SORT` affects execution plans of queries. Because a standard index cannot be used as a source of values sorted in a linguistic order, an explicit sort operation must usually be performed instead of an index range scan. A functional index on the `NLSSORT` function may be defined to provide values sorted in a linguistic order and reintroduce the index range scan to the execution plan.

Note:

The value of the initialization parameter `NLS_SORT` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overriden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG230) for more information about this parameter and a current listing of values you can specify