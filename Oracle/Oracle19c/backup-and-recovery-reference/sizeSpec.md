---
title: Backup and Recovery Reference
book: Oracle AI Database Backup and Recovery Reference
doc_id: E96242-15
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/sizeSpec.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-reference
---

## 4.19 sizeSpec

Purpose

The `sizeSpec` subclause specifies the size of the data.

Syntax

sizeSpec::=

![sizespec](img/sizespec.gif)

> integer \[ {G | K | M}\]
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2025, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

| Syntax Element | Description |
| --- | --- |
| `integer` `[G \| K \| M]` | Specifies the size of data in gigabytes (`G`), kilobytes (`K`), or megabytes (`M`). |

Examples

Example 4-36 Setting the Maximum Size of a Backup Piece

This `ALLOCATE` command specifies in the `MAXPIECESIZE` parameter that no backup piece written to tape can exceed 800 MB.

```
RUN
{
  ALLOCATE CHANNEL c1 DEVICE TYPE sbt 
    PARMS 'SBT_LIBRARY=/usr/local/oracle/backup/lib/libobk.so, 
    ENV=(OB_DEVICE_1=stape1)'
    MAXPIECESIZE 800M;
}
```