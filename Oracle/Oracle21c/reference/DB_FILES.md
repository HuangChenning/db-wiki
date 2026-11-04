---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.83 DB\_FILES

`DB_FILES` specifies the maximum number of database files that can be opened for this database.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `200` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | Minimum: the largest among the absolute file numbers of the datafiles in the database  Maximum: operating system-dependent |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

The maximum valid value is the maximum number of files, subject to operating system constraint, that will ever be specified for the database, including files to be added by `ADD DATAFILE` statements.

If you increase the value of `DB_FILES`, then you must shut down and restart all instances accessing the database before the new value can take effect. If you have a primary and standby database, then they should have the same value for this parameter.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD816) for information on setting this parameter in an Oracle RAC environment
- Your operating system-specific Oracle documentation for the default value of this parameter