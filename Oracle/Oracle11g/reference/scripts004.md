---
title: Upgrade and Downgrade Scripts
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/scripts004.htm
tags:
  - oracle
  - 11g
  - reference
---

The scripts in Table B-4 are used when upgrading or downgrading to another release of Oracle. To run these scripts, you must be connected to Oracle as a user with `SYSDBA` privileges.

Table B-4 Upgrade and Downgrade Scripts

| Script Name | Needed For | Description |
| --- | --- | --- |
| `catdwgrd.sql` | Downgrading | Provides a direct downgrade path from the new Oracle Database 11g release |
| `catupgrd.sql` | Upgrading | Provides a direct upgrade path to the new Oracle Database 11g release |
| `utlu112i.SQL` | Pre-Upgrade Information | Analyzes the database to be upgraded, detailing requirements and issues for the upgrade to Oracle Database 11g Release 2 (11.2) |
| `utlu112s.SQL` | Post-Upgrade Status | Displays the component upgrade status after an upgrade to Oracle Database 11g Release 2 (11.2) |

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for more information about these scripts