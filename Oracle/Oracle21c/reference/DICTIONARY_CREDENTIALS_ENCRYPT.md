---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DICTIONARY_CREDENTIALS_ENCRYPT.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.184 DICTIONARY\_CREDENTIALS\_ENCRYPT

`DICTIONARY_CREDENTIALS_ENCRYPT` indicates whether encryption of dictionary credentials is enforced or not. You can encrypt sensitive credential information, such as passwords that are stored in the data dictionary.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ENFORCEMENT` | `VARCHAR2(8)` |  | Enforcement status for encryption of dictionary credentials. Possible values:  - `ENABLED`: Encryption of dictionary credentials is enforced - `DISABLED`: Encryption of dictionary credentials is not enforced |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-F9451BB4-8BF5-4E0B-8C49-8CE9C0C4AB1F) for information about encrypting sensitive credential information in the data dictionary