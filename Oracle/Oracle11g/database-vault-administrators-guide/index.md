---
title: Index
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/index.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

A B C D E F G H I J L M N O P Q R S T U V W X

---

## Symbols

% wildcard, [18.3](reports.md)

---

## A

access control policy

configuring with tools and components

reports

access control run-time PL/SQL procedures and functions, [15.1](plsql_interfaces.md)

Access to Sensitive Objects Report, [18.5.3.2](reports.md)

accessibility features, [C.4](dvca.md)

accounts

Accounts With DBA Roles Report, [18.5.5.2](reports.md)

Accounts with SYSDBA/SYSOPER Privilege Report, [18.5.3.4](reports.md)

ad hoc tools

preventing use of, [7.8.1](cfgfact.md)

administrators

DBA operations in Oracle Database Vault, [10](dba.md)

restricting different types, [7.9.1](cfgfact.md)

ADRCI utility

Database Vault, [E.1.6.3](troubleshooting.md)

alerts

email alert in rule set, [5.8.1](cfrulset.md)

Enterprise Manager Grid Control, [10.1.3](dba.md)

ALTER DATABASE statement

monitoring, [17.2](monitoring.md)

ALTER ROLE statement

monitoring, [17.3.1](monitoring.md)

ALTER SESSION privilege

enabling trace files, [E.1.5](troubleshooting.md)

reports, ALTER SYSTEM or ALTER SESSION Report, [18.5.5.5](reports.md)

ALTER SESSION statement

guidelines on managing privileges, [D.6.6](guidelines.md)

ALTER SYSTEM or ALTER SESSION Report, [18.5.5.5](reports.md)

ALTER SYSTEM privilege

reports, ALTER SYSTEM or ALTER SESSION Report, [18.5.5.5](reports.md)

ALTER SYSTEM statement

controlling with command rules, [6.1](cfcmdaut.md)

guidelines on managing privileges, [D.6.6](guidelines.md)

ALTER TABLE statement

monitoring, [17.2](monitoring.md)

ALTER USER statement

monitoring, [17.3.1](monitoring.md)

ANY privileges, [11.2.12](db_objects.md)

ANY System Privileges for Database Accounts Report, [18.5.2.4](reports.md)

APIs

*See* DBMS\_MACADM package, DBMS\_MACSEC\_ROLES package, DBMS\_MACUTL package

assistive technology, [C.4](dvca.md)

AUD$ table

*See* SYS.AUD$ table

audit policy change

monitoring, [17.3.1](monitoring.md)

AUDIT privilege, [18.5.5.10](reports.md)

AUDIT Privileges Report, [18.5.5.10](reports.md)

AUDIT\_SYS\_OPERATIONS initialization parameter, [2.1](dv_impact.md)

AUDIT\_TRAIL initialization parameter

effect on Core Database Audit Report, [18.5.8](reports.md)

AUDIT\_TRAIL$ system table

affected by AUDIT\_TRAIL initialization parameter, [A.1.2](audplcy.md)

archiving, [A.2](audplcy.md)

format, [A.1.2](audplcy.md)

purging, [A.2](audplcy.md)

auditing

archiving Database Vault audit trail, [A.2](audplcy.md)

Core Database Audit Report, [18.5.8](reports.md)

DBMS\_MACUTL fields, [14.2.1](apis_dbms_macutl.md)

factors

options, [7.3](cfgfact.md)

intruders

using factors, [7.3](cfgfact.md)

using rule sets, [5.3](cfrulset.md)

Oracle Database audit settings, [A.3](audplcy.md)

purging Database Vault audit trail, [A.2](audplcy.md)

realms

DBMS\_MACUTL fields, [14.2.1](apis_dbms_macutl.md)

options, [4.3](cfrealms.md)

reports, [18.4.2](reports.md)

rule sets

DBMS\_MACUTL fields, [14.2.1](apis_dbms_macutl.md)

options, [5.3](cfrulset.md)

secure application roles

audit records, [8.8](cfseappr.md)

views used to audit events, [16.2](views.md)

auditing policies

about, [A](audplcy.md)

audit events

about, [A.1.1](audplcy.md)

custom events

audit trail, [A.1.2](audplcy.md)

events that are tracked, [A.1.1](audplcy.md)

monitoring changes to, [17.3.1](monitoring.md)

authentication

Authentication\_Method default factor, [7.2](cfgfact.md)

command rules, [6.1](cfcmdaut.md)

method, finding with DVF.F$AUTHENTICATION\_METHOD, [15.2.1](plsql_interfaces.md)

realm procedures, [12.2](apis_dbms_macadm.md)

authorizations

Oracle Data Pump activities, [10.2.1](dba.md)

realms, [4.6](cfrealms.md)

scheduling database jobs, [10.3.1](dba.md)

---

## B

BECOME USER Report, [18.5.5.4](reports.md)

BECOME USER system privilege

about, [18.5.5.4](reports.md)

---

## C

catalog-based roles, [18.5.5.9](reports.md)

child factors

*See* factors

clients

finding IP address with DVF.F$CLIENT\_IP, [15.2.2](plsql_interfaces.md)

code groups

retrieving value with DBMS\_MACUTL functions, [14.3](apis_dbms_macutl.md)

Command Rule Audit Report, [18.4.2.2](reports.md)

Command Rule Configuration Issues Report, [18.4.1.1](reports.md)

command rules

about, [6.1](cfcmdaut.md)

creating, [6.4](cfcmdaut.md)

data dictionary view, [6.10](cfcmdaut.md)

data masking, [10.8.4](dba.md)

default command rules, [6.2](cfcmdaut.md)

default command rules not showing in Database Vault Administrator, [C.1](dvca.md)

deleting, [6.5](cfcmdaut.md)

editing, [6.4](cfcmdaut.md)

functions

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

guidelines, [6.8](cfcmdaut.md)

how command rules work, [6.6](cfcmdaut.md)

objects

name, [6.4](cfcmdaut.md)

owner, [6.4](cfcmdaut.md)

performance effect, [6.9](cfcmdaut.md)

procedures

DBMS\_MACADM (configuration), [12.4](apis_dbms_macadm.md)

process flow, [6.6](cfcmdaut.md)

propagating policies to other databases, [10.1.2](dba.md)

reports, [6.10](cfcmdaut.md)

troubleshooting

with auditing report, [18.4.2.2](reports.md)

tutorial, [6.7.1](cfcmdaut.md)

views, [6.10](cfcmdaut.md), [16.3](views.md)

*See also* rule sets

selecting, [6.4](cfcmdaut.md)

used with, [6.1](cfcmdaut.md)

compliance

Oracle Database Vault addressing, [1.3](dvintro.md)

computer name

finding with DVF.F$MACHINE, [15.2.13](plsql_interfaces.md)

Machine default factor, [7.2](cfgfact.md)

configuration

monitoring changes, [17.3.1](monitoring.md)

*See also* DBMS\_MACADM package

CONNECT events, controlling with command rules, [6.1](cfcmdaut.md)

core database

troubleshooting with Core Database Vault Audit Report, [18.4.2.5](reports.md)

Core Database Audit Report, [18.5.8](reports.md)

Core Database Vault Audit Trail Report, [18.4.2.5](reports.md)

CPU\_PER\_SESSION resource profile, [18.5.6.2](reports.md)

CREATE ANY JOB privilege, [D.6.3](guidelines.md)

CREATE ANY JOB statement

guidelines on managing privileges, [D.6.3](guidelines.md)

CREATE EXTERNAL JOB privilege, [D.6.4](guidelines.md)

CREATE JOB privilege, [D.6.3](guidelines.md)

CREATE JOB statement

guidelines on managing privileges, [D.6.3](guidelines.md)

CREATE ROLE statement

monitoring, [17.3.1](monitoring.md)

CREATE TABLE statement

monitoring, [17.2](monitoring.md)

CREATE USER statement

monitoring, [17.3.1](monitoring.md)

---

## D

data definition language (DDL)

statement

controlling with command rules, [6.1](cfcmdaut.md)

data dictionary

adding DV\_ACCTMGR role to realm, [3.3.2](getting_started.md)

Data Dictionary realm

data masking, [10.8.2](dba.md)

data manipulation language (DML)

statement

checking with DBMS\_MACUTL.CHECK\_DVSYS\_DML\_ALLOWED function, [14.3](apis_dbms_macutl.md)

controlling with command rules, [6.1](cfcmdaut.md)

data masking

about, [10.8.1](dba.md)

adding users to realms for, [10.8.3](dba.md)

creating command rule for, [10.8.4](dba.md)

errors that can appear, [10.8.1](dba.md)

data Oracle Database Vault recognizes

*See* factors

Data Pump

*See* Oracle Data Pump

Database Account Default Password Report, [18.5.7.1](reports.md)

Database Account Status Report, [18.5.7.2](reports.md)

database accounts

counting privileges of, [18.5.4.1](reports.md)

DBSNMP

changing password, [10.1.5](dba.md)

granted DV\_MONITOR role, [11.2.4](db_objects.md)

realm for, [4.2](cfrealms.md)

DVSYS, [11.3](db_objects.md)

LBACSYS, [11.3](db_objects.md)

monitoring, [17.3.1](monitoring.md)

reports

Accounts With DBA Roles Report, [18.5.5.2](reports.md)

ALTER SYSTEM or ALTER SESSION Report, [18.5.5.5](reports.md)

ANY System Privileges for Database Accounts Report, [18.5.2.4](reports.md)

AUDIT Privileges Report, [18.5.5.10](reports.md)

BECOME USER Report, [18.5.5.4](reports.md)

Database Account Default Password Report, [18.5.7.1](reports.md)

Database Account Status Report, [18.5.7.2](reports.md)

Database Accounts With Catalog Roles Report, [18.5.5.9](reports.md)

Direct and Indirect System Privileges By Database Account Report, [18.5.2.2](reports.md)

Direct Object Privileges Report, [18.5.1.3](reports.md)

Direct System Privileges By Database Account Report, [18.5.2.1](reports.md)

Hierarchical System Privileges by Database Account Report, [18.5.2.3](reports.md)

Object Access By PUBLIC Report, [18.5.1.1](reports.md)

Object Access Not By PUBLIC Report, [18.5.1.2](reports.md)

OS Security Vulnerability Privileges, [18.5.5.11](reports.md)

Password History Access Report, [18.5.5.6](reports.md)

Privileges Distribution By Grantee Report, [18.5.4.1](reports.md), [18.5.4.1](reports.md), [18.5.4.1](reports.md)

Privileges Distribution By Grantee, Owner Report, [18.5.4.2](reports.md), [18.5.4.2](reports.md)

Privileges Distribution By Grantee, Owner, Privilege Report, [18.5.4.3](reports.md), [18.5.4.3](reports.md)

Roles/Accounts That Have a Given Role Report, [18.5.5.8](reports.md)

Security Policy Exemption Report, [18.5.5.3](reports.md)

WITH ADMIN Privilege Grants Report, [18.5.5.1](reports.md)

WITH GRANT Privileges Report, [18.5.5.7](reports.md)

solution for lockouts, [B.1](dvdisabl.md)

suggested, [11.3](db_objects.md)

SYSMAN

realm for, [4.2](cfrealms.md)

Database Accounts With Catalog Roles Report, [18.5.5.9](reports.md)

database administrative operations, [10](dba.md)

database configuration

monitoring changes, [17.2](monitoring.md)

Database Configuration Assistant (DBCA)

Oracle Database Vault, [3.1](getting_started.md)

database definition language (DDL)

statements

controlling with command rules, [6.1](cfcmdaut.md)

database domains, Database\_Domain default factor, [7.2](cfgfact.md)

database objects

Oracle Database Vault, [11](db_objects.md), [16.22](views.md)

reports

Object Dependencies Report, [18.5.1.4](reports.md)

*See also* objects

database options, installing, [B.1](dvdisabl.md)

database roles

about, [11.2.1](db_objects.md)

counting privileges of, [18.5.4.1](reports.md)

default Oracle Database Vault, [11.2.1](db_objects.md)

DV\_ACCTMGR

about, [11.2.12](db_objects.md)

adding to Data Dictionary realm, [3.3.2](getting_started.md)

DV\_ADMIN, [11.2.3](db_objects.md)

DV\_AUDIT\_CLEANUP, [11.2.6](db_objects.md)

DV\_GOLDENGATE\_ADMIN, [11.2.9](db_objects.md)

DV\_GOLDENGATE\_REDO\_ACCESS, [11.2.10](db_objects.md)

DV\_MONITOR, [11.2.4](db_objects.md)

DV\_OWNER, [11.2.2](db_objects.md)

DV\_PATCH\_ADMIN, [11.2.11](db_objects.md)

DV\_PUBLIC, [11.2.15](db_objects.md)

DV\_REALM\_OWNER, [11.2.13](db_objects.md)

DV\_REALM\_RESOURCE, [11.2.14](db_objects.md)

DV\_SECANALYST, [11.2.5](db_objects.md)

DV\_STREAMS\_ADMIN, [11.2.7](db_objects.md)

DV\_XSTREAM\_ADMIN, [11.2.8](db_objects.md)

enabled, determining with DVSYS.ROLE\_IS\_ENABLED, [15.1.5](plsql_interfaces.md)

monitoring, [17.3.1](monitoring.md)

Oracle Database Vault, default, [11.2.1](db_objects.md)

reports

Accounts With DBA Roles Report, [18.5.5.2](reports.md)

ALTER SYSTEM or ALTER SESSION Report, [18.5.5.5](reports.md)

AUDIT Privileges Report, [18.5.5.10](reports.md)

BECOME USER Report, [18.5.5.4](reports.md)

Database Accounts With Catalog Roles Report, [18.5.5.9](reports.md)

OS Security Vulnerability Privileges, [18.5.5.11](reports.md)

Privileges Distribution By Grantee Report, [18.5.4.1](reports.md)

Roles/Accounts That Have a Given Role Report, [18.5.5.8](reports.md)

Security Policy Exemption Report, [18.5.5.3](reports.md)

WITH ADMIN Privilege Grants Report, [18.5.5.1](reports.md)

separation of duty enforcement, [2.3](dv_impact.md)

database sessions, [7.3](cfgfact.md)

controlling with Allow Sessions default rule set, [5.2](cfrulset.md)

factor evaluation, [7.7.1](cfgfact.md)

session user name, Proxy\_User default factor, [7.2](cfgfact.md)

Database Vault

*See* Oracle Database Vault

Database Vault Account Management realm

SYS access to, [4.2](cfrealms.md)

Database Vault Administrator

setting URL in Oracle Enterprise Manager, [10.1.1](dba.md)

databases

dbconsole

checking process, [3.2.2](getting_started.md)

starting process, [3.2.2](getting_started.md)

defined with factors, [7.1](cfgfact.md)

domain, Domain default factor, [7.2](cfgfact.md)

event monitoring, [E.1.1](troubleshooting.md)

grouped schemas

*See* realms

host names, Database\_Hostname default factor, [7.2](cfgfact.md)

instance, retrieving information with functions, [12.5](apis_dbms_macadm.md)

instances

Database\_Instance default factor, [7.2](cfgfact.md)

managing multiple instances, [3.2.2](getting_started.md)

names, finding with DVF.F$DATABASE\_INSTANCE, [15.2.5](plsql_interfaces.md)

number, finding with DVSYS.DV\_INSTANCE\_NUM, [15.3.3](plsql_interfaces.md)

IP addresses

Database\_IP default factor, [7.2](cfgfact.md)

retrieving with DVF.F$DATABASE\_IP, [15.2.6](plsql_interfaces.md)

log file location, [3.2.2](getting_started.md)

monitoring events, [E.1.1](troubleshooting.md)

names

Database\_Name default factor, [7.2](cfgfact.md)

retrieving with DVF.F$DATABASE\_NAME, [15.2.7](plsql_interfaces.md)

retrieving with DVSYS.DV\_DATABASE\_NAME, [15.3.4](plsql_interfaces.md)

parameters

Security Related Database Parameters Report, [18.5.6.1](reports.md)

roles that do not exist, [18.4.1.7](reports.md)

schema creation, finding with DVF.F$IDENTIFICATION\_TYPE, [15.2.10](plsql_interfaces.md)

schema creation, Identification\_Type default factor, [7.2](cfgfact.md)

structural changes, monitoring, [17.2](monitoring.md)

user name, Session\_User default factor, [7.2](cfgfact.md)

DBA role

impact of Oracle Database Vault installation, [2.4](dv_impact.md)

DBA\_DV\_COMMAND\_RULE view, [6.10](cfcmdaut.md)

DBA\_USERS\_WITH\_DEFPWD data dictionary view

access to in Oracle Database Vault, [2.4](dv_impact.md)

dbconsole process

checking status, [3.2.2](getting_started.md)

starting, [3.2.2](getting_started.md)

DBMS\_FILE\_TRANSFER package, guidelines on managing, [D.6.1](guidelines.md)

DBMS\_MACADM package

about, [12.1](apis_dbms_macadm.md)

command rule procedures, listed, [12.4](apis_dbms_macadm.md)

factor procedures, listed, [12.5](apis_dbms_macadm.md)

Oracle Label Security policy procedures, listed, [12.7](apis_dbms_macadm.md)

realm procedures, listed, [12.2](apis_dbms_macadm.md)

rule set procedures, listed, [12.3](apis_dbms_macadm.md)

secure application role procedures, listed, [12.6](apis_dbms_macadm.md)

DBMS\_MACADM.ADD\_AUTH\_TO\_REALM procedure, [12.2.1](apis_dbms_macadm.md)

DBMS\_MACADM.ADD\_FACTOR\_LINK procedure, [12.5.1](apis_dbms_macadm.md)

DBMS\_MACADM.ADD\_NLS\_DATA

procedure, [C.6](dvca.md)

DBMS\_MACADM.ADD\_NLS\_DATA procedure, [12.8.1](apis_dbms_macadm.md)

DBMS\_MACADM.ADD\_OBJECT\_TO\_REALM procedure, [12.2.2](apis_dbms_macadm.md)

DBMS\_MACADM.ADD\_POLICY\_FACTOR procedure, [12.5.2](apis_dbms_macadm.md)

DBMS\_MACADM.ADD\_RULE\_TO\_RULE\_SET procedure, [12.3.1](apis_dbms_macadm.md)

DBMS\_MACADM.AUTHORIZE\_DATAPUMP\_USER procedure, [12.8.2](apis_dbms_macadm.md), [12.8.4](apis_dbms_macadm.md)

DBMS\_MACADM.AUTHORIZE\_SCHEDULER\_USER procedure, [12.8.3](apis_dbms_macadm.md)

DBMS\_MACADM.CHANGE\_IDENTITY\_FACTOR procedure, [12.5.3](apis_dbms_macadm.md)

DBMS\_MACADM.CHANGE\_IDENTITY\_VALUE procedure, [12.5.4](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_COMMAND\_RULE procedure, [12.4.1](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_DOMAIN\_IDENTITY procedure, [12.5.5](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_FACTOR procedure, [12.5.6](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_FACTOR\_TYPE procedure, [12.5.7](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_IDENTITY procedure, [12.5.8](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_IDENTITY\_MAP procedure, [12.5.9](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_MAC\_POLICY procedure, [12.7.1](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_POLICY\_LABEL procedure, [12.7.2](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_REALM procedure, [12.2.3](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_ROLE procedure, [12.6.1](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_RULE procedure, [12.3.2](apis_dbms_macadm.md)

DBMS\_MACADM.CREATE\_RULE\_SET procedure, [12.3.3](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_AUTH\_FROM\_REALM procedure, [12.2.4](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_COMMAND\_RULE procedure, [12.4.2](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_FACTOR procedure, [12.5.10](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_FACTOR\_LINK procedure, [12.5.11](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_FACTOR\_TYPE procedure, [12.5.12](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_IDENTITY procedure, [12.5.13](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_IDENTITY\_MAP procedure, [12.5.14](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_MAC\_POLICY\_CASCADE procedure, [12.7.3](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_OBJECT\_FROM\_REALM procedure, [12.2.5](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_POLICY\_FACTOR procedure, [12.7.4](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_POLICY\_LABEL procedure, [12.7.5](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_REALM procedure, [12.2.6](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_REALM\_CASCADE procedure, [12.2.7](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_ROLE procedure, [12.6.2](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_RULE procedure, [12.3.4](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_RULE\_FROM\_RULE\_SET procedure, [12.3.5](apis_dbms_macadm.md)

DBMS\_MACADM.DELETE\_RULE\_SET procedure, [12.3.6](apis_dbms_macadm.md)

DBMS\_MACADM.DROP\_DOMAIN\_IDENTITY procedure, [12.5.15](apis_dbms_macadm.md)

DBMS\_MACADM.GET\_INSTANCE\_INFO function, [12.5.16](apis_dbms_macadm.md)

DBMS\_MACADM.GET\_SESSION\_INFO function, [12.5.17](apis_dbms_macadm.md)

DBMS\_MACADM.RENAME\_FACTOR procedure, [12.5.18](apis_dbms_macadm.md)

DBMS\_MACADM.RENAME\_FACTOR\_TYPE procedure, [12.5.19](apis_dbms_macadm.md)

DBMS\_MACADM.RENAME\_REALM procedure, [12.2.8](apis_dbms_macadm.md)

DBMS\_MACADM.RENAME\_ROLE procedure, [12.6.3](apis_dbms_macadm.md)

DBMS\_MACADM.RENAME\_RULE procedure, [12.3.7](apis_dbms_macadm.md)

DBMS\_MACADM.RENAME\_RULE\_SET procedure, [12.3.8](apis_dbms_macadm.md)

DBMS\_MACADM.SYNC\_RULES procedure, [12.3.9](apis_dbms_macadm.md)

DBMS\_MACADM.UNAUTHORIZE\_SCHEDULER\_USER procedure, [12.8.5](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_COMMAND\_RULE procedure, [12.4.3](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_FACTOR procedure, [12.5.20](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_FACTOR\_TYPE procedure, [12.5.21](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_IDENTITY procedure, [12.5.22](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_MAC\_POLICY procedure, [12.7.6](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_REALM procedure, [12.2.9](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_REALM\_AUTH procedure, [12.2.10](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_ROLE procedure, [12.6.4](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_RULE procedure, [12.3.10](apis_dbms_macadm.md)

DBMS\_MACADM.UPDATE\_RULE\_SET procedure, [12.3.11](apis_dbms_macadm.md)

DBMS\_MACSEC\_ROLES package

about, [13.1](apis_macsec_roles.md)

functions, listed, [13.1](apis_macsec_roles.md)

DBMS\_MACSEC\_ROLES.CAN\_SET\_ROLE function, [13.2](apis_macsec_roles.md)

DBMS\_MACSEC\_ROLES.SET\_ROLE procedure, [13.3](apis_macsec_roles.md)

DBMS\_MACUTL package

about, [14.1](apis_dbms_macutl.md)

constants (fields)

examples, [14.2.2](apis_dbms_macutl.md)

listed, [14.2.1](apis_dbms_macutl.md)

procedures and functions, listed, [14.3](apis_dbms_macutl.md)

DBMS\_MACUTL.CHECK\_DVSYS\_DML\_ALLOWED procedure, [14.3.1](apis_dbms_macutl.md)

DBMS\_MACUTL.GET\_CODE\_VALUE function, [14.3.2](apis_dbms_macutl.md)

DBMS\_MACUTL.GET\_DAY function, [14.3.6](apis_dbms_macutl.md)

DBMS\_MACUTL.GET\_HOUR function, [14.3.5](apis_dbms_macutl.md)

DBMS\_MACUTL.GET\_MINUTE function, [14.3.4](apis_dbms_macutl.md)

DBMS\_MACUTL.GET\_MONTH function, [14.3.7](apis_dbms_macutl.md)

DBMS\_MACUTL.GET\_SECOND function, [14.3.3](apis_dbms_macutl.md)

DBMS\_MACUTL.GET\_YEAR function, [14.3.8](apis_dbms_macutl.md)

DBMS\_MACUTL.IS\_ALPHA function, [14.3.9](apis_dbms_macutl.md)

DBMS\_MACUTL.IS\_DIGIT function, [14.3.10](apis_dbms_macutl.md)

DBMS\_MACUTL.IS\_DVSYS\_OWNER function, [14.3.11](apis_dbms_macutl.md)

DBMS\_MACUTL.IS\_OLS\_INSTALLED function, [14.3.12](apis_dbms_macutl.md)

DBMS\_MACUTL.IS\_OLS\_INSTALLED\_VARCHAR function, [14.3.13](apis_dbms_macutl.md)

DBMS\_MACUTL.USER\_HAS\_ROLE function, [14.3.14](apis_dbms_macutl.md)

DBMS\_MACUTL.USER\_HAS\_ROLE\_VARCHAR function, [14.3.15](apis_dbms_macutl.md)

DBMS\_MACUTL.USER\_HAS\_SYSTEM\_PRIVILEGE function, [14.3.16](apis_dbms_macutl.md)

DBMS\_RLS PL/SQL package

SYS granting or revoking EXECUTE on, [Preface](whatsnew.md)

DBSNMP user account

changing password, [10.1.5](dba.md)

granted DV\_MONITOR role, [11.2.4](db_objects.md)

realm for, [4.2](cfrealms.md)

deinstalling Oracle Database Vault, [C.7](dvca.md)

DELETE\_CATALOG\_ROLE role, [18.5.5.9](reports.md)

Denial of Service (DoS) attacks

reports

System Resource Limits Report, [18.5.6.3](reports.md)

Tablespace Quotas Report, [18.5.9.6](reports.md)

Direct and Indirect System Privileges By Database Account Report, [18.5.2.2](reports.md)

Direct Object Privileges Report, [18.5.1.3](reports.md)

direct system privileges, [18.5.2.3](reports.md)

Direct System Privileges By Database Account Report, [18.5.2.1](reports.md)

disabling system features with Disabled default rule set, [5.2](cfrulset.md)

domains

defined with factors, [7.1](cfgfact.md)

finding database domain with DVF.F$DATABASE\_DOMAIN, [15.2.3](plsql_interfaces.md)

finding with DVF.F$DOMAIN, [15.2.8](plsql_interfaces.md)

DROP ROLE statement

monitoring, [17.3.1](monitoring.md)

DROP TABLE statement

monitoring, [17.2](monitoring.md)

DROP USER statement

monitoring, [17.3.1](monitoring.md)

dual key connection, dual key security

*See* two-person integrity (TPI)

DV\_ACCTMGR role

about, [11.2.12](db_objects.md)

adding to Data Dictionary realm, [3.3.2](getting_started.md)

DV\_ADMIN role

about, [11.2.3](db_objects.md)

changing password for user granted DV\_ADMIN, [11.2.3](db_objects.md)

DV\_AUDIT\_CLEANUP role

about, [11.2.6](db_objects.md)

changing password for user granted DV\_AUDIT\_CLEANUP, [11.2.6](db_objects.md)

Database Vault disabled, [11.2.6](db_objects.md)

GRANT and REVOKE operations affected by, [11.2.6](db_objects.md)

privileges associated with, [11.2.6](db_objects.md)

DV\_GOLDENGATE\_ADMIN role, [11.2.9](db_objects.md)

DV\_GOLDENGATE\_REDO\_ACCESS role, [11.2.10](db_objects.md)

DV\_MONITOR role, [11.2.4](db_objects.md)

DV\_OWNER role

about, [11.2.2](db_objects.md)

changing password for user granted DV\_OWNER, [11.2.2](db_objects.md)

DV\_PATCH\_ADMIN role, [11.2.11](db_objects.md)

privileges associated with, [11.2.11](db_objects.md)

DV\_PUBLIC role, [11.2.15](db_objects.md)

DV\_REALM\_OWNER role, [11.2.13](db_objects.md)

DV\_REALM\_RESOURCE role, [11.2.14](db_objects.md)

DV\_SECANALYST role

about, [11.2.5](db_objects.md)

changing password for user granted DV\_SECANALYST, [11.2.5](db_objects.md)

DV\_STREAMS\_ADMIN role, [11.2.7](db_objects.md)

DV\_XSTREAM\_ADMIN role, [11.2.8](db_objects.md)

DVA

*See* Oracle Database Vault Administrator

DVF account

auditing policy, [A.3](audplcy.md)

database accounts, [11.3](db_objects.md)

DVF schema, [15.2](plsql_interfaces.md)

about, [11.1.2](db_objects.md)

auditing policy, [A.3](audplcy.md)

DVSYS account, [11.3](db_objects.md)

auditing policy, [A.3](audplcy.md)

DVSYS schema

about, [11.1.1](db_objects.md)

auditing policy, [A.3](audplcy.md)

command rules, [6.4](cfcmdaut.md)

DV\_OWNER role, [11.2.2](db_objects.md)

factor validation methods, [7.3](cfgfact.md)

DVSYS.DBA\_DV\_CODE view, [16.2](views.md)

DVSYS.DBA\_DV\_COMMAND\_RULE view, [16.3](views.md)

DVSYS.DBA\_DV\_DATAPUMP\_AUTH view, [16.4](views.md)

DVSYS.DBA\_DV\_FACTOR view, [16.5](views.md)

DVSYS.DBA\_DV\_FACTOR\_LINK view, [16.6](views.md)

DVSYS.DBA\_DV\_FACTOR\_TYPE view, [16.7](views.md)

DVSYS.DBA\_DV\_IDENTITY view, [16.8](views.md)

DVSYS.DBA\_DV\_IDENTITY\_MAP view, [16.9](views.md)

DVSYS.DBA\_DV\_MAC\_POLICY view, [16.10](views.md)

DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR view, [16.11](views.md)

DVSYS.DBA\_DV\_POLICY\_LABEL view, [16.12](views.md)

DVSYS.DBA\_DV\_PUB\_PRIVS view, [16.13](views.md)

DVSYS.DBA\_DV\_REALM view, [16.14](views.md)

DVSYS.DBA\_DV\_REALM\_AUTH view, [16.15](views.md)

DVSYS.DBA\_DV\_REALM\_OBJECT view, [16.16](views.md)

DVSYS.DBA\_DV\_ROLE view, [16.17](views.md)

DVSYS.DBA\_DV\_RULE view, [16.18](views.md)

DVSYS.DBA\_DV\_RULE\_SET view, [16.19](views.md)

DVSYS.DBA\_DV\_RULE\_SET\_RULE view, [16.20](views.md)

DVSYS.DBA\_DV\_USER\_PRIVS view, [16.21](views.md)

DVSYS.DBA\_DV\_USER\_PRIVS\_ALL view, [16.22](views.md)

---

## E

email alert in rule set, [5.8.1](cfrulset.md)

enabling system features with Enabled default rule set, [5.2](cfrulset.md)

encrypted information, [18.5.9.5](reports.md)

enterprise identities, Enterprise\_Identity default factor, [7.2](cfgfact.md)

Enterprise Manager

*See* Oracle Enterprise Manager

errors

factor error options, [7.3](cfgfact.md)

rule set error options, [5.3](cfrulset.md)

event handler

rule sets, [5.3](cfrulset.md)

examples

.DBMS\_MACUTL constants, [14.2.2](apis_dbms_macutl.md)

realms, [4.12](cfrealms.md)

separation of duty matrix, [D.1.3](guidelines.md)

trace files, [E.1.7](troubleshooting.md)

*See also* tutorials

Execute Privileges to Strong SYS Packages Report, [18.5.3.1](reports.md)

EXECUTE\_CATALOG\_ROLE role, [18.5.5.9](reports.md)

impact of Oracle Database Vault installation, [2.4](dv_impact.md)

EXEMPT ACCESS POLICY system privilege, [18.5.5.3](reports.md)

exporting data

*See* Oracle Data Pump

external network services, fine-grained access to

example using email alert, [5.8.1](cfrulset.md)

---

## F

Factor Audit Report, [18.4.2.3](reports.md)

Factor Configuration Issues Report, [18.4.1.2](reports.md)

Factor Without Identities Report, [18.4.1.3](reports.md)

factors

about, [7.1](cfgfact.md)

assignment, [7.3](cfgfact.md)

disabled rule set, [18.4.1.2](reports.md)

incomplete rule set, [18.4.1.2](reports.md)

validate, [7.3](cfgfact.md)

assignment operation, [18.4.2.3](reports.md)

audit events, custom, [A.1.1](audplcy.md)

audit options, [7.3](cfgfact.md)

child factors

about, [7.3](cfgfact.md)

Factor Configuration Issues Report, [18.4.1.2](reports.md)

mapping, [7.5.3](cfgfact.md), [7.5.3](cfgfact.md)

creating, [7.3](cfgfact.md)

creating names, [7.3](cfgfact.md)

data dictionary views, [7.12](cfgfact.md)

DBMS\_MACUTL constants, example of, [14.2.2](apis_dbms_macutl.md)

default factors, [7.2](cfgfact.md), [7.2](cfgfact.md)

default factors not showing in Database Vault Administrator, [C.1](dvca.md)

deleting, [7.6](cfgfact.md)

domain, finding with DVF.F$DOMAIN, [15.2.8](plsql_interfaces.md)

editing, [7.4](cfgfact.md)

error options, [7.3](cfgfact.md)

evaluate, [7.3](cfgfact.md)

evaluation operation, [18.4.2.3](reports.md)

factor type

about, [7.3](cfgfact.md)

selecting, [7.3](cfgfact.md)

factor-identity pair mapping, [7.5.3](cfgfact.md)

functionality, [7.7](cfgfact.md)

functions

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

DBMS\_MACUTL constants (fields), [14.2.1](apis_dbms_macutl.md)

guidelines, [7.10](cfgfact.md)

identifying using child factors, [7.5.3](cfgfact.md)

identities

about, [7.3](cfgfact.md), [7.5.1](cfgfact.md)

adding to factor, [7.5](cfgfact.md)

assigning, [7.3](cfgfact.md)

configuring, [7.5.2](cfgfact.md)

creating, [7.5.2](cfgfact.md)

data dictionary views, [7.12](cfgfact.md)

database session, [7.3](cfgfact.md)

deleting, [7.5.2](cfgfact.md)

determining with DVSYS.GET\_FACTOR, [7.3](cfgfact.md)

editing, [7.5.2](cfgfact.md)

enterprise-wide users, [15.2.8](plsql_interfaces.md)

how factor identities work, [7.3](cfgfact.md)

labels, [7.3](cfgfact.md), [7.5.2](cfgfact.md)

mapping, about, [7.5.3](cfgfact.md)

mapping, identified, [7.3](cfgfact.md)

mapping, procedure, [7.5.3](cfgfact.md)

mapping, tutorial, [7.9.1](cfgfact.md)

Oracle Label Security labels, [7.3](cfgfact.md)

reports, [7.12](cfgfact.md)

resolving, [7.3](cfgfact.md)

retrieval methods, [7.3](cfgfact.md)

setting dynamically, [15.1.1](plsql_interfaces.md)

trust levels, [7.3](cfgfact.md), [7.5.2](cfgfact.md)

with Oracle Label Security, [7.3](cfgfact.md)

initialization, command rules, [6.1](cfcmdaut.md)

invalid audit options, [18.4.1.2](reports.md)

label, [18.4.1.2](reports.md)

naming conventions, [7.3](cfgfact.md)

Oracle Virtual Private Database, attaching factors to, [9.3](dv_ols.md)

parent factors, [7.3](cfgfact.md)

performance effect, [7.11](cfgfact.md)

procedures

DBMS\_MACADM (configuration), [12.5](apis_dbms_macadm.md)

process flow, [7.7](cfgfact.md)

propagating policies to other databases, [10.1.2](dba.md)

reports, [7.12](cfgfact.md)

retrieving, [7.7.2](cfgfact.md)

retrieving with DVSYS.GET\_FACTOR, [15.1.2](plsql_interfaces.md)

setting, [7.7.3](cfgfact.md)

setting with DVSYS.SET\_FACTOR, [15.1.1](plsql_interfaces.md)

troubleshooting

auditing report, [18.4.2.3](reports.md)

configuration problems, [E.3](troubleshooting.md)

tips, [E.2](troubleshooting.md)

type (category of factor), [7.3](cfgfact.md)

validating, [7.3](cfgfact.md)

values (identities), [7.1](cfgfact.md)

views

DVSYS.DBA\_DV\_CODE, [16.2](views.md)

DVSYS.DBA\_DV\_FACTOR\_LINK, [16.6](views.md)

DVSYS.DBA\_DV\_FACTOR\_TYPE, [16.7](views.md)

DVSYS.DBA\_DV\_IDENTITY, [16.8](views.md)

DVSYS.DBA\_DV\_IDENTITY\_MAP, [16.9](views.md)

DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR, [16.11](views.md)

ways to assign, [7.3](cfgfact.md)

rule sets

selecting, [7.3](cfgfact.md)

used with, [7.1](cfgfact.md)

features, new

*See* new features

functions

command rules

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

DVSYS schema enabling, [15.1](plsql_interfaces.md)

factors

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

Oracle Label Security policy

DBMS\_MACADM (configuration), [12.7](apis_dbms_macadm.md)

realms

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

rule sets

.DBMS\_MACADM (configuration), [12.3](apis_dbms_macadm.md)

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

PL/SQL functions for inspecting SQL, [15.3](plsql_interfaces.md)

secure application roles

DBMS\_MACADM (configuration), [12.6](apis_dbms_macadm.md)

DBMS\_MACSEC\_ROLES (configuration), [13.1](apis_macsec_roles.md)

.DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

---

## G

general security reports, [18.5](reports.md)

GRANT statement

monitoring, [17.3.1](monitoring.md)

guidelines

ALTER SESSION privilege, [D.6.6](guidelines.md)

ALTER SYSTEM privilege, [D.6.6](guidelines.md)

command rules, [6.8](cfcmdaut.md)

CREATE ANY JOB privilege, [D.6.3](guidelines.md)

CREATE EXTERNAL JOB privilege, [D.6.4](guidelines.md)

CREATE JOB privilege, [D.6.3](guidelines.md)

DBMS\_FILE\_TRANSFER package, [D.6.1](guidelines.md)

factors, [7.10](cfgfact.md)

general security, [D](guidelines.md)

LogMiner packages, [D.6.5](guidelines.md)

managing DV\_OWNER and DV\_ACCTMGR accounts, [11.3](db_objects.md)

operating system access, [D.2.4](guidelines.md)

Oracle software owner, [D.4.2](guidelines.md)

performance effect, [7.11](cfgfact.md)

realms, [4.14](cfrealms.md)

recycle bin, [D.6.2](guidelines.md)

root access, [D.2.4](guidelines.md)

root user access, [D.4.1](guidelines.md)

rule sets, [5.10](cfrulset.md)

secure application roles, [8.3](cfseappr.md)

SYSDBA access, [D.4.3](guidelines.md)

SYSDBA privilege, limiting, [D.2.3](guidelines.md)

SYSOPER access, [D.4.4](guidelines.md)

SYSTEM schema and application tables, [D.2.2](guidelines.md)

SYSTEM user account, [D.2.1](guidelines.md)

trusted accounts and roles, [D.3](guidelines.md)

using Database Vault in a production environment, [D.5](guidelines.md)

UTL\_FILE package, [D.6.1](guidelines.md)

---

## H

hackers

*See* security attacks

Hierarchical System Privileges by Database Account Report, [18.5.2.3](reports.md)

host names

finding with DVF.F$DATABASE\_HOSTNAME, [15.2.4](plsql_interfaces.md)

---

## I

identities

*See* factors, identities

Identity Configuration Issues Report, [18.4.1.4](reports.md)

IDLE\_TIME resource profile, [18.5.6.2](reports.md)

IMP\_FULL\_DATABASE role

impact of Oracle Database Vault installation, [2.4](dv_impact.md)

importing data

*See* Oracle Data Pump

incomplete rule set, [18.4.1.2](reports.md)

role enablement, [18.4.1.7](reports.md)

initialization parameters

Allow System Parameters default rule set, [5.2](cfrulset.md)

modified after installation, [2.1](dv_impact.md)

modified by Oracle Database Vault, [2.1](dv_impact.md)

reports, [18.5.6](reports.md)

insider threats

*See* intruders

installations

security considerations, [D.6](guidelines.md)

intruders

*See* security attacks

IP addresses

Client\_IP default factor, [7.2](cfgfact.md)

defined with factors, [7.1](cfgfact.md)

---

## J

Java Policy Grants Report, [18.5.9.1](reports.md)

jobs, scheduling

*See* scheduling database jobs

---

## L

Label Security Integration Audit Report, [18.4.2.4](reports.md)

labels

about, [7.5.2](cfgfact.md)

*See also* Oracle Label Security

languages

adding to Oracle Database Vault, [C.6](dvca.md)

consistency between Oracle Database and operating system, [C.1](dvca.md)

finding with DVF.F$LANG, [15.2.11](plsql_interfaces.md)

finding with DVF.F$LANGUAGE, [15.2.12](plsql_interfaces.md)

name

Lang default factor, [7.2](cfgfact.md)

Language default factor, [7.2](cfgfact.md)

LBACSYS account

about, [11.3](db_objects.md)

auditing policy, [A.3](audplcy.md)

factor integration with OLS policy requirement, [9.4.3](dv_ols.md)

*See also* Oracle Label Security

LBACSYS schema

auditing policy, [A.3](audplcy.md)

locked out accounts, solution for, [B.1](dvdisabl.md)

log files

Database Vault log files, [A.1.2](audplcy.md)

location for Oracle Database logs, [3.2.2](getting_started.md)

logging on

Oracle Database Vault

Oracle Database Vault Owner account, [3.2.2](getting_started.md)

reports, Core Database Audit Report, [18.5.8](reports.md)

LogMiner packages

guidelines, [D.6.5](guidelines.md)

---

## M

maintenance on Oracle Database Vault, [B.1](dvdisabl.md)

managing user accounts and profiles

Can Maintain Accounts/Profiles default rule set, [5.2](cfrulset.md)

managing user accounts and profiles on own account, Can Maintain Own Accounts default rule set, [5.2](cfrulset.md)

mapping identities, [7.5.3](cfgfact.md)

monitoring

accessibility features, enabling, [C.4.2](dvca.md)

activities, [17](monitoring.md)

textual representation in charts, enabling, [C.4.2](dvca.md)

My Oracle Support, [7.8.3](cfgfact.md)

about, [Preface](preface.md)

---

## N

naming conventions

factors, [7.3](cfgfact.md)

realms, [4.3](cfrealms.md)

rule sets, [5.3](cfrulset.md)

rules, [5.5.1](cfrulset.md)

network protocol

finding with DVF.F$NETWORK\_PROTOCOL, [15.2.14](plsql_interfaces.md)

network protocol, Network\_Protocol default factor, [7.2](cfgfact.md)

new features, [Preface](whatsnew.md)

NOAUDIT statement

monitoring, [17.3.1](monitoring.md)

Non-Owner Object Trigger Report, [18.5.9.7](reports.md)

nonsystem database accounts, [18.5.1.3](reports.md)

---

## O

Object Access By PUBLIC Report, [18.5.1.1](reports.md)

Object Access Not By PUBLIC Report, [18.5.1.2](reports.md)

Object Dependencies Report, [18.5.1.4](reports.md)

object owners

nonexistent, [18.4.1.1](reports.md)

reports

Command Rule Configuration Issues Report, [18.4.1.1](reports.md)

object privilege reports, [18.5.1](reports.md)

objects

command rule objects

name, [6.4](cfcmdaut.md)

owner, [6.4](cfcmdaut.md)

processing, [6.6](cfcmdaut.md)

dynamic SQL use, [18.5.9.3](reports.md)

monitoring, [17.3.1](monitoring.md)

object names

finding with DVSYS.DV\_DICT\_OBJ\_NAME, [15.3.7](plsql_interfaces.md)

object owners

finding with DVSYS.DV\_DICT\_OBJ\_OWNER, [15.3.6](plsql_interfaces.md)

realms

object name, [4.5](cfrealms.md)

object owner, [4.5](cfrealms.md)

object type, [4.5](cfrealms.md)

procedures for registering, [12.2](apis_dbms_macadm.md)

reports

Access to Sensitive Objects Report, [18.5.3.2](reports.md)

Accounts with SYSDBA/SYSOPER Privilege Report, [18.5.3.4](reports.md)

Direct Object Privileges Report, [18.5.1.3](reports.md)

Execute Privileges to Strong SYS Packages Report, [18.5.3.1](reports.md)

Non-Owner Object Trigger Report, [18.5.9.7](reports.md)

Object Access By PUBLIC Report, [18.5.1.1](reports.md)

Object Access Not By PUBLIC Report, [18.5.1.2](reports.md)

Object Dependencies Report, [18.5.1.4](reports.md)

Objects Dependent on Dynamic SQL Report, [18.5.9.3](reports.md)

OS Directory Objects Report, [18.5.9.2](reports.md)

privilege, [18.5.1](reports.md)

Public Execute Privilege To SYS PL/SQL Procedures Report, [18.5.3.3](reports.md)

sensitive, [18.5.3](reports.md)

System Privileges By Privilege Report, [18.5.2.5](reports.md)

types

finding with DVSYS.DV\_DICT\_OBJ\_TYPE, [15.3.5](plsql_interfaces.md)

views, DVSYS.DBA\_DV\_REALM\_OBJECT, [16.16](views.md)

*See also* database objects

Objects Dependent on Dynamic SQL Report, [18.5.9.3](reports.md)

OEM

*See* Oracle Enterprise Manager (OEM)

OLS

*See* Oracle Label Security

operating system access

guideline for using with Database Vault, [D.2.4](guidelines.md)

operating systems

reports

OS Directory Objects Report, [18.5.9.2](reports.md)

OS Security Vulnerability Privileges Report, [18.5.5.11](reports.md)

vulnerabilities, [18.5.5.11](reports.md)

ORA-00942 error, [8.6.7](cfseappr.md)

ORA-01031 error, [5.3](cfrulset.md)

ORA-01301 error, [10.8.1](dba.md)

ORA-06512 error, [5.8.4](cfrulset.md), [14.3.1](apis_dbms_macutl.md)

ORA-24247 error, [5.8.4](cfrulset.md)

ORA-47305 error, [8.6.7](cfseappr.md)

ORA-47400 error, [5.8.6](cfrulset.md), [10.8.1](dba.md)

ORA-47401 error, [4.10](cfrealms.md), [10.8.1](dba.md)

ORA-47408 error, [10.8.1](dba.md)

ORA-47409 error, [10.8.1](dba.md)

ORA-47920 error, [14.3.1](apis_dbms_macutl.md)

Oracle Data Guard

using with Oracle Database Vault, [9](dv_ols.md)

Oracle Data Pump

Allow Oracle Data Pump Operation rule set, [5.2](cfrulset.md)

archiving the Oracle Database Vault audit trail with, [A.2](audplcy.md)

DVSYS.DBA\_DV\_DATAPUMP\_AUTH view, [16.4](views.md)

DVSYS.MACADM procedures for authorization, [12.8.2](apis_dbms_macadm.md)

granting authorization to use with Database Vault, [10.2.2](dba.md)

guidelines before performing an export or import, [10.2.3](dba.md)

revoking authorization from using with Database Vault, [10.2.4](dba.md)

using with Oracle Database Vault, [10.2.1](dba.md)

Oracle database

*See* databases

Oracle Database Vault

about, [1.1](dvintro.md)

components, [1.2](dvintro.md), [1.2.1](dvintro.md)

deinstalling, [C.7](dvca.md)

disabling

checking if disabled, [B.2](dvdisabl.md)

procedures for, [B](dvdisabl.md)

reasons for, [B.1](dvdisabl.md)

enabling

checking if enabled, [B.2](dvdisabl.md)

procedures for, [B](dvdisabl.md)

frequently asked questions, [1.1](dvintro.md)

integrating with other Oracle products, [9](dv_ols.md)

maintenance, [B.1](dvdisabl.md)

Oracle Database installation, affect on, [2](dv_impact.md)

post-installation procedures, [C](dvca.md)

registering, [3.1](getting_started.md)

reinstalling, [C.8](dvca.md)

Oracle Database Vault Administrator

starting, [3.2](getting_started.md)

starting without Oracle Enterprise Manager, [3.2.2](getting_started.md)

Oracle Database Vault Administrator (DVA)

accessibility features, enabling, [C.4](dvca.md)

accessibility mode, [C.4.1](dvca.md)

configuring users to access from Database Control, [3.2.1.3](getting_started.md)

deploying manually

to Database Console OC4J container, [C.2.2](dvca.md)

to standalone OC4J container, [C.2.1](dvca.md)

logging into from Oracle Enterprise Manager Database Control, [3.2.1.3](getting_started.md)

logging on, [3.2](getting_started.md)

logging on from Oracle Enterprise Manager Grid Control, [3.2.1.2](getting_started.md)

logging on without Oracle Enterprise Manager, [3.2.2](getting_started.md)

textual representation in charts, [C.4.2](dvca.md)

time-out value, [C.3](dvca.md)

Oracle Database Vault Owner account

example of logging on with, [3.2.2](getting_started.md)

Oracle Enterprise Manager

DBSNMP account

changing password, [10.1.5](dba.md)

granted DV\_MONITOR role, [11.2.4](db_objects.md)

realm for, [4.2](cfrealms.md)

default realm used for, [4.2](cfrealms.md)

performance tools, [4.15](cfrealms.md)

setting URL for Database Vault Administrator, [10.1.1](dba.md)

SYSMAN account

realm for, [4.2](cfrealms.md)

using Oracle Database Vault with, [10.1](dba.md)

Oracle Enterprise Manager Database Control

configuring users for Database Vault Administrator, [3.2.1.3](getting_started.md)

starting Database Vault Administrator from, [3.2.1.3](getting_started.md)

starting Oracle Database Vault from, [3.2.1.1](getting_started.md)

Oracle Enterprise Manager Grid Control

monitoring Database Vault for attempted violations, [11.2.4](db_objects.md)

propagating Database Vault policies to other databases, [10.1.2](dba.md)

starting Oracle Database Vault from, [3.2.1.2](getting_started.md)

Oracle Enterprise User Security, integrating with Oracle Database Vault, [9.1](dv_ols.md)

Oracle GoldenGate

Database Vault role used for

DV\_GOLDENGATE\_ADMIN, [11.2.9](db_objects.md)

DV\_GOLDENGATE\_REDO\_ACCESS, [11.2.10](db_objects.md)

in an Oracle Database Vault environment, [10.7](dba.md)

Oracle Internet Directory Distinguished Name, Proxy\_Enterprise\_Identity default factor, [7.2](cfgfact.md)

Oracle Label Security (OLS)

audit events, custom, [A.1.1](audplcy.md)

checking if installed using DBMS\_MACUTL functions, [14.3](apis_dbms_macutl.md)

data dictionary views, [9.4.5](dv_ols.md)

database option, [1.2.5](dvintro.md)

functions

DBMS\_MACUTL (utility), [14.2.1](apis_dbms_macutl.md)

how Database Vault integrates with, [9.4.1](dv_ols.md)

initialization, command rules, [6.1](cfcmdaut.md)

integration with Oracle Database Vault

example, [9.4.4.1](dv_ols.md)

Label Security Integration Audit Report, [18.4.2.4](reports.md), [18.4.2.4](reports.md)

procedure, [9.4.3](dv_ols.md)

requirements, [9.4.2](dv_ols.md)

labels

about, [7.5.2](cfgfact.md)

determining with GET\_FACTOR\_LABEL, [15.1.6](plsql_interfaces.md)

invalid label identities, [18.4.1.4](reports.md)

policies

accounts that bypass, [18.5.5.3](reports.md)

monitoring policy changes, [17.3.1](monitoring.md)

nonexistent, [18.4.1.2](reports.md)

Oracle Policy Manager, [1.2.5](dvintro.md)

procedures

DBMS\_MACADM (configuration), [12.7](apis_dbms_macadm.md)

reports, [9.4.5](dv_ols.md)

views

DVSYS.DBA\_DV\_MAC\_POLICY, [16.10](views.md)

DVSYS.DBA\_DV\_MAC\_POLICY\_FACTOR, [16.11](views.md)

DVSYS.DBA\_DV\_POLICY\_LABEL, [16.12](views.md)

*See also* LBACSYS account

Oracle MetaLink

*See* My Oracle Support

Oracle Policy Manager

used with Oracle Label Security, [1.2.5](dvintro.md)

Oracle Real Application Clusters

compatibility with Oracle Database Vault, [1.1](dvintro.md)

configuring Database Vault on RAC nodes, [C.5](dvca.md)

deinstalling Oracle Database Vault from, [C.7](dvca.md)

multiple factor identities, [7.3](cfgfact.md)

Oracle Recovery Manager (RMAN)

in an Oracle Database Vault environment, [10.4](dba.md)

Oracle software owner, guidelines on managing, [D.4.2](guidelines.md)

Oracle Streams

Database Vault role used for, [11.2.7](db_objects.md)

in an Oracle Database Vault environment, [10.5](dba.md)

Oracle Virtual Private Database (VPD)

accounts that bypass, [18.5.5.3](reports.md)

factors, attaching to, [9.3](dv_ols.md)

GRANT EXECUTE privileges with Grant VPD Administration default rule set, [5.2](cfrulset.md)

using Database Vault factors with Oracle Label Security, [9.4.4.1](dv_ols.md)

OS Directory Objects Report, [18.5.9.2](reports.md)

OS Security Vulnerability Privileges Report, [18.5.5.11](reports.md)

OS\_ROLES initialization parameter, [2.1](dv_impact.md)

---

## P

parameters

modified after installation, [2.1](dv_impact.md)

reports

Security Related Database Parameters Report, [18.5.6.1](reports.md)

parent factors

*See* factors

Password History Access Report, [18.5.5.6](reports.md)

passwords

forgotten, solution for, [B.1](dvdisabl.md)

reports, [18.5.7](reports.md)

Database Account Default Password Report, [18.5.7.1](reports.md)

Password History Access Report, [18.5.5.6](reports.md)

Username/Password Tables Report, [18.5.9.5](reports.md)

patches

DV\_PATCH\_ADMIN requirement for, [11.2.11](db_objects.md)

security consideration, [D.6](guidelines.md)

two-person integrity used for, [5.9.1](cfrulset.md)

performance effect

command rules, [6.9](cfcmdaut.md)

realms, [4.15](cfrealms.md)

reports

Resource Profiles Report, [18.5.6.2](reports.md)

System Resource Limits Report, [18.5.6.3](reports.md)

rule sets, [5.11](cfrulset.md)

secure application roles, [8.7](cfseappr.md)

static evaluation for rule sets, [5.11](cfrulset.md)

performance tools

Database Control, realms, [4.15](cfrealms.md)

Oracle Enterprise Manager

command rules, [6.9](cfcmdaut.md)

factors, [7.11](cfgfact.md)

realms, [4.15](cfrealms.md)

rule sets, [5.11](cfrulset.md)

secure application roles, [8.7](cfseappr.md)

Oracle Enterprise Manager Database Control

command rules, [6.9](cfcmdaut.md)

factors, [7.11](cfgfact.md)

rule sets, [5.11](cfrulset.md)

secure application roles, [8.7](cfseappr.md)

STATSPACK utility

command rules, [6.9](cfcmdaut.md)

factors, [7.11](cfgfact.md)

realms, [4.15](cfrealms.md)

rule sets, [5.11](cfrulset.md)

secure application roles, [8.7](cfseappr.md)

TKPROF utility

command rules, [6.9](cfcmdaut.md)

factors, [7.11](cfgfact.md)

realms, [4.15](cfrealms.md)

rule sets, [5.11](cfrulset.md)

secure application roles, [8.7](cfseappr.md)

PL/SQL

packages

summarized, [15.4](plsql_interfaces.md)

unwrapped bodies, [18.5.9.4](reports.md)

Unwrapped PL/SQL Package Bodies Report, [18.5.9.4](reports.md)

PL/SQL factor functions, [15.2](plsql_interfaces.md)

policy changes, monitoring, [17.3.1](monitoring.md), [17.4](monitoring.md)

port number

finding, [3.2.1.3](getting_started.md), [3.2.2](getting_started.md)

Oracle Database Vault, [3.2.1.3](getting_started.md), [3.2.2](getting_started.md)

post-installation procedures, [C](dvca.md)

privileges

ANY privileges, [11.2.12](db_objects.md)

existing users and roles, Database Vault affect on, [2.4](dv_impact.md)

least privilege principle

violations to, [18.5.9.1](reports.md)

monitoring

GRANT statement, [17.3.1](monitoring.md)

REVOKE statement, [17.3.1](monitoring.md)

Oracle Database Vault restricting, [2.2](dv_impact.md)

prevented from existing users and roles, [2.5](dv_impact.md)

reports

Accounts With DBA Roles Report, [18.5.5.2](reports.md)

ALTER SYSTEM or ALTER SESSION Report, [18.5.5.5](reports.md)

ANY System Privileges for Database Accounts Report, [18.5.2.4](reports.md)

AUDIT Privileges Report, [18.5.5.10](reports.md)

Database Accounts With Catalog Roles Report, [18.5.5.9](reports.md)

Direct and Indirect System Privileges By Database Account Report, [18.5.2.2](reports.md)

Direct System Privileges By Database Account Report, [18.5.2.1](reports.md)

Hierarchical System Privileges By Database Account Report, [18.5.2.3](reports.md)

listed, [18.5.4](reports.md)

OS Directory Objects Report, [18.5.9.2](reports.md)

Privileges Distribution By Grantee Report, [18.5.4.1](reports.md)

Privileges Distribution By Grantee, Owner Report, [18.5.4.2](reports.md)

Privileges Distribution By Grantee, Owner, Privilege Report, [18.5.4.3](reports.md)

WITH ADMIN Privilege Grants Report, [18.5.5.1](reports.md)

WITH GRANT Privileges Report, [18.5.5.7](reports.md)

roles

checking with DBMS\_MACUTL.USER\_HAS\_ROLE\_VARCHAR function, [14.3](apis_dbms_macutl.md)

system

checking with DBMS\_MACUTL.USER\_HAS\_SYSTEM\_PRIVILEGE function, [14.3](apis_dbms_macutl.md)

views

DVSYS.DBA\_DV\_PUB\_PRIVS, [16.13](views.md)

DVSYS.DBA\_DV\_USER\_PRIVS, [16.21](views.md)

DVSYS.DBA\_DV\_USER\_PRIVS\_ALL, [16.22](views.md)

Privileges Distribution By Grantee Report, [18.5.4.1](reports.md)

Privileges Distribution By Grantee, Owner Report, [18.5.4.2](reports.md)

Privileges Distribution By Grantee, Owner, Privilege Report, [18.5.4.3](reports.md)

privileges using external password, [18.5.3.4](reports.md)

problems, diagnosing, [E.1.1](troubleshooting.md)

procedures

command rules

DBMS\_MACADM (configuration), [12.4](apis_dbms_macadm.md)

factors

DBMS\_MACADM (configuration), [12.5](apis_dbms_macadm.md)

realms

.DBMS\_MACADM (configuration), [12.2](apis_dbms_macadm.md)

production environments

guidelines for securing, [D.5](guidelines.md)

profiles, [18.5.6](reports.md)

PUBLIC access to realms, [4.9](cfrealms.md)

Public Execute Privilege To SYS PL/SQL Procedures Report, [18.5.3.3](reports.md)

PUBLIC user account

impact of Oracle Database Vault installation, [2.4](dv_impact.md)

---

## Q

quotas

tablespace, [18.5.9.6](reports.md)

---

## R

RAC

*See* Oracle Real Application Clusters

Realm Audit Report, [18.4.2.1](reports.md)

Realm Authorization Configuration Issues Report, [18.4.1.5](reports.md)

realms

about, [4.1](cfrealms.md)

adding roles to as grantees, [4.14](cfrealms.md)

audit events, custom, [A.1.1](audplcy.md)

authentication-related procedures, [12.2](apis_dbms_macadm.md)

authorization

enabling access to realm-protected objects, [4.11](cfrealms.md)

how realm authorizations work, [4.10](cfrealms.md)

process flow, [4.10](cfrealms.md)

troubleshooting, [E.2](troubleshooting.md)

updating with DBMS\_MACADM.UPDATE\_REALM\_AUTH, [12.2](apis_dbms_macadm.md)

authorizations

grantee, [4.6](cfrealms.md)

rule set, [4.6](cfrealms.md)

creating, [4.3](cfrealms.md)

creating names, [4.3](cfrealms.md)

data dictionary views, [4.16](cfrealms.md)

data masking, [10.8.3](dba.md)

DBMS\_MACUTL constants, example of, [14.2.2](apis_dbms_macutl.md)

default realms

listed, [4.2](cfrealms.md)

default realms not showing in Database Vault Administrator, [C.1](dvca.md)

deleting, [4.8](cfrealms.md)

disabling, [4.7](cfrealms.md)

DV\_REALM\_OWNER role, [11.2.13](db_objects.md)

DV\_REALM\_RESOURCE role, [11.2.14](db_objects.md)

editing, [4.4](cfrealms.md)

effect on other Oracle Database Vault components, [4.13](cfrealms.md)

enabling, [4.7](cfrealms.md)

enabling access to realm-protected objects, [4.11](cfrealms.md)

example, [4.12](cfrealms.md)

functions

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

DBMS\_MACUTL constants (fields), [14.2.1](apis_dbms_macutl.md)

guidelines, [4.14](cfrealms.md)

how realms work, [4.9](cfrealms.md)

naming conventions, [4.3](cfrealms.md)

object-related procedures, [12.2](apis_dbms_macadm.md)

performance effect, [4.15](cfrealms.md)

procedures

DBMS\_MACADM (configuration), [12.2](apis_dbms_macadm.md), [12.2](apis_dbms_macadm.md)

process flow, [4.9](cfrealms.md)

propagating policies to other databases, [10.1.2](dba.md)

protection after object is dropped, [4.14](cfrealms.md)

PUBLIC access, [4.9](cfrealms.md)

realm authorizations

about, [4.6](cfrealms.md)

realm secured objects

deleting, [4.5](cfrealms.md)

editing, [4.5](cfrealms.md)

object name, [4.5](cfrealms.md)

object owner, [4.5](cfrealms.md)

object type, [4.5](cfrealms.md)

realm system authorizations

creating, [4.6](cfrealms.md)

deleting, [4.6](cfrealms.md)

editing, [4.6](cfrealms.md)

realm-secured objects, [4.5](cfrealms.md)

reports, [4.16](cfrealms.md)

roles

DV\_REALM\_OWNER, [11.2.13](db_objects.md)

DV\_REALM\_RESOURCE, [11.2.14](db_objects.md)

secured object, [18.4.1.5](reports.md)

territory a realm protects, [4.5](cfrealms.md)

troubleshooting, [E.2](troubleshooting.md), [E.3](troubleshooting.md)

tutorial, [3.3.1](getting_started.md)

updating with DBMS\_MACADM.UPDATE\_REALM, [12.2](apis_dbms_macadm.md)

views

DVSYS.DBA\_DV\_CODE, [16.2](views.md)

DVSYS.DBA\_DV\_REALM, [16.14](views.md)

DVSYS.DBA\_DV\_REALM\_AUTH, [16.15](views.md)

DVSYS.DBA\_DV\_REALM\_OBJECT, [16.16](views.md), [16.16](views.md)

*See also* rule sets

RECOVERY\_CATALOG\_OWNER role, [18.5.5.9](reports.md)

recycle bin, guidelines on managing, [D.6.2](guidelines.md)

RECYCLEBIN initialization parameter

default setting in Oracle Database Vault, [2.1](dv_impact.md)

security considerations, [D.6.2](guidelines.md)

registering Oracle Database Vault, [3.1](getting_started.md)

reinstalling Oracle Database Vault, [C.8](dvca.md)

REMOTE\_LOGIN\_PASSWORDFILE initialization parameter, [2.1](dv_impact.md)

reporting menu

report results page, [18.3](reports.md)

parameter, [18.3](reports.md)

reports

about, [18.1](reports.md)

Access to Sensitive Objects Report, [18.5.3.2](reports.md)

Accounts With DBA Roles Report, [18.5.5.2](reports.md)

Accounts with SYSDBA/SYSOPER Privilege Report, [18.5.3.4](reports.md)

ALTER SYSTEM or ALTER SESSION Report, [18.5.5.5](reports.md)

ANY System Privileges for Database Accounts Report, [18.5.2.4](reports.md)

AUDIT Privileges Report, [18.5.5.10](reports.md)

auditing, [18.4.2](reports.md)

BECOME USER Report, [18.5.5.4](reports.md)

categories of, [18.1](reports.md)

Command Rule Audit Report, [18.4.2.2](reports.md)

Command Rule Configuration Issues Report, [18.4.1.1](reports.md)

Core Database Audit Report, [18.5.8](reports.md)

Core Database Vault Audit Trail Report, [18.4.2.5](reports.md)

Database Account Default Password Report, [18.5.7.1](reports.md)

Database Account Status Report, [18.5.7.2](reports.md)

Database Accounts With Catalog Roles Report, [18.5.5.9](reports.md)

Direct and Indirect System Privileges By Database Account Report, [18.5.2.2](reports.md)

Direct Object Privileges Report, [18.5.1.3](reports.md)

Direct System Privileges By Database Account Report, [18.5.2.1](reports.md)

Enterprise Manager Grid Control, [10.1.4](dba.md)

Execute Privileges to Strong SYS Packages Report, [18.5.3.1](reports.md)

Factor Audit Report, [18.4.2.3](reports.md)

Factor Configuration Issues Report, [18.4.1.2](reports.md)

Factor Without Identities, [18.4.1.3](reports.md)

general security, [18.5](reports.md)

Hierarchical System Privileges by Database Account Report, [18.5.2.3](reports.md)

Identity Configuration Issues Report, [18.4.1.4](reports.md)

Java Policy Grants Report, [18.5.9.1](reports.md)

Label Security Integration Audit Report, [18.4.2.4](reports.md)

Non-Owner Object Trigger Report, [18.5.9.7](reports.md)

Object Access By PUBLIC Report, [18.5.1.1](reports.md)

Object Access Not By PUBLIC Report, [18.5.1.2](reports.md)

Object Dependencies Report, [18.5.1.4](reports.md)

Objects Dependent on Dynamic SQL Report, [18.5.9.3](reports.md)

OS Directory Objects Report, [18.5.9.2](reports.md)

OS Security Vulnerability Privileges, [18.5.5.11](reports.md)

Password History Access Report, [18.5.5.6](reports.md)

permissions for running, [18.2](reports.md)

privilege management, [18.5.4](reports.md)

Privileges Distribution By Grantee Report, [18.5.4.1](reports.md)

Privileges Distribution By Grantee, Owner Report, [18.5.4.2](reports.md)

Privileges Distribution By Grantee, Owner, Privilege Report, [18.5.4.3](reports.md)

Public Execute Privilege To SYS PL/SQL Procedures Report, [18.5.3.3](reports.md)

Realm Audit Report, [18.4.2.1](reports.md)

Realm Authorization Configuration Issues Report, [18.4.1.5](reports.md)

Resource Profiles Report, [18.5.6.2](reports.md)

Roles/Accounts That Have a Given Role Report, [18.5.5.8](reports.md)

Rule Set Configuration Issues Report, [18.4.1.6](reports.md)

running, [18.3](reports.md)

Secure Application Configuration Issues Report, [18.4.1.7](reports.md)

Secure Application Role Audit Report, [18.4.2.6](reports.md)

Security Policy Exemption Report, [18.5.5.3](reports.md)

Security Related Database Parameters, [18.5.6.1](reports.md)

security vulnerability, [18.5.9](reports.md)

System Privileges By Privilege Report, [18.5.2.5](reports.md)

System Resource Limits Report, [18.5.6.3](reports.md)

Tablespace Quotas Report, [18.5.9.6](reports.md)

Unwrapped PL/SQL Package Bodies Report, [18.5.9.4](reports.md)

Username /Password Tables Report, [18.5.9.5](reports.md)

WITH ADMIN Privileges Grants Report, [18.5.5.1](reports.md)

WITH GRANT Privileges Report, [18.5.5.7](reports.md)

required parameters page

Resource Profiles Report, [18.5.6.2](reports.md)

resources

reports

Resource Profiles Report, [18.5.6.2](reports.md)

System Resource Limits Report, [18.5.6.3](reports.md)

REVOKE statement

monitoring, [17.3.1](monitoring.md)

roles

adding to realms as grantees, [4.14](cfrealms.md)

catalog-based, [18.5.5.9](reports.md)

Database Vault default roles, [11.2.1](db_objects.md)

privileges, checking with DBMS\_MACUTL.USER\_HAS\_ROLE\_VARCHAR function, [14.3](apis_dbms_macutl.md)

role enablement in incomplete rule set, [18.4.1.7](reports.md)

role-based system privileges, [18.5.2.3](reports.md)

*See also* secure application roles

Roles/Accounts That Have a Given Role Report, [18.5.5.8](reports.md)

root access

guideline for using with Database Vault, [D.2.4](guidelines.md)

root access, guidelines on managing, [D.4.1](guidelines.md)

Rule Set Configuration Issues Report, [18.4.1.6](reports.md)

rule sets

about, [5.1](cfrulset.md)

adding existing rules, [5.5.2](cfrulset.md)

audit options, [5.3](cfrulset.md)

command rules

disabled, [18.4.1.1](reports.md)

selecting for, [6.4](cfcmdaut.md)

used with, [6.1](cfcmdaut.md)

CONNECT role configured incorrectly, solution for, [B.1](dvdisabl.md)

creating, [5.3](cfrulset.md)

rules in, [5.5.1](cfrulset.md)

creating names, [5.3](cfrulset.md)

data dictionary views, [5.12](cfrulset.md)

DBMS\_MACUTL constants, example of, [14.2.2](apis_dbms_macutl.md)

default rule sets, [5.2](cfrulset.md)

default rule sets not showing in Database Vault Administrator, [C.1](dvca.md)

deleting

rule set, [5.6](cfrulset.md)

rules from, [5.5.1](cfrulset.md), [5.5.1](cfrulset.md)

disabled for

factor assignment, [18.4.1.2](reports.md)

realm authorization, [18.4.1.5](reports.md)

editing

rule sets, [5.4](cfrulset.md)

rules in, [5.5.1](cfrulset.md)

error options, [5.3](cfrulset.md)

evaluation of rules, [5.5](cfrulset.md)

evaluation options, [5.3](cfrulset.md)

event handlers, [5.3](cfrulset.md)

events firing, finding with DVSYS.DV\_SYSEVENT, [15.3.1](plsql_interfaces.md)

factors, selecting for, [7.3](cfgfact.md)

factors, used with, [7.1](cfgfact.md)

fail code, [5.3](cfrulset.md)

fail message, [5.3](cfrulset.md)

functions

DBMS\_MACADM (configuration), [12.3](apis_dbms_macadm.md)

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

DBMS\_MACUTL constants (fields), [14.2.1](apis_dbms_macutl.md)

PL/SQL functions for rule sets, [15.3](plsql_interfaces.md)

guidelines, [5.10](cfrulset.md)

how rule sets work, [5.7.1](cfrulset.md)

incomplete, [18.4.1.1](reports.md)

naming conventions, [5.3](cfrulset.md)

nested rules, [5.7.2](cfrulset.md)

performance effect, [5.11](cfrulset.md)

procedures

DBMS\_MACADM (configuration), [12.3](apis_dbms_macadm.md)

process flow, [5.7.1](cfrulset.md)

propagating policies to other databases, [10.1.2](dba.md)

reports, [5.12](cfrulset.md)

rules that exclude one user, [5.7.3](cfrulset.md)

static evaluation, [5.10](cfrulset.md)

troubleshooting, [E.2](troubleshooting.md), [E.3](troubleshooting.md)

views

DVSYS.DBA\_DV\_RULE, [16.18](views.md)

DVSYS.DBA\_DV\_RULE\_SET, [16.19](views.md)

DVSYS.DBA\_DV\_RULE\_SET\_RULE, [16.20](views.md)

*See also* command rules, factors, realms, rules, secure application roles

rules

about, [5.5](cfrulset.md)

creating, [5.5.1](cfrulset.md)

creating names, [5.5.1](cfrulset.md)

data dictionary views, [5.12](cfrulset.md)

deleting from rule set, [5.5.1](cfrulset.md)

editing, [5.5.1](cfrulset.md)

existing rules, adding to rule set, [5.5.2](cfrulset.md)

naming conventions, [5.5.1](cfrulset.md)

nested within a rule set, [5.7.2](cfrulset.md)

removing from rule set, [5.5.1](cfrulset.md)

reports, [5.12](cfrulset.md)

troubleshooting, [E.2](troubleshooting.md)

views

DVSYS.DBA\_DV\_RULE, [16.18](views.md)

DVSYS.DBA\_DV\_RULE\_SET\_RULE, [16.20](views.md)

*See also* rule sets

rules sets

audit event, custom, [A.1.1](audplcy.md)

---

## S

SCHEDULER\_ADMIN role

impact of Oracle Database Vault installation, [2.4](dv_impact.md)

scheduling database jobs

about, [10.3.1](dba.md)

Allow Scheduler Job rule set, [5.2](cfrulset.md)

CREATE EXTERNAL JOB privilege security consideration, [D.6.4](guidelines.md)

granting Oracle Database Vault authorization, [10.3.2](dba.md)

revoking Oracle Database Vault authorization, [10.3.3](dba.md)

schemas

DVF, [11.1.2](db_objects.md)

DVSYS, [11.1.1](db_objects.md)

Secure Application Configuration Issues Report, [18.4.1.7](reports.md)

secure application role, [8.1](cfseappr.md)

Secure Application Role Audit Report, [18.4.2.6](reports.md)

secure application roles

audit event, custom, [A.1.1](audplcy.md)

creating, [8.2](cfseappr.md)

data dictionary view, [8.8](cfseappr.md)

DBMS\_MACSEC\_ROLES.SET\_ROLE function, [8.2](cfseappr.md)

deleting, [8.4](cfseappr.md)

functionality, [8.5](cfseappr.md)

functions

DBMS\_MACADM (configuration), [12.6](apis_dbms_macadm.md)

DBMS\_MACSEC\_ROLES (configuration), [13.1](apis_macsec_roles.md)

DBMS\_MACSEC\_ROLES package, [13.1](apis_macsec_roles.md)

DBMS\_MACUTL (utility), [14.1](apis_dbms_macutl.md)

DBMS\_MACUTL constants (fields), [14.2.1](apis_dbms_macutl.md)

guidelines on managing, [8.3](cfseappr.md)

performance effect, [8.7](cfseappr.md)

procedure

.DBMS\_MACADM (configuration), [12.6](apis_dbms_macadm.md)

procedures and functions

DBMS\_MACUTL (utility), [14.3](apis_dbms_macutl.md)

propagating policies to other databases, [10.1.2](dba.md)

reports, [8.8](cfseappr.md)

Rule Set Configuration Issues Report, [18.4.1.6](reports.md)

troubleshooting, [E.3](troubleshooting.md)

troubleshooting with auditing report, [18.4.2.6](reports.md)

tutorial, [8.6.1](cfseappr.md)

views

DVSYS.DBA\_DV\_ROLE, [16.17](views.md)

*See also* roles, rule sets

security attacks

Denial of Service attacks

finding tablespace quotas, [18.5.9.6](reports.md)

Denial of Service (DoS) attacks

finding system resource limits, [18.5.6.3](reports.md)

eliminating audit trail, [18.5.5.10](reports.md)

monitoring security violations, [17.1](monitoring.md)

Oracle Database Vault addressing insider threats, [1.4](dvintro.md)

reports

AUDIT Privileges Report, [18.5.5.10](reports.md)

Objects Dependent on Dynamic SQL Report, [18.5.9.3](reports.md)

Privileges Distribution By Grantee, Owner Report, [18.5.4.2](reports.md)

Unwrapped PL/SQL Package Bodies Report, [18.5.9.4](reports.md)

SQL injection attacks, [18.5.9.3](reports.md)

tracking

with factor auditing, [7.3](cfgfact.md)

with rule set auditing, [5.3](cfrulset.md)

security policies

monitoring changes, [17.4](monitoring.md)

security policies, Oracle Database Vault addressing, [1.5](dvintro.md)

Security Policy Exemption Report, [18.5.5.3](reports.md)

Security Related Database Parameters Report, [18.5.6.1](reports.md)

security violations

monitoring attempts, [17.1](monitoring.md)

security vulnerabilities

how Database Vault addresses, [1.6](dvintro.md)

operating systems, [18.5.5.11](reports.md)

reports, [18.5.9](reports.md)

Security Related Database Parameters Report, [18.5.6.1](reports.md)

root operating system directory, [18.5.9.2](reports.md)

SELECT statement

controlling with command rules, [6.1](cfcmdaut.md)

SELECT\_CATALOG\_ROLE role, [18.5.5.9](reports.md)

sensitive objects reports, [18.5.3](reports.md)

separation of duty concept

about, [D.1.1](guidelines.md)

command rules, [6.2](cfcmdaut.md)

database accounts, [11.3](db_objects.md)

database accounts, suggested, [11.3](db_objects.md)

database roles, [2.3](dv_impact.md)

Database Vault Account Manager role, [11.3](db_objects.md)

documenting tasks, [D.1.4](guidelines.md)

example matrix, [D.1.3](guidelines.md)

how Oracle Database Vault addresses, [2.3](dv_impact.md)

Oracle Database Vault enforcing, [1.1](dvintro.md)

realms, [1.6](dvintro.md)

restricting privileges, [2.2](dv_impact.md)

roles, [11.2.1](db_objects.md)

tasks in Oracle Database Vault environment, [D.1.2](guidelines.md)

session time, setting for Oracle Database Vault Administrator, [C.3](dvca.md)

sessions

audit events, custom, [A.1.1](audplcy.md)

DBMS\_MACUTL fields, [14.2.1](apis_dbms_macutl.md)

finding session user with DVF.F$SESSION\_USER, [15.2.16](plsql_interfaces.md)

restricting data based on, [7.9.1](cfgfact.md)

retrieving information with functions, [12.5](apis_dbms_macadm.md)

SQL injection attacks, detecting with Object Dependent on Dynamic SQL Report, [18.5.9.3](reports.md)

SQL statements

default command rules that protect, [6.2](cfcmdaut.md)

SQL text, finding with DVSYS.DV\_SQL\_TEXT, [15.3.8](plsql_interfaces.md)

SQL92\_SECURITY initialization parameter, [2.1](dv_impact.md)

subfactors

*See* child factors under factors topic

SYS schema

command rules, [6.4](cfcmdaut.md)

SYS user account

access to Database Vault Account Management realm, [4.2](cfrealms.md)

adding to realm authorization, [4.14](cfrealms.md)

granting or revoking EXECUTE on DBMS\_RLS package, [Preface](whatsnew.md)

SYS.AUD$ table

location for Oracle Database Vault, [2.6.1](dv_impact.md)

object owner for realm protection, [4.5](cfrealms.md)

protecting with realm, [2.6.1](dv_impact.md)

SYSDBA access

guidelines on managing, [D.4.3](guidelines.md)

SYSDBA privilege

limiting, importance of, [D.2.3](guidelines.md)

SYS.FGA\_LOG$ table

protecting with realm, [2.6.1](dv_impact.md)

SYSMAN user account

realm for, [4.2](cfrealms.md)

SYSOPER access

guidelines on managing, [D.4.4](guidelines.md)

system features

disabling with Disabled rule set, [5.2](cfrulset.md)

enabling with Enabled rule set, [5.2](cfrulset.md)

system privileges

checking with DBMS\_MACUTL.USER\_HAS\_SYSTEM\_PRIVILEGE function, [14.3](apis_dbms_macutl.md)

reports

System Privileges By Privileges Report, [18.5.2.5](reports.md)

System Privileges By Privilege Report, [18.5.2.5](reports.md)

System Resource Limits Report, [18.5.6.3](reports.md)

system root access, guideline on managing, [D.4.1](guidelines.md)

SYSTEM schema

application tables in, [D.2.2](guidelines.md)

SYSTEM user account

guidelines for using with Database Vault, [D.2.1](guidelines.md)

SYSTEM.AUD$ table

location for Oracle Database Vault, [2.6.1](dv_impact.md)

---

## T

tablespace quotas, [18.5.9.6](reports.md)

Tablespace Quotas Report, [18.5.9.6](reports.md)

third party products, affected by Oracle Database Vault, [B.1](dvdisabl.md)

time data

DBMS\_MACUTL functions, [14.3](apis_dbms_macutl.md)

time-out value, setting for Oracle Database Vault Administrator, [C.3](dvca.md)

trace files

about, [E.1.1](troubleshooting.md)

trace files, Oracle Database Vault

about, [E.1.1](troubleshooting.md)

activities that can be traced, [E.1.2](troubleshooting.md)

ADRCI utility, [E.1.6.3](troubleshooting.md)

directory location for trace files, [E.1.6.1](troubleshooting.md)

disabling for all sessions, [E.1.8.2](troubleshooting.md)

disabling for current session, [E.1.8.1](troubleshooting.md)

enabling for all sessions, [E.1.5.2](troubleshooting.md)

enabling for current session, [E.1.5.1](troubleshooting.md)

examples, [E.1.7](troubleshooting.md)

finding trace file directory, [E.1.6.1](troubleshooting.md)

levels of trace events, [E.1.3](troubleshooting.md)

performance effect, [E.1.4](troubleshooting.md)

querying

ADRCI utility, [E.1.6.3](troubleshooting.md)

Linux grep command, [E.1.6.2](troubleshooting.md)

Transparent Data Encryption, used with Oracle Database Vault, [9.2](dv_ols.md)

triggers

different from object owner account, [18.5.9.7](reports.md)

reports, Non-Owner Object Trigger Report, [18.5.9.7](reports.md)

troubleshooting

access security sessions, [18.4.2.5](reports.md)

auditing reports, using, [18.4.2](reports.md)

Database Vault Administrator not showing default realms, command rules, rule sets, or factors, [C.1](dvca.md)

factors, [E.2](troubleshooting.md)

general diagnostic tips, [E.2](troubleshooting.md)

locked out accounts, [B.1](dvdisabl.md)

passwords, forgotten, [B.1](dvdisabl.md)

realms, [E.2](troubleshooting.md)

rule sets, [E.2](troubleshooting.md)

rules, [E.2](troubleshooting.md)

secure application roles, [18.4.2.6](reports.md)

trust levels

about, [7.5.2](cfgfact.md)

determining for identities with DVSYS.GET\_TRUST\_LEVEL\_FOR\_IDENTITY, [15.1.4](plsql_interfaces.md)

determining with DVSYS.GET\_TRUST\_LEVEL, [15.1.3](plsql_interfaces.md)

factor identity, [7.5.2](cfgfact.md)

factors, [7.5.2](cfgfact.md)

for factor and identity requested, [15.1.4](plsql_interfaces.md)

identities, [7.3](cfgfact.md)

of current session identity, [15.1.3](plsql_interfaces.md)

trusted users

accounts and roles that should be limited, [D.4](guidelines.md)

default for Oracle Database Vault, [D.3](guidelines.md)

tutorials

access, granting with secure application roles, [8.6.1](cfseappr.md)

ad hoc tool access, preventing, [7.8.1](cfgfact.md)

configuring two-person integrity (TPI), [5.9.1](cfrulset.md)

Database Vault factors with Virtual Private Database and Oracle Label Security, [9.4.4.1](dv_ols.md)

email alert in rule set, [5.8.1](cfrulset.md)

factors, mapping identities, [7.9.1](cfgfact.md)

Oracle Label Security integration with Oracle Database Vault, [9.4.4.1](dv_ols.md)

restricting access based on session data, [7.9.1](cfgfact.md)

restricting user activities with command rules, [6.7.1](cfcmdaut.md)

schema, protecting with a realm, [3.3.1](getting_started.md)

*See also* examples

two-man rule security

*See* two-person integrity (TPI)

two-person integrity (TPI)

about, [5.9.1](cfrulset.md)

configuring with a rule set, [5.9.1](cfrulset.md)

---

## U

Unwrapped PL/SQL Package Bodies Report, [18.5.9.4](reports.md)

user names

reports, Username/Password Tables Report, [18.5.9.5](reports.md)

USER\_HISTORY$ table, [18.5.5.6](reports.md)

Username/Password Tables Report, [18.5.9.5](reports.md)

users

enterprise identities, finding with DVF.F$PROXY\_ENTERPRISE\_IDENTITY, [15.2.15](plsql_interfaces.md)

enterprise-wide identities, finding with DVF.F$ENTERPRISE\_IDENTITY, [15.2.9](plsql_interfaces.md)

finding session user with DVF.F$SESSION\_USER, [15.2.16](plsql_interfaces.md)

login user name, finding with DVSYS.DV\_LOGIN\_USER, [15.3.2](plsql_interfaces.md)

restricting access by factor identity, [7.9.1](cfgfact.md)

utility functions

*See*.DBMS\_MACUTL package

UTL\_FILE object, [18.5.1.4](reports.md)

UTL\_FILE package, guidelines on managing, [D.6.1](guidelines.md)

---

## V

views

VPD

---

## W

wildcard, %, [18.3](reports.md)

WITH ADMIN Privileges Grants Report, [18.5.5.1](reports.md)

WITH ADMIN status, [18.5.2.1](reports.md), [18.5.2.2](reports.md)

WITH GRANT clause, [18.5.5.7](reports.md)

WITH GRANT Privileges Report, [18.5.5.7](reports.md)

---

## X

XStream