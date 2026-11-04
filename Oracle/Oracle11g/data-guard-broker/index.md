---
title: Index
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/index.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

A B C D E F H I L M N O P Q R S T U V W

---

## A

Add Standby Database wizard

adding

ALTER SYSTEM statement

altering

AlternateLocation property, [8.3.1](dbpropref.md)

application integration, [1.2](concepts.md)

apply errors

managing, [4.5.5](dbresource.md)

apply instance, [4.5.7](dbresource.md)

failover, [4.5.7](dbresource.md)

PreferredApplyInstance property, [4.5.7.1](dbresource.md)

selecting, [4.5.7.1](dbresource.md)

ApplyInstanceTimeout property, [4.5.7.2](dbresource.md), [8.3.2](dbpropref.md)

ApplyLagThreshold property, [8.3.3](dbpropref.md), [8.3.3](dbpropref.md)

ApplyParallel property, [4.5.2](dbresource.md), [8.3.4](dbpropref.md)

architecture

Data Guard broker, [1.4](concepts.md)

ARCHIVE\_LAG\_TARGET initialization parameter

setting in a broker configuration, [8.3.5](dbpropref.md)

archived redo logs

destination and configuration parameters, [3.1](configure.md)

in a Data Guard configuration, [3.1](configure.md)

primary database setup, [2.2](install.md)

ArchiveLagTarget property, [8.3.5](dbpropref.md)

ASYNC redo transport service, [4.4.2](dbresource.md)

Automatic Storage Management (ASM)

creating a standby database that uses, [2.2](install.md)

---

## B

background processes

DMON, [1.6.1](concepts.md)

banners

suppressing from DGMGRL command-line interface output, [7.1.1](dgmgrl.md)

before you perform a switchover, [5.3.1](sofo.md)

before you use DGMGRL, [6.1](cli.md)

benefits

Data Guard broker, [1.2](concepts.md)

high availability, [1.2](concepts.md)

scalability, [1.2](concepts.md)

with Oracle Real Application Clusters, [1.2](concepts.md)

binary configuration file, [1.6.2](concepts.md)

Binding property, [8.3.6](dbpropref.md)

broker

components, [1.4](concepts.md)

configuration, [1.1.1](concepts.md)

Data Guard configuration file, [1.6.2](concepts.md)

drc\* log files, [9.1](troubleshooting.md)

installation, [2.2](install.md)

introduction, [1.1.2](concepts.md)

managing databases, [4.1](dbresource.md)

user interfaces, [1.5](concepts.md)

broker configurations

benefits, [1.2](concepts.md)

changing roles, [3.4](configure.md)

components, [3.1](configure.md)

creating, [6.2](cli.md), [6.2](cli.md), [7.2](dgmgrl.md)

Data Guard configuration file, [1.6.1](concepts.md)

database objects, [1.3](concepts.md)

database profiles, [1.3](concepts.md)

disabling databases, [3.5](configure.md), [7.2](dgmgrl.md)

effects of removing metadata from, [7.2](dgmgrl.md)

enabling, [6.4](cli.md), [7.2](dgmgrl.md)

enabling databases, [3.4](configure.md), [3.5](configure.md), [6.4](cli.md), [7.2](dgmgrl.md)

enabling fast-start failover, [7.2](dgmgrl.md)

health, [1.6.1](concepts.md), [3.6](configure.md)

instance objects, [1.3](concepts.md)

life cycle, [3.4](configure.md)

management, [1.3](concepts.md), [1.5.1](concepts.md), [1.5.2](concepts.md), [1.6.2](concepts.md)

monitoring, [6.12](cli.md)

objects, [1.3](concepts.md)

Oracle Net Services configuration, [1.2](concepts.md), [1.5.1](concepts.md)

overview, [3.1](configure.md)

properties, [4.3](dbresource.md)

protection modes, [7.2](dgmgrl.md)

setting protection mode, [4.6.1](dbresource.md)

status modes, [3.6](configure.md)

supported, [1.3](concepts.md), [3.1](configure.md), [3.1](configure.md)

bystander standby databases, [5.3](sofo.md)

reintegrating into configuration, [5.4.2.1](sofo.md)

BystandersFollowRoleChange property, [8.1.1](dbpropref.md)

---

## C

CFS

*See* cluster file system

changed features, [A](deprecated_appx.md)

changing

properties

databases in a broker configuration, [3.4](configure.md), [4.3.2](dbresource.md)

roles

within the broker configuration, [3.4](configure.md)

states

databases in a broker configuration, [4.2.1](dbresource.md)

of databases in a broker configuration, [6.7](cli.md)

*See also* editing

cluster file system (CFS)

broker configuration files, [3.2.2.1](configure.md)

command prompts

suppressing from DGMGRL command-line interface output, [7.1.1](dgmgrl.md)

command-line interface

*See* Data Guard command-line interface (DGMGRL)

CommunicationTimeout property, [8.1.2](dbpropref.md)

COMPATIBLE initialization parameter

requirements for setting, [2.2](install.md)

complete failover, [5.4.1](sofo.md), [7.2](dgmgrl.md)

components

broker, [1.4](concepts.md)

Data Guard configuration, [3.1](configure.md)

configurable properties, [4.3](dbresource.md)

AlternateLocation, [8.3.1](dbpropref.md)

ApplyInstanceTimeout, [8.3.2](dbpropref.md)

ApplyLagThreshold, [8.3.3](dbpropref.md), [8.3.3](dbpropref.md)

ApplyParallel, [8.3.4](dbpropref.md)

ArchiveLagTarget, [8.3.5](dbpropref.md)

Binding, [8.3.6](dbpropref.md)

database, [4.3.2](dbresource.md), [4.3.2](dbresource.md), [8.3](dbpropref.md)

DbFileNameConvert, [8.3.7](dbpropref.md)

DelayMins, [8.3.8](dbpropref.md)

DGConnectIdentifier, [8.3.9](dbpropref.md)

FastStartFailoverTarget, [8.3.10](dbpropref.md)

LogArchiveFormat, [8.3.11](dbpropref.md)

LogArchiveMaxProcesses, [8.3.12](dbpropref.md)

LogArchiveMinSucceedDest, [8.3.13](dbpropref.md)

LogArchiveTrace, [8.3.14](dbpropref.md)

LogFileNameConvert, [8.3.15](dbpropref.md)

LogShipping, [8.3.16](dbpropref.md)

LogXptMode, [8.3.17](dbpropref.md)

LsbyASkipCfgPr, [8.3.18](dbpropref.md)

LsbyASkipErrorCfgPr, [8.3.19](dbpropref.md)

LsbyASkipTxnCfgPr, [8.3.20](dbpropref.md)

LsbyDSkipCfgPr, [8.3.21](dbpropref.md)

LsbyDSkipErrorCfgPr, [8.3.22](dbpropref.md)

LsbyDSkipTxnCfgPr, [8.3.23](dbpropref.md)

LsbyMaxEventsRecorded, [8.3.24](dbpropref.md)

LsbyMaxServers, [8.3.26](dbpropref.md)

LsbyMaxSga, [8.3.25](dbpropref.md)

LsbyPreserveCommitOrder, [8.3.27](dbpropref.md)

LsbyRecordAppliedDdl, [8.3.28](dbpropref.md)

LsbyRecordSkipDdl, [8.3.29](dbpropref.md)

LsbyRecordSkipErrors, [8.3.30](dbpropref.md)

managing redo transport services, [4.4](dbresource.md)

MaxConnections, [8.3.31](dbpropref.md)

MaxFailure, [8.3.32](dbpropref.md)

NetTimeout, [8.3.33](dbpropref.md)

PreferredApplyInstance, [8.3.35](dbpropref.md)

RedoCompression, [8.3.36](dbpropref.md)

ReopenSecs, [8.3.37](dbpropref.md)

SidName, [8.3.38](dbpropref.md)

StandbyArchiveLocation, [8.3.39](dbpropref.md)

StandbyFileManagement, [8.3.40](dbpropref.md)

StaticConnectIdentifier, [8.3.41](dbpropref.md)

TransportDisconnectedThreshold, [8.3.42](dbpropref.md), [8.3.42](dbpropref.md)

TransportLagThreshold, [8.3.43](dbpropref.md), [8.3.43](dbpropref.md)

configuration files

fast-start failover configuration (fsfo.dat) file, [5.5.7.6](sofo.md)

*See* Also Data Guard configuration file

configuration properties

BystandersFollowRoleChange, [8.1.1](dbpropref.md)

CommunicationTimeout, [8.1.2](dbpropref.md)

ExternalDestination1, [8.1.3](dbpropref.md)

ExternalDestination2, [8.1.4](dbpropref.md)

FastStartFailoverAutoReinstate, [8.1.5](dbpropref.md)

FastStartFailoverLagLimit, [8.1.6](dbpropref.md)

FastStartFailoverPmyShutdown, [8.1.7](dbpropref.md)

FastStartFailoverThreshold, [8.1.8](dbpropref.md)

ObserverOverride, [8.1.9](dbpropref.md), [8.1.9](dbpropref.md)

ObserverReconnect, [8.1.10](dbpropref.md), [8.1.10](dbpropref.md)

OperationTimeout, [8.1.11](dbpropref.md)

PrimaryLostWriteAction, [8.1.12](dbpropref.md), [8.1.12](dbpropref.md)

TraceLevel, [8.1.13](dbpropref.md)

CONNECT command, [6.2](cli.md), [7.2](dgmgrl.md)

connecting

privileges required for Data Guard broker configurations, [7.1.3](dgmgrl.md)

starting the observer, [6.6](cli.md)

to the primary database, [6.2](cli.md)

controlling

available SGA memory, [4.5.3](dbresource.md)

transaction commit order, [4.5.3](dbresource.md)

CREATE CONFIGURATION command, [6.2](cli.md), [7.2](dgmgrl.md)

creating

a broker configuration, [6.2](cli.md), [6.2](cli.md), [6.2](cli.md), [7.2](dgmgrl.md)

with the Add Standby Database wizard, [3.4](configure.md)

a standby database, [3.4](configure.md)

---

## D

Data Guard

troubleshooting, [9](troubleshooting.md)

Data Guard broker

changed features, [A](deprecated_appx.md)

deprecated features, [A](deprecated_appx.md)

*See* Also broker

Data Guard command-line interface

commands

ENABLE FAST\_START FAILOVER, [7.2](dgmgrl.md)

SET STATE, [4.5.7.1](dbresource.md)

DG\_BROKER\_START initialization parameter, [2.2](install.md)

enabling a database, [6.4](cli.md)

introduction, [1.1.2](concepts.md), [1.5.2](concepts.md)

Data Guard command-line interface (DGMGRL)

banners from output, [7.1.1](dgmgrl.md)

commands

CONNECT, [7.2](dgmgrl.md)

CREATE CONFIGURATION, [7.2](dgmgrl.md)

DISABLE CONFIGURATION, [7.2](dgmgrl.md)

DISABLE DATABASE, [7.2](dgmgrl.md)

DISABLE FAST\_START FAILOVER, [5.5.5](sofo.md), [7.2](dgmgrl.md)

DISABLE FAST\_START FAILOVER CONDITION, [7.2](dgmgrl.md)

EDIT CONFIGURATION (property), [7.2](dgmgrl.md)

EDIT CONFIGURATION (protection mode), [7.2](dgmgrl.md)

EDIT DATABASE (property), [7.2](dgmgrl.md)

EDIT DATABASE (rename), [7.2](dgmgrl.md)

EDIT DATABASE (state), [7.2](dgmgrl.md)

EDIT INSTANCE (AUTO PFILE), [7.2](dgmgrl.md)

EDIT INSTANCE (property), [7.2](dgmgrl.md)

ENABLE CONFIGURATION, [7.2](dgmgrl.md)

ENABLE DATABASE, [7.2](dgmgrl.md)

ENABLE FAST\_START FAILOVER CONDITION, [7.2](dgmgrl.md)

EXIT, [7.2](dgmgrl.md)

FAILOVER, [6.9](cli.md)

HELP, [7.2](dgmgrl.md)

QUIT, [7.2](dgmgrl.md)

REMOVE CONFIGURATION, [7.2](dgmgrl.md)

REMOVE DATABASE, [7.2](dgmgrl.md)

REMOVE INSTANCE, [7.2](dgmgrl.md)

SHOW CONFIGURATION, [7.2](dgmgrl.md)

SHOW DATABASE, [7.2](dgmgrl.md)

SHOW FAST\_START FAILOVER, [7.2](dgmgrl.md)

SHOW INSTANCE, [7.2](dgmgrl.md)

SHUTDOWN, [7.2](dgmgrl.md)

STARTUP, [7.2](dgmgrl.md)

SWITCHOVER, [6.8](cli.md), [7.2](dgmgrl.md)

creating a configuration, [6.2](cli.md)

DG\_BROKER\_START initialization parameter, [7.1.3](dgmgrl.md)

enabling the configuration, [6.4](cli.md)

FSFO.DAT file creation, [7.2](dgmgrl.md)

monitoring broker configurations, [6.12](cli.md)

performing routine management tasks, [6.7](cli.md)

prerequisites, [6.1](cli.md)

setting critical database properties, [6.3](cli.md)

setting up standby redo log files, [4.6.1](dbresource.md)

single command mode, [7.1.1](dgmgrl.md)

starting, [6.2](cli.md), [7.1](dgmgrl.md)

stopping, [7.2](dgmgrl.md)

string values, [7.1.3](dgmgrl.md)

summary of commands, [7.1.2](dgmgrl.md)

suppressing command prompts, [7.1.1](dgmgrl.md)

Data Guard configuration file

for an Oracle RAC database, [3.2.2](configure.md)

in a CFS area, [3.2.2.1](configure.md)

inconsistent values from server parameter file, [8.2.2](dbpropref.md)

on a raw device, [3.2.2.3](configure.md)

relationship to DMON process, [1.6.1](concepts.md)

renaming, [1.6.2](concepts.md)

setting up, [3.2](configure.md)

Data Guard configurations

automated creation of, [1.2](concepts.md)

background, [3.1](configure.md)

supported, [3.1](configure.md)

Data Guard monitor (DMON), [1.6](concepts.md)

interaction with the Oracle database, [1.6.1](concepts.md)

maintaining configuration data, [1.6.2](concepts.md)

managing objects, [3.1](configure.md), [3.4](configure.md), [6.4](cli.md)

Oracle database background processes, [1.6.1](concepts.md)

overview, [1.6.1](concepts.md)

removing objects, [6.7.3](cli.md)

starting with the DG\_BROKER\_START parameter, [3.3](configure.md)

two-way network communication, [1.6.1](concepts.md)

data protection modes

*See* protection modes

database resources

monitoring, [1.2](concepts.md)

databases

changing the state of, [6.7](cli.md)

connecting to, [6.2](cli.md)

creating and adding to a broker configuration, [1.5.1](concepts.md)

dependencies, [4.2](dbresource.md)

disabling management of, [7.2](dgmgrl.md)

during

fast-start failover, [5.5](sofo.md)

manual failover, [5.4](sofo.md)

switchover, [5.3](sofo.md)

enabling, [6.4](cli.md)

health, [4.9](dbresource.md)

installation for broker management, [2.2](install.md)

monitorable database properties, [4.3.1](dbresource.md), [8.2](dbpropref.md)

network setup, [1.6.1](concepts.md), [2.2](install.md)

objects, [1.3](concepts.md)

definition, [1.3](concepts.md)

in a broker configuration, [1.3](concepts.md)

prerequisites for broker configurations, [2.2](install.md)

properties, [1.5.1](concepts.md), [4.3.2](dbresource.md), [8.3](dbpropref.md)

property management, [1.6.3](concepts.md)

reenabling after a role transition, [5.4.3](sofo.md)

removing

from a broker configuration, [6.7.3](cli.md)

restarting

after fast-start failover, [5.5.9](sofo.md)

shutting down

effect on fast-start failover, [5.5.2.1](sofo.md), [5.5.2.3](sofo.md), [5.5.9](sofo.md)

states, [4.2](dbresource.md)

dependencies, [4.2](dbresource.md)

transitions, [4.2.1](dbresource.md)

status, [4.9](dbresource.md)

DB\_FILE\_NAME\_CONVERT initialization parameter

initialization parameters

setting DB\_FILE\_NAME\_CONVERT in a broker configuration, [8.3.7](dbpropref.md)

DBA\_LOGSTDBY\_EVENTS table

managing, [4.5.6](dbresource.md)

DbFileNameConvert property, [8.3.7](dbpropref.md)

delaying

application of redo data with DelayMins property, [4.5.1](dbresource.md)

DelayMins property, [8.3.8](dbpropref.md)

delaying log apply services, [4.5.1](dbresource.md)

deprecated features, [A](deprecated_appx.md)

destinations

archived redo log file parameters, [3.1](configure.md)

viewing the LogXptStatus property, [8.2.3](dbpropref.md)

DG\_BROKER\_CONFIG\_FILEn file, [1.6.2](concepts.md), [3.2.2](configure.md)

in a CFS area, [3.2.2.1](configure.md)

on a raw device, [3.2.2.3](configure.md)

DG\_BROKER\_START initialization parameter, [2.2](install.md), [6.1](cli.md), [7.1.3](dgmgrl.md)

DGConnectIdentifier property, [8.3.9](dbpropref.md)

DGMGRL

reinstating a database, [5.4.3.1](sofo.md)

DGMGRL commands

FAILOVER, [7.2](dgmgrl.md)

SWITCHOVER, [7.2](dgmgrl.md)

diagnostic information

sources, [9.1](troubleshooting.md)

DISABLE CONFIGURATION command, [7.2](dgmgrl.md)

example, [6.7.2.1](cli.md)

DISABLE DATABASE command, [7.2](dgmgrl.md)

example, [6.7.2.2](cli.md)

DISABLE FAST\_START FAILOVER command, [5.5.5](sofo.md), [7.2](dgmgrl.md)

DISABLE FAST\_START FAILOVER CONDITION command, [7.2](dgmgrl.md)

disabling

broker configuration, [6.7.2](cli.md), [7.2](dgmgrl.md)

broker management of standby database, [7.2](dgmgrl.md)

databases, [3.5](configure.md), [6.7.2.1](cli.md), [6.7.2.2](cli.md)

fast-start failover, [5.5.5](sofo.md), [7.2](dgmgrl.md)

on a standby database, [5.5.5](sofo.md)

*See also* each DISABLE command

disaster protection

benefits, [1.2](concepts.md)

displaying

configuration information, [7.2](dgmgrl.md)

help for DGMGRL commands, [7.2](dgmgrl.md)

properties, [4.3](dbresource.md)

distributed management framework, [1.1.2](concepts.md)

DMON

*See* Data Guard monitor (DMON)

downgrading

Data Guard, [B.4](upgrade_appx.md)

Oracle Enterprise Manager, [B.4](upgrade_appx.md)

protection mode, [4.6.2.1](dbresource.md)

drc\* log files

broker diagnostic information, [9.1](troubleshooting.md)

during reinstatement, [5.5.4.1](sofo.md)

recording failed reinstatement, [5.5.8.3](sofo.md)

---

## E

EDIT CONFIGURATION (Property) command, [7.2](dgmgrl.md)

EDIT CONFIGURATION (protection mode) command, [7.2](dgmgrl.md)

EDIT DATABASE (property) command, [7.2](dgmgrl.md)

example, [6.7.1.1](cli.md)

EDIT DATABASE (rename) command, [7.2](dgmgrl.md)

EDIT DATABASE (state) command, [7.2](dgmgrl.md)

example, [6.7.1.2](cli.md)

EDIT INSTANCE (AUTO PFILE) command, [7.2](dgmgrl.md)

EDIT INSTANCE (property) command, [7.2](dgmgrl.md)

editing

configurable properties, [7.2](dgmgrl.md)

database instance, [7.2](dgmgrl.md), [7.2](dgmgrl.md)

database name, [7.2](dgmgrl.md)

database properties, [7.2](dgmgrl.md)

database state, [7.2](dgmgrl.md)

protection modes, [7.2](dgmgrl.md)

effect of switchovers on, [5.3.3](sofo.md)

e-mail

reporting events, [1.5.1](concepts.md)

ENABLE CONFIGURATION command, [6.4](cli.md), [7.2](dgmgrl.md)

ENABLE DATABASE command, [7.2](dgmgrl.md)

ENABLE FAST\_START FAILOVER command, [7.2](dgmgrl.md)

ENABLE FAST\_START FAILOVER CONDITION command, [7.2](dgmgrl.md)

enabling

broker configuration, [3.4](configure.md), [6.4](cli.md), [6.4](cli.md), [6.4](cli.md)

databases in a broker configuration, [3.5](configure.md)

fast-start failover, [5.5.1](sofo.md), [5.5.2](sofo.md)

*See also* each ENABLE command

Enterprise Edition database

installation, [2.1](install.md)

Enterprise Manager

Fast-Start Failover wizard

disabling fast-start failover, [5.5.5](sofo.md)

wizards

automate standby database creation, [1.1.2](concepts.md)

error messages

ORA-16795, [5.4.3](sofo.md), [5.4.3](sofo.md)

error status, [3.6](configure.md)

events

managing

in a logical standby database, [4.5.6](dbresource.md)

monitoring with Oracle Enterprise Manager, [1.1.2](concepts.md)

Oracle Enterprise Manager, [1.2](concepts.md)

reporting, [1.5.1](concepts.md)

responding to, [1.2](concepts.md)

EXIT command, [7.2](dgmgrl.md)

*See also* QUIT command

ExternalDestination1 property, [8.1.3](dbpropref.md)

ExternalDestination2 property, [8.1.4](dbpropref.md)

---

## F

failover

failing over to a standby database, [7.2](dgmgrl.md)

Oracle Enterprise Manager, [1.5.1](concepts.md)

FAILOVER command, [6.9](cli.md), [7.2](dgmgrl.md)

failovers

and FastStartFailoverTarget property, [6.6](cli.md)

benefits, [1.2](concepts.md)

broker tasks, [5.4.2.1](sofo.md)

choosing a target standby database, [5.2](sofo.md)

complete, [5.4.2.1](sofo.md)

defined, [5.1](sofo.md)

fast-start failover, [5.5.2.2](sofo.md)

effect on data protection mode, [5.5.1](sofo.md)

V$DATABASE, [5.5.4.1](sofo.md)

immediate, [5.4.2.2](sofo.md)

managing, [5](sofo.md)

fast-start, [5.5](sofo.md)

manual, [5.4](sofo.md)

manual

complete option, [5.4.1](sofo.md)

effect on data protection mode, [5.4.2](sofo.md)

immediate option, [5.4.1](sofo.md)

reenabling disabled databases after, [5.4.2.1](sofo.md)

starting manually, [5.4.2](sofo.md)

using DGMGRL, [6.9](cli.md)

failures

observer, [5.5.7.3](sofo.md)

fast-start failover, [5.1](sofo.md)

configuration information in the fsfo.dat file, [5.5.7.6](sofo.md)

defined, [5.5](sofo.md)

DGMGRL client as the observer, [1.5.2](concepts.md)

disabling, [5.5.5](sofo.md), [5.5.5](sofo.md)

to perform manual failover, [5.5.5](sofo.md)

enabling, [5.5.2](sofo.md), [7.2](dgmgrl.md)

instance failures, [5.5.2.1](sofo.md)

monitoring by the observer, [5.5.2.1](sofo.md)

observer monitoring, [5.5.2.1](sofo.md)

observer overview, [5.5](sofo.md)

performing manual failovers when enabled, [5.5.2.4](sofo.md)

performing switchover when enabled, [5.5.2.4](sofo.md)

querying V$DATABASE, [5.5.2.2](sofo.md)

reinstating the former primary database, [5.5.8](sofo.md)

requirements, [5.5.1](sofo.md)

restarting databases after shut down, [5.5.9](sofo.md)

setting the FastStartFailoverTarget property, [5.5.2](sofo.md), [5.5.2](sofo.md), [6.6](cli.md)

setting the FastStartFailoverThreshold property, [5.5.2](sofo.md)

shutdown abort, [5.5.2.1](sofo.md), [5.5.2.3](sofo.md)

shutting down databases, [5.5.9](sofo.md)

to Oracle RAC database instances, [5.5.2.1](sofo.md)

unobserved, [5.5.7.3](sofo.md)

verifying the environment, [5.5.2](sofo.md)

viewing failover configuration statistics, [5.5.4.1](sofo.md)

FastStartFailoverAutoReinstate property, [8.1.5](dbpropref.md)

FastStartFailoverLagLimit property, [8.1.6](dbpropref.md)

FastStartFailoverPmyShutdown property, [8.1.7](dbpropref.md)

FastStartFailoverTarget property, [8.3.10](dbpropref.md)

setting, [5.5.2](sofo.md), [5.5.2](sofo.md), [6.6](cli.md)

FastStartFailoverThreshold property, [8.1.8](dbpropref.md)

setting, [5.5.2](sofo.md)

files

naming the server parameter file, [1.6.3](concepts.md)

Flashback Database

reinstating databases, [5.4.3.1](sofo.md)

use after failover, [5.4.2.1](sofo.md)

flashback logs

reinstating a failed primary database, [5.4.3.1](sofo.md)

FORCE option

disabling fast-start failover, [5.5.5](sofo.md), [7.2](dgmgrl.md)

performing a manual failover, [5.5.5](sofo.md)

FS\_FAILOVER\_OBSERVER\_HOST column

of V$DATABASE view, [5.5.7.2](sofo.md)

FS\_FAILOVER\_OBSERVER\_PRESENT column

of V$DATABASE view, [5.5.7.2](sofo.md)

FS\_FAILOVER\_STATUS column

of V$DATABASE view

failed reinstatement, [5.5.4.1](sofo.md)

FSFO.DAT file

overview, [5.5.7.6](sofo.md)

START OBSERVER command, [7.2](dgmgrl.md)

---

## H

health check, [1.2](concepts.md)

monitoring, [1.6.1](concepts.md), [1.6.1](concepts.md)

on primary database, [4.9](dbresource.md)

on standby database, [4.9](dbresource.md)

revealed by configuration status, [3.6](configure.md)

HELP command, [7.2](dgmgrl.md)

high availability

benefits, [1.2](concepts.md)

levels of data protection, [4.6](dbresource.md), [8.3.17](dbpropref.md)

LogXptMode property, [8.3.17](dbpropref.md)

restoring after fast-start failover, [5.5.8](sofo.md)

---

## I

immediate failover, [5.4.1](sofo.md), [7.2](dgmgrl.md)

InconsistentLogXptProps property, [8.2.1](dbpropref.md)

InconsistentProperties property, [8.2.2](dbpropref.md)

increased scalability

benefits, [1.2](concepts.md)

initialization parameters

COMPATIBLE, [2.2](install.md)

database configurable properties, [4.3.2](dbresource.md)

