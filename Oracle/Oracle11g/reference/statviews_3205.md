---
title: DBA_HIST_BASELINE_TEMPLATE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3205.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_BASELINE_TEMPLATE` displays the templates used by the system for baseline generation. The system uses this information to determine which baselines should be automatically created or removed.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `TEMPLATE_ID` | `NUMBER` | `NOT NULL` | Internal ID for the template |
| `TEMPLATE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the template |
| `TEMPLATE_TYPE` | `VARCHAR2(9)` | `NOT NULL` | Type of the template, as follows:  `SINGLE` - one time period  `REPEATING` - maintain a time period |
| `BASELINE_NAME_PREFIX` | `VARCHAR2(30)` | `NOT NULL` | Name to use for the baselines that are created:  For a template type of `SINGLE`, the `BASELINE_NAME` `_PREFIX` is the name that will be used.  For a template type of `REPEATING`, the `BASELINE_NAME` will be the prefix to the name. |
| `START_TIME` | `DATE` | `NOT NULL` | For a template type of `SINGLE`, this is the start time for future baselines  For a template type of `REPEATING`, this is the effective start time that baselines should start being generated. |
| `END_TIME` | `DATE` | `NOT NULL` | For a template type of `SINGLE`, this is the end time for future baselines.  For a template type of `REPEATING`, this is the effective end time that baselines should stop being generated. |
| `DAY_OF_WEEK` | `VARCHAR2(9)` |  | For a template type of `REPEATING`, this indicates the day of the week to create the baseline: `SUNDAY`, `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `ALL`. |
| `HOUR_IN_DAY` | `NUMBER` |  | For a template type of `REPEATING`, a value from 0 - 23 to indicate the hour of the day to create the baseline for. |
| `DURATION` | `NUMBER` |  | For a template type of `REPEATING`, the length of time for the baseline to be created. |
| `EXPIRATION` | `NUMBER` |  | How long to keep the baseline, in number of days |
| `REPEAT_INTERVAL` | `VARCHAR2(128)` |  | String that represents the time repeating information in the format used by the `DBMS_SCHEDULER` package |
| `LAST_GENERATED` | `DATE` |  | Last time a baseline was generated for this template |