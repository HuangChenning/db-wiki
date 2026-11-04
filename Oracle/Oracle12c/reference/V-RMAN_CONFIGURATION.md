---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RMAN_CONFIGURATION.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RMAN_CONFIGURATION` lists information about RMAN persistent configuration settings.

| Column | Datatype | Description |
| --- | --- | --- |
| `CONF#` | `NUMBER` | A unique key identifying this configuration record within the target database that owns it. |
| `NAME` | `VARCHAR2(65)` | The type of configuration. All options of the `CONFIGURE` command are valid types except:  - CONFIGURE EXCLUDE (described in RC\_TABLESPACE) - CONFIGURE AUXNAME (described in RC\_DATAFILE) - CONFIGURE SNAPSHOT CONTROLFILE (stored only in control file) |
| `VALUE` | `VARCHAR2(1025)` | The `CONFIGURE` command setting. Example: `RETENTION POLICY TO RECOVERY WINDOW OF 10 DAYS` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |