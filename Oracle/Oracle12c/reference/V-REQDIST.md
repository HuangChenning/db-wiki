---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-REQDIST.html
tags:
  - oracle
  - 12c
  - reference
---

`V$REQDIST` lists statistics for the histogram of shared server dispatcher request times, divided into 12 buckets, or ranges of time. The time ranges grow exponentially as a function of the bucket number.

| Column | Datatype | Description |
| --- | --- | --- |
| `BUCKET` | `NUMBER` | Bucket number: `0 - 11`; the maximum time for each bucket is (`4 * 2^N)/100` seconds |
| `COUNT` | `NUMBER` | Count of requests whose total time to complete (excluding wait time) falls in this range |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |