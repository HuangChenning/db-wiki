---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_HTTP.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 268 UTL\_HTTP

The `UTL_HTTP` package makes Hypertext Transfer Protocol (HTTP) callouts from SQL and PL/SQL. You can use it to access data on the Internet over HTTP.

When the package fetches data from a Web site using HTTPS, it requires Oracle Wallet Manager which can be created by either Oracle Wallet Manager or the `orapki` utility. Non-HTTPS fetches do not require an Oracle wallet.

Note:

Oracle Wallet Manager (OWM) is deprecated with Oracle Database 21c. Please ensure your wallets are using the strongest protections available.

Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

Oracle recommends that you do not use deprecated values in new applications. Support for deprecated features is for backward compatibility only.

This chapter contains the following topics:

See Also:

- [UTL\_URL](UTL_URL.md)
- [UTL\_SMTP](UTL_SMTP.md)
- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBIMI-GUID-D0AA8373-B0AC-4DD8-9FA9-403E345E5A71) for more information on Wallet Manager

### 268.1 UTL\_HTTP Overview

With the `UTL_HTTP` package, you can write PL/SQL programs that communicate with Web (HTTP) servers. `UTL_HTTP` also contains a function that can be used in SQL queries.

The package supports HTTP over the Secured Socket Layer protocol (SSL), also known as HTTPS. It also supports SSL client authentication by sending the client-certificate in a wallet to authenticate with the remote Web server.

Other Internet-related data-access protocols (such as the File Transfer Protocol (FTP) or the Gopher protocol) are also supported using an HTTP proxy server that supports those protocols.

### 268.2 UTL\_HTTP Security Model

This package is an invoker's rights package. The invoking user will need the `connect` privilege granted in the access control list assigned to the remote network host to which he wants to connect, as well as the `use-client-certificates` or the `use-passwords` privilege to authenticate himself with the remote Web server using the credentials stored in an Oracle wallet.

Note:

For more information about managing fine-grained access, see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG-GUID-B7DB516A-3245-417F-BB89-8E8212A97542)

### 268.3 UTL\_HTTP Constants

The `UTL_HTTP` package defines several constants to use when specifying parameter values.

These are shown in following tables.

- Table 268-1
- Table 268-2
- Table 268-3

Table 268-1 UTL\_HTTP Constants - HTTP Versions

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `HTTP_VERSION_1_0 ` | `VARCHAR2` (10) | `'HTTP/1.0'` | Denotes HTTP version 1.0 that can be used in the function `BEGIN_REQUEST`. |
| `HTTP_VERSION_1_1 ` | `VARCHAR2` (10) | `'HTTP/1.1'` | Denotes HTTP version 1.1 that can be used in the function `BEGIN_REQUEST`. |

Table 268-2 UTL\_HTTP Constants - Default Ports

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `DEFAULT_HTTP_PORT` | `PLS_INTEGER` | `80` | The default TCP/IP port (80) at which a Web server or proxy server listens |
| `DEFAULT_HTTPS_PORT` | `PLS_INTEGER` | `443` | The default TCP/IP port (443) at which an HTTPS Web server listens |

