---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/CONTAINERS_PARALLEL_DEGREE.html
tags:
  - oracle
  - 12c
  - reference
---

`CONTAINERS_PARALLEL_DEGREE` can be used to control the degree of parallelism of a query involving containers().

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `65535` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | Cannot be set to a value lower than `2` or higher than `65535`. |
| Basic | No |
| Oracle RAC | Different values can be set on different instances. |

The value of `CONTAINERS_PARALLEL_DEGREE`, if set, will override the default DOP for a containers() query.

By default, a containers() query uses a degree of parallelism equal to (`1` + number of open PDBs) in the case of CDB root and (`1` + number of open application PDBs) in the case of application root.

If the value of `CONTAINERS_PARALLEL_DEGREE` is lower than `65535`, then this value is used as the degree of parallelism of a query involving containers(). Otherwise (when the value is `65535`), the default degree of parallelism is (`1` + number of open PDBs) or (`1` + number of open application PDBs) as described above.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT-GUID-4311CC75-87D3-4548-A7CE-11FE5141C9E3) for more information about CDB roots
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT-GUID-CA425AC1-CA1C-498C-BC09-AD246BA67346) for more information about application roots