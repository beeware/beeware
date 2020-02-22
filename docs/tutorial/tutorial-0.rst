==============================
Tutorial 0 - Let's get set up!
==============================

Before we build our first BeeWare app, we have to make sure we've got
all the prerequisites for running BeeWare.

Install Python
==============

The first thing we'll need is a working Python interpreter, running Python 3.5
or higher.

.. tabs::

  .. group-tab:: macOS

    If you're on macOS, you can get the official installer from
    `the Python website <https://www.python.org/downloads>`_. You can use any
    stable version of Python from 3.5 onward (although we'd advice avoiding
    alphas, betas and release candidates unless you *really* know what you're
    doing).

  .. group-tab:: Linux

    If you're on Linux, you'll install Python using the system package manager
    (``apt`` on Debian/Ubuntu/Mint; ``dnf`` on Fedora, or ``pacman`` on Arch).

  .. group-tab:: Windows

    If you're on Windows, you can get the official installer from
    `the Python website <https://www.python.org/downloads>`_. You can use any
    stable version of Python 3.5, 3.6 or 3.7. We would advise *against* using
    Python 3.8 at this time, as some libraries needed for this tutorial aren't
    yet available for Python 3.8. We also advise avoiding alphas, betas and
    release candidates unless you *really* know what you're doing.

.. admonition:: Alternative Python distributions

    There are lots of different ways of installing Python. You can install
    Python through `homebrew
    <https://docs.brew.sh/Homebrew-and-Python>`__. You can use `pyenv
    <https://github.com/pyenv/pyenv#simple-python-version-management-pyenv>`__
    to manage multiple Python installs on the same machine. Windows users
    can install Python from the Windows App Store. Users from a data science
    background might want to use `Anaconda
    <https://docs.anaconda.com/anaconda/install/>`__ or `Miniconda
    <https://docs.conda.io/en/latest/miniconda.html>`__.

    It doesn't matter *how* you've installed Python - it only matters that you
    can run `python3` from your operating system's command prompt/terminal
    application, and get a working Python interpreter.

.. _install-dependencies:

Install dependencies
====================

Next, install the additional dependencies needed for your operating system:

.. tabs::

  .. group-tab:: macOS

    Building BeeWare apps on macOS requires:

    * **Git**, a version control system. You can download Git from from
      `git-scm.org <https://git-scm.com/download/>`__.

    * **Xcode**, Apple's IDE tooling. Xcode is available for free
      from `the macOS App Store
      <https://apps.apple.com/au/app/xcode/id497799835?mt=12>`__.

  .. group-tab:: Linux

    Building BeeWare apps on Linux requires some system packages. The list
    of packages required varies depending on your distribution:

    **Ubuntu 16.04, Debian 9**

    .. code-block:: bash

      $ sudo apt-get update
      $ sudo apt-get install git python3-dev python3-venv libgirepository1.0-dev libcairo2-dev libpango1.0-dev libwebkitgtk-3.0-0 gir1.2-webkit-3.0

    **Ubuntu 18.04, Debian 10**

    .. code-block:: bash

      $ sudo apt-get update
      $ sudo apt-get install git python3-dev python3-venv libgirepository1.0-dev libcairo2-dev libpango1.0-dev libwebkit2gtk-4.0-37 gir1.2-webkit2-4.0

    **Fedora**

    .. code-block:: bash

      $ sudo dnf install git pkg-config python3-devel gobject-introspection-devel cairo-devel cairo-gobject-devel pango-devel webkitgtk3

  .. group-tab:: Windows

    Building BeeWare apps on Windows requires:

    * **Git**, a version control system. You can download Git from from
      `git-scm.org <https://git-scm.com/download/>`__.

    * **WiX Toolset**, a set of utilities for building Windows installers. An
      installer can be obtained from `the WiX Toolset website
      <https://wixtoolset.org/releases/>`__.


Set up a virtual environment
============================

We're now going to create a virtual environment - a "sandbox" that we can use
to isolate our work on this tutorial from our main Python installation. If we
install packages into the virtual environment, our main Python installation
(and any other Python projects on our computer) won't be affected. If we make
a complete mess of our virtual environment, we'll be able to simply delete it
and start again, without affecting any other Python project on our computer,
and without the need to re-install Python.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      $ mkdir beeware-tutorial
      $ cd beeware-tutorial
      $ python3 -m venv beeware-venv
      $ source beeware-venv/bin/activate

  .. group-tab:: Linux

    .. code-block:: bash

      $ mkdir beeware-tutorial
      $ cd beeware-tutorial
      $ python3 -m venv beeware-venv
      $ source beeware-venv/bin/activate

  .. group-tab:: Windows

    .. code-block:: doscon

      C:\...>md beeware-tutorial
      C:\...>cd beeware-tutorial
      C:\...>py -m venv beeware-venv
      C:\...>beeware-venv\Scripts\activate.bat

If this worked, your prompt should now be changed - it should have a
``(beeware-venv)`` prefix. This lets you know that you're currently in your
BeeWare virtual environment. Whenever you're working on this tutorial, you
should make sure your virtual environment is activated. If it isn't, re-run the
last command (the ``activate`` command) to re-activate your environment.

.. admonition:: Alternative virtual environments

    If you're using Anaconda or miniconda, you may be more familiar with using
    conda environments. You might also have heard of ``virtualenv``, a
    predecessor to Python's built in ``venv`` module. As with Python installs -
    it doesn't matter *how* you create your virtual environment, as long as you
    have one.

    Even then - strictly speaking, using a virtual environment is optional. You
    *can* install BeeWare's tools directly into your main Python environment.
    However, it's really, *really*, **really** recommended that you use a
    virtual environment.

Next steps
==========

We've now set up our environment. We're ready to :doc:`create our first BeeWare
application <tutorial-1>`.
