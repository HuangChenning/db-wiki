---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/part_3.html
tags:
  - oracle
  - 21c
  - security-guide
---

- [Using Application Contexts to Retrieve User Information](using-application-contexts-to-retrieve-user-information.md)  
	An application context stores user identification that can enable or prevent a user from accessing data in the database.
- [Using Oracle Virtual Private Database to Control Data Access](using-oracle-vpd-to-control-data-access.md)  
	Oracle Virtual Private Database (VPD) enables you to filter users who access data.
- [Using Transparent Sensitive Data Protection](using-transparent-sensitive-data-protection.md)  
	Transparent sensitive data protection enables you to find all table columns in a database that hold sensitive data.
- [Encryption of Sensitive Credential Data in the Data Dictionary](encrypt-sensitive-data.md)  
	You can encrypt sensitive credential information, such as passwords that are stored in the data dictionary.
- [Securing and Isolating Resources Using DbNest](dbnest.md)  
	You can secure and isolate instance-level and operating system resources by using dbNest.
- [Manually Encrypting Data](manually-encrypting-data.md)  
	You can use the `DBMS_CRYPTO` PL/SQL package to manually encrypt data.