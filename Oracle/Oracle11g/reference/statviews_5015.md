---
title: DBA_STREAMS_SPLIT_MERGE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5015.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_SPLIT_MERGE` displays information about current automatic split and merge operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ORIGINAL_CAPTURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the original capture process |
| `CLONED_CAPTURE_NAME` | `VARCHAR2(30)` |  | Name of the cloned capture process |
| `ORIGINAL_CAPTURE_STATUS` | `VARCHAR2(8)` |  | Status of the original capture process: |
| `CLONED_CAPTURE_STATUS` | `VARCHAR2(8)` |  | Status of the cloned capture process: |
| `ORIGINAL_STREAMS_NAME` | `VARCHAR2(30)` |  | Name of the original Oracle Streams component that receives database changes directly from the original capture process. The component is either a propagation or a local apply process. |
| `CLONED_STREAMS_NAME` | `VARCHAR2(30)` |  | Name of the cloned Oracle Streams component that receives database changes directly from the cloned capture process. The component is either a propagation or a local apply process. |
| `STREAMS_TYPE` | `VARCHAR2(11)` |  | Type of the component in `ORIGINAL_STREAMS_NAME` and `CLONED_STREAMS_NAME`: - `PROPAGATION` - `APPLY` |
| `RECOVERABLE_SCRIPT_ID` | `RAW(16)` |  | Unique ID of the operation |
| `SCRIPT_STATUS` | `VARCHAR2(12)` |  | State of the recoverable script: - `GENERATING` - `NOT EXECUTED` - `EXECUTING` - `EXECUTED` - `ERROR` |
| `ACTION_TYPE` | `VARCHAR2(7)` |  | Type of action performed by the script: - `SPLIT` - `MERGE` - `MONITOR` |
| `ACTION_THRESHOLD` | `VARCHAR2(40)` |  | For `SPLIT` actions, the threshold set by the `split_threshold` capture process parameter. For `MERGE` actions, the threshold set by the `merge_threshold` capture process parameter. |
| `STATUS` | `VARCHAR2(16)` |  | Status of the action: - `NOTHING TO SPLIT` - Not ready to split or does not need to split - `ABOUT TO SPLIT` - `SPLITTING` - A split is in process - `SPLIT DONE` - A split is done - `NOTHING TO MERGE` - Not ready to merge - `ABOUT TO MERGE` - `MERGING` - A merge is in process - `MERGE DONE` - A merge is done - `ERROR` - An error was returned during a split or merge - `NONSPLITTABLE` - The original capture is not splittable either because it is disabled, it has more than one publisher to its queue, or it has only one destination for captured messages |
| `STATUS_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time when status was last updated |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Time when the action started |
| `LAG` | `NUMBER` |  | Time (in seconds) that the cloned capture process lags behind the original capture process |
| `JOB_OWNER` | `VARCHAR2(30)` |  | Owner of the job that performs the split or merge operation |
| `JOB_NAME` | `VARCHAR2(30)` |  | Name of the job that performs the split or merge operation |
| `JOB_STATE` | `VARCHAR2(15)` |  | Current state of the job: - `DISABLED` - `RETRY SCHEDULED` - `SCHEDULED` - `RUNNING` - `COMPLETED` - `BROKEN` - `FAILED` - `REMOTE` - `SUCCEEDED` - `CHAIN_STALLED` |
| `JOB_NEXT_RUN_DATE` | `VARCHAR2(64)` |  | Next time the job will run |
| `ERROR_NUMBER` | `NUMBER` |  | Error number if the capture process was aborted |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message if the capture process was aborted |