---
title: UTL_HTTP
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/u_http.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 225 UTL\_HTTP

The `UTL_HTTP` package makes Hypertext Transfer Protocol (HTTP) callouts from SQL and PL/SQL. You can use it to access data on the Internet over HTTP.

When the package fetches data from a Web site using HTTPS, it requires Oracle Wallet Manager which can be created by either Oracle Wallet Manager or the orapki utility. Non-HTTPS fetches do not require an Oracle wallet.

See Also:

- [Chapter 239, "UTL\_URL"](u_url.md)
- [Chapter 236, "UTL\_SMTP"](u_smtp.md)
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for more information on Wallet Manager

This chapter contains the following topics:

---

## Using UTL\_HTTP

This section contains topics which relate to using the `UTL_HTTP` package.

- Overview
- Security Model
- Constants
- Datatypes
- Operational Notes
- Exceptions
- Examples

---

### Overview

With the `UTL_HTTP` package, you can write PL/SQL programs that communicate with Web (HTTP) servers. And `UTL_HTTP` contains a function that can be used in SQL queries.

The package supports HTTP over the Secured Socket Layer protocol (SSL), also known as HTTPS. It also supports SSL client authentication by sending the client-certificate in a wallet to authenticate with the remote Web server.

Other Internet-related data-access protocols (such as the File Transfer Protocol (FTP) or the Gopher protocol) are also supported using an HTTP proxy server that supports those protocols.

---

### Security Model

This package is an invoker's rights package and the invoking user will need the `connect` privilege granted in the access control list assigned to the remote network host to which he wants to connect, as well as the `use-client-certificates` or the `use-passwords` privilege to authenticate himself with the remote Web server using the credentials stored in an Oracle wallet.

Note:

For more information, see [Managing Fine-grained Access to External Network Services](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG40012) in [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/toc.htm)

---

### Constants

The `UTL_HTTP` package uses the constants shown in following tables.

- UTL\_HTTP Constants - HTTP Versions
- UTL\_HTTP Constants - Default Ports
- UTL\_HTTP Constants - HTTP 1.1 Status Codes

Table 225-1 UTL\_HTTP Constants - HTTP Versions

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `HTTP_VERSION_1_0` | `VARCHAR2` (10) | `'HTTP/1.0'` | Denotes HTTP version 1.0 that can be used in the function `BEGIN_REQUEST`. |
| `HTTP_VERSION_1_1` | `VARCHAR2` (10) | `'HTTP/1.1'` | Denotes HTTP version 1.1 that can be used in the function `BEGIN_REQUEST`. |

Table 225-2 UTL\_HTTP Constants - Default Ports

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `DEFAULT_HTTP_PORT` | `PLS_INTEGER` | `80` | The default TCP/IP port (80) at which a Web server or proxy server listens |
| `DEFAULT_HTTPS_PORT` | `PLS_INTEGER` | `443` | The default TCP/IP port (443) at which an HTTPS Web server listens |

Table 225-3 UTL\_HTTP Constants - HTTP 1.1 Status Codes

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `HTTP_CONTINUE` | `PLS_INTEGER` | `100` | The client should continue with its request. This interim response is used to inform the client that the initial part of the request has been received and has not yet been rejected by the server. |
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

---

### Datatypes

- REQ Type
- RESP Type
- COOKIE and COOKIE\_TABLE Types
- CONNECTION Type
- REQUEST\_CONTEXT\_KEY Type

#### REQ Type

Use this PL/SQL record type to represent an HTTP request.

Syntax

```
TYPE req IS RECORD (
   url           VARCHAR2(32767),
   method        VARCHAR2(64),
   http_version  VARCHAR2(64));
```

Parameters

Table 225-4 REQ Type Parameters

| Parameter | Description |
| --- | --- |
| `url` | The URL of the HTTP request. It is set after the request is created by `BEGIN_REQUEST`. |
| `method` | The method to be performed on the resource identified by the URL. It is set after the request is created by `BEGIN_REQUEST`. |
| `http_version` | The HTTP protocol version used to send the request. It is set after the request is created by `BEGIN_REQUEST`. |

Usage Notes

The information returned in `REQ` from the interface `begin_request` is for read-only. Changing the field values in the record has no effect on the request.

There are other fields in `REQ` record type whose names begin with the prefix `private_.` The fields are private and are intended for use by implementation of the `UTL_HTTP` package. You should not modify the fields.

#### REQUEST\_CONTEXT\_KEY Type

This type is used to represent the key to a request context. A request context is a context that holds a private wallet and cookie table to make a HTTP request. This private wallet and cookie table, unlike the session-wide ones maintained in the package, will not be shared with other HTTP requests within the database session.

Syntax

```
SUBTYPE request_context_key IS PLS_INTEGER;
```

Usage Notes

To provide enhanced security, `UTL_HTTP` allows PL/SQL programs to create request contexts. A request context is a private context that holds a wallet and a cookie table that will not be shared with other programs in the same database session when making HTTP requests and receiving HTTP responses. PL/SQL programs should use request contexts when they need to use wallets or cookies that contain sensitive information such as authentication credentials.

#### RESP Type

This PL/SQL record type is used to represent an HTTP response.

Syntax

```
TYPE resp IS RECORD (
   status_code    PLS_INTEGER,
   reason_phrase  VARCHAR2(256),
   http_version   VARCHAR2(64));
```

Parameters

Table 225-5 RESP Type Parameters

| Parameter | Description |
| --- | --- |
| `status_code` | The status code returned by the Web server. It is a 3-digit integer that indicates the results of the HTTP request as handled by the Web server. It is set after the response is processed by `GET_RESPONSE`. |
| `reason_phrase` | The short textual message returned by the Web server that describe the status code. It gives a brief description of the results of the HTTP request as handled by the Web server. It is set after the response is processed by `GET_RESPONSE`. |
| `http_version` | The HTTP protocol version used in the HTTP response. It is set after the response is processed by `GET_RESPONSE`. |

Usage Notes

The information returned in `RESP` from the interface `GET_RESPONSE` is read-only. There are other fields in the `RESP` record type whose names begin with the prefix `private_.` The fields are private and are intended for use by implementation of the `UTL_HTTP` package. You should not modify the fields.

#### COOKIE and COOKIE\_TABLE Types

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

Fields of COOKIE Record Type

Table 225-6 shows the fields for the `COOKIE` and `COOKIE_TABLE` record types.

Table 225-6 Fields of COOKIE and COOKIE\_TABLE Type

| Field | Description |
| --- | --- |
| `name` | The name of the HTTP cookie |
| `value` | The value of the cookie |
| `domain` | The domain for which the cookie is valid |
| `expire` | The time by which the cookie will expire |
| `path` | The subset of URLs to which the cookie applies |
| `secure` | Should the cookie be returned to the Web server using secured means only. |
| `version` | The version of the HTTP cookie specification the cookie conforms. This field is `NULL` for Netscape cookies. |