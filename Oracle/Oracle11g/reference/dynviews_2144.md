---
title: "V$RMAN_BACKUP_TYPE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2144.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RMAN_BACKUP_TYPE` displays information about RMAN backup types.

| Column | Datatype | Description |
| --- | --- | --- |
| `WEIGHT` | `NUMBER` | Used to set precedence order of different backup types in reports. |
| `INPUT_TYPE` | `VARCHAR2(13)` | Used to represent possible filters used in creating various reporting screens. |