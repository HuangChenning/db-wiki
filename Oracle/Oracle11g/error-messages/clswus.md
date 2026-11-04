---
title: CLSW-00001 to CLSW-01000
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/clswus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 63 CLSW-00001 to CLSW-01000

CLSW-00001: Cluster Wallet operation failed

Cause: This is generic internal error for Cluster Wallet.

Action: Contact Oracle Customer Support.

CLSW-00002: Out of heap memory.

Cause: The program ran out of heap memory.

Action: Retry the operation when more memory is available.

CLSW-00003: Error in the cluster registry (OCR) layer. \[number\] \[string\]

Cause: An error occurred in the cluster registry layer while performing a cluster wallet operation.

Action: Ensure correct operation of cluster registry by inspecting ocr error (oerr proc \<ocrerror>), by using ocrcheck and ocrdump, and retry the operation.

CLSW-00004: Error in the network security layer. \[number\] \[string\]

Cause: An error occurred in the network security layer while performing a cluster wallet operation.

Action: Inspect the network security error (oerr ora \<nzerr>), and take corrective action to ensure correct operation.

CLSW-00005: Cannot perform cluster wallet operation because one of the parameters is NULL.

Cause: Program tried a cluster wallet operation using a NULL parameter.

Action: Check the parameters, and retry the operation.

CLSW-00006: Cannot perform cluster wallet operation because the context is invalid.

Cause: The cluster wallet context passed was invalid.

Action: Intialize the cluster wallet and retry the operation.

CLSW-00007: Cannot perform cluster wallet operation because one of the parameters is invalid. \[number\] \[string\]

Cause: Program tried a cluster wallet operation using an invalid parameter.

Action: Check the parameters, and retry the operation.

CLSW-00008: The cluster wallet to be created already exists.

Cause: The program tried to create a cluster wallet that already exists.

Action: Retry the operation after unsetting the CLSW\_FLAGS\_WALLET\_CREATE

CLSW-00009: The cluster wallet to be operated on does not exist.

Cause: Program tried to access a cluster wallet which does not exist.

Action: Check to see if the cluster wallet exists and try the operation

CLSW-00010: Error in the NLS services.

Cause: An error occurred in the NLS services while performing a cluster wallet operation.

Action: Check to see if the message file exists in $ORACLE\_HOME/has/mesg/clsw\*.msb

CLSW-00011: Cannot perform cluster wallet operation because data stored in the registry is invalid.

Cause: The data stored in the registry cannot be converted to a wallet.

Action: Delete the registry key associated with the wallet and recreate the wallet.

CLSW-00012: User is not authorized to perform the cluster wallet operation. \[number\] \[string\]

Cause: Program tried an operation on a cluster wallet for which it does not have permission.

Action: Check to see if program is run as the correct user.

CLSW-00013: Error in the clusterware operating system (SCLS) services. \[string\]

Cause: An error occurred in the SCLS services while performing a cluster wallet operation.

Action: Check to see if NIS/LDAP on Unix and Active Directory Service on Windows has been correctly configured.

CLSW-01000: Enter Password:

Cause: This is a prompt to user to enter password.

Action: Enter password.