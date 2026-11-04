---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/TIMING.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
TIMI[NG] [START text | SHOW | STOP]
```

Records timing data for an elapsed period of time, lists the current timer's name and timing data, or lists the number of active timers.

Terms

```
START text
```

Sets up a timer and makes text the name of the timer. You can have more than one active timer by STARTing additional timers before STOPping the first; SQL\*Plus nests each new timer within the preceding one. The timer most recently STARTed becomes the current timer.

```
SHOW
```

Lists the current timer's name and timing data.

```
STOP
```

Lists the current timer's name and timing data, then deletes the timer. If any other timers are active, the next most recently STARTed timer becomes the current timer.

Enter TIMING with no clauses to list the number of active timers. For other information about TIMING, see SET AUTOTRACE

Usage

You can use this data to do a performance analysis on any commands or blocks run during the period.

See the SET TIMING command for information on automatically displaying timing data after each SQL command or PL/SQL block you run.

To delete all timers, use the CLEAR TIMING command.

Examples

To create a timer named SQL\_TIMER, enter

```
TIMING START SQL_TIMER
```

To list the current timer's title and accumulated time, enter

```
TIMING SHOW
```

To list the current timer's title and accumulated time and to remove the timer, enter

```
TIMING STOP
```