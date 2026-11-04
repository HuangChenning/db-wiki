---
title: Backup and Recovery Reference
book: Oracle AI Database Backup and Recovery Reference
doc_id: E96242-15
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/EXIT.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-reference
---

## 2.22 EXIT

Purpose

Use the `EXIT` command to shut down the Recovery Manager utility. This command is functionally equivalent to the [QUIT](QUIT.md) command.

Prerequisites

Execute only at the RMAN prompt.

Syntax

exit::=

![exit](img/exit.gif)

> EXIT
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2025, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Example

Example 2-99 Exiting RMAN

This example terminates RMAN:

```
RMAN> EXIT
```