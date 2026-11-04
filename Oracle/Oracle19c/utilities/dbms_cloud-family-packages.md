---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/dbms_cloud-family-packages.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20 DBMS\_CLOUD Family of Packages

To use the `DBMS_CLOUD` and other packages in the `DBMS_CLOUD` family of packages, you must complete certain tasks.

Starting with Oracle Database 19c release update 19.30, you can install `DBMS_CLOUD` and other packages of the `DBMS_CLOUD` family with installation scripts deployed with Oracle Database. These packages are not preinstalled. You must manually install these packages, and also configure users or roles to use these packages.

- [Using the DBMS\_CLOUD Family of Packages](using-dbms_cloud-family-packages.md)  
	Learn about the requirements for deploying and using the `DBMS_CLOUD` family of packages.
- [Installing DBMS\_CLOUD](installing-dbms_cloud.md)  
	To use the `DBMS_CLOUD` family of packages on a customer-managed Oracle Database, you must create a new user and install `DBMS_CLOUD` packages as that user.
- [Create SSL Wallet with Certificates](create-ssl-wallet-with-certificates.md)  
	To access HTTP URIs and Object Stores safely from within your database, you must create a wallet with the appropriate certificates.
- [Configure ACEs for DBMS\_CLOUD (CDB and Non-CDB)](configure-dateabase-aces-for-dbms_cloud.md)  
	Create Access Control Entries (ACEs) to enable communication with Object Stores and other trusted `https` endpoints (URIs).
- [Verify Configuration of DBMS\_CLOUD](verify-configuration-dbms_cloud.md)  
	After you verify that the `DBMS_CLOUD` code is correctly installed, verify the proper setup of the SSL Wallet and the Access Control Entities (ACEs).
- [Configuring Users or Roles to use DBMS\_CLOUD](configuring-users-roles-use-dbms_cloud.md)  
	After successfully installing `DBMS_CLOUD`, you must configure users or roles to be able to use all of its supported functionality.

**Parent topic:** [Other Utilities](other-oracle-utilities.md)