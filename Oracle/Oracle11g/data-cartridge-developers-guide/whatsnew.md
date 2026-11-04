---
title: "What's New in Data Cartridges?"
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/whatsnew.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

This section describes the new features of Data Cartridges.

## New Features in Oracle 11g Release 1 (11.1)

New data cartridge features include:

- `MERGE` operations are now supported on tables with domain indexes. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9016.htm#SQLRF01606) for an in-depth explanation of the `MERGE` statement.
- System-partitioning of storage tables is introduced in [Chapter 8, "Building Domain Indexes"](dom_idx.md), section ["Using System Partitioning"](dom_idx.md). This approach replaces the earlier system-managed approach. Meanwhile, the differences between the system-managed and user-managed approaches is documented in [Appendix A, "User-Managed Local Domain Indexes"](user_man_idx_apnd.md).
- A related feature, system-managed partitioning of domain indexes and the associated statistics, is discussed fully in the following chapters:
	- [Chapter 8, "Building Domain Indexes"](dom_idx.md), sections ["Using System-Managed Domain Indexes"](dom_idx.md) and ["Designing System-Managed Domain Indexes"](dom_idx.md)
		- [Chapter 10, "Using Extensible Optimizer"](ext_optimizer.md) sections ["Generating Statistics for System-Managed Domain Indexes"](ext_optimizer.md) and ["Domain Index Statistics"](ext_optimizer.md)