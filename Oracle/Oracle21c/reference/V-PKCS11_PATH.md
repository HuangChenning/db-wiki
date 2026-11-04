---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PKCS11_PATH.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.122 V$PKCS11\_PATH

`V$PKCS11_PATH` displays all processes that are using a PKCS#11 library for Transparent Data Encryption (TDE).

The SQL command `ADMINISTER` `KEY` `MANAGEMENT` `SWITCHOVER` `TO` `LIBRARY` instructs the database to switch over from the current PKCS#11 library to a new PKCS#11 library, without incurring system downtime. After you issue this command, foreground and background processes are gradually switched over to the new library. You can use this view to monitor the PKCS#11 library being used by each process. When you determine that all processes have switched over to the new library, you can safely remove the old library from disk.

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | ID of the process |
| `PNAME` | `VARCHAR2(5)` | Name of the process |
| `PKCS11_LIB_PATH` | `VARCHAR2(4000)` | Full operating system path for the PKCS#11 library being used by the process |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.