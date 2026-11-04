---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/dbca-exit-codes.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

The outcome of running DBCA commands in silent mode is reported as an exit code.

The following table shows the exit codes that DBCA returns to the operating system.

Table 20-1 Exit Codes for Database Configuration Assistant

| Exit Code | Description |
| --- | --- |
| 0 | Command execution successful |
| 6 | Command execution successful but with warnings |
| \-1 | Command execution failed |
| \-2 | Invalid input from user |
| \-4 | Command canceled by user |