---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/verify-setup-user-roles-use-dbms_cloud.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.6.3 Verify Setup of Users and Roles to Use DBMS\_CLOUD

When user and roles are set up correctly, you can create credentials and access data in the Object Store.

To access data in the Object Store that is not public, you need to authenticate with an OCI user in your tenancy who has appropriate privileges to the object storage bucket in the region in question. You need to create either an OCI API signing key or an auth token for a user in your tenancy. For details about access to the Oracle Cloud Infrastructure (OCI) Object store, see:

[https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm)

Example 20-6 Create Credential Object and Access the Object Store

Assuming you have created an authorization token (`auth`), you must create a credential object in your database schema for authentication. For example:

```
BEGIN
    DBMS_CLOUD.CREATE_CREDENTIAL(
        credential_name => 'your credential name',
        username => 'OCI within your tenancy',
        password => 'auth token generated for OCI user');
END;
/
```

After the creation of your credential object, you should now be able to access the Object Store bucket in your tenancy for which the OCI user in your tenancy has privileges. Replace the credential name, region, object storage name space. and bucket name with the correct values for your tenancy:

`select * from                         dbms_cloud.list_objects('CredentialName','https://objectstorage.region.oraclecloud.com/n/ObjectStorageNameSpace/b/BucketName/o/');`

Example 20-7 Validate User Configuration and Privilege (accessibility of wallet, privilege to use wallet, database-wide setting of wallet)

If you encounter problems with `DBMS_CLOUD` with the user or role you have configured, you can test the proper configuration of your environment without `DBMS_CLOUD` by using the same example code used for the DBMS\_CLOUD setup with the user or role that you configured.

Assuming you set up a user named `SCOTT`, wrap the following commands into a SQL script and execute it as SYS in the pluggable database you were configuring. Be aware of the following requirements to use the script example:

- Set the variables for your environment appropriately. If you do not set them correctly, then the example procedure will not work, independent of whether or not you have set up your user or role correctly.
- To use the example code you rquire additional privileges for your user or role. Specifically you require name EXECUTE on UTL\_HTTP. If your user or role does not have this privilege, then you must grant it temporarily to run this code successfully. If you have granted the ACLs through a role, then you must grant those privileges explicitly to user `SCOTT` for this example to work
```
-- user to troubleshoot
define clouduser=SCOTT
 
-- CUSTOMER SPECIFIC SETUP, NEEDS TO BE PROVIDED BY THE CUSTOMER
-- - SSL Wallet directory and password
define sslwalletdir=<Set SSL Wallet Directory>
define sslwalletpwd=<Set SSL Wallet password>
 
-- In environments w/ a proxy, you need to set the proxy in the verification code
-- define proxy_uri=<your proxy URI address>
 
-- create and run this procedure as owner of the ACLs, which is the future owner
-- of DBMS_CLOUD
CREATE OR REPLACE PROCEDURE &clouduser..GET_PAGE(url IN VARCHAR2)
AS
    request_context UTL_HTTP.REQUEST_CONTEXT_KEY;
    req UTL_HTTP.REQ;
    resp UTL_HTTP.RESP;
    data VARCHAR2(32767) default null;
    err_num NUMBER default 0;
    err_msg VARCHAR2(4000) default null;
 
BEGIN
 
-- Create a request context with its wallet and cookie table
request_context := UTL_HTTP.CREATE_REQUEST_CONTEXT(wallet_path => 'file:&sslwalletdir',wallet_password => '&sslwalletpwd');
 
-- Make a HTTP request using the private wallet and cookie
-- table in the request context
 
-- uncomment if proxy is required
--    UTL_HTTP.SET_PROXY('&proxy_uri', NULL);
  
req := UTL_HTTP.BEGIN_REQUEST(url => url,request_context => request_context);
resp := UTL_HTTP.GET_RESPONSE(req);
 
DBMS_OUTPUT.PUT_LINE('valid response');
 
EXCEPTION
WHEN OTHERS THEN
    err_num := SQLCODE;
    err_msg := SUBSTR(SQLERRM, 1, 3800);
    DBMS_OUTPUT.PUT_LINE('possibly raised PLSQL/SQL error: ' ||err_num||' - '||err_msg);
 
    UTL_HTTP.END_RESPONSE(resp);
    data := UTL_HTTP.GET_DETAILED_SQLERRM ;
    IF data IS NOT NULL THEN
        DBMS_OUTPUT.PUT_LINE('possibly raised HTML error: ' ||data);
    END IF;
END;
/
 
set serveroutput on
BEGIN
    &clouduser..GET_PAGE('https://objectstorage.eu-frankfurt-1.oraclecloud.com');
END;
/
 
set serveroutput off
drop procedure &clouduser..GET_PAGE;
```

Correct any errors in the configuration. This procedure will run successfully if you have configured your user or role correctly.

**Parent topic:** [Configuring Users or Roles to use DBMS\_CLOUD](configuring-users-roles-use-dbms_cloud.md)