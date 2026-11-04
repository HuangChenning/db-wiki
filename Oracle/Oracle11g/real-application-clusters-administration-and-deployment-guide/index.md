---
title: Index
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/index.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

A B C D E F G H I J K L M N O P Q R S T U V W X

---

## Symbols

$ORACLE\_HOME/root.sh script, [8.3](clonerac.md)

---

## A

abnormal instance termination, [3.2.1](admin.md)

ACMS

Active Session History, Oracle RAC, [13.8.1](monitor.md)

Active Session History, Top Cluster Events, [13.8.2](monitor.md)

Active Session History, Top Remote Instance, [13.8.3](monitor.md)

active sessions, [13.8.1](monitor.md)

ACTIVE\_INSTANCE\_COUNT initialization parameter, [3.6](admin.md)

adding nodes to an existing cluster, [9.1](cloneracwithoui.md)

adding Oracle RAC to nodes on Linux and UNIX, [10.1](adddelunix.md)

adding Oracle RAC to nodes on Windows, [11.1](adddelwin.md)

ADDM

global monitoring, [13.7](monitor.md)

*See* Automatic Database Diagnostic Monitor

ADDM for Oracle Real Application Clusters mode, [13.7](monitor.md)

administering

services, [5.9.1](hafeats.md)

services with SRVCTL, [5.9.3](hafeats.md)

administering instances

with Server Management, [3.1](admin.md)

administering Oracle Enterprise Manager jobs, [3.11.3.1](admin.md)

administering services

Oracle Enterprise Manager, [5.9](hafeats.md)

SRVCTL, [5.9](hafeats.md)

administrative tools

overview and concepts, [1.6.2](admcon.md)

SYSASM privilege, [3.2.3](admin.md)

administrator-managed database instances

adding, [11.1.1](adddelwin.md)

administrator-managed databases, [3.1.1](admin.md), [5.3.2.6](hafeats.md)

AVAILABLE instances for services, [5.3.2.6](hafeats.md)

converting to policy-managed, [3.7](admin.md)

defined, [1.6.1](admcon.md)

PREFERRED instances for services, [5.3.2.6](hafeats.md)

ADRCI

ADR Command-Line Interpreter, [B.2](appsupport.md)

Advanced Queuing

and FAN, [5.5.1](hafeats.md)

Advisor Central in Oracle Enterprise Manager, [13.7](monitor.md)

aggregates

by instances, [13.1.1.3](monitor.md)

by services, [13.1.1.3](monitor.md)

by waits, [13.1.1.3](monitor.md)

alert administration

Oracle Enterprise Manager, [3.11.3.2](admin.md)

alert blackouts

Oracle Enterprise Manager, [3.11.3.3](admin.md)

alert logs, [B.3](appsupport.md)

managing, [B.1](appsupport.md)

ALTER SYSTEM ARCHIVE LOG CURRENT statement, [3.1.3.2](admin.md)

ALTER SYSTEM ARCHIVE LOG statement, [3.1.3.2](admin.md)

INSTANCE option, [3.1.3.2](admin.md)

ALTER SYSTEM CHECKPOINT LOCAL statement, [3.1.3.2](admin.md)

ALTER SYSTEM CHECKPOINT statement

global versus local, [3.1.3.2](admin.md)

specifying an instance, [3.1.3.2](admin.md)

ALTER SYSTEM KILL SESSION statement

terminating a session on a specific instance, [3.4](admin.md)

ALTER SYSTEM QUIESCE RESTRICTED statement

quiescing a noncluster database, [3.8](admin.md)

ALTER SYSTEM statement

CHECKPOINT clause, [3.1.3.2](admin.md)

ALTER SYSTEM SWITCH LOGFILE statement, [3.1.3.2](admin.md), [3.1.3.2](admin.md)

applications

consolidating multiple in a single database, [12.1.3](design.md)

highly available, [12.1](design.md)

scalability, [12.1.4](design.md)

spanning XA transactions across Oracle RAC instances, [5.8.1](hafeats.md)

using pre-created database sessions, [5.7.5](hafeats.md)

ARCHIVE LOG command

SQL\*Plus, [3.1.3.2](admin.md)

ARCHIVE\_LAG\_TARGET initialization parameter, [3.6.3](admin.md)

archived redo log files

applying in parallel, [7.5.1](backup.md)

file format and destination, [6.8](rman.md)

log sequence number, [6.8](rman.md)

archiver process

monitor, [6.10](rman.md)

archiving mode

changing, [6.2](rman.md)

ASH reports, [13.8.1](monitor.md)

asm

SRVCTL object name, [A](srvctladmin.md)

ASM\_PREFERRED\_READ\_FAILURE\_GROUPS initialization parameter, [2.6.4](storage.md), [3.6](admin.md)

Atomic Controlfile to Memory Service (ACMS), [1.3.4](admcon.md)

Automatic Database Diagnostic Monitor, [13.9.2](monitor.md), [13.9.3.2](monitor.md), [13.9.5](monitor.md)

Automatic Database Diagnostic Monitor (ADDM), [1.6.3](admcon.md)

analyzing AWR data, [13.7](monitor.md)

DBMS\_ADDM PL/SQL package, [13.7](monitor.md)

DBMS\_ADVISOR PL/SQL package, [13.7](monitor.md)

Global ADDM mode, [13.7](monitor.md)

Local ADDM mode, [13.7](monitor.md)

Automatic Database Diagnostic Monitoring (ADDM), [13.7](monitor.md)

Automatic Diagnostic Repository (ADR), [B.2](appsupport.md)

ADRCI command-line interpreter, [B.2](appsupport.md)

automatic load balancing

configuring RMAN channels for multiple instances, [6.6](rman.md)

AUTOMATIC management policy, [3.2.4](admin.md)

Automatic Performance Diagnostics (AWR)

monitor performance statistics, [13.7](monitor.md)

automatic segment space management (ASSM), [12.3.1](design.md)

tablespace use in Oracle RAC, [12.3.1](design.md)

automatic undo management

tablespace use in Oracle RAC, [12.3.1](design.md)

automatic workload management

concepts, [1.4](admcon.md), [5.3.1](hafeats.md)

description, [5.1](hafeats.md)

manual rebalancing, [5.2](hafeats.md)

Automatic Workload Repository, [5.1](hafeats.md), [5.2](hafeats.md), [5.2](hafeats.md), [5.10](hafeats.md), [13.9.3.2](monitor.md)

Automatic Workload Repository (AWR), [13.7](monitor.md), [13.9](monitor.md)

monitoring performance, [5.3.3.3](hafeats.md)

snapshots, [13.7](monitor.md)

AVAILABLE instances

for services, [5.3.2.6](hafeats.md)

Average Active Sessions chart

performance monitoring, [13.1.1.3](monitor.md)

AWR

*See* Automatic Workload Repository

---

## B

background processes

Oracle RAC, [1.3.4](admcon.md)

SMON, [3.2.1](admin.md), [7.3.1](backup.md)

background thread trace files, [B.1](appsupport.md)

backups

server parameter file, [3.5.3](admin.md)

bandwidth

interconnect, [13.2](monitor.md)

best practices

deploying Oracle RAC for high availability, [12.1.2](design.md)

blackouts

defining, [3.11.3.3](admin.md)

block mode conversions

statistics for, [13.6](monitor.md)

blocks

associated with instance, [7.3.1](backup.md)

buffer cache, [1.3.3](admcon.md)

instance recovery, [7.3.1](backup.md)

buffer sizes

interprocess communication (IPC)

adjusting for Oracle RAC, [13.3](monitor.md)

---

## C

cache coherency, [13.9.3.1](monitor.md)

Cache Fusion, [1.3.3](admcon.md), [12.3.5](design.md)

and e-commerce applications, [12.3.5](design.md)

overview, [1.6.4](admcon.md)

Cache Fusion performance, [13.2](monitor.md)

cache fusion transfers, [13.9.4](monitor.md)

callouts

how they are run, [5.5.3](hafeats.md)

capacity

increasing, [12.1.4](design.md)

cardinality, [3.1.1](admin.md)

catclustdb.sql script, [1.6.3](admcon.md)

CATCLUST.SQL script

using to create views for Oracle RAC, [13.5](monitor.md)

changing the configuration of all services, [4.3.1](onenode.md)

channels

configure one RMAN channel for each Oracle RAC instance, [6.6.2](rman.md)

configuring during crosscheck or restore operations, [6.5](rman.md)

configuring for RMAN, [6.6](rman.md)

chart

Global Cache Block Access Latency, [13.1.1.3](monitor.md)

charts

Average Active Sessions, [13.1.1.3](monitor.md)

Cluster Host Load Average, [13.1.1.3](monitor.md)

Database Throughput, [13.1.1.3](monitor.md)

checking the interconnect, [B.6](appsupport.md)

CLB\_GOAL\_SHORT, [5.5.1](hafeats.md)

client

application environments and FAN, [5.7](hafeats.md)

client connections with SCAN, [3.1.1](admin.md)

clients

integrated for FAN events, [5.5.1](hafeats.md)

JDBC Thin Driver, [5.7.2](hafeats.md)

JDBC/OCI, [5.7.2.2](hafeats.md)

client-side

load balancing, [5.4](hafeats.md)

client-side load balancing, [5.4.1](hafeats.md)

clone.pl, [8.4](clonerac.md)

clone.pl script

cloning parameters, [8.3](clonerac.md)

environment variables, [8.3](clonerac.md)

cloning, [1.5.3](admcon.md), [8](clonerac.md), [8.2](clonerac.md)

deployment phase, [8.3](clonerac.md)

log files, [8.4](clonerac.md)

parameters passed to the clone.pl script, [8.3](clonerac.md)

preparation phase, [8.2](clonerac.md)

running $ORACLE\_HOME/root.sh script, [8.3](clonerac.md)

setting ORACLE\_BASE, [8.3](clonerac.md)

setting ORACLE\_HOME, [8.3](clonerac.md)

setting ORACLE\_HOME\_NAME, [8.3](clonerac.md)

cloning log files, [8.4](clonerac.md)

cluster

definition of, [1.1](admcon.md)

cluster cache coherency, [13.1.1.2](monitor.md)

Cluster Database Performance page

Top Activity drill down menu, [13.1.1.3](monitor.md)

cluster file system

archiving parameter settings, [6.9.1.2](rman.md)

archiving scenario, [6.9.1](rman.md)

restore, [7.2.1](backup.md)

storage in Oracle RAC, [2.1](storage.md)

Cluster Host Load Average page

cluster database performance, [13.1.1.3](monitor.md)

cluster nodes name

in clone.pl script, [8.3](clonerac.md)

Cluster Verification Utility

overview and concepts, [1.6.2](admcon.md)

CLUSTER\_DATABASE initialization parameter, [3.6](admin.md), [3.6.1](admin.md)

CLUSTER\_DATABASE\_INSTANCE initialization parameter, [3.6.1](admin.md)

CLUSTER\_DATABASE\_INSTANCES initialization parameter, [3.6](admin.md)

CLUSTER\_INTERCONNECTS

parameter, [13.3](monitor.md)

CLUSTER\_INTERCONNECTS initialization parameter, [3.9.1](admin.md)

CLUSTER\_INTERCONNECTS parameter

examples, [3.9.2](admin.md), [3.9.2](admin.md)

CLUSTER\_NODE\_NAME parameter

FAN, and matching database signature, [5.5.5](hafeats.md)

CLUSTER\_NODES parameter

in clone.pl script, [8.3](clonerac.md)

clustered Oracle ASM

converting a noncluster Oracle ASM, [2.6.5](storage.md)

clusters

consolidating multiple databases in, [12.1.3](design.md)

clusterware management solution, [1.2](admcon.md)

CMAN session pools

and FAN, [5.7.1](hafeats.md)

cold backups, [3.8](admin.md)

command-line interpreter

ADR Command-Line Interpreter (ADRCI), [B.2](appsupport.md)

committed data

instance failure, [7.3.1](backup.md)

communication protocols

verifying settings for, [13.2](monitor.md)

compatibility

Oracle RAC and Oracle Database software, [1.5.1](admcon.md)

COMPATIBLE initialization parameter, [3.6.1](admin.md)

configuring channels

during restore or crosscheck operations, [6.5](rman.md)

configuring preferred mirror read disks in extended clusters, [2.6.4](storage.md)

CONNECT command, [3.1.3.2](admin.md)

SQL\*Plus, [3.1.3.2](admin.md)

CONNECT SYS

example of, [3.2.3](admin.md)

connecting

to instances, [1.6.2](admcon.md), [3.1.3](admin.md)

connection load balancing

concepts, [1.4](admcon.md)

introduction to, [5.1](hafeats.md)

long method, [5.4.3](hafeats.md)

short method, [5.4.3](hafeats.md)

connection pools

and FAN, [5.7.1](hafeats.md)

consistent blocks, [1.3.3](admcon.md)

CONTROL\_FILES initialization parameter, [3.6.1](admin.md)

converting a database from Oracle RAC One Node to Oracle RAC, [4.3.2](onenode.md)

converting an Oracle RAC database with one instance to Oracle RAC One Node, [4.3.1](onenode.md)

corrupted data blocks, [B.2](appsupport.md)

CREATE PFILE

FROM MEMORY clause, [3.5](admin.md)

CREATE PFILE statement, [3.5.3](admin.md)

CREATE SPFILE

FROM MEMORY clause, [3.5](admin.md)

creating

server parameter files, [3.5](admin.md)

services, [5.9.1](hafeats.md)

SPFILE backups, [3.5.3](admin.md)

crosscheck operations

configuring channels during, [6.5](rman.md)

crosschecking on multiple nodes

RMAN backups, [6.5](rman.md)

CRS Administrator, [3.1.1](admin.md)

CRS resources

management of, [1.2](admcon.md)

current blocks, [1.3.3](admcon.md)

CVU

*See* Cluster Verification Utility

---

## D

data dictionary

querying views, [13.5](monitor.md)

Data Recovery Advisor, [B.2](appsupport.md)

data security

wallet, [12.3.8.1](design.md)

data warehouse

deploying applications for in Oracle RAC, [12.3.7](design.md)

data warehouse systems, [12.3.7](design.md)

database

creation, [1.5.2](admcon.md)

services

singleton, [3.7](admin.md)

uniform, [3.7](admin.md)

SRVCTL object name, [A](srvctladmin.md)

Database Configuration Assistant (DBCA), [1.5.2](admcon.md)

adding and deleting instances in interactive mode

on Windows, [11.1.1.1](adddelwin.md)

adding and deleting instances in silent mode

on Windows, [11.1.1.2](adddelwin.md)

adding instances in interactive mode

on Linux and UNIX, [10.1.2.1](adddelunix.md)

adding instances in silent mode

on Linux and UNIX, [10.1.2.2](adddelunix.md)

cloning Oracle RAC instances, [8.3](clonerac.md)

creating views for Oracle Real Application Clusters, [13.5](monitor.md)

Database Storage page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

deleting instances in interactive mode

on Linux and UNIX, [10.2.1.1](adddelunix.md)

on Windows, [11.2.1.1](adddelwin.md)

deleting instances in silent mode

on Linux and UNIX, [10.2.1.2](adddelunix.md)

on Windows, [11.2.1.2](adddelwin.md)

Instance Management page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

List of Cluster Databases page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

Operations page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

running the catclustdb.sql script, [1.6.3](admcon.md)

Welcome page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

database instances

administrator managed

deleting, [10.2.1](adddelunix.md), [11.2.1](adddelwin.md)

database resource, [3.1.1](admin.md)

Database Resource Manager, [3.8](admin.md)

database role, [3.2.4](admin.md)

database signatures

matching the FAN parameters, [5.5.5](hafeats.md)

database state, [3.2](admin.md)

Database Storage page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

Database Throughput page

performance monitoring, [13.1.1.3](monitor.md)

DATABASE\_UNIQUE\_NAME parameter

FAN, and matching database signature, [5.5.5](hafeats.md)

databases

adding

Oracle RAC One Node, [4.2](onenode.md)

administrator managed, [3.1.1](admin.md), [5.3.2.6](hafeats.md)

consolidating multiple in a cluster, [12.1.3](design.md)

controlling restarts, [3.10](admin.md)

Oracle RAC One Node

services on, [4.2](onenode.md)

policy managed, [3.1.1](admin.md), [5.3.2.7](hafeats.md)

scalability, [12.1.4](design.md)

databases sessions

pre-created, [5.7.5](hafeats.md)

Datagram Protocol (UDP), [1.3.2](admcon.md)

DB\_BLOCK\_SIZE initialization parameter, [3.6.1](admin.md)

DB\_DOMAIN initialization parameter, [3.6.1](admin.md)

DB\_FILES initialization parameter, [3.6.1](admin.md)

DB\_NAME initialization parameter, [3.6](admin.md), [3.6.1](admin.md)

DB\_RECOVERY\_FILE\_DEST initialization parameter, [3.6.1](admin.md), [7.6](backup.md)

DB\_RECOVERY\_FILE\_DEST\_SIZE initialization parameter, [3.6.1](admin.md)

DB\_UNIQUE\_NAME initialization parameter, [3.6.1](admin.md)

DBCA

*See* Database Configuration Assistant (DBCA)

DDL statements, [12.3.2](design.md)

default database service, [1.5.2](admcon.md), [3.6](admin.md), [5.9.1](hafeats.md)

degree of parallelism (DOP), [12.3.7.1](design.md)

deleting administrator-managed database instances, [10.2.1](adddelunix.md), [11.2.1](adddelwin.md)

dependencies

and services, [5.3.3.1](hafeats.md)

deploying

Oracle Real Application Clusters environments, [1.6.1](admcon.md), [12](design.md)

design

Oracle Real Application Clusters environments, [1.6.1](admcon.md), [12](design.md)

diagnosing problems for Oracle RAC, [B](appsupport.md)

diagnosing problems using ADR, [B.2](appsupport.md)

