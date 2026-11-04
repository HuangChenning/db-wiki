---
title: Index
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/index.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

A B C D E F G H I K L M N O P Q R S T U V W Z

---

## A

ACFS snapshot, [8.6.1](config_backuprec.md)

Active Data Guard option

Active Session History Reports (ASH), [5.2.3](config_db.md)

Advanced Queuing (AQ), [9.3.1](config_dg.md)

alerts

ALTER DATABASE statement

ALTER DISKGROUP ALL MOUNT statement, [4.5.3](config_storage.md)

ALTER SESSION ENABLE RESUMABLE statement, [5.2.9](config_db.md)

ANALYZE TABLE tablename VALIDATE STRUCTURE CASCADE, [9.3.8.3](config_dg.md)

application failover

DBMS\_DG.INITIATE\_FS\_FAILOVER, [13.2.4](outage.md)

in an Oracle Data Guard configuration, [13.2.4](outage.md)

in an Oracle RAC configuration, [13.2.4](outage.md)

application workloads

database performance requirements for, [4.1](config_storage.md)

applications

defining as services, [6.2.5](config_cw.md)

failover, [13.2.4](outage.md)

Fast Application Notification (FAN), [6.1.1.2](config_cw.md), [13.2.4](outage.md)

fast failover, [11.5](config_fcf.md)

login storms, [11.5](config_fcf.md)

monitor response times, [13.2.4](outage.md)

service brownouts, [12.2.3](monitor.md)

tracking performance with Beacon, [12.2.2](monitor.md)

upgrades, [14.2.9](schedule_outage.md)

Apply Lag

metric in Enterprise Manager, [12.2.4](monitor.md)

AQ\_HA\_NOTIFICATIONS parameter, [11.1](config_fcf.md)

AQ\_TM\_PROCESSES parameter, [9.4.1](config_dg.md)

architecture

high availability, [1.1](intro.md)

archival backups

keeping, [8.2.1](config_backuprec.md)

ARCHIVELOG mode, [5.1.1](config_db.md)

archiver (ARCn) processes

reducing, [9.4.1](config_dg.md)

archiving strategy, [9.3.5](config_dg.md)

ASM

See Oracle Automatic Storage Management (Oracle ASM), [4.2](config_storage.md)

ASM\_DISKGROUPS initialization parameter, [4.5.3](config_storage.md)

ASM\_DISKSTRING parameter, [4.4.1](config_storage.md)

ASM\_POWER\_LIMIT

initialization parameter, [4.5.2](config_storage.md)

ASM\_PREFERRED\_READ\_FAILURE\_GROUPS initialization parameter

in extended clusters, [7.3.4](config_rac.md)

ASMCA utility

storage management, [4.5.8](config_storage.md)

ASMCMD command-line utility

storage management, [4.5.7](config_storage.md)

ASMLib, [4.4.6](config_storage.md)

disk labels, [4.4.4](config_storage.md)

ASR

See Oracle Auto Service Request (ASR)

asynchronous disk I/O, [5.1.7](config_db.md)

asynchronous I/O

enabling, [7.1.3](config_rac.md)

V$IOSTAT\_FILE view, [5.1.7](config_db.md)

AUTOBACKUP statement

RMAN, [8.2.5](config_backuprec.md)

Automatic Database Diagnostic Monitor (ADDM), [5.2.3](config_db.md)

automatic performance tuning, [5.2.3](config_db.md)

automatic segment space management, [5.2.7](config_db.md)

using, [5.2.7](config_db.md)

Automatic Shared Memory Management, [5.1.9](config_db.md)

Automatic Storage Management (Oracle ASM)

redundancy, [4.3.2.2](config_storage.md)

automatic tablespace point-in-time recovery TSPITR, [13.2.7.4](outage.md)

automatic undo management

described, [5.2.5](config_db.md)

Automatic Workload Repository (AWR), [5.1.4](config_db.md), [5.2.3](config_db.md), [9.7](config_dg.md)

best practices, [5.2.3](config_db.md)

evaluating performance requirements, [4.1](config_storage.md)

AWR

See Automatic Workload Repository (AWR)

---

## B

backup and recovery

best practices, [8.2](config_backuprec.md)

checksums calculated during, [5.1.6.1](config_db.md)

enabling with ARCHIVELOG mode, [5.1.1](config_db.md)

backup files

fast recovery area disk group failure, [13.2.5.4](outage.md)

backup undo optimization, [8.1.3](config_backuprec.md)

backups

automatic, [8.2.5](config_backuprec.md)

comparing options, [8.3](config_backuprec.md)

configuring, [8.2](config_backuprec.md)

creating and synchronizing, [8.2.3](config_backuprec.md)

determine a retention policy, [8.2.1](config_backuprec.md)

keeping archival (long term), [8.2.1](config_backuprec.md)

OCR, [6.3.2](config_cw.md)

performing regularly, [8.5.4](config_backuprec.md)

RMAN recovery catalog, [8.2.2](config_backuprec.md)

Beacons, [12.2.2](monitor.md)

configuring, [12.2.2](monitor.md)

benefits

Data Guard broker, [9.3.1](config_dg.md)

high availability best practices, [1.2](intro.md)

best practices

AWR, [5.2.3](config_db.md)

backup and recovery, [8.2](config_backuprec.md)

Data Guard configuration, [9](config_dg.md)

Database Resource Manager, [5.2.10](config_db.md)

failover

manual, [9.4.2.4](config_dg.md)

failover (fast-start), [9.4.2.3](config_dg.md), [13.2.2.2](outage.md)

failover (manual), [13.2.2.3](outage.md), [13.2.2.3](outage.md)

fast connection failover configuration, [11](config_fcf.md)

high availability, [1.1](intro.md)

Oracle ASM configuration, [4.4](config_storage.md)

Oracle ASM operational best practices, [4.5](config_storage.md)

Oracle ASM strategic, [4.3](config_storage.md)

Oracle Clusterware configuration, [6.2](config_cw.md)

Oracle Clusterware operations and management, [6.3](config_cw.md)

Oracle Database configuration, [5.1](config_db.md)

Oracle Database operations and management, [5.2](config_db.md)

Oracle GoldenGate configuration, [10.2](config_gg.md)

Oracle RAC configuration, [7.1](config_rac.md), [7.1](config_rac.md)

Oracle RAC rolling upgrades, [14.2.4.2](schedule_outage.md)

storage subsystems, [4](config_storage.md)

switchover, [14.2.1.2](schedule_outage.md)

upgrades, [14.2.4.1](schedule_outage.md)

BLOCK CHANGE TRACKING clause, [8.2.4](config_backuprec.md)

brownouts, [12.2.3](monitor.md)

---

## C

capacity planning, [6.3.1](config_cw.md)

change tracking

for incremental backups, [8.2.4](config_backuprec.md)

checkpointing

bind Mean Time To Recover (MTTR), [7.1.1](config_rac.md)

client connections

migrating to and from nodes, [6.1.1](config_cw.md)

clients

application failover, [13.2.4](outage.md)

configuring for failover, [11.1](config_fcf.md)

load balancing, [6.2.6](config_cw.md)

cluster file system

using shared during software patching, [6.2.2](config_cw.md)

Cluster Health Monitor (CHM), [12.4](monitor.md)

Cluster Ready Services (CRS)

described, [13.3.1.1](outage.md)

moving services, [13.2.3.2](outage.md)

recovering service availability, [13.3.1.1](outage.md)

relationship to OCR, [13.2.3.3](outage.md)

Cluster Time Synchronization Service (CTSS), [6.2.8](config_cw.md)

clustered ASM

enabling the storage grid, [4.2.1](config_storage.md)

clusters

extended, [7.3](config_rac.md)

clusterwide outage

restoring the standby database after, [13.3.4](outage.md)

COMMIT NOWAIT

Oracle GoldenGate, [10.2.3](config_gg.md)

COMPATIBLE initialization parameter, [14.2.3](schedule_outage.md)

complete site failover

recovery time objective (RTO), [13.2.1.2](outage.md)

compression

redo transport, [9.3.7.2](config_dg.md)

configuring databases for high availability

with the MAA Advisor, [12.3.4](monitor.md)

configuring Oracle Database for shared server, [11.5](config_fcf.md)

connection pools

adjusting number of, [11.5](config_fcf.md)

Connection Rate Limiter

listener, [11.5](config_fcf.md)

connect-time failover, [13.3.1.3](outage.md)

control files

in a fast recovery area disk group failure, [13.2.5.4](outage.md)

CONTROL\_FILES initialization parameter, [13.2.5.4.1](outage.md)

coordinated, time-based, distributed database recovery, [13.2.8](outage.md)

corruptions

checking database files, [8.5.2](config_backuprec.md)

preventing with Data Recovery Advisor, [5.2.2](config_db.md)

CREATE DISKGROUP statement

examples, [4.3.1](config_storage.md), [4.3.2.1](config_storage.md)

CRS

See Cluster Ready Services (CRS)

crsctl command for system maintenance, [14.2.11](schedule_outage.md)

CRSD process

OCR backups, [6.3.2](config_cw.md)

CTSS

time management, [6.2.8](config_cw.md)

cumulative incremental backup set, [8.3](config_backuprec.md)

---

## D

Dark Fiber

Dense Wavelength Division Multiplexing (DWDM), [7.1.4](config_rac.md)

data

criticality and RPO, [8.2.1](config_backuprec.md)

recovering backups and RTO, [8.2.1](config_backuprec.md)

data area

contents, [4.3.1](config_storage.md)

disk partitioning, [4.3.1](config_storage.md)

data area disk group failure

recovery options, [13.2.5.3](outage.md)

data corruption

detecting, [5.1.6.2](config_db.md)

protection through Oracle ASM redundancy disk groups, [5.1.6.1](config_db.md)

solution, [5.1.6.1](config_db.md)

data failure

restoring fault tolerance on standby database, [13.3.5](outage.md)

Data Guard

archiving strategies, [9.3.5](config_dg.md)

broker, [9.3.1](config_dg.md)

using FAN/AQ, [9.3.1](config_dg.md)

database upgrades, [14.2.6.2](schedule_outage.md)

failover

best practices (fast-start), [9.4.2.3](config_dg.md)

best practices (manual), [9.4.2.4](config_dg.md)

recovery for data area disk group failures, [13.2.5.3](outage.md)

when to perform, [13.2.2.1](outage.md)

log apply services, [9.3.8](config_dg.md)

managing targets, [12.3.3](monitor.md)

monitoring, [12.2.4](monitor.md)

multiple standby databases, [9.3.9](config_dg.md)

performance, [9.7](config_dg.md)

platform migration, [14.2.7.4](schedule_outage.md)

protection against data corruption, [5.1.6.1](config_db.md)

redo transport services, [9.2.1](config_dg.md)

restoring standby databases, [13.3.2](outage.md)

role transitions, [9.4.2.4](config_dg.md)

snapshot standby databases, [9.6](config_dg.md)

SQL Apply, [14.2.6.2](schedule_outage.md)

standby-first patch apply, [14.2.3](schedule_outage.md)

status events in Enterprise Manager, [12.2.4](monitor.md)

switchover, [14.2.1.3](schedule_outage.md)

Data Pump

for platform migration, [14.2.7.7](schedule_outage.md)

moving the contents of the SYSTEM tablespace, [14.2.7.8](schedule_outage.md)

Data Recovery Advisor

detect and prevent data corruption, [5.2.2](config_db.md)

data retaining backups, [8.2.1](config_backuprec.md)

data type restrictions

resolving with Extended Datatype Support (EDS), [14.2.6.2.1](schedule_outage.md)

data-area disk group failure

See Also Data Guard failover, fast-start failover, local recovery

database files

management optimizations, [4.2](config_storage.md)

Oracle ASM integration, [4.2](config_storage.md)

recovery-related, [4.3.1](config_storage.md)

database patch upgrades

recommendations, [14.2.4.1](schedule_outage.md)

Database Resource Manager, [5.2.10](config_db.md)

best practices, [5.2.10](config_db.md)

Database Upgrade Assistant (DBUA), [14.2.6.1](schedule_outage.md)

database upgrades

with edition-based redefinition, [14.2.8](schedule_outage.md)

with transient logical standby database, [14.2.6.2.2](schedule_outage.md)

databases

checking files for corruption, [8.5.2](config_backuprec.md)

configuration recommendations, [5](config_db.md)

configuring with the MAA Advisor, [12.3.4](monitor.md)

evaluating performance requirements, [4.1](config_storage.md)

migration, [14.2.7.5](schedule_outage.md)

object reorganization, [14.2.10](schedule_outage.md)

recovery in a distributed environment, [13.2.8](outage.md)

resolving inconsistencies, [13.2.7.3](outage.md)

switching primary and standby roles among, [14.2.1.1](schedule_outage.md)

upgrades, [14.2.6](schedule_outage.md)

DB\_BLOCK\_CHECKING initialization parameter, [5.1.6.1](config_db.md), [9.3.8.3](config_dg.md)

DB\_BLOCK\_CHECKSUM initialization parameter, [4.6.1](config_storage.md), [5.1.6.1](config_db.md), [9.3.8.3](config_dg.md)

DB\_CACHE\_SIZE initialization parameter, [9.3.8.4](config_dg.md)

DB\_CREATE\_FILE\_DEST initialization parameter

enabling Oracle Managed Files, [4.3.1](config_storage.md)

DB\_CREATE\_ONLINE\_LOG\_DEST\_n initialization parameter

location of Oracle managed files, [4.3.1](config_storage.md)

DB\_FLASHBACK\_RETENTION\_TARGET parameter, [5.1.4](config_db.md)

DB\_KEEP\_CACHE\_SIZE initialization parameter, [9.3.8.4](config_dg.md)

DB\_LOST\_WRITE\_PROTECT initialization parameter, [5.1.6.1](config_db.md), [9.3.8.3](config_dg.md)

DB\_RECOVERY\_FILE\_DEST initialization parameter

fast recovery area, [5.1.3](config_db.md)

DB\_RECOVERY\_FILE\_DEST\_SIZE initialization parameter

limit for fast recovery area, [5.1.3](config_db.md)

DB\_RECYCLE\_CACHE\_SIZE initialization parameter, [9.3.8.4](config_dg.md)

DBCA

balancing client connections, [6.2.6](config_cw.md)

DBMS\_DG.INITIATE\_FS\_FAILOVER PL/SQL procedure

application failover, [13.2.4](outage.md)

DBMS\_FLASHBACK.TRANSACTION\_BACKOUT PL/SQL procedure, [13.2.7.1](outage.md)

DBMS\_REDEFINITION PL/SQL package, [14.2.10](schedule_outage.md)

DBVERIFY utility, [9.3.8.3](config_dg.md)

decision support systems (DSS)

application workload, [4.1](config_storage.md)

default temporary tablespace

specifying, [5.2.8](config_db.md)

DEFAULT TEMPORARY TABLESPACE clause

CREATE DATABASE statement, [5.2.8](config_db.md)

DEFAULT\_SDU\_SIZE sqlnet.ora parameter, [9.3.7.2](config_dg.md)

Dense Wavelength Division Multiplexing (DWDM or Dark Fiber), [7.1.4](config_rac.md)

Device Mapper

disk multipathing, [4.4.1](config_storage.md)

differential incremental backup set, [8.3](config_backuprec.md)

DISABLE BLOCK CHANGE TRACKING, [8.2.4](config_backuprec.md)

disabling parallel recovery, [5.1.10](config_db.md), [5.1.10](config_db.md)

disk backup methods, [8.3](config_backuprec.md)

disk devices

ASMLib disk name defaults, [4.4.4](config_storage.md)

configuration, [4.3.1](config_storage.md), [4.3.2.1](config_storage.md), [4.3.4](config_storage.md)

disk labels, [4.4.4](config_storage.md)

multipathing, [4.4.1](config_storage.md)

naming

ASM\_DISKSTRING parameter, [4.4.1](config_storage.md)

ASMLib, [4.4.6](config_storage.md)

partitioning for Oracle ASM, [4.3.1](config_storage.md)

protecting from failures, [4.3.2](config_storage.md)

disk errors

mining vendor logs, [4.5.6](config_storage.md)

disk failures

protection from, [4.3.2](config_storage.md)

restoring redundancy after, [4.3.2.2](config_storage.md)

disk groups

checking with V$ASM\_DISK\_IOSTAT view, [4.5.5](config_storage.md)

configuration, [4.3.1](config_storage.md)

determining size of, [4.3.2.2](config_storage.md), [4.3.4](config_storage.md)

failure of fast recovery area, [13.2.5.4](outage.md)

imbalanced, [4.5.5](config_storage.md)

mounting, [4.5.3](config_storage.md)

offline after failures, [13.2.5.4](outage.md)

SYSASM access to Oracle ASM instances, [4.5.1](config_storage.md)

disk multipathing, [4.4.1](config_storage.md)

DISK\_ASYNCH\_IO initialization parameter, [5.1.7](config_db.md), [9.3.8.6](config_dg.md)

DISK\_REPAIR\_TIME parameter, [4.4.5](config_storage.md)

disks

Oracle ASM failures, [13.2.5.2](outage.md), [13.2.5.2](outage.md)

distributed databases

recovering, [13.2.8](outage.md)

DNS failover, [13.2.1.3](outage.md)

dropped tablespace

fix using Flashback Database, [13.2.7.3](outage.md)

dropping database objects, [13.2.7.1](outage.md)

dual failures

restoring, [13.3.7](outage.md)

DWDM

Dense Wavelength Division Multiplexing., [7.1.4](config_rac.md)

---

## E

edition-based redefinition, [10.1.4](config_gg.md), [14.2.8](schedule_outage.md)

ENABLE BLOCK CHANGE TRACKING, [8.2.4](config_backuprec.md)

endian format

determining, [14.2.7.3](schedule_outage.md)

Enterprise Manager

alerts, [12.2.1](monitor.md)

Beacon

application failover, [13.2.4](outage.md)

Database Targets page, [12.2.3](monitor.md)

High Availability Console (HA Console), [12.3.3](monitor.md)

home page, [12.2.1](monitor.md)

MAA Advisor, [12.3.4](monitor.md)

managing Data Guard targets, [12.3.3](monitor.md)

managing patches, [12.3.2](monitor.md)

metrics, [12.2.1](monitor.md)

notification rules, [12.2.2](monitor.md), [12.2.3](monitor.md)

performance, [12.2.3](monitor.md)

policy violations, [12.3.1](monitor.md)

Policy Violations, [12.3.1](monitor.md)

Support Workbench, [12.2.2](monitor.md)

Enterprise Manager monitoring, [12.2](monitor.md)

equations

standby redo log files, [9.3.6](config_dg.md)

Estimated Failover Time

event in Enterprise Manager, [12.2.4](monitor.md)

Exadata Database Machine

and MAA best practices, [2.11](operational_bps.md)

HARD, [4.6.1](config_storage.md)

extended clusters

overview, [7.3](config_rac.md)

setting the ASM\_PREFERRED\_READ\_FAILURE\_GROUPS parameter, [7.3.4](config_rac.md)

extents

Oracle ASM mirrored, [5.1.6.1](config_db.md), [5.1.6.1](config_db.md)

external redundancy

Oracle ASM disk failures, [13.2.5.2](outage.md)

Oracle ASM server-based mirroring, [7.3.4](config_rac.md)

EXTERNAL REDUNDANCY clause

on the CREATE DISKGROUP statement, [4.3.2.1](config_storage.md)

Extraction, Transformation, and Loading (ETL)

application workload, [4.1](config_storage.md)

---

## F

failovers

application, [13.2.4](outage.md)

comparing manual and fast-start failover, [9.4.2.1](config_dg.md)

complete site, [13.2.1](outage.md)

defined, [13.2.2](outage.md)

described, [13.2.2.2](outage.md)

effect on network routes, [13.2.1.3](outage.md)

Fast Application Notification (FAN), [9.3.1](config_dg.md)

Fast Connection Failover, [11.5](config_fcf.md)

manual

best practices, [9.4.2.4](config_dg.md)

when to perform, [9.4.2.1](config_dg.md), [13.2.2.1](outage.md)

nondisruptive, [4.4.1](config_storage.md)

restoring standby databases after, [13.3.2](outage.md)

failure detection

CRS response, [13.2.3.2](outage.md)

failure groups

ASM redundancy, [4.3.5](config_storage.md)

defining, [4.3.2.2](config_storage.md)

multiple disk failures, [13.2.5.4](outage.md)

specifying in an extended cluster, [7.3.4](config_rac.md)

failures

rebalancing Oracle ASM disks, [13.2.5.2](outage.md)

space allocation, [5.2.9](config_db.md)

Fast Application Notification (FAN), [6.1.1.2](config_cw.md), [13.2.4](outage.md)

after failovers, [9.3.1](config_dg.md)

Fast Connection Failover, [11.5](config_fcf.md)

fast local restart

after fast recovery area disk group failure, [13.2.5.4.1](outage.md)

fast recovery area

backups, [8.4.3](config_backuprec.md)

contents, [4.3.1](config_storage.md)

disk group failures, [13.2.5.4](outage.md)

disk partitioning, [4.3.1](config_storage.md)

local recovery steps, [13.2.5.4.3](outage.md)

using, [5.1.3](config_db.md)

FAST\_START\_MTTR\_TARGET initialization parameter, [5.1.10](config_db.md), [7.1.1](config_rac.md)

controlling instance recovery time, [5.1.5](config_db.md)

setting in a single-instance environment, [7.1.1](config_rac.md)

FAST\_START\_PARALLEL\_ROLLBACK initialization parameter

determining how many processes are used for transaction recovery, [7.1.2](config_rac.md)

fast-start failover

comparing to manual failover, [9.4.2.1](config_dg.md)

fast-start fault recovery

instance recovery, [5.1.5](config_db.md)

FastStartFailoverAutoReinstate configuration property, [13.3.2](outage.md)

fault tolerance

configuring storage subsystems, [4](config_storage.md)

restoring, [13.3](outage.md)

restoring after OPEN RESETLOGS, [13.3.6](outage.md)

flash recovery area

See fast recovery area, [12.3.3](monitor.md)

Flashback Database, [13.2.7](outage.md), [13.2.7.3](outage.md)

enabling, [5.1.4](config_db.md), [5.1.4](config_db.md)

in Data Guard configurations, [9.3.3](config_dg.md)

setting maximum memory, [5.1.8](config_db.md)

Flashback Drop, [13.2.7](outage.md), [13.2.7.1](outage.md)

flashback logs

fast recovery area disk group failure, [13.2.5.4](outage.md)

Flashback Query, [13.2.7](outage.md), [13.2.7.2](outage.md)

Flashback Table, [13.2.7](outage.md), [13.2.7.1](outage.md)

flashback technology

example, [13.2.7.2](outage.md)

recovering from user error, [13.2.7](outage.md)

resolving database-wide inconsistencies, [13.2.7.3](outage.md)

resolving tablespace inconsistencies, [13.2.7.4](outage.md)

solutions, [13.2.7](outage.md)

Flashback Transaction, [13.2.7](outage.md)

DBMS\_FLASHBACK.TRANSACTION\_BACKOUT PL/SQL procedure, [13.2.7.1](outage.md)

Flashback Transaction Query, [13.2.7](outage.md), [13.2.7.2](outage.md)

Flashback Version Query, [13.2.7](outage.md), [13.2.7.2](outage.md)

FORCE LOGGING mode, [5.1.1](config_db.md), [9.3.4](config_dg.md)

full data file copy, [8.3](config_backuprec.md)

full or level 0 backup set, [8.3](config_backuprec.md)

---

## G

gap resolution

compression, [9.3.7.2](config_dg.md)

GoldenGate (Oracle GoldenGate), [10](config_gg.md)

Grid Control (Oracle Grid Control)

monitoring, [12.2](monitor.md)

guaranteed restore points, [8.1.4](config_backuprec.md)

GV$SYSSTAT view

gathering workload statistics, [4.1](config_storage.md)

---

## H

HA (Oracle High Availability technologies), [1.3](intro.md)

HARD Hardware Assisted Resilient Data, [4.6.1](config_storage.md)

Hardware Assisted Resilient Data (HARD)

when using Oracle ASM, [4.3.5](config_storage.md)

hardware RAID storage subsystem

deferring mirroring to, [7.3.4](config_rac.md)

High Availability

(HA) Console

monitoring databases, [12.3.3](monitor.md)

described, [1.1](intro.md)

restoring after fast-start failover, [13.3.2](outage.md)

high redundancy

Automatic Storage Management (Oracle ASM)

disk groups, [4.3.2.2](config_storage.md)

Oracle ASM disk failures, [13.2.5.2](outage.md)

Oracle ASM disk groups, [4.3.1](config_storage.md)

host bus adapters (HBA)

load balancing across, [4.4.1](config_storage.md)

HR service

scenarios, [13.3.1.1](outage.md)

human errors

recovery, [13.2.7](outage.md)

---

## I

imbalanced disk groups

checking, [4.5.5](config_storage.md)

incremental backups

BLOCK CHANGE TRACKING, [8.2.4](config_backuprec.md)

incrementally updated backup, [8.3](config_backuprec.md)

initialization parameters

primary and physical standby example, [9.3.5](config_dg.md)

instance failures

recovery, [5.1.5](config_db.md)

single, [13.2.3.1](outage.md)

instance recovery

controlling with fast-start fault recovery, [5.1.5](config_db.md)

interconnect subnet

verifying, [6.2.9](config_cw.md)

interim patches, [14.2.2](schedule_outage.md)

I/O operations

load balancing, [4.4.1](config_storage.md)

tuning, [9.3.8.6](config_dg.md)

---

## K

KEEP IDENTITY clause, [14.2.6.2.2](schedule_outage.md)

KEEP option

RMAN BACKUP command, [8.2.1](config_backuprec.md)

---

## L

library

ASMLib support for Oracle ASM, [4.4.6](config_storage.md)

listener connection rate throttling, [11.5](config_fcf.md)

listeners

balancing clients across, [6.2.6](config_cw.md)

Connection Rate Limiter, [11.5](config_fcf.md)

load balancing

application services, [13.3.1.3](outage.md)

client connections, [6.2.6](config_cw.md)

I/O operations, [4.4.1](config_storage.md)

through disk multipathing, [4.4.1](config_storage.md)

LOAD\_BALANCE parameter, [6.2.6](config_cw.md), [11.1](config_fcf.md)

balancing client connections, [6.2.6](config_cw.md)

local homes

use during rolling patches, [6.2.2](config_cw.md)

local recovery

after fast recovery area disk group failure, [13.2.5.4.1](outage.md)

for data area disk group failures, [13.2.5.3](outage.md)

for fast recovery area disk group failures, [13.2.5.4.3](outage.md)

locally managed tablespaces, [5.2.6](config_db.md)

described, [5.2.6](config_db.md)

log apply services

best practices, [9.3.8](config_dg.md)

LOG\_ARCHIVE\_DEST\_n initialization parameter, [9.3.9](config_dg.md)

LOG\_ARCHIVE\_FORMAT initialization parameter, [9.3.5](config_dg.md)

LOG\_ARCHIVE\_MAX\_PROCESSES initialization parameter, [9.3.7.1](config_dg.md)

setting in a multiple standby environment, [9.3.7.1](config_dg.md)

setting in an Oracle RAC, [9.3.7.1](config_dg.md)

LOG\_BUFFER initialization parameter, [5.1.4](config_db.md), [5.1.8](config_db.md)

LOG\_FILE\_NAME\_CONVERT initialization parameter, [9.4.1](config_dg.md), [9.4.2.2](config_dg.md)

logical standby databases

failover, [13.2.2.3](outage.md)

switchover, [14.2.1.3](schedule_outage.md)

upgrades on, [14.2.6.2](schedule_outage.md)

logical unit numbers (LUNs), [4.3.2.1](config_storage.md)

defined, [Glossary](glossary.md)

login storms

controlling with shared server, [11.5](config_fcf.md)

preventing, [11.5](config_fcf.md)

low bandwidth networks

compression on, [9.3.7.2](config_dg.md)

low-cost storage subsystems, [4.1](config_storage.md)

LUNs

See Also logical unit numbers (LUNs)

See logical unit numbers (LUNs), [4.3.2.1](config_storage.md)

---

## M

MAA

See Oracle Maximum Availability Architecture (MAA)

manageability

improving, [5.2](config_db.md)

managing scheduled outages, [14.1.1](schedule_outage.md), [14.1.2](schedule_outage.md)

manual failover

best practices, [9.4.2.4](config_dg.md), [13.2.2.3](outage.md)

comparing to fast-start failover, [9.4.2.1](config_dg.md)

when to perform, [9.4.2.1](config_dg.md), [13.2.2.1](outage.md)

Maximum Availability Architecture (MAA) Advisor page, [12.3.4](monitor.md)

maximum availability mode

redo transport requirements, [9.2.2](config_dg.md)

maximum number of connections

adjusting in the mid tier connection pool, [11.5](config_fcf.md)

maximum performance mode

redo transport requirements, [9.2.2](config_dg.md)

maximum protection mode

initialization parameter example, [9.3.5](config_dg.md)

Mean Time To Recover (MTTR)

checkpointing, [7.1.1](config_rac.md)

reducing with Data Recovery Advisor, [5.2.2](config_db.md)

memory consumption

managing with MEMORY\_TARGET parameter, [4.4.2](config_storage.md)

memory management, [5.1.9](config_db.md)

MEMORY\_TARGET initialization parameter, [4.4.2](config_storage.md)

metrics

Enterprise Manager, [12.2.1](monitor.md)

for Data Guard in Enterprise Manager, [12.2.4](monitor.md)

mid tier connection pool

adjusting maximum number of connections, [11.5](config_fcf.md)

migrating

planning for, [14.2.7](schedule_outage.md)

transportable database, [14.2.7.5](schedule_outage.md)

migration planning, [14.2.7.2](schedule_outage.md)

migration strategy

scheduled outages, [14.2.7.1](schedule_outage.md)

minimizing space usage, [8.3](config_backuprec.md)

minimizing system resource consumption, [8.3](config_backuprec.md)

mining vendor logs for disk errors, [4.5.6](config_storage.md)

mirrored extents

protection from data corruptions, [5.1.6.1](config_db.md), [5.1.6.1](config_db.md)

mirroring

across storage arrays, [4.3.2.2](config_storage.md)

deferring to RAID storage subsystem, [7.3.4](config_rac.md)

monitoring

application response time, [13.2.4](outage.md)

Enterprise Manager, [12.2](monitor.md)

Oracle Grid Control, [12.2](monitor.md)

rebalance operations, [14.2.5.2.2](schedule_outage.md)

mounting disk groups, [4.5.3](config_storage.md)

multipathing (disks)

path abstraction, [4.4.1](config_storage.md)

multiple disk failures, [13.2.5.4](outage.md)

---

## N

net services parameter

DEFAULT\_SDU\_SIZE, [9.3.7.2](config_dg.md)

RECV\_BUF\_SIZE, [9.3.7.2](config_dg.md)

SEND\_BUF\_SIZE, [9.3.7.2](config_dg.md)

TCP.NODELAY, [9.3.7.2](config_dg.md)

Network Attached Storage (NAS), [9.3.8.6](config_dg.md)

network detection and failover

Oracle Clusterware and Oracle RAC, [6.2.9](config_cw.md)

network routes

after site failover, [13.2.1.3](outage.md)

before site failover, [13.2.1.3](outage.md)

network server processes (LNSn), [Glossary](glossary.md)

Network Time Protocol (NTP), [6.2.8](config_cw.md)

NOCATALOG Mode

creating backups, [8.2.3](config_backuprec.md)

node failures

multiple, [13.2.3.1](outage.md)

nodes

migrating client connections, [6.1.1](config_cw.md)

nondisruptive failovers, [4.4.1](config_storage.md)

normal redundancy

Oracle ASM disk failures, [13.2.5.2](outage.md)

NORMAL REDUNDANCY clause

on the CREATE DISKGROUP statement, [4.3.2.2](config_storage.md)

notification rules

recommended, [12.2.3](monitor.md)

service-level requirement influence on monitoring, [12.2.2](monitor.md)

notifications

application failover, [13.2.4](outage.md)

NTP, [6.2.8](config_cw.md)

---

## O

OCI\_EVENTS parameter, [11.1](config_fcf.md)

OCR

backups of, [6.3.2](config_cw.md)

failure of, [13.2.3.3](outage.md)

recovering, [13.2.3.3](outage.md)

ocrconfig -showbackup command, [6.3.2](config_cw.md)

OMF

See Oracle Managed Files

online patching, [14.2.2](schedule_outage.md)

online redo log files

multiplex, [5.1.2](config_db.md)

Online Reorganization and Redefinition, [14.2.10](schedule_outage.md)

Online Transaction Processing (OLTP)

application workload, [4.1](config_storage.md)

opatch command-line utility, [14.2.4](schedule_outage.md)

optimizing

recovering times, [8.3](config_backuprec.md)

Oracle ACFS snapshot, [8.6.1](config_backuprec.md)

Oracle ASM

See Oracle Automatic Storage Management (Oracle ASM), [4.2](config_storage.md)

Oracle Auto Service Request (ASR), [2.10.2](operational_bps.md)

Oracle Automatic Storage Management (Oracle ASM)

ASM\_DISKSTRING parameter, [4.4.1](config_storage.md)

ASMLib, [4.4.6](config_storage.md)

clustering to enable the storage grid, [4.2.1](config_storage.md)

configuring with ASMCA, [4.5.8](config_storage.md)

database file management, [4.2](config_storage.md)

disk device allocation, [4.3.1](config_storage.md)

disk failures, [13.2.5.2](outage.md), [13.2.5.2](outage.md)

disk group size, [4.3.2.2](config_storage.md), [4.3.4](config_storage.md)

failure groups, [7.3.4](config_rac.md)

failure groups and redundancy, [4.3.5](config_storage.md)

handling disk errors, [4.5.6](config_storage.md)

HARD-compliant storage, [4.3.5](config_storage.md)

imbalanced disk groups, [4.5.5](config_storage.md)

managing memory with MEMORY\_TARGET parameter, [4.4.2](config_storage.md)

managing with ASMCMD, [4.5.7](config_storage.md)

migrating databases to and from, [14.2.5.2.1](schedule_outage.md)

multiple disk failures, [13.2.5.4](outage.md)

Oracle Restart, [4.2.2](config_storage.md)

power limit for faster rebalancing, [4.6.2](config_storage.md)

REBALANCE POWER, [4.5.2](config_storage.md)

rebalancing, [4.5.4](config_storage.md)

rebalancing disks after a failure, [13.2.5.2](outage.md)

recovery, [13.2.5](outage.md)

redundancy, [4.3.2.2](config_storage.md), [5.1.6.1](config_db.md), [5.1.6.1](config_db.md)

rolling upgrade, [14.2.5.2.3](schedule_outage.md)

server-based mirroring, [7.3.4](config_rac.md)

SYSASM role, [4.5.1](config_storage.md), [4.5.1](config_storage.md)

using disk labels, [4.4.4](config_storage.md)

using normal or high redundancy, [4.3.2.2](config_storage.md), [7.3.4](config_rac.md)

volume manager, [7.3.4](config_rac.md)

with disk multipathing software, [4.4.1](config_storage.md)

Oracle Cluster Registry (OCR)

failure of, [13.2.3.3](outage.md)

Oracle Clusterware

capacity planning, [6.3.1](config_cw.md)

CTSS time management, [6.2.8](config_cw.md)

system maintenance, [14.2.11](schedule_outage.md)

verifying the interconnect subnet, [6.2.9](config_cw.md)

Oracle Data Guard

See Data Guard, [9](config_dg.md)

Oracle Data Pump

for platform migration, [14.2.7.7](schedule_outage.md)

platform migrations, [14.2.7.7](schedule_outage.md)

Oracle Database 11g

configuration recommendations, [5](config_db.md)

Data Guard, [9](config_dg.md)

extended cluster configurations, [7.3](config_rac.md)

Oracle RAC configuration recommendations, [7.1](config_rac.md)

Oracle Enterprise Manager

High Availability (HA) Console, [12.3.3](monitor.md)

MAA Advisor page, [12.3.4](monitor.md)

Oracle Flashback Database

restoring fault tolerance to configuration, [13.3.2](outage.md)

Oracle GoldenGate

and Oracle RAC, [10.1.2](config_gg.md)

best practices, [10](config_gg.md)

configuring, [10](config_gg.md)

database migration, [14.2.7.6](schedule_outage.md)

for database upgrades, [14.2.6.3](schedule_outage.md)

overview, [10](config_gg.md)

replicat commit, [10.2.3](config_gg.md)

replicat COMMIT NOWAIT, [10.2.3](config_gg.md)

upgrades using, [14.2.6.3](schedule_outage.md)

with Oracle Data Guard, [10.1.3](config_gg.md)

Oracle Grid Control

home page, [12.2.1](monitor.md)

monitoring, [12.2](monitor.md)

Oracle High Availability technologies, [1.3](intro.md)

Oracle Managed Files (OMF)

database file management, [4.3.1](config_storage.md)

disk and disk group configuration, [4.3.1](config_storage.md)

fast recovery area, [5.1.3](config_db.md)

Oracle Management Agent, [12.2](monitor.md)

monitoring targets, [12.2](monitor.md)

Oracle Maximum Availability Architecture (MAA)

defined, [Glossary](glossary.md)

described, [1.3](intro.md)

website, [1.3](intro.md)

Oracle Notification Service (ONS)

after failovers, [9.3.1](config_dg.md)

Oracle RAC rolling patch upgrades, [14.2.4](schedule_outage.md)

Oracle Real Application Clusters (Oracle RAC)

adding disks to nodes, [4.4.6](config_storage.md)

application failover, [13.2.4](outage.md)

configuration, [7.1](config_rac.md)

extended clusters, [7.3](config_rac.md)

network detection and failover, [6.2.9](config_cw.md)

preparing for switchovers, [9.4.1](config_dg.md)

recovery from unscheduled outages, [13.2.3](outage.md)

restoring failed nodes or instances, [13.3.1](outage.md)

rolling upgrade, [14.2.4](schedule_outage.md)

rolling upgrades, [14.2.4](schedule_outage.md)

setting LOG\_ARCHIVE\_MAX\_PROCESSES initialization parameter, [9.3.7.1](config_dg.md)

system maintenance, [14.2.11](schedule_outage.md)

using redundant dedicated connections, [7.1.4](config_rac.md)

verifying the interconnect subnet, [6.2.9](config_cw.md)

voting disk, [6.2.7](config_cw.md), [7.3.2](config_rac.md), [13.2.3.3](outage.md)

Oracle Restart, [4.2.2](config_storage.md), [5.2.1](config_db.md)

Oracle Secure Backup, [8.1.3](config_backuprec.md)

OCR backups, [6.3.2](config_cw.md)

Oracle Storage Grid, [4.6](config_storage.md)

Oracle Streams

and Oracle GoldenGate, [10.1.1](config_gg.md)

Oracle Sun SFS Storage Appliance, [8.6.2](config_backuprec.md)

Oracle Universal Installer, [14.2.4.2](schedule_outage.md)

outages

unscheduled, [13.1](outage.md)

---

## P

parallel recovery

disabling, [5.1.10](config_db.md)

PARALLEL\_EXECUTION\_MESSAGE\_SIZE parameter, [5.1.4](config_db.md)

partitions

allocating disks for Oracle ASM use, [4.3.1](config_storage.md)

patch sets

rolling upgrades, [14.2.4](schedule_outage.md)

patches

managing with Enterprise Manager, [12.3.2](monitor.md)

rolling, [6.2.2](config_cw.md)

using shared cluster file system, [6.2.2](config_cw.md)

path failures

protection from, [4.4.1](config_storage.md)

performance

application, tracking with Beacon, [12.2.2](monitor.md)

asynchronous disk I/O, [5.1.7](config_db.md)

automatic tuning, [5.2.3](config_db.md)

Data Guard, [9.7](config_dg.md)

database, gathering requirements, [4.1](config_storage.md)

physical standby databases

as snapshot standby databases, [9.6](config_dg.md)

failover, [13.2.2.3](outage.md)

location migrations, [14.2.7.9](schedule_outage.md)

real-time query, [9.5](config_dg.md)

switchover, [14.2.1.3](schedule_outage.md)

platform migrations, [14.2.6](schedule_outage.md)

endian format for, [14.2.7.3](schedule_outage.md)

with physical standby database, [14.2.7.4](schedule_outage.md)

point-in-time recovery

TSPITR, [13.2.7.4](outage.md)

pool

resizing, [5.1.9](config_db.md)

power limit

setting for rebalancing, [4.6.2](config_storage.md)

preferred read failure groups

specifying Oracle ASM, [7.3.4](config_rac.md)

preventing login storms, [11.5](config_fcf.md)

primary database

reinstating after a fast-start failover, [13.3.2](outage.md)

restoring fault tolerance, [13.3.6](outage.md)

PROCESSES initialization parameter, [4.4.3](config_storage.md)

---

## Q

quorum disk

voting disk, [7.3.2](config_rac.md)

---

## R

RAID protection, [4.3.2.1](config_storage.md)

real-time apply

configuring for switchover, [9.4.1](config_dg.md)

real-time query

Active Data Guard option, [9.5](config_dg.md)

rebalance operations, [4.5.2](config_storage.md)

monitoring, [14.2.5.2.2](schedule_outage.md)

Oracle ASM disk partitions, [4.3.1](config_storage.md), [4.3.1](config_storage.md)

REBALANCE POWER

limits, [4.5.2](config_storage.md)

rebalancing, [4.5.4](config_storage.md)

Oracle ASM disk groups, [4.5.2](config_storage.md), [4.5.5](config_storage.md)

Oracle ASM disks after failure, [13.2.5.2](outage.md)

setting Oracle ASM power limit, [4.6.2](config_storage.md)

recommendations

database configuration, [5](config_db.md)

recovery

coordinated, time-based, distributed database recovery, [13.2.8](outage.md)

options for fast recovery area, [13.2.5.4](outage.md)

steps for unscheduled outages, [13.1.1](outage.md)

testing procedures, [8.5.3](config_backuprec.md)

times optimizing, [8.3](config_backuprec.md)

recovery catalog

including in regular backups, [8.5.4](config_backuprec.md)

RMAN repository, [8.2.2](config_backuprec.md)

recovery files

created in the recovery area location, [5.1.3](config_db.md)

Recovery Manager

See Also RMAN

recovery point objective (RPO)

