---
title: USE_LARGE_PAGES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams268.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `USE_LARGE_PAGES = { TRUE \| FALSE \| ONLY }` |
| Default value | `TRUE` |
| Modifiable | No |
| Basic | No |
| Oracle RAC | Multiple instances can use different values |

`USE_LARGE_PAGES` is used to manage the database's use of large pages for SGA memory. This parameter does not affect process-private memory allocations. This parameter is applicable only on the Linux operating system.

Values:

- `TRUE`
	Specifies that the instance can use large pages if large pages are configured on the system.
	In Oracle Database 11g Release 2 (11.2.0.2), if there are not enough large pages configured on the system, then regular sized pages will be used to allocate SGA memory. This can cause the free large pages to go unused, and the operating system can allocate a huge amount of memory to create page tables to map SGA into physical pages for the Oracle processes. This may lead to `ORA-04030` errors and severe performance degradation on an instance.
	In Oracle Database 11g Release 2 (11.2.0.3), Oracle allocates as much of the SGA as it can in large pages, and if it runs out, it will allocate the rest of the SGA using regular sized pages. This can cause the instance to create additional shared memory segments for the SGA, but the total SGA size will be unchanged. In this supported mixed page mode allocation, the database will exhaust the available large pages before switching to regular sized pages.
- `FALSE`
	Specifies that the instance will not use large pages. This setting is not recommended because it can cause severe performance degradation for the instance.
- `ONLY`
	Specifies that the instance will fail to start if large pages cannot be used for the entire SGA memory.

Note:

This initialization parameter is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

- [Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/cd/E11882_01/server.112/e10839/appi_vlm.htm#UNXAR394) for an overview of HugePages and information on configuring HugePages