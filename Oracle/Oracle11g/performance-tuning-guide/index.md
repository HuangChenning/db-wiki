---
title: Index
book: Performance Tuning Guide
doc_id: E41573-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41573/index.htm
tags:
  - oracle
  - 11g
  - performance-tuning-guide
---

A B C D E F G H I J K L M N O P Q R S T U V W

---

## A

access paths

Active Session History, [5.1.1.3](autostat.md)

report

activity over time, [5.3.9.8](autostat.md)

load profile, [5.3.9.2](autostat.md)

top events, [5.3.9.1](autostat.md)

top files, [5.3.9.7](autostat.md)

top Java, [5.3.9.5](autostat.md)

top latches, [5.3.9.7](autostat.md)

top objects, [5.3.9.7](autostat.md)

top PL/SQL, [5.3.9.4](autostat.md)

top sessions, [5.3.9.6](autostat.md)

Top SQL, [5.3.9.3](autostat.md)

using, [5.3.9](autostat.md)

adaptive thresholds, [5.2.3](autostat.md)

ALL\_OUTLINE\_HINTS view

stored outline hints, [20.1.7](outlines.md)

ALL\_OUTLINES view

stored outlines, [20.1.7](outlines.md)

ALL\_ROWS hint, [11.5.2.2](optimops.md)

allocation of memory, [7.1](memory.md)

ALTER INDEX statement, [14.1.7](data_acc.md)

ALTER SESSION statement

examples, [21.4.2](sqltrace.md)

SET SESSION\_CACHED\_CURSORS clause, [7.3.7.2](memory.md)

ANALYZE statement, [13.3.1](stats.md)

antijoins, [11.3.2](optimops.md)

applications

deploying, [2.7](design.md)

design principles, [2.5](design.md)

development trends, [2.5.7](design.md)

implementing, [2.5.6](design.md)

Automatic Database Diagnostic Monitor

actions and rationales of recommendations, [6.1.3](diag.md)

analysis results example, [6.1.4](diag.md)

and DB time, [6.1.1](diag.md)

CONTROL\_MANAGEMENT\_PACK\_ACCESS parameter, [6.2](diag.md)

DBIO\_EXPECTED, [6.2](diag.md)

example report, [6.1.4](diag.md)

findings, [6.1.3](diag.md)

overview, [6.1](diag.md)

results, [6.1.3](diag.md)

setups, [6.2](diag.md)

STATISTICS\_LEVEL parameter, [6.2](diag.md)

types of problems considered, [6.1.1](diag.md)

types of recommendations, [6.1.3](diag.md)

automatic database diagnostic monitoring, [1.2.1](perf_overview.md), [16.4.1](sql_overview.md)

automatic segment-space management, [4.1.4.1](build_db.md), [8.2.6.2](iodesign.md), [10.3.1.2.1](instance_tune.md)

Automatic Shared Memory Management, [7.1.3](memory.md)

automatic SQL tuning, [1.2.1](perf_overview.md), [16.4.2](sql_overview.md)

analysis, [17.1](sql_tune.md)

overview, [17](sql_tune.md)

Automatic Tuning Optimizer, [17.1](sql_tune.md)

automatic undo management, [4.1.2](build_db.md), [4.1.2](build_db.md)

Automatic Workload Repository, [1.2.1](perf_overview.md)

configuring, [5.2](autostat.md)

data gathering, [5.1](autostat.md)

DBMS\_WORKLOAD\_REPOSITORY package, [5.3.1](autostat.md), [5.3.2](autostat.md), [5.3.3](autostat.md)

default settings, [5.2.4](autostat.md)

factors affecting space usage, [5.2.4](autostat.md)

managing with APIs, [5.3.1](autostat.md), [5.3.2](autostat.md), [5.3.3](autostat.md)

minimizing space usage, [5.2.4](autostat.md)

overview, [5.2](autostat.md)

recommendations for retention period, [5.2.4](autostat.md)

reports, [5.3.6](autostat.md), [5.3.7](autostat.md), [5.3.8](autostat.md)

retention period, [5.2.4](autostat.md)

settings in DBA\_HIST\_WR\_CONTROL view, [5.3.1.3](autostat.md)

space usage, [5.2.4](autostat.md)

statistics collected, [5.2](autostat.md)

turning off automatic snapshot collection, [5.2.4](autostat.md)

unusual percentages in reports, [5.3.6](autostat.md)

views for accessing data, [5.3.5](autostat.md)

awrrpt.sql

Automatic Workload Repository report, [5.3.6](autostat.md), [5.3.7](autostat.md), [5.3.8](autostat.md)

---

## B

baselines, [1.1.2.2](perf_overview.md), [5.2.2](autostat.md)

performance, [5.1](autostat.md)

benchmarking workloads, [2.6.2.2](design.md)

big bang rollout strategy, [2.7.1](design.md)

bind variables, [7.3.1.3](memory.md)

peeking, [11.1.3](optimops.md)

bitmap indexes, [2.5.3.2.2](design.md)

inlist iterator, [12.9.5.3](ex_plan.md)

on joins, [14.6](data_acc.md)

when to use, [14.5](data_acc.md)

block cleanout, [10.2.4.2](instance_tune.md)

block size

choosing, [8.2.6](iodesign.md)

optimal, [8.2.6](iodesign.md)

bottlenecks

elimination, [1.1.2.4.2](perf_overview.md)

fixing, [3.1](technique.md)

identifying, [3.1](technique.md)

memory, [7.1](memory.md)

resource, [10.3.18.1.2](instance_tune.md)

broadcast

distribution value, [12.10](ex_plan.md)

B-tree indexes, [2.5.3.2.1](design.md)

buffer busy wait events, [10.2.3](instance_tune.md), [10.3.1](instance_tune.md)

actions, [10.3.1.2](instance_tune.md)

buffer cache

contention, [10.3.2](instance_tune.md), [10.3.3](instance_tune.md), [10.3.10.2](instance_tune.md)

hit ratio, [7.2.2.3](memory.md)

reducing buffers, [7.2.3.2](memory.md), [7.3.4.2](memory.md)

buffer pools

default cache, [7.2.4.1](memory.md)

hit ratio, [7.2.6](memory.md)

KEEP, [7.2.8](memory.md)

KEEP cache, [7.2.4.1](memory.md)

multiple, [7.2.4](memory.md)

RECYCLE cache, [7.2.4.1](memory.md)

business logic, [2.4.1.2.2](design.md), [2.5.6](design.md)

BYTES column

PLAN\_TABLE table, [12.10](ex_plan.md)

---

## C

CARDINALITY column

PLAN\_TABLE table, [12.10](ex_plan.md)

cardinality, column, [11.1.2.2](optimops.md)

cartesian joins, [11.3.6](optimops.md)

chained rows, [10.2.4.3](instance_tune.md)

classes

wait events, [5.1.1.1](autostat.md), [10.1.3.2](instance_tune.md)

client/server applications, [9.4.1.2](os.md)

clusters, [14.8](data_acc.md), [14.8](data_acc.md)

hash and scans of, [11.2.5](optimops.md)

scans of, [11.2.4](optimops.md)

sorted hash, [14.9](data_acc.md)

column order

indexes, [2.5.3.5](design.md)

columns

cardinality, [11.1.2.2](optimops.md)

to index, [14.1.3](data_acc.md)

COMPATIBLE initialization parameter, [4.1.1](build_db.md)

components

hardware, [2.4.1.1](design.md)

software, [2.4.1.2](design.md)

composite indexes, [14.1.4](data_acc.md)

composite partitioning

examples of, [12.9.2](ex_plan.md)

conceptual modeling, [3.1.2](technique.md)

consistency

read, [10.2.4.2](instance_tune.md)

consistent gets from cache statistic, [7.2.2.3](memory.md)

consistent mode

TKPROF, [21.4.4.1](sqltrace.md)

constraints, [14.1.10](data_acc.md)

contention

library cache latch, [10.3.10.3](instance_tune.md)

memory, [7.1](memory.md), [10](instance_tune.md)

shared pool, [10.3.10.3](instance_tune.md)

tuning, [10](instance_tune.md)

wait events, [10.3.10](instance_tune.md)

context switches, [9.4.1.4.2](os.md)

CONTROL\_FILES initialization parameter, [4.1.1](build_db.md)

CONTROL\_MANAGEMENT\_PACK\_ACCESS initialization parameter

enabling automatic database diagnostic monitoring, [6.2](diag.md)

cost

optimizer calculation, [11.1.1](optimops.md)

COST column

PLAN\_TABLE table, [12.10](ex_plan.md)

cost-based optimizations

procedures for plan stability, [20.2](outlines.md)

upgrading to, [20.2.2](outlines.md)

CPUs, [2.4.1.1.1](design.md)

statistics, [5.1.2.1](autostat.md), [10.1.2.1.3](instance_tune.md)

utilization, [9.4.1](os.md)

CREATE INDEX statement

PARALLEL clause, [4.2.3](build_db.md)

CREATE OUTLINE statement, [20.1.5](outlines.md)

create\_extended\_statistics, [13.5.2.1.1](stats.md), [13.5.2.2.1](stats.md)

CREATE\_STORED\_OUTLINES initialization parameter, [20.1.5](outlines.md), [20.1.5.1](outlines.md)

CREATE\_STORED\_OUTLINES parameter, [20.1.5](outlines.md)

current mode

TKPROF, [21.4.4.1](sqltrace.md)

CURSOR\_NUM column

TKPROF\_TABLE table, [21.4.5.3](sqltrace.md)

CURSOR\_SHARING initialization parameter, [7.3.2.1](memory.md)

CURSOR\_SPACE\_FOR\_TIME initialization parameter, [7.3.6](memory.md)

cursors

accessing, [7.3.2.6](memory.md)

sharing, [7.3.2.6](memory.md)

---

## D

data

and transactions, [2.4.1.2.4](design.md)

cache, [9.1.1](os.md)

gathering, [5.1](autostat.md)

modeling, [2.5.2](design.md)

queries, [2.4.2](design.md)

searches, [2.4.2](design.md)

data dictionary, [7.3.4.1.2](memory.md)

statistics in, [13.7.1](stats.md)

views used in optimization, [13.7.1](stats.md)

Data Pump

Export utility

statistics on system-generated columns names, [13.5.4](stats.md)

Import utility

copying statistics, [13.5.4](stats.md)

database monitoring, [1.2.1](perf_overview.md), [16.4.1](sql_overview.md)

diagnostic, [6.1](diag.md)

Database Resource Manager, [9.1.3](os.md), [9.1.3](os.md), [9.4.2](os.md), [10.1.2.1.3](instance_tune.md)

database tuning

transient performance problems, [5.3.8](autostat.md)

databases

buffers, [7.2.3.2](memory.md), [7.3.4.2](memory.md)

diagnosing and monitoring, [6.1](diag.md)

size, [2.4.2](design.md)

statistics, [5.1.1](autostat.md)

DATE\_OF\_INSERT column

TKPROF\_TABLE table, [21.4.5.3](sqltrace.md)

db block gets from cache statistic, [7.2.2.3](memory.md)

db file scattered read wait events, [10.2.3](instance_tune.md), [10.3.2](instance_tune.md), [10.3.2](instance_tune.md)

actions, [10.3.2.1](instance_tune.md), [10.3.3.1](instance_tune.md)

db file sequential read wait events, [10.2.3](instance_tune.md), [10.3.2](instance_tune.md), [10.3.3](instance_tune.md)

actions, [10.3.3.1](instance_tune.md)

DB time

metric, [6.1.1](diag.md)

statistic, [5.1.1.2](autostat.md)

DB\_BLOCK\_SIZE initialization parameter, [4.1.1](build_db.md), [8.2.1.2](iodesign.md)

DB\_CACHE\_ADVICE parameter, [7.2.3.1](memory.md)

DB\_CACHE\_SIZE initialization parameter, [7.2.3.2](memory.md), [7.2.4](memory.md)

DB\_DOMAIN initialization parameter, [4.1.1](build_db.md)

DB\_FILE\_MULTIBLOCK\_READ\_COUNT initialization parameter, [8.2.1.1](iodesign.md), [8.2.1.2](iodesign.md), [8.2.1.3](iodesign.md), [10.3.2](instance_tune.md), [11.2.1](optimops.md)

cost-based optimization, [11.3.2](optimops.md)

DB\_KEEP\_CACHE\_SIZE

initialization parameter, [7.2.8](memory.md)

DB\_NAME initialization parameter, [4.1.1](build_db.md)

DB\_nK\_CACHE\_SIZE initialization parameter, [7.2.3.1](memory.md)

DB\_RECYCLE\_CACHE\_SIZE

initialization parameter, [7.2.9](memory.md)

DB\_WRITER\_PROCESSES initialization parameter, [10.3.8.3.1](instance_tune.md)

DBA\_HIST views, [5.3.5](autostat.md)

DBA\_HIST\_WR\_CONTROL view

Automatic Workload Repository settings, [5.3.1.3](autostat.md)

DBA\_OBJECTS view, [7.2.7](memory.md)

DBA\_OUTLINE\_HINTS view

stored outline hints, [20.1.7](outlines.md)

DBA\_OUTLINES view

stored outlines, [20.1.7](outlines.md)

DBIO\_EXPECTED parameter, [6.2](diag.md)

DBMS\_ADDM package

Automatic Database Diagnostic Monitor, [6.3](diag.md)

DBMS\_ADVISOR package, [18.1](advisor.md)

setting DBIO\_EXPECTED, [6.2](diag.md)

setups for ADDM, [6.2](diag.md), [6.2](diag.md)

DBMS\_MONITOR package

End-to-End Application Tracing, [21.1](sqltrace.md)

DBMS\_OUTLN package

procedures for managing outlines, [20.1.4](outlines.md)

DBMS\_OUTLN\_EDIT package

procedures for managing outlines, [20.1.4](outlines.md)

DBMS\_RESULT\_CACHE, [7.6.1.3](memory.md), [7.6.1.3.2](memory.md)

DBMS\_SHARED\_POOL package

managing the shared pool, [7.3.9](memory.md)

DBMS\_SPM

EVOLVE\_SQL\_PLAN\_BASELINE, [15.2.3.2](optplanmgmt.md)

DBMS\_SQLDIAG, [16.6.1.2](sql_overview.md)

DBMS\_SQLTUNE package

SQL Tuning Advisor, [17.3.4](sql_tune.md), [17.4](sql_tune.md)

SQL Tuning Sets, [17.4](sql_tune.md)

dbms\_stats functions

create\_extended\_statistics, [13.5.2.1.1](stats.md)

drop\_extended\_stats, [13.5.2.1.3](stats.md), [13.5.2.2.3](stats.md)

gather\_table\_stats, [13.5.2.2.1](stats.md)

show\_extended\_stats\_name, [13.5.2.1.2](stats.md)

dbms\_stats package

method\_opt, [13.5.2.1.5](stats.md)

DBMS\_STATS package, [13.3.1](stats.md), [13.3.4](stats.md), [18.1](advisor.md)

managing query optimizer statistics, [11.5.2.3](optimops.md)

manually determining sample size for gathering procedures, [13.3.1.1](stats.md)

DBMS\_STATS\_DISCOVER, [13.5.2.1](stats.md)

DBMS\_WORKLOAD\_REPOSITORY package

managing the Automatic Workload Repository, [5.3.1](autostat.md), [5.3.2](autostat.md), [5.3.3](autostat.md)

DBMS\_XPLAN package

displaying plan table output, [12.4](ex_plan.md)

debugging designs, [2.6.4](design.md)

default cache, [7.2.4.1](memory.md)

deploying applications, [2.7](design.md)

DEPTH column

TKPROF\_TABLE table, [21.4.5.3](sqltrace.md)

design principles, [2.5](design.md)

designs

debugging, [2.6.4](design.md)

testing, [2.6.4](design.md)

validating, [2.6.4](design.md)

development environments, [2.5.6](design.md)

diagnostic monitoring, [1.2.1](perf_overview.md), [6.1](diag.md), [16.4.1](sql_overview.md)

introduction, [6.1](diag.md)

DIAGNOSTIC\_DEST initialization parameter, [21.4.1](sqltrace.md)

direct path

read events, [10.3.4](instance_tune.md)

read events actions, [10.3.4.2](instance_tune.md)

read events causes, [10.3.4.1](instance_tune.md)

wait events, [10.3.5](instance_tune.md)

write events actions, [10.3.5.2](instance_tune.md)

write events causes, [10.3.5.1](instance_tune.md)

disabled constraints, [14.1.10](data_acc.md)

disks

monitoring operating system file activity, [10.1.2.2](instance_tune.md)

statistics, [5.1.2.3](autostat.md)

DISTRIBUTION column

PLAN\_TABLE table, [12.10](ex_plan.md)

domain indexes

and EXPLAIN PLAN, [12.9.6](ex_plan.md)

using, [14.7](data_acc.md)

drop\_extended\_stats, [13.5.2.1.3](stats.md), [13.5.2.2.3](stats.md)

dynamic statistics

process, [13.6.2.1](stats.md)

sampling levels, [13.6.2.1](stats.md)

when to use, [13.6.4](stats.md)

---

## E

emergencies

performance, [3.2](technique.md)

Emergency Performance Method, [3.2.1](technique.md)

enabled constraints, [14.1.10](data_acc.md)

End-to-End Application Tracing, [21](sqltrace.md), [21.1](sqltrace.md)

action and module names, [2.5.6](design.md), [21.1](sqltrace.md)

creating a service, [21.1](sqltrace.md)

DBMS\_APPLICATION\_INFO package, [21.1](sqltrace.md)

DBMS\_MONITOR package, [21.1](sqltrace.md)

enforced constraints, [14.1.10](data_acc.md)

enqueue wait events, [10.2.3](instance_tune.md), [10.3.6](instance_tune.md)

actions, [10.3.6.2](instance_tune.md)

statistics, [10.1.3.4.5](instance_tune.md)

equijoins, [16.5.3.1](sql_overview.md)

error message documentation, [Preface](preface.md)

estimating workloads, [2.6.2](design.md)

benchmarking, [2.6.2.2](design.md)

extrapolating, [2.6.2.1](design.md)

examples

ALTER SESSION statement, [21.4.2](sqltrace.md)

EXPLAIN PLAN output, [21.4.4.10](sqltrace.md)

SQL trace facility output, [21.4.4.10](sqltrace.md)

EXECUTE\_TASK procedure, [18.2.5.5.1](advisor.md)

execution plans

capturing SQL plan baselines, [15.2.1](optplanmgmt.md)

evolving SQL plan baselines, [15.2.3](optplanmgmt.md)

examples, [21.4.3.1](sqltrace.md)

joins, [11.3.1](optimops.md)

loading from a SQL Tuning Set, [15.2.1.2.1](optplanmgmt.md)

loading from AWR snapshots, [15.2.1.2.1](optplanmgmt.md)

loading from the cursor cache, [15.2.1.2.2](optplanmgmt.md)

managing SQL plan baselines, [15.2](optplanmgmt.md)

overview of, [11.4](optimops.md)

plan stability, [20.1](outlines.md)

preserving with plan stability, [20.1](outlines.md)

selecting SQL plan baselines, [15.2.2](optplanmgmt.md)

TKPROF, [21.4.3.1](sqltrace.md), [21.4.3.2](sqltrace.md)

viewing with the utlxpls.sql script, [11.4.1](optimops.md)

EXPLAIN PLAN statement

access paths, [11.2.6](optimops.md)

and domain indexes, [12.9.6](ex_plan.md)

and full partition-wise joins, [12.9.4](ex_plan.md)

and partial partition-wise joins, [12.9.3](ex_plan.md)

and partitioned objects, [12.9](ex_plan.md)

basic steps, [11.4.1](optimops.md)

examples of output, [21.4.4.10](sqltrace.md)

execution order of steps in output, [11.4.1](optimops.md)

invoking with the TKPROF program, [21.4.3.2](sqltrace.md)

PLAN\_TABLE table, [12.2](ex_plan.md)

restrictions, [12.1.4](ex_plan.md)

scripts for viewing output, [11.4.1](optimops.md)

viewing the output, [11.4.1](optimops.md)

EXPLAIN\_MVIEW procedure, [18.3](advisor.md)

expression

mixed-type, [16.5.3.2](sql_overview.md)

Expression Statistics, [13.5.2.2](stats.md)

Extended Statistics, [13.5.2](stats.md)

extended syntax

for specifying tables in hints, [19.2.3](hintsref.md)

global hints, [19.2.3](hintsref.md)

EXTENT MANAGEMENT LOCAL

creating temporary tablespaces, [4.1.4.2](build_db.md)

extrapolating workloads, [2.6.2.1](design.md)

---

## F

FAST\_START\_MTTR\_TARGET

and tuning instance recovery, [10.5.3](instance_tune.md)

Fast-Start checkpointing architecture, [10.5.2](instance_tune.md)

Fast-Start Fault Recovery, [10.5](instance_tune.md), [10.5.2](instance_tune.md)

features, new, [Preface](whatsnew.md)

FILESYSTEMIO\_OPTIONS initialization parameter, [9.1.1.2](os.md)

FIRST\_ROWS(n) hint, [11.5.2.2](optimops.md)

free buffer wait events, [10.2.3](instance_tune.md), [10.3.8](instance_tune.md)

free lists, [10.3.1.2.1](instance_tune.md)

FULL hint, [14.1.6](data_acc.md)

full outer joins, [11.3.7.4](optimops.md)

full partition-wise joins, [12.9.4](ex_plan.md)

full table scans, [10.3.4.2.2](instance_tune.md)

function-based indexes, [2.5.3.2.3](design.md), [14.2](data_acc.md)

---

## G

GATHER\_ INDEX\_STATS procedure

in DBMS\_STATS package, [13.3.1](stats.md)

GATHER\_DATABASE\_STATS procedure

in DBMS\_STATS package, [13.3.1](stats.md)

GATHER\_DICTIONARY\_STATS procedure

in DBMS\_STATS package, [13.3.1](stats.md), [13.3.4](stats.md)

GATHER\_SCHEMA\_STATS procedure

in DBMS\_STATS package, [13.3.1](stats.md), [13.3.4](stats.md)

gather\_table\_stats, [13.5.2.2.1](stats.md)

GATHER\_TABLE\_STATS procedure

in DBMS\_STATS package, [13.3.1](stats.md), [13.3.4](stats.md)

GETMISSES column

in V$ROWCACHE table, [7.3.4.1.2](memory.md)

GETS column

in V$ROWCACHE view, [7.3.4.1.2](memory.md)

global hints, [19.2.3](hintsref.md)

GV$BUFFER\_POOL\_STATISTICS view, [7.2.6](memory.md)

---

## H

hard parsing, [2.5.5](design.md)

hardware

components, [2.4.1.1](design.md)

limitations of components, [2.3.3](design.md)

sizing of components, [2.3.3](design.md)

hash

distribution value, [12.10](ex_plan.md)

hash clusters

scans of, [11.2.5](optimops.md)

sorted, [14.9](data_acc.md)

hash joins, [11.3.4](optimops.md)

cost-based optimization, [11.3.2](optimops.md)

index join, [11.2.3.8.1](optimops.md)

hash partitions, [12.9](ex_plan.md)

examples of, [12.9.1](ex_plan.md)

hashing, [14.9](data_acc.md)

high water mark, [11.2.1](optimops.md)

hints

access paths, [16.5.4](sql_overview.md), [19.1.2.8](hintsref.md)

as used in outlines, [20.1.1.1](outlines.md)

cannot override sample access path, [11.2.7](optimops.md)

degree of parallelism, [19.1.2.7](hintsref.md)

FULL, [14.1.6](data_acc.md)

global, [19.2.3](hintsref.md)

global compared to local, [19.2.3](hintsref.md)

INDEX\_FFS, [11.2.3.7](optimops.md)

INDEX\_JOIN, [11.2.3.8](optimops.md)

indexspec syntax, [19.2.4](hintsref.md)

location syntax, [19.2.2](hintsref.md)

NO\_INDEX, [14.1.6](data_acc.md)

optimization approach and goal, [19.1.2.1](hintsref.md)

overriding optimizer choice, [11.2.7](optimops.md)

overriding OPTIMIZER\_MODE, [11.5.2.2](optimops.md)

parallel query option, [19.1.2.7](hintsref.md)

specifying a query block, [19.2.2](hintsref.md)

specifying indexes, [19.2.4](hintsref.md)

tablespec syntax, [19.2.3](hintsref.md)

using extended syntax, [19.2.3](hintsref.md)

histograms

frequency, [13.7.2.2](stats.md)

height-balanced, [13.7.2.1](stats.md)

HOLD\_CURSOR clause, [7.3.2.6.2](memory.md)

hours of service, [2.4.2](design.md)

HW enqueue

contention, [10.3.6.2.2](instance_tune.md)

---

## I

ID column

PLAN\_TABLE table, [12.10](ex_plan.md)

idle wait events, [10.3.9](instance_tune.md)

SQL\*Net message from client, [10.3.18.1](instance_tune.md)

implementing business logic, [2.4.1.2.2](design.md)

INDEX hint, [14.1.6](data_acc.md)

INDEX\_COMBINE hint, [14.1.6](data_acc.md)

INDEX\_FFS hint, [11.2.3.7](optimops.md), [11.2.3.7.1](optimops.md)

INDEX\_JOIN hint, [11.2.3.8](optimops.md)

indexes

adding columns, [2.5.3.1](design.md)

appending columns, [2.5.3.1](design.md)

avoiding the use of, [14.1.6](data_acc.md)

bitmap, [2.5.3.2.2](design.md), [14.5](data_acc.md)

B-tree, [2.5.3.2.1](design.md)

choosing columns for, [14.1.3](data_acc.md)

column order, [2.5.3.5](design.md)

composite, [14.1.4](data_acc.md)

costs, [2.5.3.3](design.md)

creating, [4.2.3](build_db.md)

design, [2.5.3](design.md)

domain, [14.7](data_acc.md)

dropping, [14.1.1](data_acc.md)

enforcing uniqueness, [14.1.9](data_acc.md)

ensuring the use of, [14.1.5](data_acc.md)

function-based, [2.5.3.2.3](design.md), [14.2](data_acc.md)

improving selectivity, [14.1.4](data_acc.md)

index joins, [11.2.3.8.1](optimops.md)

joins, [11.2.3.8.1](optimops.md)

low selectivity, [14.1.6](data_acc.md)

modifying values of, [14.1.3](data_acc.md)

non-unique, [14.1.9](data_acc.md)

partitioned, [2.5.3.2.4](design.md)

placement on disk, [8.2.2](iodesign.md)

rebuilding, [14.1.7](data_acc.md)

re-creating, [14.1.7](data_acc.md)

reducing I/O, [2.5.3.5](design.md)

reverse key, [2.5.3.2.5](design.md)

scans of, [11.2.3](optimops.md)

selectivity, [2.5.3.5](design.md)

selectivity of, [14.1.3](data_acc.md)

sequences in, [2.5.3.4](design.md)

serializing in, [2.5.3.4](design.md)

specifying in hints, [19.2.4](hintsref.md)

statistics gathering, [13.5](stats.md)

indexspec

hint syntax, [19.2.4](hintsref.md)

initialization parameters

CONTROL\_FILES, [4.1.1](build_db.md)

DB\_BLOCK\_SIZE, [4.1.1](build_db.md)

DB\_DOMAIN, [4.1.1](build_db.md)

DB\_FILE\_MULTIBLOCK\_READ\_COUNT, [11.3.2](optimops.md)

DB\_NAME, [4.1.1](build_db.md)

DIAGNOSTIC\_DEST, [21.4.1](sqltrace.md)

OPEN\_CURSORS, [4.1.1](build_db.md)

OPTIMIZER\_FEATURES\_ENABLE, [11.2.3.7](optimops.md), [11.2.3.8](optimops.md)

OPTIMIZER\_MODE, [11.5.2.1](optimops.md), [19.1.2.1](hintsref.md)

PGA\_AGGREGATE\_TARGET, [4.2.3.1](build_db.md)

PROCESSES, [4.1.1](build_db.md)

SESSIONS, [4.1.1](build_db.md)

STREAMS\_POOL\_SIZE, [4.1.1](build_db.md), [7.1.3](memory.md)

INLIST ITERATOR operation, [12.9.5](ex_plan.md)

inlists, [12.9.5](ex_plan.md)

instance caging, [9.4](os.md)

instance configuration

initialization files, [4.1.1](build_db.md)

performance considerations, [4.1](build_db.md)

instance recovery

Fast-Start Fault Recovery, [10.5.2](instance_tune.md)

performance tuning, [10.5](instance_tune.md)

Internet scalability, [2.3.2](design.md)

I/O

and SQL statements, [10.3.2.4](instance_tune.md)

contention, [5.1.1.1](autostat.md), [10.1.2.2.1](instance_tune.md), [10.1.3.2](instance_tune.md), [10.3.2.2](instance_tune.md), [10.3.14](instance_tune.md)

excessive I/O waits, [10.3.2.2](instance_tune.md)

monitoring, [10.1.2.2](instance_tune.md)

objects causing I/O waits, [10.3.2.5](instance_tune.md)

reducing, [14.1.4](data_acc.md)

---

## J

joins

antijoins, [11.3.2](optimops.md)

cartesian, [11.3.6](optimops.md)

execution plans and, [11.3.1](optimops.md)

full outer, [11.3.7.4](optimops.md)

hash, [11.3.4](optimops.md)

index joins, [11.2.3.8.1](optimops.md)

join order and execution plans, [11.4](optimops.md)

nested loop, [11.3.3](optimops.md)

nested loops and cost-based optimization, [11.3.2](optimops.md)

order, [16.5.4](sql_overview.md), [16.5.4](sql_overview.md)

outer, [11.3.7](optimops.md)

partition-wise

examples of full, [12.9.4](ex_plan.md)

examples of partial, [12.9.3](ex_plan.md)

full, [12.9.4](ex_plan.md)

semijoins, [11.3.2](optimops.md)

sort merge, [11.3.5](optimops.md)

sort-merge and cost-based optimization, [11.3.2](optimops.md), [11.3.2](optimops.md)

---

## K

KEEP buffer pool, [7.2.8](memory.md)

KEEP cache, [7.2.4.1](memory.md)

---

## L

LARGE\_POOL\_SIZE initialization parameter, [7.3.5.1](memory.md)

latch contention

library cache latches, [10.2.1.2](instance_tune.md)

shared pool latches, [10.2.1.2](instance_tune.md)

latch free wait events, [10.2.3](instance_tune.md)

actions, [10.3.10.1](instance_tune.md)

latch wait events, [10.3.10](instance_tune.md)

latches, [5.3.9.7.3](autostat.md)

tuning, [1.1.2.3](perf_overview.md), [10.3.10.3](instance_tune.md)

library cache

latch contention, [10.3.10.3](instance_tune.md)

latch wait events, [10.3.10.1](instance_tune.md)

lock, [10.3.13](instance_tune.md)

memory allocation, [7.3.4.1.1](memory.md)

pin, [10.3.12](instance_tune.md)

linear scalability, [2.3.3](design.md)

locks and lock holders

finding, [10.3.6.1](instance_tune.md)

log buffer

space wait events, [10.2.3](instance_tune.md), [10.3.14](instance_tune.md)

tuning, [7.4.1](memory.md)

log file

parallel write wait events, [10.3.11](instance_tune.md)

switch wait events, [10.3.15](instance_tune.md)

sync wait events, [10.2.3](instance_tune.md), [10.3.16](instance_tune.md)

log writer processes

tuning, [8.2.3.2](iodesign.md)

LOG\_BUFFER initialization parameter, [7.4](memory.md)

setting, [7.4.2](memory.md)

LRU

aging policy, [7.2.4](memory.md)

latch contention, [10.3.10.3.4](instance_tune.md)

---

## M

managing the user interface, [2.4.1.2.1](design.md)

materialized views

tuning, [18.3](advisor.md)

max session memory statistic, [7.3.5.1.2](memory.md)

MAX\_DISPATCHERS initialization parameter, [4.3.1.1](build_db.md)

MAX\_DUMP\_FILE\_SIZE initialization parameter

SQL Trace, [21.4.1](sqltrace.md)

MAXOPENCURSORS clause, [7.3.2.6.2](memory.md)

memory

hardware component, [2.4.1.1.2](design.md)

memory allocation

importance, [7.1](memory.md)

library cache, [7.3.4.1.1](memory.md)

shared SQL areas, [7.3.4.1.1](memory.md)

tuning, [7.1.7](memory.md)

method\_opt, [13.5.2.1.5](stats.md)

metrics, [5.1](autostat.md)

migrated rows, [10.2.4.3](instance_tune.md)

mirroring

redo logs, [8.2.3.3](iodesign.md)

modeling

conceptual, [3.1.2](technique.md)

data, [2.5.2](design.md)

workloads, [2.6.3](design.md)

monitoring

diagnostic, [1.2.1](perf_overview.md), [16.4.1](sql_overview.md)

MultiColumn Statistics, [13.5.2.1](stats.md)

multiple buffer pools, [7.2.4](memory.md)

---

## N

NAMESPACE column

V$LIBRARYCACHE view, [7.3.3.2](memory.md)

nested loop joins, [11.3.3](optimops.md)

cost-based optimization, [11.3.2](optimops.md)

network

hardware component, [2.4.1.1.4](design.md)

speed, [2.4.2](design.md)

statistics, [5.1.2.4](autostat.md)

network communication wait events, [10.3.18](instance_tune.md)

db file scattered read wait events, [10.3.2](instance_tune.md)

db file sequential read wait events, [10.3.2](instance_tune.md), [10.3.3](instance_tune.md)

SQL\*Net message from Dblink, [10.3.18.2](instance_tune.md)

SQL\*Net more data to client, [10.3.18.3](instance_tune.md)

new features, [Preface](whatsnew.md)

NO\_INDEX hint, [14.1.6](data_acc.md)

NOT IN subquery, [11.3.2](optimops.md)

---

## O

OBJECT\_INSTANCE column

PLAN\_TABLE table, [12.10](ex_plan.md)

OBJECT\_NAME column

PLAN\_TABLE table, [12.10](ex_plan.md)

OBJECT\_NODE column

PLAN\_TABLE table, [12.10](ex_plan.md)

OBJECT\_OWNER column

PLAN\_TABLE table, [12.10](ex_plan.md)

OBJECT\_TYPE column

PLAN\_TABLE table, [12.10](ex_plan.md)