Table 268-3 UTL\_HTTP Constants - HTTP 1.1 Status Codes

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `HTTP_CONTINUE ` | `PLS_INTEGER` | `100` | The client should continue with its request. This interim response is used to inform the client that the initial part of the request has been received and has not yet been rejected by the server. |
| `HTTP_SWITCHING_PROTOCOLS` | `PLS_INTEGER` | `101` | The server understands and is willing to comply with the client's request, through the Upgrade message header field, for a change in the application protocol being used on this connection. The server will switch protocols to those defined by the response's Upgrade header field immediately after the empty line which terminates the 101 response. |
| `HTTP_OK` | `PLS_INTEGER` | `200` | The request has succeeded. The information returned with the response is dependent on the method used in the request |
| `HTTP_CREATED CONSTANT` | `PLS_INTEGER` | `201` | The request has been fulfilled and resulted in a new resource being created. |
| `HTTP_ACCEPTED` | `PLS_INTEGER` | `202` | The request has been accepted for processing, but the processing has not been completed. The request might or might not eventually be acted upon, as it might be disallowed when processing actually takes place. |
| `HTTP_NON_AUTHORITATIVE_INFO` | `PLS_INTEGER` | `203` | The returned metainformation in the entity-header is not the definitive set as available from the origin server, but is gathered from a local or a third-party copy. |
| `HTTP_NO_CONTENT` | `PLS_INTEGER` | `204` | The server has fulfilled the request but does not need to return an entity-body, and might want to return updated metainformation. |
| `HTTP_RESET_CONTENT` | `PLS_INTEGER` | `205` | The server has fulfilled the request and the user agent should reset the document view which caused the request to be sent. The response must not include an entity. |
| `HTTP_PARTIAL_CONTENT` | `PLS_INTEGER` | `206` | The server has fulfilled the partial GET request for the resource. |
| `HTTP_MULTIPLE_CHOICES` | `PLS_INTEGER` | `300` | The requested resource corresponds to any one of a set of representations, each with its own specific location, and agent- driven negotiation information is being provided so that the user (or user agent) can select a preferred representation and redirect its request to that location. |
| `HTTP_MOVED_PERMANENTLY` | `PLS_INTEGER` | `301` | The requested resource has been assigned a new permanent URI and any future references to this resource should use one of the returned URIs. |
| `HTTP_FOUND CONSTANT` | `PLS_INTEGER` | `302` | The requested resource resides temporarily under a different URI. |
| `HTTP_SEE_OTHER` | `PLS_INTEGER` | `303` | The response to the request can be found under a different URI and should be retrieved using a GET method on that resource. |
| `HTTP_NOT_MODIFIED` | `PLS_INTEGER` | `304` | If the client has performed a conditional GET request and access is allowed, but the document has not been modified, the server responds with this status code. |
| `HTTP_USE_PROXY` | `PLS_INTEGER` | `305` | The requested resource must be accessed through the proxy given by the Location field. The Location field gives the URI of the proxy. |
| `HTTP_TEMPORARY_REDIRECT` | `PLS_INTEGER` | `307` | The requested resource resides temporarily under a different URI. |
| `HTTP_BAD_REQUEST` | `PLS_INTEGER` | `400` | The request could not be understood by the server due to malformed syntax. |
| `HTTP_UNAUTHORIZED` | `PLS_INTEGER` | `401` | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. |
| `HTTP_PAYMENT_REQUIRED` | `PLS_INTEGER` | `402` | This code is reserved for future use. |
| `HTTP_FORBIDDEN` | `PLS_INTEGER` | `403` | The server understood the request, but is refusing to fulfill it. |
| `HTTP_NOT_FOUND` | `PLS_INTEGER` | `404` | The server has not found anything matching the Request-URI. |
| `HTTP_NOT_ACCEPTABLE` | `PLS_INTEGER` | `406` | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |
| `HTTP_PROXY_AUTH_REQUIRED` | `PLS_INTEGER` | `407` | This code is similar to 401 (Unauthorized), but indicates that the client must first authenticate itself with the proxy. |
| `HTTP_REQUEST_TIME_OUT` | `PLS_INTEGER` | `408` | The client did not produce a request within the time that the server was prepared to wait. |
| `HTTP_CONFLICT` | `PLS_INTEGER` | `409` | The request could not be completed due to a conflict with the current state of the resource. |
| `HTTP_GONE` | `PLS_INTEGER` | `410` | The requested resource is no longer available at the server and no forwarding address is known. |
| `HTTP_LENGTH_REQUIRED` | `PLS_INTEGER` | `411` | The server refuses to accept the request without a defined `Content-Length`. |
| `HTTP_PRECONDITION_FAILED` | `PLS_INTEGER` | `412` | The precondition given in one or more of the request-header fields evaluated to false when it was tested on the server. |
| `HTTP_REQUEST_ENTITY_TOO_LARGE CONSTANT` | `PLS_INTEGER` | `413` | The server is refusing to process a request because the request entity is larger than the server is willing or able to process. |
| `HTTP_REQUEST_URI_TOO_LARGE` | `PLS_INTEGER` | `414` | The server is refusing to service the request because the Request-URI is longer than the server is willing to interpret. |
| `HTTP_UNSUPPORTED_MEDIA_TYPE` | `PLS_INTEGER` | `415` | The server is refusing to service the request because the entity of the request is in a format not supported by the requested resource for the requested method. |
| `HTTP_REQ_RANGE_NOT_SATISFIABLE` | `PLS_INTEGER` | `416` | A server returns a response with this status code if a request included a Range request-header field, and none of the range-specifier values in this field overlap the current extent of the selected resource, and the request did not include an If-Range request-header field. |
| `HTTP_EXPECTATION_FAILED` | `PLS_INTEGER` | `417` | The expectation given in an Expect request-header field could not be met by this server, or, if the server is a proxy, the server has unambiguous evidence that the request could not be met by the next-hop server. |
| `HTTP_NOT_IMPLEMENTED` | `PLS_INTEGER` | `501` | The server does not support the functionality required to fulfill the request. |
| `HTTP_BAD_GATEWAY` | `PLS_INTEGER` | `502` | The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed in attempting to fulfill the request |
| `HTTP_SERVICE_UNAVAILABLE` | `PLS_INTEGER` | `503` | The server is currently unable to handle the request due to a temporary overloading or maintenance of the server. |
| `HTTP_GATEWAY_TIME_OUT` | `PLS_INTEGER` | `504` | The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server specified by the URI (for example, HTTP, FTP, LDAP) or some other auxiliary server (for example, DNS) it needed to access in attempting to complete the request. |
| `HTTP_VERSION_NOT_SUPPORTED` | `PLS_INTEGER` | `505` | The server does not support, or refuses to support, the HTTP protocol version that was used in the request message. |

