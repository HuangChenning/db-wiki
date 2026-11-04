---
title: "V$BACKUP_COPY_DETAILS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1050.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_COPY_DETAILS` contains information about all available control file and datafile copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `COPY_KEY` | `NUMBER` | Unique identifier for this datafile or control file copy |
| `FILE#` | `NUMBER` | Absolute datafile number |
| `NAME` | `VARCHAR2(513)` | File name of the datafile copy. The maximum length of the name is dependent on your operating system. |
| `TAG` | `VARCHAR2(32)` | Datafile copy tag |
| `CREATION_CHANGE#` | `NUMBER` | Datafile creation change number |
| `CREATION_TIME` | `DATE` | Datafile creation timestamp |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change number of the datafile when the copy was made |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint timestamp of the datafile when the copy was made |
| `MARKED_CORRUPT` | `NUMBER` | Number of blocks marked corrupt by this copy operation. That is, blocks that were not marked corrupted in the source datafile, but were detected and marked as corrupted during the copy operation. |
| `OUTPUT_BYTES` | `NUMBER` | Total output bytes written |
| `COMPLETION_TIME` | `DATE` | Time when the copy was completed |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | Type of control file. B indicates normal copies. S indicates standby copies. |
| `KEEP` | `VARCHAR2(3)` | (`YES` \| `NO`) Indicates whether or not this backup set has a retention policy that is different than the value for the configure retention policy |
| `KEEP_UNTIL` | `DATE` | If specified, this is the date after which the backup becomes obsolete. If this column is null, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(10)` | Lists additional retention options for this backup set. Possible values are: - `LOGS` - The logs needed to recover this backup set are kept - `NOLOGS` - The logs needed to recover this backup set are not kept |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Size of backup set to display |