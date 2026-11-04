---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TSDP_POLICY_FEATURE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.62 DBA\_TSDP\_POLICY\_FEATURE

`DBA_TSDP_POLICY_FEATURE` shows the Transparent Sensitive Data Protection policy security feature mapping for all the TSDP policies in the database.

At this time, only Oracle Data Redaction is supported.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | The name of the Transparent Sensitive Data Protection policy |
| `SECURITY_FEATURE` | `VARCHAR2(12)` |  | The Oracle security feature with which the Transparent Sensitive Data Protection policy is associated |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG855) for more information about using Transparent Sensitive Data Protection