### 268.4 UTL\_HTTP Exceptions

Exceptions indicate that the UTL\_HTTP package encountered issues.

The following table lists these exceptions. By default, `UTL_HTTP` raises the exception `request_failed` when a request fails to execute. If the package is set to raise a detailed exception by `set_detailed_excp_support`, the rest of the exceptions will be raised directly (except for the exception `end_of_body`, which will be raised by `READ_TEXT`, `READ_LINE`, and `READ_RAW` regardless of the setting).

Table 268-4 UTL\_HTTP Exceptions

| Exception | Error Code | Reason | Where Raised |
| --- | --- | --- | --- |
| `BAD_ARGUMENT` | `29261` | The argument passed to the interface is bad | Any HTTP request or response interface when `detailed_exception` is enabled |
| `BAD_URL` | `29262` | The requested URL is badly formed | `BEGIN_REQUEST`, when `detailed_exception` is enabled |
| `END_OF_BODY` | `29266` | The end of HTTP response body is reached | `READ_RAW`, `READ_TEXT`, and `READ_LINE`, when `detailed_exception` is enabled |
| `HEADER_NOT_FOUND` | `29265` | The header is not found | `GET_HEADER`, `GET_HEADER_BY_NAME`, when `detailed_exception` is enabled |
| `HTTP_CLIENT_ERROR` | `29268` | From `GET_RESPONSE`, the response status code indicates that a client error has occurred (status code in 4xx range). Or from `begin_request`, the HTTP proxy returns a status code in the 4xx range when making an HTTPS request through the proxy. | `GET_RESPONSE`, `BEGIN_REQUEST` when d `etailed_exception` is enabled |
| `HTTP_SERVER_ERROR` | `29269` | From `GET_RESPONSE`, the response status code indicates that a client error has occurred (status code in 5xx range). Or from `begin_request`, the HTTP proxy returns a status code in the 5xx range when making an HTTPS request through the proxy. | `GET_RESPONSE,` `BEGIN_REQUEST` when `detailed_exception` is enabled |
| `NETWORK_ACCESS_DENIED` | `24247` | Access to the remote network host or credentials in an Oracle wallet is denied | `BEGIN_REQUEST` and `SET_AUTHENTICATION_FROM_WALLET` when `detailed_exception` is enabled |
| `ILLEGAL_CALL` | `29267` | The call to `UTL_HTTP` is illegal at the current state of the HTTP request | `SET_HEADER`, `SET_AUTHENTICATION`, and `SET_PERSISTENT_CONN_SUPPORT`, when `detailed_exception` is enabled |
| `PARTIAL_MULTIBYTE_EXCEPTION` | `29275` | No complete character is read and a partial multibyte character is found at the end of the response body | `READ_TEXT ` and `READ_LINE,` when `detailed_exception` is enabled |
| `PROTOCOL_ERROR` | `29263` | An HTTP protocol error occurs when communicating with the Web server | `SET_HEADER`, `GET_RESPONSE`, `READ_RAW`, `READ_TEXT`, and `READ_LINE`, when `detailed_exception` is enabled |
| `REQUEST_FAILED` | `29273` | The request fails to executes | Any HTTP request or response interface when `detailed_exception` is disabled |
| `TOO_MANY_REQUESTS` | `29270` | Too many requests or responses are open | `BEGIN_REQUEST`, when detailed\_exception is enabled |
| `TRANSFER_TIMEOUT` | `29276` | No data is read and a read timeout occurred | `READ_TEXT ` and `READ_LINE,` when `detailed_exception` is enabled |
| `UNKNOWN_SCHEME` | `29264` | The scheme of the requested URL is unknown | `BEGIN_REQUEST` and `GET_RESPONSE`, when `detailed_exception` is enabled |