object-orientation, [2.5.7](design.md)

OLAP\_PAGE\_POOL\_SIZE initialization parameter, [7.5.2](memory.md)

OPEN\_CURSORS initialization parameter, [4.1.1](build_db.md)

operating system

data cache, [9.1.1](os.md)

monitoring disk I/O, [10.1.2.2](instance_tune.md)

statistics, [5.1.2](autostat.md)

OPERATION column

PLAN\_TABLE table, [12.10](ex_plan.md), [12.10](ex_plan.md)

optimization

choosing the approach, [11.5.2.1](optimops.md)

cost calculation, [11.1.1](optimops.md)

cost-based and choosing an access path, [11.2.7](optimops.md)

described, [11.1](optimops.md)

hints, [11.2.3.7](optimops.md), [11.2.3.8](optimops.md), [11.5.2.2](optimops.md)

manual, [11.5.2.2](optimops.md)

operations performed, [11.1.1](optimops.md)

optimizer

cost calculation, [11.1.1](optimops.md)

estimator, [11.1.2.2](optimops.md)

goals, [11.5.2](optimops.md)

introduction, [1.1.3.1](perf_overview.md), [11.1](optimops.md)

modes, [17.1](sql_tune.md)

moving to from RBO, [20.2.1](outlines.md)

operations, [11.1.1](optimops.md)

parameters for setting mode, [11.5.2.1](optimops.md)

plan stability, [20.1](outlines.md)

query, [1.1.3.1](perf_overview.md)

statistics, [13.1](stats.md)

throughput, [11.5.2](optimops.md)

upgrading, [20.2.2](outlines.md)

OPTIMIZER column

PLAN\_TABLE, [12.10](ex_plan.md)

OPTIMIZER\_FEATURES\_ENABLE initialization parameter, [11.2.3.7](optimops.md), [11.2.3.8](optimops.md)

OPTIMIZER\_MODE initialization parameter, [11.5.2.1](optimops.md), [11.5.2.1](optimops.md), [19.1.2.1](hintsref.md)

hints affecting, [11.5.2.2](optimops.md)

OPTIONS column

PLAN\_TABLE table, [12.10](ex_plan.md)

Oracle CPU statistics, [10.1.2.1.3](instance_tune.md)

Oracle Enterprise Manager

advisors, [1.2.1](perf_overview.md)

Performance page, [1.2.1](perf_overview.md)

Oracle Forms

control of parsing and private SQL areas, [7.3.2.6.5](memory.md)

Oracle Managed Files, [8.2.5](iodesign.md)

tuning, [8.2.5](iodesign.md)

Oracle Orion

calibration tool parameters, [8.4.4](iodesign.md)

command-line options, [8.4.4](iodesign.md)

Oracle performance improvement method, [3.1](technique.md)

steps, [3.1.1](technique.md)

order

joins, [16.5.4](sql_overview.md)

OTHER column

PLAN\_TABLE table, [12.10](ex_plan.md)

OTHER\_TAG column

PLAN\_TABLE table, [12.10](ex_plan.md)

outer joins, [11.3.7](optimops.md), [16.5.4.1](sql_overview.md)

outlines

CREATE OUTLINE statement, [20.1.5](outlines.md)

creating and using, [20.1.5](outlines.md)

description, [20.1](outlines.md)

execution plans and plan stability, [20.1](outlines.md)

hints, [20.1.1.1](outlines.md)

moving tables, [20.1.8](outlines.md)

moving to the cost-based optimizer, [20.2.1](outlines.md)

storage requirements, [20.1.2](outlines.md)

using, [20.1.6](outlines.md)

viewing data for, [20.1.7](outlines.md)

---

## P

package

DBMS\_RESULT\_CACHE, [7.6.1.3](memory.md), [7.6.1.3.2](memory.md)

packages

DBMS\_ADVISOR, [18.1](advisor.md)

DBMS\_STATS, [18.1](advisor.md)

page table, [9.4.1.1.2](os.md)

paging, [9.4.1.2](os.md)

reducing, [7.1.6.1](memory.md)

PARALLEL clause

CREATE INDEX statement, [4.2.3](build_db.md)

parameter

RESULT\_CACHE\_MAX\_SIZE, [7.6.1.3.1](memory.md)

RESULT\_CACHE\_MODE, [7.6.3.1](memory.md)

PARENT\_ID column

PLAN\_TABLE table, [12.10](ex_plan.md)

parsing

hard, [2.5.5](design.md)

Oracle Forms, [7.3.2.6.5](memory.md)

Oracle precompilers, [7.3.2.6.2](memory.md)

reducing unnecessary calls, [7.3.2.6](memory.md)

soft, [2.5.5](design.md)

PARTITION\_ID column

PLAN\_TABLE table, [12.10](ex_plan.md)

PARTITION\_START column

PLAN\_TABLE table, [12.10](ex_plan.md)

PARTITION\_STOP column

PLAN\_TABLE table, [12.10](ex_plan.md)

partitioned indexes, [2.5.3.2.4](design.md)

partitioned objects

and EXPLAIN PLAN statement, [12.9](ex_plan.md)

partitioning

distribution value, [12.10](ex_plan.md)

examples of, [12.9.1](ex_plan.md)

examples of composite, [12.9.2](ex_plan.md)

hash, [12.9](ex_plan.md)

range, [12.9](ex_plan.md)

start and stop columns, [12.9.1](ex_plan.md)

partition-wise joins

full, [12.9.4](ex_plan.md)

full, and EXPLAIN PLAN output, [12.9.4](ex_plan.md)

partial, and EXPLAIN PLAN output, [12.9.3](ex_plan.md)

PCTFREE parameter, [4.2](build_db.md), [10.2.4.3](instance_tune.md)

PCTUSED parameter, [10.2.4.3](instance_tune.md), [10.2.4.3](instance_tune.md)

peeking

bind variables, [11.1.3](optimops.md)

performance

emergencies, [3.2](technique.md)

improvement method, [3.1](technique.md)

improvement method steps, [3.1.1](technique.md)

mainframe, [9.2.3](os.md)

monitoring memory on Windows, [9.4.1.1.1](os.md)

tools for diagnosing and tuning, [1.2](perf_overview.md)

UNIX-based systems, [9.2.1](os.md)

viewing execution plans, [11.4.1](optimops.md)

Windows, [9.2.2](os.md)

performance problems

transient, [5.3.8](autostat.md)

performance tuning

Fast-Start Fault Recovery, [10.5](instance_tune.md)

instance recovery, [10.5](instance_tune.md)

FAST\_START\_MTTR\_TARGET, [10.5.2](instance_tune.md)

setting FAST\_START\_MTTR\_TARGET, [10.5.3](instance_tune.md)

using V$INSTANCE\_RECOVERY, [10.5.2.3](instance_tune.md)

PGA\_AGGREGATE\_TARGET initialization parameter, [4.1.1](build_db.md), [4.2.3.1](build_db.md), [7.5.1](memory.md), [9.1.2.2](os.md)

physical reads from cache statistic, [7.2.2.3](memory.md)

plan stability, [20.1](outlines.md)

limitations of, [20.1.1](outlines.md)

preserving execution plans, [20.1](outlines.md)

procedures for the cost-based optimizer, [20.2](outlines.md)

use of hints, [20.1.1](outlines.md)

PLAN\_TABLE table

BYTES column, [12.10](ex_plan.md)

CARDINALITY column, [12.10](ex_plan.md)

COST column, [12.10](ex_plan.md)

creating, [12.2](ex_plan.md), [12.2](ex_plan.md)

displaying, [12.4](ex_plan.md)

DISTRIBUTION column, [12.10](ex_plan.md)

ID column, [12.10](ex_plan.md)

OBJECT\_INSTANCE column, [12.10](ex_plan.md)

OBJECT\_NAME column, [12.10](ex_plan.md)

OBJECT\_NODE column, [12.10](ex_plan.md)

OBJECT\_OWNER column, [12.10](ex_plan.md)

OBJECT\_TYPE column, [12.10](ex_plan.md)

OPERATION column, [12.10](ex_plan.md)

OPTIMIZER column, [12.10](ex_plan.md)

OPTIONS column, [12.10](ex_plan.md)

OTHER column, [12.10](ex_plan.md)

OTHER\_TAG column, [12.10](ex_plan.md)

PARENT\_ID column, [12.10](ex_plan.md)

PARTITION\_ID column, [12.10](ex_plan.md)

PARTITION\_START column, [12.10](ex_plan.md)

PARTITION\_STOP column, [12.10](ex_plan.md)

POSITION column, [12.10](ex_plan.md)

REMARKS column, [12.10](ex_plan.md)

SEARCH\_COLUMNS column, [12.10](ex_plan.md)

STATEMENT\_ID column, [12.10](ex_plan.md)

TIMESTAMP column, [12.10](ex_plan.md)

PL/SQL procedures

EXPLAIN\_MVIEW, [18.3](advisor.md)

TUNE\_MVIEW, [18.3](advisor.md)

POSITION column

PLAN\_TABLE table, [12.10](ex_plan.md)

precompilers

control of parsing and private SQL areas, [7.3.2.6.2](memory.md)

PRIMARY KEY constraint, [14.1.9](data_acc.md)

PRIVATE\_SGA variable, [7.3.5.1.3](memory.md)

privileges

SQL Access Advisor, [18.2.2](advisor.md)

proactive monitoring, [1.1.2.4.1](perf_overview.md)

processes

scheduling, [9.4.1.4.1](os.md)

PROCESSES initialization parameter, [4.1.1](build_db.md)

program global area (PGA)

direct path read, [10.3.4](instance_tune.md)

direct path write, [10.3.5](instance_tune.md)

shared servers, [7.3.5.1.1](memory.md)

programming languages, [2.5.6](design.md)

---

## Q

queries

avoiding the use of indexes, [14.1.6](data_acc.md)

data, [2.4.2](design.md)

ensuring the use of indexes, [14.1.5](data_acc.md)

query optimizer, [1.1.3.1](perf_overview.md)

See optimizer

---

## R

range

distribution value, [12.10](ex_plan.md)

examples of partitions, [12.9.1](ex_plan.md)

partitions, [12.9](ex_plan.md)

rdbms ipc reply wait events, [10.3.17](instance_tune.md)

read consistency, [10.2.4.2](instance_tune.md)

read wait events

direct path, [10.3.4](instance_tune.md)

scattered, [10.3.2](instance_tune.md)

REBUILD clause, [14.1.7](data_acc.md)

recursive calls, [21.4.4.5](sqltrace.md)

RECYCLE cache, [7.2.4.1](memory.md)

REDO BUFFER ALLOCATION RETRIES statistic, [7.4.2](memory.md)

redo logs, [4.1.3](build_db.md)

buffer size, [10.3.14](instance_tune.md)

mirroring, [8.2.3.3](iodesign.md)

placement on disk, [8.2.3.2](iodesign.md)

sizing, [4.1.3](build_db.md)

space requests, [10.2.4.1](instance_tune.md)

reducing

contention with dispatchers, [4.3.1.1](build_db.md)

data dictionary cache misses, [7.3.4.1.2](memory.md)

paging and swapping, [7.1.6.1](memory.md)

unnecessary parse calls, [7.3.2.6](memory.md)

RELEASE\_CURSOR clause, [7.3.2.6.2](memory.md)

REMARKS column

PLAN\_TABLE table, [12.10](ex_plan.md)

resources

allocation, [2.4.1.2.3](design.md), [2.5.6](design.md)

bottlenecks, [10.3.18.1.2](instance_tune.md)

wait events, [10.3.3](instance_tune.md)

response time, [2.4.2](design.md)

cost-based approach, [11.5.2.1](optimops.md)

result cache, [7.6.1](memory.md)

reverse key indexes, [2.5.3.2.5](design.md)

rollout strategies

big bang approach, [2.7.1](design.md)

trickle approach, [2.7.1](design.md)

round-robin

distribution value, [12.10](ex_plan.md)

row cache objects, [10.3.10.3.6](instance_tune.md)

row sources, [11.4.2](optimops.md)

rowids

table access by, [11.2.2](optimops.md)

rows

row sources, [11.4.2](optimops.md)

rowids used to locate, [11.2.2](optimops.md)

---

## S

SAMPLE BLOCK clause, [11.2.6](optimops.md)

access path and hints, [11.2.7](optimops.md)

SAMPLE clause, [11.2.6](optimops.md)

access path and hints cannot override, [11.2.7](optimops.md)

sample table scans, [11.2.6](optimops.md)

hints cannot override, [11.2.7](optimops.md)

sar UNIX command, [9.4.1.1.1](os.md)

scalability, [2.3.1](design.md)

factors preventing, [2.3.3](design.md), [2.3.3](design.md)

Internet, [2.3.2](design.md)

linear, [2.3.3](design.md)

scans

index, [11.2.3](optimops.md)

index joins, [11.2.3.8.1](optimops.md)

index of type bitmap, [11.2.3.9](optimops.md)

sample table, [11.2.6](optimops.md)

sample table and hints cannot override, [11.2.7](optimops.md)

scattered read wait events, [10.3.2](instance_tune.md)

actions, [10.3.2.1](instance_tune.md)

SEARCH\_COLUMNS column

PLAN\_TABLE table, [12.10](ex_plan.md)

segment-level statistics, [10.1.3.5](instance_tune.md)

SELECT statement

SAMPLE clause, [11.2.6](optimops.md)

selectivity

creating indexes, [14.1.3](data_acc.md)

improving for an index, [14.1.4](data_acc.md)

indexes, [14.1.6](data_acc.md)

ordering columns in an index, [2.5.3.5](design.md)

semijoins, [11.3.2](optimops.md)

sequential read wait events

actions, [10.3.3.1](instance_tune.md)

service hours, [2.4.2](design.md)

session memory statistic, [7.3.5.1.2](memory.md)

SESSIONS initialization parameter, [4.1.1](build_db.md)

SGA size, [7.4.1](memory.md)

SGA\_TARGET initialization parameter, [4.1.1](build_db.md)

and Automatic Shared Memory Management, [7.1.3](memory.md)

automatic memory management, [7.1.3](memory.md)

shared pool contention, [10.3.10.3](instance_tune.md)

shared server

performance issues, [4.3](build_db.md)

reducing contention, [4.3](build_db.md)

tuning, [4.3](build_db.md)

tuning memory, [7.3.5.1](memory.md)

shared SQL areas

memory allocation, [7.3.4.1.1](memory.md)

SHARED\_POOL\_RESERVED\_SIZE initialization parameter, [7.3.8.2](memory.md)

SHARED\_POOL\_SIZE initialization parameter, [7.3.4.1.2](memory.md), [7.3.4.2](memory.md), [7.3.8.4](memory.md)

allocating library cache, [7.3.4.1.1](memory.md)

tuning the shared pool, [7.3.5.1.4](memory.md)

SHOW SGA statement, [7.1.6.2](memory.md)

show\_extended\_stats\_name, [13.5.2.1.2](stats.md)

sizing redo logs, [4.1.3](build_db.md)

snapshots

about, [5.2.1](autostat.md)

soft parsing, [2.5.5](design.md)

software

components, [2.4.1.2](design.md)

sort areas

tuning, [7.5](memory.md)

sort merge joins, [11.3.5](optimops.md)

cost-based optimization, [11.3.2](optimops.md)

SQL Access Advisor, [18.1](advisor.md), [18.1](advisor.md), [18.2.3.2](advisor.md)

constants, [18.2.8](advisor.md)

creating a task, [18.1.1](advisor.md)

EXECUTE\_TASK procedure, [18.2.5.5.1](advisor.md)

generating the recommendations, [18.1.1](advisor.md)

privileges, [18.2.2](advisor.md)

recommendation process, [18.2.5.7](advisor.md)

steps in using, [18.1.1](advisor.md)

SQL management base

about, [15.6](optplanmgmt.md)

disk space usage, [15.6.1](optplanmgmt.md)

purging policy, [15.6.2](optplanmgmt.md)

SQL plan baseline

automatic plan capture, [15.2.1.1](optplanmgmt.md)

capturing

automatic, [15.2.1.1](optplanmgmt.md)

manual, [15.2.1.2](optplanmgmt.md)

evolving manually, [15.2.3.1](optplanmgmt.md)

evolving with DBMS\_SPM.EVOLVE\_SQL\_PLAN\_BASELINE, [15.2.3.2](optplanmgmt.md)

loading plans from a SQL Tuning Set, [15.2.1.2.1](optplanmgmt.md)

loading plans from AWR snapshots, [15.2.1.2.1](optplanmgmt.md)

loading plans from the cursor cache, [15.2.1.2.2](optplanmgmt.md)

manual plan loading, [15.2.1.2](optplanmgmt.md)

SQL Tuning Advisor, [15.3](optplanmgmt.md)

SQL plan baseline, fixed, [15.4](optplanmgmt.md)

SQL plan baselines

about, [15.2.1](optplanmgmt.md)

capturing, [15.2.1](optplanmgmt.md)

displaying, [15.5](optplanmgmt.md)

enabling, [15.2.2](optplanmgmt.md)

evolving, [15.2.3](optplanmgmt.md)

importing and exporting, [15.7](optplanmgmt.md)

managing, [15.2](optplanmgmt.md)

plan history, [15.2.1](optplanmgmt.md)

selecting, [15.2.2](optplanmgmt.md)

statement log, [15.2.1](optplanmgmt.md)

