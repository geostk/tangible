Tangible
========

.. image:: https://img.shields.io/travis/dbrgn/tangible/master.svg
    :alt: Travis-CI build status
    :target: http://travis-ci.org/dbrgn/tangible

.. image:: https://img.shields.io/coveralls/dbrgn/tangible/master.svg
    :target: https://coveralls.io/r/dbrgn/tangible
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/v/tangible.svg
    :target: https://pypi.python.org/pypi/tangible/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/wheel/tangible.svg
    :target: https://pypi.python.org/pypi/tangible/
    :alt: Wheel Availability

*Tangible* is a Python library to convert data into tangible 3D models. It
generates code for different backends like *OpenSCAD* or *ImplicitSCAD*. It is
inspired by projects like *OpenSCAD* and *d3.js*.

.. image:: https://raw.github.com/dbrgn/tangible/master/example1.jpg
    :alt: Example 1

Implementation
--------------

The difference from Projects like *SolidPython* is that *Tangible* is a modular
system with an intermediate representation of objects that is capable of
generating code for different backends, not just *OpenSCAD*. Additionally, its
main focus is not general CAD, but printable 3D visualization of data.

The workflow to get a real object from data is as follows::

    Python code => Intermediate representation (AST) => Programmatic CAD code
    => STL file => Slicer => G code => 3D printer => Tangible object

Of these, *Tangible* does the first three steps. The fourth step is handled by
a programmatic CAD tool like *OpenSCAD* or *ImplicitSCAD* and the last four
steps are handled by the specific 3D printer software.

Currently supported Python version is 2.7 and 3.4+.

This library was my student research project thesis at `HSR <http://hsr.ch/>`_.
You can find the thesis paper here: https://files.dbrgn.ch/sa-thesis.pdf

Contributions are very welcome! Please open an issue or a pull request.


Installation
------------

You can install Tangible directly via PyPI::

    pip install tangible

If you want the current development version::

    pip install -e git+https://github.com/dbrgn/tangible#egg=tangible-dev

 
Documentation
-------------

Documentation can be found on ReadTheDocs: `http://tangible.readthedocs.org/
<http://tangible.readthedocs.org/>`_

If you want to know more about the architecture of the library, please refer to
my `thesis PDF <https://files.dbrgn.ch/sa-thesis.pdf>`_.


Coding Guidelines
-----------------

`PEP8 <http://www.python.org/dev/peps/pep-0008/>`__ via `flake8
<https://pypi.python.org/pypi/flake8>`_ with max-line-width set to 99 and
E126-E128,E266,E731 ignored.

All Python files must start with an UTF8 encoding declaration and some
`future-imports <http://stackful-dev.com/quick-tips-on-making-your-code-python-3-ready.html>`_:

.. sourcecode:: python

    # -*- coding: utf-8 -*-
    from __future__ import print_function, division, absolute_import, unicode_literals

Docstrings convention: `Sphinx style <http://stackoverflow.com/a/5339352/284318>`__.


Testing
-------

Prepare::

    pip install -r requirements-dev.txt --use-mirrors
    pip install -e .

Run tests::

    pytest

Violations of the PEP8 coding guidelines above will be counted as test fails.


Versioning
----------

Tangible implements `Semantic Versioning 2.0
<http://semver.org/spec/v2.0.0.html>`_.


License
-------

LGPLv3 or later `http://www.gnu.org/licenses/lgpl.html
<http://www.gnu.org/licenses/lgpl.html>`_
