Automatic Workflow Documentation
================================

Generates a Graphviz File form a workflow defintion.

.. image:: http://bluedynamics.com/plone_workflow.png

Usage:
------

- in ZMI got to the workflow which you want to document.

- there are two additional tabs one for raw dot data file, one for a rendered svg file.


Features:
---------

- generation of Graphviz file with states and transitions.
- each state shows a permissions-table
- each transition shows its guards.

Todo:
-----

- add views to control_panel

Installation
============

Just depend in your buildout on the egg ``collective.wfautodoc``.
When used within Plone ZCML is loaded automagically with ```z3c.autoinclude```.
Otherwise add the package to buildout section ```instance``` ```zcml```
variable.

 This package is written for Plone 4.1 or later but works also in a pure
 Zope2/CMF environment.

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

