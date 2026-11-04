---
title: Index
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/index.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

A B C D E F G H I J L M N O P R S T U V W

---

## A

Advanced installation type, [2.4](racinstl.md)

architecture

archive logs

ASM

ASMSNMP, [1.4.2](chklist.md)

Automatic Diagnostic Repository, [Preface](whatsnew.md)

automatic undo management, [7.5](undrstnd.md)

---

## B

backups

block devices, [1.3.4](chklist.md)

supported for upgrades only, [1.3.4](chklist.md)

---

## C

candidate disks, [3.6](dbcacrea.md)

changing host names, [7.1](undrstnd.md)

cluster database

installed configuration, [7.4.1](undrstnd.md)

cluster file system

storage option for data files, [1.3.4](chklist.md)

Cluster Manager

ports, ranges and protocol, [F.3](ports.md)

Cluster Synchronization Services (CSS)

ports, ranges and protocol, [F.3](ports.md)

Cluster Verification Utility

checking the integrity of the Cluster Manager, [A.1.3](trouble.md)

DBCA database creation stage readiness check, [3.5](dbcacrea.md)

verifying readiness for database installation, [1.5](chklist.md)

CLUSTER\_DATABASE\_INSTANCES, [3.6](dbcacrea.md)

clusterware diagnostics, [A.1.3](trouble.md)

commands

crsctl start crs, [2.3.1](racinstl.md)

lsnrctl start instance, [2.3.4](racinstl.md)

ps, [1.6](chklist.md)

components

created when using DBCA, [7.4](undrstnd.md)

configuration assistants

troubleshooting, [A.1.5](trouble.md)

connection load balancing, [7.8](undrstnd.md)

control file

installed configuration, [7.4.2](undrstnd.md)

control files, [1.4.4](chklist.md)

described, [7.4.2](undrstnd.md)

convert to cluster database

administrative considerations, [C.1](cvrt2rac.md)

from non-cluster system, [C.2.1](cvrt2rac.md)

from single-instance, [C.2.3](cvrt2rac.md)

from single-instance to Oracle Real Application Clusters, [C](cvrt2rac.md)

post-conversion, [C.6](cvrt2rac.md)

reasons not to convert, [C.2](cvrt2rac.md)

to Oracle Real Application Clusters from single-instance Oracle databases, [C](cvrt2rac.md)

converting

from single instance to Oracle Real Application Clusters, [C.3](cvrt2rac.md)

from single-instance to Oracle Real Application Clusters, [C.3.4](cvrt2rac.md)

to Oracle Real Application Clusters from single-instance Oracle databases, [B](scripts.md)

with rconfig, [C.3](cvrt2rac.md)

create database

using scripts, [B.1](scripts.md)

creating

Oracle Real Application Clusters database

with Database Configuration Assistant, [2.8](racinstl.md), [3.1](dbcacrea.md), [3.6](dbcacrea.md)

---

## D

data files

storage options, [1.3.4](chklist.md)

database

components, created when using DBCA, [7.4](undrstnd.md)

Database Agent, [7.8.2](undrstnd.md)

and listeners, [7.9.2](undrstnd.md)

and server parameter files, [5.2.1](params.md)

Database Configuration Assistant

components created by, [7.4](undrstnd.md)

control files, [7.4.2](undrstnd.md)

creating Oracle Real Application Clusters database

after installation, [3.6](dbcacrea.md)

during installation, [2.8](racinstl.md), [3.1](dbcacrea.md)

datafiles, [7.4.1](undrstnd.md)

deleting databases with, [3.7](dbcacrea.md)

deleting Oracle Real Application Clusters databases, [3.7](dbcacrea.md)

initialization parameter files, [7.6](undrstnd.md)

Initialization Parameters page, [3.6](dbcacrea.md)

List of Cluster Databases page, [3.7](dbcacrea.md)

Operations page, [3.7](dbcacrea.md)

Oracle ASM Disk Groups page, [3.6](dbcacrea.md)

Recovery Configuration page, [3.6](dbcacrea.md)

redo log files, [7.4.3](undrstnd.md)

rollback segments, [7.5](undrstnd.md)

running in silent mode, [B.8](scripts.md)

Summary dialog, [3.7](dbcacrea.md)

tablespaces, [7.4.1](undrstnd.md)

using, [3.1](dbcacrea.md)

Welcome page, [3.6](dbcacrea.md), [3.6](dbcacrea.md)

*See* DBCA

database configuration type

selecting, [2.4](racinstl.md)

Database Control

configuring after installation, [6.2](srvpool.md), [6.2.4](srvpool.md)

configuring during installation, [6.2](srvpool.md)

configuring with DBCA, [6.2.3](srvpool.md)

configuring with EMCA, [6.2.4](srvpool.md)

database creation using scripts, [B.1](scripts.md)

database files

supported storage options, [1.3.4](chklist.md)

datafiles, [1.4.4](chklist.md)

and DBCA, [7.4.1](undrstnd.md)

described, [7.4.1](undrstnd.md)

daylight savings time

and TIMESTAMP WITH TIME ZONE data, [1.4.5](chklist.md)

DB\_NAME, [3.6](dbcacrea.md)

DB\_UNIQUE\_NAME, [3.6](dbcacrea.md)

initialization parameters, [3.6](dbcacrea.md)

DBCA

configuring Database Control with, [6.2.3](srvpool.md)

delete database, [3.7](dbcacrea.md)

loading SSH keys into memory to start, [3.6](dbcacrea.md)

Management Options page, [6.2.3](srvpool.md)

no longer sets local\_listener and remote\_listener, [7.10](undrstnd.md)

starting on UNIX, [6.2.3](srvpool.md)

starting on Windows, [6.2.3](srvpool.md)

dbca.rsp file, [B.5.1](scripts.md)

DBSNMP

password requirements for, [2.7](racinstl.md)

dedicated servers, [7.8.2](undrstnd.md)

delete database with DBCA, [3.7](dbcacrea.md)

deprecated features

service management, [2.8](racinstl.md)

diagnostics, [A.1.3](trouble.md)

directory structure, [D](apa.md)

disk groups

and preferred read disk groups, [Preface](whatsnew.md)

DNS

registering server addresses in, [1.2.4](chklist.md)

downloading installer updates before installing from a secure data center, [1.1.2](chklist.md)

DV\_ACCTMGR, [2.3.2.2](racinstl.md)

DV\_OWNER, [2.3.2.1](racinstl.md)

---

## E

Easy Connect, [7.11](undrstnd.md)

EMCA

command-line arguments, [6.2.4](srvpool.md)

configuring Database Control for Oracle Real Application Clusters, [6.2.1](srvpool.md)

configuring Database Control with, [6.2.4](srvpool.md)

reconfiguring Database Control after changing the listener port, [6.2.7.1](srvpool.md)

specifying port assignments, [6.2.6](srvpool.md)

troubleshooting problems with the Database Control, [6.2.7](srvpool.md)

troubleshooting tips, [6.2.7](srvpool.md)

using an input file for EMCA parameters, [6.2.5](srvpool.md)

Enterprise Manager Configuration Assistant

*See* EMCA

enterprise.rsp file, [B.5.1](scripts.md)

environment variables

ORACLE\_HOME, [1.6](chklist.md)

error messages

during installation, [A.1](trouble.md)

ORA-00845, [3.6](dbcacrea.md)

ORA-01078, [3.6](dbcacrea.md)

/etc/hosts

server addresses in, [1.2.4](chklist.md)

---

## F

failover

and service registration, [7.8.1](undrstnd.md)

failure group, [3.6](dbcacrea.md)

Fast Mirror Resynch, [Preface](whatsnew.md)

Fast Recovery

and files managed by Oracle, [C.3.4](cvrt2rac.md)

Fast Recovery area, [3.6](dbcacrea.md)

features, new, [Preface](whatsnew.md)

file system

storage option for data files, [1.3.4](chklist.md)

file systems

supported options for Oracle Database, [1.3.4](chklist.md)

files

dbca.rsp, [B.5.1](scripts.md)

enterprise.rsp, [B.5.1](scripts.md)

response files, [B.5](scripts.md)

---

## G

gid

selecting, [2.10](racinstl.md)

global database name

selecting, [2.10](racinstl.md)

globalization

support for, [1.1.7](chklist.md), [2.4.2](racinstl.md)

---

## H

high availability

interconnect, [1.1.4](chklist.md)

stopping services, [E.3.2](procstop.md)

high availability IP addresses, [1.1.4](chklist.md)

host names

changing, [7.1](undrstnd.md)

---

## I

initialization parameter files, [7.6](undrstnd.md)

for instances, [5.1](params.md)

listener parameters, [7.9.2](undrstnd.md)

initialization parameters

CLUSTER\_DATABASE\_INSTANCES, [3.6](dbcacrea.md)

DB\_NAME, [3.6](dbcacrea.md)

DISPATCHERS, [7.8.2](undrstnd.md)

LOCAL\_LISTENER, [7.8.2](undrstnd.md)

MEMORY\_TARGET, [3.6](dbcacrea.md)

REMOTE\_LISTENER, [7.8.2](undrstnd.md)

installation

and globalization, [1.1.7](chklist.md), [2.4.2](racinstl.md)

directory structure, [D](apa.md)

listener.ora file, [7.9.4](undrstnd.md)

non-interactive, [B.1](scripts.md)

of additional products after installation is completed, [3.6](dbcacrea.md)

Oracle Configuration Manager, [2.5](racinstl.md)

Oracle Database Vault, [2.3](racinstl.md)

response files, [B.5](scripts.md)

preparing, [B.5](scripts.md), [B.5.2](scripts.md)

templates, [B.5](scripts.md)

silent mode, [B.6](scripts.md)

tnsnames.ora file, [7.10](undrstnd.md)

instances

initialization parameter files, [5.1](params.md)

---

## J

Java Message Service (JMS), [6.2.6](srvpool.md)

---

## L

language

*See* globalization., [1.1.7](chklist.md)

language support and installation, [2.4.2](racinstl.md)

List of Cluster Databases page, [3.7](dbcacrea.md)

listener

automatic migration from 10.1 to 10.2, [3.3](dbcacrea.md)

identifying Oracle home for, [1.6](chklist.md)

lsnrctl command, [1.6](chklist.md)

registration, [7.9.4.1](undrstnd.md)

service registration, [7.9.4](undrstnd.md)

stopping, [1.6](chklist.md), [1.6](chklist.md)

stopping existing listener process, [1.6](chklist.md)

listener.ora file, [7.9.4](undrstnd.md)

configuring, [7.9](undrstnd.md)

default configuration, [7.9.4](undrstnd.md)

listeners

listener.ora file, [7.9.4](undrstnd.md)

load balancing

and service registration, [7.8](undrstnd.md)

local listener

configuring, [7.8.2](undrstnd.md)

local\_listener

no longer set in tnsnames.ora by DBCA, [7.10](undrstnd.md)

log file

how to see the log file during installation, [2](racinstl.md)

troubleshooting with, [A.1.4](trouble.md)

lsnrctl command, [1.6](chklist.md)

---

## M

Management Options page

in DBCA, [6.2.3](srvpool.md)

Memory Size (SGA and PGA), [3.6](dbcacrea.md)

MEMORY\_TARGET, [3.6](dbcacrea.md)

migration

from single-instance, [C.2](cvrt2rac.md)

multiple Oracle homes

and Oracle Clusterware, [1.1.6](chklist.md)

multiple Oracle RAC databases

clusterware requirements for, [1.1.6](chklist.md)

My Oracle Support, [4.1.1](postinst.md)

and storage requirements, [1.3](chklist.md)

check before installation, [1.1.1](chklist.md)

---

## N

Net Configuration Assistant (NetCA)

response files, [B.7](scripts.md)

running at command prompt, [B.7](scripts.md)

Net naming methods, [7.11](undrstnd.md)

net service names, [7.10](undrstnd.md)

netca.rsp file, [B.5.1](scripts.md)

network

planned interface use, [1.2](chklist.md)

server addresses, [1.2.4](chklist.md)

network attached storage (NAS), [1.3.4](chklist.md)

network configuration files

listener.ora, [7.9.4](undrstnd.md)

sqlnet.ora, [7.11](undrstnd.md)

tnsnames.ora, [7.10](undrstnd.md)

network directory, [D.2](apa.md)

new features, [Preface](whatsnew.md)

---

## O

olsnodes command, [A.1.3](trouble.md)

operating system

preinstallation requirements for Oracle RAC, [1.2.7](chklist.md)

Optimal Flexible Architecture (OFA), [2.8](racinstl.md)

Oracle Application Express

online help, [2.1.3](racinstl.md)

Oracle Text and, [2.1.3](racinstl.md)

requirements for installation, [2.1](racinstl.md)

web browsers supported for, [1.2.6](chklist.md)

Oracle ASM

and candidate disks, [3.6](dbcacrea.md)

and failure groups, [3.6](dbcacrea.md)

Change disk discovery path, [3.6](dbcacrea.md)

disk group, [Preface](whatsnew.md)

Fast Mirror Resync, [Preface](whatsnew.md)

Oracle Database versions compatible with this release, [1.6](chklist.md)

OSASM group, [Preface](whatsnew.md)

preferred read disk groups, [Preface](whatsnew.md)

response files, [B.4.2](scripts.md)

rolling upgrade of, [Preface](whatsnew.md)

storage option for data files, [1.3.4](chklist.md)

SYSASM privilege, [Preface](whatsnew.md)

Oracle Cluster Registry port, [F.3](ports.md)

Oracle Clusterware

and multiple database versions, [1.1.6](chklist.md)

ports, ranges and protocol, [F.3](ports.md)

Oracle Configuration Manager

information needed to enable, [2.5](racinstl.md)

information to provide for configuration of, [Preface](whatsnew.md)

postinstallation, [4.3](postinst.md)

Oracle Connection Manager

ports, ranges and protocol, [F.3](ports.md)

Oracle Data Guard

ports, ranges and protocol, [F.3](ports.md)

Oracle Data Mining, [Preface](whatsnew.md)

Oracle Database

data file storage options, [1.3.4](chklist.md)

supported storage options for, [1.3.3](chklist.md)

upgrades of, [1.1.6](chklist.md), [2.2](racinstl.md)

versions that can coexist using Oracle ASM, [1.6](chklist.md)

Oracle Database Configuration Assistant

response file, [B.5.1](scripts.md)

Oracle Database Upgrade Assistant, [3.3](dbcacrea.md), [C](cvrt2rac.md)

Oracle Database Vault, [Preface](whatsnew.md), [Preface](whatsnew.md)

configuration, [2.3](racinstl.md)

Oracle Database Vault Account Manager (DV\_ACCTMGR), [2.3.2.2](racinstl.md)

Oracle Database Vault Owner (DV\_OWNER), [2.3.2.1](racinstl.md)

starting and stopping Oracle RAC instances with, [2.3.4](racinstl.md)

Oracle Enterprise Management Agent

ports

changing, [F.4](ports.md)

ranges and protocol, [F.3](ports.md)

Oracle Enterprise Manager

ASMSNMP, [1.4.2](chklist.md)

using to convert single-instance databases to Oracle Real Application Clusters, [C.3.4](cvrt2rac.md)

Oracle Enterprise Manager Database Console

ports

changing, [F.5](ports.md)

ranges and protocol, [F.3](ports.md)

Oracle Event Manager

ports, ranges and protocol, [F.3](ports.md)

oracle home

ASCII path for, [1.2.3](chklist.md)

Oracle home directory

identifying for listener, [1.6](chklist.md)

Oracle Net

identifying Oracle home for listener, [1.6](chklist.md)

lsnrctl command, [1.6](chklist.md)

stopping existing listener, [1.6](chklist.md)

stopping listener, [1.6](chklist.md)

stopping the listener, [1.6](chklist.md)

Oracle Net Configuration Assistant

response file, [B.5.1](scripts.md)

Oracle Net Listener

ports

ranges and protocol, [F.3](ports.md)

Oracle RAC One Node, [2.4](racinstl.md)

Oracle RAC Technologies Certification Matrix, [1.1.1](chklist.md)

Oracle Real Application Clusters

databases, deleting, [3.7](dbcacrea.md)

installed components of, [1.4.4](chklist.md)

operating system requirements for, [1.2.7](chklist.md)

overview, [3](dbcacrea.md), [7](undrstnd.md)

ports

ranges and protocol, [F.3](ports.md)

storage requirements for, [1.3](chklist.md)

Oracle Real Application Testing, [Preface](whatsnew.md)

Oracle SQL Developer, [Preface](whatsnew.md), [Preface](whatsnew.md)

Oracle Text

Oracle Application Express requirement for, [2.1.3](racinstl.md)

Oracle Ultra Search, [Preface](whatsnew.md)

Oracle Universal Installer

response files

list of, [B.5.1](scripts.md)

Oracle Upgrade Companion, [1.1.6](chklist.md), [2.2](racinstl.md)

Oracle Warehouse Builder, [Preface](whatsnew.md), [Preface](whatsnew.md)

Oracle XML DB, [Preface](whatsnew.md)

ports

changing, [F.6](ports.md)

ranges and protocol, [F.3](ports.md)

ORACLE\_BASE environment variable

setting, [4.2.2](postinst.md)

ORACLE\_HOME environment variable

setting, [1.6](chklist.md), [4.2.2](postinst.md)

ORACLE\_SID environment variable

setting, [4.2.2](postinst.md)

Oracle9i

checking for listener, [1.6](chklist.md)

oratab file, [7.3](undrstnd.md)

OSASM

and SYSASM, [Preface](whatsnew.md)

OWBSYS repository, [Preface](whatsnew.md)

---

## P

parameter file search order, [5.3](params.md)

parameters

initialization, [5](params.md)

pass phrase, [3.6](dbcacrea.md)

for SSH, [3.6](dbcacrea.md)

password

Oracle Database Vault Account Manager, [2.3.2.2](racinstl.md)

Oracle Database Vault Owner, [2.3.2.1](racinstl.md)

passwords, [2.7](racinstl.md)

patch updates

download, [4.1.1](postinst.md)

install, [4.1.1](postinst.md)

My Oracle Support, [4.1.1](postinst.md)

patch upgrades, [E.3.1](procstop.md)

patches

operating system patches for Oracle RAC, [1.2.7](chklist.md)

policy-managed databases

and SCANs, [6.1](srvpool.md)

portlist.ini file, [F.2](ports.md)

ports

access URLs, [F.2](ports.md)

Cluster Manager, ranges and protocol, [F.3](ports.md)

Cluster Synchronization Services, ranges and protocol, [F.3](ports.md)

configured for applications, [F.2](ports.md)

default ranges, [F](ports.md)

Oracle Cluster Registry, [F.3](ports.md)

Oracle Clusterware, ranges and protocol, [F.3](ports.md)

Oracle Connection Manager, ranges and protocol, [F.3](ports.md)

Oracle Data Guard, ranges and protocol, [F.3](ports.md)

Oracle Enterprise Management Agent

changing, [F.4](ports.md)

ranges and protocol, [F.3](ports.md)

Oracle Enterprise Manager Database Console

changing, [F.5](ports.md)

ranges and protocol, [F.3](ports.md)

Oracle Event Manager, ranges and protocol, [F.3](ports.md)

Oracle Net Listener

ranges and protocol, [F.3](ports.md)

Oracle Real Application Clusters

ranges and protocol, [F.3](ports.md)

Oracle XML DB

changing, [F.6](ports.md)

ranges and protocol, [F.3](ports.md)

reconfiguring Database Control after changing the listener port, [6.2.7.1](srvpool.md)

specifying Database Control ports, [6.2.6](srvpool.md)

postinstallation

patch download and install, [4.1.1](postinst.md)

product configuration, [4.1.3](postinst.md)

root.sh back up, [4.2.1](postinst.md)

