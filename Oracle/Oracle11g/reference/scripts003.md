---
title: "The \"NO\" Scripts"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/scripts003.htm
tags:
  - oracle
  - 11g
  - reference
---

The scripts in Table B-3 are used to remove dictionary information for various optional services or components.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for more information about these scripts

Table B-3 The NO Scripts

| Script Name | Needed For | Run By | Description |
| --- | --- | --- | --- |
| `catnoadt.sql` | Objects | `SYS` | Drops views and synonyms on dictionary metadata that relate to object types |
| `catnoaud.sql` | Security | `SYS` | Drops views and synonyms on auditing metadata |
| `catnohs.sql` | Heterogeneous Services | `SYS` | Removes Heterogeneous Services dictionary metadata |
| `catnoprt.sql` | Partitioning | `SYS` | Drops views and synonyms on dictionary metadata that relate to partitioned tables and indexes |
| `catnosvm.sql` | Server Manager | `SYS` | Removes Oracle7 Server Manager views and synonyms |
| `catnsnmp.sql` | Distributed management | `SYS` | Drops the DBSNMP user and SNMPAGENT role |