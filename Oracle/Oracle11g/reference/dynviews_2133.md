---
title: "V$REQDIST"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2133.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$REQDIST` lists statistics for the histogram of shared server dispatcher request times, divided into 12 buckets, or ranges of time. The time ranges grow exponentially as a function of the bucket number.

| Column | Datatype | Description |
| --- | --- | --- |
| `BUCKET` | `NUMBER` | Bucket number: `0 - 11`; the maximum time for each bucket is (`4 * 2^N)/100` seconds |
| `COUNT` | `NUMBER` | Count of requests whose total time to complete (excluding wait time) falls in this range |