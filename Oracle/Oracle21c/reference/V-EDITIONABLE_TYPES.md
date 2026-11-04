---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EDITIONABLE_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.193 V$EDITIONABLE\_TYPES

`V$EDITIONABLE_TYPES` lists all the editionable types based on the current compatibility setting. The `SELECT` privilege on `V$EDITIONABLE_TYPES` will be granted to `PUBLIC`.

The database compatibility setting will determine the set of editionable types.

With compatibility set to 11.2 or 12, this set includes FUNCTION, LIBRARY, PACKAGE, PACKAGE BODY, PROCEDURE, SYNONYM, TRIGGER, TYPE, TYPE BODY, and VIEW. With compatibility set to 12, the set will include these types as well as the SQL TRANSLATION PROFILE.

| Column | Datatype | Description |
| --- | --- | --- |
| `EDITIONABLE_TYPE` | `VARCHAR2(64)` | The name of the type that is editionable |
| `TYPE#` | `NUMBER` | The number of the type that is editionable |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

For more information about edition-based redefinitions, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADFNS898).