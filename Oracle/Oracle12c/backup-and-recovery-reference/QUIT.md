---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/QUIT.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

Purpose

Use the `QUIT` command to shut down the Recovery Manager utility. This command is functionally equivalent to the `EXIT` command.

Prerequisites

Execute only at the RMAN prompt.

Syntax

quit::=

![quit](img/quit.gif)

> QUIT


Example

Example 2-116 Quitting RMAN

This example terminates RMAN (sample output included):

```
RMAN> QUIT
 
 
Recovery Manager complete.
```