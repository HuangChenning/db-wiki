---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DML_LOCKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.114 DML\_LOCKS

`DML_LOCKS` specifies the maximum number of DML locks—one for each table modified in a transaction.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived: 4 \* `TRANSACTIONS` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 20 to unlimited; a setting of 0 disables enqueues |
| Basic | No |
| Oracle RAC | You must set this parameter for every instance, and all instances must have positive values or all must be 0. |

A DML lock is a lock obtained on a table that is undergoing a DML operation (insert, update, delete). The `DML_LOCKS` value should equal the grand total of locks on tables currently referenced by all users. For example, if three users are modifying data in one table, then three entries would be required. If three users are modifying data in two tables, then six entries would be required.

The default value assumes an average of four tables referenced for each transaction. For some systems, this value may not be enough.

Enqueues are shared memory structures that serialize access to database resources. If you set the value of `DML_LOCKS` to `0`, enqueues are disabled and performance is slightly increased. However, you should be aware of the following restrictions when you set you `DML_LOCKS` to `0`:

- You cannot use `DROP TABLE`, `CREATE INDEX` statements
- You cannot use explicit lock statements such as `LOCK TABLE IN EXCLUSIVE MODE`
- Enterprise Manager cannot run on any instances for which `DML_LOCKS` is set to `0`

Oracle holds more locks during parallel DML than during serial execution. Therefore, if your database supports a lot of parallel DML, you may need to increase the value of this parameter.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT1331) for a discussion of lock and enqueue resources needed for parallel DML
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT964) for more information on data concurrency