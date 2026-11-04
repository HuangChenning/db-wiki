---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-MAP_FILE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$MAP_FILE` displays a list of all file mapping structures in the shared memory of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_MAP_IDX` | `NUMBER` | Index corresponding to the file |
| `FILE_CFGID` | `VARCHAR2(256)` | Configuration ID (N/A if configuration ID is not supported) |
| `FILE_STATUS` | `VARCHAR2(7)` | Status of the mapping information:  - `VALID` - File mapping information is latest - `INVALID` - Mapping must be refreshed |
| `FILE_NAME` | `VARCHAR2(256)` | Absolute file name |
| `FILE_TYPE` | `VARCHAR2(11)` | File type:  - `DATAFILE` - `SPFILE` - `TEMPFILE` - `CONTROLFILE` - `LOGFILE` - `ARCHIVEFILE` |
| `FILE_STRUCTURE` | `VARCHAR2(9)` | File structure:  - `FILE` - `RAWVOLUME` - `RAWDEVICE` - `NONE` |
| `FILE_SIZE` | `NUMBER` | File size in HKB (half KB) |
| `FILE_NEXTS` | `NUMBER` | Number of file extents in the file (not necessarily the same as the number of file extents mapped) |
| `LIB_IDX` | `NUMBER` | Index of mapping library claiming ownership of the file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |