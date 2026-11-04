---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PRE_PAGE_SGA.html
tags:
  - oracle
  - 12c
  - reference
---

`PRE_PAGE_SGA` determines whether Oracle accesses the entire SGA at instance startup.

Operating system page table entries are then prebuilt for each page of the SGA.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

When this parameter is set to `true`, the database server touches the entire SGA after the instance startup. These accesses are done by a background process and are initiated after the instance startup. The accesses cause the OS to allocate memory to the SGA and populate the page tables, making the SGA memory resident and increasing database performance.

Note:

This setting does not prevent your operating system from paging or swapping the SGA after it is initially read into memory.