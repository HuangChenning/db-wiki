---
title: NZE-43000 to NZE-43021
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/nze2us.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 24 NZE-43000 to NZE-43021

NZE-43000: pkcs11 library not found

Cause: The PKCS11 library could not be found.

Action: Make sure that the pkcs11 library is at the location specified in the wallet.

NZE-43001: pkcs11 token not found

Cause: The PKCS11 token could not be found.

Action: Make sure that a token with correct label is present in slot.

NZE-43002: pkcs11 passphrase is wrong

Cause: The PKCS11 passphrase is wrong.

Action: Make sure that the token passphrase specified is correct.

NZE-43005: pkcs11: No tokens present

Cause: a token is not present in the slot

Action: Place a pkcs11 token in the slot

NZE-43011: pkcs11: Token login failed

Action: Check the token passphrase.

NZE-43014: pkcs11: finding private key on token error

Cause: error occurred while finding private key on token

Action: Make sure the private key corresponding to the certificate in wallet is on the token. Check trace message

NZE-43015: pkcs11: key pair gen error

Cause: error occurred while generating key pair using HSM

Action: Check trace message

NZE-43017: pkcs11: No certificate found on the smart card/HSM

Cause: No certificate was found on the smart card/HSM.

Action: Follow smart card/HSM vendor documentation to populate the smart card/HSM with certificate.

NZE-43018: pkcs11: No user certificate found on the smart card/HSM

Cause: No user certificate was found on the smart card/HSM.

Action: Follow smart card/HSM vendor documentation to populate the smart card/HSM with certificate and private key.

NZE-43019: pkcs11: No certificate found on smart card/HSM label with given cert label

Cause: There were no certificate labels on the smart card/HSM that matched the certificate label specified in the wallet.

Action: Follow smart card/HSM vendor documentation to set certificate label in smart card/HSM.

NZE-43020: pkcs11: Multiple certificates found on smart card/HSM with given cert label

Cause: Certificates with identical labels were found in the smart card/HSM.

Action: Follow smart card/HSM vendor documentation to assign unique certificate labels to certificates.

NZE-43021: pkcs11: Certificate with given cert label is not a user cert

Cause: The certificate with the specified certificate label did not have a matching private key in the smart card/HSM.

Action: Follow smart card/HSM vendor instructions to create credentials (certificate/private key) in smart card/HSM.