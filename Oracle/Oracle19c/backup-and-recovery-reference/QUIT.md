---
title: Backup and Recovery Reference
book: Oracle AI Database Backup and Recovery Reference
doc_id: E96242-15
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/QUIT.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-reference
---

## 2.29 QUIT

Purpose

Use the `QUIT` command to shut down the Recovery Manager utility. This command is functionally equivalent to the `EXIT` command.

Prerequisites

Execute only at the RMAN prompt.

Syntax

quit::=

![quit](img/quit.gif)

> QUIT
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2025, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Example

Example 2-117 Quitting RMAN

This example terminates RMAN (sample output included):

```
RMAN> QUIT
 
 
Recovery Manager complete.
```