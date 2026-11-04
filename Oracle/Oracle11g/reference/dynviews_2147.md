---
title: "V$RMAN_ENCRYPTION_ALGORITHMS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2147.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RMAN_ENCRYPTION_ALGORITHMS` displays supported encryption algorithms. It is used by the RMAN client to validate user-requested algorithms. This view will list AES128, AES192, and AES256 encryption algorithms for the current release. The default algorithm is AES128.

| Column | Datatype | Description |
| --- | --- | --- |
| `ALGORITHM_ID` | `NUMBER` | Number to identify the algorithm |
| `ALGORITHM_NAME` | `VARCHAR2(64)` | Name of the algorithm (for example, AES128, AES192, or AES256) |
| `ALGORITHM_DESCRIPTION` | `VARCHAR2(64)` | Description of the algorithm |
| `IS_DEFAULT` | `VARCHAR2(3)` | Indicates whether this is the default encryption algorithm (`YES`) or not (`NO`). This value is set by Oracle Database and may vary for each Release (that is, it is not dependent on user-specified RMAN configuration). |
| `RESTORE_ONLY` | `VARCHAR2(3)` | Indicates whether this algorithm can be used for restore only (`YES`) or not (`NO`). If the value is `NO`, then the algorithm is also allowed for backup. This column is useful in determining whether an encryption algorithm is deprecated for backup purpose. |