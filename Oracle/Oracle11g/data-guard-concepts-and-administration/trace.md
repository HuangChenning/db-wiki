---
title: Setting Archive Tracing
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/trace.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## F Setting Archive Tracing

The Oracle database uses the `LOG_ARCHIVE_TRACE` parameter to enable and control the generation of comprehensive trace information for log archiving and redo transport activity. This tracing information is written to the Automatic Diagnostic Repository.

This appendix contains the following sections:

- Setting the LOG\_ARCHIVE\_TRACE Initialization Parameter
- Choosing an Integer Value

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about the Automatic Diagnostic Repository

## F.1 Setting the LOG\_ARCHIVE\_TRACE Initialization Parameter

The format for the archiving trace parameter is as follows, where trace\_level is an integer:

```
LOG_ARCHIVE_TRACE=trace_level
```

To enable, disable, or modify the `LOG_ARCHIVE_TRACE` parameter, issue a SQL statement similar to the following:

```
SQL> ALTER SYSTEM SET LOG_ARCHIVE_TRACE=15;
```

In the previous example, setting the `LOG_ARCHIVE_TRACE` parameter to a value of 15 sets trace levels 1, 2, 4, and 8 as described in Section F.2.

## F.2 Choosing an Integer Value

The integer values for the `LOG_ARCHIVE_TRACE` parameter represent levels of tracing data. In general, the higher the level, the more detailed the information. The following integer levels are available:

| Level | Meaning |
| --- | --- |
| 0 | Disables archived redo log tracing (default setting) |
| 1 | Tracks archiving of log files |
| 2 | Tracks archive status by archive log file destination |
| 4 | Tracks archive operational phase |
| 8 | Tracks archive log destination activity |
| 16 | Tracks detailed archive log destination activity |
| 32 | Tracks archive log destination parameter modifications |
| 64 | Tracks ARCn process state activity |
| 128 | Tracks FAL server process activity |
| 256 | Tracks RFS Logical Client |
| 512 | Tracks LGWR redo shipping network activity |
| 1024 | Tracks RFS physical client |
| 2048 | Tracks RFS/ARCn ping heartbeat |
| 4096 | Tracks real-time apply activity |
| 8192 | Tracks Redo Apply activity (media recovery or physical standby) |
| 16384 | Tracks archive I/O buffers |
| 32768 | Tracks LogMiner dictionary archiving |

You can combine tracing levels by setting the value of the `LOG_ARCHIVE_TRACE` parameter to the sum of the individual levels. For example, setting the parameter to 6 generates level 2 and level 4 trace output.

The following are examples of the ARC0 trace data generated on the primary site by the archiving of log file 387 to two different destinations: the service `standby1` and the local directory `/oracle/dbs`.

Note:

The level numbers do not appear in the actual trace output; they are shown here for clarification only.
```
Level   Corresponding entry content (sample) 
-----   -------------------------------- 
( 1)    ARC0: Begin archiving log# 1 seq# 387 thrd# 1 
( 4)    ARC0: VALIDATE 
( 4)    ARC0: PREPARE 
( 4)    ARC0: INITIALIZE 
( 4)    ARC0: SPOOL 
( 8)    ARC0: Creating archive destination 2 : 'standby1' 
(16)    ARC0:  Issuing standby Create archive destination at 'standby1' 
( 8)    ARC0: Creating archive destination 1 : '/oracle/dbs/d1arc1_387.log' 
(16)    ARC0:  Archiving block 1 count 1 to : 'standby1' 
(16)    ARC0:  Issuing standby Archive of block 1 count 1 to 'standby1' 
(16)    ARC0:  Archiving block 1 count 1 to :  '/oracle/dbs/d1arc1_387.log' 
( 8)    ARC0: Closing archive destination 2  : standby1 
(16)    ARC0:  Issuing standby Close archive destination at 'standby1' 
( 8)    ARC0: Closing archive destination 1  :  /oracle/dbs/d1arc1_387.log 
( 4)    ARC0: FINISH 
( 2)    ARC0: Archival success destination 2 : 'standby1' 
( 2)    ARC0: Archival success destination 1 : '/oracle/dbs/d1arc1_387.log' 
( 4)    ARC0: COMPLETE, all destinations archived 
(16)    ARC0: ArchivedLog entry added: /oracle/dbs/d1arc1_387.log 
(16)    ARC0: ArchivedLog entry added: standby1 
( 4)    ARC0: ARCHIVED 
( 1)    ARC0: Completed archiving log# 1 seq# 387 thrd# 1 
 
(32)  Propagating archive 0 destination version 0 to version 2 
         Propagating archive 0 state version 0 to version 2 
         Propagating archive 1 destination version 0 to version 2 
         Propagating archive 1 state version 0 to version 2 
         Propagating archive 2 destination version 0 to version 1 
         Propagating archive 2 state version 0 to version 1 
         Propagating archive 3 destination version 0 to version 1 
         Propagating archive 3 state version 0 to version 1 
         Propagating archive 4 destination version 0 to version 1 
         Propagating archive 4 state version 0 to version 1 
 
(64) ARCH: changing ARC0 KCRRNOARCH->KCRRSCHED 
        ARCH: STARTING ARCH PROCESSES 
        ARCH: changing ARC0 KCRRSCHED->KCRRSTART 
        ARCH: invoking ARC0 
        ARC0: changing ARC0 KCRRSTART->KCRRACTIVE 
        ARCH: Initializing ARC0 
        ARCH: ARC0 invoked 
        ARCH: STARTING ARCH PROCESSES COMPLETE 
        ARC0 started with pid=8 
        ARC0: Archival started
```

The following is the trace data generated by the RFS process on the standby site as it receives archived redo log file 387 in directory `/stby` and applies it to the standby database:

```
level    trace output (sample) 
----    ------------------ 
( 4)      RFS: Startup received from ARCH pid 9272 
( 4)      RFS: Notifier 
( 4)      RFS: Attaching to standby instance 
( 1)      RFS: Begin archive log# 2 seq# 387 thrd# 1 
(32)      Propagating archive 5 destination version 0 to version 2 
(32)      Propagating archive 5 state version 0 to version 1 
( 8)      RFS: Creating archive destination file: /stby/parc1_387.log 
(16)      RFS:  Archiving block 1 count 11 
( 1)      RFS: Completed archive log# 2 seq# 387 thrd# 1 
( 8)      RFS: Closing archive destination file: /stby/parc1_387.log 
(16)      RFS: ArchivedLog entry added: /stby/parc1_387.log 
( 1)      RFS: Archivelog seq# 387 thrd# 1 available 04/02/99 09:40:53 
( 4)      RFS: Detaching from standby instance 
( 4)      RFS: Shutdown received from ARCH pid 9272
```