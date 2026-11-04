---
title: "MySQL :: MySQL 26.7 Reference Manual :: 4 Downgrading MySQL"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/downgrading.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## Chapter 4 Downgrading MySQL

Notes

- Make sure you understand [the MySQL release model](mysql-releases.md) for MySQL long-term support (LTS) and Innovation releases before proceeding with a downgrade.
- A replication topology is downgraded by following the rolling downgrade scheme described at [Section 19.5.3, “Upgrading or Downgrading a Replication Topology”](replication-upgrade.md), which uses one of the supported single-server methods for each individual server downgrade.
- Monthly Rapid Updates (MRUs) and hot fixes also count as releases in this documentation.

Important

Downgrading to MySQL 5.7 or earlier is not supported.