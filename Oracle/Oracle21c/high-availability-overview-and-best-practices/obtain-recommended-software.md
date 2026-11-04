---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/obtain-recommended-software.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Obtain Recommended Software

Selecting and deploying the correct Oracle software versions and patches is essential for availability, security, and support. Use Oracle’s automated tooling or validated My Oracle Support resources to determine the right targets and to obtain secure, policy-compliant software.

Key Practices

- Use automated tools (FPP, AutoUpgrade, or DBCA/DBCACTL with Oracle Update Advisor integration) wherever possible to minimize manual errors.
- For environments where automation is not feasible, carefully reference Exachk output and relevant KB articles.
- Always verify downloaded artifacts using Oracle’s provided digital signatures and checksums.

### Database and Grid Infrastructure, On-Premises

Recommended Approach – DBCA/DBCACTL, AutoUpgrade, or FPP with Oracle Update Advisor

Obtain recommended software as a Gold Image with Oracle Update Advisor functionality. Use Gold Images to perform updates in the recommended out-of-place, image-based manner.

Recommended workflow:

1. Generate a gold image that contains the recommended software matching your policy and required patches.
2. Download the recommended gold image.
3. Validate the image in a non-production environment.
4. Promote the validated image through the maintenance lifecycle.

Gold images are automatically tailored:

- Include Oracle’s recommended RU and any required interim or critical patches.
- Resolve patch conflicts.
- Retain or add customer-specific patches when specified and supported.

DBCA Example

```
$ dbca -managePatches -generateGoldImage -silent
$ dbca -managePatches -downloadGoldImage -goldImageDownloadLocation /u01/swdepot -silent
```

FPP Example using FPP Server Mode

```
$ rhpctl evaluate patch -image DB238000 -generateimage -importtoimage DB239000
```

Feature-Specific Database Recommendations (Manual Process Only)

Oracle Update Advisor may not provide all feature-specific recommendations for every database feature. For additional features such as Data Pump, review the applicable My Oracle Support knowledge base articles to identify recommended interim patches or feature-specific fixes.

If you are using manual methods for core database software:

An alternative approach is to review relevant KB articles, run Exachk, and download either gold images or recommended interim patches.

- Review relevant Knowledge Base notes and identify recommended software.
	- [Primary Note for Database Quarterly Release Updates (KB888)](https://support.oracle.com/support/?documentId=KB888)
		- [Exadata Critical Issues (KB623062)](https://support.oracle.com/support/?documentId=KB623062)
		- [Oracle Database 19c and Oracle AI Database 26ai Important Recommended One-off Patches (KB188772)](https://support.oracle.com/support/?documentId=KB188772)
		- [Oracle Database End of Premier Support For Major Releases - Frequently Asked Questions (FAQ2181)](https://support.oracle.com/support/?documentId=FAQ2181)
- Run Exachk and review recommended software checks.
	- Review MAA Scorecard section for Recommended Release and Release Update (RU)
	- Review Critical issues section for Recommended critical issue updates
	- Review Important bug fixes check for Recommended important issue updates
- Adjust recommendation to adhere to your software maintenance policy.
- Follow [Platinum Process for Gold Image based In Place and Out of Place Grid - Oracle home Patching (KB324119)](https://support.oracle.com/support/?documentId=KB324119) to request and download gold images for Database and Grid Infrastructure software homes, supplying your inventory and the recommended software manually identified above as candidate patches.

### Exadata (On-Premises)

Review relevant My Oracle Support knowledge base articles, run Exachk, and download recommended updates.

- Review relevant KB articles and identify recommended software.
	- Review [Oracle Exadata Database Machine Operations Best Practices (KB214168)](https://support.oracle.com/support/?documentId=KB214168) for Recommended Exadata software
		- [Exadata Critical Issues (KB623062)](https://support.oracle.com/support/?documentId=KB623062)
		- Review [Oracle Exadata: Exadata and Linux Important Recommended Fixes (KB403624)](https://support.oracle.com/support/?documentId=KB403624) for Recommended important issue updates
- Run Exachk and review recommended software checks.
	- Review MAA Scorecard section for Recommended Release and Release Update (RU)
	- Review Critical issues section for Recommended critical issue patches
	- Review Important bug fixes check for Recommended important issue patches
- Adjust recommendation to adhere to your software maintenance policy.
- Follow [Oracle Exadata Database Machine Operations Best Practices (KB214168](https://support.oracle.com/support/?documentId=KB214168)) to download recommended updates for Exadata compute nodes, storage servers, and switches directly.