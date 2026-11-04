---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/READ_ONLY_OPEN_DELAYED.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.299 READ\_ONLY\_OPEN\_DELAYED

`READ_ONLY_OPEN_DELAYED` determines when datafiles in read-only tablespaces are accessed.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

Values

- `true`
	The datafiles are accessed for the first time only when an attempt is made to read data stored within them.
- `false`
	The datafiles are accessed at database open time.

You can use this parameter to speed up some operations (primarily opening the database) for very large databases when substantial portions of the database are stored in read-only tablespaces. Consider setting this parameter to `true` for such databases, especially if portions of the read-only data are stored on slow-access devices or hierarchical storage.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11382) for information on the consequences of delaying access of datafiles in read-only tablespaces