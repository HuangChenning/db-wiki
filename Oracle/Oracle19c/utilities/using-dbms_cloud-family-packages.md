---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/using-dbms_cloud-family-packages.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.1 Using the DBMS\_CLOUD Family of Packages

Learn about the requirements for deploying and using the `DBMS_CLOUD` family of packages.

In Oracle Autonomous AI Database, the `DBMS_CLOUD` family of packages are preinstalled and configured. Oracle maintains them automatically. However, to use the `DBMS_CLOUD` packages with a customer-managed Oracle AI Database, you must manually install and configure the packages.

Compared with Oracle Autonomous AI Database, customer-managed Oracle AI Database deployments support a subset of the DBMS\_CLOUD family of packages functionality. This documentation describes only the APIs and functionality supported for customer-managed deployments.

Note:

For customer-managed, non-Autonomous AI Database uses of `DBMS_CLOUD`, see the documentation for the database release. The installation in Oracle Database 19c, Oracle Database 21c, and earlier releases of Oracle AI Database 26ai is different than the processes for Oracle AI Database 26ai Release update 7 and later release updates. For information about using `DBMS_CLOUD` with earlier releases, see KB54212 How To Setup And Use DBMS\_CLOUD Package (Doc ID 2748362.1)

DBMS\_CLOUD Packages

The `DBMS_CLOUD` family of packages consists of the following:

- `DBMS_CLOUD`
- `DBMS_CLOUD_AI`
- `DBMS_CLOUD_AI_AGENT`
- `DBMS_CLOUD_NOTIFICATION`
- `DBMS_CLOUD_PIPELINE`
- `DBMS_CLOUD_REPO`

Overview of Installation and Configuration Steps

To set up `DBMS_CLOUD`, the following installation and configuration steps must be completed:

Installing and configuring `DBMS_CLOUD`:

- Create a schema owning the `DBMS_CLOUD` package, and install the `DBMS_CLOUD` code in the container database (CDB), and all pluggable databases (PDBs).
- Create a wallet to contain the certificates required to access HTTP URIs and Object Stores.
- Configure your database environment to use the new SSL wallet.
- Configure your database with access control lists (ACLs) for `DBMS_CLOUD`.
- Verify the configuration of `DBMS_CLOUD`.

Configuring users or roles to use `DBMS_CLOUD`:

- Grant the minimum privileges required for a user or role to use `DBMS_CLOUD`
- Configure ACLs for a user or role to use `DBMS_CLOUD`
- Verify the proper setup of your user or role for using `DBMS_CLOUD`

Prerequisites for Using DBMS\_CLOUD

The `DBMS_CLOUD` suite of packages offer powerful capabilities that leverage a full range of database features. For example, all features available with Autonomous AI Database, which complies with United States FedRAMP security guidelines, can potentially be leveraged with the `DBMS_CLOUD` suite. As a general guideline, Oracle suggests that you deploy a complete database install to avoid dependency errors.

For customized deployments to support particular applications, the following are the minimal set of features required:

- `CATALOG` (Oracle Database Catalog Views)
- `XDB` (Oracle XML Database)
- `CONTEXT` (Oracle Text)

Note:

To use the Select AI feature, you must have Oracle Text and Vector Search enabled for your database.