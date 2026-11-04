---
title: "V$STREAMS_CAPTURE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3080.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STREAMS_CAPTURE` displays information about each capture process that sends LCRs to an XStream outbound server.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier of the capture process |
| `SERIAL#` | `NUMBER` | Session serial number of the capture process session |
| `CAPTURE#` | `NUMBER` | Capture process number. A capture process is an Oracle background process, prefixed by `cp`. |
| `CAPTURE_NAME` | `VARCHAR2(30)` | Name of the capture process |
| `LOGMINER_ID` | `NUMBER` | Session ID of the LogMiner session associated with the capture process |
| `STARTUP_TIME` | `DATE` | Time when the capture process was last started |
| `STATE` | `VARCHAR2(551)` | State of the capture process: - `INITIALIZING` - `CAPTURING CHANGES` - `EVALUATING RULE` - `ENQUEUING MESSAGE` - `SHUTTING DOWN` - `ABORTING` - `CREATING LCR` - `WAITING FOR DICTIONARY REDO` - `WAITING FOR REDO` - `PAUSED FOR FLOW CONTROL` - `DICTIONARY INITIALIZATION` - `WAITING` `FOR` `SUBSCRIBER` `TO` `BE` `ADDED` - `WAITING FOR BUFFERED QUEUE TO SHRINK` - `SUSPENDED FOR AUTO SPLIT/MERGE` - `WAITING` `FOR` `TRANSACTION` <sup>Foot 1</sup> - `WAITING` `FOR` `INACTIVE` `DEQUEUERS` <sup>Footref 1</sup>  See Also: [Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/xstrm_dp_views.htm#XSTRM72534) for detailed descriptions of these values |
| `TOTAL_PREFILTER_DISCARDED` | `NUMBER` | Total number of prefiltered messages discarded |
| `TOTAL_PREFILTER_KEPT` | `NUMBER` | Total number of prefiltered messages kept |
| `TOTAL_PREFILTER_EVALUATIONS` | `NUMBER` | Total number of prefilter evaluations |
| `TOTAL_MESSAGES_CAPTURED` | `NUMBER` | Total number of redo entries passed by LogMiner to the capture process for detailed rule evaluation since the capture process last started. A capture process converts a redo entry into a message and performs detailed rule evaluation on the message when capture process prefiltering cannot discard the change. |
| `CAPTURE_TIME` | `DATE` | Time when the most recent message was captured |
| `CAPTURE_MESSAGE_NUMBER` | `NUMBER` | Number of the most recently captured message |
| `CAPTURE_MESSAGE_CREATE_TIME` | `DATE` | Creation time of the most recently captured message |
| `TOTAL_MESSAGES_CREATED` | `NUMBER` | Count associated with `ELAPSED_LCR_TIME` to calculate rate |
| `TOTAL_FULL_EVALUATIONS` | `NUMBER` | Count associated with `ELAPSED_RULE_TIME` to calculate rate |
| `TOTAL_MESSAGES_ENQUEUED` | `NUMBER` | Total number of messages enqueued since the capture process was last started |
| `ENQUEUE_TIME` | `DATE` | Time when the last message was enqueued |
| `ENQUEUE_MESSAGE_NUMBER` | `NUMBER` | Number of the last enqueued message |
| `ENQUEUE_MESSAGE_CREATE_TIME` | `DATE` | Creation time of the last enqueued message |
| `AVAILABLE_MESSAGE_NUMBER` | `NUMBER` | For local capture, the last redo SCN flushed to the logfiles. For downstream capture, the last SCN added to LogMiner via the archive logs. |
| `AVAILABLE_MESSAGE_CREATE_TIME` | `DATE` | For local capture, the time the SCN was written to the logfile. For downstream capture, the time the most recent archive log (containing the most recent SCN) was added to LogMiner. |
| `ELAPSED_CAPTURE_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) scanning for changes in the redo log since the capture process was last started |
| `ELAPSED_RULE_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) evaluating rules since the capture process was last started |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) enqueuing messages since the capture process was last started |
| `ELAPSED_LCR_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) creating logical change records (LCRs) since the capture process was last started |
| `ELAPSED_REDO_WAIT_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) spent by the capture process in the `WAITING FOR REDO` state |
| `ELAPSED_PAUSE_TIME` | `NUMBER` | Elapsed flow control pause time (in hundredths of a second) |
| `STATE_CHANGED_TIME` | `DATE` | Time at which the state of the capture process changed |
| `APPLY_NAME` | `VARCHAR2(30)` | Reserved for internal use |
| `APPLY_DBLINK` | `VARCHAR2(128)` | Reserved for internal use |
| `APPLY_MESSAGES_SENT` | `NUMBER` | Reserved for internal use |
| `APPLY_BYTES_SENT` | `NUMBER` | Reserved for internal use |
| `OPTIMIZATION` | `NUMBER` | Indicates whether a capture process uses combined capture and apply (greater than zero) or a capture process does not use combined capture and apply (`0`) |
| `PURPOSE` <sup>Foot 2</sup> | `VARCHAR2(10)` | Purpose of the capture process: - `Streams` - The capture process is part of an Oracle Streams configuration - `XStream` - The capture process is part of an XStream configuration |
| `SGA_USED` <sup>Footref 2</sup> | `NUMBER` | The total amount of shared memory (in bytes) currently used by the capture process out of the amount allocated (`SGA_ALLOCATED`) |
| `SGA_ALLOCATED` <sup>Footref 2</sup> | `NUMBER` | The total amount of shared memory (in bytes) allocated from the Streams pool for the capture process |
| `BYTES_OF_REDO_MINED` <sup>Footref 2</sup> | `VARCHAR2(64)` | The total amount of redo data mined (in bytes) since the capture process last started |
| `SESSION_RESTART_SCN` <sup>Footref 2</sup> | `VARCHAR2(64)` | The SCN from which the capture process started mining redo data when it was last started |

<sup>Footnote 1</sup> This state is available starting with Oracle Database 11g Release 2 (11.2.0.2).

<sup>Footnote 2</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

Note:

The `ELAPSED_CAPTURE_TIME`, `ELAPSED_RULE_TIME`, `ELAPSED_ENQUEUE_TIME`, `ELAPSED_LCR_TIME`, and `ELAPSED_REDO_WAIT_TIME` columns are only populated if the `TIMED_STATISTICS` initialization parameter is set to `true`, or if the `STATISTICS_LEVEL` initialization parameter is set to `TYPICAL` or `ALL`.