DG\_BROKER\_CONFIG\_FILEn, [3.2.2](configure.md)

DG\_BROKER\_START, [2.2](install.md), [6.1](cli.md)

dynamic, [4.3.2](dbresource.md)

inconsistent, [8.2.2](dbpropref.md)

LOG\_ARCHIVE\_DEST\_n, [4.4.5](dbresource.md)

static, [4.3.2](dbresource.md)

*See also* server parameter file,

installation

ARCHIVELOG mode setup, [2.2](install.md)

Data Guard, [2.1](install.md)

Oracle Enterprise Manager, [2.1](install.md)

Oracle Instant Client, [2.1](install.md), [7.2](dgmgrl.md)

prerequisites, [2.2](install.md)

instances

failures, [5.5.2.1](sofo.md)

objects

in a broker configuration, [1.3](concepts.md)

removing, [7.2](dgmgrl.md), [7.2](dgmgrl.md), [7.2](dgmgrl.md)

shutting down, [7.2](dgmgrl.md)

starting, [7.2](dgmgrl.md)

intended state

configuration health check, [3.6](configure.md)

invoking

the Data Guard command-line interface, [6.2](cli.md)

---

## L

life cycle of a broker configuration, [3.4](configure.md)

log apply services

and apply instance failover, [4.5.7](dbresource.md)

and parallel apply, [4.5.2](dbresource.md)

apply instance, [4.5.7](dbresource.md)

configuring, [1.5.1](concepts.md)

Data Guard configuration, [3.1](configure.md)

delayed application of redo data, [4.5.1](dbresource.md)

delaying, [8.3.8](dbpropref.md)

in an Oracle RAC database, [4.5.7](dbresource.md)

managing, [4.5](dbresource.md)

selecting the apply instance, [4.5.7.1](dbresource.md)

verifying, [1.2](concepts.md)

log files

broker, [5.5.8.3](sofo.md)

FSFO.DAT

creating, [7.2](dgmgrl.md)

LOG\_ARCHIVE\_DEST\_n initialization parameter

setting redo transport services, [4.4.5](dbresource.md)

setting the DELAY attribute, [8.3.8](dbpropref.md)

setting the ENABLE and DEFER attributes, [8.3.16](dbpropref.md)

setting the MANDATORY or OPTIONAL attributes, [8.3.6](dbpropref.md)

LOG\_ARCHIVE\_FORMAT initialization parameter, [8.3.11](dbpropref.md)

LOG\_ARCHIVE\_MAX\_PROCESSES initialization parameter, [8.3.12](dbpropref.md)

LOG\_ARCHIVE\_MIN\_SUCCEED initialization parameter, [8.3.13](dbpropref.md)

LOG\_ARCHIVE\_TRACE initialization parameter

setting LogArchiveTrace property, [8.3.14](dbpropref.md)

LOG\_FILE\_NAME\_CONVERT initialization parameter

setting LogFileNameConvert property, [8.3.15](dbpropref.md)

LogArchiveFormat property, [8.3.11](dbpropref.md)

LogArchiveMaxProcesses property, [8.3.12](dbpropref.md)

LogArchiveMinSucceedDest property, [8.3.13](dbpropref.md)

LogArchiveTrace property, [8.3.14](dbpropref.md)

LogFileNameConvert property, [8.3.15](dbpropref.md)

logical standby databases

and SQL Apply error handling, [4.5.5](dbresource.md)

and SQL Apply filters, [4.5.4](dbresource.md)

managing events, [4.5.6](dbresource.md)

SQL Apply, [4.5.3](dbresource.md)

state transitions, [4.2.1](dbresource.md)

switchover to the primary role, [5.3](sofo.md)

LogShipping property, [8.3.16](dbpropref.md)

LogXptMode property, [8.3.17](dbpropref.md)

LogXptStatus property, [8.2.3](dbpropref.md)

LsbyASkipCfgPr property, [8.3.18](dbpropref.md)

LsbyASkipErrorCfgPr property, [4.5.5](dbresource.md), [8.3.19](dbpropref.md)

LsbyASkipTxnCfgPr property, [8.3.20](dbpropref.md)

LsbyDSkipCfgPr property, [8.3.21](dbpropref.md)

LsbyDSkipErrorCfgPr property, [4.5.5](dbresource.md), [8.3.22](dbpropref.md)

LsbyDSkipTxnCfgPr property, [8.3.23](dbpropref.md)

LsbyFailedTxnInfo property, [8.2.4](dbpropref.md)

LsbyMaxEventsRecorded property, [8.3.24](dbpropref.md)

LsbyMaxServers property, [8.3.26](dbpropref.md)

LsbyMaxSga property, [4.5.3](dbresource.md), [8.3.25](dbpropref.md)

LsbyParameters property, [8.2.5](dbpropref.md)

LsbyPreserveCommitOrder property, [4.5.3](dbresource.md), [8.3.27](dbpropref.md)

LsbyRecordAppliedDdl property, [8.3.28](dbpropref.md)

LsbyRecordSkipDdl property, [8.3.29](dbpropref.md)

LsbyRecordSkipErrors property, [8.3.30](dbpropref.md)

LsbySkipTable property, [8.2.6](dbpropref.md)

LsbySkipTxnTable property, [8.2.7](dbpropref.md)

---

## M

management

benefits, [1.2](concepts.md)

model, [1.3](concepts.md)

Oracle Enterprise Manager, [1.5.1](concepts.md)

managing

a broker configuration, [3](configure.md), [6](cli.md)

apply errors, [4.5.5](dbresource.md)

databases, [4](dbresource.md)

DBA\_LOGSTDBY\_EVENTS table, [4.5.6](dbresource.md)

events

in a logical standby database, [4.5.6](dbresource.md)

fast-start failover, [5.5](sofo.md)

local operations, [1.1.2](concepts.md)

log apply services, [4.5](dbresource.md)

manual failover, [5.4](sofo.md)

objects in a broker configuration, [1.3](concepts.md)

parallel apply in a physical standby database, [4.5.2](dbresource.md)

remote operations, [1.1.2](concepts.md)

roles, [5](sofo.md)

fast-start failover, [5.5](sofo.md)

manual failover, [5.4](sofo.md)

switchover, [5.3](sofo.md)

switchover, [5.3](sofo.md)

MANDATORY attribute

set with the Binding property, [8.3.6](dbpropref.md)

manual failover, [1.2](concepts.md), [5.1](sofo.md)

complete option, [5.4.1](sofo.md)

effect on protection modes, [4.6.2.3](dbresource.md)

immediate option, [5.4.1](sofo.md)

performing when fast-start failover is enabled, [5.5.2.4](sofo.md), [5.5.5](sofo.md)

starting, [5.4.2](sofo.md)

manual role changes

performing when fast-start failover is enabled, [5.5.2.4](sofo.md)

MaxConnections property, [8.3.31](dbpropref.md)

