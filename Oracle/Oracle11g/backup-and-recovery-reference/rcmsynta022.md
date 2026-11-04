---
title: EXIT
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta022.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `EXIT` command to shut down the Recovery Manager utility. This command is functionally equivalent to the [QUIT](rcmsynta029.md) command.

Prerequisites

Execute only at the RMAN prompt.

Syntax

exit::=

  
[Description of the illustration exit.gif](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/img_text/exit.htm)  

Example

Example 2-86 Exiting RMAN

This example terminates RMAN:

```
RMAN> EXIT
```