Note:

The `partial_multibyte_char` and `transfer_timeout` exceptions are duplicates of the same exceptions defined in `UTL_TCP. `They are defined in this package so that the use of this package does not require the knowledge of the `UTL_TCP`. As those exceptions are duplicates, an exception handle that catches the `partial_multibyte_char` and `transfer_timeout ` exceptions in this package also catch the exceptions in the `UTL_TCP. `

For `REQUEST` and `REQUEST_PIECES`, the `request_failed` exception is raised when any exception occurs and `detailed_exception` is disabled.

### 268.5 UTL\_HTTP Examples

#### 268.5.1 UTL\_HTTP General Usage

This is an general example of `UTL_HTTP` usage.

```
SET SERVEROUTPUT ON SIZE 40000
  
DECLARE
  req   UTL_HTTP.REQ;
  resp  UTL_HTTP.RESP;
  value VARCHAR2(1024);
BEGIN
  UTL_HTTP.SET_PROXY('proxy.my-company.com', 'corp.my-company.com');
  req := UTL_HTTP.BEGIN_REQUEST('http://www-hr.corp.my-company.com');
  UTL_HTTP.SET_HEADER(req, 'User-Agent', 'Mozilla/4.0');
  resp := UTL_HTTP.GET_RESPONSE(req);
  LOOP
    UTL_HTTP.READ_LINE(resp, value, TRUE);
    DBMS_OUTPUT.PUT_LINE(value);
  END LOOP;
  UTL_HTTP.END_RESPONSE(resp);
EXCEPTION
  WHEN UTL_HTTP.END_OF_BODY THEN
    UTL_HTTP.END_RESPONSE(resp);
END;
```

#### 268.5.2 UTL\_HTTP Retrieving HTTP Response Headers

This example shows how `UTL_HTTP` retrieves HTTP response headers.

```
SET SERVEROUTPUT ON SIZE 40000
  
DECLARE
  req   UTL_HTTP.REQ;
  resp  UTL_HTTP.RESP;
  name  VARCHAR2(256);
  value VARCHAR2(1024);
BEGIN
  UTL_HTTP.SET_PROXY('proxy.my-company.com', 'corp.my-company.com');
  req := UTL_HTTP.BEGIN_REQUEST('http://www-hr.corp.my-company.com');
  UTL_HTTP.SET_HEADER(req, 'User-Agent', 'Mozilla/4.0');
  resp := UTL_HTTP.GET_RESPONSE(req);
  DBMS_OUTPUT.PUT_LINE('HTTP response status code: ' || resp.status_code);
  DBMS_OUTPUT.PUT_LINE('HTTP response reason phrase: ' || resp.reason_phrase);
  FOR i IN 1..UTL_HTTP.GET_HEADER_COUNT(resp) LOOP
    UTL_HTTP.GET_HEADER(resp, i, name, value);
    DBMS_OUTPUT.PUT_LINE(name || ': ' || value);
  END LOOP;
  UTL_HTTP.END_RESPONSE(resp);
END;
```

#### 268.5.3 UTL\_HTTP Handling HTTP Authentication

This code sample indicates how `UTL_HTTP` handles HTTP authentication.

```
SET serveroutput ON SIZE 40000
  
CREATE OR REPLACE PROCEDURE get_page (url      IN VARCHAR2,
                                      username IN VARCHAR2 DEFAULT NULL,
                                      password IN VARCHAR2 DEFAULT NULL,
                                      realm    IN VARCHAR2 DEFAULT NULL) AS
  req       UTL_HTTP.REQ;
  resp      UTL_HTTP.RESP;
  my_scheme VARCHAR2(256);
  my_realm  VARCHAR2(256);
  name      VARCHAR2(256);
  value     VARCHAR2(256);
BEGIN
  -- Turn off checking of status code. We will check it by ourselves.
  UTL_HTTP.SET_RESPONSE_ERROR_CHECK(FALSE);
  req := UTL_HTTP.BEGIN_REQUEST(url);
  IF (username IS NOT NULL) THEN
    UTL_HTTP.SET_AUTHENTICATION(req, username, password); -- Use HTTP Basic Authen. Scheme
  END IF;
  resp := UTL_HTTP.GET_RESPONSE(req);
  IF (resp.status_code = UTL_HTTP.HTTP_UNAUTHORIZED) THEN
    UTL_HTTP.GET_AUTHENTICATION(resp, my_scheme, my_realm, FALSE);
    DBMS_OUTPUT.PUT_LINE('Web proxy server is protected.');
    DBMS_OUTPUT.PUT('Please provide the required ' || my_scheme || ' authentication username/password for realm ' || my_realm || '
     for the proxy server.');
    UTL_HTTP.END_RESPONSE(resp);
    RETURN;
  ELSIF (resp.status_code = UTL_HTTP.HTTP_PROXY_AUTH_REQUIRED) THEN
    UTL_HTTP.GET_AUTHENTICATION(resp, my_scheme, my_realm, TRUE);
    DBMS_OUTPUT.PUT_LINE('Web page ' || url || ' is protected.');
    DBMS_OUTPUT.PUT('Please provide the required ' || my_scheme || ' authentication username/password for realm ' || my_realm || '
     for the Web page.');
    UTL_HTTP.END_RESPONSE(resp);
    RETURN;
  END IF;
  FOR i IN 1..UTL_HTTP.GET_HEADER_COUNT(resp) LOOP
    UTL_HTTP.GET_HEADER(resp, i, name, value);
    DBMS_OUTPUT.PUT_LINE(name || ': ' || value);
  END LOOP;
  UTL_HTTP.END_RESPONSE(resp);
END;
```

#### 268.5.4 UTL\_HTTP Retrieving and Restoring Cookies

This example show how UTL\_HTTP can be used to retrieve and restore cookies.

