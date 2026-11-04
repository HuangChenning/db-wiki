---
title: Index
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/index.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

A B C D E F G H I J K L M N O P Q R S T U V W X

---

## A

aggregates, [9.2.1](basicmv.md), [19.7.5](qradv.md)

ALL\_PUBLISHED\_COLUMNS view, [17.9.6](cdc.md)

ALTER MATERIALIZED VIEW statement, [9.3](basicmv.md)

altering dimensions, [11.6](dimen.md)

amortization

analysis tools

analytic functions, [23.3.5](sqlmodel.md)

analytic processing

applications

architecture

data warehouse, [1.2](concept.md)

asynchronous Autolog publishing

source database performance impact, [17.6.2](cdc.md), [17.6.2](cdc.md), [17.6.2](cdc.md)

asynchronous AutoLog publishing

latency for, [17.6.2](cdc.md), [17.6.2](cdc.md)

location of staging database, [17.6.2](cdc.md), [17.6.2](cdc.md)

requirements for, [17.6.1.1](cdc.md)

setting database initialization parameters for, [17.6.3.4](cdc.md)

asynchronous Change Data Capture

archived redo log files and, [17.11.1](cdc.md)

ARCHIVELOGMODE and, [17.11.1](cdc.md)

supplemental logging, [17.11.2](cdc.md)

supplemental logging and, [17.2.2](cdc.md)

Asynchronous Change Data Capture

columns of built-in Oracle datatypes supported by, [17.11.4](cdc.md)

asynchronous change sets

disabling, [17.9.2.2](cdc.md)

enabling, [17.9.2.2](cdc.md)

exporting, [17.9.5.1](cdc.md)

importing, [17.9.5.1](cdc.md)

managing, [17.9.2](cdc.md)

recovering from capture errors, [17.9.2.4](cdc.md)

example of, [17.9.2.4.1](cdc.md), [17.9.2.4.2](cdc.md)

removing DDL, [17.9.2.4.2](cdc.md)

specifying ending values for, [17.9.2.1](cdc.md)

specifying starting values for, [17.9.2.1](cdc.md)

stopping capture on DDL, [17.9.2.3](cdc.md)

excluded statements, [17.9.2.3](cdc.md)

asynchronous change tables

exporting, [17.9.5.1](cdc.md)

importing, [17.9.5.1](cdc.md)

asynchronous Hotlog publishing

source database performance impact, [17.6.2](cdc.md)

asynchronous HotLog publishing

latency for, [17.6.2](cdc.md)

location of staging database, [17.6.2](cdc.md)

requirements for, [17.6.1.1](cdc.md)

setting database initialization parameters for, [17.6.3.2](cdc.md), [17.6.3.3](cdc.md), [17.6.3.4](cdc.md), [17.6.3.4](cdc.md)

attributes, [2.2](logical.md), [11.2](dimen.md)

Automatic Storage Management, [4.2](hardware.md)

---

## B

bind variables

with query rewrite, [19.3.11](qradv.md)

bitmap indexes, [7.1](indexes.md)

nulls and, [7.1.3](indexes.md)

on partitioned tables, [7.1.4](indexes.md)

parallel query and DML, [7.1.1](indexes.md), [7.1.1](indexes.md)

bitmap join indexes, [7.1.5](indexes.md)

B-tree indexes, [7.2](indexes.md)

bitmap indexes versus, [7.1.2](indexes.md)

build methods, [9.3.4](basicmv.md)

business intelligence

queries, [24](advbi.md)

business rules

violation of, [15.4.1](transform.md)

---

## C

capture errors

recovering from, [17.9.2.4](cdc.md)

cardinality

degree of, [7.1.2](indexes.md)

CASE expressions, [22.7.3](analysis.md)

cell referencing, [23.2.4](sqlmodel.md)

Change Data Capture, [13.2.3](extract.md)

asynchronous

Streams apply process and, [17.6.4](cdc.md)

Streams capture process and, [17.6.4](cdc.md)

benefits for subscribers, [17.1.3.2](cdc.md)

choosing a mode, [17.6.2](cdc.md)

effects of stopping on DDL, [17.9.2.3](cdc.md)

latency, [17.6.2](cdc.md)

location of staging database, [17.6.2](cdc.md)

modes of data capture

asynchronous AutoLog, [17.2.2.3](cdc.md)

asynchronous Distributed HotLog, [17.2.2.2](cdc.md)

asynchronous HotLog, [17.2.2.1](cdc.md)

synchronous, [17.2.1](cdc.md)

Oracle Data Pump and, [17.9.5](cdc.md)

removing from database, [17.12](cdc.md)

restriction on direct-path INSERT statement, [17.10.1](cdc.md)

setting up, [17.6](cdc.md)

source database performance impact, [17.6.2](cdc.md)

static data dictionary views, [17.5](cdc.md)

supported export utility, [17.9.5](cdc.md)

supported import utility, [17.9.5](cdc.md)

synchronous, [13.2.3.3](extract.md)

systemwide triggers installed by, [17.12](cdc.md)

Change Data Capture publisher

default tablespace for, [17.6.1.2](cdc.md)

change sets

defined, [17.3](cdc.md)

effects of disabling, [17.9.2.2](cdc.md)

managing asynchronous, [17.9.2](cdc.md)

synchronous Change Data Capture and, [17.3](cdc.md)

valid combinations with change sources, [17.3.1](cdc.md)

change sources

asynchronous AutoLog Change Data Capture and, [17.2.2.3](cdc.md)

asynchronous Distributed HotLog Change Data Capture and, [17.2.2.2](cdc.md)

database instance represented, [17.3.1](cdc.md)

defined, [17.1.3.1](cdc.md), [17.1.3.1](cdc.md)

HOTLOG\_SOURCE, [17.2.2.1](cdc.md)

