---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-METRICGROUP.html
tags:
  - oracle
  - 12c
  - reference
---

`V$METRICGROUP` displays information about the metric group for each of the four major Streams components: capture, propagation, apply, and queue.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_ID` | `NUMBER` | Internal ID associated with each group |
| `NAME` | `VARCHAR2(64)` | External name of the group |
| `INTERVAL_SIZE` | `NUMBER` | How often to collect statistics |
| `MAX_INTERVAL` | `NUMBER` | Total number of intervals over which statistics should be collected |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |