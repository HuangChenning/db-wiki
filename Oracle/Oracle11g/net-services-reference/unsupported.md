---
title: Features Not Supported in this Release
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/unsupported.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## A Features Not Supported in this Release

This appendix describes features no longer supported by Oracle Net Services.

This appendix contains the following topics:

## Overview of Unsupported Features

The following section describe the features and the configuration file that are no longer being supported in Oracle Database. This is based on an effort to streamline configuration and use of Oracle Database.

### Oracle Names

Oracle Names is not supported as a [naming method](glossary.md) in Oracle Database 11g. You must migrate to [directory naming](glossary.md).

See Also:

[Oracle Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/naming.htm#NETAG008) for additional information about migrating to directory naming

## Unsupported Parameters

Table A-1 describes the networking parameters no longer supported since Oracle9i.

Table A-1 Unsupported Networking Parameters

| File | Parameter | Description | Last Supported Release |
| --- | --- | --- | --- |
| `names.ora` | All parameters | Oracle Names is no longer supported. | 9.2 |
| `sqlnet.ora` | `SQLNET.CRYPTO_SEED` | This parameter was used to seed a random number generator for Oracle Advanced Security. Starting with Oracle Database 10g, Oracle Advanced Security uses a random number generator that does not to require a user-supplied seed value. | 9.2 |

## Unsupported Control Utility Commands

Table A-2 describes the control utility commands not supported since Oracle9i.

Table A-2 Unsupported Network Control Utility Commands

| Control Utility | Commands | Description | Last Supported Release |
| --- | --- | --- | --- |
| Oracle Names Control Utility | All commands | Oracle Names is no longer supported. | 9.2 |