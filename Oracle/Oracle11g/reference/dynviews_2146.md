---
title: "V$RMAN_CONFIGURATION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2146.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RMAN_CONFIGURATION` lists information about RMAN persistent configuration settings.

| Column | Datatype | Description |
| --- | --- | --- |
| `CONF#` | `NUMBER` | A unique key identifying this configuration record within the target database that owns it. |
| `NAME` | `VARCHAR2(65)` | The type of configuration. All options of the `CONFIGURE` command are valid types except: |
| `VALUE` | `VARCHAR2(1025)` | The `CONFIGURE` command setting. Example: `RETENTION POLICY TO RECOVERY WINDOW OF 10 DAYS` |