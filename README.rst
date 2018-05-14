.. image:: http://pybee.org/static/images/brutus-270.png
    :width: 72px
    :target: https://pybee.org/

BeeWare
=======

.. image:: https://img.shields.io/pypi/pyversions/beeware.svg
    :target: https://pypi.python.org/pypi/beeware

.. image:: https://img.shields.io/pypi/v/beeware.svg
    :target: https://pypi.python.org/pypi/beeware

.. image:: https://img.shields.io/pypi/status/beeware.svg
    :target: https://pypi.python.org/pypi/beeware

.. image:: https://img.shields.io/pypi/l/beeware.svg
    :target: https://github.com/pybee/beeware/blob/master/LICENSE

.. image:: https://badges.gitter.im/pybee/general.svg
    :target: https://gitter.im/pybee/general


BeeWare is a collection of tools and libraries to aid native application
development in Python.

This package provides a convenient user interface to drive those tools.

Usage
-----

To install BeeWare, create a new virtual environment::

    $ mkdir beeware
    $ cd beeware
    beeware $ python -m venv venv
    beeware $ ./venv/bin/activate

(or, if you're on Windows)::

    beeware $ venv\Scripts\activate.bat

Then, install BeeWare in that virtual environment::

    (venv) $ pip install beeware

To start a new project, run::

    (venv) $ beeware new

This will prompt you for details of your new project, such as the name,
description, and license.

Once you've added your application code, run::

    (venv) $ beeware build ios

from the directory that beeware created to build your application. To run
your application::

    (venv) $ beeware run ios

You can also target `android`, `macos`, `windows`, `linux` or `django`.

Depending on your choice of target, this will either (as appropriate):

* Run the app in the simulator for iOS or Android;
* Start a desktop app on Windows, macOS or Linux; or
* Start a webserver on port 8000 for Django

Community
---------

You can talk to the BeeWare community through:

* `@pybeeware on Twitter`_

* The `pybee/general`_ channel on Gitter.

We foster a welcoming and respectful community as described in our
`BeeWare Community Code of Conduct`_.

Contributing
------------

If you experience problems with BeeWare, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _BeeWare suite: http://pybee.org
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _pybee/general: https://gitter.im/pybee/general
.. _BeeWare Community Code of Conduct: http://pybee.org/community/behavior/
.. _log them on Github: https://github.com/pybee/beeware/issues
.. _fork the code: https://github.com/pybee/beeware
.. _submit a pull request: https://github.com/pybee/beeware/pulls
