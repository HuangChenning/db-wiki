---
title: DBA_WORKLOAD_FILTERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5093.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WORKLOAD_FILTERS` displays all the workload filters that have been defined in the current database. In Oracle Database 11g, only workload filters of type `CAPTURE` are supported.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TYPE` | `VARCHAR2(30)` |  | Type of the workload filter |
| `ID` | `VARCHAR2(40)` |  | Sequence number of the workload filter |
| `STATUS` | `VARCHAR2(6)` |  | Status of the workload filter: - `NEW` - This filter will be used by the next subsequent operation such as the next workload capture. - `IN USE` - This filter is currently being used by an operation that is in progress such as an active workload capture. - `USED` - This filter was used in the past by some operation such as a past workload capture. |
| `SET_NAME` <sup>Foot 1</sup> | `VARCHAR2(1000)` |  | Name of the filter set to which the filter belongs |
| `NAME` | `VARCHAR2(128)` |  | Name of the workload filter |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Name of the attribute on which the filter is defined |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the attribute on which the filter is defined. Wildcards such as `%` and `_` are supported if the attribute is of string type. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).