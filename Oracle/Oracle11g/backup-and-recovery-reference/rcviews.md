---
title: Recovery Catalog Views
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

## 5 Recovery Catalog Views

This chapter contains descriptions of recovery catalog views. You can only access these views if you have created a recovery catalog (see `CREATE CATALOG`). For a summary of the recovery catalog views, refer to ["Summary of RMAN Recovery Catalog Views"](rcviews001.md).

Note:

These views are not normalized, but are optimized for RMAN and Enterprise Manager usage. Hence, most catalog views have redundant values that result from joining of several underlying tables.

The views intended for use by Enterprise Manager are generally less useful for direct querying than the other views.