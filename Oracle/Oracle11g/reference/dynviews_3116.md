---
title: "V$TRANSPORTABLE_PLATFORM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3116.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TRANSPORTABLE_PLATFORM` displays all platforms that support cross-platform tablespace transport. Specifically, it lists all platforms supported by the RMAN `CONVERT TABLESPACE` command, along with the endianness of each platform.

| Column | Datatype | Description |
| --- | --- | --- |
| `PLATFORM_ID` | `NUMBER` | Platform identification number |
| `PLATFORM_NAME` | `VARCHAR2(101)` | Platform name |
| `ENDIAN_FORMAT` | `VARCHAR2(14)` | Platform endian format: - `Big` - `Little` - `UNKNOWN FORMAT` |