criticality of data, [8.2.1](config_backuprec.md)

defined, [Glossary](glossary.md)

for data area disk group failures, [13.2.5.3](outage.md)

solutions for disk group failures, [13.2.5.4](outage.md)

recovery time objective (RTO)

defined, [Glossary](glossary.md)

described, [13.2.1.2](outage.md)

for data-area disk group failures, [13.2.5.3](outage.md)

recovery time, [8.2.1](config_backuprec.md)

solutions for disk group failures, [13.2.5.4](outage.md)

RECOVERY\_ESTIMATED\_IOS initialization parameter

for parallel recovery, [5.1.10](config_db.md)

RECOVERY\_PARALLELISM initialization parameter, [5.1.10](config_db.md), [5.1.10](config_db.md)

RECV\_BUF\_SIZE sqlnet.ora parameter, [9.3.7.2](config_dg.md)

recycle bin, [13.2.7.1](outage.md)

Redo Apply

real-time query, [9.5](config_dg.md)

Redo Apply Rate

event in Enterprise Manager, [12.2.4](monitor.md)

redo data

compressing, [9.3.7.2](config_dg.md)

redo log members

fast recovery area disk group failure, [13.2.5.4](outage.md)

redo transport services

best practices, [9.2.1](config_dg.md)

redundancy

Automatic Storage Management (Oracle ASM), [4.3.2.2](config_storage.md)

CREATE DISKGROUP DATA statement, [4.3.2.1](config_storage.md)

dedicated connections, [7.1.4](config_rac.md)

disk devices, [4.3.2](config_storage.md)

restoring after disk failures, [4.3.2.2](config_storage.md)

reinstatement, [13.3.2](outage.md)

FastStartFailoverAutoReinstate property, [13.3.2](outage.md)

remote archiving, [9.3.5](config_dg.md)

REMOTE\_LISTENER parameter, [6.2.5](config_cw.md), [6.2.6](config_cw.md)

resetlogs on primary database

restoring standby database, [13.3.6](outage.md)

resource consumption

minimizing, [8.3](config_backuprec.md)

resource management

using Database Resource Manager, [5.2.10](config_db.md)

response times

detecting slowdown, [13.2.4](outage.md)

restore points, [8.1.4](config_backuprec.md)

restoring

client connections, [13.3.1.3](outage.md)

failed instances, [13.3.1](outage.md)

failed nodes, [13.3.1](outage.md)

services, [13.3.1.1](outage.md)

resumable space allocation, [5.2.9](config_db.md), [5.2.9](config_db.md)

RESUMABLE\_TIMEOUT initialization parameter, [5.2.9](config_db.md)

RESYNC CATALOG command

resynchronize backup information, [8.2.3](config_backuprec.md)

RETENTION GUARANTEE clause, [5.2.5](config_db.md), [5.2.5](config_db.md), [8.2.7](config_backuprec.md)

retention policy for backups, [8.2.1](config_backuprec.md)

RMAN

backup undo optimization, [8.1.3](config_backuprec.md)

BACKUP VALIDATE command, [9.3.8.3](config_dg.md)

calculates checksums, [5.1.6.1](config_db.md)

creating standby databases, [9.3.2](config_dg.md)

database backups, [8.1.2](config_backuprec.md)

DUPLICATE command, [8.5.3](config_backuprec.md)

DUPLICATE TARGET DATABASE FOR STANDBY command, [9.3.2](config_dg.md)

FROM ACTIVE DATABASE command, [9.3.2](config_dg.md)

recovery catalog, [8.2.2](config_backuprec.md)

TSPITR, [13.2.7.4](outage.md)

unused block compression, [8.1.3](config_backuprec.md)

VALIDATE command, [8.5.2](config_backuprec.md)

RMAN BACKUP command

KEEP option, [8.2.1](config_backuprec.md)

role transitions

best practices, [9.4.2.4](config_dg.md)

role-based destinations, [9.3.5](config_dg.md)

rolling patches, [6.2.2](config_cw.md)

rolling upgrade

Oracle RAC, [14.2.4](schedule_outage.md)

rolling upgrades

patch set, [14.2.4](schedule_outage.md)

row and transaction inconsistencies, [13.2.7.2](outage.md)

RPO

See recovery point objective (RPO)

RTO

See recovery time objective (RPO)

---

## S

SALES scenarios

setting initialization parameters, [9.3.5](config_dg.md)

SAME

See stripe and mirror everything (SAME)

scenarios

fast-start failover, [13.3.2.1](outage.md)

HR service, [13.3.1.1](outage.md)

object reorganization, [14.2.10](schedule_outage.md)

Oracle ASM disk failure and repair, [13.2.5.2.1](outage.md)

recovering from human error, [13.2.7.2](outage.md)

SALES, [9.3.5](config_dg.md)

scheduled outages

Data Guard standby-first patch apply, [14.2.3](schedule_outage.md)

described, [14.1](schedule_outage.md)

edition-based redefinition, [14.2.8](schedule_outage.md)

migration, [14.2.7](schedule_outage.md)

migration planning, [14.2.7.2](schedule_outage.md)

migration strategy, [14.2.7.1](schedule_outage.md)

online patching, [14.2.2](schedule_outage.md)

Oracle ASM

rolling upgrade, [14.2.5.2.3](schedule_outage.md)

Oracle Real Application Clusters (Oracle RAC) rolling patch upgrades, [14.2.4](schedule_outage.md)

platform migration, [14.2.7.4](schedule_outage.md)

primary site, [14.1.1](schedule_outage.md)

recommended solutions, [14.1.1](schedule_outage.md), [14.1.2](schedule_outage.md)

reducing downtime for, [14.2](schedule_outage.md)

secondary site, [14.1.2](schedule_outage.md)

switchback, [14.2.1](schedule_outage.md)

switchover, [14.2.1](schedule_outage.md)

transportable tablespaces upgrades, [14.2.6.4](schedule_outage.md)

upgrades with Oracle GoldenGate, [14.2.6.3](schedule_outage.md)

See Also unscheduled outages

secondary site outage

restoring the standby database after, [13.3.4](outage.md)

SEND\_BUF\_SIZE sqlnet.ora parameter, [9.3.7.2](config_dg.md)

server parameter file (SPFILE), [5.2.4](config_db.md), [9.3.5](config_dg.md)

backup with RMAN, [8.2.5](config_backuprec.md)

server-based mirroring

Oracle ASM, [7.3.4](config_rac.md)

service availability

recovering, [13.3.1.1](outage.md)

service level agreements (SLA), [1.3](intro.md)

effect on monitoring and notification, [12.2.2](monitor.md)

service tests and Beacons

configuring, [12.2.2](monitor.md)

SERVICE\_TIME

service-level goal, [6.2.6](config_cw.md)

services

and FAN, [6.1.1.1](config_cw.md)

automatic relocation, [13.2.3.2](outage.md)

definition of, [6.1.1.1](config_cw.md)

making highly available, [6.2.3](config_cw.md)

Oracle RAC application failover, [13.2.4](outage.md)

Oracle RAC application workloads, [6.2.5](config_cw.md)

relocation after application failover, [13.2.4](outage.md)

tools for administration, [6.2.5](config_cw.md)

SGA\_TARGET initialization parameter, [5.1.9](config_db.md)

shared server

configuring Oracle Database, [11.5](config_fcf.md)

site failover

network routes, [13.2.1.3](outage.md)

SMON process

in a surviving instance, [7.1.1](config_rac.md)

sort operations

improving, [5.2.8](config_db.md)

space management, [5.2.7](config_db.md)

space usage

minimizing, [8.3](config_backuprec.md)

SQL Access Advisor, [5.2.3](config_db.md)

SQL Apply, [14.2.6.2](schedule_outage.md)

SQL Tuning Advisor, [5.2.3](config_db.md)

SRVCTL

Oracle Restart, [4.2.2](config_storage.md)

standby databases

configuring multiple, [9.3.9](config_dg.md)

creating, [9.3.2](config_dg.md)

restoring, [13.3.2](outage.md)

standby redo log files

determining number of, [9.3.6](config_dg.md)

standby-first patch apply (Data Guard), [14.2.3](schedule_outage.md)

STATISTICS\_LEVEL initialization parameter, [9.7](config_dg.md)

Statspack

storage

mirroring to RAID, [7.3.4](config_rac.md)

storage appliance, [8.6.2](config_backuprec.md)

Storage Area Network (SAN), [9.3.8.6](config_dg.md)

storage arrays

mirroring across, [4.3.2.2](config_storage.md)

multiple disk failures in, [13.2.5.4](outage.md)

storage grid

through clustered Oracle ASM, [4.2.1](config_storage.md)

storage subsystems, [4](config_storage.md)

configuring Oracle ASM, [4.2](config_storage.md)

configuring redundancy, [4.3.2](config_storage.md)

performance requirements, [4.1](config_storage.md)

stripe and mirror everything (SAME), [4.2](config_storage.md)

Support Workbench, [12.2.2](monitor.md)

switchovers

configuring real-time apply, [9.4.1](config_dg.md)

described, [14.2.1.1](schedule_outage.md)

in Oracle RAC, [9.4.1](config_dg.md)

reducing archiver (ARCn) processes, [9.4.1](config_dg.md)

See Also Data Guard

setting the LOG\_FILE\_NAME\_CONVERT initialization parameter, [9.4.1](config_dg.md)

to a logical standby database, [14.2.1.3](schedule_outage.md)

to a physical standby database, [14.2.1.3](schedule_outage.md)

SYSASM role

Oracle ASM Authentication, [4.5.1](config_storage.md)

system failure

recovery, [5.1.5](config_db.md)

system maintenance, [14.2.11](schedule_outage.md)

system resources

assessing, [9.3.8.7](config_dg.md)

SYSTEM tablespace

moving the contents of, [14.2.7.8](schedule_outage.md)

---

## T

table inconsistencies, [13.2.7.1](outage.md)

tablespace point-in-time recovery (TSPITR), [13.2.7.4](outage.md)

tablespaces

locally managed, [5.2.6](config_db.md)

resolving inconsistencies, [13.2.7.4](outage.md)

temporary, [5.2.8](config_db.md), [5.2.8](config_db.md)

targets

in Enterprise Manager, [12.2](monitor.md)

monitoring, [12.2](monitor.md)

TCP Nagle algorithm

disabling, [9.3.7.2](config_dg.md)

TCP.NODELAY sqlnet.ora parameter, [9.3.7.2](config_dg.md)

temporary tablespaces, [5.2.8](config_db.md), [5.2.8](config_db.md)

THROUGHPUT

service-level goal, [6.2.6](config_cw.md)

transaction recovery

determining how many processes are used, [7.1.2](config_rac.md)

transient logical standby database

rolling upgrade, [14.2.6.2.2](schedule_outage.md)

Transport Lag

event in Enterprise Manager, [12.2.4](monitor.md)

transportable database, [14.2.7.5](schedule_outage.md)

transportable tablespaces

database upgrades, [14.2.6.4](schedule_outage.md)

platform migration, [14.2.7.8](schedule_outage.md)

---

## U

undo retention

tuning, [5.2.5](config_db.md)

undo space

managing, [5.2.5](config_db.md)

UNDO\_MANAGEMENT initialization parameter, [8.2.7](config_backuprec.md)

automatic undo management, [5.2.5](config_db.md)

UNDO\_RETENTION initialization parameter, [8.2.7](config_backuprec.md)

automatic undo management, [5.2.5](config_db.md)

UNDO\_TABLESPACE initialization parameter

automatic undo management, [5.2.5](config_db.md)

unscheduled outages

Data Guard switchover, [14.2.1.3](schedule_outage.md)

described, [13.1](outage.md)

Oracle RAC recovery, [13.2.3](outage.md)

recovery from, [13.1.1](outage.md), [13.2](outage.md)

types, [13.1](outage.md)

See Also scheduled outages

unused block compression, [8.1.3](config_backuprec.md)

upgrades

application, [14.2.9](schedule_outage.md)

applying interim patches, [14.2.2](schedule_outage.md)

best practices, [14.2.4.1](schedule_outage.md)

Database Upgrade Assistant (DBUA), [14.2.6.1](schedule_outage.md)

methods, [14.2.6](schedule_outage.md)

online patching, [14.2.2](schedule_outage.md)

Oracle RAC rolling

best practices, [14.2.4.2](schedule_outage.md)

USABLE\_FILE\_MB column

on the V$ASM\_DISKGROUP view, [4.3.2.2](config_storage.md)

user error

flashback technology, [13.2.7](outage.md)

---

## V

V$ASM\_DISK view, [9.3.8.7](config_dg.md)

V$ASM\_DISK\_IOSTAT view

checking disk group imbalance, [4.5.5](config_storage.md)

V$ASM\_DISKGROUP view

REQUIRED\_MIRROR\_FREE\_MB column, [4.3.2.2](config_storage.md)

USABLE\_FILE\_MB column, [4.3.2.2](config_storage.md)

V$ASM\_OPERATION view

monitoring rebalance operations, [14.2.5.2.2](schedule_outage.md)

V$EVENT\_HISTOGRAM view, [9.3.8.5](config_dg.md)

V$INSTANCE\_RECOVERY view

tuning recovery processes, [5.1.10](config_db.md)

V$IOSTAT\_FILE view

asynchronous I/O, [5.1.7](config_db.md)

V$OSSTAT view, [9.3.8.7](config_dg.md), [9.7](config_dg.md)

V$SESSION\_WAIT view, [9.3.8.5](config_dg.md)

V$SYSMETRIC\_HISTORY view, [9.7](config_dg.md)

V$SYSMETRIC\_SUMMARY view, [9.7](config_dg.md)

V$SYSTEM\_EVENT view, [9.3.8.5](config_dg.md), [9.3.8.7](config_dg.md)

VALID\_FOR attribute, [9.3.5](config_dg.md)

VALIDATE option

on the RMAN BACKUP command, [9.3.8.3](config_dg.md)

validation

checksums during RMAN backup, [5.1.6.1](config_db.md)

verifying the interconnect subnet, [6.2.9](config_cw.md)

VIP address

Virtual Internet Protocol (VIP) Address

volume manager

Oracle ASM, [7.3.4](config_rac.md)

voting disk (Oracle RAC)

---

## W

wait events

websites

workloads

---

## Z

ZFS storage appliance, [8.6.2](config_backuprec.md)