SYNC\_SOURCE, [17.2.1](cdc.md)

valid combinations with change sets, [17.3.1](cdc.md)

change tables

adding a column to, [17.9.6](cdc.md)

control columns, [17.9.4.2](cdc.md)

defined, [17.1.3.1](cdc.md)

dropping, [17.9.4.7](cdc.md)

dropping with active subscribers, [17.9.4.7](cdc.md)

effect of SQL DROP USER CASCADE statement on, [17.9.4.7](cdc.md)

exporting, [17.9.5](cdc.md)

granting subscribers access to, [17.9.4.5](cdc.md)

importing, [17.9.5](cdc.md)

importing for Change Data Capture, [17.9.5.3](cdc.md)

managing, [17.9.4](cdc.md)

purging all in a named change set, [17.9.4.6](cdc.md)

purging all on staging database, [17.9.4.6](cdc.md)

purging by name, [17.9.4.6](cdc.md)

purging of unneeded data, [17.9.4.6](cdc.md)

source tables referenced by, [17.9.4.1](cdc.md)

tablespaces created in, [17.9.4.1](cdc.md)

change-value selection, [17.1.1](cdc.md)

columns

cardinality, [7.1.2](indexes.md)

COMMIT\_TIMESTAMP$

control column, [17.9.4.2](cdc.md)

common joins, [19.1.3.1.1](qradv.md)

COMPLETE clause, [9.3.7](basicmv.md)

complete refresh, [16.3.1](refresh.md)

complex queries

snowflake schemas, [20.3.1](schemas.md)

composite

columns, [21.6](aggreg.md)

compression

See data segment compression, [9.3.3](basicmv.md)

concatenated groupings, [21.7](aggreg.md)

concatenated ROLLUP, [21.10.1](aggreg.md)

configuration

bandwidth, [4.1.1](hardware.md)

constraints, [8.1](constra.md), [11.4](dimen.md)

foreign key, [8.3.2](constra.md)

RELY, [8.3.3](constra.md)

states, [8.2](constra.md)

unique, [8.3.1](constra.md)

view, [8.3.7](constra.md), [19.3.6](qradv.md)

with partitioning, [8.3.6](constra.md)

with query rewrite, [19.7.1](qradv.md)

control columns

used to indicate changed columns in a row, [17.9.4.3](cdc.md)

controls columns

COMMIT\_TIMESTAMP$, [17.9.4.2](cdc.md)

CSCN$, [17.9.4.2](cdc.md)

OPERATION$, [17.9.4.2](cdc.md)

ROW\_ID$, [17.9.4.2](cdc.md)

RSID$, [17.9.4.2](cdc.md)

SOURCE\_COLMAP$, [17.9.4.2](cdc.md)

interpreting, [17.9.4.3](cdc.md)

SYS\_NC\_OID$, [17.9.4.2](cdc.md)

TARGET\_COLMAP$, [17.9.4.2](cdc.md)

interpreting, [17.9.4.3](cdc.md)

TIMESTAMP$, [17.9.4.2](cdc.md)

USERNAME$, [17.9.4.2](cdc.md)

XIDSEQ$, [17.9.4.2](cdc.md)

XIDSLT$, [17.9.4.2](cdc.md)

XIDUSN$, [17.9.4.2](cdc.md)

cost-based rewrite, [19.1.1](qradv.md)

CREATE DIMENSION statement, [11.2](dimen.md)

CREATE MATERIALIZED VIEW statement, [9.3](basicmv.md)

enabling query rewrite, [18.2](qrbasic.md)

CREATE SESSION privilege, [17.6.1.1](cdc.md)

CREATE TABLE privilege, [17.6.1.1](cdc.md)

CSCN$

control column, [17.9.4.2](cdc.md)

CUBE clause, [21.3](aggreg.md)

partial, [21.3.3](aggreg.md)

when to use, [21.3.1](aggreg.md)

cubes

hierarchical, [10.2.1](advmv.md)

materialized views, [10.2.1](advmv.md)

CUME\_DIST function, [22.2.1.3](analysis.md)

---

## D

data

partitioning, [5.1](parpart.md)

purging, [16.2.3](refresh.md), [16.2.3](refresh.md)

sufficiency check, [19.1.3.2](qradv.md)

transformation, [15.3](transform.md)

transportation, [14.2.1](transport.md)

data compression

See data segment compression, [9.3.3](basicmv.md)

data cubes

hierarchical, [21.7.1](aggreg.md)

data densification, [22.5](analysis.md)

time series calculation, [22.6](analysis.md)

with sparse data, [22.5.2](analysis.md)

data dictionary

asynchronous change data capture and, [17.7.4](cdc.md)

data extraction

with and without Change Data Capture, [17.1.2](cdc.md)

data marts, [1.2.3](concept.md)

data rules

violation of, [15.4.2](transform.md)

data segment compression, [3.2.3.1](physical.md)

materialized views, [9.3.3](basicmv.md)

partitioning, [3.2.3.1](physical.md)

data transformation

multistage, [15.1.1.1](transform.md)

pipelined, [15.1.1.2](transform.md)

data warehouse, [9.1](basicmv.md)

architectures, [1.2](concept.md)

dimension tables, [9.1.6](basicmv.md)

dimensions, [20.3](schemas.md)

fact tables, [9.1.6](basicmv.md)

logical design, [2.2](logical.md)

physical design, [3.1](physical.md)

refresh tips, [16.3.9](refresh.md)

star queries, [20.3](schemas.md)

database

staging, [9.1](basicmv.md)

database initialization parameters

adjusting when Streams values change, [17.6.4](cdc.md)

date folding

with query rewrite, [19.3.5](qradv.md)

DBA role, [17.6.1.1](cdc.md)

