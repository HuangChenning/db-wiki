---
title: Preface
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/preface.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

Oracle Database Net Services Administrator's Guide describes how to use Oracle Net Services. This guide describes the Oracle Net Services product and its components, as well as Oracle Net Services administrative and deployment topics. This preface contains the following topics:

## Audience

Oracle Database Net Services Administrator's Guide is intended for the following readers:

- Network administrators
- Directory server administrators
- Database administrators
- Decision makers

This guide is especially targeted for network administrators who are responsible for ensuring connectivity. For network administrators, Oracle recommends:

- For a conceptual understanding of Oracle Net Services, read all of [Part I, "Understanding Oracle Net Services"](part1.md)
- For essential configuration instructions, read all of [Part I, "Configuration and Administration of Oracle Net Services"](part2.md)
- For troubleshooting, read [Part I, "Testing and Troubleshooting Oracle Net Services"](part3.md)

For directory administrators, Oracle recommends:

- For understanding how Oracle Net Services uses a directory server, read [Chapter 3, "Managing Network Address Information"](config_concepts.md) in [Part I](part1.md)
- For instructions about configuring naming information in a directory server, and exporting existing naming data to a directory server, read [Chapter 8, "Configuring Naming Methods"](naming.md) in [Part I](part2.md)

For database administrators, Oracle recommends:

- For a general understanding of networking, read [Chapter 1, "Introducing Oracle Net Services"](intro.md) and [Chapter 6, "Quick Start to Oracle Net Services"](gettingstart.md)
- For an overview of communication layers, read [Chapter 4, "Understanding the Communication Layers"](layers.md)
- For understanding how to configure Oracle database server features that require listener and shared server configuration, read [Chapter 9, "Configuring and Administering Oracle Net Listener"](listenercfg.md), [Chapter 11, "Configuring Dispatchers"](dispatcher.md), and [Chapter 14, "Optimizing Performance"](performance.md)

For decision makers, Oracle recommends

- For an understanding of how Oracle Net Services fits into the overall network architecture and for explaining the basics of Oracle Net Services, read [Chapter 1, "Introducing Oracle Net Services"](intro.md), [Chapter 3, "Managing Network Address Information"](config_concepts.md), and [Chapter 6, "Quick Start to Oracle Net Services"](gettingstart.md)

Oracle recommends that all readers look over [Part I](part1.md), to ensure that they have the background required to benefit from the rest of the guide.

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers that have purchased support have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

## Related Documentation

For additional information, see the following Oracle resources:

- [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/toc.htm)
- Oracle Database 11g documentation set

Many books in the documentation set use the sample schemas of the seed database, which is installed by default when you install Oracle Database. Refer to [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm) for information about how these schemas were created and how you can use them yourself.

To download free release notes, installation documentation, white papers, or other collateral, visit the Oracle Technology Network. You must register online before using Oracle Technology Network; registration is free and can be done at

`http://www.oracle.com/technetwork/index.html`

If you already have a user name and password for Oracle Technology Network, then you can go directly to the documentation section of the Oracle Technology Network Web site at

`http://www.oracle.com/technetwork/indexes/documentation/index.html`

For additional information about [OSI](glossary.md), see:

`http://www.ietf.org`

Oracle error message documentation is only available in HTML. If you only have access to the Oracle Documentation CD, then you can browse the error messages by range. After you find the specific range, use your browser's "find in page" feature to locate the specific message. When connected to the Internet, you can search for a specific error message using the error message search feature of the Oracle online documentation.

## Conventions

The examples for directories in the book are for Linux. Unless otherwise noted, Microsoft Windows directory paths are the same except that they use a backslash (\\) instead of the forward slash (/).

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |