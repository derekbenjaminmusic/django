Release Policy
##############

Major versions of DMP are released in January and July. Minor versions,
containing bug fixes and/or security updates are released as required.

Past versions with new features
===============================

18.7 - 18.11
------------

Initial release in July 2018 had a very simple data structure. It used external API
for CWR generation. The code was open-source, but it was dependant on a free tier of a commercial service.

19.1 Epiphany
-------------

CWR generation and complete data validation was added to the open-source code. Full support for
modified works was added, as well as basic co-publishing support.
Data export in JSON format was added.

19.7 Metanoia
-------------

Support for multiple recordings per work and CWR 3.0 generation, labeled as "experimental", were added.
CWR preview, for both versions, received basic syntax highlighting. Since this version, CWR files are zipped.

20 Twenty
---------

Twenty-twenty was primarily about simplified deployment. Since this version, DMP can be deployed to the Free Heroku dyno
(container) by non-techies.

Support for custom global share splits was added. MR/SR affiliations for writers are available when implied by share
split settings.

Syntax highlighting for CWR acknowledgements was added, for simpler dealing with conflicts and other registration-related
issues.

20.7 Endemic
------------

Index (home) page became clearer due to grouping of views. User manual was reorganised to follow
the same structure. ``User manual`` links now lead to the relevant page.

Basic CSV imports and exports for musical works, and JSON exports for releases were added.
ISWCs can now be imported from CWR acknowledgements.

Processing of royalty statements was added. It is the most important new feature since the 
initial release. It can import statements in **any** CSV format. And processing is 
extremely fast.  

Controlled writers with no society affiliation are now fully supported.

Future open-source features
===========================

There is a business model behind Django-Music-Publisher. In order for a feature to be
released as open-source code, all of the following must apply:

* Code must be global, or near-global. Features that apply to one or couple of 
  countries will not be included.
  E.g. US publishers with multiple affiliations and BUMA/STEMRA
  share split rules are not covered.

* Code must be applicable to small publishers (and soon labels). The goal is to help them
  grow. If a feature is required only by established companies, it will not be included. 
  E.g. administrators and sub-publishers.

* A feature must not require complex customisations or deployments.
  Open-source solutions for end-users must be deployable by end-users.
  E.g. registrations in GEMA and licencing of production music.

* It must be legal. E.g. integrating DDEX into open-source code is currently not legal
  because DDEX licence is not compatible with MIT license.