```
CREATE TABLE my_cookies (
    session_id  INTEGER,
    name        VARCHAR2(256),
    value       VARCHAR2(1024),
    domain      VARCHAR2(256),
    expire      DATE,
    path        VARCHAR2(1024),
    secure      VARCHAR2(1),
    version     INTEGER);

CREATE SEQUENCE session_id;
SET SERVEROUTPUT ON SIZE 40000

REM Retrieve cookies from UTL_HTTP
CREATE OR REPLACE FUNCTION save_cookies RETURN PLS_INTEGER AS
  cookies        UTL_HTTP.COOKIE_TABLE;
  my_session_id  PLS_INTEGER;
  secure         VARCHAR2(1);
BEGIN
  /* assume that some cookies have been set in previous HTTP requests. */
  UTL_HTTP.GET_COOKIES(cookies);
  SELECT session_id.nextval INTO my_session_id FROM DUAL;
  FOR i in 1..cookies.count LOOP
    IF (cookies(i).secure) THEN
      secure := 'Y';
    ELSE
      secure := 'N';
    END IF;
    INSERT INTO my_cookies
    VALUES (my_session_id, cookies(i).name, cookies(i).value,
            cookies(i).domain,
            cookies(i).expire, cookies(i).path, secure, cookies(i).version);
  END LOOP;
  RETURN my_session_id;
END;
/

REM Retrieve cookies from UTL_HTTP
CREATE OR REPLACE PROCEDURE restore_cookies (this_session_id IN PLS_INTEGER)
AS
  cookies        UTL_HTTP.COOKIE_TABLE;
  cookie         UTL_HTTP.COOKIE;
  i              PLS_INTEGER := 0;
  CURSOR c (c_session_id PLS_INTEGER) IS
    SELECT * FROM my_cookies WHERE session_id = c_session_id;
BEGIN
  FOR r IN c(this_session_id) LOOP
    i := i + 1;
    cookie.name     := r.name;
    cookie.value    := r.value;
    cookie.domain   := r.domain;
    cookie.expire   := r.expire;
    cookie.path     := r.path;
    IF (r.secure = 'Y') THEN
      cookie.secure := TRUE;
    ELSE
      cookie.secure := FALSE;
    END IF;
    cookie.version := r.version;
    cookies(i) := cookie;
  END LOOP;
  UTL_HTTP.CLEAR_COOKIES;
  UTL_HTTP.ADD_COOKIES(cookies);
END;
/
```

#### 268.5.5 UTL\_HTTP Making HTTP Request with Private Wallet and Cookie Table

This example shows how `UTL_HTTP` creates a request context with a wallet and cookie table, then makes an HTTP Request using that wallet and cookie table.

```
SET SERVEROUTPUT ON SIZE 40000
 
CREATE OR REPLACE PROCEDURE DISPLAY_PAGE(url IN VARCHAR2) AS
  request_context UTL_HTTP.REQUEST_CONTEXT_KEY;
  req             UTL_HTTP.REQ;
  resp            UTL_HTTP.RESP;
  data            VARCHAR2(1024);
 
BEGIN

  -- Create a request context with its wallet and cookie table
  request_context := UTL_HTTP.CREATE_REQUEST_CONTEXT(
                       wallet_path          => 'file:/oracle/wallets/test/wallet',
                       wallet_password      => '******',
                       enable_cookies       => TRUE,
                       max_cookies          => 300,
                       max_cookies_per_site => 20);
 
  -- Make a HTTP request using the private wallet and cookie
  -- table in the request context
  req := UTL_HTTP.BEGIN_REQUEST(
           url             => url,
           request_context => request_context);
  resp := UTL_HTTP.GET_RESPONSE(req);
 
  BEGIN
    LOOP
       UTL_HTTP.READ_TEXT(resp, data);
       DBMS_OUTPUT.PUT(data);
    END LOOP;
  EXCEPTION
      WHEN UTL_HTTP.END_OF_BODY THEN
         UTL_HTTP.END_RESPONSE(resp); 
  END;
 
  -- Destroy the request context
  UTL_HTTP.DESTROY_REQUEST_CONTEXT(request_context);
 
END;
 
BEGIN
  DISPLAY_PAGE('https://www.example.com/');
END;
/
```

#### 268.5.6 UTL\_HTTP Using a Proxy Server

This example shows using a proxy server for an Oracle Database connection.

The `UTL_HTTP.REQUEST` procedure uses the proxy server host name and the port number to access the HTTPS URL from within the Oracle Database.

```
SELECT UTL_HTTP.REQUEST('<URL>', '<proxy_hostname>:<proxy_port_number>', '<wallet_directory>', '<wallet_password>') FROM DUAL;
```

Note:

By default, the `UTL_HTTP.REQUEST` procedure enables you to omit or set the "proxy" argument as `NULL`.

### 268.6 UTL\_HTTP Data Structures

#### 268.6.1 REQ Type

Use this PL/SQL record type to represent an HTTP request.

Syntax

```
TYPE req IS RECORD (
   url           VARCHAR2(32767),
   method        VARCHAR2(64),
   http_version  VARCHAR2(64));
```

Parameters

Table 268-5 REQ Type Parameters

| Parameter | Description |
| --- | --- |
| `url` | The URL of the HTTP request. It is set after the request is created by `BEGIN_REQUEST`. |
| `method` | The method to be performed on the resource identified by the URL. It is set after the request is created by `BEGIN_REQUEST`. |
| `http_version` | The HTTP protocol version used to send the request. It is set after the request is created by `BEGIN_REQUEST`. |

Usage Notes

The information returned in `REQ` from the interface `begin_request` is for read-only. Changing the field values in the record has no effect on the request.

There are other fields in `REQ` record type whose names begin with the prefix `private_.` The fields are private and are intended for use by implementation of the `UTL_HTTP` package. You should not modify the fields.

#### 268.6.2 REQUEST\_CONTEXT\_KEY Type

This type is used to represent the key to a request context.

A request context is a context that holds a private wallet and cookie table to make a HTTP request. This private wallet and cookie table, unlike the session-wide ones maintained in the package, will not be shared with other HTTP requests within the database session.

Syntax

```
SUBTYPE request_context_key IS PLS_INTEGER;
```

Usage Notes

To provide enhanced security, `UTL_HTTP` allows PL/SQL programs to create request contexts. A request context is a private context that holds a wallet and a cookie table that will not be shared with other programs in the same database session when making HTTP requests and receiving HTTP responses. PL/SQL programs should use request contexts when they need to use wallets or cookies that contain sensitive information such as authentication credentials.

#### 268.6.3 RESP Type

This PL/SQL record type is used to represent an HTTP response.

Syntax

```
TYPE resp IS RECORD (
   status_code    PLS_INTEGER,
   reason_phrase  VARCHAR2(256),
   http_version   VARCHAR2(64));
```

Parameters

Table 268-6 RESP Type Parameters

| Parameter | Description |
| --- | --- |
| `status_code` | The status code returned by the Web server. It is a 3-digit integer that indicates the results of the HTTP request as handled by the Web server. It is set after the response is processed by `GET_RESPONSE`. |
| `reason_phrase` | The short textual message returned by the Web server that describe the status code. It gives a brief description of the results of the HTTP request as handled by the Web server. It is set after the response is processed by `GET_RESPONSE`. |
| `http_version` | The HTTP protocol version used in the HTTP response. It is set after the response is processed by `GET_RESPONSE`. |

Usage Notes

The information returned in `RESP` from the interface `GET_RESPONSE` is read-only. There are other fields in the `RESP` record type whose names begin with the prefix `private_.` The fields are private and are intended for use by implementation of the `UTL_HTTP` package. You should not modify the fields.

#### 268.6.4 COOKIE and COOKIE\_TABLE Types

The `COOKIE` type is the PL/SQL record type that represents an HTTP cookie. The `COOKIE_TABLE` type is a PL/SQL index-by-table type that represents a collection of HTTP cookies.

Syntax

```
TYPE cookie IS RECORD (
   name  VARCHAR2(256),
   value  VARCHAR2(1024),
   domain  VARCHAR2(256),
   expire  TIMESTAMP WITH TIME ZONE,
   path  VARCHAR2(1024),
   secure  BOOLEAN,
   version  PLS_INTEGER,
   comment  VARCHAR2(1024));

TYPE cookie_table IS TABLE OF cookie INDEX BY binary_integer;
```

Table 268-7 shows the fields for the `COOKIE` and `COOKIE_TABLE` record types.

Table 268-7 Fields of COOKIE and COOKIE\_TABLE Type

| Field | Description |
| --- | --- |
| `name` | The name of the HTTP cookie |
| `value` | The value of the cookie |
| `domain` | The domain for which the cookie is valid |
| `expire` | The time by which the cookie will expire |
| `path` | The subset of URLs to which the cookie applies |
| `secure` | Should the cookie be returned to the Web server using secured means only. |
| `version` | The version of the HTTP cookie specification the cookie conforms. This field is `NULL` for Netscape cookies. |