---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/EXIT.html
tags:
  - oracle
  - 21c
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
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Example

Example 2-100 Exiting RMAN

This example terminates RMAN:

```
RMAN> EXIT
```