---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/verify-configuration-dbms_cloud.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.5 Verify Configuration of DBMS\_CLOUD

After you verify that the `DBMS_CLOUD` code is correctly installed, verify the proper setup of the SSL Wallet and the Access Control Entities (ACEs).

Wrap into a SQL script the commands shown in the example that follows, and run the script as the user `SYS` either within the CDB or in any PDB.

Note:

Ensure that you have set the variables for your environment appropriately. If you do not set them correctly then this example procedure will not work, independent of whether or not you have set up ` DBMS_CLOUD` correctly.

```
define clouduser=C##CLOUD$SERVICE
 
-- CUSTOMER SPECIFIC SETUP, NEEDS TO BE PROVIDED BY THE CUSTOMER
-- - SSL Wallet directory and password
define sslwalletdir=<Set SSL Wallet Directory>
define sslwalletpwd=<Set SSL Wallet password>
 
-- In environments w/ a proxy, you need to set the proxy in the verification code
-- define proxy_uri=<your proxy URI address>
 
-- create and run this procedure as owner of the ACLs, which is the future owner
-- of DBMS_CLOUD
 
CREATE OR REPLACE PROCEDURE &clouduser..GET_PAGE(url IN VARCHAR2) AS
    request_context UTL_HTTP.REQUEST_CONTEXT_KEY;
    req UTL_HTTP.REQ;
    resp UTL_HTTP.RESP;
    data VARCHAR2(32767) default null;
    err_num NUMBER default 0;
    err_msg VARCHAR2(4000) default null;
 
BEGIN
 
-- Create a request context with its wallet and cookie table
    request_context := UTL_HTTP.CREATE_REQUEST_CONTEXT(
        wallet_path => 'file:&sslwalletdir',
        wallet_password => '&sslwalletpwd');
 
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

If you have properly configured the SSL wallet and set up your database environment, then the script will return "valid response" and you can successfully connect to the Oracle Object Store.

If you receive an error, then your installation was not done properly. Correct any possible errors before continuing. If you cannot successfully access the example page, then you will not be able to access any Object Storage either.

**Parent topic:** [DBMS\_CLOUD Family of Packages](dbms_cloud-family-packages.md)