---
title: "V$GOLDENGATE_CAPTURE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1169.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GOLDENGATE_CAPTURE` displays information about each capture process that sends LCRs to an Oracle GoldenGate outbound server.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier of the capture process |
| `SERIAL#` | `NUMBER` | Session serial number of the capture process session |
| `CAPTURE#` | `NUMBER` | Capture process number. A capture process is an Oracle background process prefixed by `cp`. |
| `CAPTURE_NAME` | `VARCHAR2(30)` | Name of the capture process |
| `LOGMINER_ID` | `NUMBER` | Session ID of the Oracle LogMiner session associated with the capture process |
| `STARTUP_TIME` | `DATE` | Time when the capture process was last started |
| `STATE` | `VARCHAR2(589)` | State of the capture process and state of the network. The two states are separated by a semicolon. The possible values are: - `INITIALIZING` - Starting up. - `WAITING FOR DICTIONARY REDO` - Waiting for redo log files containing the dictionary build related to the first SCN to be added to the capture process session. A capture process cannot begin to scan the redo log files until all of the log files containing the dictionary build have been added. - `DICTIONARY INITIALIZATION` - Processing a dictionary build. - `MINING` `(PROCESSED SCN` = scn\_value`)` - Mining a dictionary build at the SCN scn\_value. - `LOADING` (step X of Y) - Processing information from a dictionary build and currently at step X in a process that involves Y steps, where X and Y are numbers. - `CAPTURING CHANGES` - Scanning the redo log for changes that satisfy the capture process rule sets. - `WAITING FOR REDO` - Waiting for new redo log files to be added to the capture process session. The capture process has finished processing all of the redo log files added to its session. This state is possible if there is no activity at a source database. For a downstream capture process, this state is possible if the capture process is waiting for new log files to be added to its session. - `EVALUATING RULE` - Evaluating a change against a capture process rule set. - `CREATING LCR` - Converting a change into an LCR. - `ENQUEUING MESSAGE` - Enqueuing an LCR that satisfies the capture process rule sets into the capture process queue. - `PAUSED FOR FLOW CONTROL` - Unable to enqueue LCRs either because of low memory or because propagations and outbound servers are consuming messages slower than the capture process is creating them. This state indicates flow control that is used to reduce spilling of captured LCRs when propagation or apply has fallen behind or is unavailable. - `WAITING FOR THE BUFFERED QUEUE TO SHRINK` - Waiting for the buffered queue to change to a smaller size. The buffered queue shrinks when there is a memory limitation or when an administrator reduces its size. - `WAITING FOR` n `SUBSCRIBER(S) INITIALIZING` - Waiting for outbound servers that receive LCRs from the capture process to start, where n is the number of apply processes. - `WAITING FOR TRANSACTION` - Waiting for LogMiner to provide more transactions. - `WAITING FOR INACTIVE DEQUEUERS` - Waiting for the capture process's queue subscribers to start. The capture process stops enqueuing LCRs if there are no active subscribers to the queue. - `SUSPENDED FOR AUTO SPLIT/MERGE` - Waiting for a merge operation to complete. - `SHUTTING DOWN` - Stopping. - `ABORTING` - Aborting. |
| `TOTAL_PREFILTER_DISCARDED` | `NUMBER` | Total number of prefiltered messages discarded |
| `TOTAL_PREFILTER_KEPT` | `NUMBER` | Total number of prefiltered messages kept |
| `TOTAL_PREFILTER_EVALUATIONS` | `NUMBER` | Total number of prefilter evaluations |
| `TOTAL_MESSAGES_CAPTURED` | `NUMBER` | Total number of redo entries passed by LogMiner to the capture process for detailed rule evaluation since the capture process last started. A capture process converts a redo entry into a message and performs detailed rule evaluation on the message when capture process prefiltering cannot discard the change. |
| `CAPTURE_TIME` | `DATE` | Time when the most recent message was captured |
| `CAPTURE_MESSAGE_NUMBER` | `NUMBER` | Number of the most recently captured message |
| `CAPTURE_MESSAGE_CREATE_TIME` | `DATE` | Creation time of the most recently captured message |
| `TOTAL_MESSAGES_CREATED` | `NUMBER` | Count associated with ELAPSED\_LCR\_TIME to calculate rate |
| `TOTAL_FULL_EVALUATIONS` | `NUMBER` | Count associated with ELAPSED\_RULE\_TIME to calculate rate |
| `TOTAL_MESSAGES_ENQUEUED` | `NUMBER` | Total number of messages enqueued since the capture process was last started |
| `ENQUEUE_TIME` | `DATE` | Time when the last message was enqueued |
| `ENQUEUE_MESSAGE_NUMBER` | `NUMBER` | Number of the last enqueued message |
| `ENQUEUE_MESSAGE_CREATE_TIME` | `DATE` | Creation time of the last enqueued message |
| `AVAILABLE_MESSAGE_NUMBER` | `NUMBER` | For local capture, the last redo SCN flushed to the log files. For downstream capture, the last SCN added to LogMiner through the archived redo log files. |
| `AVAILABLE_MESSAGE_CREATE_TIME` | `DATE` | For local capture, the time the SCN was written to the log file. For downstream capture, the time the most recent archived redo log file (containing the most recent SCN) was added to LogMiner. |
| `ELAPSED_CAPTURE_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) scanning for changes in the redo log since the capture process was last started |
| `ELAPSED_RULE_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) evaluating rules since the capture process was last started |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) enqueuing messages since the capture process was last started |
| `ELAPSED_LCR_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) creating LCRs since the capture process was last started |
| `ELAPSED_REDO_WAIT_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) spent by the capture process in the `WAITING FOR REDO` state |
| `ELAPSED_PAUSE_TIME` | `NUMBER` | Elapsed flow control pause time (in hundredths of a second) |
| `STATE_CHANGED_TIME` | `DATE` | Time at which the state of the capture process changed |
| `SGA_USED` | `NUMBER` | The total amount of shared memory used (in bytes) by the capture process |
| `SGA_ALLOCATED` | `NUMBER` | The total amount of shared memory (in bytes) allocated from the Streams pool for the capture process |
| `BYTES_OF_REDO_MINED` | `VARCHAR2(64)` | The total amount of redo data mined (in bytes) since the capture process last started |
| `SESSION_RESTART_SCN` | `VARCHAR2(64)` | The SCN from which the capture process started mining redo data when it was last started |
| `SPID` <sup>Foot 1</sup> | `VARCHAR2(12)` | Operating system process identifier of the capture process |
| `EXTRACT_NAME` <sup>Footref 1</sup> | `VARCHAR2(30)` | Name of the extract process |
| `SERVER_SID` <sup>Footref 1</sup> | `NUMBER` | Session ID of the capture server |
| `SERVER_SERIAL#` <sup>Footref 1</sup> | `NUMBER` | Session serial number of the capture server |
| `SERVER_SPID` <sup>Footref 1</sup> | `VARCHAR2(12)` | Operating system process identifier of the capture server |
| `TOTAL_MESSAGES_SENT` <sup>Footref 1</sup> | `NUMBER` | Total number of LCRs sent by the capture process to the GoldenGate extract process since the last time the extract attached to the capture |
| `SEND_TIME` <sup>Footref 1</sup> | `DATE` | Time the last LCR was sent by the capture process to the extract process |
| `LAST_SENT_MESSAGE_NUMBER` <sup>Footref 1</sup> | `NUMBER` | Message number of the last LCR sent by the capture process to the extract process |
| `LAST_SENT_MESSAGE_CREATE_TIME` <sup>Footref 1</sup> | `DATE` | Message number of the last LCR sent by the capture process to the extract process |
| `ELAPSED_SEND_TIME` <sup>Footref 1</sup> | `NUMBER` | Time elapsed (in hundredths of a second) sending LCRs to the extract process since the last time the extract process attached to the capture process |
| `BYTES_SENT` <sup>Footref 1</sup> | `NUMBER` | Total number of bytes sent by the capture process to the extract process since the last time the extract process attached to the capture process |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)