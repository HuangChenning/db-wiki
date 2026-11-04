---
title: "V$PROXY_COPY_SUMMARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2109.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PROXY_COPY_SUMMARY` provides summary information about the output proxy datafile and control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_COPIES` | `NUMBER` | Number of copies created |
| `NUM_DISTINCT_COPIES` | `NUMBER` | Number of distinct copies (that contain datafiles with different checkpoints) |
| `MIN_CHECKPOINT_CHANGE#` | `NUMBER` | Minimum checkpoint change SCN |
| `MAX_CHECKPOINT_CHANGE#` | `NUMBER` | Maximum checkpoint change SCN |
| `MIN_CHECKPOINT_TIME` | `DATE` | Minimum checkpoint change time |
| `MAX_CHECKPOINT_TIME` | `DATE` | Maximum checkpoint change time |
| `OUTPUT_BYTES` | `NUMBER` | Total output bytes |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |