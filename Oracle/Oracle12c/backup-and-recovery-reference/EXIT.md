---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/EXIT.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

Purpose

Use the `EXIT` command to shut down the Recovery Manager utility. This command is functionally equivalent to the [QUIT](QUIT.md) command.

Prerequisites

Execute only at the RMAN prompt.

Syntax

exit::=

![exit](img/exit.gif)

> EXIT


Example

Example 2-99 Exiting RMAN

This example terminates RMAN:

```
RMAN> EXIT
```