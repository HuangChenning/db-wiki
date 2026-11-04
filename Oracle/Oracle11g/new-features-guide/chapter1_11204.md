---
title: Oracle Database 11g Release 2 (11.2.0.4) New Features
book: New Features Guide
doc_id: E41360-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41360/chapter1_11204.htm
tags:
  - oracle
  - 11g
  - new-features-guide
---

## 1 Oracle Database 11g Release 2 (11.2.0.4) New Features

This chapter contains descriptions of all of the features that are new to Oracle Database 11g Release 2 (11.2.0.4).

## 1.1 Oracle Data Redaction

This new database security feature is part of Oracle Advanced Security and prevents data columns (such as credit card numbers, U.S. Social Security numbers, and other sensitive or regulated data) from being displayed by applications. It is driven by declarative policies that can take into account database session factors and information passed by applications. Sensitive display data can be redacted at runtime on live production systems with minimal disruption to running applications and without altering the actual stored data. Different types of redaction are supported including full, partial, random, and regular expression redaction. You can conceal entire data values or redact only part of the value. The functionality is implemented inside of the database, therefore separate installation is not required.

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asopart1b.htm#ASOAG10135) for details

## 1.2 Trace File Analyzer and Collector

The Trace File Analyzer (TFA) and Collector, also known as TFA Collector, is a diagnostic collection utility to simplify diagnostic data collection on Oracle Clusterware, Oracle Grid Infrastructure and Oracle RAC systems.

Unlike similar solutions, the TFA Collector optimizes data gathering by providing a single source of management as well as various focus levels. Data for a whole cluster can be gathered from one node using one command and can be stored on a central server for further analysis and processing. The TFA Collector also allows for trimming data collection by focusing on certain components or relevant time frames only.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/troubleshoot.htm#CWADD92407) for details

## 1.3 RACcheck - The Oracle RAC Configuration Audit Tool

RACcheck is designed to audit vital configuration settings for the Oracle Database, single instance databases, as well as Oracle Real Application Clusters (Oracle RAC) databases. It also includes checks for Oracle Clusterware, Oracle Automatic Storage Management (Oracle ASM) and Oracle Grid Infrastructure.

RACcheck provides best practices recommedations considering the whole stack, including Maximum Availability Architecture (MAA) configurations and is therefore the ideal tool for regular health checks as well as pre- and post-upgrade best practices assessments.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racchk.htm#RACAD8365) for details

## 1.4 Database Replay Support for Database Consolidation

Database Replay now supports simultaneous execution of multiple database captures on a single consolidated database. Consolidated database replay supports scheduling of the individual replays enabling investigations of various scenarios (for example, what if all my individual workloads hit their peak utilizations at the same time).

Consolidated replay provides the ability to test database performance for database consolidation projects, whether consolidating onto an Oracle database machine or other consolidated infrastructure.

See Also:

[Oracle Database Testing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/dbr_consolidated.htm#RATUG4080) for details

## 1.5 Optimization for Flashback Data Archive History Tables

When using flashback data archive to track changes on tables, you can now enable optimization of the corresponding history tables using the `OPTIMIZE DATA` clause when creating or altering a flashback data archive.

Optimization of flashback data archive history tables provides better storage efficiency and better performance for flashback queries on the change history without additional intervention needed by the DBA.

See Also:

[Oracle Database Development Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS1008) for details

## 1.6 Desupported Features

The following features are desupported in Oracle Database 11g Release 2 (11.2):

- The `-cleanupOBase` flag of the deinstallation tool is desupported. There is no replacement for this flag.
- The DES and RC4 algorithms are desupported.

See Also:

[Oracle Database Upgrade Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=UPGRD60000) for details

## 1.7 New sqlnet.ora Parameter SSL\_EXTENDED\_KEY\_USAGE

Starting with this release, you can use the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter in the sqlnet.ora file to select a Secure Sockets Layer certificate to be used automatically to authenticate clients. For example, suppose you have multiple certificates for a smart card but only one of the certificates has an extended key usage field of client authentication. In the application, a certificate chooser dialog box would appear, prompting the user to select the type of authentication. Because the type of authentication would always be for clients, the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter can enable the application to bypass this dialog box and automatically choose client authentication. As a result, the user has fewer steps to perform in a task, thereby making the user's job easier and more efficient.

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asossl.htm#ASOAG10541) for details

## 1.8 New PrimaryLostWriteAction Property

The new `PrimaryLostWriteAction` Data Guard broker configuration property determines what action is taken if a standby database detects that a lost write has occurred at the primary database.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbpropref.htm#DGBKR3637) for details

## 1.9 ENABLE\_GOLDENGATE\_REPLICATION for Oracle GoldenGate

The `ENABLE_GOLDENGATE_REPLICATION` initialization parameter controls services provided by the RDBMS for Oracle GoldenGate (both capture and apply services). Set this to true to enable RDBMS services used by Oracle GoldenGate.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams086.htm#REFRN10346) for details