MaxFailure property, [8.3.32](dbpropref.md)

maximize availability, [1.2](concepts.md), [3.4](configure.md), [8.3.17](dbpropref.md)

maximize data protection, [1.2](concepts.md), [3.4](configure.md), [8.3.17](dbpropref.md)

maximize performance, [1.2](concepts.md), [3.4](configure.md), [8.3.17](dbpropref.md)

maximum availability

data protection mode, [4.6.1](dbresource.md)

maximum performance

data protection mode, [4.6.1](dbresource.md)

maximum protection

data protection mode, [4.6.1](dbresource.md)

monitorable properties, [4.3](dbresource.md)

database, [4.3.1](dbresource.md)

InconsistentLogXptProps, [8.2.1](dbpropref.md)

InconsistentProperties, [8.2.2](dbpropref.md)

LogXptStatus, [8.2.3](dbpropref.md), [8.2.3](dbpropref.md)

LsbyFailedTxnInfo, [8.2.4](dbpropref.md), [8.2.4](dbpropref.md)

LsbyParameters, [8.2.5](dbpropref.md)

LsbySkipTable, [8.2.6](dbpropref.md)

LsbySkipTxnTable, [8.2.7](dbpropref.md)

RecvQEntries, [8.2.8](dbpropref.md)

SendQEntries, [8.2.9](dbpropref.md)

TopWaitEvents, [8.2.10](dbpropref.md)

monitoring

broker configurations, [1.6.1](concepts.md), [6](cli.md), [6.12](cli.md)

local and remote databases, [1.2](concepts.md)

observer

fast-start failover environment, [5.5.2.1](sofo.md)

Oracle Enterprise Manager performance page, [3.4](configure.md)

through the command-line interface, [1.5.2](concepts.md)

---

## N

NetTimeout property, [8.3.33](dbpropref.md)

networks

Data Guard configuration, [3.1](configure.md)

setting up files, [2.2](install.md)

two-way communication, [1.6.1](concepts.md)

normal status, [3.6](configure.md)

---

## O

objects

broker configuration, [1.3](concepts.md), [3.1](configure.md)

disabling, [6.7.2](cli.md)

properties for databases, [1.6.3](concepts.md)

relationship, [1.3](concepts.md)

observer, [5.5](sofo.md)

and FastStartFailoverThreshold property, [5.5.2](sofo.md)

connecting to the configuration, [6.6](cli.md)

connection to the local computer, [5.5.7.2](sofo.md)

detecting

database shutdown, [5.5.2.1](sofo.md), [5.5.2.3](sofo.md)

instance failures, [5.5.2.1](sofo.md)

failures, [5.5.7.3](sofo.md)

finding host machine name, [5.5.7.2](sofo.md)

installing Oracle Instant Client kit, [2.1](install.md), [7.2](dgmgrl.md)

lost connection, [5.5.7.3](sofo.md)

maintaining fast-start failover configuration information, [5.5.7.6](sofo.md)

monitoring, [5.5.2.1](sofo.md), [5.5.2.1](sofo.md)

shutting down, [5.5.9](sofo.md)

using Oracle Wallet for connection credentials, [7.2](dgmgrl.md)

ObserverOverride property, [8.1.9](dbpropref.md), [8.1.9](dbpropref.md)

ObserverReconnect property, [8.1.10](dbpropref.md), [8.1.10](dbpropref.md)

operations

complete failover, [7.2](dgmgrl.md)

disable broker management

effect on protection modes, [4.6.2.4](dbresource.md)

downgrade

effect on protection modes, [4.6.2.1](dbresource.md)

effect on protection modes, [4.6.2](dbresource.md)

enable broker management

effect on protection modes, [4.6.2.4](dbresource.md)

failover, [6.9](cli.md)

immediate failover, [7.2](dgmgrl.md)

manual failover

effect on protection modes, [4.6.2.3](dbresource.md)

removing a database from the configuration

effect on protection modes, [4.6.2.5](dbresource.md)

OperationTimeout property, [8.1.11](dbpropref.md)

OPTIONAL attribute

set with the Binding property, [8.3.6](dbpropref.md)

ORA-16661 message

reinstating a database, [5.4.3](sofo.md), [5.4.3](sofo.md), [5.4.3.1](sofo.md)

ORA-16795 message

re-creating a database, [5.4.3](sofo.md)

Oracle Clusterware, [1.2](concepts.md)

and instances of an Oracle RAC database, [1.2](concepts.md)

integration with Data Guard broker, [1.2](concepts.md)

recover failed instances, [1.2](concepts.md)

Oracle Enterprise Manager, [1.5.1](concepts.md)

Add Standby Database wizard, [1.5.1](concepts.md)

database property pages, [1.5.1](concepts.md)

downgrading, [B.4](upgrade_appx.md)

event management system, [1.2](concepts.md)

integration, [1.5.1](concepts.md)

integration with the Data Guard monitor, [1.5.1](concepts.md)

introduction, [1.1.2](concepts.md), [1.4](concepts.md)

making Oracle Net Services configuration changes, [1.2](concepts.md), [1.5.1](concepts.md)

monitoring events, [1.1.2](concepts.md)

performance tools and graphs, [1.5.1](concepts.md)

setting up standby redo log files, [4.6.1](dbresource.md)

upgrading, [B.1](upgrade_appx.md)

wizards

creating standby databases, [1.5.1](concepts.md)

Oracle Instant Client

installing, [2.1](install.md), [7.2](dgmgrl.md)

Oracle Managed Files (OMF)

creating a standby database that uses, [2.2](install.md)

Oracle Net Services

configuration changes, [1.2](concepts.md), [1.5.1](concepts.md)

installation prerequisites, [2.2](install.md)

supported configuration, [3.1](configure.md)

two-way communication, [1.6.1](concepts.md)

Oracle Real Application Clusters

and log apply services, [4.5.7](dbresource.md)

and setting the apply instance, [4.5.7.1](dbresource.md)

availability of instances with Oracle Clusterware, [1.2](concepts.md)

benefits, [1.2](concepts.md)

fast-start failover, [5.5.2.1](sofo.md)

observer behavior in, [5.5.2.1](sofo.md)

observer connection to instances, [5.5.7.2](sofo.md)

Oracle Clusterware, [1.2](concepts.md)

Oracle Universal Installer

installing Oracle Instant Client, [2.1](install.md), [7.2](dgmgrl.md)

Oracle Wallet

starting the observer, [7.2](dgmgrl.md)

---

## P

parallel apply

and log apply services, [4.5.2](dbresource.md)

managing in a physical standby database, [4.5.2](dbresource.md)

performance

Oracle Enterprise Manager tools, [1.5.1](concepts.md)

physical standby databases

managing parallel apply, [4.5.2](dbresource.md)

state transitions, [4.2.1](dbresource.md)

switchover to the primary role, [5.3](sofo.md)

PreferredApplyInstance property, [4.5.7.1](dbresource.md), [8.3.35](dbpropref.md)

prerequisites

installation, [2.2](install.md)

switchover, [5.3.1](sofo.md)

primary database

ARCHIVELOG mode, [2.2](install.md)

configuration, [3.1](configure.md)

connecting to, [6.2](cli.md), [6.2](cli.md)

constructing a standby database, [3.4](configure.md), [6.1](cli.md)

Data Guard configuration, [3.1](configure.md)

during failover, [1.5.1](concepts.md)

during switchover, [5.3.3](sofo.md)

Flashback Database, [5.4.3.1](sofo.md)

health check, [4.9](dbresource.md)

preparing for switchover, [5.3.1](sofo.md)

reinstating after a fast-start failover, [5.5.8](sofo.md)

shutting down when fast-start failover is enabled, [5.5.9](sofo.md)

standby redo log files on, [4.6.1](dbresource.md)

state transitions, [4.2.1](dbresource.md)

switching over to the standby role, [7.2](dgmgrl.md)

PrimaryLostWriteAction property, [8.1.12](dbpropref.md), [8.1.12](dbpropref.md)

processes

DMON, [1.6.1](concepts.md)

Oracle database, [1.6.1](concepts.md)

properties, [4.3.2](dbresource.md)

AlternateLocation, [4.4.4](dbresource.md)

ApplyInstanceTimeout, [4.5.7.2](dbresource.md)

ApplyParallel, [4.5.2](dbresource.md)

configurable, [4.3](dbresource.md)

database, [4.3](dbresource.md)

DelayMins, [4.5.1](dbresource.md)

LsbyASkipErrorCfgPr, [4.5.5](dbresource.md)

LsbyDSkipErrorCfgPr, [4.5.5](dbresource.md)

LsbyMaxSga, [4.5.3](dbresource.md)

LsbyPreserveCommitOrder, [4.5.3](dbresource.md)

managing, [1.6.3](concepts.md)

monitorable, [4.3](dbresource.md)

PreferredApplyInstance, [4.5.7.1](dbresource.md)

setting, [3.4](configure.md), [6.3](cli.md)

in server parameter file, [1.6.3](concepts.md), [2.2](install.md)

StandbyArchiveLocation, [4.4.4](dbresource.md)

property pages

database, [1.5.1](concepts.md)

protection modes

after a failover, [4.6.2.3](dbresource.md), [5.4.2](sofo.md), [5.5.1](sofo.md)

benefits, [1.2](concepts.md)

configuration, [7.2](dgmgrl.md)

downgrading, [4.6.2.1](dbresource.md)

redo transport services setup, [8.3.17](dbpropref.md)

setting for a broker configuration, [4.6](dbresource.md)

updating, [3.4](configure.md)

upgrading, [4.6.2.1](dbresource.md)

---

## Q

QUIT command, [7.2](dgmgrl.md)

*See also* EXIT command

---

## R

raw devices

and broker configuration files, [3.2.2.3](configure.md)

sizing, [3.2.2.3](configure.md)

RecvQEntries property, [8.2.8](dbpropref.md)

Redo Apply, [3.1](configure.md), [5.3.3](sofo.md)

redo transport services

ASYNC mode, [4.4.2](dbresource.md), [8.3.17](dbpropref.md)

configuring, [1.5.1](concepts.md)

data protection modes, [8.3.17](dbpropref.md)

Data Guard configuration, [3.1](configure.md)

LogShipping property, [8.3.16](dbpropref.md)

managing, [4.4](dbresource.md)

SYNC mode, [4.4.2](dbresource.md), [8.3.17](dbpropref.md)

tuning, [4.4.5](dbresource.md)

turning off, [4.4.3](dbresource.md)

turning on, [4.4.3](dbresource.md)

verifying, [1.2](concepts.md)

RedoCompression property, [8.3.36](dbpropref.md)

reinstatement, [5.5.8](sofo.md)

failure logged in broker drc\* log files, [5.5.4.1](sofo.md)

Flashback Database requirement, [5.4.3.1](sofo.md)

flashback logs requirement, [5.4.3.1](sofo.md)

how to, [5.4.3.1](sofo.md)

logged in broker log files, [5.5.8.3](sofo.md)

ORA-16661 message, [5.4.3](sofo.md), [5.4.3](sofo.md), [5.4.3.1](sofo.md)

requires standby redo log files, [4.6.1](dbresource.md)

using DGMGRL, [5.4.3.1](sofo.md)

using Enterprise Manager, [5.4.3.1](sofo.md)

relationship

objects in a broker configuration, [1.3](concepts.md)

REMOVE CONFIGURATION command, [7.2](dgmgrl.md)

example, [6.7.3](cli.md)

REMOVE DATABASE command, [7.2](dgmgrl.md)

REMOVE INSTANCE command, [7.2](dgmgrl.md)

removing

a standby database, [4.6.2.5](dbresource.md)

*See* each REMOVE command

ReopenSecs property, [8.3.37](dbpropref.md)

requests

passing between sites, [1.6.1](concepts.md)

requirements

for enabling fast-start failover, [5.5.1](sofo.md)

restarting

databases

when fast-start failover is enabled, [5.5.9](sofo.md)

role transitions

changing, [3.4](configure.md)

managing, [5](sofo.md)

fast-start failover, [5.5](sofo.md)

manual failover, [5.4](sofo.md)

switchover, [5.3](sofo.md)

---

## S

scripts

using Data Guard command-line interface (DGMGRL), [7](dgmgrl.md)

selecting the apply instance, [4.5.7.1](dbresource.md)

SendQEntries property, [8.2.9](dbpropref.md)

server parameter file

broker property management, [1.6.3](concepts.md), [2.2](install.md)

filenames, [1.6.3](concepts.md)

inconsistent values from Data Guard configuration file, [8.2.2](dbpropref.md)

server-side software, [1.6](concepts.md)

SET STATE command

and setting the apply instance, [4.5.7.1](dbresource.md)

setting

configuration protection mode, [4.6.1](dbresource.md)

database properties, [6.3](cli.md)

log apply services, [4.4.4](dbresource.md)

redo transport services, [4.4.5](dbresource.md)

SGA memory

and SQL Apply, [4.5.3](dbresource.md)

SHOW CONFIGURATION command, [6.2](cli.md), [6.2](cli.md), [6.4](cli.md), [7.2](dgmgrl.md)

SHOW CONFIGURATION VERBOSE

example, [5.5.4](sofo.md)

SHOW DATABASE command, [7.2](dgmgrl.md)

SHOW DATABASE VERBOSE command

displaying properties, [4.3](dbresource.md)

SHOW FAST\_START FAILOVER command, [7.2](dgmgrl.md)

SHOW FAST-START FAILOVER command

example, [5.5.4](sofo.md)

SHOW INSTANCE command, [7.2](dgmgrl.md)

showing

*See* each SHOW command

shutdown

FS\_FAILOVER\_OBSERVER\_PRESENT view, [5.5.9](sofo.md)

shutdown abort, [5.5.2.1](sofo.md)

effect on fast-start failover, [5.5.2.3](sofo.md)

SHUTDOWN command, [7.2](dgmgrl.md)

shutting down an Oracle instance, [7.2](dgmgrl.md)

SidName property, [8.3.38](dbpropref.md)

single command mode

for Data Guard command-line interface, [7.1.1](dgmgrl.md)

SQL Apply, [3.1](configure.md)

and logical standby databases, [4.5.3](dbresource.md)

effect of switchovers on, [5.3.3](sofo.md)

error handling

and logical standby databases, [4.5.5](dbresource.md)

filters

and logical standby databases, [4.5.4](dbresource.md)

standby databases

choosing a target standby database, [5.2](sofo.md)

constructing from backups, [3.4](configure.md), [6.1](cli.md)

creating, [1.5.1](concepts.md)

if primary database uses ASM or OMF, [2.2](install.md)

Data Guard configuration, [3.1](configure.md)

health check, [4.9](dbresource.md)

not involved in a switchover, [5.3.3](sofo.md)

reenabling after failover, [5.4.2.1](sofo.md)

removing, [4.6.2.5](dbresource.md), [7.2](dgmgrl.md)

require standby redo log files, [4.6.1](dbresource.md)

shutting down when fast-start failover is enabled, [5.5.9](sofo.md)

specifying the location of archived redo logs, [4.4.4](dbresource.md)

switching over to the primary role, [7.2](dgmgrl.md)

standby redo log files

setting up, [4.6.1](dbresource.md)

setting up with DGMGRL, [4.6.1](dbresource.md)

StandbyArchiveLocation property, [8.3.39](dbpropref.md)

StandbyFileManagement property, [8.3.40](dbpropref.md)

START OBSERVER command

fast-start failover configuration file (fsfo.dat), [5.5.7.6](sofo.md)

starting

Data Guard command-line interface (DGMGRL), [6.2](cli.md), [7.1](dgmgrl.md)

Data Guard monitor (DMON), [3.3](configure.md)

manual failover, [5.4.2](sofo.md)

Oracle instance, [7.2](dgmgrl.md)

switchover, [5.3.2](sofo.md)

STARTUP command, [7.2](dgmgrl.md)

state transitions

effect on database states, [4.2.1](dbresource.md)

logical standby database, [4.2.1](dbresource.md)

physical standby database, [4.2.1](dbresource.md)

primary database, [4.2.1](dbresource.md)

states, [3.5](configure.md)

changing, [6.7](cli.md)

database, [4.2](dbresource.md)

database transitions, [4.2.1](dbresource.md)

logical standby database

APPLY-OFF, [4.2](dbresource.md)

APPLY-ON, [4.2](dbresource.md)

physical standby database

APPLY-OFF, [4.2](dbresource.md)

APPLY-ON, [4.2](dbresource.md)

primary database

TRANSPORT-OFF, [4.2](dbresource.md)

TRANSPORT-ON, [4.2](dbresource.md)

StaticConnectIdentifier property, [8.3.41](dbpropref.md)

status

configuration, [3.6](configure.md)

health check on primary database, [4.9](dbresource.md)

health check on standby database, [4.9](dbresource.md)

health of the database, [4.9](dbresource.md)

intended state of a configuration, [3.6](configure.md)

status messages

ORA-16661, [5.4.3](sofo.md), [5.4.3](sofo.md)

ORA-16795, [5.4.3](sofo.md)

string values

Data Guard command-line interface, [7.1.3](dgmgrl.md)

supported broker configuration, [1.3](concepts.md)

SWITCHOVER command, [6.8](cli.md), [7.2](dgmgrl.md)

switchovers

benefits, [1.2](concepts.md)

broker tasks, [5.3.3](sofo.md)

choosing a target standby database, [5.2](sofo.md)

DGMGRL SWITCHOVER command, [6.8](cli.md)

effect on

database startup, [7.2](dgmgrl.md)

primary database, [5.3.3](sofo.md)

protection modes, [4.6.2.2](dbresource.md)

standby databases not involved in the switchover, [5.3.3](sofo.md)

managing, [5](sofo.md), [5.3](sofo.md)

overview, [5.1](sofo.md)

Oracle Enterprise Manager, [1.5.1](concepts.md)

performing when fast-start failover is enabled, [5.5.2.4](sofo.md)

preparing the primary database, [5.3.1](sofo.md)

prerequisites, [5.3.1](sofo.md)

reenabling disabled standby databases, [5.4.3](sofo.md)

starting, [5.3.2](sofo.md)

transitioning

a logical standby database to the primary role, [5.3](sofo.md)

a physical standby database to the primary role, [5.3](sofo.md)

using the DGMGRL SWITCHOVER command, [7.2](dgmgrl.md)

SYNC redo transport mode, [4.4.2](dbresource.md)

SYSDBA privileges, [6.2](cli.md)

to connect to the database, [7.1.3](dgmgrl.md)

---

## T

target standby database

choosing, [5.2](sofo.md)

disabling fast-start failover on, [5.5.5](sofo.md)

setting with the FastStartFailoverTarget property, [5.5.2](sofo.md), [6.6](cli.md)

TopWaitEvents property, [8.2.10](dbpropref.md)

Tracelevel property, [8.1.13](dbpropref.md)

transaction commit order

controlling, [4.5.3](dbresource.md)

TransportDisconnectedThreshold property, [8.3.42](dbpropref.md), [8.3.42](dbpropref.md)

TransportLagThreshold property, [8.3.43](dbpropref.md), [8.3.43](dbpropref.md)

TRANSPORT-OFF state

LogShipping property setting, [8.3.16](dbpropref.md)

TRANSPORT-ON state

setting LogShipping property, [8.3.16](dbpropref.md)

troubleshooting

Data Guard, [9](troubleshooting.md)

diagnostics logged in broker drc\* log files, [9.1](troubleshooting.md)

tuning

redo transport services, [4.4.5](dbresource.md)

two-way communication channel, [1.6.1](concepts.md)

---

## U

unobserved configuration, [5.5.7.3](sofo.md)

updating configuration properties, [4.3](dbresource.md)

upgrading

Data Guard, [B.1](upgrade_appx.md), [B.2](upgrade_appx.md)

Oracle Enterprise Manager, [B.1](upgrade_appx.md)

protection mode, [4.6.2.1](dbresource.md)

user interfaces

overview, [1.5](concepts.md)

---

## V

V$DATABASE view

V$FS\_FAILOVER\_STATS view, [5.5.4.2](sofo.md)

verifying

fast-start failover environment, [5.5.2](sofo.md)

viewing

---

## W

warning status, [3.6](configure.md)

wizards