SQL statements

avoiding the use of indexes, [14.1.6](data_acc.md)

ensuring the use of indexes, [14.1.5](data_acc.md)

execution plans of, [11.4](optimops.md)

modifying indexed data, [14.1.3](data_acc.md)

waiting for I/O, [10.3.2.4](instance_tune.md)

SQL Test Case Builder, [16.6](sql_overview.md)

SQL trace facility, [21.3.1](sqltrace.md), [21.4.3](sqltrace.md)

example of output, [21.4.4.10](sqltrace.md)

output, [21.4.4.1](sqltrace.md)

statement truncation, [21.4.4.7](sqltrace.md)

steps to follow, [21.4](sqltrace.md)

trace files, [21.4.1](sqltrace.md)

SQL Tuning Advisor, [1.2.1](perf_overview.md), [16.4.2](sql_overview.md)

administering with APIs, [17.3.4](sql_tune.md), [17.4](sql_tune.md)

input sources, [17.3.1](sql_tune.md)

overview, [17.2](sql_tune.md)

tuning options, [17.3.2](sql_tune.md)

SQL Tuning Sets

description, [16.4.3](sql_overview.md), [17.3](sql_tune.md), [17.3.1](sql_tune.md), [17.3.4](sql_tune.md)

managing with APIs, [17.4](sql_tune.md), [17.4](sql_tune.md)

SQL\*Net

message from client idle events, [10.3.18.1](instance_tune.md)

message from dblink wait events, [10.3.18.2](instance_tune.md)

more data to client wait events, [10.3.18.3](instance_tune.md)

SQL, recursive, [13.6](stats.md)

SQL\_STATEMENT column

TKPROF\_TABLE, [21.4.5.3](sqltrace.md)

SQLAccess Advisor, [1.2.1](perf_overview.md), [16.4.4](sql_overview.md)

SQLTUNE\_CATEGORY initialization parameter

determining the SQL Profile category, [17.5.3](sql_tune.md)

ST enqueue

contention, [10.3.6.2.1](instance_tune.md)

start columns

in partitioning and EXPLAIN PLAN statement, [12.9.1](ex_plan.md)

STATEMENT\_ID column

PLAN\_TABLE table, [12.10](ex_plan.md)

statistics

and STATISTICS\_LEVEL initialization parameter, [1.2](perf_overview.md)

baselines, [5.1](autostat.md)

consistent gets from cache, [7.2.2.3](memory.md)

databases, [5.1.1](autostat.md)

db block gets from cache, [7.2.2.3](memory.md)

displaying in views, [13.7.1](stats.md)

exporting and importing, [13.5.4](stats.md)

gathering, [5.1](autostat.md)

gathering stale, [13.3.1.5](stats.md)

gathering using sampling, [13.3.1.1](stats.md)

gathering with DBMS\_STATS package, [13.3.1](stats.md), [13.3.4](stats.md)

gathering with DBMS\_STATS procedures, [13.3.1](stats.md)

limitations on restoring previous versions, [13.5.3](stats.md)

locking, [13.5.6](stats.md)

manually gathering, [13.3](stats.md)

max session memory, [7.3.5.1.2](memory.md)

missing, [13.5.8](stats.md)

operating systems, [5.1.2](autostat.md)

CPU statistics, [5.1.2.1](autostat.md)

disk statistics, [5.1.2.3](autostat.md)

network statistics, [5.1.2.4](autostat.md)

virtual memory statistics, [5.1.2.2](autostat.md)

optimizer, [13.1](stats.md)

optimizer mode, [11.5.2.1](optimops.md)

physical reads from cache, [7.2.2.3](memory.md)

restoring previous versions, [13.5.3](stats.md)

segment-level, [10.1.3.5](instance_tune.md)

session memory, [7.3.5.1.2](memory.md)

shared server processes, [4.3.2](build_db.md)

stale, [13.3.1.5](stats.md)

system, [13.4](stats.md)

time model, [5.1.1.2](autostat.md)

user-defined, [13.3.1.6](stats.md)

when to gather, [13.3.3](stats.md)

STATISTICS\_LEVEL initialization parameter, [5.1.3](autostat.md), [10.1.3.1](instance_tune.md)

and Automatic Workload Repository, [5.2](autostat.md)

enabling automatic database diagnostic monitoring, [6.2](diag.md)

settings for statistic gathering, [1.2](perf_overview.md)

stop columns

in partitioning and EXPLAIN PLAN statement, [12.9.1](ex_plan.md)

stored outlines

creating and using, [20.1.5](outlines.md)

execution plans and plan stability, [20.1](outlines.md)

hints, [20.1.1.1](outlines.md)

moving tables, [20.1.8](outlines.md)

storage requirements, [20.1.2](outlines.md)

using, [20.1.6](outlines.md)

viewing data for, [20.1.7](outlines.md)

STREAMS\_POOL\_SIZE initialization parameter, [4.1.1](build_db.md), [7.1.3](memory.md)

striping

manual, [8.2.2](iodesign.md)

subqueries

NOT IN, [11.3.2](optimops.md)

unnesting, [16.5.4.1.3](sql_overview.md)

swapping, [9.4.1.1.1](os.md), [9.4.1.2](os.md)

reducing, [7.1.6.1](memory.md)

switching processes, [9.4.1.4.1](os.md)

system architecture, [2.4](design.md)

configuration, [2.4.2](design.md)

hardware components, [2.4.1.1](design.md)

CPUs, [2.4.1.1.1](design.md)

I/O subsystems, [2.4.1.1.3](design.md)

memory, [2.4.1.1.2](design.md)

networks, [2.4.1.1.4](design.md)

software components, [2.4.1.2](design.md)

data and transactions, [2.4.1.2.4](design.md)

implementing business logic, [2.4.1.2.2](design.md)

managing the user interface, [2.4.1.2.1](design.md)

user requests and resource allocation, [2.4.1.2.3](design.md)

System Global Area tuning, [7.1.6.2](memory.md)

---

## T

tables

creating, [4.2](build_db.md)

design, [2.5.3](design.md)

full scans, [10.3.4.2.2](instance_tune.md)

placement on disk, [8.2.2](iodesign.md)

setting storage options, [4.2](build_db.md)

tablespaces, [4.1.4](build_db.md)

creating, [4.1.4](build_db.md), [4.1.4.2](build_db.md)

temporary, [4.1.4](build_db.md), [4.1.4.2](build_db.md)

tablespec

hint syntax, [19.2.3](hintsref.md)

templates

SQL Access Advisor, [18.2.3.2](advisor.md)

temporary tablespaces, [4.1.4](build_db.md)

creating, [4.1.4.2](build_db.md)

testing designs, [2.6.4](design.md)

thrashing, [9.4.1.2](os.md)

thresholds

adaptive, [5.2.3](autostat.md)

throughput

optimizer goal, [11.5.2](optimops.md)

time model statistics, [5.1.1.2](autostat.md)

TIMED\_STATISTICS initialization parameter

SQL Trace, [21.4.1](sqltrace.md)

TIMESTAMP column

PLAN\_TABLE table, [12.10](ex_plan.md)

TKPROF program, [21.3.2](sqltrace.md), [21.4.3](sqltrace.md)

editing the output SQL script, [21.4.5.2](sqltrace.md)

example of output, [21.4.4.10](sqltrace.md)

generating the output SQL script, [21.4.5.1](sqltrace.md)

row source operations, [21.4.4.2](sqltrace.md)

syntax, [21.4.3.2](sqltrace.md)

using the EXPLAIN PLAN statement, [21.4.3.2](sqltrace.md)

wait event information, [21.4.4.3](sqltrace.md)

TKPROF\_TABLE, [21.4.5.3](sqltrace.md), [21.4.5.3](sqltrace.md)

TM enqueue contention, [10.3.6.2.3](instance_tune.md)

tools for performance tuning, [1.2](perf_overview.md)

Top Java

Active Session History report, [5.3.9.5](autostat.md)

top PL/SQL

Active Session History report, [5.3.9.4](autostat.md)

Top Sessions

Active Session History report, [5.3.9.6](autostat.md)

Top SQL

Active Session History report, [5.3.9.3](autostat.md)

TRACEFILE\_IDENTIFIER initialization parameter

identifying trace files, [21.4.1](sqltrace.md)

tracing

consolidating with trcsess, [21.2](sqltrace.md)

identifying files, [21.4.1](sqltrace.md)

transactions and data, [2.4.1.2.4](design.md)

trcsess utility, [21.2](sqltrace.md)

trickle rollout strategy, [2.7.1](design.md)

TUNE\_MVIEW procedure, [18.3](advisor.md)

tuning

and bottleneck elimination, [1.1.2.4.2](perf_overview.md)

and proactive monitoring, [1.1.2.4.1](perf_overview.md)

