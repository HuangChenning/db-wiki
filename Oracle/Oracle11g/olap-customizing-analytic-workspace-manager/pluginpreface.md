---
title: Preface
book: OLAP Customizing Analytic Workspace Manager
doc_id: E17237-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/olap.112/e17237/pluginpreface.htm
tags:
  - oracle
  - 11g
  - olap-customizing-analytic-workspace-manager
---

With Oracle Analytic Workspace Manager, Version 11.2, you can add custom objects and menus to the user interface. You can customize Analytic Workspace Manager by doing the following:

- Adding custom reports and calculation templates to the navigation tree.
- Adding selections to the menu that appears when the user right-clicks a navigation tree object.
- Providing graphical user interface elements for viewing or editing relational database objects or OLAP objects, or both.

[Chapter 1, "Customizing With XML Documents"](olawxml.md) describes how you can add reports and calculation templates to the navigation tree by using XML documents. It also describes how you can specify an Analytic Workspace Manager Java plug-in within an XML document.

[Chapter 2, "Introducing Analytic Workspace Manager Plug-ins"](pluginintro.md) describes the Java plug-in interfaces that Analytic Workspace Manager supports and demonstrates how to develop a plug-in. With a plug-in you can add items to the right-click menu of an Analytic Workspace Manager navigation tree object. You can also provide a viewer or an editor plug-in that displays in the Analytic Workspace Manager property inspector.

This document describes the Analytic Workspace Manager XML and Java plug-in interfaces and provides simple examples of implementations of them.

This preface contains the following topics.

- Audience
- Documentation Accessibility
- Related Documents
- Conventions

## Audience

This document is intended for XML or Java developers who want to use XML documents or Java plug-ins to extend the functionality of Analytic Workspace Manager in Oracle Database 11g Release 2 (11.2) with the OLAP option.

## Documentation Accessibility

Our goal is to make Oracle products, services, and supporting documentation accessible to all users, including users that are disabled. To that end, our documentation includes features that make information available to users of assistive technology. This documentation is available in HTML format, and contains markup to facilitate access by the disabled community. Accessibility standards will continue to evolve over time, and Oracle is actively engaged with other market-leading technology vendors to address technical obstacles so that our documentation can be accessible to all of our customers. For more information, visit the Oracle Accessibility Program Web site at `http://www.oracle.com/accessibility/`.

Accessibility of Code Examples in Documentation

Screen readers may not always correctly read the code examples in this document. The conventions for writing code require that closing braces should appear on an otherwise empty line; however, some screen readers may not always read a line of text that consists solely of a bracket or brace.

Accessibility of Links to External Web Sites in Documentation

This documentation may contain links to Web sites of other companies or organizations that Oracle does not own or control. Oracle neither evaluates nor makes any representations regarding the accessibility of these Web sites.

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/support/contact.html` or visit `http://www.oracle.com/accessibility/support.html` if you are hearing impaired.

## Related Documents

For more information on Oracle OLAP, on using Analytic Workspace Manager, and on the Oracle OLAP Java API, see the following documents.

- [Oracle OLAP User's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e17123/toc.htm)
- [Oracle OLAP Java API Reference](https://docs.oracle.com/cd/E11882_01/olap.112/e10794/toc.htm)
- [Oracle OLAP Java API Developer's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e10795/toc.htm)

## Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |