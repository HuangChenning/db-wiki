---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SESSION_MAX_OPEN_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.329 SESSION\_MAX\_OPEN\_FILES

Once this number is reached, subsequent attempts to open more files in the session by using `DBMS_LOB.FILEOPEN()` or `OCILobFileOpen()` will fail. The maximum value for this parameter depends on the equivalent parameter defined for the underlying operating system.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `10` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 1 to either 50 or the value of `MAX_OPEN_FILES` defined at the operating system level, whichever is less |
| Basic | No |

See Also:

- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADLOB001) for information on LOBs in general
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADLOB-GUID-D4642C92-F343-4700-9F1F-486F82249FB8) for information on BFILEs
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS66685) for information on the `DBMS_LOB.FILEOPEN()` procedure
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNOCI17193) for information on the `OCILobFileOpen()` procedure