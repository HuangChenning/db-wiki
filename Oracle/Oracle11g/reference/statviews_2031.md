---
title: ALL_SCHEDULER_CHAIN_STEPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2031.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_CHAIN_STEPS` displays information about the defined steps of the chains accessible to the current user (that is, those chains that the user has `ALTER` or `EXECUTE` privileges for).

Related Views

- `DBA_SCHEDULER_CHAIN_STEPS` displays information about the defined steps of all chains in the database.
- `USER_SCHEDULER_CHAIN_STEPS` displays information about the defined steps of the chains owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Scheduler chain the step is in |
| `CHAIN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Scheduler chain the step is in |
| `STEP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the chain step |
| `PROGRAM_OWNER` | `VARCHAR2(98)` |  | Owner of the program that runs during the step |
| `PROGRAM_NAME` | `VARCHAR2(98)` |  | Name of the program that runs during the step |
| `EVENT_SCHEDULE_OWNER` | `VARCHAR2(98)` |  | Owner of the event schedule that this step waits for |
| `EVENT_SCHEDULE_NAME` | `VARCHAR2(98)` |  | Name of the event schedule that this step waits for |
| `EVENT_QUEUE_OWNER` | `VARCHAR2(30)` |  | Owner of the source queue into which the event will be raised |
| `EVENT_QUEUE_NAME` | `VARCHAR2(30)` |  | Name of the source queue into which the event will be raised |
| `EVENT_QUEUE_AGENT` | `VARCHAR2(30)` |  | Name of the AQ agent used by the user on the event source queue (for a secure queue) |
| `EVENT_CONDITION` | `VARCHAR2(4000)` |  | Boolean expression used as the subscription rule for an event on the source queue |
| `CREDENTIAL_OWNER` | `VARCHAR2(30)` |  | Owner of the credential to be used for an external step job |
| `CREDENTIAL_NAME` | `VARCHAR2(30)` |  | Name of the credential to be used for an external step job |
| `DESTINATION` | `VARCHAR2(128)` |  | Destination host on which a remote step job will run |
| `SKIP` | `VARCHAR2(5)` |  | Indicates whether the step should be skipped (`TRUE`) or not (`FALSE`) |
| `PAUSE` | `VARCHAR2(5)` |  | Indicates whether the step should be paused after running (`TRUE`) or not (`FALSE`) |
| `PAUSE_BEFORE` <sup>Foot 1</sup> | `VARCHAR2(5)` |  | Indicates whether the step should be paused before running (`TRUE`) or not (`FALSE`) |
| `RESTART_ON_RECOVERY` | `VARCHAR2(5)` |  | Indicates whether the step should be restarted on database recovery (`TRUE`) or not (`FALSE`) |
| `RESTART_ON_FAILURE` | `VARCHAR2(5)` |  | Indicates whether the step should be restarted on application failure (`TRUE`) or not (`FALSE`) |
| `STEP_TYPE` | `VARCHAR2(14)` |  | Type of the step: |
| `TIMEOUT` | `INTERVAL DAY(3) TO SECOND(0)` |  | Timeout for waiting on an event schedule |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

- ["DBA\_SCHEDULER\_CHAIN\_STEPS"](statviews_4235.md)
- ["USER\_SCHEDULER\_CHAIN\_STEPS"](statviews_5423.md)