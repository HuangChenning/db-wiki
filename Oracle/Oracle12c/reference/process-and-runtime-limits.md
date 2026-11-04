---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/process-and-runtime-limits.html
tags:
  - oracle
  - 12c
  - reference
---

This table describes limit types and limit values for process and runtime items.

| Item | Type of Limit | Limit Value |
| --- | --- | --- |
| Instances per database | Maximum number of cluster database instances per database | Operating system-dependent |
| Locks | Row-level | Unlimited |
| Locks | Distributed Lock Manager | Operating system dependent |
| SGA size | Maximum value | Operating system-dependent; typically `2` to `4` GB for 32-bit operating systems, and > `4` GB for 64-bit operating systems |
| Advanced Queuing Processes | Maximum per instance | `10` |
| Job Queue Processes | Maximum per instance | `1000` |
| I/O Slave Processes | Maximum per background process (DBWR, LGWR, and so on) | 15 |
| I/O Slave Processes | Maximum per Backup session | 15 |
| Sessions | Maximum per instance | 2 <sup>16</sup>; limited by the `PROCESSES` and `SESSIONS` initialization parameters. 2 <sup>16</sup> is 65536. |
| Global Cache Service Processes | Maximum per instance | `10` |
| Shared Servers | Maximum per instance | Unlimited within constraints set by the `PROCESSES` and `SESSIONS` initialization parameters, for instance |
| Dispatchers | Maximum per instance | Unlimited within constraints set by `PROCESSES` and `SESSIONS` initialization parameters, for instance |
| Parallel Execution Slaves | Maximum per instance | Unlimited within constraints set by `PROCESSES` and `SESSIONS` initialization parameters, for instance |
| Backup Sessions | Maximum per instance | Unlimited within constraints set by `PROCESSES` and `SESSIONS` initialization parameters, for instance |
| Services | Maximum per instance | 8200 |