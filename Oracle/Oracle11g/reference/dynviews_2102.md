---
title: "V$PROCESS_MEMORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2102.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PROCESS_MEMORY` displays dynamic PGA memory usage by named component categories for each process.

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | Oracle process identifier |
| `SERIAL#` | `NUMBER` | Oracle process serial number |
| `CATEGORY` | `VARCHAR2(15)` | Category name. Categories include "SQL", "PL/SQL", "OLAP" and "JAVA". Special categories are "Freeable" and "Other". Freeable memory has been allocated to the process by the operating system, but has not been allocated to a category. "Other" memory has been allocated to a category, but not to one of the named categories. |
| `ALLOCATED` | `NUMBER` | Bytes of PGA memory allocated by the process for the category. For the "Freeable" category, it is the amount of free PGA memory eligible to be released to the operating system. |
| `USED` | `NUMBER` | Bytes of PGA memory used by the process for the category. For "Freeable", the value is zero. For "Other", the value is NULL for performance reasons. |
| `MAX_ALLOCATED` | `NUMBER` | Maximum bytes of PGA memory ever allocated by the process for the category. |