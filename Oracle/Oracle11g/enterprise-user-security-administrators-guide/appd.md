---
title: Upgrading from Oracle9i to Oracle Database 11g Release 2 (11.2)
book: "Enterprise User Security Administrator's Guide"
doc_id: E10744-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10744/appd.htm
tags:
  - oracle
  - 11g
  - enterprise-user-security-administrators-guide
---

## D Upgrading from Oracle9i to Oracle Database 11g Release 2 (11.2)

This appendix discusses upgrading Oracle9i Database (9.2.0.8) to Oracle Database 11g Release 2 (11.2) with respect to Enterprise User Security. It includes the following sections:

## D.1 Upgrading Oracle Internet Directory from Release 9.2 to Release 9.0.4

Oracle9i Database Release 2 can work with Oracle Internet Directory Release 9.2 or Release 9.0.4. Oracle Database 11g Release 2 (11.2) requires Oracle Internet Directory 9.0.4 or later. In case you are using Oracle Internet Directory Release 9.2, you need to upgrade it to Release 9.0.4.

The following list discusses upgrading Oracle Internet Directory Release 9.2 to Oracle Internet Directory Release 9.0.4:

1. Use Oracle Internet Directory Configuration Assistant to upgrade Oracle Internet Directory. This is required if you want to register Oracle Database 11g Release 2 (11.2) instances in the directory.
2. Upgrade Oracle Contexts used for Enterprise User Security to Identity Management Realms, if they are not root contexts. Use the Oracle Internet Directory Configuration Assistant command-line utility as follows:
	```
	oidca mode=CTXTOIMR
	```
	This step is required if you want to register an Oracle Database 11g Release 2 (11.2) instance in a realm.
	You cannot use the root Oracle Context for Oracle Database 11g Release 2 (11.2) databases because it is not an Identity Management Realm.
3. Use Oracle Internet Directory tools, such as `ldapmodify` and `bulkmodify`, to add the `orcluserV2` `objectclass` to existing user entries. This `objectclass` is required for users to change their database passwords, and for kerberos authentication to the database.
4. In a realm that contains both Oracle9i Database and Oracle Database 11g Release 2 (11.2), use a DAS-based tool in Oracle Internet Directory Release 9.0.4 to create and manage users. You can use either Oracle Internet Directory Self-Service Console or Enterprise Security Manager Console. Do not use Enterprise Security Manager or Enterprise Login Assistant from Oracle9i installations.

## D.2 Upgrading Oracle Database from Release 9.2.0.8 to Release 11.2

For each Oracle9i Database (9.2.0.8) instance that you upgrade to Oracle Database 11g Release 2 (11.2), perform the following steps:

1. Use Oracle Wallet Manager to disable automatic login for the database wallet.
2. Copy the database distinguished name (DN) from the initialization parameter `rdbms_server_dn` to a file in a secure location.
3. Upgrade the database to Oracle Database 11g Release 2 (11.2).
4. Depending on where your database `admin` directory is stored, move the database wallet either to `$ORACLE_BASE/admin/` `olddbuniquename` `/wallet` or `$ORACLE_HOME/admin/` `olddbuniquename` `/wallet`. Note that `$ORACLE_HOME` is for the new Oracle Database 11g Release 2 (11.2). You may have to create the `wallet` directory.
5. Copy the old `$ORACLE_HOME/network/admin/ldap.ora` file to the new `$ORACLE_HOME/ldap/admin/ldap.ora` file. Alternatively, you can use Oracle Net Configuration Assistant to create a new `ldap.ora` file.
6. Use the command-line utility, `mkstore`, to put the database DN (from the file in the previously created secure directory location) into the wallet by using the following syntax:
	```
	mkstore -wrl database_wallet_location -createEntry 
	ORACLE.SECURITY.DN database_DN
	```
	You will be prompted for the wallet password.
	If you make a mistake in the `mkstore` command, then you can use the `-modifyEntry` option to correct it.
7. Use Database Configuration Assistant to generate the database-to-directory password in the database wallet. Choose the Modify Database option.
8. Use Oracle Wallet Manager to re-enable automatic login for the database wallet.
9. Use Oracle Net Manager to set the new wallet location in the `sqlnet.ora` file to the directory specified in step 4.

The default for the nickname attribute, such as CN, remains unchanged. The upgrade process does not change the default nickname attribute setting. After upgrading from Oracle Internet Directory Release 9.2 to Release 9.0.4, if you are unable to log in to Oracle Database 11g Release 2 (11.2), then you must use the DAS-based Oracle Internet Directory Self-Service Console to reset your password.

## D.3 Upgrading Oracle Database from Release 10g (10.1) and Higher to Oracle Database 11g Release 2 (11.2)

For each Oracle Database 10g Release 1 (10.2) and higher instance that you upgrade to Oracle Database 11g Release 2 (11.2), perform the following steps:

1. Upgrade the database to Oracle Database 11g Release 2 (11.2).
2. Depending on where your database `admin` directory is stored, move the database wallet either to `$ORACLE_BASE/admin/` `olddbuniquename` `/wallet` or `$ORACLE_HOME/admin/` `olddbuniquename` `/wallet`. Note that `$ORACLE_HOME` is for the new Oracle Database 11g Release 2 (11.2). You may have to create the `wallet` directory.
3. Copy the old `$ORACLE_HOME/network/admin/ldap.ora` file to the new `$ORACLE_HOME/ldap/admin/ldap.ora` file. Alternatively, you can use Oracle Net Configuration Assistant to create a new `ldap.ora` file.
4. Use Oracle Wallet Manager to re-enable automatic login for the database wallet.
5. Use Oracle Net Manager to set the new wallet location in the `sqlnet.ora` file to the directory specified in step 2.