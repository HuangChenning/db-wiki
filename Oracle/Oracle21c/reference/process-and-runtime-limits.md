---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/process-and-runtime-limits.html
tags:
  - oracle
  - 21c
  - reference
---

## A.4 Process and Runtime Limits

This table describes limit types and limit values for process and runtime items.

| Item | Type of Limit | Limit Value |
| --- | --- | --- |
| Advanced Queuing Processes | Maximum per instance | `10` |
| Backup Sessions | Maximum per instance | Limited by the `PROCESSES` and `SESSIONS` initialization parameters, for instance |
| Dispatchers | Maximum per instance | Limited by the `PROCESSES` and `SESSIONS` initialization parameters, for instance |
| Global Cache Service Processes | Maximum per instance | `10` |
| Instances per database | Maximum number of cluster database instances per database | Operating system-dependent |
| I/O Worker Processes | Maximum per background process (DBWR, LGWR, and so on) | 15 |
| I/O Worker Processes | Maximum per Backup session | 15 |
| Job Queue Processes | Maximum per instance | `1000` |
| Locks | Distributed Lock Manager | Operating system dependent |
| Locks | Row-level | Not defined |
| Parallel Execution Workers | Maximum per instance | Limited by the `PROCESSES` and `SESSIONS` initialization parameters, for instance |
| Services | Maximum per instance | 8200 |
| Sessions | Maximum per instance | 2 <sup>18</sup> - 1, which is 262143; limited by the `PROCESSES` and `SESSIONS` initialization parameters. |
| SGA size | Maximum value | Operating system-dependent; typically `2` to `4` GB for 32-bit operating systems, and > `4` GB for 64-bit operating systems |
| Shared Servers | Maximum per instance | Limited by the `PROCESSES` and `SESSIONS` initialization parameters, for instance |