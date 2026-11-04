---
title: Index
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/index.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

A B C D E F G H I J K L M N O P Q R S T U V W Z

---

## A

activating

Active Data Guard

adding

adjusting

initialization parameter file

for logical standby database, [4.2.4.2](create_ls.md)

AFFIRM attribute, [15](log_arch_dest_param.md)

ALTER DATABASE statement

ABORT LOGICAL STANDBY clause, [16.1](sql_stmts.md)

ACTIVATE STANDBY DATABASE clause, [8.3.2](role_management.md), [11.8.6](rman.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md)

ADD STANDBY LOGFILE clause, [16.1](sql_stmts.md), [A.1.1](troubleshooting.md)

ADD STANDBY LOGFILE MEMBER clause, [16.1](sql_stmts.md), [A.1.1](troubleshooting.md), [A.1.1](troubleshooting.md)

ADD SUPPLEMENTAL LOG DATA clause, [16.1](sql_stmts.md)

CLEAR UNARCHIVED LOGFILES clause, [9.5](manage_ps.md)

COMMIT TO SWITCHOVER clause, [8.3.1](role_management.md), [8.3.1](role_management.md), [8.3.1](role_management.md), [16.1](sql_stmts.md)

in Oracle Real Application Clusters, [D.3.1](rac_support.md)

troubleshooting, [A.4.2](troubleshooting.md), [A.4.2](troubleshooting.md), [A.4.3](troubleshooting.md)

CREATE CONTROLFILE clause, [9.5](manage_ps.md)

CREATE DATAFILE AS clause, [A.1.1](troubleshooting.md)

CREATE STANDBY CONTROLFILE clause, [3.2.2](create_ps.md), [A.1.3](troubleshooting.md)

REUSE clause, [16.1](sql_stmts.md)

DROP LOGFILE clause, [A.1.1](troubleshooting.md)

DROP STANDBY LOGFILE MEMBER clause, [16.1](sql_stmts.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md), [A.1.1](troubleshooting.md)

FORCE LOGGING clause, [2.3.2](standby.md), [3.1.1](create_ps.md), [13.4](scenarios.md), [13.4](scenarios.md), [16.1](sql_stmts.md)

GUARD clause, [10.2](manage_ls.md)

MOUNT STANDBY DATABASE clause, [16.1](sql_stmts.md)

OPEN READ ONLY clause, [16.1](sql_stmts.md)

OPEN RESETLOGS clause, [3.2.2](create_ps.md), [9.5](manage_ps.md)

PREPARE TO SWITCHOVER clause, [8.3.1](role_management.md), [8.3.1](role_management.md), [16.1](sql_stmts.md)

RECOVER MANAGED STANDBY DATABASE clause, [3.2.6](create_ps.md), [4.2.5](create_ls.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md)

background process, [7.3.1](log_apply.md)

canceling, [7.3.2](log_apply.md)

controlling Redo Apply, [7.3.1](log_apply.md), [11.8.2](rman.md)

failover, [16.1](sql_stmts.md)

foreground session, [7.3.1](log_apply.md)

overriding the delay interval, [7.2.2](log_apply.md)

starting real time apply, [7.3.1](log_apply.md)

REGISTER LOGFILE clause, [16.1](sql_stmts.md), [A.4.1](troubleshooting.md)

RENAME FILE clause, [A.1.1](troubleshooting.md), [A.1.1](troubleshooting.md)

SET STANDBY DATABASE clause

TO MAXIMIZE AVAILABILITY clause, [16.1](sql_stmts.md)

TO MAXIMIZE PERFORMANCE clause, [8.1.4](role_management.md)

TO MAXIMIZE PROTECTION clause, [16.1](sql_stmts.md)

START LOGICAL STANDBY APPLY clause, [7.4.1](log_apply.md), [12.5](rollup.md), [A.6](troubleshooting.md)

IMMEDIATE keyword, [7.4.1](log_apply.md)

starting SQL Apply, [4.2.5](create_ls.md)

STOP LOGICAL STANDBY APPLY clause, [7.4.2](log_apply.md), [8.3.2](role_management.md), [16.1](sql_stmts.md)

ALTER SESSION DISABLE GUARD statement

overriding the database guard, [10.5.4](manage_ls.md)

ALTER SESSION statement

ENABLE GUARD clause, [16.2](sql_stmts.md)

ALTER SYSTEM statement

SWITCH LOGFILE clause, [3.2.7](create_ps.md)

ALTER TABLESPACE statement, [9.3.4](manage_ps.md), [13.4.2](scenarios.md), [A.10.1.1](troubleshooting.md)

FORCE LOGGING clause, [9.3.6](manage_ps.md)

alternate archive destinations

setting up initialization parameters for, [A.2](troubleshooting.md)

ALTERNATE attribute, [15](log_arch_dest_param.md), [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_DEST\_n initialization parameter, [A.2](troubleshooting.md)

LOG\_ARCHIVE\_DEST\_STATE\_n initialization parameter, [6.2.2](log_transport.md)

ANALYZER process, [10.1](manage_ls.md)

APPLIER process, [10.1](manage_ls.md)

apply lag

monitoring in a real-time query environment, [9.2.1.1](manage_ps.md)

apply lag tolerance

configuring in a real-time query environment, [9.2.1.2](manage_ps.md)

apply services

defined, [1.2.2](concepts.md), [7.1](log_apply.md)

delaying application of redo data, [7.2.2](log_apply.md), [15](log_arch_dest_param.md)

real-time apply

defined, [7.2.1](log_apply.md), [7.2.1](log_apply.md)

monitoring with LOG\_ARCHIVE\_TRACE, [F.2](trace.md)

Redo Apply

defined, [7.1](log_apply.md), [7.3](log_apply.md)

monitoring, [7.3.3](log_apply.md)

starting, [7.3.1](log_apply.md)

stopping, [7.3.2](log_apply.md)

SQL Apply

defined, [1.2.2](concepts.md), [7.1](log_apply.md), [7.1](log_apply.md)

monitoring, [7.4.3](log_apply.md)

starting, [7.4.1](log_apply.md)

stopping, [7.4.2](log_apply.md)

applying

redo data immediately, [7.2.1](log_apply.md)

redo data on standby database, [1.2](concepts.md), [1.2.2](concepts.md), [7](log_apply.md)

SQL statements to logical standby databases, [7.4](log_apply.md)

applying state, [10.4.1](manage_ls.md)

AQ\_TM\_PROCESSES dynamic parameter, [A.4.2](troubleshooting.md)

archive destinations

alternate, [A.2](troubleshooting.md)

archived redo log files

accessing information about, [9.5.1.3](manage_ps.md)

applying

Redo Apply technology, [1.2.2](concepts.md)

SQL Apply technology, [1.2.2](concepts.md)

delaying application, [15](log_arch_dest_param.md)

on the standby database, [7.2.2](log_apply.md)

deleting unneeded, [10.4.2](manage_ls.md)

destinations

disabling, [6.2.2](log_transport.md)

enabling, [6.2.2](log_transport.md)

managing gaps, [1.7](concepts.md)

See also gap management

manually transferring, [2.3.2](standby.md)

redo data transmitted, [1.2.2](concepts.md), [7.1](log_apply.md)

registering

during failover, [8.3.2](role_management.md)

standby databases and, [7.3.3](log_apply.md), [7.4.3](log_apply.md), [9.5.1](manage_ps.md)

troubleshooting switchover problems, [A.4.1](troubleshooting.md)

ARCHIVELOG mode

software requirements, [2.3.2](standby.md)

archiver processes (ARCn)

influenced by MAX\_CONNECTIONS attribute, [15](log_arch_dest_param.md)

archiving

real-time apply, [7.2.1](log_apply.md)

specifying

failure resolution policies for, [15](log_arch_dest_param.md)

standby redo logs, [6.2.3.2](log_transport.md)

to a fast recovery area, [6.2.3.2.2](log_transport.md)

to a local file system, [6.2.3.2.3](log_transport.md)

to failed destinations, [15](log_arch_dest_param.md)

ASM

See Automatic Storage Management (ASM)

ASYNC attribute, [15](log_arch_dest_param.md)

attributes

deprecated for the LOG\_ARCHIVE\_DEST\_n initialization parameter, [15](log_arch_dest_param.md)

AUD$ table

replication on logical standbys, [C.12.2](data_support.md)

automatic block repair, [9.2.1.5](manage_ps.md)

automatic detection of missing log files, [1.2.1](concepts.md), [1.7](concepts.md)

automatic failover, [1.2.3](concepts.md)

Automatic Storage Management (ASM)

creating a standby database that uses, [13.5](scenarios.md)

automatic switchover, [1.2.3](concepts.md)

See also switchovers

---

## B

BACKUP INCREMENTAL FROM SCN command

scenarios using, [11.10](rman.md)

backup operations

after failovers, [8.3.2](role_management.md)

after unrecoverable operations, [13.4.3](scenarios.md), [13.4.3](scenarios.md)

configuring on a physical standby database, [1.1.3](concepts.md)

datafiles, [13.4.2](scenarios.md)

offloading on the standby database, [1.7](concepts.md)

primary databases, [1.1.2](concepts.md)

used by the broker, [1.3](concepts.md)

using RMAN, [11](rman.md)

basic readable standby database See simulating a standby database environment

batch processing

on a logical standby database, [10.1.1.4](manage_ls.md)

benefits

Data Guard, [1.7](concepts.md)

logical standby database, [2.1.2](standby.md)

of a rolling upgrade, [12.1](rollup.md)

physical standby database, [2.1.1](standby.md)

BFILE data types

in logical standby databases, [C.1.2](data_support.md)

block repair, automatic, [9.2.1.5](manage_ps.md)

broker

command-line interface, [1.7](concepts.md)

defined, [1.3](concepts.md)

graphical user interface, [1.7](concepts.md)

BUILDER process, [10.1](manage_ls.md)

---

## C

cascading redo data, [6.3](log_transport.md)

configuration requirements, [6.3](log_transport.md)

data protection considerations, [6.3.2](log_transport.md)

restrictions, [6.3](log_transport.md)

character sets

changing on primary databases, [13.8](scenarios.md)

configurations with differing, [C.15](data_support.md)

checklist

tasks for creating physical standby databases, [3.2](create_ps.md), [3.2](create_ps.md)

tasks for creating standby databases, [4.2](create_ls.md), [4.2](create_ls.md)

checkpoints

V$LOGSTDBY\_PROGRESS view, [10.1.1.3](manage_ls.md)

chunking

transactions, [10.1.1.1](manage_ls.md)

CJQ0 process, [A.4.2](troubleshooting.md)

CLEAR UNARCHIVED LOGFILES clause

of ALTER DATABASE, [9.5](manage_ps.md)

collections data types

in logical standby databases, [C.1.2](data_support.md)

command-line interface

broker, [1.7](concepts.md)

commands, Recovery Manager

DUPLICATE, [E.2.1](rcmbackp.md)

COMMIT TO SWITCHOVER clause

of ALTER DATABASE, [8.3.1](role_management.md), [8.3.1](role_management.md), [16.1](sql_stmts.md)

in Oracle Real Application Clusters, [D.3.1](rac_support.md)

troubleshooting, [A.4.2](troubleshooting.md), [A.4.2](troubleshooting.md), [A.4.3](troubleshooting.md)

COMMIT TO SWITCHOVER TO PRIMARY clause

of ALTER DATABASE, [8.3.1](role_management.md)

communication

between databases in a Data Guard configuration, [1.1](concepts.md)

COMPATIBLE initialization parameter

setting after upgrading Oracle Database software, [B.4](upgrades.md)

setting for a rolling upgrade, [12.2](rollup.md), [12.5](rollup.md), [12.5](rollup.md)

complementary technologies, [1.6](concepts.md)

COMPRESSION attribute, [15](log_arch_dest_param.md)

configuration options

creating with Data Guard broker, [1.3](concepts.md)

overview, [1.1](concepts.md)

physical standby databases

location and directory structure, [2.4](standby.md)

standby databases

delayed standby, [7.2.2](log_apply.md)

configuring

backups on standby databases, [1.1.3](concepts.md)

disaster recovery, [1.1.3](concepts.md)

initialization parameters

for alternate archive destinations, [A.2](troubleshooting.md)

listener for physical standby databases, [3.2.5](create_ps.md)

no data loss, [1.2.3](concepts.md)

physical standby databases, [2.4](standby.md)

reporting operations on a logical standby database, [1.1.3](concepts.md)

standby databases at remote locations, [1.1.3](concepts.md)

constraints

handled on a logical standby database, [10.6.3](manage_ls.md)

Context

unsupported data types, [C.1.2](data_support.md)

Context data types

in logical standby databases, [C.1.2](data_support.md)

control files

copying, [3.2.4](create_ps.md)

creating for standby databases, [3.2.2](create_ps.md)

CONVERT TO SNAPSHOT STANDBY clause on the ALTER DATABASE statement, [16.1](sql_stmts.md)

converting

a logical standby database to a physical standby database

aborting, [4.2.4.1](create_ls.md)

a physical standby database to a logical standby database, [4.2.4.1](create_ls.md)

COORDINATOR process, [10.1](manage_ls.md)

LSP background process, [10.1](manage_ls.md)

copying

control files, [3.2.4](create_ps.md)

CREATE CONTROLFILE clause

of ALTER DATABASE, [9.5](manage_ps.md)

CREATE DATABASE statement

FORCE LOGGING clause, [13.4](scenarios.md)

CREATE DATAFILE AS clause

of ALTER DATABASE, [A.1.1](troubleshooting.md)

CREATE STANDBY CONTROLFILE clause

of ALTER DATABASE, [3.2.2](create_ps.md), [16.1](sql_stmts.md), [A.1.3](troubleshooting.md)

CREATE TABLE AS SELECT (CTAS) statements

applied on a logical standby database, [10.1.1.5](manage_ls.md)

creating

indexes on logical standby databases, [10.5.4.1](manage_ls.md)

---

## D

data availability

balancing against system performance requirements, [1.7](concepts.md)

Data Guard broker

defined, [1.3](concepts.md)

distributed management framework, [8](role_management.md)

failovers, [1.3](concepts.md)

fast-start, [8](role_management.md)

manual, [1.3](concepts.md), [8](role_management.md)

fast-start failover, [1.3](concepts.md)

switchovers, [8](role_management.md)

Data Guard configurations

archiving to standby destinations using the log writer process, [7.2.1](log_apply.md)

defined, [1.1](concepts.md)

protection modes, [1.4](concepts.md)

upgrading Oracle Database software, [B](upgrades.md)

data loss

due to failover, [1.2.3](concepts.md)

switchover and, [8.1](role_management.md)

data protection

balancing against performance, [1.7](concepts.md)

benefits, [1.7](concepts.md)

flexibility, [1.7](concepts.md)

provided by Data Guard, [1](concepts.md)

data protection modes

enforced by redo transport services, [1.2.1](concepts.md)

overview, [1.4](concepts.md), [1.4](concepts.md)

Data Pump utility

using transportable tablespaces with physical standby databases, [9.3.3](manage_ps.md)

data types

BFILE, [C.1.2](data_support.md)

collections in logical standby databases, [C.1.2](data_support.md)

ROWID, [C.1.2](data_support.md)

Spatial, Image, and Context, [C.1.2](data_support.md)

UROWID, [C.1.2](data_support.md)

user-defined, [C.1.2](data_support.md)

database guard, [10.5.4](manage_ls.md)

overriding, [10.5.4](manage_ls.md)

database incarnation

changes with OPEN RESETLOGS, [9.4](manage_ps.md), [9.4](manage_ps.md)

database roles

primary, [1.1.1](concepts.md), [8.1](role_management.md)

standby, [1.1.2](concepts.md), [8.1](role_management.md)

transitions, [1.2.3](concepts.md)

database schema

physical standby databases, [1.1.2](concepts.md)

databases

failover and, [8.1.4](role_management.md)

role transition and, [8.1](role_management.md)

surviving disasters and data corruptions, [1](concepts.md)

upgrading software versions, [12.1](rollup.md)

datafiles

adding to primary database, [9.3.1](manage_ps.md)

monitoring, [9.5](manage_ps.md), [13.4.2](scenarios.md)

renaming on the primary database, [9.3.4](manage_ps.md)

DB\_FILE\_NAME\_CONVERT initialization parameter

setting at standby site after a switchover, [A.4.4](troubleshooting.md)

setting on physical standby database, [3.2.3](create_ps.md)

when planning standby location and directory structure, [2.4](standby.md)

DB\_NAME initialization parameter, [3.1.4](create_ps.md)

DB\_ROLE\_CHANGE system event, [8.1.5](role_management.md)

DB\_UNIQUE\_NAME attribute, [15](log_arch_dest_param.md)

DB\_UNIQUE\_NAME initialization parameter, [A.4.3](troubleshooting.md)

required with LOG\_ARCHIVE\_CONFIG parameter, [14](init_params.md)

setting database initialization parameters, [3.1.4](create_ps.md)

DBA\_DATA\_FILES view, [9.5](manage_ps.md)

DBA\_LOGMNR\_PURGED\_LOG view

list archived redo log files that can be deleted, [10.4.2](manage_ls.md)

DBA\_LOGSTDBY\_EVENTS view, [10.3.1](manage_ls.md), [17](views.md), [A.6](troubleshooting.md)

recording unsupported operations in, [10.5.1](manage_ls.md)

DBA\_LOGSTDBY\_HISTORY view, [17](views.md)

DBA\_LOGSTDBY\_LOG view, [10.3.2](manage_ls.md), [17](views.md)

DBA\_LOGSTDBY\_NOT\_UNIQUE view, [17](views.md)

DBA\_LOGSTDBY\_PARAMETERS view, [17](views.md)

DBA\_LOGSTDBY\_SKIP view, [17](views.md)

DBA\_LOGSTDBY\_SKIP\_TRANSACTION view, [17](views.md)

DBA\_LOGSTDBY\_UNSUPPORTED view, [17](views.md)

DBA\_TABLESPACES view, [9.5](manage_ps.md)

DBMS\_ALERT, [C.9.2](data_support.md)

DBMS\_AQ, [C.9.2](data_support.md)

DBMS\_DESCRIBE, [C.9.1](data_support.md)

DBMS\_JAVA, [C.9.2](data_support.md)

DBMS\_LOB, [C.9.1](data_support.md)

DBMS\_LOGSTDBY package

INSTANTIATE\_TABLE procedure, [10.5.5](manage_ls.md)

SKIP procedure, [A.6](troubleshooting.md)

SKIP\_ERROR procedure, [A.3](troubleshooting.md)

SKIP\_TRANSACTION procedure, [A.6](troubleshooting.md)

DBMS\_LOGSTDBY.BUILD procedure

building a dictionary in the redo data, [4.2.3.2](create_ls.md)

DBMS\_METADATA, [C.9.1](data_support.md)

DBMS\_OBFUSCATION\_TOOLKIT, [C.9.1](data_support.md)

DBMS\_OUTPUT, [C.9.1](data_support.md)

DBMS\_PIPE, [C.9.1](data_support.md)

DBMS\_RANDOM, [C.9.1](data_support.md)

DBMS\_REDEFINITION, [C.9.2](data_support.md)

DBMS\_REFRESH, [C.9.2](data_support.md)

DBMS\_REGISTRY, [C.9.2](data_support.md)

DBMS\_SCHEDULER, [C.9.1](data_support.md)

DBMS\_SPACE\_ADMIN, [C.9.2](data_support.md)

DBMS\_SQL, [C.9.1](data_support.md)

DBMS\_TRACE, [C.9.1](data_support.md)

DBMS\_TRANSACTION, [C.9.1](data_support.md)

DBSNMP process, [A.4.2](troubleshooting.md)

DDL statements

supported by SQL Apply, [C](data_support.md)

DDL Statements

that use DBLINKS, [C.12.1](data_support.md)

DDL transactions

applied on a logical standby database, [10.1.1.5](manage_ls.md)

applying to a logical standby database, [10.1.1.5](manage_ls.md)

DEFER attribute

LOG\_ARCHIVE\_DEST\_STATE\_n initialization parameter, [6.2.2](log_transport.md)

DELAY attribute, [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_DEST\_n initialization parameter, [7.2.2](log_apply.md)

DELAY option

of ALTER DATABASE RECOVER MANAGED STANDBY DATABASE

cancelling, [7.2.2](log_apply.md)

delaying

application of archived redo log files, [15](log_arch_dest_param.md)

application of redo log files, [7.2.2](log_apply.md)

deleting

archived redo log files

indicated by the DBA\_LOGMNR\_PURGED\_LOG view, [10.4.2](manage_ls.md)

not needed by SQL Apply, [10.4.2](manage_ls.md)

deprecated attributes

on the LOG\_ARCHIVE\_DEST\_n initialization parameter, [15](log_arch_dest_param.md)

destinations

displaying with V$ARCHIVE\_DEST view, [17](views.md)

role-based definitions, [15](log_arch_dest_param.md)

detecting

missing archived redo log files, [1.2.1](concepts.md), [1.7](concepts.md)

DG\_CONFIG attribute, [15](log_arch_dest_param.md)

DGMGRL command-line interface

invoking failovers, [1.3](concepts.md), [8](role_management.md)

simplifying switchovers, [1.3](concepts.md), [8](role_management.md)

dictionary

building a LogMiner, [4.2.3.2](create_ls.md)

direct path inserts

SQL Apply DML considerations, [10.1.1.4](manage_ls.md)

directory locations

Optimal Flexible Architecture (OFA), [2.4](standby.md), [2.4](standby.md)

set up with ASM, [2.4](standby.md)

set up with OMF, [2.4](standby.md)

structure on standby databases, [2.4](standby.md)

disabling

a destination for archived redo log files, [6.2.2](log_transport.md)

disaster recovery

benefits, [1.7](concepts.md)

configuring, [1.1.3](concepts.md)

provided by Data Guard, [1](concepts.md)

provided by standby databases, [1.1.3](concepts.md)

disk I/O

controlling with the AFFIRM and NOAFFIRM attributes, [15](log_arch_dest_param.md)

distributed transactions, [C.13](data_support.md)

DML

batch updates on a logical standby database, [10.1.1.4](manage_ls.md)

DML transactions

applying to a logical standby database, [10.1.1.4](manage_ls.md)

downgrading

Oracle Database software, [B.6](upgrades.md)

DROP STANDBY LOGFILE clause

of ALTER DATABASE, [A.1.1](troubleshooting.md)

DROP STANDBY LOGFILE MEMBER clause

of ALTER DATABASE, [16.1](sql_stmts.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md), [A.1.1](troubleshooting.md)

dropping

dynamic parameters

AQ\_TM\_PROCESSES, [A.4.2](troubleshooting.md)

JOB\_QUEUE\_PROCESSES, [A.4.2](troubleshooting.md)

---

## E

ENABLE attribute

LOG\_ARCHIVE\_DEST\_STATE\_n initialization parameter, [6.2.2](log_transport.md)

ENABLE GUARD clause

of ALTER SESSION, [16.2](sql_stmts.md)

enabling

database guard on logical standby databases, [16.2](sql_stmts.md)

destinations for archived redo log files, [6.2.2](log_transport.md)

real-time apply

on logical standby databases, [7.4.1](log_apply.md)

on physical standby databases, [7.3.1](log_apply.md)

extensible indexes

supported by logical standby databases, [C.1.2](data_support.md)

---

## F

failovers, [1.2.3](concepts.md)

Data Guard broker, [1.3](concepts.md), [8](role_management.md)

defined, [1.2.3](concepts.md), [8.1](role_management.md)

displaying history with DBA\_LOGSTDBY\_HISTORY, [17](views.md)

fast-start failover, [8](role_management.md)

flashing back databases after, [8.4](role_management.md)

logical standby databases and, [8.3.2](role_management.md)

manual versus automatic, [1.2.3](concepts.md)

performing backups after, [8.3.2](role_management.md)

physical standby databases and, [16.1](sql_stmts.md)

preparing for, [8.1.4](role_management.md)

simplifying with Data Guard broker, [8](role_management.md)

transferring redo data before, [8.1.4](role_management.md)

viewing characteristics for logical standby databases, [10.3.3](manage_ls.md)

with maximum performance mode, [8.1.4](role_management.md)

with maximum protection mode, [8.1.4](role_management.md)

failure resolution policies

specifying for redo transport services, [15](log_arch_dest_param.md)

fast-start failover

automatic failover, [1.3](concepts.md), [8](role_management.md)

monitoring, [9.5](manage_ps.md)

FGA\_LOG$ table

replication on logical standbys, [C.12.2](data_support.md)

file specifications

renaming on the logical standby database, [10.5.3](manage_ls.md)

Flashback Database

after a role transition, [8.4](role_management.md)

after OPEN RESETLOGS, [13.3](scenarios.md)

after role transitions, [8.4](role_management.md)

characteristics complementary to Data Guard, [1.6](concepts.md)

physical standby database, [13.2.1](scenarios.md)

FORCE LOGGING clause

of ALTER DATABASE, [2.3.2](standby.md), [3.1.1](create_ps.md), [13.4](scenarios.md), [13.4](scenarios.md), [16.1](sql_stmts.md)

of ALTER TABLESPACE, [9.3.6](manage_ps.md)

of CREATE DATABASE, [13.4](scenarios.md)

---

## G

gap management

automatic detection and resolution, [1.2.1](concepts.md), [1.7](concepts.md)

detecting missing log files, [1.7](concepts.md)

registering archived redo log files

during failover, [8.3.2](role_management.md)

GV$INSTANCE view, [D.3.1](rac_support.md)

---

## H

high availability

benefits, [1.7](concepts.md)

provided by Data Guard, [1](concepts.md)

provided by Oracle RAC and Data Guard, [1.6](concepts.md)

---

## I

idle state, [10.4.1](manage_ls.md)

Image data types

in logical standby databases, [C.1.2](data_support.md)

incarnation of a database

changed, [9.4](manage_ps.md), [9.4](manage_ps.md)

initialization parameters

DB\_UNIQUE\_NAME, [3.1.4](create_ps.md), [A.4.3](troubleshooting.md)

LOG\_ARCHIVE\_MIN\_SUCCEED\_DEST, [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_TRACE, [F.2](trace.md)

LOG\_FILE\_NAME\_CONVERT, [E.2.2.4](rcmbackp.md)

modifying for physical standby databases, [3.2.3](create_ps.md)

setting for both the primary and standby roles, [15](log_arch_dest_param.md)

INITIALIZING state, [10.4.1](manage_ls.md)

INSTANTIATE\_TABLE procedure

of DBMS\_LOGSTDBY, [10.5.5](manage_ls.md)

---

## J

JOB\_QUEUE\_PROCESSES dynamic parameter, [A.4.2](troubleshooting.md)

---

## K

KEEP IDENTITY clause, [4.2.4.1](create_ls.md)

---

## L

latency

on logical standby databases, [10.1.1.4](manage_ls.md), [10.1.1.5](manage_ls.md)

listener.ora file

configuring, [3.2.5](create_ps.md)

redo transport services tuning and, [A.7](troubleshooting.md)

troubleshooting, [A.1.2](troubleshooting.md), [A.7](troubleshooting.md)

loading dictionary state, [10.4.1](manage_ls.md)

LOCATION attribute, [15](log_arch_dest_param.md)

setting

LOG\_ARCHIVE\_DEST\_n initialization parameter, [A.2](troubleshooting.md)

log apply services

Redo Apply

monitoring, [9.5.1](manage_ps.md)

starting, [9.1.1](manage_ps.md)

stopping, [9.1.2](manage_ps.md)

tuning for Redo Apply, [9.6](manage_ps.md)

log writer process (LGWR)

ASYNC network transmission, [15](log_arch_dest_param.md)

NET\_TIMEOUT attribute, [15](log_arch_dest_param.md)

SYNC network transmission, [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_CONFIG initialization parameter, [3.1.4](create_ps.md), [3.1.4](create_ps.md), [3.2.3](create_ps.md)

example, [15](log_arch_dest_param.md)

listing unique database names defined with, [17](views.md)

relationship to DB\_UNIQUE\_NAME parameter, [14](init_params.md)

relationship to DG\_CONFIG attribute, [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_DEST\_n initialization parameter

AFFIRM attribute, [15](log_arch_dest_param.md)

ALTERNATE attribute, [15](log_arch_dest_param.md), [15](log_arch_dest_param.md), [A.2](troubleshooting.md)

ASYNC attribute, [15](log_arch_dest_param.md)

COMPRESSION attribute, [15](log_arch_dest_param.md)

DB\_UNIQUE\_NAME attribute, [15](log_arch_dest_param.md)

DELAY attribute, [7.2.2](log_apply.md), [15](log_arch_dest_param.md)

deprecated attributes, [15](log_arch_dest_param.md)

LOCATION attribute, [15](log_arch_dest_param.md), [A.2](troubleshooting.md)

MANDATORY attribute, [15](log_arch_dest_param.md)

MAX\_CONNECTIONS attribute, [15](log_arch_dest_param.md)

MAX\_FAILURE attribute, [15](log_arch_dest_param.md)

NET\_TIMEOUT attribute, [15](log_arch_dest_param.md)

NOAFFIRM attribute, [15](log_arch_dest_param.md)

NOALTERNATE attribute, [A.2](troubleshooting.md)

NODELAY attribute, [7.2.2](log_apply.md)

NOREGISTER attribute, [15](log_arch_dest_param.md)

REOPEN attribute, [15](log_arch_dest_param.md), [15](log_arch_dest_param.md)

SERVICE attribute, [15](log_arch_dest_param.md)

SYNC attribute, [15](log_arch_dest_param.md)

VALID\_FOR attribute, [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_DEST\_STATE\_n initialization parameter

ALTERNATE attribute, [6.2.2](log_transport.md)

DEFER attribute, [6.2.2](log_transport.md)

ENABLE attribute, [6.2.2](log_transport.md)

LOG\_ARCHIVE\_MAX\_PROCESSES initialization parameter

relationship to MAX\_CONNECTIONS, [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_MIN\_SUCCEED\_DEST initialization parameter, [15](log_arch_dest_param.md)

LOG\_ARCHIVE\_TRACE initialization parameter, [F.2](trace.md)

LOG\_FILE\_NAME\_CONVERT initialization parameter

setting at standby site after a switchover, [A.4.4](troubleshooting.md)

setting on physical standby databases, [3.2.3](create_ps.md)

when planning standby location and directory structure, [2.4](standby.md)

logical change records (LCR)

converted by PREPARER process, [10.1](manage_ls.md)

exhausted cache memory, [10.1.1.2](manage_ls.md)

staged, [10.1](manage_ls.md)

logical standby databases, [1.1.2](concepts.md)

adding

datafiles, [A.10.1.1](troubleshooting.md)

indexes, [2.1.2](standby.md), [10.5.4.1](manage_ls.md)

tables, [10.5.5](manage_ls.md)

background processes, [10.1](manage_ls.md)

benefits, [2.1.2](standby.md)

controlling user access to tables, [10.2](manage_ls.md)

creating, [4](create_ls.md)

converting from a physical standby database, [4.2.4.1](create_ls.md)

with Data Guard broker, [1.3](concepts.md)

data types

supported, [C](data_support.md), [C.1.1](data_support.md)

unsupported, [C.1.2](data_support.md)

database guard

overriding, [10.5.4](manage_ls.md)

executing SQL statements on, [1.1.2](concepts.md)

failovers, [8.3.2](role_management.md)

displaying history of, [17](views.md), [17](views.md)

handling failures, [A.3](troubleshooting.md)

viewing characteristics with V$LOGSTDBY\_STATS, [10.3.3](manage_ls.md)

logical standby process (LSP) and, [10.1](manage_ls.md)

materialized views

creating on, [2.1.2](standby.md)

support for, [C.11](data_support.md)

monitoring, [7.4.3](log_apply.md), [17](views.md)

renaming the file specification, [10.5.3](manage_ls.md)

setting up a skip handler, [10.5.3](manage_ls.md)

SQL Apply, [1.2.2](concepts.md)

resynchronizing with primary database branch of redo, [10.6.5](manage_ls.md)

skipping DDL statements, [C.11](data_support.md)

skipping SQL statements, [C.11](data_support.md)

starting real-time apply, [7.4.1](log_apply.md)

stopping, [7.4.2](log_apply.md)

technology, [7.1](log_apply.md)

transaction size considerations, [10.1.1.1](manage_ls.md)

starting

real-time apply, [7.4.1](log_apply.md), [7.4.1](log_apply.md)

states

applying, [10.4.1](manage_ls.md)

idle, [10.4.1](manage_ls.md)

initializing, [10.4.1](manage_ls.md)

loading dictionary, [10.4.1](manage_ls.md)

waiting on gaps, [10.4.1](manage_ls.md)

support for primary databases with Transparent Data Encryption, [C.2](data_support.md)

switchovers, [8.3.1](role_management.md), [8.3.1](role_management.md)

throughput and latency, [10.1.1.4](manage_ls.md), [10.1.1.5](manage_ls.md)

upgrading, [B.3](upgrades.md)

rolling upgrades, [2.3.2](standby.md)

logical standby process (LSP)

COORDINATOR process, [10.1](manage_ls.md)

LogMiner dictionary

using DBMS\_LOGSTDBY.BUILD procedure to build, [4.2.3.2](create_ls.md)

when creating a logical standby database, [4.2.4.1](create_ls.md)

---

## M

managed recovery operations

See Redo Apply

MANDATORY attribute, [15](log_arch_dest_param.md)

materialized views

creating on logical standby databases, [2.1.2](standby.md)

MAX\_CONNECTIONS attribute

configuring Oracle RAC for parallel archival, [15](log_arch_dest_param.md)

reference, [15](log_arch_dest_param.md)

MAX\_FAILURE attribute, [15](log_arch_dest_param.md)

maximum availability mode

introduction, [1.4](concepts.md)

maximum performance mode, [8.1.4](role_management.md)

introduction, [1.4](concepts.md)

maximum performance protection mode, [5.1](protection.md)

maximum protection mode

for Oracle Real Application Clusters, [D.2.2](rac_support.md)

introduction, [1.4](concepts.md)

standby databases and, [8.1.4](role_management.md)

memory

exhausted LCR cache, [10.1.1.2](manage_ls.md)

missing log sequence

See also gap management

detecting, [1.7](concepts.md), [1.7](concepts.md)

modifying

a logical standby database, [10.5.4](manage_ls.md)

initialization parameters for physical standby databases, [3.2.3](create_ps.md)

monitoring

primary database events, [9.5](manage_ps.md)

tablespace status, [9.5](manage_ps.md)

MOUNT STANDBY DATABASE clause

of ALTER DATABASE, [16.1](sql_stmts.md)

multimedia data types

in logical standby databases, [C.1.2](data_support.md)

unsupported by logical standby databases, [C.1.2](data_support.md)

---

## N

NET\_TIMEOUT attribute, [15](log_arch_dest_param.md)

network connections

configuring multiple, [15](log_arch_dest_param.md)

in an Oracle RAC environment, [15](log_arch_dest_param.md)

network I/O operations

network timers

NET\_TIMEOUT attribute, [15](log_arch_dest_param.md)

tuning

redo transport services, [A.7](troubleshooting.md)

network timeouts

acknowledging, [15](log_arch_dest_param.md)

no data loss

data protection modes overview, [1.4](concepts.md)

ensuring, [1.2.3](concepts.md)

guaranteeing, [1.2.3](concepts.md)

provided by maximum availability mode, [1.4](concepts.md)

provided by maximum protection mode, [1.4](concepts.md)

NOAFFIRM attribute, [15](log_arch_dest_param.md)

NOALTERNATE attribute

LOG\_ARCHIVE\_DEST\_n initialization parameter, [A.2](troubleshooting.md)

NODELAY attribute

LOG\_ARCHIVE\_DEST\_n initialization parameter, [7.2.2](log_apply.md)

NOREGISTER attribute, [15](log_arch_dest_param.md)

---

## O

OMF

See Oracle Managed Files (OMF)

on-disk database structures

physical standby databases, [1.1.2](concepts.md)

online redo log files

adding, [9.3.5](manage_ps.md)

dropping, [9.3.5](manage_ps.md)

OPEN READ ONLY clause

of ALTER DATABASE, [16.1](sql_stmts.md)

OPEN RESETLOGS

flashing back after, [13.3](scenarios.md)

OPEN RESETLOGS clause

database incarnation change, [9.4](manage_ps.md), [9.4](manage_ps.md)

of ALTER DATABASE, [3.2.2](create_ps.md), [9.5](manage_ps.md)

recovery, [9.4](manage_ps.md), [9.4](manage_ps.md)

operational requirements, [2.3](standby.md), [2.3.2](standby.md)

Optimal Flexible Architecture (OFA)

directory structure, [2.4](standby.md), [2.4](standby.md)

ORA-01102 message

causing switchover failures, [A.4.3](troubleshooting.md)

Oracle Automatic Storage Management (ASM), [2.4](standby.md)

Oracle Database software

requirements for upgrading with SQL Apply, [12.2](rollup.md)

upgrading, [2.3.2](standby.md), [B.1](upgrades.md)

upgrading with SQL Apply, [12.1](rollup.md)

Oracle Enterprise Manager

invoking failovers, [1.3](concepts.md), [8](role_management.md)

invoking switchovers, [1.3](concepts.md), [8](role_management.md)

Oracle Managed Files (OMF), [2.4](standby.md)

creating a standby database that uses, [13.5](scenarios.md)

Oracle Net

communication between databases in a Data Guard configuration, [1.1](concepts.md)

Oracle Real Application Clusters

characteristics complementary to Data Guard, [1.6](concepts.md)

configuring for multiple network connections, [15](log_arch_dest_param.md)

primary databases and, [1.1.1](concepts.md), [D.1.1](rac_support.md)

setting

maximum data protection, [D.2.2](rac_support.md)

standby databases and, [1.1.2](concepts.md), [D.1](rac_support.md)

Oracle Recovery Manager utility (RMAN)

backing up files on a physical standby database, [11](rman.md)

Oracle Standard Edition

simulating a standby database environment, [2.3.2](standby.md)

---

## P

pageout considerations, [10.1.1.2](manage_ls.md)

pageouts

SQL Apply, [10.1.1.2](manage_ls.md)

parallel DML (PDML) transactions

SQL Apply, [10.1.1.3](manage_ls.md), [10.1.1.4](manage_ls.md)

patch set releases

upgrading, [2.3.2](standby.md)

performance

balancing against data availability, [1.7](concepts.md)

balancing against data protection, [1.7](concepts.md)

physical standby databases

and Oracle Active Data Guard, [2.1.1](standby.md)

applying redo data, [7.1](log_apply.md), [7.3](log_apply.md)

Redo Apply technology, [7.3](log_apply.md)

applying redo log files

starting, [7.3.1](log_apply.md)

benefits, [2.1.1](standby.md)

configuration options, [2.4](standby.md)

converting datafile path names, [3.2.3](create_ps.md)

converting log file path names, [3.2.3](create_ps.md)

converting to a logical standby database, [4.2.4.1](create_ls.md)

creating

checklist of tasks, [3.2](create_ps.md)

configuring a listener, [3.2.5](create_ps.md)

directory structure, [2.4](standby.md)

initialization parameters for, [3.2.3](create_ps.md)

with Data Guard broker, [1.3](concepts.md)

defined, [1.1.2](concepts.md)

failover

checking for updates, [8.1.4](role_management.md)

flashing back after failover, [13.2.1](scenarios.md)

monitoring, [7.3.3](log_apply.md), [9.5.1](manage_ps.md), [17](views.md)

opening for read-only or read/write access, [9.2](manage_ps.md)

read-only, [9.2](manage_ps.md)

recovering through OPEN RESETLOGS, [9.4](manage_ps.md)

Redo Apply, [1.2.2](concepts.md)

resynchronizing with primary database branch of redo, [9.4](manage_ps.md), [9.4](manage_ps.md)

role transition and, [8.2](role_management.md)

rolling forward with BACKUP INCREMENTAL FROM SCN command, [11.10](rman.md)

shutting down, [9.1.2](manage_ps.md)

starting

apply services, [7.3.1](log_apply.md)

real-time apply, [7.3.1](log_apply.md)

synchronizing with the primary database, [11.10](rman.md)

tuning the log apply rate, [9.6](manage_ps.md)

upgrading, [B.2](upgrades.md)

using transportable tablespaces, [9.3.3](manage_ps.md)

PL/SQL supplied packages

supported, [C.9.1](data_support.md)

unsupported, [C.9.2](data_support.md)

PREPARE TO SWITCHOVER clause

of ALTER DATABASE, [8.3.1](role_management.md), [8.3.1](role_management.md), [16.1](sql_stmts.md)

PREPARER process, [10.1](manage_ls.md)

staging LCRs in SGA, [10.1](manage_ls.md)

primary database

backups and, [8.3.2](role_management.md)

configuring

on Oracle Real Application Clusters, [1.1.1](concepts.md)

single-instance, [1.1.1](concepts.md)

datafiles

adding, [9.3.1](manage_ps.md)

defined, [1.1.1](concepts.md)

failover and, [8.1](role_management.md)

gap resolution, [1.7](concepts.md)

initialization parameters

and physical standby database, [3.2.3](create_ps.md)

monitoring events on, [9.5](manage_ps.md)

network connections

avoiding network hangs, [15](log_arch_dest_param.md)

handling network timeouts, [15](log_arch_dest_param.md)

Oracle Real Application Clusters and

setting up, [D.1.1](rac_support.md)

preparing for

physical standby database creation, [3.1](create_ps.md)

prerequisite conditions for

logical standby database creation, [4.1](create_ls.md)

redo transport services on, [1.2.1](concepts.md)

reducing workload on, [1.7](concepts.md)

switchover, [8.1.3](role_management.md)

tablespaces

adding, [9.3.1](manage_ps.md)

primary databases

ARCHIVELOG mode, [2.3.2](standby.md)

software requirements, [2.3.2](standby.md)

primary key columns

logged with supplemental logging, [4.2.3.2](create_ls.md), [10.1.1.4](manage_ls.md)

primary role, [1.1.1](concepts.md)

processes

CJQ0, [A.4.2](troubleshooting.md)

DBSNMP, [A.4.2](troubleshooting.md)

preventing switchover, [A.4.2](troubleshooting.md)

QMN0, [A.4.2](troubleshooting.md)

SQL Apply architecture, [10.1](manage_ls.md), [10.4.1](manage_ls.md)

protection modes

maximum availability mode, [1.4](concepts.md)

maximum performance, [5.1](protection.md)

maximum performance mode, [1.4](concepts.md)

maximum protection mode, [1.4](concepts.md)

monitoring, [9.5](manage_ps.md)

setting on a primary database, [5.2](protection.md)

---

## Q

QMN0 process, [A.4.2](troubleshooting.md)

queries

offloading on the standby database, [1.7](concepts.md)

---

## R

READER process, [10.1](manage_ls.md)

read-only operations, [1.2.2](concepts.md)

physical standby databases and, [9.2](manage_ps.md)

real-time apply

defined, [7.2.1](log_apply.md)

overview of log apply services, [1.2](concepts.md)

starting, [7.3.1](log_apply.md)

on logical standby, [7.4.1](log_apply.md)

starting on logical standby databases, [7.4.1](log_apply.md)

starting on physical standby databases, [7.3.1](log_apply.md)

stopping

on logical standby, [7.4.2](log_apply.md)

on physical standby databases, [9.1.2](manage_ps.md)

tracing data with LOG\_ARCHIVE\_TRACE initialization parameter, [F.2](trace.md)

real-time query feature, [9.2](manage_ps.md)

and Oracle Active Data Guard, [9.2](manage_ps.md), [9.2.1](manage_ps.md)

configuring apply lag tolerance, [9.2.1.2](manage_ps.md)

forcing Redo Apply synchronization, [9.2.1.3](manage_ps.md)

monitoring apply lag, [9.2.1.1](manage_ps.md)

restrictions, [9.2.1.4](manage_ps.md)

using, [9.2.1](manage_ps.md)

RECORD\_UNSUPPORTED\_OPERATIONS

example, [10.5.1](manage_ls.md)

RECOVER MANAGED STANDBY DATABASE CANCEL clause

aborting, [4.2.4.1](create_ls.md)

RECOVER MANAGED STANDBY DATABASE clause

canceling the DELAY control option, [7.2.2](log_apply.md)

of ALTER DATABASE, [3.2.6](create_ps.md), [4.2.5](create_ls.md), [7.3.1](log_apply.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md), [16.1](sql_stmts.md)

background process, [7.3.1](log_apply.md)

controlling Redo Apply, [7.3.1](log_apply.md), [11.8.2](rman.md)

foreground session, [7.3.1](log_apply.md)

overriding the delay interval, [7.2.2](log_apply.md)

starting real time apply, [7.3.1](log_apply.md)

RECOVER TO LOGICAL STANDBY clause

converting a physical standby database to a logical standby database, [4.2.4.1](create_ls.md)

recovering

from errors, [A.10.1](troubleshooting.md)

logical standby databases, [10.6.5](manage_ls.md)

physical standby databases

after an OPEN RESETLOGS, [9.4](manage_ps.md), [9.4](manage_ps.md)

through resetlogs, [9.4](manage_ps.md), [10.6.5](manage_ls.md)

Recovery Manager

characteristics complementary to Data Guard, [1.6](concepts.md)

commands

DUPLICATE, [E.2.1](rcmbackp.md)

standby database

creating, [E.2.1](rcmbackp.md)

LOG\_FILE\_NAME\_CONVERT initialization parameter, [E.2.2.4](rcmbackp.md)

preparing using RMAN, [E.2.2](rcmbackp.md)

re-creating

a table on a logical standby database, [10.5.5](manage_ls.md)

Redo Apply

defined, [1.2.2](concepts.md), [7.1](log_apply.md)

flashing back after failover, [13.2.1](scenarios.md)

starting, [3.2.6](create_ps.md), [7.3.1](log_apply.md)

stopping, [9.1.2](manage_ps.md)

technology, [1.2.2](concepts.md)

tuning the log apply rate, [9.6](manage_ps.md)

redo data

applying

through Redo Apply technology, [1.2.2](concepts.md)

through SQL Apply technology, [1.2.2](concepts.md)

to standby database, [7.1](log_apply.md)

to standby databases, [1.1.2](concepts.md)

applying during conversion of a physical standby database to a logical standby database, [4.2.4.1](create_ls.md)

archiving on the standby system, [1.2.2](concepts.md), [7.1](log_apply.md)

building a dictionary in, [4.2.3.2](create_ls.md)

cascading, [6.3](log_transport.md)

manually transferring, [2.3.2](standby.md)

transmitting, [1.1.2](concepts.md), [1.2.1](concepts.md)

redo gaps, [6.4.3](log_transport.md)

manual resolution, [6.4.3.1](log_transport.md)

reducing resolution time, [6.4.3](log_transport.md)

redo log files

delaying application, [7.2.2](log_apply.md)

redo logs

automatic application on physical standby databases, [7.3.1](log_apply.md)

update standby database tables, [1.7](concepts.md)

redo transport services, [6](log_transport.md)

archive destinations

alternate, [A.2](troubleshooting.md)

re-archiving to failed destinations, [15](log_arch_dest_param.md)

authenticating sessions

using a password file, [6.2.1.2](log_transport.md)

using SSL, [6.2.1.1](log_transport.md)

configuring, [6.2](log_transport.md)

configuring security, [6.2.1](log_transport.md)

defined, [1.2.1](concepts.md)

gap detection, [6.4.3](log_transport.md)

handling archive failures, [15](log_arch_dest_param.md)

monitoring status, [6.4.1](log_transport.md)

network

tuning, [A.7](troubleshooting.md)

protection modes

maximum availability mode, [1.4](concepts.md)

maximum performance mode, [1.4](concepts.md)

maximum protection mode, [1.4](concepts.md)

receiving redo data, [6.2.3](log_transport.md)

sending redo data, [6.2.2](log_transport.md)

synchronous and asynchronous disk I/O, [15](log_arch_dest_param.md)

wait events, [6.4.4](log_transport.md)

REGISTER LOGFILE clause

of ALTER DATABASE, [16.1](sql_stmts.md), [A.4.1](troubleshooting.md)

REGISTER LOGICAL LOGFILE clause

of ALTER DATABASE, [8.3.2](role_management.md)

registering

archived redo log files

during failover, [8.3.2](role_management.md)

RELY constraint

creating, [4.1.2](create_ls.md)

remote file server process (RFS)

log writer process and, [7.2.1](log_apply.md)

RENAME FILE clause

of ALTER DATABASE, [A.1.1](troubleshooting.md), [A.1.1](troubleshooting.md)

renaming

datafiles

on the primary database, [9.3.4](manage_ps.md)

setting the STANDBY\_FILE\_MANAGEMENT parameter, [9.3.4](manage_ps.md)

REOPEN attribute, [15](log_arch_dest_param.md), [15](log_arch_dest_param.md)

reporting operations

configuring, [1.1.3](concepts.md)

offloading on the standby database, [1.7](concepts.md)

performing on a logical standby database, [1.1.2](concepts.md)

requirements

of a rolling upgrade, [12.2](rollup.md)

restart considerations

SQL Apply, [10.1.1.3](manage_ls.md)

resynchronizing

logical standby databases with a new branch of redo, [10.6.5](manage_ls.md)

physical standby databases with a new branch of redo, [9.4](manage_ps.md), [9.4](manage_ps.md)

retrieving

missing archived redo log files, [1.2.1](concepts.md), [1.7](concepts.md)

RMAN

incremental backups, [11.10](rman.md)

rolling forward physical standby databases, [11.10](rman.md)

RMAN BACKUP INCREMENTAL FROM SCN command, [11.10](rman.md)

RMAN backups

accessibility in Data Guard environment, [11.1.3](rman.md)

association in Data Guard environment, [11.1.2](rman.md)

interchangeability in Data Guard environment, [11.1.1](rman.md)

role management services

defined, [8](role_management.md)

role transition triggers, [8.1.5](role_management.md)

DB\_ROLE\_CHANGE system event, [8.1.5](role_management.md)

role transitions, [1.2.3](concepts.md), [8.1](role_management.md)

choosing a type of, [8.1.1](role_management.md)

defined, [1.2.3](concepts.md)

flashing back the databases after, [8.4](role_management.md)

logical standby database and, [8.3](role_management.md)

monitoring, [9.5](manage_ps.md)

physical standby databases and, [8.2](role_management.md)

reversals, [1.2.3](concepts.md), [8.1](role_management.md)

role-based destinations

setting, [15](log_arch_dest_param.md)

rollback

after switchover failures, [A.4.5](troubleshooting.md)

rolling upgrade

software requirements, [2.3.2](standby.md)

rolling upgrades

benefits, [12.1](rollup.md)

patch set releases, [2.3.2](standby.md)

requirements, [12.2](rollup.md)

setting the COMPATIBLE initialization parameter, [12.2](rollup.md), [12.5](rollup.md), [12.5](rollup.md)

unsupported data types and storage attributes, [12.4](rollup.md)

use of KEEP IDENTITY clause, [4.2.4.1](create_ls.md)

ROWID data types

in logical standby databases, [C.1.2](data_support.md)

---

## S

scenarios

recovering

after NOLOGGING is specified, [13.4](scenarios.md)

schemas

identical to primary database, [1.1.2](concepts.md)

SCN

using for incremental backups, [11.10](rman.md)

sequences

unsupported on logical standby databases, [C.10](data_support.md)

SERVICE attribute, [15](log_arch_dest_param.md)

SET STANDBY DATABASE clause

of ALTER DATA, [16.1](sql_stmts.md)

of ALTER DATABASE, [8.1.4](role_management.md), [16.1](sql_stmts.md)

shutting down

physical standby database, [9.1.2](manage_ps.md)

simulating

standby database environment, [2.3.2](standby.md)

skip handler

setting up on a logical standby database, [10.5.3](manage_ls.md)

SKIP procedure

of DBMS\_LOGSTDBY, [A.6](troubleshooting.md)

SKIP\_ERROR procedure

of the DBMS\_LOGSTDBY package, [A.3](troubleshooting.md)

SKIP\_TRANSACTION procedure

of DBMS\_LOGSTDBY, [A.6](troubleshooting.md)

snapshot standby databases, [1.1.2](concepts.md)

managing, [9.7](manage_ps.md)

software requirements, [2.3.2](standby.md)

rolling upgrades, [2.3.2](standby.md), [2.3.2](standby.md)

Spatial data types

in logical standby databases, [C.1.2](data_support.md)

SQL Apply, [7.4.2](log_apply.md), [10.1.1.2](manage_ls.md)

after an OPEN RESETLOGS, [10.6.5](manage_ls.md)

ANALYZER process, [10.1](manage_ls.md)

APPLIER process, [10.1](manage_ls.md)

applying CREATE TABLE AS SELECT (CTAS) statements, [10.1.1.5](manage_ls.md)

applying DDL transactions, [10.1.1.5](manage_ls.md), [10.1.1.5](manage_ls.md)

applying DML transactions, [10.1.1.4](manage_ls.md)

architecture, [10.1](manage_ls.md), [10.4.1](manage_ls.md)

BUILDER process, [10.1](manage_ls.md)

COORDINATOR process, [10.1](manage_ls.md)

defined, [1.2.2](concepts.md), [7.1](log_apply.md)

deleting archived redo log files, [10.4.2](manage_ls.md)

parallel DML (PDML) transactions, [10.1.1.3](manage_ls.md), [10.1.1.4](manage_ls.md)

performing a rolling upgrade, [12.1](rollup.md)

PREPARER process, [10.1](manage_ls.md)

READER process, [10.1](manage_ls.md)

requirements for rolling upgrades, [12.2](rollup.md)

restart considerations, [10.1.1.3](manage_ls.md)

rolling upgrades, [2.3.2](standby.md)

starting

real-time apply, [7.4.1](log_apply.md)

stopping

real-time apply, [7.4.2](log_apply.md)

support for DDL statements, [C](data_support.md)

support for PL/SQL supplied packages, [C.9.1](data_support.md)

supported data types, [C.1.1](data_support.md)

transaction size considerations, [10.1.1.1](manage_ls.md)

unsupported data types, [C.1.2](data_support.md)

unsupported PL/SQL supplied packages, [C.9.2](data_support.md)

viewing current activity, [10.1](manage_ls.md)

of processes, [10.1](manage_ls.md)

what to do if it stops, [A.6](troubleshooting.md)

SQL sessions

causing switchover failures, [A.4.2](troubleshooting.md)

SQL statements

executing on logical standby databases, [1.1.2](concepts.md), [1.2.2](concepts.md)

skipping on logical standby databases, [C.11](data_support.md)

standby database

creating logical, [4](create_ls.md)

standby databases

about creating using RMAN, [E.2.1](rcmbackp.md)

apply services on, [7.1](log_apply.md)

applying redo data on, [7](log_apply.md)

applying redo log files on, [1.2.2](concepts.md), [1.7](concepts.md)

ARCn processes using multiple network connections, [15](log_arch_dest_param.md)

configuring, [1.1](concepts.md)

maximum number of, [2](standby.md)

on Oracle Real Application Clusters, [1.1.2](concepts.md), [D.1](rac_support.md)

on remote locations, [1.1.3](concepts.md)

single-instance, [1.1.2](concepts.md)

creating, [1.1.2](concepts.md), [3](create_ps.md)

checklist of tasks, [4.2](create_ls.md)

directory structure considerations, [2.4](standby.md)

if primary uses ASM or OMF, [13.5](scenarios.md)

on remote host with same directory structure, [E.3](rcmbackp.md)

with a time lag, [7.2.2](log_apply.md)

defined, [2.1](standby.md)

failover

preparing for, [8.1.4](role_management.md)

failover to, [8.1.4](role_management.md)

LOG\_FILE\_NAME\_CONVERT initialization parameter, [E.2.2.4](rcmbackp.md)

operational requirements, [2.3](standby.md), [2.3.2](standby.md)

preparing to use RMAN, [E.2.2](rcmbackp.md)

recovering through OPEN RESETLOGS, [9.4](manage_ps.md)

resynchronizing with the primary database, [1.7](concepts.md)

rolling forward with RMAN incremental backups, [11.10](rman.md)

SET AUXNAME command, [E.2.2.4](rcmbackp.md)

SET NEWNAME command, [E.2.2.4](rcmbackp.md)

software requirements, [2.3.2](standby.md)

starting apply services on physical, [7.3.1](log_apply.md)

See also physical standby databases

standby redo log files

and real-time apply, [7.2.1](log_apply.md)

standby redo logs

archiving to a fast recovery area, [6.2.3.2.2](log_transport.md)

archiving to a local file system, [6.2.3.2.3](log_transport.md)

configuring archival of, [6.2.3.2](log_transport.md)

creating and managing, [6.2.3.1](log_transport.md)

standby role, [1.1.2](concepts.md)

STANDBY\_FILE\_MANAGEMENT initialization parameter

when renaming datafiles, [9.3.4](manage_ps.md)

START LOGICAL STANDBY APPLY clause

IMMEDIATE keyword, [7.4.1](log_apply.md)

of ALTER DATABASE, [4.2.5](create_ls.md), [7.4.1](log_apply.md), [12.5](rollup.md), [A.6](troubleshooting.md)

starting

logical standby databases, [4.2.5](create_ls.md)

physical standby databases, [3.2.6](create_ps.md)

real-time apply, [7.4.1](log_apply.md), [7.4.1](log_apply.md)

on logical standby databases, [7.4.1](log_apply.md), [7.4.1](log_apply.md)

on physical standby databases, [7.3.1](log_apply.md), [7.3.1](log_apply.md)

Redo Apply, [3.2.6](create_ps.md), [7.3.1](log_apply.md), [9.1.1](manage_ps.md)

SQL Apply, [4.2.5](create_ls.md), [7.4.1](log_apply.md)

STOP LOGICAL STANDBY APPLY clause

of ALTER DATABASE, [7.4.2](log_apply.md), [8.3.2](role_management.md), [16.1](sql_stmts.md)

stopping

real-time apply

on logical standby databases, [7.4.2](log_apply.md)

real-time apply on physical standby databases, [7.3.2](log_apply.md)

Redo Apply, [7.3.2](log_apply.md)

SQL Apply, [7.4.2](log_apply.md)

storage attributes

unsupported during a rolling upgrade, [12.4](rollup.md)

streams capture

running on a logical standby, [10.6.6](manage_ls.md)

supplemental logging

setting up to log primary key and unique-index columns, [4.2.3.2](create_ls.md), [10.1.1.4](manage_ls.md)

supported data types

for logical standby databases, [C](data_support.md), [C.12](data_support.md)

supported PL/SQL supplied packages, [C.9.1](data_support.md)

SWITCH LOGFILE clause

of ALTER SYSTEM, [3.2.7](create_ps.md)

SWITCHOVER\_STATUS column

of V$DATABASE view, [A.4.1](troubleshooting.md)

switchovers, [1.2.3](concepts.md)

choosing a target standby database, [8.1.2](role_management.md)

defined, [1.2.3](concepts.md), [8.1](role_management.md)

displaying history with DBA\_LOGSTDBY\_HISTORY, [17](views.md)

fails with ORA-01102, [A.4.3](troubleshooting.md)

flashing back databases after, [8.4](role_management.md)

logical standby databases and, [8.3.1](role_management.md)

manual versus automatic, [1.2.3](concepts.md)

monitoring, [9.5](manage_ps.md)

no data loss and, [8.1](role_management.md)

preparing for, [8.1.3](role_management.md)

prevented by

active SQL sessions, [A.4.2](troubleshooting.md)

CJQ0 process, [A.4.2](troubleshooting.md)

DBSNMP process, [A.4.2](troubleshooting.md)

processes, [A.4.2](troubleshooting.md)

QMN0 process, [A.4.2](troubleshooting.md)

seeing if the last archived redo log file was transmitted, [A.4.1](troubleshooting.md)

setting DB\_FILE\_NAME\_CONVERT after, [A.4.4](troubleshooting.md)

setting LOG\_FILE\_NAME\_CONVERT after, [A.4.4](troubleshooting.md)

simplifying with Data Guard broker, [1.3](concepts.md), [8](role_management.md)

starting over, [A.4.5](troubleshooting.md)

typical use for, [8.1.3](role_management.md)

SYNC attribute, [15](log_arch_dest_param.md)

system events

role transitions, [8.1.5](role_management.md)

system global area (SGA)

logical change records staged in, [10.1](manage_ls.md)

system resources

efficient utilization of, [1.7](concepts.md)

---

## T

tables

logical standby databases

adding on, [10.5.5](manage_ls.md)

re-creating tables on, [10.5.5](manage_ls.md)

unsupported on, [C.10](data_support.md)

tablespaces

adding

a new datafile, [A.10.1.1](troubleshooting.md)

to primary database, [9.3.1](manage_ps.md)

monitoring status changes, [9.5](manage_ps.md)

moving between databases, [9.3.3](manage_ps.md)

target standby database

for switchover, [8.1.2](role_management.md)

terminating

network connection, [15](log_arch_dest_param.md)

text indexes

supported by logical standby databases, [C.1.2](data_support.md)

throughput

on logical standby databases, [10.1.1.4](manage_ls.md), [10.1.1.5](manage_ls.md)

time lag

delaying application of archived redo log files, [7.2.2](log_apply.md), [15](log_arch_dest_param.md)

in standby database, [7.2.2](log_apply.md)

TIME\_COMPUTED column, [8.1.2](role_management.md)

TIME\_COMPUTED column of the V$DATAGUARD\_STATS view, [8.1.2](role_management.md)

tnsnames.ora file

redo transport services tuning and, [A.7](troubleshooting.md)

troubleshooting, [A.1.2](troubleshooting.md), [A.4.4](troubleshooting.md), [A.7](troubleshooting.md)

trace files

levels of tracing data, [F.2](trace.md)

setting, [F.1](trace.md)

tracking real-time apply, [F.2](trace.md)

transaction size considerations

SQL Apply, [10.1.1.1](manage_ls.md)

Transparent Data Encryption

support by SQL Apply, [C.2](data_support.md)

transportable tablespaces

using with a physical standby database, [9.3.3](manage_ps.md)

triggers

handled on a logical standby database, [10.6.3](manage_ls.md)

role transitions, [8.1.5](role_management.md)

troubleshooting

if SQL Apply stops, [A.6](troubleshooting.md)

last redo data was not transmitted, [A.4.1](troubleshooting.md)

listener.ora file, [A.1.2](troubleshooting.md), [A.7](troubleshooting.md)

logical standby database failures, [A.3](troubleshooting.md)

processes that prevent switchover, [A.4.2](troubleshooting.md)

SQL Apply, [A.6](troubleshooting.md)

switchovers, [A.4](troubleshooting.md)

active SQL sessions, [A.4.2](troubleshooting.md)

ORA-01102 message, [A.4.3](troubleshooting.md)

roll back and start over, [A.4.5](troubleshooting.md)

tnsnames.ora file, [A.1.2](troubleshooting.md), [A.4.4](troubleshooting.md), [A.7](troubleshooting.md)

tuning

log apply rate for Redo Apply, [9.6](manage_ps.md)

---

## U

unique-index columns

logged with supplemental logging, [4.2.3.2](create_ls.md), [10.1.1.4](manage_ls.md)

unrecoverable operations, [13.4.2](scenarios.md)

backing up after, [13.4.3](scenarios.md)

unsupported data types

during a rolling upgrade, [12.4](rollup.md)

unsupported operations

capturing in DBA\_LOGSTDBY\_EVENTS view, [10.5.1](manage_ls.md)

unsupported PL/SQL supplied packages, [C.9.2](data_support.md)

upgrading

Oracle Database software, [2.3.2](standby.md), [12.1](rollup.md), [B](upgrades.md), [B.1](upgrades.md)

setting the COMPATIBLE initialization parameter, [B.4](upgrades.md)

UROWID data types

in logical standby databases, [C.1.2](data_support.md)

user-defined data types

in logical standby databases, [C.1.2](data_support.md)

USING CURRENT LOGFILE clause

starting real time apply, [7.3.1](log_apply.md)

---

## V

V$ARCHIVE\_DEST view, [17](views.md), [A.1.2](troubleshooting.md)

displaying information for all destinations, [17](views.md)

V$ARCHIVE\_DEST\_STATUS view, [17](views.md)

V$ARCHIVE\_GAP view, [17](views.md)

V$ARCHIVED\_LOG view, [9.5.1.3](manage_ps.md), [17](views.md), [A.4.1](troubleshooting.md)

V$DATABASE view, [17](views.md)

monitoring fast-start failover, [9.5](manage_ps.md)

SWITCHOVER\_STATUS column and, [A.4.1](troubleshooting.md)

V$DATABASE\_INCARNATION view, [17](views.md)

V$DATAFILE view, [13.4.2](scenarios.md), [13.4.3](scenarios.md), [17](views.md)

V$DATAGUARD\_CONFIG view, [17](views.md)

listing database names defined with LOG\_ARCHIVE\_CONFIG, [17](views.md)

V$DATAGUARD\_STATS view, [8.1.2](role_management.md), [17](views.md)

V$DATAGUARD\_STATUS view, [9.5.1.5](manage_ps.md), [17](views.md)

V$FS\_FAILOVER\_STATS view, [17](views.md)

V$LOG view, [17](views.md)

V$LOG\_HISTORY view, [9.5.1.4](manage_ps.md), [17](views.md)

V$LOGFILE view, [17](views.md)

V$LOGSTDBY\_PROCESS view, [10.1](manage_ls.md), [10.3.4](manage_ls.md), [10.3.4](manage_ls.md), [10.4.1](manage_ls.md), [10.7.3.1](manage_ls.md), [10.7.3.2](manage_ls.md), [17](views.md)

V$LOGSTDBY\_PROGRESS view, [10.3.5](manage_ls.md), [17](views.md)

RESTART\_SCN column, [10.1.1.3](manage_ls.md)

V$LOGSTDBY\_STATE view, [8.1.2](role_management.md), [10.3.6](manage_ls.md), [10.4.1](manage_ls.md), [17](views.md)

V$LOGSTDBY\_STATS view, [10.1](manage_ls.md), [10.3.7](manage_ls.md), [17](views.md)

failover characteristics, [10.3.3](manage_ls.md)

V$LOGSTDBY\_TRANSACTION view, [17](views.md)

V$MANAGED\_STANDBY view, [9.5.1.2](manage_ps.md), [9.5.1.2](manage_ps.md), [17](views.md)

V$REDO\_DEST\_RESP\_HISTOGRAM

using to monitor synchronous redo transport response time, [6.4.2](log_transport.md)

V$REDO\_DEST\_RESP\_HISTOGRAM view, [17](views.md)

V$SESSION view, [A.4.2](troubleshooting.md)

V$STANDBY\_EVENT\_HISTOGRAM view, [17](views.md)

V$STANDBY\_LOG view, [17](views.md)

V$THREAD view, [9.5](manage_ps.md)

VALID\_FOR attribute, [15](log_arch_dest_param.md)

verifying

logical standby databases, [4.2.6](create_ls.md)

physical standby databases, [3.2.7](create_ps.md)

versions

upgrading Oracle Database software, [12.1](rollup.md)

views

DBA\_LOGSTDBY\_EVENTS, [10.3.1](manage_ls.md), [17](views.md), [A.6](troubleshooting.md)

DBA\_LOGSTDBY\_HISTORY, [17](views.md)

DBA\_LOGSTDBY\_LOG, [10.3.2](manage_ls.md), [17](views.md)

DBA\_LOGSTDBY\_NOT\_UNIQUE, [17](views.md)

DBA\_LOGSTDBY\_PARAMETERS, [17](views.md)

DBA\_LOGSTDBY\_SKIP, [17](views.md)

DBA\_LOGSTDBY\_SKIP\_TRANSACTION, [17](views.md)

DBA\_LOGSTDBY\_UNSUPPORTED, [17](views.md)

GV$INSTANCE, [D.3.1](rac_support.md)

V$ARCHIVE\_DEST, [17](views.md), [A.1.2](troubleshooting.md)

V$ARCHIVE\_DEST\_STATUS, [17](views.md)

V$ARCHIVED\_GAP, [17](views.md)

V$ARCHIVED\_LOG, [9.5.1.3](manage_ps.md), [17](views.md)

V$DATABASE, [17](views.md)

V$DATABASE\_INCARNATION, [17](views.md)

V$DATAFILE, [13.4.2](scenarios.md), [13.4.3](scenarios.md), [17](views.md)

V$DATAGUARD\_CONFIG, [17](views.md)

V$DATAGUARD\_STATS, [17](views.md)

V$DATAGUARD\_STATUS, [9.5.1.5](manage_ps.md), [17](views.md)

V$FS\_FAILOVER\_STATS, [17](views.md)

V$LOG, [17](views.md)

V$LOG\_HISTORY, [9.5.1.4](manage_ps.md), [17](views.md)

V$LOGFILE, [17](views.md)

V$LOGSTDBY\_PROCESS, [10.1](manage_ls.md), [10.3.4](manage_ls.md), [17](views.md)

V$LOGSTDBY\_PROGRESS, [10.3.5](manage_ls.md), [17](views.md)

V$LOGSTDBY\_STATE, [10.3.6](manage_ls.md), [17](views.md)

V$LOGSTDBY\_STATS, [10.1](manage_ls.md), [10.3.7](manage_ls.md), [17](views.md)

V$LOGSTDBY\_TRANSACTION, [17](views.md)

V$MANAGED\_STANDBY, [9.5.1.2](manage_ps.md), [9.5.1.2](manage_ps.md), [17](views.md)

V$REDO\_DEST\_RESP\_HISTOGRAM, [17](views.md)

V$SESSION, [A.4.2](troubleshooting.md)

V$STANDBY\_EVENT\_HISTOGRAM, [17](views.md)

V$STANDBY\_LOG, [17](views.md)

V$THREAD, [9.5](manage_ps.md)

---

## W

wait events

WAITING FOR DICTIONARY LOGS state, [10.4.1](manage_ls.md)

waiting on gap state, [10.4.1](manage_ls.md)

---

## Z

zero downtime instantiation

logical standby databases, [4.2](create_ls.md)