user accounts setup, [4.2.4](postinst.md)

preconfigured database installation types, [2.4.1](racinstl.md)

preinstallation requirements

operating system, [1.2.7](chklist.md)

private IP address, [1.2.4](chklist.md)

process

stopping existing, [1.6](chklist.md)

stopping existing listener process, [1.6](chklist.md)

stopping listener process, [1.6](chklist.md)

ps command, [1.6](chklist.md)

public IP address, [1.2.4](chklist.md)

---

## R

racgimon, [7.8.2](undrstnd.md)

raw devices

supported for upgrades only, [1.3.4](chklist.md)

RBS tablespace

description, [7.4.1](undrstnd.md)

rconfig, [C.3](cvrt2rac.md)

readme.txt file, [F.2](ports.md)

recovery files

supported storage options, [1.3.4](chklist.md)

redo log file

installed configuration, [7.4.3](undrstnd.md)

redo log files, [1.4.4](chklist.md)

described, [7.4.3](undrstnd.md)

Redundant Interconnect Usage, [1.1.4](chklist.md)

remote listener

configuring, [7.8.2](undrstnd.md)

Remote Method Invocation (RMI), [6.2.6](srvpool.md)

remote\_listener

no longer set in tnsnames.ora by DBCA, [7.10](undrstnd.md)

response file installation

preparing, [B.5](scripts.md)

response files

templates, [B.5](scripts.md)

silent mode, [B.6](scripts.md)

response file mode

about, [B.4](scripts.md)

reasons for using, [B.4.1](scripts.md)

*See also* response files, silent mode,

response files

about, [B.4](scripts.md)

creating with template, [B.5.1](scripts.md)

dbca.rsp, [B.5.1](scripts.md)

enterprise.rsp, [B.5.1](scripts.md)

for Oracle ASM, [B.4.2](scripts.md)

general procedure, [B.4.3](scripts.md)

Net Configuration Assistant, [B.7](scripts.md)

netca.rsp, [B.5.1](scripts.md)

passing values at command line, [B.4](scripts.md)

specifying with Oracle Universal Installer, [B.6](scripts.md)

*See also* silent mode.,

rollback segments

described, [7.5](undrstnd.md)

root.sh

back up, [4.2.1](postinst.md)

---

## S

SCANs

use of SCANs required for clients of policy-managed databases, [6.1](srvpool.md)

scripts to create an Oracle Real Application Clusters database, [B.1](scripts.md)

Secure Configuration database installation option, [2.6](racinstl.md)

secure data center

downloading installer updates for, [1.1.2](chklist.md)

secure shell configuration, [1.2.5](chklist.md)

security

command line DBCA required to enable or disable, [2.6](racinstl.md)

for Oracle Database Vault Account Manager password, [2.3.2.2](racinstl.md)

for Oracle Database Vault owner password, [2.3.2.1](racinstl.md)

Secure Configuration option, [2.6](racinstl.md)

selecting passwords, [2.7](racinstl.md)

server parameter files, [1.4.4](chklist.md), [5](params.md), [5.2](params.md), [7.6](undrstnd.md)

errors, [5.5](params.md)

server pools

configuration, [6](srvpool.md)

SCANs required for policy-managed, [6.1](srvpool.md)

XML conversion files for, [C.5](cvrt2rac.md)

service registration

about, [7.9.4](undrstnd.md)

configuring, [7.8](undrstnd.md)

shared server, [7.8.2](undrstnd.md)

sid, [2.10](racinstl.md)

silent mode

about, [B.4](scripts.md)

reasons for using, [B.4.1](scripts.md)

*See also* response files.,

silent mode installation, [B.6](scripts.md)

single-instance databases

converting, [C.3.4](cvrt2rac.md)

SPFILE

default creation, [5.2](params.md)

default location, [5.2.1](params.md)

managing on raw device, [5.2.1](params.md)

migrating to, [5.4](params.md)

sqlnet.ora file, [7.11](undrstnd.md)

SSH, [3.6](dbcacrea.md)

ssh configuration, [1.2.5](chklist.md)

Standard Edition Oracle Database

supported storage options for, [1.3.3](chklist.md)

storage

for Oracle RAC, [1.3](chklist.md)

supported options, [1.3.4](chklist.md)

storage options

Fast Mirror Resynch, [Preface](whatsnew.md)

for Enterprise Edition installations, [1.3.3](chklist.md)

for Standard Edition installations, [1.3.3](chklist.md)

Summary dialog, [3.7](dbcacrea.md)

supported storage options, [1.3.4](chklist.md), [1.3.4](chklist.md)

and block devices, [1.3.4](chklist.md)

supported technology, [1.1.1](chklist.md)

SYS

password requirements for, [2.7](racinstl.md)

SYSASM, [Preface](whatsnew.md)

and OSASM, [Preface](whatsnew.md)

sysasm privilege

storage tasks requiring, [3.6](dbcacrea.md), [3.6](dbcacrea.md), [3.6](dbcacrea.md)

SYSMAN

password requirements for, [2.7](racinstl.md)

SYSTEM

password requirements for, [2.7](racinstl.md)

system identifier, [2.10](racinstl.md)

SYSTEM tablespace

description, [7.4.1](undrstnd.md)

---

## T

tablespaces

and DBCA, [7.4.1](undrstnd.md)

expanding for large sorts, [7.4.1](undrstnd.md)

RBS, [7.4.1](undrstnd.md)

SYSTEM, [7.4.1](undrstnd.md)

TEMP, [7.4.1](undrstnd.md)

undo tablespaces for automatic undo management, [7.4.1](undrstnd.md)

USERS, [7.4.1](undrstnd.md)

TEMP tablespace

described, [7.4.1](undrstnd.md)

time zone version files, [1.4.5](chklist.md)

tnsnames.ora file, [7.10](undrstnd.md)

default configuration, [7.10](undrstnd.md)

troubleshoooting

Nodes unavailable for selection, [A.1.1](trouble.md)

troubleshooting

An error occurred while trying to get the disks, [A.1.1](trouble.md)

Can’t open display, [A.1.1](trouble.md)

configuration assistant errors, [A.1.5](trouble.md)

Connection refused by server, [A.1.1](trouble.md)

disk space errors, [1.2.3](chklist.md)

error starting instance, [A.1.1](trouble.md)

Failed to connect to server, [A.1.1](trouble.md)

log file, [2](racinstl.md), [A.1.4](trouble.md)

node is unreachable, [A.1.1](trouble.md)

online help for Oracle Application Express, [2.1.3](racinstl.md)

PRKP-1001

Error starting instance, [A.1.1](trouble.md)

problems starting or configuring the Database Control, [6.2.7](srvpool.md)

PROT-8

Failed to import data from specified file to the cluster registry, [A.1.1](trouble.md)

reviewing a log file, [A.1.4](trouble.md)

time stamp in the future, [A.1.1](trouble.md)

with EMCA, [6.2.7](srvpool.md)

X server, [A.1.1](trouble.md)

YPBINDPROC\_DOMAIN

Domain not bound, [A.1.1](trouble.md)

Troubleshooting

when using EMCA, [6.2.7](srvpool.md)

Typical install type, [2.4](racinstl.md)

---

## U

undo management, [7.5](undrstnd.md)

upgrade, [1.1.6](chklist.md), [1.1.6](chklist.md), [2.2](racinstl.md)

and using same Oracle home, [1.2.3](chklist.md)

and using same Oracle home type, [2.12](racinstl.md)

of existing Oracle Databases, [3.3](dbcacrea.md)

of listener, [3.3](dbcacrea.md)

of Oracle Database with patch, [E.3.1](procstop.md)

Oracle Clusterware version requirement for, [1.1.6](chklist.md)

TIMESTAMP WITH TIME ZONE data, [1.4.5](chklist.md)

upgrades

user accounts

USERS tablespace

described, [7.4.1](undrstnd.md)

---

## V

vip address, [1.2.4](chklist.md)

virtual IP.*See* VIP, [1.2.4](chklist.md)

virtual IP address, [1.2.4](chklist.md)

---

## W

web browsers