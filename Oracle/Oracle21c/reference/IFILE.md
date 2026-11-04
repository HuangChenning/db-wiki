---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/IFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.147 IFILE

Use `IFILE` to embed another parameter file within the current parameter file.

| Property | Description |
| --- | --- |
| Parameter type | Parameter file |
| Syntax | `IFILE = ` `parameter_file_name` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Valid parameter filenames |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

For example:

```
IFILE = COMMON.ORA
```

You can have up to three levels of nesting. In this example, the file `COMMON.ORA` could contain a second `IFILE` parameter for the file `COMMON2.ORA`, which could contain a third `IFILE` parameter for the file `GCPARMS.ORA`. You can also include multiple parameter files in one parameter file by listing `IFILE` several times with different values:

```
IFILE = DBPARMS.ORA
IFILE = GCPARMS.ORA
IFILE = LOGPARMS.ORA
```

Note:

You must list multiple entries on contiguous lines of the parameter file.