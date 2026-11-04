---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/preface.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Preface

This guide explains how to install and configure Oracle Real Application Clusters (Oracle RAC).

Before you use this guide, you must first complete an installation of Oracle Clusterware, as described in the *Oracle Grid Infrastructure Installation Guide* for your platform.

## Intended Audience

*Oracle Real Application Clusters Installation Guide* \_for Linux and UNIX\_provides database installation information for database administrators (DBAs) who install and configure Oracle RAC.

## Set Up Java Access Bridge to Implement Java Accessibility

Install Java Access Bridge so that assistive technologies on Microsoft Windows systems can use the Java Accessibility API.

Java Access Bridge is a technology that enables Java applications and applets that implement the Java Accessibility API to be visible to assistive technologies on Microsoft Windows systems.

Refer to Java Platform, Standard Edition Accessibility Guide for information about the minimum supported versions of assistive technologies required to use Java Access Bridge. Also refer to this guide to obtain installation and testing instructions, and instructions for how to use Java Access Bridge.

Related Topics

- [*Java Platform, Standard Edition Java Accessibility Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/26/rilin&id=JSACC-GUID-7890D37B-16F2-48EC-B45F-2A6CF0613EE5)

## Command Syntax

Refer to these command syntax conventions to understand command examples in this guide.

| Convention | Description |
| --- | --- |
| `$` | Bourne or BASH shell prompt in a command example. Do not enter the prompt as part of the command. |
| `%` | C Shell prompt in a command example. Do not enter the prompt as part of the command. |
| `#` | Superuser (root) prompt in a command example. Do not enter the prompt as part of the command. |
| `monospace` | UNIX command syntax |
| backslash | A backslash is the UNIX and Linux command continuation character. It is used in command examples that are too long to fit on a single line. Enter the command as displayed (with a backslash) or enter it on a single line without a backslash:  ```code dd if=/dev/rdsk/c0t1d0s6 of=/dev/rst0 bs=10b \  count=10000 ``` |
| braces { } | Braces indicate required items:  ```code .DEFINE {macro1} ``` |
| brackets \[ \] | Brackets indicate optional items:  ```code cvtcrt termname [outfile] ``` |
| ellipses... | Ellipses indicate an arbitrary number of similar items:  ```code CHKVAL fieldname value1 value2 ... valueN ``` |
| *italic* | Italic type indicates a variable. Substitute a value for the variable:  ```code library_name ``` |
| vertical line \| | A vertical line indicates a choice within braces or brackets:  ```code FILE filesize [K\|M] ``` |

## Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| **boldface** | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| *italic* | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |