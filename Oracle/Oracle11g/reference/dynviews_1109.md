---
title: "V$DB_TRANSPORTABLE_PLATFORM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1109.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DB_TRANSPORTABLE_PLATFORM` displays all platforms to which the database can be transported using the RMAN `CONVERT DATABASE` command. The transportable database feature only supports transports of the same endian platform. Therefore, `V$DB_TRANSPORTABLE_PLATFORM` displays fewer rows than `V$TRANSPORTABLE_PLATFORM`.

| Column | Datatype | Description |
| --- | --- | --- |
| `PLATFORM_ID` | `NUMBER` | Platform identification number |
| `PLATFORM_NAME` | `VARCHAR2(101)` | Platform name |
| `ENDIAN_FORMAT` | `VARCHAR2(14)` | Platform endian format: |