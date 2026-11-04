---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_COPY_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.88 V$BACKUP\_COPY\_DETAILS

`V$BACKUP_COPY_DETAILS` contains information about all available control file and data file copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `COPY_KEY` | `NUMBER` | Unique identifier for this data file or control file copy |
| `FILE#` | `NUMBER` | Absolute data file number |
| `NAME` | `VARCHAR2(513)` | File name of the data file copy. The maximum length of the name is dependent on your operating system. |
| `TAG` | `VARCHAR2(32)` | Data file copy tag |
| `CREATION_CHANGE#` | `NUMBER` | Data file creation change number |
| `CREATION_TIME` | `DATE` | Data file creation timestamp |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change number of the data file when the copy was made |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint timestamp of the data file when the copy was made |
| `MARKED_CORRUPT` | `NUMBER` | Number of blocks marked corrupt by this copy operation. That is, blocks that were not marked corrupted in the source data file, but were detected and marked as corrupted during the copy operation. |
| `OUTPUT_BYTES` | `NUMBER` | Total output bytes written |
| `COMPLETION_TIME` | `DATE` | Time when the copy was completed |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | Type of control file. B indicates normal copies. S indicates standby copies. |
| `KEEP` | `VARCHAR2(3)` | (`YES` \| `NO`) Indicates whether or not this backup set has a retention policy that is different than the value for the configure retention policy |
| `KEEP_UNTIL` | `DATE` | If specified, this is the date after which the backup becomes obsolete. If this column is null, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | Lists additional retention options for this backup set. Possible values are:  - `LOGS` - The logs needed to recover this backup set are kept - `NOLOGS` - The logs needed to recover this backup set are not kept |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `SPARSE_BACKUP` | `VARCHAR2(3)` | Indicates whether the file is sparse (`YES`) or not (`NO`) |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Size of backup set to display |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |