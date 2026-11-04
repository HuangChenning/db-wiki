---
title: Index
book: Database High Availability Overview
doc_id: E17157-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17157/index.htm
tags:
  - oracle
  - 11g
  - high-availability-overview
---

A B C D E F G H I L M N O P R S T U V W

---

## Numerics

24x365, [1.1](overview.md)

64-bit systems

---

## A

access control

Active Data Guard

Active Session History (ASH)

ADD COLUMN

advisor framework, [6.1](manageability.md)

ALTER DATABASE RECOVER MANAGED STANDBY statement

analysis

determining high availability requirements, [2](hadesign.md)

applications

defining a virtual IP address, [7.1.2](architectures.md)

online maintenance and upgrades, [4.5](planned.md)

applying interim database patches, [4.1.3](planned.md)

architectures

choosing, [7.2](architectures.md), [7.2](architectures.md)

CPU, [3.6](unplanned.md)

failures in, [1.1](overview.md)

grid computing, [5.1](grid.md)

MAA, [7](architectures.md)

manageability, [2.2.5](hadesign.md)

multiple standby database, [7.1.5.2](architectures.md)

Oracle Application Server, [7.2](architectures.md), [7.3](architectures.md), [7.3.1](architectures.md)

Oracle Clusterware, [7.1.2](architectures.md)

Oracle Clusterware and Oracle Data Guard, [7.1.5.3](architectures.md), [7.1.6](architectures.md)

Oracle Data Guard, [7.1.5](architectures.md)

Oracle Data Guard standby hub, [7.1.5.2](architectures.md), [7.1.5.3](architectures.md)

Oracle Database, [7.1.1](architectures.md)

Oracle RAC, [7.1.4](architectures.md)

Oracle RAC and Oracle Data Guard, [7.1.8](architectures.md)

Oracle RAC on extended clusters, [7.1.4.1](architectures.md)

Oracle RAC One Node, [7.1.3](architectures.md)

Oracle RAC One Node and Oracle Data Guard, [7.1.7](architectures.md)

recommendations, [7.2](architectures.md)

requirements, [1.1](overview.md), [2.1](hadesign.md), [2.3](hadesign.md)

roadmap, [1.5](overview.md)

same processor platforms, [4.1.2](planned.md)

single standby database, [7.1.5](architectures.md), [7.1.5.1](architectures.md)

ASM

See Oracle Automatic Storage Management (Oracle ASM)

auditing

security control, [3.14](unplanned.md)

authentication

security controls, [3.14](unplanned.md)

automatic block repair, [3.8.9](unplanned.md), [3.20](unplanned.md)

automatic failover

Oracle Data Guard, [7.1.5.1](architectures.md)

automatic maintenance tasks, [6.1](manageability.md)

automatic shared memory management

dynamic memory allocation, [4.2.1](planned.md)

Automatic Workload Repository (AWR), [6.1](manageability.md)

availability

about, [1.1](overview.md)

disruptions, [1.3](overview.md)

roadmap, [1.5](overview.md)

See also high availability

---

## B

backing out a transaction, [3.8.3](unplanned.md)

backups

fast recovery area, [3.10](unplanned.md)

offload from the primary database, [3.6.1](unplanned.md)

Oracle Secure Backup, [3.13](unplanned.md)

between objects, [4.5.6](planned.md)

block corruption

repairing, [3.20](unplanned.md)

block recovery

reducing time, [3.20](unplanned.md)

using Flashback logs, [3.8.9](unplanned.md)

block recovery using flashback logs, [3.8.9](unplanned.md)

bounded recovery, [3.2](unplanned.md)

Bourne shell script

physru, [3.6.3](unplanned.md)

budget planning, [2.3.1](hadesign.md)

business impact analysis

internal knowledge management system example, [2.2.1](hadesign.md)

semiconductor manufacturer example, [2.2.1](hadesign.md)

business performance planning, [2.3.1](hadesign.md)

---

## C

change assurance, [6](manageability.md)

checkpointing

fast-start fault recovery, [3.2](unplanned.md)

choosing the correct high availability architecture, [7.2](architectures.md)

client failover, [3.19](unplanned.md)

Cluster Ready Services (CRS)

avoiding downtime during upgrades, [4.1.4](planned.md)

clusters

extended, [7.1.4.1](architectures.md)

Oracle Clusterware, [7.1.2](architectures.md)

cold cluster failover, [7.1.2](architectures.md), [7.1.6](architectures.md)

with Oracle Clusterware, [7.1.2](architectures.md)

with Oracle Clusterware and Data Guard, [7.1.6](architectures.md)

components

integrated with Oracle Restart, [3.3](unplanned.md)

compressed redo data

Oracle Data Guard, [7.1.5](architectures.md)

computer failure, [1.4](overview.md)

corruptions

prevention and detection, [3.21](unplanned.md)

repairing, [3.20](unplanned.md)

costs

quantifying, [2.2.2](hadesign.md)

CPU architectures, [3.6](unplanned.md)

CREATE TRIGGER statement

clauses for, [4.5.4](planned.md)

crossedition triggers, [4.5.1.3](planned.md)

---

## D

data corruptions, [1.4](overview.md)

automatic detection and repair, [3.20](unplanned.md)

detecting, [3.21](unplanned.md)

prevention and detection parameters, [3.21](unplanned.md)

data distribution

Oracle GoldenGate, [3.7](unplanned.md)

data encryption, [3.14](unplanned.md)

Data Guard

See Oracle Data Guard

data integration

Oracle GoldenGate, [3.7](unplanned.md)

data protection

maximizing, [1.2](overview.md)

Data Recovery Advisor, [3.12](unplanned.md)

data transformation, [3.7.1](unplanned.md)

data type restrictions

resolving with Extended Datatype Support (EDS), [4.1.9.1](planned.md), [4.1.9.4](planned.md)

data types

supporting advanced with EDS, [3.6.3](unplanned.md)

Database Replay, [6.2](manageability.md)

Database Server Grid, [5.1](grid.md)

about, [5.2](grid.md)

Database Storage Grid, [5.1](grid.md)

about, [5.3](grid.md)

database upgrades

using transportable tablespace, [4.1.9.2](planned.md)

databases

applying Oracle interim patches, [4.1.3](planned.md)

checkpointing, [3.2](unplanned.md)

dynamic reconfiguration, [4.2.1](planned.md)

security, [3.14](unplanned.md)

server grid, [5.1](grid.md)

data-loss tolerance, [2.2.4](hadesign.md)

DBA\_FLASHBACK\_TRANSACTION\_STATE view, [3.8.3](unplanned.md)

DBFS Content Store, [3.18](unplanned.md)

DBMS\_FLASHBACK.TRANSACTION\_BACKOUT() procedure, [3.8.3](unplanned.md)

DDL with the WAIT option, [4.5.3](planned.md)

dependencies, [4.5.6](planned.md)

DISABLE clause

FOLLOWS clause

CREATE TRIGGER statement, [4.5.4](planned.md)

disaster recovery solutions

Oracle Application Server, [7.3.1](architectures.md)

disk group

administering with Oracle ASM, [3.9](unplanned.md)

downtime

causes, [1.4](overview.md)

cost, [1.3](overview.md), [2.2.2](hadesign.md)

minimizing with Oracle GoldenGate and Oracle Data Guard, [4.1.9.3](planned.md)

mitigating, [1.3](overview.md)

solutions summary

planned, [4.1](planned.md)

unplanned, [3.1](unplanned.md)

See also unplanned downtime

dynamic reconfiguration, [4.2.1](planned.md)

---

## E

edition-based redefinition, [4.5.1](planned.md)

crossedition triggers, [4.5.1.3](planned.md)

editioning view, [4.5.1.2](planned.md)

editions, [4.5.1.1](planned.md)

ENABLE clause

CREATE TRIGGER statement, [4.5.4](planned.md)

encryption

of data, [3.14](unplanned.md)

endian format platforms

avoiding downtime during migration of different, [4.1.11](planned.md)

avoiding downtime during migration of same, [4.1.10](planned.md)

Exadata Cell, [3.16](unplanned.md)

See also Oracle Exadata Storage Server Software

EXCLUDE STANDBY option

of the RMAN RECOVER BLOCK command, [3.20](unplanned.md)

extended clusters

architecture, [7.1.4.1](architectures.md)

Extended Data Type Support (EDS)

rolling upgrades, [3.6.3](unplanned.md)

Extended Datatype Support (EDS)

patch set and database upgrades, [4.1.9](planned.md)

---

## F

failovers

fast, [7.1.5.1](architectures.md)

multiple standby databases

architecture, [7.1.5.2](architectures.md)

single standby database architecture, [7.1.5.1](architectures.md)

failure group

administering with Oracle ASM, [3.9](unplanned.md)

Oracle ASM, [3.9](unplanned.md)

failures

computer, [1.4](overview.md)

probability, [7.2](architectures.md)

site, [1.4](overview.md)

storage, [1.4](overview.md)

fast application notification (FAN)

for hardware upgrades, [4.1.1](planned.md)

for operating system upgrades, [4.1.1](planned.md)

Fast Connection Failover

for nonpooled connections, [3.4.2](unplanned.md)

Fast Mirror Resync

Oracle ASM, [3.9](unplanned.md)

fast recovery area

about, [3.10](unplanned.md)

benefits, [3.10](unplanned.md)

in a Data Guard configuration, [7.1.5](architectures.md)

fast-start failover

single standby database failover, [7.1.5.1](architectures.md)

Fast-Start Fault Recovery

benefits of using, [3.2](unplanned.md)

fault diagnosability infrastructure, [6.1](manageability.md)

flashback logs

block recovery using, [3.8.9](unplanned.md)

used by Flashback features, [3.8](unplanned.md)

Flashback technology

block recovery using Flashback logs, [3.8.9](unplanned.md)

See also Oracle Flashback technology

forward crossedition triggers, [4.5.1.3](planned.md)

frequency of outages, [7.2](architectures.md), [7.2](architectures.md)

FUSE (Filesystem in Userspace) API

with Client for Database Filesystem (CDF), [3.18](unplanned.md)

---

## G

grid computing, [5.1](grid.md)

Database Server Grid, [5.1](grid.md)

Database Storage Grid, [5.1](grid.md)

grids

server and storage, [5.1](grid.md)

growth planning, [2.3.1](hadesign.md)

---

## H

hangs or slow down, [1.4](overview.md)

hardware upgrades

avoiding downtime during, [4.1.1](planned.md)

using FAN during, [4.1.1](planned.md)

high availability

24x365, [1.1](overview.md)

about, [1.1](overview.md), [1.1](overview.md)

analysis framework, [2.1](hadesign.md)

applications, [7.3.1](architectures.md)

architectures, [1.1](overview.md), [2.2.5](hadesign.md), [7](architectures.md), [7.2](architectures.md)

business impact analysis, [2.2.1](hadesign.md)

determining requirements, [2](hadesign.md)

importance, [1.2](overview.md)

maximizing, [1.2](overview.md)

Oracle Application Server, [7.3](architectures.md)

Oracle Database, [7.1](architectures.md)

planned downtime, [4.1](planned.md)

planning, [2.3.1](hadesign.md)

setting manageability goals, [2.2.5](hadesign.md)

single-instance databases, [3.3](unplanned.md)

solutions, [1.1](overview.md)

unplanned downtime, [3](unplanned.md)

See also availability

high availability features

Oracle Database, [7.1.1](architectures.md)

hub-and-spoke deployment, [3.7.1](unplanned.md)

human errors, [1.4](overview.md)

---

## I

indexes

invisible, [4.5.7](planned.md)

intelligent infrastructure, [6](manageability.md), [6.1](manageability.md)

interblock corruption, [1.4](overview.md)

interconnects

Oracle RAC, [7.1.4](architectures.md)

intrablock corruption, [1.4](overview.md)

invisible indexes, [4.5.7](planned.md)

I/O Resource Management

Oracle Storage Grid, [5.3](grid.md)

---

## L

load balancing advisory, [3.4.2](unplanned.md)

logical corruption, [1.4](overview.md)

logical standby databases

about, [3.6.5](unplanned.md)

benefits of, [3.6.5](unplanned.md)

transient, [3.6.3](unplanned.md), [3.6.3](unplanned.md)

LogMiner utility

about, [3.15](unplanned.md)

lost writes, [1.4](overview.md)

---

## M

making data changes, [4.5.1.1](planned.md)

manageability

goals, [2.2.5](hadesign.md)

optimizing, [6](manageability.md)

overhead (MO), [2.2.5](hadesign.md), [7.2](architectures.md)

manual block repair, [3.20](unplanned.md)

Maximum Availability Architecture

See Oracle Maximum Availability Architecture (MAA)

media corruption

physical corruption, [1.4](overview.md)

memory

automatic management of, [4.2.2](planned.md)

memory advisors, [6.1](manageability.md)

MEMORY\_MAX\_TARGET initialization parameter, [4.2.2](planned.md)

MEMORY\_TARGET initialization parameter, [4.2.2](planned.md)

metadata

dependencies, [4.5.6](planned.md)

migrating storage

avoiding downtime, [4.1.6](planned.md)

migrations

32-bit to 64-bit systems, [4.1.2.1](planned.md)

Oracle Exadata Storage Server Software, [4.1.7](planned.md)

storage, [4.1.6](planned.md)

mirroring

Oracle ASM native, [3.9](unplanned.md)

multimaster replication, [3.7.1](unplanned.md)

multiple standby databases

Data Guard hub, [7.1.5.3](architectures.md)

failovers, [7.1.5.2](architectures.md)

using transient logical standby, [3.6.3](unplanned.md), [3.6.3](unplanned.md)

---

## N

nodes

virtual IP addresses, [7.1.2](architectures.md)

---

## O

observer

fast-start failover, [7.1.5.1](architectures.md)

one-off patches, [4.1.3](planned.md)

online database relocation utility, [7.1.3](architectures.md)

online maintenance

application, [4.5](planned.md)

online redefnition of tables, [4.3](planned.md)

online reorganization

about, [4.3](planned.md)

online table redefinition, [4.5.8](planned.md)

OPatch utility

patch upgrades for Oracle RAC, [4.1.3](planned.md)

operating systems

requirements for Oracle Clusterware, [7.1.2](architectures.md)

upgrades, [4.1.1](planned.md)

using FAN during upgrades, [4.1.1](planned.md)

Oracle Active Data Guard

standby databases

benefits of, [3.6.2](unplanned.md)

Oracle Active Data Guard option, [5.4.1](grid.md)

collecting ASH samples on, [6.1](manageability.md)

Oracle Application Server

high availability architectures, [7.3.1](architectures.md)

security, [7.3.1](architectures.md)

Oracle Automatic Storage Management (Oracle ASM)

about, [3.9](unplanned.md)

benefits, [3.9](unplanned.md)

distribution of files, [4.2.3](planned.md)

failure group, [3.9](unplanned.md)

Fast Mirror Resync, [3.9](unplanned.md)

native mirroring, [3.9](unplanned.md)

storage migration, [4.1.5](planned.md)

upgrading, [4.1.5](planned.md)

with Database Storage Grid, [5.3](grid.md)

Oracle Automatic Storage Management Cluster File System (Oracle ACFS), [3.9](unplanned.md), [7.1.1](architectures.md)

Oracle Call Interface (OCI), [3.4.2](unplanned.md)

Oracle Clusterware

about, [7.1.2](architectures.md)

advantages over third-party clusterware, [7.1.2](architectures.md)

avoiding downtime when upgrading, [4.1.4](planned.md)

benefits, [7.1.2](architectures.md)

cold cluster failover, [7.1.2](architectures.md)

configured with Data Guard, [7.1.6](architectures.md)

Oracle Data Guard

about, [3.6](unplanned.md)

benefits, [3.6](unplanned.md), [7.1.5](architectures.md)

benefits of, [3.6](unplanned.md)

configured with Oracle Clusterware, [7.1.6](architectures.md)

configuring with Oracle GoldenGate, [3.7.2](unplanned.md), [4.1.9.3](planned.md)

hub architecture, [7.1.5.3](architectures.md)

multiple standby database architecture, [7.1.5.2](architectures.md)

single standby database architecture, [7.1.5.1](architectures.md)

system and cluster upgrades, [4.1.2](planned.md)

Oracle Data Provider for.NET (ODP.NET), [3.4.2](unplanned.md)

Oracle Database

basic architecture, [7.1.1](architectures.md)

with Data Guard, [7.1.5](architectures.md)

with Oracle Clusterware (cold cluster failover), [7.1.2](architectures.md)

with Oracle Clusterware and Oracle Data Guard, [7.1.6](architectures.md)

with Oracle RAC, [7.1.4](architectures.md)

with Oracle RAC and Oracle Data Guard - MAA, [7.1.8](architectures.md)

with Oracle RAC on an extended cluster, [7.1.4.1](architectures.md)

Oracle Database File System (DBFS), [3.18](unplanned.md), [7.1.5](architectures.md)

Oracle Database Resource Manager Instance Caging, [7.1.3](architectures.md)

Oracle Enterprise Manager Grid Control, [6](manageability.md), [6.3](manageability.md)

Oracle Exadata Database Machine, [3.17](unplanned.md)

Oracle Exadata Storage Server Software, [3.16](unplanned.md)

combined with Sun Oracle Database Machine, [3.17](unplanned.md)

migrating, [4.1.7](planned.md)

upgrading, [4.1.8](planned.md)

Oracle Flashback Data Archive, [3.8.10](unplanned.md)

Oracle Flashback Database, [3.8.8](unplanned.md)

Oracle Flashback Drop, [3.8.6](unplanned.md)

Oracle Flashback Query, [3.8.1](unplanned.md)

Oracle Flashback Table, [3.8.5](unplanned.md)

Oracle Flashback technology, [3.8](unplanned.md)

Oracle Flashback Transaction, [3.8.3](unplanned.md)

Oracle Flashback Transaction Query, [3.8.4](unplanned.md)

Oracle Flashback Version Query, [3.8.2](unplanned.md)

Oracle GoldenGate, [3.7](unplanned.md)

about, [3.7](unplanned.md)

comparing to Oracle Streams, [3.7](unplanned.md)

configure to minimize downtime, [4.1.9.3](planned.md)

configuring with Oracle Data Guard, [3.7.2](unplanned.md)

rolling upgrades, [4.5.2](planned.md)

Oracle interim (one-off) patches, [4.1.3](planned.md)

applying, [4.1.3](planned.md)

avoiding downtime during, [4.1.3](planned.md)

Oracle Management Agents

Oracle Enterprise Management Grid Control, [6.3](manageability.md)

Oracle Management Repository

Oracle Enterprise Manager Grid Control, [6.3](manageability.md)

Oracle Management Service (OMS)

Oracle Enterprise Manager Grid Control, [6.3](manageability.md)

Oracle Maximum Availability Architecture (MAA)

about, [1.5](overview.md)

architectures, [7](architectures.md)

benefits, [7.1.8](architectures.md)

roadmap, [1.5](overview.md)

Oracle Real Application Clusters One Node, [7.1.3](architectures.md)

online database relocation utility, [7.1.3](architectures.md)

See Oracle RAC One Node

Oracle Real Application Clusters (Oracle RAC)

about, [7.1.4](architectures.md)

applying Oracle interim database patches, [4.1.3](planned.md)

automatic redundant interconnects, [7.1.4](architectures.md)

benefits, [3.4.2](unplanned.md)

extended clusters, [7.1.4.1](architectures.md)

operating system and hardware upgrades, [4.1.1](planned.md)

Storage Area Network (SAN), [7.1.4.1](architectures.md)

Oracle Restart, [3.3](unplanned.md)

Oracle Secure Backup

about, [3.13](unplanned.md)

benefits, [3.13](unplanned.md)

Oracle Streams, [3.7](unplanned.md)

comparing to Oracle GoldenGate, [3.7](unplanned.md)

Oracle UCP run-time connection load balancing, [3.4.2](unplanned.md)

Oracle VM

Domain Live Migration, [5.5](grid.md)

with Oracle RAC One Node, [7.1.3](architectures.md)

outages

frequency, [7.2](architectures.md), [7.2](architectures.md)

types of, [1.4](overview.md)

---

## P

performance

ASH sampling to address transient problems, [6.1](manageability.md)

physical corruption, [1.4](overview.md)

physical standby databases

benefits of, [3.6.1](unplanned.md)

collecting ASH samples, [6.1](manageability.md)

real-time query, [5.4.1](grid.md)

snapshot standby, [3.6.4](unplanned.md)

transient logical standby database, [3.6.3](unplanned.md)

physru shell script, [3.6.3](unplanned.md)

planned activities

probability of failure during, [7.2](architectures.md)

planned downtime

online patching, [4.1.3.1](planned.md)

recovery times, [7.2](architectures.md)

planned outages

minimizing with Oracle GoldenGate and Oracle Data Guard, [4.1.9.3](planned.md)

platform migrations

using transportable database, [4.1.10.1](planned.md)

policy management

prioritizing

high availability investment, [2.2.2](hadesign.md)

probability

of different failures during unplanned and planned activities, [7.2](architectures.md)

Program Global Area (PGA)

automatic management, [4.2.2](planned.md)

---

## R

real-time query, [5.4.1](grid.md)

collecting ASH samples on, [6.1](manageability.md)

reconfiguring

databases dynamically, [4.2.1](planned.md)

Recovery Manager (RMAN)

about, [3.11](unplanned.md)

benefits, [3.11](unplanned.md)

recovery point objective (RPO)

about, [2.2.4](hadesign.md), [7.2](architectures.md)

recovery time objective (RTO)

about, [2.2.3](hadesign.md), [7.2](architectures.md)

recovery times

planned downtime, [7.2](architectures.md)

reducing downtime from data block corruption, [3.20](unplanned.md)

unplanned downtime, [7.2](architectures.md)

redundant interconnect, [7.1.4](architectures.md)

relocation

online database, [7.1.3](architectures.md)

replication

Oracle GoldenGate, [3.7](unplanned.md)

Oracle Streams, [3.7](unplanned.md)

restore points

Oracle Flashback, [3.8.7](unplanned.md)

return on investment (ROI), [2.2.6](hadesign.md), [7.2](architectures.md)

optimizing, [5](grid.md)

reverse crossedition triggers, [4.5.1.3](planned.md)

RMAN RECOVER BLOCK command

repairing data block corruption, [3.20](unplanned.md)

roadmap to Maximum Availability Architecture (MAA), [1.5](overview.md)

rollback

transactions, [3.8.3](unplanned.md)

rolling upgrades

Oracle GoldenGate, [4.5.2](planned.md)

supporting data types with Extended Data Type Support (EDS), [3.6.3](unplanned.md)

using the physru shell script, [3.6.3](unplanned.md)

using transient logical standby, [3.6.3](unplanned.md), [3.6.3](unplanned.md)

row level security

virtual private database, [3.14](unplanned.md)

run-time connection load balancing, [3.4.2](unplanned.md)

---

## S

secure communications

between tiers in grid control environments, [6.3](manageability.md)

Secure Sockets Layer (SSL)

enabling for secure communications, [6.3](manageability.md)

use with grid control, [6.3](manageability.md)

SecureFile LOBs, [3.18](unplanned.md)

security

about, [3.14](unplanned.md)

benefits, [3.14](unplanned.md)

between tiers in firewall-protected environments, [6.3](manageability.md)

data encryption, [3.14](unplanned.md)

Oracle Application Server, [7.3.1](architectures.md)

Oracle ASM, [3.9](unplanned.md)

RMAN, [3.11](unplanned.md)

Segment Advisor, [6.1](manageability.md)

server grid, [5.1](grid.md)

server-generated alerts, [6.1](manageability.md)

servers

Oracle Clusterware requirements, [7.1.2](architectures.md)

service-level agreements (SLAs), [2.1](hadesign.md)

single standby database architecture

failovers, [7.1.5.1](architectures.md)

single-instance databases

Oracle Restart, [3.3](unplanned.md)

site failure, [1.4](overview.md)

SLAs, [2.1](hadesign.md)

snapshot standby database

about, [3.6.4](unplanned.md)

snapshot standby databases

benefits of, [3.6.4](unplanned.md)

SQL Access Advisor, [6.1](manageability.md)

SQL Apply

upgrades, [4.1.9](planned.md), [4.1.9.1](planned.md)

with Extended Datatype Support (EDS), [4.1.9.1](planned.md)

with logical standby databases, [3.6.5](unplanned.md)

SQL Performance Analyzer, [6.2](manageability.md)

SQL Tuning Advisor, [6.1](manageability.md)

SSL

See Secure Sockets Layer (SSL)

standby databases

active, [5.4](grid.md)

Active Data Guard option, [5.4.1](grid.md)

benefits of, [3.6](unplanned.md)

example hub configurations, [7.1.5.3](architectures.md)

logical standby, [3.6.3](unplanned.md), [3.6.3](unplanned.md)

multiple-standby architecture, [7.1.5.2](architectures.md)

single-standby architecture, [7.1.5.1](architectures.md)

snapshot standby database, [3.6.1](unplanned.md)

transient logical standby database, [3.6.1](unplanned.md)

standby reader farms, [5.4.2](grid.md)

storage

failures, [1.4](overview.md), [3.9](unplanned.md)

grid, [5.1](grid.md)

migration, [4.1.6](planned.md)

Oracle ASM protection, [3.9](unplanned.md)

Storage Area Network (SAN)

extended clusters, [7.1.4.1](architectures.md)

System Global Area (SGA)

automatic management, [4.2.2](planned.md)

system upgrades

avoiding downtime during, [4.1.1](planned.md)

---

## T

tables

editionable, [4.5.1.2](planned.md)

tape backups

with Oracle Secure Backup, [3.13](unplanned.md)

thin client watchdog

observer for fast-start failover, [7.1.5.1](architectures.md)

total cost of ownership (TCO), [2.2.6](hadesign.md), [7.2](architectures.md)

transactions

backing out with Flashback Transaction, [3.8.3](unplanned.md)

transient logical standby databases

about, [3.6.3](unplanned.md)

benefits of, [3.6.3](unplanned.md)

physru shell script, [3.6.3](unplanned.md)

transportable database

for platform migration, [4.1.10.1](planned.md)

for unplanned downtime, [4.4](planned.md)

transportable tablespace

for unplanned downtime, [4.4](planned.md)

upgrading the database, [4.1.9.2](planned.md)

---

## U

Undo Advisor, [6.1](manageability.md)

undo data

used by flashback features, [3.8](unplanned.md)

unplanned activities

probability of failure during, [7.2](architectures.md)

unplanned downtime

causes, [1.4](overview.md)

recovery times, [7.2](architectures.md)

solutions summary, [3.1](unplanned.md)

transportable technologies, [4.4](planned.md)

updatable standby databases, [3.6.4](unplanned.md)

upgrades

application, [4.5](planned.md)

cluster, [4.1.2](planned.md)

database, [4.1.9](planned.md)

hardware, [4.1.1](planned.md)

operating system, [4.1.1](planned.md), [4.1.2](planned.md)

Oracle ASM, [4.1.5](planned.md)

Oracle Clusterware, [4.1.4](planned.md)

Oracle Exadata Storage Server Software, [4.1.8](planned.md)

Oracle Real Application Clusters (Oracle RAC), [4.1.1](planned.md)

patches, [4.1.3](planned.md)

rolling with Oracle GoldenGate, [4.5.2](planned.md)

using crossedition triggers, [4.5.1.3](planned.md)

using transportable tablespace, [4.1.9.2](planned.md)

with logical standby databases (SQL Apply), [3.6.3](unplanned.md), [3.6.3](unplanned.md)

---

## V

V$DATABASE\_BLOCK\_CORRUPTION view, [3.21](unplanned.md)

virtual IP (VIP) address

virtual private database

virtualization

---

## W

WAIT option

Web scalability