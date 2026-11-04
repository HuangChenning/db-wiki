---
title: "Integrating Authentication Devices Using RADIUS"
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/asoappc.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## C Integrating Authentication Devices Using RADIUS

This appendix describes how third-party authentication vendors customize the RADIUS challenge-response user interface to fit their particular device.

This appendix contains the following topics:

- About the RADIUS Challenge-Response User Interface
- Customizing the RADIUS Challenge-Response User Interface
	See Also:
	[Chapter 11, "Configuring RADIUS Authentication"](asoradus.md)

## C.1 About the RADIUS Challenge-Response User Interface

You can set up any authentication device that supports the RADIUS standard to authenticate Oracle users. When your authentication device uses the challenge-response mode, a graphical interface prompts the user first for a password and then for additional information. For example, a dynamic password that the user obtains from a token card. This interface is Java-based to provide optimal platform independence.

Third party vendors of authentication devices must customize this graphical user interface to fit their particular device. For example, a smart card vendor customizes the Oracle client to issue the challenge to the smart card reader. Then, when the smart card receives a challenge, it responds by prompting the user for more information, such as a PIN.

## C.2 Customizing the RADIUS Challenge-Response User Interface

You can customize this interface by creating your own class to support the functionality described in Table C-1. You can then open the `sqlnet.ora` file, look up the `SQLNET.RADIUS_AUTHENTICATION_INTERFACE` parameter, and replace the name of the class listed there (`DefaultRadiusInterface`), with the name of the new class you have just created. When you make this change in the `sqlnet.ora` file, the class is loaded on the Oracle client in order to handle the authentication process.

The third party must implement the Oracle RADIUS Interface, which is located in the `ORACLE.NET.RADIUS` package.

```
public interface OracleRadiusInterface {
  public void radiusRequest();
  public void radiusChallenge(String challenge);
  public String getUserName();
  public String getPassword();
}
```

Table C-1 Server Encryption Level Setting

| Parameter | Description |
| --- | --- |
| ``` radiusRequest ``` | Generally, this prompts the user for a user name and password, which will later be retrieved through `getUserName` and `getPassword`. |
| ``` getUserName ``` | Extracts the user name the user enters. If this method returns an empty string, it is assumed that the user wants to cancel the operation. The user then receives a message indicating that the authentication attempt failed. |
| ``` getPassword ``` | Extracts the password the user enters. If `getUserName` returns a valid string, but `getPassword` returns an empty string, the challenge keyword is replaced as the password by the database. If the user enters a valid password, a challenge may or may not be returned by the RADIUS server. |
| ``` radiusChallenge ``` | Presents a request sent from the RADIUS server for the user to respond to the server's challenge. |
| ``` getResponse ``` | Extracts the response the user enters. If this method returns a valid response, that information then populates the `User-Password` attribute in the new `Access-Request` packet. If an empty string is returned, the operation is aborted from both sides by returning the corresponding value. |