DBMS\_ADVISOR.TUNE\_MVIEW package, [9.3.5](basicmv.md)

DBMS\_CDC\_PUBLISH package, [17.1.3.1](cdc.md)

privileges required to use, [17.6.1.1](cdc.md)

DBMS\_CDC\_PUBLISH.DROP\_CHANGE\_TABLE PL/SQL procedure, [17.9.4.7](cdc.md)

DBMS\_CDC\_PUBLISH.PURGE PL/SQL procedure, [17.9.4.6](cdc.md), [17.9.4.6](cdc.md)

DBMS\_CDC\_PUBLISH.PURGE\_CHANG\_SET PL/SQL procedure, [17.9.4.6](cdc.md)

DBMS\_CDC\_PUBLISH.PURGE\_CHANGE\_TABLE PL/SQL procedure, [17.9.4.6](cdc.md)

DBMS\_CDC\_SUBSCRIBE package, [17.1.3.2](cdc.md)

DBMS\_CDC\_SUBSCRIBE.PURGE\_WINDOW PL/SQL procedure, [17.9.4.6](cdc.md)

DBMS\_ERROR package, [15.4.2.2](transform.md)

DBMS\_JOB package, [17.9.4.6](cdc.md)

DBMS\_MVIEW package, [16.3.5](refresh.md), [16.3.5](refresh.md)

EXPLAIN\_MVIEW procedure, [9.7.1](basicmv.md)

EXPLAIN\_REWRITE procedure, [19.6.2](qradv.md)

REFRESH procedure, [16.3](refresh.md), [16.3.6](refresh.md)

REFRESH\_ALL\_MVIEWS procedure, [16.3](refresh.md)

REFRESH\_DEPENDENT procedure, [16.3](refresh.md)

DBMS\_STATS package, [19.1.1](qradv.md)

decision support systems (DSS)

bitmap indexes, [7.1.1](indexes.md)

degree of cardinality, [7.1.2](indexes.md)

DENSE\_RANK function, [22.2.1.1](analysis.md)

densification

data, [22.5](analysis.md)

design

logical, [3.1](physical.md)

physical, [3.1](physical.md)

dimension levels

skipping, [11.2](dimen.md)

dimension tables, [2.4](logical.md), [9.1.6](basicmv.md)

normalized, [11.2.3](dimen.md)

dimensional modeling, [2.2](logical.md)

dimensions, [2.4.2](logical.md), [11.1](dimen.md), [11.4](dimen.md)

altering, [11.6](dimen.md)

analyzing, [21.1.1](aggreg.md)

creating, [11.2](dimen.md)

definition, [11.1](dimen.md)

dimension tables, [9.1.6](basicmv.md)

dropping, [11.7](dimen.md)

hierarchies, [2.4.2.1](logical.md)

hierarchies overview, [2.4.2.1](logical.md)

multiple, [21.1.1](aggreg.md)

skipping levels, [11.2](dimen.md)

star joins, [20.3](schemas.md)

star queries, [20.3](schemas.md)

validating, [11.5](dimen.md)

with query rewrite, [19.7.2](qradv.md)

direct-path INSERT statement

Change Data Capture restriction, [17.10.1](cdc.md)

disk redundancy, [4.1.3](hardware.md)

DML access

subscribers, [17.9.4.5](cdc.md)

downstream capture, [17.7.4](cdc.md)

drilling down, [11.1](dimen.md)

hierarchies, [11.1](dimen.md)

DROP MATERIALIZED VIEW statement, [9.3](basicmv.md)

prebuilt tables, [9.4](basicmv.md)

dropping

dimensions, [11.7](dimen.md)

materialized views, [9.6](basicmv.md)

dropping change tables, [17.9.4.7](cdc.md)

---

## E

ENFORCED mode, [18.2.3](qrbasic.md)

entity, [2.2](logical.md)

error logging, [15.4](transform.md)

table, [15.4.2.2](transform.md)

errors

handling, [15.4](transform.md)

ORA-31424, [17.9.4.7](cdc.md)

ORA-31496, [17.9.4.7](cdc.md)

ETL. See extraction, transformation, and loading (ETL), [12.1](ettover.md)

EXCHANGE PARTITION statement, [8.3.6](constra.md)

EXECUTE privilege, [17.6.1.1](cdc.md)

EXECUTE\_CATALOG\_ROLE privilege, [17.6.1.1](cdc.md)

execution plans

star transformations, [20.4.2.2](schemas.md)

EXPAND\_GSET\_TO\_UNION hint, [19.3.8.2](qradv.md), [19.7.10.4](qradv.md)

EXPLAIN PLAN statement, [19.6.1](qradv.md)

star transformations, [20.4.2.2](schemas.md)

EXPLAIN\_REWRITE procedure, [19.6.2](qradv.md)

exporting

a change table, [17.9.5](cdc.md)

asynchronous change sets, [17.9.5.1](cdc.md)

asynchronous change tables, [17.9.5.1](cdc.md)

EXP utility, [13.3.1.3](extract.md)

expression matching

with query rewrite, [19.3.10](qradv.md)

external tables, [15.2.2](transform.md)

extraction, transformation, and loading (ETL), [12.1](ettover.md)

overview, [12.1](ettover.md)

process, [8.1](constra.md)

extractions

data files, [13.3.1](extract.md)

distributed operations, [13.3.2](extract.md)

full, [13.2.1](extract.md)

incremental, [13.2.1.2](extract.md)

OCI, [13.3.1.2](extract.md)

online, [13.2.2.1](extract.md)

overview, [13.1](extract.md)

physical, [13.2.2](extract.md)

Pro\*C, [13.3.1.2](extract.md)

SQL\*Plus, [13.3.1.1](extract.md)

---

## F

fact tables, [2.4](logical.md), [2.4.1](logical.md)

star joins, [20.3](schemas.md)

star queries, [20.3](schemas.md)

facts, [11.1](dimen.md)

FAST clause, [9.3.7](basicmv.md)

fast refresh, [16.3.2](refresh.md)

restrictions, [9.3.7.1](basicmv.md)

with UNION ALL, [16.3.18](refresh.md)

features, new, [Preface](whatsnew.md)

files

ultralarge, [3.2.2](physical.md)

filling gaps

with data, [22.5.6](analysis.md)

FIRST\_VALUE function, [22.2.5.1](analysis.md)

FIRST/LAST functions, [22.3.2](analysis.md)

FOR loops, [23.3.1](sqlmodel.md)

FORCE clause, [9.3.7](basicmv.md)

foreign key

constraints, [8.3.2](constra.md)

joins

snowflake schemas, [20.3.1](schemas.md)

frequent itemsets, [22.7.4](analysis.md)

functions

analytic, [23.3.5](sqlmodel.md)

COUNT, [7.1.3](indexes.md)

CUME\_DIST, [22.2.1.3](analysis.md)

DENSE\_RANK, [22.2.1.1](analysis.md)

FIRST\_VALUE, [22.2.5.1](analysis.md)

FIRST/LAST, [22.3.2](analysis.md)

GROUP\_ID, [21.4.4](aggreg.md)

GROUPING, [21.4](aggreg.md)

GROUPING\_ID, [21.4.3](aggreg.md)

LAG/LEAD, [22.2.4](analysis.md)

LAST\_VALUE, [22.2.5.1](analysis.md)

linear regression, [22.3.5](analysis.md)

LISTAGG, [22.3.1](analysis.md)

NTH\_VALUE, [22.2.5.2](analysis.md)

NTILE, [22.2.1.5](analysis.md)

PERCENT\_RANK, [22.2.1.4](analysis.md)

RANK, [22.2.1.1](analysis.md)

ranking, [22.2.1](analysis.md)

RATIO\_TO\_REPORT, [22.2.3.1](analysis.md)

REGR\_AVGX, [22.3.5.2](analysis.md)

REGR\_AVGY, [22.3.5.2](analysis.md)

REGR\_COUNT, [22.3.5.1](analysis.md)

REGR\_INTERCEPT, [22.3.5.3](analysis.md)

REGR\_SLOPE, [22.3.5.3](analysis.md)

REGR\_SXX, [22.3.5.5](analysis.md)

REGR\_SXY, [22.3.5.5](analysis.md)

REGR\_SYY, [22.3.5.5](analysis.md)

reporting, [22.2.3](analysis.md)

ROW\_NUMBER, [22.2.1.6](analysis.md)

WIDTH\_BUCKET, [22.7.1](analysis.md), [22.7.1.1](analysis.md)

window, [23.3.5](sqlmodel.md)

windowing, [22.2.2](analysis.md)

---

## G

GRANT statement, [17.9.4.5](cdc.md)

GROUP\_ID function, [21.4.4](aggreg.md)

grouping

compatibility check, [19.1.3.3](qradv.md)

conditions, [19.7.6](qradv.md)

GROUPING function, [21.4](aggreg.md)

when to use, [21.4.2](aggreg.md)

GROUPING\_ID function, [21.4.3](aggreg.md)

GROUPING\_SETS expression, [21.5](aggreg.md)

GT GlossaryTitle, [Glossary](glossary.md)

---

## H

hierarchical cubes, [10.2.1](advmv.md), [21.10.1](aggreg.md)

in SQL, [21.10](aggreg.md)

hierarchies, [11.1](dimen.md)

how used, [2.4.2.1](logical.md)

multiple, [11.2.2](dimen.md)

overview, [2.4.2.1](logical.md), [2.4.2.1](logical.md)

rolling up and drilling down, [11.1](dimen.md)

high boundary

defined, [17.1.3.2](cdc.md)

hints

EXPAND\_GSET\_TO\_UNION, [19.3.8.2](qradv.md), [19.7.10.4](qradv.md)

NOWRITE, [19.7.10.1](qradv.md)

query rewrite, [18.2](qrbasic.md), [19.7.10.1](qradv.md)

REWRITE, [19.7.10.1](qradv.md)

REWRITE\_OR\_ERROR, [19.7.10.2](qradv.md)

histograms

creating with user-defined buckets, [22.7.3.1](analysis.md)

HOTLOG\_SOURCE change sources, [17.2.2.1](cdc.md)

hypothetical rank, [22.3.4](analysis.md)

---

## I

importing

a change table, [17.9.5](cdc.md), [17.9.5.3](cdc.md)

asynchronous change sets, [17.9.5.1](cdc.md)

asynchronous change tables, [17.9.5.1](cdc.md)

data into a source table, [17.9.5.3](cdc.md)

indexes

bitmap indexes, [7.1.4](indexes.md)

bitmap join, [7.1.5](indexes.md)

B-tree, [7.2](indexes.md)

cardinality, [7.1.2](indexes.md)

nulls and, [7.1.3](indexes.md)

partitioned tables, [7.1.4](indexes.md)

initcdc.sql script, [17.12](cdc.md)

initialization parameters

JOB\_QUEUE\_PROCESSES, [16.3.9](refresh.md)

OPTIMIZER\_MODE, [16.3.11](refresh.md), [18.2.1](qrbasic.md)

PARALLEL\_MAX\_SERVERS, [16.3.11](refresh.md)

PGA\_AGGREGATE\_TARGET, [16.3.11](refresh.md)

QUERY\_REWRITE\_ENABLED, [18.2](qrbasic.md), [18.2.1](qrbasic.md)

QUERY\_REWRITE\_INTEGRITY, [18.2.1](qrbasic.md)

STAR\_TRANSFORMATION\_ENABLED, [20.4.1](schemas.md)

integrity constraints, [8.1](constra.md)

invalidating

materialized views, [10.4](advmv.md)

itemsets

frequent, [22.7.4](analysis.md)

---

## J

Java

used by Change Data Capture, [17.12](cdc.md)

JOB\_QUEUE\_PROCESSES initialization parameter, [16.3.9](refresh.md)

join compatibility, [19.1.3.1](qradv.md)

joins

star joins, [20.3](schemas.md)

star queries, [20.3](schemas.md)

---

## K

key lookups, [15.5.1](transform.md)

keys, [9.1.6](basicmv.md), [20.3](schemas.md)

---

## L

LAG/LEAD functions, [22.2.4](analysis.md)

LAST\_VALUE function, [22.2.5.1](analysis.md)

level relationships, [2.4.2.1](logical.md)

purpose, [2.4.2.1.2](logical.md)

levels, [2.4.2](logical.md), [2.4.2.1.1](logical.md)

levels in a dimension

skipping, [11.2](dimen.md)

linear regression functions, [22.3.5](analysis.md)

LISTAGG function, [22.3.1](analysis.md)

local indexes, [7.1.1](indexes.md), [7.1.4](indexes.md)

logging

error, [15.4](transform.md)

logical design, [3.1](physical.md)

logs

materialized views, [9.3.9](basicmv.md)

lookup tables

See dimension tables, [9.1.6](basicmv.md), [9.1.6](basicmv.md)

low boundary

defined, [17.1.3.2](cdc.md)

---

## M

manual

refresh, [16.3.5](refresh.md)

manual refresh

with DBMS\_MVIEW package, [16.3.5](refresh.md)

materialized view logs, [9.3.9](basicmv.md)

materialized views

aggregates, [9.2.1](basicmv.md)

altering, [10.6](advmv.md)

analytic processing, [10.2](advmv.md)

build methods, [9.3.4](basicmv.md)

checking status, [16.3.13](refresh.md)

containing only joins, [9.2.2](basicmv.md)

creating, [9.3](basicmv.md)

cubes, [10.2.1](advmv.md)

data segment compression, [9.3.3](basicmv.md)

delta joins, [19.1.3.1.3](qradv.md)

dropping, [9.4](basicmv.md), [9.6](basicmv.md)

invalidating, [10.4](advmv.md)

logs, [13.2.3.3](extract.md)

multiple, [19.2.8](qradv.md)

naming, [9.3.2](basicmv.md)

nested, [9.2.3](basicmv.md)

Partition Change Tracking (PCT), [10.1.1](advmv.md)

partitioned tables, [16.4](refresh.md)

partitioning, [10.1](advmv.md)

prebuilt, [9.3](basicmv.md)

query rewrite

hints, [18.2](qrbasic.md), [19.7.10.1](qradv.md)

matching join graphs, [9.3.6](basicmv.md)

parameters, [18.2.1](qrbasic.md)

privileges, [18.2.4](qrbasic.md)

refresh dependent, [16.3.8](refresh.md)

refreshing, [9.3.7](basicmv.md), [16.3](refresh.md)

refreshing all, [16.3.7](refresh.md)

registration, [9.4](basicmv.md)

restrictions, [9.3.6.1](basicmv.md)

rewrites

enabling, [18.2](qrbasic.md)

schema design, [9.1.7](basicmv.md)

schema design guidelines, [9.1.7](basicmv.md)

security, [10.5](advmv.md), [10.5](advmv.md)

set operators, [10.2.4](advmv.md)

storage characteristics, [9.3.3](basicmv.md)

types of, [9.2](basicmv.md)

uses for, [9.1](basicmv.md)

with VPD, [10.5.1](advmv.md)

measures, [9.1.6](basicmv.md), [20.3](schemas.md)

MERGE statement, [16.2.1](refresh.md)

Change Data Capture restriction, [17.10.1](cdc.md)

MODEL clause, [23.1](sqlmodel.md)

cell referencing, [23.2.4](sqlmodel.md)

data flow, [23.1.1](sqlmodel.md)

keywords, [23.2.3](sqlmodel.md)

parallel execution, [23.4.1](sqlmodel.md)

rules, [23.2.5](sqlmodel.md)

monitoring

refresh, [16.3.12](refresh.md)

mortgage calculation, [23.5](sqlmodel.md)

multiple hierarchies, [11.2.2](dimen.md)

multiple materialized views, [19.2.8](qradv.md)

MV\_CAPABILITIES\_TABLE table, [9.7.1.2](basicmv.md)

---

## N

nested materialized views, [9.2.3](basicmv.md)

refreshing, [16.3.17](refresh.md)

restrictions, [9.2.3.4](basicmv.md)

net present value

NEVER clause, [9.3.7](basicmv.md)

new features, [Preface](whatsnew.md)

nonvolatile data, [1.1.3](concept.md)

NOREWRITE hint, [18.2](qrbasic.md), [19.7.10.1](qradv.md)

NTH\_VALUE function, [22.2.5.2](analysis.md)

NTILE function, [22.2.1.5](analysis.md)

nulls

indexes and, [7.1.3](indexes.md)

---

## O

ON COMMIT clause, [9.3.7](basicmv.md)

ON DEMAND clause, [9.3.7](basicmv.md)

OPERATION$

control column, [17.9.4.2](cdc.md)

optimizations

query rewrite

enabling, [18.2](qrbasic.md)

hints, [18.2](qrbasic.md), [19.7.10.1](qradv.md)

matching join graphs, [9.3.6](basicmv.md)

query rewrites

privileges, [18.2.4](qrbasic.md)

optimizer

with rewrite, [18.1](qrbasic.md)

OPTIMIZER\_MODE initialization parameter, [16.3.11](refresh.md), [18.2.1](qrbasic.md)

