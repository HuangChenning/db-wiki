---
title: "V$SQL_CS_HISTOGRAM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3047.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_CS_HISTOGRAM` summarizes the monitoring information stored by adaptive cursor sharing. This information is used to decide whether to enable extended cursor sharing for a query. It is stored in a histogram, whose bucket's contents are exposed by this view.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor being monitored |
| `BUCKET_ID` | `NUMBER` | Bucket number of the monitoring histogram |
| `COUNT` | `NUMBER` | Value in this bucket of the histogram |