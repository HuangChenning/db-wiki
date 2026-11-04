---
title: DBMS_ODCI
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_odci.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 97 DBMS\_ODCI

`DBMS_ODCI` package contains a single user function related to the use of Data Cartridges.

See Also:

- [Oracle Database Data Cartridge Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/toc.htm)

This chapter contains the following topic:

- Summary of DBMS\_ODCI Subprograms

---

## Summary of DBMS\_ODCI Subprograms

Table 97-1 DBMS\_ODCI Package Subprograms

| Subprogram | Description |
| --- | --- |
| ESTIMATE\_CPU\_UNITS Function | Returns the approximate number of CPU instructions (in thousands) corresponding to a specified time interval (in seconds) |

---

### ESTIMATE\_CPU\_UNITS Function

This function returns the approximate number of CPU instructions (in thousands) corresponding to a specified time interval (in seconds). This information can be used to associate the CPU cost with a user-defined function for the extensible optimizer.

The function takes as input the elapsed time of the user function, measures CPU units by multiplying the elapsed time by the processor speed of the machine, and returns the approximate number of CPU instructions that should be associated with the user function. For a multiprocessor machine, `ESTIMATE_CPU_UNITS` considers the speed of a single processor.

Syntax

```
DBMS_ODCI.ESTIMATE_CPU_UNITS(
   elapsed_time     NUMBER) 
  RETURN NUMBER;
```

Parameters

| Parameter | Description |
| --- | --- |
| `elapsed_time` | The elapsed time in seconds that it takes to execute a function. |

Usage Notes

When associating CPU cost with a user-defined function, use the full number of CPU units rather than the number of thousands of CPU units returned by `ESTIMATE_CPU_UNITS`; multiply the number returned by `ESTIMATE_CPU_UNITS` by 1,000.