ORA-31424 error, [17.9.4.7](cdc.md)

ORA-31496 error, [17.9.4.7](cdc.md)

Oracle Data Pump

using with Change Data Capture, [17.9.5](cdc.md)

ORDER BY clause, [9.3.8](basicmv.md)

outer joins

with query rewrite, [19.7.3](qradv.md)

---

## P

packages

DBMS\_ADVISOR, [9.1.4](basicmv.md)

DBMS\_CDC\_PUBLISH, [17.1.2](cdc.md)

DBMS\_CDC\_SUBSCRIBE, [17.1.2](cdc.md)

DBMS\_DIMENSION, [11.3.2](dimen.md)

DBMS\_ERROR, [15.4.2.2](transform.md)

DBMS\_ERRORLOG, [15.4.2.2](transform.md), [15.5.3](transform.md)

DBMS\_JOB, [17.9.4.6](cdc.md)

DBMS\_MVIEW, [9.7.1.1](basicmv.md), [16.3](refresh.md)

DBMS\_STATS, [19.1.1](qradv.md)

paragraph tags

GT GlossaryTitle, [Glossary](glossary.md)

parallel DML

bitmap indexes, [7.1.1](indexes.md)

parallel execution, [6.1](px.md)

parallel query

bitmap indexes, [7.1.1](indexes.md)

PARALLEL\_MAX\_SERVERS initialization parameter, [16.3.11](refresh.md)

parallelism, [6.1](px.md)

Partition Change Tracking (PCT), [10.1.1](advmv.md), [16.4.1](refresh.md), [19.2.7](qradv.md)

refresh, [16.3.3](refresh.md)

with Pmarkers, [19.2.7.4](qradv.md)

partitioned outer join, [22.5](analysis.md)

partitioned tables

materialized views, [16.4](refresh.md)

partitioning, [13.2.3.2](extract.md)

data, [5.1](parpart.md)

in data warehouses, [5](parpart.md)

materialized views, [10.1](advmv.md)

prebuilt tables, [10.1.3](advmv.md)

partitions

bitmap indexes, [7.1.4](indexes.md)

PERCENT\_RANK function, [22.2.1.4](analysis.md)

PGA\_AGGREGATE\_TARGET initialization parameter, [16.3.11](refresh.md)

physical design, [3.1](physical.md)

structures, [3.2.1](physical.md)

pivoting, [15.5.4](transform.md), [15.5.4](transform.md), [22.4](analysis.md)

operations, [22.4](analysis.md)

plans

star transformations, [20.4.2.2](schemas.md)

PL/SQL procedures

DBMS\_CDC\_PUBLISH\_DROP\_CHANGE\_TABLE, [17.9.4.7](cdc.md)

DBMS\_CDC\_PUBLISH.PURGE, [17.9.4.6](cdc.md), [17.9.4.6](cdc.md)

DBMS\_CDC\_PUBLISH.PURGE\_CHANGE\_SET, [17.9.4.6](cdc.md)

DBMS\_CDC\_PUBLISH.PURGE\_CHANGE\_TABLE, [17.9.4.6](cdc.md)

DBMS\_CDC\_SUBSCRIBE.PURGE\_WINDOW, [17.9.4.6](cdc.md)

Pmarkers

with PCT, [19.2.7.4](qradv.md)

prebuilt materialized views, [9.3](basicmv.md)

privileges required

to publish change data, [17.6.1.1](cdc.md)

publication

defined, [17.1.3.1](cdc.md)

publishers

components associated with, [17.1.3.1](cdc.md)

defined, [17.1.3](cdc.md)

determining the source tables, [17.1.3.1](cdc.md)

privileges for reading views, [17.5](cdc.md)

purpose, [17.1.3.1](cdc.md)

table partitioning properties and, [17.9.4.1](cdc.md)

tasks, [17.1.3.1](cdc.md)

publishing

asynchronous AutoLog mode

step-by-step example, [17.7.4](cdc.md)

asynchronous HotLog mode

step-by-step example, [17.7.2](cdc.md)

synchronous mode

step-by-step example, [17.7.1](cdc.md)

publishing change data

preparations for, [17.6](cdc.md)

privileges required, [17.6.1.1](cdc.md)

purging change tables

automatically, [17.9.4.6](cdc.md)

by name, [17.9.4.6](cdc.md)

in a named changed set, [17.9.4.6](cdc.md)

on the staging database, [17.9.4.6](cdc.md)

publishers, [17.9.4.6](cdc.md)

subscribers, [17.9.4.6](cdc.md)

purging data, [16.2.3](refresh.md)

---

## Q

queries

query delta joins, [19.1.3.1.2](qradv.md)

query rewrite

advanced, [19.4](qradv.md)

checks made by, [19.1.3](qradv.md)

controlling, [18.2.2](qrbasic.md)

correctness, [18.2.3](qrbasic.md)

date folding, [19.3.5](qradv.md)

enabling, [18.2](qrbasic.md), [18.2](qrbasic.md)

hints, [18.2](qrbasic.md), [19.7.10.1](qradv.md)

matching join graphs, [9.3.6](basicmv.md)

methods, [19.1](qradv.md)

parameters, [18.2.1](qrbasic.md)

privileges, [18.2.4](qrbasic.md)

restrictions, [9.3.6.2](basicmv.md)

using equivalences, [19.4](qradv.md)

using GROUP BY extensions, [19.3.8.1](qradv.md)

using nested materialized views, [19.3.1](qradv.md)

using PCT, [19.2.7](qradv.md)

VPD, [10.5.1.1](advmv.md)

when it occurs, [18.1.1](qrbasic.md)

with bind variables, [19.3.11](qradv.md)

with DBMS\_MVIEW package, [19.6.2](qradv.md)

with expression matching, [19.3.10](qradv.md)

with inline views, [19.3.2](qradv.md)

with partially stale materialized views, [19.3.10.1](qradv.md)

with selfjoins, [19.3.4](qradv.md)

with set operator materialized views, [19.3.7](qradv.md)

with view constraints, [19.3.6](qradv.md)

query tools

QUERY\_REWRITE\_ENABLED initialization parameter, [18.2](qrbasic.md), [18.2.1](qrbasic.md)

QUERY\_REWRITE\_INTEGRITY initialization parameter, [18.2.1](qrbasic.md)

---

## R

RANK function, [22.2.1.1](analysis.md)

ranking functions, [22.2.1](analysis.md)

RATIO\_TO\_REPORT function, [22.2.3.1](analysis.md)

recovery

from asynchronous change set capture errors, [17.9.2.4](cdc.md)

redo log files

archived

asynchronous Change Data Capture and, [17.11.1](cdc.md)

determining which are no longer needed by Change Data Capture, [17.11.1](cdc.md)

reference tables

See dimension tables, [9.1.6](basicmv.md)

refresh

monitoring, [16.3.12](refresh.md)

options, [9.3.7](basicmv.md)

Partition Change Tracking (PCT), [16.3.3](refresh.md)

scheduling, [16.3.14](refresh.md)

with UNION ALL, [16.3.18](refresh.md)

refreshing

materialized views, [16.3](refresh.md)

nested materialized views, [16.3.17](refresh.md)

partitioning, [16.1](refresh.md)

REGR\_AVGX function, [22.3.5.2](analysis.md)

REGR\_AVGY function, [22.3.5.2](analysis.md)

REGR\_COUNT function, [22.3.5.1](analysis.md)

REGR\_INTERCEPT function, [22.3.5.3](analysis.md)

REGR\_R2 function, [22.3.5.4](analysis.md)

REGR\_SLOPE function, [22.3.5.3](analysis.md)

REGR\_SXX function, [22.3.5.5](analysis.md)

REGR\_SXY function, [22.3.5.5](analysis.md)

REGR\_SYY function, [22.3.5.5](analysis.md)

RELY constraints, [8.3.3](constra.md)

removing

Change Data Capture from source database, [17.12](cdc.md)

reporting functions, [22.2.3](analysis.md)

restrictions

fast refresh, [9.3.7.1](basicmv.md)

nested materialized views, [9.2.3.4](basicmv.md)

query rewrite, [9.3.6.2](basicmv.md)

result set, [20.4.2](schemas.md)

REVOKE statement, [17.9.4.5](cdc.md)

REWRITE hint, [18.2](qrbasic.md), [19.7.10.1](qradv.md), [19.7.10.1](qradv.md)

REWRITE\_OR\_ERROR hint, [19.7.10.2](qradv.md)

rewrites

hints, [19.7.10.1](qradv.md)

parameters, [18.2.1](qrbasic.md)

privileges, [18.2.4](qrbasic.md)

query optimizations

hints, [18.2](qrbasic.md), [19.7.10.1](qradv.md)

matching join graphs, [9.3.6](basicmv.md)

rmcdc.sql script, [17.12](cdc.md)

rolling up hierarchies, [11.1](dimen.md)

ROLLUP, [21.2](aggreg.md)

concatenated, [21.10.1](aggreg.md)

partial, [21.2.3](aggreg.md)

when to use, [21.2.1](aggreg.md)

root level, [2.4.2.1.1](logical.md)

ROW\_ID$

control column, [17.9.4.2](cdc.md)

ROW\_NUMBER function, [22.2.1.6](analysis.md)

RSID$

control column, [17.9.4.2](cdc.md)

rules

in MODEL clause, [23.2.5](sqlmodel.md)

in SQL modeling, [23.2.5](sqlmodel.md)

order of evaluation, [23.2.6](sqlmodel.md)

---

## S

schema-level export operations, [17.9.5.1](cdc.md)

schema-level import operations, [17.9.5.1](cdc.md)

schemas, [20.1](schemas.md)

design guidelines for materialized views, [9.1.7](basicmv.md)

snowflake, [2.3](logical.md)

star, [2.3](logical.md)

third normal form, [20.1](schemas.md), [20.2](schemas.md)

scripts

initcdc.sql for Change Data Capture, [17.12](cdc.md)

rmcdc.sql for Change Data Capture, [17.12](cdc.md)

SELECT\_CATALOG\_ROLE privilege, [17.5](cdc.md), [17.6.1.1](cdc.md)

set operators

materialized views, [10.2.4](advmv.md)

simultaneous equations, [23.5](sqlmodel.md)

SKIP WHEN NULL clause, [11.2](dimen.md)

skipping levels in a dimension, [11.2](dimen.md)

snowflake schemas, [20.3.1](schemas.md)

complex queries, [20.3.1](schemas.md)

source database

defined, [17.1.3.1](cdc.md)

source systems, [13.1](extract.md)

source tables

importing for Change Data Capture, [17.9.5.3](cdc.md)

referenced by change tables, [17.9.4.1](cdc.md)

SOURCE\_COLMAP$

control column, [17.9.4.2](cdc.md)

interpreting, [17.9.4.3](cdc.md)

sparse data

data densification, [22.5.2](analysis.md)

SQL modeling, [23.1](sqlmodel.md)

cell referencing, [23.2.4](sqlmodel.md)

keywords, [23.2.3](sqlmodel.md)

order of evaluation, [23.2.6](sqlmodel.md)

performance, [23.4](sqlmodel.md)

rules, [23.2.5](sqlmodel.md)

rules and restrictions, [23.3.7](sqlmodel.md)

staging

areas, [1.2.2](concept.md)

databases, [9.1](basicmv.md)

files, [9.1](basicmv.md)

staging database

defined, [17.1.3.1](cdc.md)

STALE\_TOLERATED mode, [18.2.3](qrbasic.md)

star joins, [20.3](schemas.md)

star queries, [20.3](schemas.md)

star transformation, [20.4.2](schemas.md)

star schemas

advantages, [2.3.1](logical.md)

defining fact tables, [2.4.1.1](logical.md)

dimensional model, [2.3.1](logical.md), [20.3](schemas.md)

star transformations, [20.4.2](schemas.md)

restrictions, [20.4.2.6](schemas.md)

STAR\_TRANSFORMATION\_ENABLED initialization parameter, [20.4.1](schemas.md)

statistics, [19.7.9](qradv.md)

Streams apply process

asynchronous Change Data Capture and, [17.6.4](cdc.md)

Streams capture process

asynchronous Change Data Capture and, [17.6.4](cdc.md)

striping, [4.1.2](hardware.md)

subscriber view

defined, [17.1.3.2](cdc.md)

returning DML changes in order, [17.9.4.2](cdc.md), [17.9.4.2](cdc.md)

subscribers

access to change tables, [17.9.4.5](cdc.md)

ALL\_PUBLISHED\_COLUMNS view, [17.9.6](cdc.md)

components associated with, [17.1.3.2](cdc.md)

controlling access to tables, [17.9.4.5](cdc.md)

defined, [17.1.3](cdc.md)

DML access, [17.9.4.5](cdc.md)

privileges, [17.1.3.2](cdc.md)

purpose, [17.1.3.2](cdc.md)

retrieve change data from the subscriber views, [17.1.3.2](cdc.md)

tasks, [17.1.3.2](cdc.md)

subscribing

step-by-step example, [17.8](cdc.md)

subscription windows

defined, [17.1.3.2](cdc.md)

subscriptions

changes to change tables and, [17.9.6](cdc.md)

defined, [17.1.3.2](cdc.md)

effect of SQL DROP USER CASCADE statement on, [17.9.4.7](cdc.md)

summary management

components, [9.1.5](basicmv.md)

summary tables, [2.4.1](logical.md)

supplemental logging

asynchronous Change Data Capture, [17.11.2](cdc.md)

asynchronous Change Data Capture and, [17.2.2](cdc.md)

SYNC\_SET predefined change set, [17.3](cdc.md)

SYNC\_SOURCE change source, [17.2.1](cdc.md)

synchronous Change Data Capture

change sets and, [17.3](cdc.md)

synchronous change sets

disabling, [17.9.2.2](cdc.md)

enabling, [17.9.2.2](cdc.md)

synchronous publishing

latency for, [17.6.2](cdc.md)

location of staging database, [17.6.2](cdc.md)

requirements for, [17.7.1](cdc.md)

setting database initialization parameters for, [17.6.3.1](cdc.md)

source database performance impact, [17.6.2](cdc.md)

SYS\_NC\_OID$

control column, [17.9.4.2](cdc.md)

---

## T

table differencing, [17.1.1](cdc.md)

table partitioning

publisher and, [17.9.4.1](cdc.md)

tables

detail tables, [9.1.6](basicmv.md)

dimension tables (lookup tables), [9.1.6](basicmv.md)

dimensions

external, [15.2.2](transform.md)

fact tables, [9.1.6](basicmv.md)

lookup, [20.3](schemas.md)

tablespace

specifying default for Change Data Capture publisher, [17.6.1.2](cdc.md)

tablespaces

change tables and, [17.9.4.1](cdc.md)

transportable, [13.2.2.2](extract.md), [14.2.3](transport.md), [14.2.3.2](transport.md)

TARGET\_COLMAP$

control column, [17.9.4.2](cdc.md)

interpreting, [17.9.4.3](cdc.md)

text match, [19.2.1](qradv.md)

with query rewrite, [19.7.4](qradv.md)

third normal form

queries, [20.2.1](schemas.md)

schemas, [20.2](schemas.md)

time series calculations, [22.6](analysis.md)

TIMESTAMP$

control column, [17.9.4.2](cdc.md)

timestamps, [13.2.3.1](extract.md)

transformations, [15.1](transform.md)

scenarios, [15.5](transform.md)

SQL and PL/SQL, [15.3.1](transform.md)

SQL\*Loader, [15.2.1](transform.md)

transportable tablespaces, [13.2.2.2](extract.md), [14.2.3](transport.md), [14.2.3.2](transport.md)

transportation

definition, [14.1](transport.md)

distributed operations, [14.2.2](transport.md)

flat files, [14.2.1](transport.md)

triggers, [13.2.3.3](extract.md)

installed by Change Data Capture, [17.12](cdc.md)

TRUSTED mode, [18.2.3](qrbasic.md)

---

## U

ultralarge files, [3.2.2](physical.md)

unique

constraints, [8.3.1](constra.md)

identifier, [2.2](logical.md), [3.2](physical.md)

update frequencies, [9.1.9](basicmv.md)

UPDATE statement, [23.2.8](sqlmodel.md)

update windows, [9.1.9](basicmv.md)

UPSERT ALL statement, [23.2.8](sqlmodel.md)

UPSERT statement, [23.2.8](sqlmodel.md)

USERNAME$

control column, [17.9.4.2](cdc.md)

---

## V

validating dimensions, [11.5](dimen.md)

view constraints, [8.3.7](constra.md), [19.3.6](qradv.md)

VPD

---

## W

WIDTH\_BUCKET function, [22.7.1](analysis.md), [22.7.1.1](analysis.md)

window functions, [23.3.5](sqlmodel.md)

windowing functions, [22.2.2](analysis.md)

---

## X

XIDSEQ$

control column, [17.9.4.2](cdc.md)

XIDSLT$

control column, [17.9.4.2](cdc.md)

XIDUSN$

control column, [17.9.4.2](cdc.md)