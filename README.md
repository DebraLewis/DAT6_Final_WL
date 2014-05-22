Problem Statement
=============================

"Look for the current product managers who are most "connected" to senior entrepreneurs at notable companies and prolific angel and venture investors, as a proxy for people who are likely to start new companies."
Prompt:
Develop a competitive intelligence tools that evaluates entrepreneur potential by using measures of experience (past job titles) and influence (connections to investors and influencers). 


Example query: Search through dataset of entrepreneurs sourced from AngelList Find to find project managers (PMs) / product managers / engineers that are well connected to prolific investors as a proxy for entrepreneurs to track.

-predict future entrepreneurs (where LinkedIn title == ‘’founder / co-founder”) using: LinkedIn API data
-predict influence by measuring proportion of high-powered connections (whose titles = CEO / Founder / President, etc.) 


Test variables:
=============================

-former  project managers (PMs) / product managers / engineers that became CTOs / CEOs / Founders
Influence:
-connections (linkedIn) with VCs (title == “ partner / principle / managing director”)
-connections with titles including “CEO/CTO/founder

Data Sources: all data is sourced from AngelList / LinekdIn / Twitter / CrunchBase
=============================

For entrepreneurs:
-name, tw_url, al_url, li_url, followers

For investors:
-name, tw_url, al_url, li_url, followers, no_investments


Assumptions
=============================
The following assumptions were made for this analysis:

   * A connection between a Product Manager (PM) and an entrepreneur / investor is assumed to exist if the entrepreneur / investor follows the PM on AL. The underlying hypothesis is that a follow from a notable senior entrepreneur / investor indicates a much stronger connection than the reverse.
   * Senior entrepreneurs are ones with Founder or Co-Founder in their title and notability can be measured by using number of followers as proxy.
   * Prolific investors are those who are in the 90th percentile in terms of number of investments.
