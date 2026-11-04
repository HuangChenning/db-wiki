---
title: BLANK_TRIMMING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams023.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |
| Basic | No |

`BLANK_TRIMMING` specifies the data assignment semantics of character datatypes.

Values:

- `TRUE`
	Allows the data assignment of a source character string or variable to a destination character column or variable even though the source length is longer than the destination length. In this case, however, the additional length over the destination length must be all blanks, else an exception condition is raised. This value complies with the semantics of SQL-92 Transitional Level and above.
- `FALSE`
	Disallows the data assignment if the source length is longer than the destination length and reverts to SQL92 Entry Level semantics.