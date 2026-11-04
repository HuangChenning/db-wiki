---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USE_LARGE_PAGES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.378 USE\_LARGE\_PAGES

`USE_LARGE_PAGES` is used to manage the database's use of large pages for SGA memory.

Note:

This parameter is applicable only on the Linux operating system. However, setting this parameter to `FALSE` can cause performance degradation on any platform.

The exception is when `USE_LARGE_PAGES` is set to `FALSE` automatically in an Oracle ASM instance because `MEMORY_TARGET` is enabled (set to a non-zero value). In this case, the `FALSE` setting does not cause performance degradation.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `USE_LARGE_PAGES = { TRUE \| FALSE \| AUTO \| ONLY \| AUTO_ONLY }` |
| Default value | `ONLY` for Exadata Database Service in the cloud, Base Database Service in the cloud, and databases created using Exadata automation tools such as Oracle Exadata Deployment Assistant (OEDA) and OEDA Command Line Utility (OEDACLI)  `AUTO_ONLY` for all other Exadata systems  `TRUE` for all other systems |
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
	In Oracle Database 11g Release 2 (11.2.0.3) and later releases, Oracle allocates as much of the SGA as it can in large pages, and if it runs out, it will allocate the rest of the SGA using regular sized pages. This can cause the instance to create additional shared memory segments for the SGA, but the total SGA size will be unchanged. In this supported mixed page mode allocation, the database will exhaust the available large pages before switching to regular sized pages.
- `FALSE`
	Specifies that the instance will not use large pages. This setting is not recommended because it can cause severe performance degradation for the instance. Although the `USE_LARGE_PAGES` initialization parameter applies only to Linux systems, setting this parameter to `FALSE` can cause performance degradation on any platform.
- `AUTO`
	Specifies that, during startup, the instance will calculate and request the number of large pages it requires. If the operating system cannot fulfill this request, then the instance will start with a combination of large and regular pages.
- `ONLY`
	Specifies that the instance will fail to start if large pages cannot be used for the entire SGA memory. Oracle recommends this setting for consistent performance. This setting is the default setting for Exadata Database Service in the cloud and Base Database Service in the cloud.
	When `USE_LARGE_PAGES` is set to `ONLY`, you must not explicitly set values for `MEMORY_TARGET` and `MEMORY_MAX_TARGET` in the initialization parameter file. Doing so will prevent the instance from starting.
- `AUTO_ONLY`
	Specifies that, during startup, the instance will calculate and request the number of large pages it requires. If the operating system can fulfill this request, then the instance will start successfully. If the operating system cannot fulfill this request, then the instance will fail to start. This ensures that no instances will run with under-provisioned large pages. This setting is available starting with Oracle Database 19c and it is the default setting for on-premises Exadata systems.

See Also:

- " [MEMORY\_TARGET](MEMORY_TARGET.md) "
- " [MEMORY\_MAX\_TARGET](MEMORY_MAX_TARGET.md) "