DIAGNOSTIC\_DEST initialization parameter, [B.1](appsupport.md), [B.3](appsupport.md)

diskgroup

SRVCTL object name, [A](srvctladmin.md)

DISPATCHERS initialization parameter, [3.6](admin.md)

specifying a service with, [5.9.1](hafeats.md)

displaying IP addresses

with ifconfig, [3.9.2](admin.md)

with netstat, [3.9.2](admin.md)

distributed SQL transactions, [5.8.1](hafeats.md)

Distributed Transaction Processing (DTP), [12.3.4](design.md)

distributed transactions, [12.3.4](design.md)

directing to a single instance in the cluster, [5.8.2](hafeats.md)

services in Oracle RAC, [5.8.1](hafeats.md)

XA transactions span instances, [5.8.1](hafeats.md)

DML\_LOCKS initialization parameter, [3.6.1](admin.md)

DTP Service., [5.8.2](hafeats.md)

DTP/XA transactions, [5.8.1](hafeats.md)

dynamic performance views, [13.9](monitor.md)

creating, [13.5](monitor.md)

GV$, [1.6.3](admcon.md)

V$, [1.6.3](admcon.md)

dynamic resource allocation

overview, [1.6.4](admcon.md)

---

## E

e-commerce

applications in Oracle RAC, [12.3.5](design.md)

edition

services attribute, [5.3.2.3](hafeats.md)

ENCRYPTION\_WALLET\_LOCATION parameter, [12.3.8.1](design.md)

Enterprise Manager

overview, [1.2](admcon.md)

environment variables

passed to the clone.pl script, [8.3](clonerac.md)

setting with SRVCTL, [3.1.4](admin.md)

evaluating block transfers, [13.6](monitor.md)

event notification

enabling, [5.7.5](hafeats.md)

examples

setting the CLUSTER\_INTERCONNECTS parameter, [3.9.2](admin.md)

extended distance cluster, [2.6.4](storage.md)

Oracle ASM preferred mirror read, [2.6.4](storage.md)

extended distance clusters

configuring preferred mirror read disks, [2.6.4](storage.md)

external transaction managers

OraMTS, [5.8.1](hafeats.md)

---

## F

failure

instance, [7.3](backup.md)

multiple node, [7.3.2](backup.md)

node, [7.3.1](backup.md)

failure groups, [2.6.4](storage.md)

FAN events

enabling for JDBC, [5.7.2.2](hafeats.md)

Fast Application Notification (FAN), [5.5](hafeats.md)

and high availability events, [5.5.5](hafeats.md)

callouts definition, [5.5.6](hafeats.md)

callouts, how to use, [5.5.6](hafeats.md)

events, enabling for JDBC clients, [5.7.2](hafeats.md)

events, enabling for ODP.NET, [5.7.6](hafeats.md)

events, enabling for Oracle Call Interface, [5.7.4](hafeats.md)

events, enabling ODP.NET clients, [5.7.7](hafeats.md)

how events are published, [5.5.1](hafeats.md)

introduction, [5.1](hafeats.md)

overview, [5.5.1](hafeats.md)

parameters and matching database signatures, [5.5.5](hafeats.md)

uses, [5.5.1](hafeats.md)

Fast Connection Failover (FCF)

enabling JDBC clients, [5.7.2](hafeats.md)

enabling with thin and thick clients, [5.7.2.2](hafeats.md)

introduction to, [5.1](hafeats.md)

fault diagnosability, [B.2](appsupport.md)

FCF

*See* Fast Connection Failover (FCF)

features, new, [Preface](whatsnew.md)

files

archived redo log files, [6.8](rman.md)

redo log, [6.8](rman.md)

filesystem

SRVCTL object name, [A](srvctladmin.md)

FROM MEMORY clause

on CREATE PFILE or CREATE SPFILE, [3.5](admin.md)

---

## G

GC\_SERVER\_PROCESSES initialization parameter

specifying the number of LMSn processes, [12.1.3](design.md)

GCS protocol, [13.9.3.1](monitor.md)

GCS\_SERVER\_PROCESSES initialization parameter, [3.6](admin.md)

Generic server pool, [3.1.1](admin.md)

GES

*See* global cache and enqueue service (GES)

global cache and enqueue service (GES), [13.9.1](monitor.md)

Global Cache Block Access Latency chart

performance monitoring, [13.1.1.3](monitor.md)

Global Cache Service (GCS), [1.3.3](admcon.md), [3.6](admin.md)

Global Cache Service Process (LMS), [1.3.4](admcon.md)

Global Cache Service Processes (LMSn)

reducing the number of, [12.1.3](design.md)

specifying the number of, [12.1.3](design.md)

Global Cache Service statistics, [13.9.1](monitor.md), [13.9.3.1](monitor.md)

GLOBAL clause

forcing a checkpoint, [3.1.3.2](admin.md)

Global Enqueue Service Daemon (LMD), [1.3.4](admcon.md)

Global Enqueue Service (GES), [1.3.3](admcon.md)

Global Enqueue Service Monitor (LMON), [1.3.4](admcon.md)

Global Enqueue Service statistics, [13.9.1](monitor.md)

global performance data

with ADDM, [13.7](monitor.md)

Global Resource Directory (GRD), [1.3.3](admcon.md)

Global Transaction Process (GTX0-j), [1.3.4](admcon.md)

GLOBAL\_TXN\_PROCESSES initialization parameter, [5.8.1](hafeats.md)

goals

and the load balancing advisory, [5.6.1](hafeats.md)

for load balancing advisory, [5.6.2](hafeats.md)

Grid Naming Service (GNS)

SRVCTL object name, [A](srvctladmin.md)

GTX0-j

Global Transaction Process, [1.3.4](admcon.md)

GV$, [1.6.3](admcon.md)

GV$ view, [13.4](monitor.md)

GV$SESSION, [3.4](admin.md), [3.4](admin.md)

---

## H

hash partitioning

with Oracle RAC, [12.2](design.md)

high availability

best practices, [12.1.2](design.md)

for Oracle RAC Databases, [12.1](design.md)

high availability framework

concepts, [1.4](admcon.md)

introduction to, [5.1](hafeats.md)

home

SRVCTL object name, [A](srvctladmin.md)

HOST command, [3.1.3.2](admin.md)

SQL\*Plus, [3.1.3.2](admin.md)

---

## I

idle wait class, [13.8.1](monitor.md)

Implicit Connection Cache, [5.7.2](hafeats.md)

indexes

sequence-based, [12.2](design.md)

initdb\_name.ora file

DIAGNOSTIC\_DEST initialization parameter, [B.1](appsupport.md)

initialization parameters

cluster database issues regarding, [3.6](admin.md)

CLUSTER\_INTERCONNECTS, [3.9.1](admin.md), [13.3](monitor.md)

recommendations for using, [3.9.1](admin.md)

identical settings for on all instances, [3.6.3](admin.md)

RECOVERY\_PARALLELISM, [7.5.2.1](backup.md)

settings for instances, [3.5](admin.md)

specific to Oracle RAC, [3.6](admin.md)

that must be identical on all instances, [3.6.1](admin.md)

that must be unique on all instances, [3.6.2](admin.md)

INST\_ID column, [13.4](monitor.md)

installation

introduction, [1.5](admcon.md)

Oracle RAC, [1.5.2](admcon.md)

installations

performing multiple simultaneous cluster, [8](clonerac.md)

instance

SRVCTL object name, [A](srvctladmin.md)

instance discovery

Oracle Enterprise Manager Grid Control, [3.11.1](admin.md)

Instance Enqueue Process (LCK0), [1.3.4](admcon.md)

Instance Management page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

INSTANCE NAME initialization parameter, [3.6](admin.md)

INSTANCE option, [3.1.3.2](admin.md)

INSTANCE parameter

FAN, and matching database signature, [5.5.5](hafeats.md)

instance recovery, [3.2.1](admin.md)

INSTANCE\_NAME initialization parameter, [3.6.2](admin.md)

INSTANCE\_NUMBER initialization parameter, [3.6.2](admin.md)

INSTANCE\_TYPE initialization parameter, [3.6.1](admin.md)

instances

aggregated for service performance, [13.1.1.3](monitor.md)

cloning Oracle RAC, [8.3](clonerac.md)

effect of SQL\*Plus commands on, [3.1.3.2](admin.md)

failure, [7.3.2](backup.md)

initialization parameter settings, [3.5](admin.md)

maximum number for Oracle RAC, [1.1](admcon.md)

memory structures, [1.3.3](admcon.md)

parallel processes, [5.3.3.4](hafeats.md)

private interconnect usage, [B.6](appsupport.md)

recovery, [3.2.1](admin.md), [7.3.1](backup.md)

recovery, abnormal shutdown, [3.2.1](admin.md)

recovery, multiple failures, [7.3.2](backup.md)

Server Management, [3.1](admin.md)

shutting down, [3.2.1](admin.md)

starting and stopping, [3.2](admin.md)

terminating session on, [3.4](admin.md)

verifying, [3.3](admin.md), [3.3](admin.md)

verifying running, [3.3](admin.md)

instances failure

recovery from, [7.3](backup.md)

instead of Statspack, [1.6.3](admcon.md)

interconnect

and performance, [13.3](monitor.md)

and the Oracle RAC architecture, [1.1](admcon.md)

protocols for Oracle Real Application Clusters, [13.2](monitor.md)

verifying settings for, [13.2](monitor.md)

interconnect bandwidth, [13.2](monitor.md)

latency, [13.2](monitor.md)

interconnect block transfer rates, [13.6](monitor.md)

interconnect settings

verifying, [13.2](monitor.md)

interconnects

alternatives to the private network, [3.9](admin.md)

private, [B.6](appsupport.md)

Interconnects page

monitoring clusterware with Oracle Enterprise Manager, [13.1.1](monitor.md)

monitoring Oracle Clusterware, [13.1.1.2](monitor.md)

interprocess communication (IPC)

buffer sizes

adjusting, [13.3](monitor.md)

IPC protocol, [13.2](monitor.md), [13.9.3.1](monitor.md)

---

## J

Java Database Connectivity (JDBC) clients

Oracle Notification Service usage, [5.1](hafeats.md)

Java-based tools and utilities

CVU, [B.4](appsupport.md)

DBCA, [B.4](appsupport.md)

DBUA, [B.4](appsupport.md)

enabling tools for tracing, [B.4](appsupport.md)

GSD, [B.4](appsupport.md)

NETCA, [B.4](appsupport.md)

SRVCTL, [B.4](appsupport.md)

JDBC

and FAN, [5.7.1](hafeats.md)

enabling FAN events for, [5.7.2.2](hafeats.md)

JDBC clients

enabling for Fast Connection Failover (FCF), [5.7.2](hafeats.md)

JDBC Thin Driver, [5.7.2](hafeats.md)

JDBC/OCI, [5.7.2.2](hafeats.md)

job administration

Oracle Enterprise Manager, [3.11.3.1](admin.md)

---

## K

KILL SESSION clause

on the ALTER SYSTEM statement, [3.4](admin.md)

---

## L

LCK0

Instance Enqueue Process, [1.3.4](admcon.md)

level thresholds

services, [5.11](hafeats.md)

LICENSE\_MAX\_USERS initialization parameter, [3.6.3](admin.md)

List of Cluster Databases page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

listener

SRVCTL object name, [A](srvctladmin.md)

listeners

command to add to a node, [A](srvctladmin.md)

command to remove, [A](srvctladmin.md)

Oracle Net, [1.2](admcon.md)

LMD

Global Enqueue Service Daemon, [1.3.4](admcon.md)

LMON Global Enqueue Service Monitor, [1.3.4](admcon.md)

LMS

Global Cache Service Process, [1.3.4](admcon.md)

LMS processes

reducing the number of, [12.1.3](design.md)

LMSn processes

reducing the number of, [12.1.3](design.md)

load balancing, [12.3.5](design.md)

by services, [1.3.2](admcon.md)

OCI runtime connection, [5.7.5](hafeats.md)

server-side, [5.4](hafeats.md)

load balancing advisory

and FAN events, [5.6.3](hafeats.md)

concepts, [1.4](admcon.md)

configuring your environment for using, [5.6.2](hafeats.md)

deployment, [5.6.1](hafeats.md)

description of, [5.6](hafeats.md)

events and FAN, [5.5.1](hafeats.md)

introduction to, [5.1](hafeats.md)

Load Balancing Advisory, [5.3.2.8](hafeats.md)

local archiving scenario

RMAN, [6.9.2](rman.md)

Local Area Network (LAN), [1.3.2](admcon.md)

LOCAL clause

forcing a checkpoint, [3.1.3.2](admin.md)

local file system

archiving parameter settings, [6.9.2.2](rman.md)

restore, [7.2.2](backup.md)

local instance

shutting down, [3.2.3](admin.md)

starting, [3.2.3](admin.md)

local node name

in clone.pl script, [8.3](clonerac.md)

LOCAL\_NODE parameter

in clone.pl script, [8.3](clonerac.md)

locally managed tablespaces, [12.3.1](design.md)

log files

tracing, [B.4](appsupport.md)

log sequence numbers, [6.8](rman.md)

LOG\_ARCHIVE\_FORMAT initialization parameter, [3.6.3](admin.md)

LOG\_ARCHIVE\_FORMAT parameter, [6.8](rman.md)

---

## M

mass deployment

cloning, [1.5.3](admcon.md), [8](clonerac.md), [8.2](clonerac.md)

media failures

recovery from, [7.4](backup.md)

memory structures

in Oracle RAC, [1.3.3](admcon.md)

message request counters, [13.6](monitor.md)

migration

application, [12.1.4](design.md)

missing files, [B.2](appsupport.md)

mission critical systems

considerations for Oracle RAC, [12.1.1](design.md)

modified data

instance recovery, [7.3.1](backup.md)

monitoring

archiver process, [6.10](rman.md)

overview and concepts, [1.6.3](admcon.md)

performance of global cache block access, [13.1.1.3](monitor.md)

monitoring host load average, [13.1.1.3](monitor.md)

mount all non-running instances of an Oracle RAC database, [3.2.4](admin.md)

multiple cluster interconnects, [3.9](admin.md)

multiple databases in a cluster, [3.9.1](admin.md)

multiple instances

starting from a single SQL\*Plus session, [3.2.3](admin.md)

starting from one node, [3.2.3](admin.md)

multiple node failures, [7.3.2](backup.md)

multiple public networks, [1.3.2](admcon.md)

multiplexed redo log files, [2.4](storage.md)

---

## N

net service name, [3.1.3](admin.md)

network

SRVCTL object name, [A](srvctladmin.md)

Network Attached Storage (NAS), [1.3.2](admcon.md)

network resources, [1.3.2](admcon.md)

NIC bonding, [3.9](admin.md)

node

failure and VIP addresses, [1.3.2](admcon.md)

node affinity awareness, [7.3.4](backup.md)

node discovery

Oracle Enterprise Manager Grid Control, [3.11.1](admin.md)

node evictions, [13.1.1.1](monitor.md)

nodeapps

SRVCTL object name, [A](srvctladmin.md)

nodes

affinity awareness, [7.3.4](backup.md)

failure of, [7.3.1](backup.md)

virtual IP addresses, [A](srvctladmin.md), [A](srvctladmin.md)

noncluster databases

quiescing, [3.8](admin.md)

noncluster Oracle ASM

converting to clustered Oracle ASM, [2.6.5](storage.md)

---

## O

object creation and deletion, [12.3.2](design.md)

objects

creation of and effect on performance, [12.3.2](design.md)

srvctl object names and abbreviations, [A](srvctladmin.md)

OC4J

SRVCTL object name, [A](srvctladmin.md)

OCFS2, [1.3.1](admcon.md)

OCI session pooling, [5.7.5](hafeats.md)

OCI session pools

optimizing, [5.7.5](hafeats.md)

runtime connection load balancing, [5.7.5](hafeats.md)

service metrics, [5.7.5](hafeats.md)

OCI Session Pools

and FAN, [5.7.1](hafeats.md)

OCI\_EVENTS mode

setup for runtime connection load balancing, [5.7.5](hafeats.md)

OCI\_THREADED mode

setup for runtime connection load balancing, [5.7.5](hafeats.md)

OCRDUMP utility, [13.3](monitor.md)

ODP.NET

and FAN, [5.7.1](hafeats.md)

and Fast Connection Failover, [5.7.6](hafeats.md)

load balancing advisory events, [5.7.7](hafeats.md)

OLTP environments, [12.2](design.md)

online database relocation

relocation utility, [4.4](onenode.md)

online recovery, [7.3.1](backup.md)

online transaction processing (OLTP)

applications in Oracle RAC, [12.3.5](design.md)

ons

SRVCTL object name, [A](srvctladmin.md)

ONS

*See* Oracle Notification Service

Operations page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

optimal execution plans, [12.3.7.1](design.md)

Oracle ASM

*See* Oracle Automatic Storage Management (Oracle ASM)

Oracle Automatic Storage Management (Oracle ASM)

archiving scenario, [6.9.1](rman.md)

converting noncluster Oracle ASM to clustered Oracle ASM, [2.6.5](storage.md)

installation, [1.5.2](admcon.md)

instances

administering with SRVCTL, [2.6.6](storage.md)

Oracle ASM preferred read failure groups, [2.6.4](storage.md)

preferred mirror read disks, [2.6.4](storage.md)

preferred read disks, [3.6](admin.md)

SRVCTL object name, [A](srvctladmin.md)

storage solution, [2.1](storage.md)

SYSASM privilege, [3.2.3](admin.md)

Oracle Call Interface environment

to receive service metrics, [5.7.5](hafeats.md)

Oracle Call Interface (OCI)

runtime connection load balancing, [5.7.5](hafeats.md)

Oracle Cluster File System (OCFS for Windows), [1.3.1](admcon.md)

Oracle Cluster Registry (OCR), [3.1.4](admin.md), [13.3](monitor.md)

Oracle Clusterware

cloning, [1.5.3](admcon.md)

control policies

AUTOMATIC, [3.10](admin.md)

MANUAL, [3.10](admin.md)

using SRVCTL to display and change, [3.10](admin.md)

controlling database restarts, [3.10](admin.md)

described, [1.2](admcon.md), [1.2](admcon.md)

introduction, [1.2](admcon.md)

introduction and concepts of, [1](admcon.md)

managing Oracle processes, [1.2](admcon.md)

Oracle Database

session activity, [13.8.1](monitor.md)

Oracle Dynamic Volume Manager

described, [Preface](whatsnew.md)

Oracle Enterprise Manager

adding database instances to nodes

on Linux and UNIX, [10.1.2](adddelunix.md)

on Windows, [11.1.1](adddelwin.md)

alert administration, [3.11.3.2](admin.md)

alert blackouts, [3.11.3.3](admin.md)

Automatic Database Diagnostic Monitoring (ADDM), [13.7](monitor.md)

Average Active Sessions chart, [13.1.1.3](monitor.md)

Cluster Database Home page, [13.1.1.1](monitor.md)

Cluster Database page, [13.1.1](monitor.md)

Cluster Database Performance page

performance statistics for an Oracle RAC database, [13.1.1.3](monitor.md)

configuring to recognize changes in database management, [3.7](admin.md)

Database Throughput charts, [13.1.1.3](monitor.md)

deleting database instances from nodes, [10.2.1](adddelunix.md), [11.2.1](adddelwin.md)

Global Cache Block Access Latency chart, [13.1.1.3](monitor.md)

Interconnects page, [13.1.1.2](monitor.md)

job administration, [3.11.3.1](admin.md)

monitoring load values for available nodes, [13.1.1.3](monitor.md)

overview and concepts, [1.6.2](admcon.md)

Top Activity drill down menu, [13.1.1.3](monitor.md)

using the Interconnects page to monitor Oracle Clusterware, [13.1.1](monitor.md)

using to administer Oracle RAC, [3.1.2](admin.md)

using to administer services, [5.9.2](hafeats.md)

using to back up the server parameter file, [3.5.3](admin.md)

using to create DTP services, [5.8.4](hafeats.md)

using to monitor Oracle Clusterware, [13.1.1](monitor.md)

using to monitor Oracle RAC, [13.1.1](monitor.md)

using to monitor Oracle RAC environments, [1.6.3](admcon.md)

using to restore SPFILE, [7.2.3](backup.md)

using to schedule Automatic Workload Repository actions, [5.11](hafeats.md)

using to set up a fast recovery area, [7.6](backup.md)

using to start or stop a database, [3.2.2](admin.md)

using with RMAN, [6.4](rman.md)

Oracle Enterprise Manager Database Control

using emca to reconfigure, [3.7](admin.md)

Oracle Enterprise Manager Grid Control

instance discovery, [3.11.1](admin.md)

node discovery, [3.11.1](admin.md)

Oracle home

cloning, [1.5.3](admcon.md)

defined, [1.5.2](admcon.md)

Oracle Interface Configuration (OIFCFG), [13.3](monitor.md)

Oracle Managed Files, [3.1.1](admin.md)

Oracle Maximum Availability Architecture (MAA), [12.1.1](design.md)

Oracle Net

listeners, [1.2](admcon.md)

Oracle Net Services

and load balancing, [5.7.1](hafeats.md)

and services, [5.3.2.9](hafeats.md)

Oracle Notification Service, [1.2](admcon.md)

SRVCTL object name, [A](srvctladmin.md)

used by FAN, [5.1](hafeats.md)

Oracle Notification Services

API, [5.5.1](hafeats.md)

Oracle processes

managed by Oracle Clusterware, [1.2](admcon.md)

Oracle RAC

adding administrator-managed database instances, [10.1.2.1](adddelunix.md), [11.1.1](adddelwin.md)

adding policy-managed database instances, [10.1](adddelunix.md), [11.1](adddelwin.md)

adding to nodes in a cluster on Linux and UNIX, [10.1](adddelunix.md)

adding to nodes in a cluster on Windows, [11.1](adddelwin.md)

and e-commerce, [12.3.5](design.md)

background processes

ACMS, [1.3.4](admcon.md)

GTX0-j, [1.3.4](admcon.md)

LCK0, [1.3.4](admcon.md)

LMD, [1.3.4](admcon.md)

LMON, [1.3.4](admcon.md)

LMS, [1.3.4](admcon.md)

RSMN, [1.3.4](admcon.md)

benefits of cloning, [8.1](clonerac.md)

cloning, [1.5.3](admcon.md), [8](clonerac.md)

size of the binaries, [8.1](clonerac.md)

converting database from, [4.3](onenode.md)

converting database to, [4.3](onenode.md)

converting single instance to Oracle RAC One Node, [4.3.1](onenode.md)

copying the Oracle RAC home, [8.2](clonerac.md)

databases

quiescing, [3.8](admin.md)

deploying clone, [8.3](clonerac.md)

diagnosing performance problems, [13.8.1](monitor.md)

diagnosing problems for, [B](appsupport.md)

installation overview, [1.5.2](admcon.md)

overview of administration, [1](admcon.md)

removing on Windows, [11.2.2](adddelwin.md)

removing the software from Linux and UNIX, [10.2.2](adddelunix.md)

security considerations, [12.3.8](design.md)

shutting down instances, [3.2.1](admin.md)

software components, [1.3.3](admcon.md)

storage options

network file system (NFS), [1.3.1](admcon.md)

Oracle Automatic Storage Management (Oracle ASM), [1.3.1](admcon.md)

Oracle Cluster File System (OCFS for Windows), [1.3.1](admcon.md)

volume manager, [1.3.1](admcon.md)

using a fast recovery area in, [7.6](backup.md)

Oracle RAC background processes

(RMSn), [1.3.4](admcon.md)

Oracle RAC Database introspection plug-in, [C](racdb.md)

Oracle RAC One Node, [Preface](whatsnew.md), [4](onenode.md)

adding databases, [4.2](onenode.md)

converting database from, [4.3](onenode.md)

converting database to, [4.3](onenode.md)

converting to Oracle RAC, [4.3.2](onenode.md)

online database relocation, [4.4](onenode.md)

relocating to another node, [4.4](onenode.md)

Oracle RAC One Node database

services on, [4.2](onenode.md)

Oracle Real Application Clusters

*See* Oracle RAC

Oracle Real Application Clusters Configuration Audit Tool

*See* RACcheck

Oracle Real Application Clusters One Node, [4](onenode.md)

*See* Oracle RAC One Node

Oracle Streams, [5.3.3.5](hafeats.md)

Oracle Streams Advanced Queuing

and FAN, [5.5.1](hafeats.md)

Oracle Universal Installer

database installation, [1.5.2](admcon.md)

Oracle RAC installation, [1.5.2](admcon.md)

ORACLE\_BASE environment variable, [8.3](clonerac.md)

ORACLE\_HOME environment variable, [8.3](clonerac.md)

ORACLE\_HOME\_NAME environment variable, [8.3](clonerac.md)

ORACLE\_SID parameter, [3.6.2](admin.md)

oradebug ipc command, [B.6](appsupport.md)

OraMTS

external transaction manager, [5.8.1](hafeats.md)

orapwd file, [3.7](admin.md)

outages

planned, [5.5.4](hafeats.md)

unplanned, [5.5.3](hafeats.md)

---

## P

parallel execution, [12.3.7.2](design.md)

parallel processes, [5.3.3.4](hafeats.md)

parallel recovery, [7.5.2.1](backup.md)

disabling, [7.5.2](backup.md)

PARALLEL\_EXECUTION\_MESSAGE\_SIZE initialization parameter, [3.6.1](admin.md)

PARALLEL\_FORCE\_LOCAL initialization parameter, [5.3.3.4](hafeats.md)

PARALLEL\_INSTANCE\_GROUPS initialization parameter, [5.3.3.4](hafeats.md)

parallelism

in Oracle RAC, [12.3.7.2](design.md)

parallel-aware query optimization, [12.3.7.1](design.md)

parameter file

overview, [3.5](admin.md)

parameter file search order, [3.5.2](admin.md)

parameters

DB\_RECOVERY\_FILE\_DEST, [7.6](backup.md)

that must be identical on all instances, [3.6.1](admin.md)

that must be unique on all instances, [3.6.2](admin.md)

password file-based authentication, [4.4](onenode.md)

performance, [13.1.1.3](monitor.md)

aggregates by services, [13.1.1.3](monitor.md)

comprehensive global data, [13.7](monitor.md)

monitoring activity by wait events, services, and instances, [13.1.1.3](monitor.md)

monitoring database throughput, [13.1.1.3](monitor.md)

monitoring global cache block access, [13.1.1.3](monitor.md)

monitoring potential problems in the database, [13.1.1.3](monitor.md)

primary components affecting, [13.2](monitor.md)

service aggregates by instances, [13.1.1.3](monitor.md)

service aggregates by waits, [13.1.1.3](monitor.md)

using ADDM, [1.6.3](admcon.md)

performance evaluation

overview and concepts, [1.6.4](admcon.md)

performance statistics, [13.9.5](monitor.md)

PFILE

using with Oracle RAC, [3.5](admin.md)

phases

cloning deployment, [8.3](clonerac.md)

cloning preparation, [8.2](clonerac.md)

PMON background process, [3.4](admin.md)

policy-managed database instances

adding, [11.1](adddelwin.md)

policy-managed databases, [3.1.1](admin.md), [3.6.2](admin.md), [5.3.2.7](hafeats.md)

defined, [1.6.1](admcon.md)

deleting on Linux and UNIX, [10.2.1](adddelunix.md)

deleting on Windows, [11.2.1](adddelwin.md)

PREFERRED instances

for services, [5.3.2.6](hafeats.md)

preferred read disks

Oracle ASM in an Oracle RAC extended distance cluster, [2.6.4](storage.md)

private interconnect, [B.6](appsupport.md)

determining usage, [B.6](appsupport.md)

private network

alternative interconnect, [3.9](admin.md)

private network IP address, [13.3](monitor.md)

processes

managed by Oracle Clusterware, [1.2](admcon.md)

parallel, [5.3.3.4](hafeats.md)

public and private interfaces

shown in Oracle Enterprise Manager, [13.1.1.2](monitor.md)

---

## Q

query optimizer, [12.3.7.1](design.md)

default cost model for, [12.3.7.1](design.md)

queue tables, [5.3.3.5](hafeats.md)

quiesce database

in Oracle Real Application Clusters, [3.8](admin.md)

quiesced databases, [3.8](admin.md)

quiescing

noncluster database, [3.8](admin.md)

---

## R

RACcheck, [D](racchk.md)

command options, [D](racchk.md)

comparing reports, [D](racchk.md)

configuration parameters, [D](racchk.md)

running in silent mode, [D](racchk.md)

running interactively, [D](racchk.md)

troubleshooting, [D](racchk.md)

RACcheck daemon, [D](racchk.md)

rebalancing

workloads, [5.2](hafeats.md)

RECOVER command, [3.1.3.2](admin.md)

SQL\*Plus, [3.1.3.2](admin.md)

recovery

after SHUTDOWN ABORT, [3.2.1](admin.md)

from multiple node failure, [7.3.2](backup.md)

from single-node failure, [7.3.1](backup.md)

instance, [3.2.1](admin.md)

media failures, [7.4](backup.md)

online, [7.3.1](backup.md)

parallel, [7.5.2.1](backup.md)

RECOVERY\_PARALLELISM parameter, [7.5.2.1](backup.md)

redo log files

instance recovery, [7.3.1](backup.md)

log sequence number, [6.8](rman.md)

using, [2.4](storage.md)

redo log groups, [2.4](storage.md)

redo logs

format and destination specifications, [6.8](rman.md)

redo thread, [3.1.1](admin.md)

reducing contention, [12.2](design.md)

remote Oracle Notification Service subscription, [5.7.2.1](hafeats.md)

Remote Slave Monitor (RSMN), [1.3.4](admcon.md)

REMOTE\_LISTENER database parameter, [5.4.1](hafeats.md)

REMOTE\_LOGIN\_PASSWORDFILE initialization parameter, [3.6.1](admin.md)

resource contention, [13.1.1.3](monitor.md)

resource manager, [5.2](hafeats.md)

Resource Manager

and services, [5.3.3.2](hafeats.md)

resource profiles

and service creation, [5.3.3.1](hafeats.md)

resources

releasing, [7.3.1](backup.md)

resources held by the session, [3.4](admin.md)

restore scenarios

RMAN, [7.2](backup.md)

restore scheme

cluster file system, [7.2.1](backup.md)

local file system, [7.2.2](backup.md)

result cache, [3.6](admin.md)

disabling, [3.6](admin.md)

enabling, [3.6](admin.md)

RESULT\_CACHE\_MAX\_SIZE initialization parameter, [3.6](admin.md), [3.6.1](admin.md)

RMAN

CONFIGURE command, [6.3](rman.md)

configuring channels, [6.5](rman.md)

configuring channels to use automatic load balancing, [6.6](rman.md)

configuring one channel for each instance, [6.6.2](rman.md)

configuring snapshot control file locations, [6.3](rman.md)

crosschecking on multiple nodes, [6.5](rman.md)

local archiving scenario, [6.9.2](rman.md)

restore scenarios, [7.2](backup.md)

using to create SPFILE backups, [3.5.3](admin.md)

RMSn

Oracle RAC Management Processes, [1.3.4](admcon.md)

rolling back

instance recovery, [7.3.1](backup.md)

root.sh script

$ORACLE\_HOME, [8.3](clonerac.md)

RSMN

Remote Slave Monitor, [1.3.4](admcon.md)

runtime connection load balancing

defined, [5.7.5](hafeats.md)

in OCI session pools, [5.7.5](hafeats.md)

introduction to, [5.1](hafeats.md)

Runtime Connection Load Balancing, [5.3.2.8](hafeats.md)

---

## S

scalability, [12.3.5](design.md)

Oracle RAC, [12.1.4](design.md)

scan

SRVCTL object name, [A](srvctladmin.md)

SCAN, [1.2](admcon.md)

defined, [1.4](admcon.md)

scan\_listener

SRVCTL object name, [A](srvctladmin.md)

scripts

$ORACLE\_HOME/root.sh, [8.3](clonerac.md)

security

wallet, [12.3.8.1](design.md)

sequence-based indexes, [12.2](design.md)

sequences

log sequence number, [6.8](rman.md)

Server Control Utility

*See* SRVCTL

Server Management

administration of instances, [3.1](admin.md)

server parameter file

backing up, [3.5.3](admin.md)

server parameter files

creating, [3.5](admin.md)

server pool, [3.1.1](admin.md)

concepts, [1.4](admcon.md)

creating for a policy-managed database, [3.7](admin.md)

Generic, [3.1.1](admin.md)

SRVCTL object name, [A](srvctladmin.md)

servers

relocating from another server pool, [3.7](admin.md)

scalability, [12.1.4](design.md)

service

SRVCTL object name, [A](srvctladmin.md)

service level objective

defining for Oracle RAC, [12.1.1](design.md)

service levels, [12.3.6](design.md)

service metrics

OCI runtime connection load balancing, [5.7.5](hafeats.md)

runtime connection load balancing, [5.7.5](hafeats.md)

SERVICE parameter

FAN, and matching database signature, [5.5.5](hafeats.md)

SERVICE TIME

load balancing advisory goal, [5.6.2](hafeats.md)

SERVICE\_NAMES initialization parameter, [3.6](admin.md)

setting for services, [3.6](admin.md), [5.9.1](hafeats.md)

service-level agreements, [3.4](admin.md)

services, [3.6](admin.md)

activity levels aggregated by instances, [13.1.1.3](monitor.md)

activity levels aggregated by services, [13.1.1.3](monitor.md)

activity levels aggregated by waits, [13.1.1.3](monitor.md)

administering, [5.9.1](hafeats.md)

administering with Oracle Enterprise Manager, [5.9](hafeats.md)

administering with SRVCTL, [5.9](hafeats.md), [5.9.3](hafeats.md)

attributes

edition, [5.3.2.3](hafeats.md)

basic concepts about, [5.3.1](hafeats.md)

concepts, [1.4](admcon.md)

configuring automatic workload management characteristics, [5.3.2](hafeats.md)

default, [5.3.4](hafeats.md)

dependencies, [5.3.3.1](hafeats.md)

enabling event notification, [5.7.5](hafeats.md)

introduction to, [1.3.2](admcon.md), [5.1](hafeats.md)

level thresholds, [5.11](hafeats.md)

management policy

automatic, [5.3.2.4](hafeats.md)

manual, [5.3.2.4](hafeats.md)

performance monitored by AWR, [5.3.3.3](hafeats.md)

SERVICE\_NAMES parameter, [3.6](admin.md), [5.9.1](hafeats.md)

specifying a service, [5.9.1](hafeats.md)

using, [5.3.1](hafeats.md)

services for administrator-managed databases, [3.7](admin.md)

sessions

terminating on a specific instance, [3.4](admin.md)

setting instances, [1.6.2](admcon.md), [3.1.3](admin.md)

shared everything, [1.3.1](admcon.md)

shared server configuration, [3.6](admin.md)

SHOW INSTANCE command, [3.1.3.2](admin.md)

SQL\*Plus, [3.1.3.2](admin.md)

SHOW PARAMETER command

SQL\*Plus, [3.1.3.2](admin.md)

SHOW PARAMETERS command, [3.1.3.2](admin.md)

SHOW SGA command, [3.1.3.2](admin.md)

SQL\*Plus, [3.1.3.2](admin.md)

SHUTDOWN ABORT, [3.2.1](admin.md), [B.5](appsupport.md)

SHUTDOWN command

ABORT option, [3.2.1](admin.md)

SQL\*Plus, [3.1.3.2](admin.md)

SHUTDOWN IMMEDIATE, [B.5](appsupport.md)

SHUTDOWN TRANSACTIONAL, [3.2.1](admin.md)

shutting down

instances, [3.2.1](admin.md)

shutting down an instance

abnormal shutdown, [3.2.1](admin.md)

shutting down instances, [3.2.1](admin.md)

sidalrt.log file, [B.3](appsupport.md)

single client access name

*See* SCAN

single client access name (SCAN)

SRVCTL object name, [A](srvctladmin.md)

single system image, [1.3.3](admcon.md)

SMON process

instance recovery, [7.3.1](backup.md), [7.3.2](backup.md)

recovery after SHUTDOWN ABORT, [3.2.1](admin.md)

snapshot control file, [6.3](rman.md)

configuring locations, [6.3](rman.md)

speed-up for data warehouse systems, [12.3.7.1](design.md)

SPFILE

backing up, [3.5.3](admin.md)

backups

creating, [3.5.3](admin.md)

changing parameter settings, [3.5](admin.md)

corrupted, [3.5.1](admin.md)

default names, [3.5.2](admin.md)

location, [3.5](admin.md)

naming convention for, [3.5.2](admin.md)

recovering, [3.5.3](admin.md)

restore with Oracle Enterprise Manager, [7.2.3](backup.md)

restore with RMAN, [7.2.3](backup.md)

setting values in, [3.5.1](admin.md)

SPFILE initialization parameter, [3.6](admin.md), [3.6.3](admin.md)

SQL statements

executing in parallel, [5.3.3.4](hafeats.md)

instance-specific, [3.1.3.2](admin.md)

SQL\*Plus, [3.1.3](admin.md)

changing the prompt, [3.1.3.1](admin.md), [3.1.3.1](admin.md)

commands

CONNECT, [3.1.3](admin.md)

effect on instances, [3.1.3.2](admin.md)

SRVCTL

add, usage description, [A](srvctladmin.md)

administering Oracle ASM instances, [2.6.6](storage.md)

administering services with, [5.9.3](hafeats.md)

cluster database configuration tasks, [A](srvctladmin.md)

cluster database tasks, [A](srvctladmin.md)

command syntax, [A](srvctladmin.md)

commands

add asm, [A](srvctladmin.md)

add cvu, [A](srvctladmin.md), [A](srvctladmin.md)

add database, [A](srvctladmin.md)

add filesystem, [A](srvctladmin.md)

add gns, [A](srvctladmin.md)

add instance, [A](srvctladmin.md)

add listener, [A](srvctladmin.md)

add network, [A](srvctladmin.md)

add nodeapps, [A](srvctladmin.md)

add ons, [A](srvctladmin.md)

add scan, [A](srvctladmin.md)

add scan\_listener, [A](srvctladmin.md)

add service, [A](srvctladmin.md)

add srvpool, [A](srvctladmin.md)

add vip, [A](srvctladmin.md)

config asm, [A](srvctladmin.md), [A](srvctladmin.md)

config cvu, [A](srvctladmin.md)

config database, [A](srvctladmin.md)

config filesystem, [A](srvctladmin.md)

config gns, [A](srvctladmin.md)

config nodeapps, [A](srvctladmin.md)

config oc4j, [A](srvctladmin.md)

config ons, [A](srvctladmin.md)

config scan, [A](srvctladmin.md)

config scan\_listener, [A](srvctladmin.md)

config service, [A](srvctladmin.md)

config srvpool, [A](srvctladmin.md)

config vip, [A](srvctladmin.md)

convert database, [A](srvctladmin.md)

disable asm, [A](srvctladmin.md)

disable cvu, [A](srvctladmin.md)

disable database, [A](srvctladmin.md)

disable diskgroup, [A](srvctladmin.md)

disable filesystem, [A](srvctladmin.md)

disable gns, [A](srvctladmin.md)

disable instance, [A](srvctladmin.md)

disable listener, [A](srvctladmin.md)

disable nodeapps, [A](srvctladmin.md)

disable oc4j, [A](srvctladmin.md)

disable ons, [A](srvctladmin.md)

disable scan, [A](srvctladmin.md)

disable scan\_listener, [A](srvctladmin.md)

disable service, [5.9.3.3](hafeats.md), [A](srvctladmin.md)

disable vip, [A](srvctladmin.md)

downgrade database, [A](srvctladmin.md)

enable asm, [A](srvctladmin.md)

enable cvu, [A](srvctladmin.md)

enable database, [A](srvctladmin.md)

enable diskgroup, [A](srvctladmin.md), [A](srvctladmin.md)

enable filesystem, [A](srvctladmin.md)

enable instance, [A](srvctladmin.md)

enable listener, [A](srvctladmin.md)

enable nodeapps, [A](srvctladmin.md)

enable oc4j, [A](srvctladmin.md)

enable ons, [A](srvctladmin.md)

enable scan, [A](srvctladmin.md)

enable scan\_listener, [A](srvctladmin.md)

enable service, [5.9.3.3](hafeats.md), [A](srvctladmin.md)

enable vip, [A](srvctladmin.md)

getenv asm, [A](srvctladmin.md)

getenv database, [A](srvctladmin.md)

getenv listener, [A](srvctladmin.md)

getenv nodeapps, [A](srvctladmin.md), [A](srvctladmin.md)

help, [A](srvctladmin.md)

modify asm, [A](srvctladmin.md)

modify cvu, [A](srvctladmin.md)

modify database, [A](srvctladmin.md)

modify filesystem, [A](srvctladmin.md)

modify gns, [A](srvctladmin.md)

modify instance, [A](srvctladmin.md)

modify listener, [A](srvctladmin.md)

modify network, [A](srvctladmin.md)

modify nodeapps, [A](srvctladmin.md)

modify oc4j, [A](srvctladmin.md)

modify ons, [A](srvctladmin.md)

modify scan, [A](srvctladmin.md)

modify scan\_listener, [A](srvctladmin.md)

modify service, [A](srvctladmin.md)

modify srvpool, [A](srvctladmin.md)

relocate cvu, [A](srvctladmin.md)

relocate database, [A](srvctladmin.md)

relocate gns, [A](srvctladmin.md)

relocate oc4j, [A](srvctladmin.md)

relocate scan, [A](srvctladmin.md)

relocate scan\_listener, [A](srvctladmin.md)

relocate server, [A](srvctladmin.md)

relocate service, [A](srvctladmin.md)

relocate vip, [A](srvctladmin.md)

remove asm, [A](srvctladmin.md)

remove database, [A](srvctladmin.md)

remove diskgroup, [A](srvctladmin.md)

remove filesystem, [A](srvctladmin.md)

remove gns, [A](srvctladmin.md)

remove instance, [A](srvctladmin.md)

remove listener, [A](srvctladmin.md)

remove nodeapps, [A](srvctladmin.md)

remove oc4j, [A](srvctladmin.md)

remove ons, [A](srvctladmin.md)

remove scan, [A](srvctladmin.md)

remove scan\_listener, [A](srvctladmin.md)

remove service, [A](srvctladmin.md)

remove srvpool, [A](srvctladmin.md)

remove vip, [A](srvctladmin.md)

setenv asm, [A](srvctladmin.md)

setenv database, [A](srvctladmin.md), [A](srvctladmin.md)

setenv listener, [A](srvctladmin.md)

setenv nodeapps, [A](srvctladmin.md)

srvctl setenv, [3.1.4](admin.md)

start asm, [A](srvctladmin.md)

start cvu, [A](srvctladmin.md)

start database, [3.2.4](admin.md), [A](srvctladmin.md)

start diskgroup, [A](srvctladmin.md)

start filesystem, [A](srvctladmin.md)

start gns, [A](srvctladmin.md)

start home, [A](srvctladmin.md)

start instance, [3.2.4](admin.md), [A](srvctladmin.md)

start listener, [A](srvctladmin.md)

start nodeapps, [A](srvctladmin.md)

start oc4j, [A](srvctladmin.md)

start ons, [A](srvctladmin.md)

start scan, [A](srvctladmin.md)

start scan\_listener, [A](srvctladmin.md)

start service, [A](srvctladmin.md)

start vip, [A](srvctladmin.md)

status asm, [A](srvctladmin.md)

status cvu, [A](srvctladmin.md)

status database, [A](srvctladmin.md)

status diskgroup, [A](srvctladmin.md)

status filesystem, [A](srvctladmin.md)

status gns, [A](srvctladmin.md)

status home, [A](srvctladmin.md)

status instance, [A](srvctladmin.md)

status listener, [A](srvctladmin.md)

status nodeapps, [A](srvctladmin.md)

status oc4j, [A](srvctladmin.md)

status ons, [A](srvctladmin.md)

status scan, [A](srvctladmin.md)

status scan\_listener, [A](srvctladmin.md)

status server, [A](srvctladmin.md)

status service, [A](srvctladmin.md)

status srvpool, [A](srvctladmin.md)

status vip, [A](srvctladmin.md)

stop asm, [A](srvctladmin.md)

stop cvu, [A](srvctladmin.md)

stop database, [3.2.4](admin.md), [A](srvctladmin.md)

stop diskgroup, [A](srvctladmin.md)

stop filesystem, [A](srvctladmin.md)

stop gns, [A](srvctladmin.md)

stop home, [A](srvctladmin.md)

stop instance, [3.2.4](admin.md), [A](srvctladmin.md)

stop listener, [A](srvctladmin.md)

stop nodeapps, [A](srvctladmin.md)

stop oc4j, [A](srvctladmin.md)

stop ons, [A](srvctladmin.md)

stop scan, [A](srvctladmin.md)

stop scan\_listener, [A](srvctladmin.md)

stop service, [A](srvctladmin.md)

stop vip, [A](srvctladmin.md)

unsetenv asm, [A](srvctladmin.md)

unsetenv database, [A](srvctladmin.md), [A](srvctladmin.md)

unsetenv listener, [A](srvctladmin.md)

unsetenv nodeapps, [A](srvctladmin.md)

upgrade database, [A](srvctladmin.md)

concurrent commands, [A](srvctladmin.md)

config, usage description, [A](srvctladmin.md)

convert, usage description, [A](srvctladmin.md)

deprecated commands and options, [A](srvctladmin.md)

disable, usage description, [A](srvctladmin.md)

downgrade, usage description, [A](srvctladmin.md)

enable, usage description, [A](srvctladmin.md)

enabling event notification, [5.7.5](hafeats.md)

getenv, usage description, [A](srvctladmin.md)

modify, usage description, [A](srvctladmin.md)

node-level tasks, [A](srvctladmin.md)

object name

database, [A](srvctladmin.md)

diskgroup, [A](srvctladmin.md)

filesystem, [A](srvctladmin.md)

Grid Naming Service (GNS), [A](srvctladmin.md)

home, [A](srvctladmin.md)

instance, [A](srvctladmin.md)

listener, [A](srvctladmin.md)

network, [A](srvctladmin.md)

node applications (nodeapps), [A](srvctladmin.md)

oc4j, [A](srvctladmin.md)

Oracle Automatic Storage Management (Oracle ASM), [A](srvctladmin.md)

Oracle Notification Service, [A](srvctladmin.md)

scan, [A](srvctladmin.md)

scan\_listener, [A](srvctladmin.md)

server pool (srvpool), [A](srvctladmin.md)

service, [A](srvctladmin.md)

vip, [A](srvctladmin.md)

object names, [A](srvctladmin.md)

overview, [3.1.4](admin.md)

overview and concepts, [1.6.2](admcon.md)

relocate, usage description, [A](srvctladmin.md)

remove, usage description, [A](srvctladmin.md)

setenv, usage description, [A](srvctladmin.md)

start service command, [5.9.3.2](hafeats.md), [5.9.3.2](hafeats.md)

start, usage description, [A](srvctladmin.md)

status service command, [5.9.3.5](hafeats.md)

status, usage description, [A](srvctladmin.md)

stop or start cluster database, [3.2.4](admin.md)

stop, usage description, [A](srvctladmin.md)

unsetenv, usage description, [A](srvctladmin.md)

upgrade, usage description, [A](srvctladmin.md)

SRVM\_TRACE environment variable, [B.4](appsupport.md)

Standard Edition

installing Oracle ASM, [1.5.2](admcon.md)

starting administrator-managed databases, [3.2.4](admin.md)

starting policy-managed databases, [3.2.4](admin.md)

STARTUP command

SQL\*Plus, [3.1.3.2](admin.md)

statistics

contents of, [13.6](monitor.md)

Statspack, [13.9](monitor.md), [13.9.1](monitor.md)

usage, [1.6.3](admcon.md)

stop database instances, [3.2.4](admin.md)

storage

cluster file system, [2.1](storage.md)

Oracle Automatic Storage Management (Oracle ASM), [2.6.1](storage.md)

subnet

configuring for virtual IP address, [A](srvctladmin.md), [A](srvctladmin.md)

subnets, [1.3.2](admcon.md)

SYS$BACKGROUND service, [5.3.4](hafeats.md)

SYS$USERS service, [5.3.4](hafeats.md)

SYSASM privilege, [3.1.3](admin.md), [3.2.3](admin.md)

SYSAUX tablespace

increasing size when adding nodes, [12.3.3](design.md)

reducing size when removing nodes, [12.3.3](design.md)

SYSDBA, [3.1.3](admin.md)

privilege for connecting, [3.1.3](admin.md)

SYSDBA connections to an Oracle ASM instance, [3.1.3](admin.md)

SYSOPER, [3.1.3](admin.md)

SYSOPER privilege

for connecting, [3.1.3](admin.md)

system change, [6.8](rman.md)

System Global Area (SGA), [1.3.3](admcon.md), [13.8.1](monitor.md)

size requirements, [1.3.3](admcon.md)

---

## T

tablespaces

automatic segment space management (ASSM) in Oracle RAC, [12.3.1](design.md)

automatic undo management in Oracle RAC, [12.3.1](design.md)

locally managed, [12.3.1](design.md)

use in Oracle RAC, [12.3.1](design.md)

TCP network ports

Windows Firewall considerations, [12.3.8.2](design.md)

TCP/IP, [1.3.2](admcon.md)

terminating a session on a specific instance, [3.4](admin.md)

THREAD initialization parameter, [3.6](admin.md)

threads

multiple application, [5.7.5](hafeats.md)

THROUGHPUT

load balancing advisory goal, [5.6.2](hafeats.md)

timed statistics, [13.6](monitor.md)

timeout

messages, avoiding, [1.3.2](admcon.md)

tnsnames.ora file, [3.6](admin.md)

Top Activity drill down menu

on the Cluster Database Performance page, [13.1.1.3](monitor.md)

Top Cluster Events, [13.8.2](monitor.md)

Top Cluster Events, ASH report, [13.8.2](monitor.md)

Top Remote Instance, [13.8.3](monitor.md)

Top Remote Instance, ASH report, [13.8.3](monitor.md)

trace files, [B.1](appsupport.md)

managing, [B.1](appsupport.md)

sidalrt.log, [B.3](appsupport.md)

trace files for background processes, [B.1](appsupport.md)

TRACE\_ENABLED initialization parameter, [3.6.3](admin.md)

tracing

enabling Java-based tools and utilities, [B.4](appsupport.md)

SRVM\_TRACE environment variable, [B.4](appsupport.md)

writing to log files, [B.4](appsupport.md)

transactions

instance failure, [7.3.1](backup.md)

rolling back, [3.4](admin.md), [7.3.1](backup.md)

waiting for recovery, [7.3.1](backup.md)

Transparent Application Failover

and services, [5.3.2.12](hafeats.md)

Transparent Data Encryption

specifying the ENCRYPTION\_WALLET\_LOCATION parameter, [12.3.8.1](design.md)

with encrypted wallets and obfuscated wallets, [12.3.8.1](design.md)

tuning

overview, [1.6.4](admcon.md)

using ADDM, [1.6.3](admcon.md)

---

## U

undo tablespace, [3.1.1](admin.md)

UNDO\_MANAGEMENT initialization parameter, [3.6.1](admin.md)

UNDO\_RETENTION initialization parameter, [3.6.3](admin.md)

UNDO\_TABLESPACE parameter, [3.6.2](admin.md)

Universal Connection Pool

benefits, [Preface](whatsnew.md)

User Datagram Protocol (UDP), [B.6](appsupport.md)

user process trace files, [B.1](appsupport.md)

---

## V

V$, [1.6.3](admcon.md)

V$ view, [13.4](monitor.md)

V$ACTIVE\_INSTANCES, [3.3](admin.md), [3.3](admin.md)

V$CLUSTER\_INTERCONNECTS, [13.2](monitor.md), [B.6](appsupport.md)

V$CONFIGURED\_INTERCONNECTS, [13.2](monitor.md)

vendor clusterware, [1.1](admcon.md)

verification

data files, online files, [2.3](storage.md)

verifying interconnect settings, [13.2](monitor.md)

versions

compatibility for Oracle RAC and Oracle Database software, [1.5.1](admcon.md)

views

creating for Oracle Real Application Clusters, [13.5](monitor.md)

dynamic performance

for performance monitoring, [13.4](monitor.md)

GV$, [13.4](monitor.md)

for performance monitoring, [13.4](monitor.md)

GV$SESSION, [3.4](admin.md), [3.4](admin.md)

instance-specific, [13.4](monitor.md)

V$ views, [13.4](monitor.md)

VIP

SRVCTL object name, [A](srvctladmin.md)

Virtual Internet Protocol (VIP) address, [1.2](admcon.md)

virtual IP address

requirements, [A](srvctladmin.md), [A](srvctladmin.md)

---

## W

wait events, [13.9](monitor.md), [13.9.1](monitor.md)

wallet

Welcome page, [10.1.2.1](adddelunix.md), [11.1.1.1](adddelwin.md)

Windows Firewall, [12.3.8.2](design.md)

workload management

workloads

---

## X

XA transactions

XA Transactions, [12.3.4](design.md)