latches, [1.1.2.3](perf_overview.md), [10.3.10.3](instance_tune.md)

logical structure, [14.1.1](data_acc.md)

memory allocation, [7.1.7](memory.md)

resource contention, [10](instance_tune.md)

shared server, [4.3](build_db.md)

sorts, [7.5](memory.md)

SQL Tuning Advisor, [17.2](sql_tune.md)

System Global Area (SGA), [7.1.6.2](memory.md)

TX enqueue contention, [10.3.6.2.4](instance_tune.md)

type conversion, [16.5.3.2](sql_overview.md)

---

## U

undo management, automatic mode, [4.1.2](build_db.md)

UNDO TABLESPACE clause, [4.1.2](build_db.md)

UNDO\_MANAGEMENT initialization parameter, [4.1.1](build_db.md), [4.1.2](build_db.md)

UNDO\_TABLESPACE initialization parameter, [4.1.1](build_db.md)

UNIQUE constraint, [14.1.9](data_acc.md)

uniqueness, [14.1.9](data_acc.md)

UNIX system performance, [9.2.1](os.md)

untransformed column values, [16.5.3.2](sql_overview.md)

upgrade

to the cost-based optimizer, [20.2.2](outlines.md)

USE\_STORED\_OUTLINES parameter, [20.1.6](outlines.md), [20.1.6](outlines.md)

user global area (UGA)

shared servers, [4.3](build_db.md), [7.3.5.1](memory.md)

V$SESSTAT, [7.3.5.1.2](memory.md)

user requests, [2.4.1.2.3](design.md)

USER\_DUMP\_DEST initialization parameter

SQL Trace, [21.4.1](sqltrace.md)

USER\_ID column, TKPROF\_TABLE, [21.4.5.3](sqltrace.md)

USER\_OUTLINE\_HINTS view

stored outline hints, [20.1.7](outlines.md)

USER\_OUTLINES view

stored outlines, [20.1.7](outlines.md)

user\_stat\_extensions, [13.5.2.1.4](stats.md), [13.5.2.2.2](stats.md)

user-defined bind variables, [11.1.3](optimops.md)

users

interaction method, [2.4.2](design.md)

interfaces, [2.5.6](design.md)

location, [2.4.2](design.md)

network speed, [2.4.2](design.md)

number of, [2.4.2](design.md)

requests, [2.5.6](design.md)

response time, [2.4.2](design.md)

Using SQL Plan Management, [15](optplanmgmt.md)

UTLCHN1.SQL script, [10.2.4.3](instance_tune.md)

UTLXPLP.SQL script

displaying plan table output, [12.4](ex_plan.md)

for viewing EXPLAIN PLANs, [11.4.1](optimops.md)

UTLXPLS.SQL script

displaying plan table output, [12.4](ex_plan.md)

for viewing EXPLAIN PLANs, [11.4.1](optimops.md)

used for displaying EXPLAIN PLANs, [11.4.1](optimops.md)

---

## V

V$ACTIVE\_SESSION\_HISTORY view, [5.1.1.3](autostat.md), [10.1.3.3](instance_tune.md)

V$ADVISOR\_PROGRESS view, [17.3.4.5](sql_tune.md), [17.6](sql_tune.md)

V$BH view, [7.2.7](memory.md)

V$BUFFER\_POOL\_STATISTICS view, [7.2.6](memory.md), [7.2.6](memory.md)

V$DB\_CACHE\_ADVICE view, [7.2.2.1](memory.md), [7.2.2.3](memory.md), [7.2.3](memory.md), [7.2.3.1](memory.md), [7.2.3.2](memory.md), [7.2.5](memory.md)

V$EVENT\_HISTOGRAM view, [10.1.3.3](instance_tune.md)

V$FILE\_HISTOGRAM view, [10.1.3.3](instance_tune.md)

V$JAVA\_LIBRARY\_CACHE\_MEMORY view, [7.3.3.3.3](memory.md)

V$JAVA\_POOL\_ADVICE view, [7.3.3.3.3](memory.md)

V$LIBRARY\_CACHE\_MEMORY view, [7.3.3.3.2](memory.md)

V$LIBRARYCACHE view

NAMESPACE column, [7.3.3.2](memory.md)

V$OSSTAT view, [5.1.2.1](autostat.md)

V$PGASTAT view, [7.5.1.2.1](memory.md)

V$PROCESS view, [7.5.1.2.2](memory.md)

V$PROCESS\_MEMORY view, [7.5.1.2.3](memory.md)

V$QUEUE view, [4.3.2](build_db.md)

V$ROWCACHE view

GETMISSES column, [7.3.4.1.2](memory.md)

GETS column, [7.3.4.1.2](memory.md)

performance statistics, [7.3.3.4](memory.md)

V$RSRC\_CONSUMER\_GROUP view, [10.1.2.1.3](instance_tune.md)

V$SESS\_TIME\_MODEL view, [5.1.1.2](autostat.md), [10.1.3.3](instance_tune.md)

V$SESSION view, [10.1.3.3](instance_tune.md), [10.1.3.4](instance_tune.md), [10.3](instance_tune.md)

V$SESSION\_EVENT view, [10.1.3.3](instance_tune.md), [10.3](instance_tune.md)

V$SESSION\_WAIT view, [10.1.3.3](instance_tune.md), [10.3](instance_tune.md)

V$SESSION\_WAIT\_CLASS view, [10.1.3.3](instance_tune.md)

V$SESSION\_WAIT\_HISTORY view, [10.1.3.3](instance_tune.md), [10.1.3.3](instance_tune.md), [10.3](instance_tune.md)

V$SESSTAT view, [7.3.5.1.2](memory.md), [10.1.2.1.3](instance_tune.md)

V$SHARED\_POOL\_ADVICE view, [7.3.3.3.1](memory.md)

V$SHARED\_POOL\_RESERVED view, [7.3.8.4](memory.md)

V$SQL\_PLAN view

using to display execution plan, [12.1.3.1](ex_plan.md)

V$SQL\_PLAN\_STATISTICS view

using to display execution plan statistics, [12.1.3.1](ex_plan.md)

V$SQL\_PLAN\_STATISTICS\_ALL view

using to display execution plan information, [12.1.3.1](ex_plan.md)

V$SQL\_WORKAREA view, [7.5.1.2.6](memory.md)

V$SQL\_WORKAREA\_ACTIVE view, [7.5.1.2.5](memory.md)

V$SQL\_WORKAREA\_HISTOGRAM view, [7.5.1.2.4](memory.md)

V$SYS\_TIME\_MODEL view, [5.1.1.2](autostat.md), [5.1.2.1](autostat.md), [10.1.3.3](instance_tune.md)

V$SYSMETRIC\_HISTORY view, [5.1.2.1](autostat.md)

V$SYSSTAT view

redo buffer allocation, [7.4.2](memory.md)

using, [7.2.2.3](memory.md)

V$SYSTEM\_EVENT view, [10.1.3.3](instance_tune.md), [10.3](instance_tune.md)

V$SYSTEM\_WAIT\_CLASS view, [10.1.3.3](instance_tune.md)

V$TEMP\_HISTOGRAM view, [10.1.3.3](instance_tune.md)

V$UNDOSTAT view, [4.1.2](build_db.md)

V$WAITSTAT view, [10.1.3.4](instance_tune.md)

validating designs, [2.6.4](design.md)

views, [2.5.4](design.md)

DBA\_HIST, [5.3.5](autostat.md)

statistics, [13.7.1](stats.md)

virtual memory statistics, [5.1.2.2](autostat.md)

vmstat UNIX command, [9.4.1.1.1](os.md)

---

## W

wait events, [5.1.1.1](autostat.md)

buffer busy waits, [10.3.1](instance_tune.md)

classes, [5.1.1.1](autostat.md), [10.1.3.2](instance_tune.md)

contention wait events, [10.3.10](instance_tune.md)

direct path, [10.3.5](instance_tune.md)

enqueue, [10.3.6](instance_tune.md)

free buffer waits, [10.3.8](instance_tune.md)

idle wait events, [10.3.9](instance_tune.md)

latch, [10.3.10](instance_tune.md)

library cache latch, [10.3.10.1](instance_tune.md)

log buffer space, [10.3.14](instance_tune.md)

log file parallel write, [10.3.11](instance_tune.md)

log file switch, [10.3.15](instance_tune.md)

log file sync, [10.3.16](instance_tune.md)

network communication wait events, [10.3.18](instance_tune.md)

rdbms ipc reply, [10.3.17](instance_tune.md)

resource wait events, [10.3.3](instance_tune.md)

Windows performance, [9.2.2](os.md)

workloads, [2.6.2](design.md), [2.6.2.1](design.md), [2.6.2.2](design.md), [2.6.3](design.md), [2.6.4](design.md)