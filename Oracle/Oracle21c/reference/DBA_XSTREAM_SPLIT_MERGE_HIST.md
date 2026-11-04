---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_XSTREAM_SPLIT_MERGE_HIST.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.160 DBA\_XSTREAM\_SPLIT\_MERGE\_HIST

`DBA_XSTREAM_SPLIT_MERGE_HIST` displays information about past XStream automatic split and merge operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ORIGINAL_CAPTURE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the original capture process |
| `CLONED_CAPTURE_NAME` | `VARCHAR2(128)` |  | Name of the cloned capture process |
| `ORIGINAL_QUEUE_OWNER` | `VARCHAR2(128)` |  | Owner of the queue used by the original capture process |
| `ORIGINAL_QUEUE_NAME` | `VARCHAR2(128)` |  | Name of the queue used by the original capture process |
| `CLONED_QUEUE_OWNER` | `VARCHAR2(128)` |  | Owner of the queue used by the cloned capture process |
| `CLONED_QUEUE_NAME` | `VARCHAR2(128)` |  | Name of the queue used by the cloned capture process |
| `ORIGINAL_CAPTURE_STATUS` | `VARCHAR2(8)` |  | Status of the original capture process:  - `DISABLED` - `ENABLED` - `ABORTED` |
| `CLONED_CAPTURE_STATUS` | `VARCHAR2(8)` |  | Status of the cloned capture process:  - `DISABLED` - `ENABLED` - `ABORTED` |
| `ORIGINAL_XSTREAM_NAME` | `VARCHAR2(128)` |  | Name of the original XStream component that receives database changes directly from the original capture process. The component is either a progagation or a local apply process. |
| `CLONED_XSTREAM_NAME` | `VARCHAR2(128)` |  | Name of the cloned XStream component that receives database changes directly from the cloned capture process. The component is either a progagation or a local apply process. |
| `XSTREAM_TYPE` | `VARCHAR2(11)` |  | Type of the component in `ORIGINAL_XSTREAM_NAME` and `CLONED_XSTREAM_NAME`:  - `PROPAGATION` - `APPLY` |
| `RECOVERABLE_SCRIPT_ID` | `RAW(16)` |  | Unique ID of the script to split or merge operation |
| `SCRIPT_STATUS` | `VARCHAR2(12)` |  | Status of the recoverable script:  - `GENERATING` - `NOT EXECUTING` - `EXECUTING` - `EXECUTED` - `ERROR` |
| `ACTION_TYPE` | `VARCHAR2(7)` |  | type of action performed by the script:  - `SPLIT` - `MERGE` - `MONITOR` |
| `ACTION_THRESHOLD` | `VARCHAR2(40)` |  | For `SPLIT` actions, the threshold set by the split\_threshold capture process parameter. For `MERGE` actions, the threshold set by the `merge_threshold` capture process parameter. |
| `STATUS` | `VARCHAR2(16)` |  | Status of the action:  - `NOTHING TO SPLIT` - Not ready to split or does not need to split - `ABOUT TO SPLIT` - `SPLITTING` - A split is in progress - `SPLIT DONE` - A split is done - `NOTHING TO MERGE` - Not ready to merge - `ABOUT TO MERGE` - `MERGING` - A merge is in progress - `MERGE DONE` - A merge is done - `ERROR` - An error was returned during a split or merge - `NONSPLITTABLE` - The original capture is not splittable either because it is disabled, it has more than one publisher to its queue, or it has only one destination for captured messages |
| `STATUS_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time when status was last updated |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Time when the action started |
| `LAG` | `NUMBER` |  | Time (in seconds) that the cloned capture process lags behind the original capture process |
| `JOB_OWNER` | `VARCHAR2(128)` |  | Owner of the job that performs the split or merge operation |
| `JOB_NAME` | `VARCHAR2(128)` |  | Name of the job that performs the split or merge operation |
| `ERROR_NUMBER` | `NUMBER` |  | Error number if the capture process was terminated |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message if the capture process was terminated |