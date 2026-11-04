---
title: "V$DB_PIPES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1108.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DB_PIPES` displays the pipes that are currently represented in the shared pool for this instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNERID` | `NUMBER` | Owner ID of the owner (if this is a private pipe), else NULL |
| `NAME` | `VARCHAR2(1000)` | Name of the pipe (for example, `SCOTT.PIPE`) |
| `TYPE` | `VARCHAR2(7)` | Type of the pipe: |
| `PIPE_SIZE` | `NUMBER` | Amount of memory the pipe uses  Note: The value of this column may be larger than `maxpipesize` because of an internal algorithm. |