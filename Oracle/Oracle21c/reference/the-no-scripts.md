---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/the-no-scripts.html
tags:
  - oracle
  - 21c
  - reference
---

## B.3 The "NO" Scripts

These scripts are used to remove dictionary information for various optional services or components.

Table B-3 The NO Scripts

| Script Name | Needed For | Run By | Description |
| --- | --- | --- | --- |
| `catnoadt.sql` | Objects | `SYS` | Drops views and synonyms on dictionary metadata that relate to object types |
| `catnoaud.sql` | Security | `SYS` | Drops views and synonyms on auditing metadata |
| `catnoclust.sql` | Real Application Clusters | `SYS` | Drops views that are specific to Oracle Real Application Clusters (Oracle RAC) |
| `catnodrdaas.sql` | DRDA Application Server | `SYS` | Drops all DRDA Application Server objects from the database |
| `catnogwm.sql` | Global Data Services | `SYS` | Drops users, roles, and other objects created for Global Data Services. |
| `catnohs.sql` | Heterogeneous Services | `SYS` | Removes Heterogeneous Services dictionary metadata |
| `catnojav.sql` | Java | `SYS` | Drops the RDBMS Java classes and system triggers created by the `catjava.sql` script. |
| `catnoprt.sql` | Partitioning | `SYS` | Drops views and synonyms on dictionary metadata that relate to partitioned tables and indexes |
| `catnosvm.sql` | Server Manager | `SYS` | Removes Oracle7 Server Manager views and synonyms |
| `catnowrr.sql` | Database Replay | `SYS` | Main script that drops the entire schema related to Database Replay - calls the drop schema scripts for Workload Capture, Database Replay, Workload Replay, and Workload Intelligence |
| `catnowrrc.sql` | Database Replay | `SYS` | Drops the schema related to Workload Capture |
| `catnowrrp.sql` | Database Replay | `SYS` | Drops the schema related to Workload Replay |
| `catnowrrwitb.sql` | Database Replay | `SYS` | Drops the schema related to Workload Intelligence |
| `catnsnmp.sql` | Distributed management | `SYS` | Drops the DBSNMP user and SNMPAGENT role |