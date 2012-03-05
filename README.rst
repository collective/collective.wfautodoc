Automatic Workflow Documentation
================================

Generates a Graphviz File form a workflow defintion. 

!! Alpha = Work in progress. !!

.. image:: http://bluedynamics.com/plone_workflow.png

Usage:
------

- in ZMI got to the workflow which you want to document.

- on its url call @@wfautodoc_gvfile 

- download the result and process further local:

  - ``dot -Tsvg FILENAME.gv -O `` (on Ubuntu so a ``sudo apt-get install graphviz`` before). 

  - or use ``xdot FILENAME.gv`` (on Ubuntu so a ``sudo apt-get install xdot`` before.

  - there are several other tools available to render graphviz files.


Working:
--------

- generation of Graphviz file with states and transitions.
- each state has an permissions-table
- each transition show its guards.

Todo:
-----

- add tab in ZMI to access view

- add view to render svg/png on server

- add views to control_panel

Installation
============

Just depend in your buildout on the egg ``collective.wfautodoc``. ZCML is
loaded automagically with z3c.autoinclude.


This package is written for Plone 4.1 or later.

Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...)
of ``collective.wfautodoc`` this is a great idea!

The code is located in the
`github collective <https://github.com/collective/collective.wfautodoc>`_.

You can clone it or `get access to the github-collective
<http://collective.github.com/>`_ and work directly on the project.

Maintainer is Jens Klein and the BlueDynamics Alliance developer team. We
appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us
`dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

Contributors
============

- Jens W. Klein <jens@bluedynamics.com>

