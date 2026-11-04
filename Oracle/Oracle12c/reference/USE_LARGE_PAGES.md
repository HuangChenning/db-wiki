---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USE_LARGE_PAGES.html
tags:
  - oracle
  - 12c
  - reference
---

`USE_LARGE_PAGES` is used to manage the database's use of large pages for SGA memory.

Note:

This parameter is applicable only on the Linux operating system. However, setting this parameter to `FALSE` can cause performance degradation on any platform.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `USE_LARGE_PAGES = { TRUE \| FALSE \| ONLY }` |
| Default value | `TRUE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Multiple instances can use different values |

This parameter does not affect process-private memory allocations.

Values

These values can be specified for `USE_LARGE_PAGES`:

- `TRUE`
	Specifies that the instance can use large pages if large pages are configured on the system.
	In Oracle Database 11g Release 2 (11.2.0.2), if there are not enough large pages configured on the system, then regular sized pages will be used to allocate SGA memory. This can cause the free large pages to go unused, and the operating system can allocate a huge amount of memory to create page tables to map SGA into physical pages for the Oracle processes. This may lead to `ORA-04030` errors and severe performance degradation on an instance.
	In Oracle Database 11g Release 2 (11.2.0.3), Oracle allocates as much of the SGA as it can in large pages, and if it runs out, it will allocate the rest of the SGA using regular sized pages. This can cause the instance to create additional shared memory segments for the SGA, but the total SGA size will be unchanged. In this supported mixed page mode allocation, the database will exhaust the available large pages before switching to regular sized pages.
- `FALSE`
	Specifies that the instance will not use large pages. This setting is not recommended because it can cause severe performance degradation for the instance. Although the `USE_LARGE_PAGES` initialization parameter applies only to Linux systems, setting this parameter to `FALSE` can cause performance degradation on any platform.
- `ONLY`
	Specifies that the instance will fail to start if large pages cannot be used for the entire SGA memory.

Note:

`USE_LARGE_PAGES` is set to `FALSE` automatically in an Oracle ASM instance when `MEMORY_TARGET` is enabled. In this case, the `FALSE` setting does not cause performance degradation.

See Also:

- [Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UNXAR400) for an overview of HugePages and information on configuring HugePages