---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-GOLDENGATE_CAPABILITIES.html
tags:
  - oracle
  - 12c
  - reference
---

`V$GOLDENGATE_CAPABILITIES` displays information about the usage of various Oracle GoldenGate features, as well as database features used by Oracle GoldenGate.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(22)` | Feature name. Possible values:  - `AUTOCDR` - `DBENCRYPTION` - `DBLOGREADER` - `DDLTRIGGEROPTIMIZATION` - `DELETECASCADEHINT` - `GGSESSION` - `PROCREPLICATION` - `SUPPLEMENTALLOG` - `TRANSIENTDUPLICATE` - `TRIGGERSUPPRESSION` |
| `COUNT` | `NUMBER` | Number of times the feature has been used since instance startup |
| `LAST_USED` | `DATE` | Date on which the feature was last used |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |