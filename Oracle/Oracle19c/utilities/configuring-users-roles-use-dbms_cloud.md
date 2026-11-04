---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/configuring-users-roles-use-dbms_cloud.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.6 Configuring Users or Roles to use DBMS\_CLOUD

After successfully installing `DBMS_CLOUD`, you must configure users or roles to be able to use all of its supported functionality.

- [Grant Minimal Privileges to a User or Role for DBMS\_CLOUD](grant-minimal-privileges-user-role-use-dbms_cloud.md)  
	For a user or role to use DBMS\_CLOUD functionality, you have to grant at least minimal access privileges.
- [Configure ACEs for a User or Role to Use DBMS\_CLOUD](configure-aces-user-role-use-dbms_cloud.md)  
	To provide all the functionality of `DBMS_CLOUD` to a user or role, you must enable the appropriate Access Control Entries (ACEs).
- [Verify Setup of Users and Roles to Use DBMS\_CLOUD](verify-setup-user-roles-use-dbms_cloud.md)  
	When user and roles are set up correctly, you can create credentials and access data in the Object Store.

**Parent topic:** [DBMS\_CLOUD Family of Packages](dbms_cloud-family-packages.md)